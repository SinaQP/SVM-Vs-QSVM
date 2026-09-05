"""Nested tuning and paired split-level analysis for the main research notebook."""

from itertools import product
from pathlib import Path
from time import perf_counter
import hashlib
import importlib.metadata
import json
import platform

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.stats import PermutationMethod, wilcoxon
from sklearn.datasets import load_breast_cancer
from sklearn.decomposition import PCA
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score, roc_auc_score
from sklearn.model_selection import StratifiedKFold, train_test_split
from sklearn.preprocessing import MinMaxScaler, StandardScaler
from sklearn.svm import SVC
from qiskit.circuit.library import zz_feature_map
from qiskit.quantum_info import Statevector
from qiskit_machine_learning.algorithms import QSVC

SEEDS = [42, 123, 456, 789, 2026]
C_VALUES = [0.01, 0.1, 1.0, 10.0, 100.0]
GAMMA_VALUES = ["scale", "auto", 0.01, 0.1, 1.0]
TIE_ATOL = 1e-12
BOOTSTRAP_SEED = 42
N_BOOTSTRAP = 10000
METRICS = ["accuracy", "precision", "recall", "f1", "roc_auc"]
PRIMARY_COMPARISONS = ["Classical PCA2 vs QSVC PCA2", "Classical PCA4 vs QSVC PCA4", "QSVC PCA2 vs QSVC PCA4"]


def model_name(kernel, dim):
    if kernel == "quantum":
        return f"QSVC — PCA {dim} / {dim}Q (reps=1, full)"
    return f"{'Linear' if kernel == 'linear' else 'RBF'} SVM — PCA {dim}"


def candidates(kernel):
    gammas = GAMMA_VALUES if kernel == "rbf" else ["none"]
    return [{"C": c, "gamma": str(g)} for c, g in product(C_VALUES, gammas)]


def make_model(kernel, c, gamma, seed):
    if kernel == "quantum":
        return QSVC(quantum_kernel="precomputed", C=c, random_state=seed)
    gamma = gamma if gamma in ("scale", "auto") else (float(gamma) if gamma != "none" else "scale")
    return SVC(kernel=kernel, C=c, gamma=gamma, random_state=seed)


def score_predictions(y, predictions, scores):
    """All models have classes [0, 1]; negate SVC's class-1 score for malignant AUC."""
    return {
        "accuracy": float(accuracy_score(y, predictions)),
        "precision": float(precision_score(y, predictions, pos_label=0, zero_division=0)),
        "recall": float(recall_score(y, predictions, pos_label=0, zero_division=0)),
        "f1": float(f1_score(y, predictions, pos_label=0, zero_division=0)),
        "roc_auc": float(roc_auc_score(np.asarray(y) == 0, -np.asarray(scores))),
    }


def fit_preprocessing(x_train, dim, quantum):
    """Only training data can enter this fitting API; evaluation uses transform()."""
    scaler = StandardScaler()
    train_std = scaler.fit_transform(x_train)
    # Preserve the previous PCA convention and sklearn's deterministic auto solver.
    pca = PCA(n_components=dim)
    train_pca = pca.fit_transform(train_std)
    q_scaler = MinMaxScaler(feature_range=(0, np.pi), clip=True) if quantum else None
    train = q_scaler.fit_transform(train_pca) if quantum else train_pca
    assert int(scaler.n_samples_seen_) == pca.n_samples_ == len(x_train)
    if quantum:
        assert q_scaler.n_samples_seen_ == len(x_train)
    return train, (scaler, pca, q_scaler)


def transform(x, preprocessing):
    scaler, pca, q_scaler = preprocessing
    values = pca.transform(scaler.transform(x))
    return q_scaler.transform(values) if q_scaler is not None else values


def statevectors(x, dim):
    feature_map = zz_feature_map(feature_dimension=dim, reps=1, entanglement="full")
    return np.asarray([Statevector(feature_map.assign_parameters(row)).data for row in x])


def gram(states_left, states_train, training=False):
    matrix = np.abs(states_left @ states_train.conj().T) ** 2
    if training:
        np.fill_diagonal(matrix, 1.0)
    assert np.isfinite(matrix).all()
    assert matrix.min() >= -1e-10 and matrix.max() <= 1 + 1e-10
    return matrix


def kernel_diagnostics(matrix):
    assert np.allclose(matrix, matrix.T, atol=1e-10, rtol=0)
    eigenvalues = np.linalg.eigvalsh((matrix + matrix.T) / 2)
    assert eigenvalues.min() >= -1e-10
    positive = np.clip(eigenvalues, 0, None)
    probabilities = positive[positive > 0] / positive.sum()
    return {
        "kernel_condition_number": float(np.linalg.cond(matrix)),
        "effective_rank": float(np.exp(-np.sum(probabilities * np.log(probabilities)))),
        "kernel_minimum_eigenvalue": float(eigenvalues.min()),
    }


