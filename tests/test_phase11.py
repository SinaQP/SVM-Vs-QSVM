"""Focused checks for leakage, score direction, selection, and small-sample logic."""
import numpy as np
import pandas as pd
import pytest
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import StratifiedKFold
import phase11 as p


def test_training_only_preprocessing_and_extreme_holdout():
    data = load_breast_cancer()
    train_ids, test_ids = p.split_indices(data.target, 42)
    train, fitted = p.fit_preprocessing(data.data[train_ids], 4, True)
    scaler, pca, quantum = fitted
    np.testing.assert_allclose(scaler.mean_, data.data[train_ids].mean(axis=0))
    state_before = [scaler.mean_.copy(), pca.components_.copy(), quantum.data_min_.copy(), quantum.data_max_.copy()]
    transformed = p.transform(data.data[test_ids] * 1e6, fitted)
    assert np.all((transformed >= 0) & (transformed <= np.pi + 1e-14))
    for before, after in zip(state_before, [scaler.mean_, pca.components_, quantum.data_min_, quantum.data_max_]):
        np.testing.assert_array_equal(before, after)
    assert train.shape == (455, 4)


@pytest.mark.parametrize("kernel", ["rbf", "quantum"])
def test_every_fold_refits_on_inner_training_only(monkeypatch, kernel):
    data = load_breast_cancer()
    train_ids, test_ids = p.split_indices(data.target, 42)
    x, y = data.data[train_ids], data.target[train_ids]
    expected_folds = list(StratifiedKFold(5, shuffle=True, random_state=42).split(x, y))
    preprocessing_calls, gram_calls = [], []
    original_fit, original_gram = p.fit_preprocessing, p.gram

    def observed_fit(values, dim, quantum):
        fold_idx = len(preprocessing_calls)
        expected_train, _ = expected_folds[fold_idx]
        np.testing.assert_array_equal(values, x[expected_train])
        result = original_fit(values, dim, quantum)
        preprocessing_calls.append(result[1])
        return result

    def observed_gram(left, train, training=False):
        result = original_gram(left, train, training)
        gram_calls.append((result.shape, training))
        return result

    monkeypatch.setattr(p, "fit_preprocessing", observed_fit)
    monkeypatch.setattr(p, "gram", observed_gram)
    raw, selected = p.inner_search(x, y, 42, 2, kernel)
    assert len(preprocessing_calls) == 5
    assert len({id(objects[0]) for objects in preprocessing_calls}) == 5
    assert len({id(objects[1]) for objects in preprocessing_calls}) == 5
    assert len(raw) == (125 if kernel == "rbf" else 25)
    if kernel == "quantum":
        assert len({id(objects[2]) for objects in preprocessing_calls}) == 5
        assert gram_calls == [item for _ in range(5) for item in [((364, 364), True), ((91, 364), False)]]
    assert selected["n_folds"] == 5


def test_exact_gram_matches_direct_statevector_fidelity():
    inputs = np.array([[0.1, 0.2], [0.7, 2.1], [2.3, 1.8]])
    states = p.statevectors(inputs, 2)
    expected = np.array([[abs(np.vdot(a, b)) ** 2 for b in states] for a in states])
    matrix = p.gram(states, states, training=True)
    np.testing.assert_allclose(matrix, expected, atol=1e-14)
    assert np.linalg.eigvalsh(matrix).min() > -1e-10


def test_malignant_f1_and_score_orientation():
    scores = p.score_predictions([0, 0, 1, 1], [0, 1, 1, 1], [-4, -1, 2, 3])
    assert scores["roc_auc"] == 1.0
    assert scores["f1"] == pytest.approx(2 / 3)
    assert scores["recall"] == 0.5


def test_numerical_ties_prefer_smaller_c_then_scale():
    table = pd.DataFrame({"C": [10, 0.1, 0.1, 0.01], "gamma": ["scale", "auto", "scale", "scale"],
                          "inner_cv_f1_mean": [0.9 + 5e-13, 0.9, 0.9, 0.89]})
    selected = p.select_candidate(table)
    assert selected["C"] == 0.1 and selected["gamma"] == "scale"


def test_holm_known_unsorted_example_and_untestable_hypothesis():
    np.testing.assert_allclose(p.holm_adjust([0.04, 0.01, 0.03]), [0.06, 0.03, 0.06])
    np.testing.assert_allclose(p.holm_adjust([0.01, np.nan, 0.04]), [0.03, np.nan, 0.08])


def test_wilcoxon_n5_exact_resolution_and_zeros():
    statistic, p_value, method, _ = p.signed_rank([1, 2, 3, 4, 5])
    assert statistic == 0 and p_value == 0.0625 and method == "exact"
    assert np.isnan(p.signed_rank([0, 1, 2, 3, 4])[1])
    assert p.signed_rank([1, 1, 2, 3, 4])[1] == 0.0625


def test_bootstrap_reproducibility_and_paired_unit():
    differences = np.array([-0.01, 0.02, 0.03, 0.04, 0.09])
    assert p.bootstrap_interval(differences) == p.bootstrap_interval(differences)
    assert p.bootstrap_interval(np.repeat(0.1, 5)) == (0.1, 0.1)
    lower, upper = p.bootstrap_interval(differences)
    assert differences.min() <= lower <= upper <= differences.max()


def test_pairing_aligns_seeds_and_rejects_missing_pairs():
    outer = pd.DataFrame([
        {"seed": seed, "pca_components": dim, "kernel": kernel, "model": p.model_name(kernel, dim),
         "outer_f1": 0.9 if kernel == "linear" else 0.8, "outer_accuracy": 0.9, "outer_roc_auc": 0.98}
        for seed in reversed(p.SEEDS) for dim in [2, 4] for kernel in ["linear", "quantum"]
    ])
    choices = outer[outer.kernel == "linear"][["seed", "model", "pca_components"]]
    pairs = p.pair_results(outer.sample(frac=1, random_state=1), choices)
    assert pairs.iloc[:5].seed.tolist() == p.SEEDS
    np.testing.assert_allclose(pairs.iloc[:5].difference, 0.1)
    with pytest.raises(AssertionError):
        p.pair_results(outer.iloc[:-1], choices)
