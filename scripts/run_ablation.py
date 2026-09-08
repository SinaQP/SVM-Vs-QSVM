"""Run quantum feature-map ablation across reps and entanglement topologies."""

import argparse
from pathlib import Path
from time import perf_counter
import numpy as np
import pandas as pd

from svm_vs_qsvm.data import get_outer_split, load_wdbc
from svm_vs_qsvm.kernels import compute_kernel_diagnostics, compute_offdiag_statistics, exact_statevector_gram
from svm_vs_qsvm.metrics import score_predictions
from svm_vs_qsvm.preprocessing import fit_preprocessing, transform
from svm_vs_qsvm.quantum import build_qsvc, generate_statevectors
from svm_vs_qsvm.utils import DEFAULT_SEEDS, load_config, save_csv


def parse_args():
    parser = argparse.ArgumentParser(description="Run quantum feature-map ablation.")
    parser.add_argument("--config", type=str, default="configs/phase9_ablation.yaml", help="Path to config.")
    parser.add_argument("--output-dir", type=str, default="results/reproduced", help="Output directory.")
    parser.add_argument("--seeds", type=int, nargs="+", default=DEFAULT_SEEDS, help="Outer seeds.")
    return parser.parse_args()


def main():
    args = parse_args()
    config = load_config(args.config)
    print(f"Loaded config from {args.config}")
    out_dir = Path(args.output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    data = load_wdbc()
    reps_list = config.get("reps_list", [1, 2, 3])
    entanglements = config.get("entanglement_list", ["linear", "full"])
    dims = config.get("pca_components", [2, 4])
    fixed_C = config.get("fixed_C", 1.0)
    records = []

    for seed in args.seeds:
        for dim in dims:
            x_train_raw, x_test_raw, y_train, y_test, _, _ = get_outer_split(data, seed=seed)
            x_train, prep = fit_preprocessing(x_train_raw, dim=dim, quantum=True)
            x_test = transform(x_test_raw, prep)

            for reps in reps_list:
                for ent in entanglements:
                    if dim == 2 and ent == "linear":
                        continue  # Linear and full entanglement are mathematically identical for 2 qubits

                    start = perf_counter()
                    train_states = generate_statevectors(x_train, dim=dim, reps=reps, entanglement=ent)
                    test_states = generate_statevectors(x_test, dim=dim, reps=reps, entanglement=ent)

                    k_train = exact_statevector_gram(train_states, train_states, training=True)
                    k_test = exact_statevector_gram(test_states, train_states, training=False)

                    diag = compute_kernel_diagnostics(k_train)
                    offdiag = compute_offdiag_statistics(k_train)

                    clf = build_qsvc(c=fixed_C, seed=seed)
                    fit_start = perf_counter()
                    clf.fit(k_train, y_train)
                    fit_time = perf_counter() - fit_start

                    pred_start = perf_counter()
                    preds = clf.predict(k_test)
                    scores = clf.decision_function(k_test)
                    pred_time = perf_counter() - pred_start
                    total_time = perf_counter() - start

                    m = score_predictions(y_test, preds, scores)
                    records.append({
                        "seed": seed,
                        "pca_components": dim,
                        "n_qubits": dim,
                        "reps": reps,
                        "entanglement": ent,
                        "total_runtime": total_time,
                        "fit_time": fit_time,
                        "prediction_time": pred_time,
                        **m,
                        **diag,
                        **offdiag,
                    })
                    print(f"Seed {seed} | {dim}Q reps={reps} {ent}: F1={m['f1']:.4f}, EffRank={diag['effective_rank']:.2f}")

    df = pd.DataFrame(records)
    save_csv(df, out_dir, "quantum_feature_map_ablation_reproduced.csv")
    print(f"Saved {len(df)} ablation runs to {out_dir / 'quantum_feature_map_ablation_reproduced.csv'}")


if __name__ == "__main__":
    main()