def select_candidate(candidate_summary):
    """Absolute F1 tie <=1e-12, then C, then scale/auto/numeric gamma order."""
    best = candidate_summary["inner_cv_f1_mean"].max()
    tied = candidate_summary.loc[np.isclose(candidate_summary.inner_cv_f1_mean, best, atol=TIE_ATOL, rtol=0)].copy()
    gamma_order = {str(g): i for i, g in enumerate(["none"] + GAMMA_VALUES)}
    tied["gamma_order"] = tied.gamma.map(gamma_order)
    return tied.sort_values(["C", "gamma_order"], kind="stable").iloc[0].drop("gamma_order").to_dict()


def summarize_candidates(raw):
    return raw.groupby(["seed", "model", "kernel", "pca_components", "C", "gamma"], sort=False).agg(
        inner_cv_f1_mean=("inner_f1", "mean"), inner_cv_f1_std=("inner_f1", "std"),
        inner_cv_accuracy_mean=("inner_accuracy", "mean"), inner_cv_accuracy_std=("inner_accuracy", "std"),
        inner_cv_roc_auc_mean=("inner_roc_auc", "mean"), inner_cv_roc_auc_std=("inner_roc_auc", "std"),
        n_folds=("inner_fold", "nunique"),
    ).reset_index()


def choose_classical(selected):
    """Choose Linear/RBF per seed by inner F1 only; tie: smaller C, then Linear."""
    chosen = []
    for (seed, dim), group in selected[selected.kernel != "quantum"].groupby(["seed", "pca_components"]):
        maximum = group.inner_cv_f1_mean.max()
        tied = group[np.isclose(group.inner_cv_f1_mean, maximum, atol=TIE_ATOL, rtol=0)].copy()
        tied["family_order"] = (tied.kernel != "linear").astype(int)
        row = tied.sort_values(["selected_C", "family_order"], kind="stable").iloc[0]
        chosen.append({"seed": seed, "pca_components": dim, "model": row.model,
                       "selected_C": row.selected_C, "selected_gamma": row.selected_gamma,
                       "inner_cv_f1_mean": row.inner_cv_f1_mean})
    return pd.DataFrame(chosen)


def inner_search(x_train, y_train, seed, dim, kernel):
    """No outer-test data, labels, predictions, or metrics are accepted here."""
    rows = []
    start = perf_counter()
    folds = StratifiedKFold(n_splits=5, shuffle=True, random_state=seed)
    for fold, (fit_idx, val_idx) in enumerate(folds.split(x_train, y_train), start=1):
        assert not np.intersect1d(fit_idx, val_idx).size
        train, preprocessing = fit_preprocessing(x_train[fit_idx], dim, kernel == "quantum")
        validation = transform(x_train[val_idx], preprocessing)
        if kernel == "quantum":
            train_states = statevectors(train, dim)
            validation_states = statevectors(validation, dim)
            train = gram(train_states, train_states, training=True)
            validation = gram(validation_states, train_states)
        # Only C varies for quantum models, so reuse these fold-local matrices across C.
        # Nothing fitted or cached here survives into another fold or outer seed.
        for candidate in candidates(kernel):
            model = make_model(kernel, candidate["C"], candidate["gamma"], seed)
            model.fit(train, y_train[fit_idx])
            assert np.array_equal(model.classes_, [0, 1]) and model.fit_status_ == 0
            scores = score_predictions(y_train[val_idx], model.predict(validation), model.decision_function(validation))
            rows.append({"seed": seed, "model": model_name(kernel, dim), "kernel": kernel,
                         "pca_components": dim, **candidate, "inner_fold": fold,
                         "n_inner_train": len(fit_idx), "n_inner_validation": len(val_idx),
                         **{f"inner_{k}": v for k, v in scores.items()}})
    raw = pd.DataFrame(rows)
    selected = select_candidate(summarize_candidates(raw))
    selected["selected_C"] = selected.pop("C")
    selected["selected_gamma"] = selected.pop("gamma")
    selected["search_runtime"] = perf_counter() - start
    return raw, selected


def split_indices(y, seed):
    return train_test_split(np.arange(len(y)), test_size=0.20, random_state=seed, stratify=y)


def save_csv(frame, directory, name):
    frame.to_csv(Path(directory) / name, index=False)


def tune_all(directory="results"):
    """Part 1: freeze ALL choices before any Phase 11 outer-test evaluation."""
    directory = Path(directory)
    directory.mkdir(exist_ok=True, parents=True)
    data = load_breast_cancer()
    raw_parts, selections, status, split_manifest = [], [], [], []
    for seed in SEEDS:
        train_idx, test_idx = split_indices(data.target, seed)
        folds = StratifiedKFold(n_splits=5, shuffle=True, random_state=seed)
        inner = [{"inner_fold": i, "train_ids": train_idx[a].tolist(), "validation_ids": train_idx[b].tolist()}
                 for i, (a, b) in enumerate(folds.split(data.data[train_idx], data.target[train_idx]), 1)]
        split_manifest.append({"seed": seed, "outer_train_ids": train_idx.tolist(), "outer_test_ids": test_idx.tolist(), "inner_folds": inner})
        for dim, kernel in product([2, 4], ["linear", "rbf", "quantum"]):
            record = {"stage": "inner_search", "seed": seed, "model": model_name(kernel, dim), "status": "SUCCESS", "error": ""}
            try:
                raw, selected = inner_search(data.data[train_idx], data.target[train_idx], seed, dim, kernel)
                raw_parts.append(raw)
                selections.append(selected)
            except Exception as error:
                record.update(status="FAILED", error=repr(error))
                raise
            finally:
                status.append(record)
                save_csv(pd.DataFrame(status), directory, "phase11_execution_status.csv")
            all_raw = pd.concat(raw_parts, ignore_index=True)
            save_csv(all_raw[all_raw.kernel != "quantum"], directory, "classical_hyperparameter_search_raw.csv")
            save_csv(all_raw[all_raw.kernel == "quantum"], directory, "quantum_hyperparameter_search_raw.csv")
            save_csv(pd.DataFrame(selections), directory, "selected_hyperparameters.csv")
        print(f"Inner CV complete: seed {seed}, 350 candidate/fold scores; no outer evaluation yet.", flush=True)
    selected = pd.DataFrame(selections)
    comparators = choose_classical(selected)
    save_csv(comparators, directory, "selected_classical_comparators.csv")
    save_csv(summarize_candidates(pd.concat(raw_parts)), directory, "hyperparameter_candidate_summary.csv")
    manifest = {
        "seeds": SEEDS, "C_values": C_VALUES, "gamma_values": GAMMA_VALUES,
        "tie_atol": TIE_ATOL, "bootstrap_seed": BOOTSTRAP_SEED, "n_bootstrap": N_BOOTSTRAP,
        "primary_comparisons": PRIMARY_COMPARISONS, "primary_metric": "malignant_f1",
        "quantum_feature_map": {"type": "ZZ", "reps": 1, "entanglement": "full", "range": [0, float(np.pi)], "clip": True},
        "python": platform.python_version(),
        "packages": {p: importlib.metadata.version(p) for p in ["numpy", "pandas", "scikit-learn", "scipy", "qiskit", "qiskit-machine-learning", "matplotlib"]},
        "dataset_sha256": hashlib.sha256(data.data.tobytes() + data.target.tobytes()).hexdigest(),
        "implementation_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "selection_sha256": hashlib.sha256((directory / "selected_hyperparameters.csv").read_bytes()).hexdigest(),
        "comparison_selection": "Per-seed inner-CV F1; ties: smaller C, then Linear. No outer-test ranking selects comparators.",
        "limitations": "Five overlapping splits; maps selected in Phase 9 on these same splits. Inference and bootstrap are exploratory.",
        "splits": split_manifest,
    }
    (directory / "phase11_manifest.json").write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    return selected, comparators


def evaluate_outer(x_train, y_train, x_test, y_test, selection):
    seed, dim, kernel = int(selection["seed"]), int(selection["pca_components"]), selection["kernel"]
    start = perf_counter()
    train, preprocessing = fit_preprocessing(x_train, dim, kernel == "quantum")
    preprocessing_fit_time = perf_counter() - start
    sv_train_time = train_matrix_time = sv_test_time = test_matrix_time = 0.0
    if kernel == "quantum":
        start = perf_counter()
        train_states = statevectors(train, dim)
        sv_train_time = perf_counter() - start
        start = perf_counter()
        train = gram(train_states, train_states, training=True)
        train_matrix_time = perf_counter() - start
    model = make_model(kernel, selection["selected_C"], selection["selected_gamma"], seed)
    start = perf_counter()
    model.fit(train, y_train)
    fit_time = perf_counter() - start
    assert np.array_equal(model.classes_, [0, 1]) and model.fit_status_ == 0
    # The selected model has now been fitted, before even transforming outer-test features.
    start = perf_counter()
    test = transform(x_test, preprocessing)
    preprocessing_prediction_time = perf_counter() - start
    if kernel == "quantum":
        start = perf_counter()
        test_states = statevectors(test, dim)
        sv_test_time = perf_counter() - start
        start = perf_counter()
        test = gram(test_states, train_states)
        test_matrix_time = perf_counter() - start
    start = perf_counter()
    predictions, scores = model.predict(test), model.decision_function(test)
    prediction_time = perf_counter() - start
    measured = score_predictions(y_test, predictions, scores)
    sv_time, matrix_time = sv_train_time + sv_test_time, train_matrix_time + test_matrix_time
    preprocessing_time = preprocessing_fit_time + preprocessing_prediction_time
    row = {**selection, **{f"outer_{k}": v for k, v in measured.items()},
           "fit_time": fit_time, "prediction_time": prediction_time, "preprocessing_time": preprocessing_time,
           "statevector_generation_time": sv_time, "kernel_matrix_time": matrix_time,
           "kernel_total_time": sv_time + matrix_time,
           "total_runtime": preprocessing_time + fit_time + prediction_time + sv_time + matrix_time,
           "runtime_kind": "exact_statevector_simulation_CPU" if kernel == "quantum" else "classical_CPU",
           "n_outer_train": len(y_train), "n_outer_test": len(y_test)}
    start = perf_counter()
    row.update(kernel_diagnostics(train) if kernel == "quantum" else {"kernel_condition_number": np.nan, "effective_rank": np.nan, "kernel_minimum_eigenvalue": np.nan})
    row["diagnostic_time"] = perf_counter() - start if kernel == "quantum" else 0.0
    return row, predictions, scores


def evaluate_all(selected, directory="results"):
    """Part 2: one final outer-test prediction set per selected model and seed."""
    directory = Path(directory)
    frozen = json.loads((directory / "phase11_manifest.json").read_text(encoding="utf-8"))
    assert frozen["selection_sha256"] == hashlib.sha256((directory / "selected_hyperparameters.csv").read_bytes()).hexdigest()
    pd.testing.assert_frame_equal(selected.reset_index(drop=True), pd.read_csv(directory / "selected_hyperparameters.csv", keep_default_na=False), check_dtype=False, atol=1e-14)
    data = load_breast_cancer()
    rows, predictions = [], []
    status = pd.read_csv(directory / "phase11_execution_status.csv").to_dict("records")
    for selection in selected.to_dict("records"):
        seed = int(selection["seed"])
        train_idx, test_idx = split_indices(data.target, seed)
        record = {"stage": "outer_evaluation", "seed": seed, "model": selection["model"], "status": "SUCCESS", "error": ""}
        try:
            row, pred, scores = evaluate_outer(data.data[train_idx], data.target[train_idx], data.data[test_idx], data.target[test_idx], selection)
            rows.append(row)
            predictions.extend({"seed": seed, "model": selection["model"], "sample_id": int(idx),
                                "y_true": int(label), "y_pred": int(p), "malignant_score": float(-s)}
                               for idx, label, p, s in zip(test_idx, data.target[test_idx], pred, scores))
        except Exception as error:
            record.update(status="FAILED", error=repr(error))
            raise
        finally:
            status.append(record)
            save_csv(pd.DataFrame(status), directory, "phase11_execution_status.csv")
        save_csv(pd.DataFrame(rows), directory, "tuned_outer_test_results.csv")
        save_csv(pd.DataFrame(predictions), directory, "tuned_outer_test_predictions.csv")
        print(f"Outer evaluation complete: seed {seed}, {selection['model']}", flush=True)
    outer = pd.DataFrame(rows)
    summary = outer.groupby(["model", "kernel", "pca_components"], sort=False)[[f"outer_{m}" for m in METRICS] + ["total_runtime"]].agg(["mean", "std"])
    summary.columns = [f"{a.removeprefix('outer_')}_{b}" for a, b in summary.columns]
    summary = summary.reset_index()
    save_csv(summary, directory, "tuned_outer_test_summary.csv")
    return outer, summary


def holm_adjust(p_values):
    """Step-down Holm; retain untestable hypotheses in the predefined family."""
    values = np.asarray(p_values, dtype=float)
    finite = np.isfinite(values)
    working = np.where(finite, values, 1.0)
    order = np.argsort(working, kind="stable")
    adjusted = np.empty(len(values))
    adjusted[order] = np.minimum(1, np.maximum.accumulate(working[order] * np.arange(len(values), 0, -1)))
    adjusted[~finite] = np.nan
    return adjusted


def bootstrap_interval(differences):
    """Percentile interval over five split-level differences, not patient samples."""
    differences = np.asarray(differences)
    rng = np.random.default_rng(BOOTSTRAP_SEED)
    means = differences[rng.integers(0, len(differences), size=(N_BOOTSTRAP, len(differences)))].mean(axis=1)
    return tuple(np.quantile(means, [0.025, 0.975]))


def signed_rank(differences):
    # Avoid ranking floating subtraction noise as distinct values (SciPy guidance).
    differences = np.round(np.asarray(differences), 12)
    if np.any(differences == 0):
        return np.nan, np.nan, "not_run_zero_differences", "Zero differences: conventional exact Wilcoxon is not valid; no forced approximation."
    if len(np.unique(np.abs(differences))) < len(differences):
        method = PermutationMethod(n_resamples=np.inf)
        label = "exhaustive_sign_permutation_with_ties"
    else:
        method, label = "exact", "exact"
    result = wilcoxon(differences, alternative="two-sided", zero_method="wilcox", method=method)
    return float(result.statistic), float(result.pvalue), label, "Exploratory: five overlapping splits do not establish independent observations."


def pair_results(outer, comparators):
    pairs = []
    chosen = comparators.merge(outer, on=["seed", "pca_components", "model"], validate="one_to_one", suffixes=("_choice", ""))
    for comparison in PRIMARY_COMPARISONS:
        if comparison.startswith("Classical"):
            dim = 2 if "PCA2" in comparison else 4
            left = chosen[chosen.pca_components == dim]
            right = outer[(outer.kernel == "quantum") & (outer.pca_components == dim)]
        else:
            left = outer[(outer.kernel == "quantum") & (outer.pca_components == 2)]
            right = outer[(outer.kernel == "quantum") & (outer.pca_components == 4)]
        assert not left.seed.duplicated().any() and not right.seed.duplicated().any()
        assert set(left.seed) == set(right.seed) == set(SEEDS)
        aligned = left.merge(right, on="seed", suffixes=("_left", "_right"), validate="one_to_one").set_index("seed").loc[SEEDS]
        for metric in ["f1", "accuracy", "roc_auc"]:
            for seed, row in aligned.iterrows():
                a, b = row[f"outer_{metric}_left"], row[f"outer_{metric}_right"]
                pairs.append({"comparison": comparison, "metric": metric, "seed": seed,
                              "model_left": row.model_left, "model_right": row.model_right,
                              "value_left": a, "value_right": b, "difference": a - b})
    return pd.DataFrame(pairs)


def analyze(outer, comparators, directory="results"):
    directory = Path(directory)
    pairs = pair_results(outer, comparators)
    save_csv(pairs, directory, "paired_outer_test_differences.csv")
    descriptions, tests = [], []
    for (comparison, metric), group in pairs.groupby(["comparison", "metric"], sort=False):
        differences = group.set_index("seed").loc[SEEDS, "difference"].to_numpy()
        effect = {"comparison": comparison, "metric": metric, "n_pairs": len(differences),
                  "mean_paired_difference": differences.mean(), "median_paired_difference": np.median(differences),
                  "std_paired_difference": differences.std(ddof=1), "min_paired_difference": differences.min(),
                  "max_paired_difference": differences.max(), "left_wins": int(np.sum(differences > TIE_ATOL)),
                  "right_wins": int(np.sum(differences < -TIE_ATOL)), "ties": int(np.sum(np.abs(differences) <= TIE_ATOL))}
        if metric == "f1":
            lower, upper = bootstrap_interval(differences)
            statistic, p_value, method, note = signed_rank(differences)
            effect.update(bootstrap_ci_low=lower, bootstrap_ci_high=upper,
                          bootstrap_seed=BOOTSTRAP_SEED, n_bootstrap=N_BOOTSTRAP,
                          interval_scope="percentile bootstrap over the five observed split-level differences")
            tests.append({**effect, "wilcoxon_statistic": statistic, "p_raw": p_value,
                          "method": method, "note": note, "family": "three_predefined_F1_comparisons"})
        descriptions.append(effect)
    statistics = pd.DataFrame(tests).set_index("comparison").loc[PRIMARY_COMPARISONS].reset_index()
    statistics["p_holm"] = holm_adjust(statistics.p_raw)
    effects = pd.DataFrame(descriptions)
    save_csv(statistics, directory, "statistical_tests.csv")
    save_csv(effects, directory, "paired_effect_summary.csv")
    # Full-size Phase 10 uses C=1 and the same reps=1/full maps. Phase 8 QSVC used reps=2.
    historical_path = directory / "sample_size_scaling_raw.csv"
    historical = pd.read_csv(historical_path)
    baseline = historical[historical.train_size == 455].copy()
    assert len(baseline) == 30 and set(baseline.model) == set(outer.model)
    assert not baseline.duplicated(["seed", "model"]).any()
    assert baseline.groupby("model").seed.apply(lambda values: set(values) == set(SEEDS)).all()
    baseline["baseline_C"] = 1.0
    baseline["baseline_gamma"] = np.where(baseline.model.str.startswith("RBF"), "scale", "none")
    save_csv(baseline, directory, "phase11_untuned_baseline.csv")
    historical_means = baseline.groupby("model")[["accuracy", "f1", "roc_auc"]].mean().add_prefix("untuned_")
    tuned_means = outer.groupby("model")[["outer_accuracy", "outer_f1", "outer_roc_auc"]].mean()
    tuned_means.columns = ["tuned_accuracy", "tuned_f1", "tuned_roc_auc"]
    comparison = historical_means.join(tuned_means, validate="one_to_one")
    for metric in ["accuracy", "f1", "roc_auc"]:
        comparison[f"delta_{metric}"] = comparison[f"tuned_{metric}"] - comparison[f"untuned_{metric}"]
    comparison["untuned_f1_rank"] = comparison.untuned_f1.rank(ascending=False, method="min").astype(int)
    comparison["tuned_f1_rank"] = comparison.tuned_f1.rank(ascending=False, method="min").astype(int)
    comparison["baseline_source"] = "sample_size_scaling_raw.csv; train_size=455; C=1; QSVC reps=1/full"
    comparison = comparison.reset_index()
    save_csv(comparison, directory, "tuned_vs_untuned_comparison.csv")
    return pairs, effects, statistics, comparison


def plot_results(summary, pairs, comparison, directory="results"):
    directory = Path(directory)
    plt.rcParams.update({"font.size": 10, "axes.spines.top": False, "axes.spines.right": False})
    names = [model_name(kernel, dim) for dim, kernel in product([2, 4], ["linear", "rbf", "quantum"])]
    labels = [f"{kernel.title() if kernel != 'quantum' else 'QSVC'}\nPCA {dim}" for dim, kernel in product([2, 4], ["linear", "rbf", "quantum"])]
    colors = ["#305F8D", "#527D9D", "#B26338"] * 2
    ordered = summary.set_index("model").loc[names]
    fig, ax = plt.subplots(figsize=(9, 4.7), layout="constrained")
    for i, (_, row) in enumerate(ordered.iterrows()):
        ax.errorbar(i, row.f1_mean, yerr=row.f1_std, fmt="o", capsize=5, color=colors[i], markersize=8)
        ax.annotate(f"{row.f1_mean:.3f}", (i, row.f1_mean + row.f1_std), xytext=(0, 7), textcoords="offset points", ha="center")
    ax.set(xticks=range(6), xticklabels=labels, ylabel="Malignant-class F1", ylim=(0.75, 1.015), title="Tuned models · mean ± sample SD over five outer splits")
    ax.grid(axis="y", alpha=0.2)
    fig.savefig(directory / "tuned_f1_mean_std.png", dpi=180)
    plt.show()
    plt.close(fig)

    f1_pairs = pairs[(pairs.metric == "f1") & pairs.comparison.str.startswith("Classical")]
    fig, axes = plt.subplots(1, 2, figsize=(10, 4.7), sharey=True, layout="constrained")
    seed_colors = plt.get_cmap("tab10")(np.arange(5))
    for ax, comparison_name in zip(axes, PRIMARY_COMPARISONS[:2]):
        group = f1_pairs[f1_pairs.comparison == comparison_name].set_index("seed").loc[SEEDS]
        for color, (seed, row) in zip(seed_colors, group.iterrows()):
            ax.plot([0, 1], [row.value_left, row.value_right], "o-", color=color, alpha=0.85, label=str(seed))
        ax.set(xticks=[0, 1], xticklabels=["Inner-selected\nclassical", "Tuned QSVC"], title=comparison_name, xlim=(-0.2, 1.2))
        ax.grid(axis="y", alpha=0.2)
    axes[0].set_ylabel("Malignant-class F1")
    axes[1].legend(title="Outer seed", loc="lower left", fontsize=8)
    fig.savefig(directory / "paired_f1_by_seed.png", dpi=180)
    plt.show()
    plt.close(fig)

    fig, axes = plt.subplots(1, 2, figsize=(10, 4.3), sharey=True, layout="constrained")
    for ax, comparison_name in zip(axes, PRIMARY_COMPARISONS[:2]):
        group = f1_pairs[f1_pairs.comparison == comparison_name].set_index("seed").loc[SEEDS]
        ax.axhline(0, color="#333333", linewidth=1)
        ax.vlines(range(5), 0, group.difference, color=seed_colors, alpha=0.8)
        ax.scatter(range(5), group.difference, c=seed_colors, s=45, zorder=3)
        ax.set(xticks=range(5), xticklabels=SEEDS, xlabel="Outer seed", title=comparison_name)
        ax.grid(axis="y", alpha=0.2)
    axes[0].set_ylabel("F1 classical − F1 quantum")
    fig.savefig(directory / "paired_f1_differences.png", dpi=180)
    plt.show()
    plt.close(fig)

    ordered_comparison = comparison.set_index("model").loc[names]
    fig, axes = plt.subplots(1, 3, figsize=(13, 5.2), sharey=True, layout="constrained")
    short_labels = [name.replace("\n", " · ") for name in labels]
    for ax, metric, title in zip(axes, ["accuracy", "f1", "roc_auc"], ["Accuracy", "Malignant F1", "ROC-AUC"]):
        for i, (_, row) in enumerate(ordered_comparison.iterrows()):
            ax.plot([row[f"untuned_{metric}"], row[f"tuned_{metric}"]], [i, i], color="#ADB6BE", linewidth=2)
        ax.scatter(ordered_comparison[f"untuned_{metric}"], range(6), color="#87929C", marker="s", label="C=1 baseline")
        ax.scatter(ordered_comparison[f"tuned_{metric}"], range(6), color=colors, marker="o", label="Nested tuned")
        ax.set(title=title, yticks=range(6), yticklabels=short_labels, xlabel="Outer-test mean")
        ax.grid(axis="x", alpha=0.2)
    axes[0].invert_yaxis()
    axes[-1].legend(loc="lower left", fontsize=8)
    fig.suptitle("Tuned versus untuned · descriptive comparison of the same five outer splits")
    fig.savefig(directory / "tuned_vs_untuned.png", dpi=180)
    plt.show()
    plt.close(fig)


def validate_results(directory="results"):
    """Audit saved artifacts without repeating outer-test model evaluation."""
    directory = Path(directory)
    raw = pd.concat([pd.read_csv(directory / f"{family}_hyperparameter_search_raw.csv", keep_default_na=False)
                     for family in ["classical", "quantum"]], ignore_index=True)
    selected = pd.read_csv(directory / "selected_hyperparameters.csv", keep_default_na=False)
    outer = pd.read_csv(directory / "tuned_outer_test_results.csv", keep_default_na=False)
    comparisons = pd.read_csv(directory / "selected_classical_comparators.csv", keep_default_na=False)
    predictions = pd.read_csv(directory / "tuned_outer_test_predictions.csv")
    manifest = json.loads((directory / "phase11_manifest.json").read_text(encoding="utf-8"))
    assert len(raw[raw.kernel != "quantum"]) == 1500 and len(raw[raw.kernel == "quantum"]) == 250
    assert not raw.duplicated(["seed", "model", "C", "gamma", "inner_fold"]).any()
    for (seed, dim, kernel), group in raw.groupby(["seed", "pca_components", "kernel"]):
        expected = {(c["C"], c["gamma"], fold) for c in candidates(kernel) for fold in range(1, 6)}
        assert set(zip(group.C, group.gamma, group.inner_fold)) == expected
        repeated = select_candidate(summarize_candidates(group))
        original = selected[(selected.seed == seed) & (selected.pca_components == dim) & (selected.kernel == kernel)].iloc[0]
        assert repeated["C"] == original.selected_C and repeated["gamma"] == original.selected_gamma
    regenerated = choose_classical(selected)
    pd.testing.assert_frame_equal(regenerated, comparisons, check_dtype=False, atol=1e-14)
    assert len(selected) == len(outer) == 30 and not outer.duplicated(["seed", "model"]).any()
    assert outer.groupby("model").seed.apply(lambda values: set(values) == set(SEEDS)).all()
    assert len(predictions) == 30 * 114
    assert not predictions.duplicated(["seed", "model", "sample_id"]).any()
    y = load_breast_cancer().target
    for split in manifest["splits"]:
        train, test = set(split["outer_train_ids"]), set(split["outer_test_ids"])
        expected_train, expected_test = split_indices(y, split["seed"])
        assert train == set(expected_train) and test == set(expected_test)
        assert not train & test and len(train) == 455 and len(test) == 114
        seen_validation = []
        for fold in split["inner_folds"]:
            fitting, validation = set(fold["train_ids"]), set(fold["validation_ids"])
            assert not fitting & validation and fitting | validation == train
            assert not (fitting | validation) & test
            seen_validation.extend(validation)
        assert len(seen_validation) == len(set(seen_validation)) == 455
        for _, group in predictions[predictions.seed == split["seed"]].groupby("model"):
            assert set(group.sample_id) == test
            assert np.array_equal(group.y_true, y[group.sample_id.to_numpy()])
    for row in outer.to_dict("records"):
        pred = predictions[(predictions.seed == row["seed"]) & (predictions.model == row["model"])]
        recovered = score_predictions(pred.y_true, pred.y_pred, -pred.malignant_score)
        for metric in METRICS:
            assert np.isclose(recovered[metric], row[f"outer_{metric}"], atol=1e-14, rtol=0)
    pairs = pair_results(outer, comparisons)
    tests = pd.read_csv(directory / "statistical_tests.csv")
    assert tests.comparison.tolist() == PRIMARY_COMPARISONS
    np.testing.assert_allclose(tests.p_holm, holm_adjust(tests.p_raw), atol=1e-14)
    np.testing.assert_allclose(holm_adjust([0.01, 0.04, 0.03]), [0.03, 0.06, 0.06])
    for row in tests.to_dict("records"):
        difference = pairs[(pairs.metric == "f1") & (pairs.comparison == row["comparison"])].difference
        first = bootstrap_interval(difference)
        assert first == bootstrap_interval(difference)
        np.testing.assert_allclose(first, [row["bootstrap_ci_low"], row["bootstrap_ci_high"]], atol=1e-14)
    status = pd.read_csv(directory / "phase11_execution_status.csv")
    assert len(status) == 60 and status.status.eq("SUCCESS").all()
    result = {"status": "PASS", "inner_candidate_fold_rows": len(raw), "selected_configurations": len(selected),
              "outer_evaluations": len(outer), "saved_predictions": len(predictions), "paired_difference_rows": len(pairs),
              "primary_F1_tests": len(tests), "failed_runs": int(status.status.ne("SUCCESS").sum()),
              "checks": ["complete candidate grids", "selection reproduced from raw fold scores", "classical choices reproduced",
                         "outer/inner split disjointness", "identical paired seeds", "saved predictions reproduce metrics",
                         "Holm reference case", "deterministic bootstrap"]}
    (directory / "phase11_validation.json").write_text(json.dumps(result, indent=2), encoding="utf-8")
    return result


def markdown_table(frame):
    """Small tables without an optional formatting dependency."""
    def fmt(value):
        if isinstance(value, (float, np.floating)):
            return f"{value:.4f}" if np.isfinite(value) else "not run"
        return str(value).replace("|", "/")
    rows = ["| " + " | ".join(map(str, frame.columns)) + " |", "| " + " | ".join(["---"] * len(frame.columns)) + " |"]
    rows.extend("| " + " | ".join(fmt(value) for value in row) + " |" for row in frame.itertuples(index=False, name=None))
    return "\n".join(rows)


def research_report(selected, summary, comparisons, tests, tuning_comparison, validation, directory="results"):
    """Generate interpretation from the executed tables rather than hardcoded scores."""
    selected_table = selected[["model", "seed", "selected_C", "selected_gamma"]]
    scores = pd.DataFrame({"Model": summary.model})
    for metric in ["accuracy", "f1", "roc_auc"]:
        scores[metric] = [f"{mean:.4f} ± {std:.4f}" for mean, std in zip(summary[f"{metric}_mean"], summary[f"{metric}_std"])]
    ranking_before = tuning_comparison.sort_values("untuned_f1", ascending=False).model.tolist()
    ranking_after = tuning_comparison.sort_values("tuned_f1", ascending=False).model.tolist()
    family_notes = []
    for dim in [2, 4]:
        classical_names = [model_name(kernel, dim) for kernel in ["linear", "rbf"]]
        lookup = tuning_comparison.set_index("model")
        q = model_name("quantum", dim)
        before_gap = lookup.loc[classical_names, "untuned_f1"].max() - lookup.loc[q, "untuned_f1"]
        after_gap = lookup.loc[classical_names, "tuned_f1"].max() - lookup.loc[q, "tuned_f1"]
        family_notes.append(f"PCA {dim}: the largest classical mean F1 minus quantum mean F1 was {before_gap:+.4f} before tuning and {after_gap:+.4f} after tuning. This ranking description does not select the inferential comparator.")
    lines = [
        "## Phase 11 — Executed research report", "",
        "Implemented nested tuning for four classical and two fixed-map quantum configurations; all candidate/fold scores, predictions, selected configurations, diagnostics, and paired statistics are persisted.", "",
        "**Nested-CV design.** Five fixed stratified 80/20 outer splits; five shuffled stratified inner folds per seed. All scalers and PCA are fitted inside each fold. Malignant label 0 is positive. All choices are frozen before Phase 11 outer evaluation. The classical comparison is an inner-selected Linear/RBF procedure per seed, so it can choose different kernels across seeds.", "",
        "**Selected hyperparameters by model/seed**", "", markdown_table(selected_table), "",
        "**Classical comparators selected using inner CV**", "", markdown_table(comparisons), "",
        "**Tuned outer-test results: mean ± sample SD**", "", markdown_table(scores), "",
        "**Did tuning change the ranking?** " + ("The ordering of individual models changed." if ranking_before != ranking_after else "The ordering of individual models did not change."), "",
        *family_notes, "",
        "**Tuned versus C=1: outer-test means only**", "",
        markdown_table(tuning_comparison[["model", "delta_accuracy", "delta_f1", "delta_roc_auc", "untuned_f1_rank", "tuned_f1_rank"]]), "",
        "**Paired F1 effects** (left minus right; classical minus quantum, or 2Q minus 4Q)", "",
        markdown_table(tests[["comparison", "mean_paired_difference", "median_paired_difference", "std_paired_difference", "min_paired_difference", "max_paired_difference"]]), "",
        "**Wilcoxon, Holm correction, bootstrap intervals, and wins**", "",
        markdown_table(tests[["comparison", "wilcoxon_statistic", "p_raw", "p_holm", "bootstrap_ci_low", "bootstrap_ci_high", "left_wins", "right_wins", "ties"]]), "",
    ]
    for row in tests.to_dict("records"):
        lines.append(f"- {row['comparison']}: {row['method']}; {row['note']}")
    lines.extend([
        "", "**Statistical-power limitation.** There are only five paired split-level observations. With five nonzero pairs, the smallest conventional two-sided exact Wilcoxon p-value is 0.0625, even when every difference has the same sign. Holm covers the three predefined F1 comparisons. Accuracy and ROC-AUC are descriptive secondary outcomes. A nonsignificant p-value is not evidence of equivalence.", "",
        "The 95% pointwise percentile bootstrap intervals resample the five observed split-level differences (10,000 resamples, seed 42). They are exploratory intervals over these splits, not precise population intervals or simultaneous multiplicity-adjusted intervals. The splits reuse patients and training observations, so their differences are dependent; neither ordinary Wilcoxon assumptions nor independent-observation bootstrap coverage are established. A bootstrap interval excluding zero and a nonsignificant exact test need not agree with this very small sample.", "",
        "**Research interpretation.** These comparisons concern this dataset, preprocessing, fixed feature maps, and exact simulator only. Earlier feature-map selection used the same five test splits; nested hyperparameter tuning does not erase that prior selection bias. Phase 11 avoids new test-driven selection but is not independent confirmation. No universal claim about classical superiority or quantum advantage follows.", "",
        "**Computational fairness.** `fit_time` and `prediction_time` measure the classifier only; `total_runtime` also includes preprocessing and, for QSVC, statevector generation plus Gram products. `search_runtime` records inner tuning separately, and `diagnostic_time` records kernel diagnostics separately. These phase-local costs separate classical CPU SVM computation from exact statevector simulation. Simulation time is not physical-device runtime; historical ComputeUncompute timings are not pooled. The RBF and QSVC candidate grids differ in size as specified, so this is not an equal-search-budget benchmark.", "",
        f"**Validation and failed runs.** {validation['status']}: {validation['inner_candidate_fold_rows']} candidate/fold rows, {validation['outer_evaluations']} final evaluations, {validation['saved_predictions']} saved predictions, and {validation['failed_runs']} failed Phase 11 model runs. The separate notebook execution log records full sequential execution.", "",
        "**Problems and next recommended step.** Limited power, overlapping splits, and prior feature-map selection constrain interpretation. Freeze this protocol before a future independent validation study; do not expand the present phase. Hardware, noise, new datasets/maps, trainable kernels, paper writing, and repository restructuring remain outside this phase.", "",
        "Methods: [scikit-learn nested CV](https://scikit-learn.org/stable/auto_examples/model_selection/plot_nested_cross_validation_iris.html), [SciPy Wilcoxon handling of ties and zeros](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.wilcoxon.html), [QSVC precomputed kernel API](https://qiskit-community.github.io/qiskit-machine-learning/stubs/qiskit_machine_learning.algorithms.QSVC.html).", "",
    ])
    report = "\n".join(lines)
    (Path(directory) / "phase11_report.md").write_text(report, encoding="utf-8")
    return report
