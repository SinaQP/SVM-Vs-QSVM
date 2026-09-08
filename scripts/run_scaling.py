"""Run sample-size scaling across N in [50, 100, 200, 300, 455]."""

import argparse
from pathlib import Path
from time import perf_counter
import numpy as np
import pandas as pd

from svm_vs_qsvm.classical import make_classical_model
from svm_vs_qsvm.data import generate_nested_stratified_subsets, get_outer_split, load_wdbc
from svm_vs_qsvm.kernels import exact_statevector_gram
from svm_vs_qsvm.metrics import score_predictions
from svm_vs_qsvm.preprocessing import fit_preprocessing, transform
from svm_vs_qsvm.quantum import build_qsvc, generate_statevectors
from svm_vs_qsvm.utils import DEFAULT_SEEDS, load_config, model_name, save_csv


def parse_args():
    parser = argparse.ArgumentParser(description="Run sample-size scaling benchmark.")
    parser.add_argument("--config", type=str, default="configs/phase10_scaling.yaml", help="Path to config.")
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
    train_sizes = config.get("train_sizes", [50, 100, 200, 300, 455])
    dims = config.get("pca_components", [2, 4])
    records = []

    for seed in args.seeds:
        for dim in dims:
            x_train_raw, x_test_raw, y_train_full, y_test, _, _ = get_outer_split(data, seed=seed)
            subsets = generate_nested_stratified_subsets(y_train_full, train_sizes, seed=seed)

            for N in train_sizes:
                sub_idx = subsets[N]
                x_sub_raw = x_train_raw[sub_idx]
                y_sub = y_train_full[sub_idx]

                # 1. Classical Linear SVM
                x_train_c, prep_c = fit_preprocessing(x_sub_raw, dim=dim, quantum=False)
                x_test_c = transform(x_test_raw, prep_c)
                lin = make_classical_model("linear", c=1.0, seed=seed)
                t0 = perf_counter()
                lin.fit(x_train_c, y_sub)
                m_lin = score_predictions(y_test, lin.predict(x_test_c), lin.decision_function(x_test_c))
                records.append({
                    "seed": seed, "train_size": N, "pca_components": dim,
                    "model": f"Linear SVM — PCA {dim}", "model_family": "classical_linear",
                    "total_runtime": perf_counter() - t0, **m_lin,
                })

                # 2. Quantum QSVC (reps=1, full)
                x_train_q, prep_q = fit_preprocessing(x_sub_raw, dim=dim, quantum=True)
                x_test_q = transform(x_test_raw, prep_q)
                t0_q = perf_counter()
                train_states = generate_statevectors(x_train_q, dim=dim, reps=1, entanglement="full")
                test_states = generate_statevectors(x_test_q, dim=dim, reps=1, entanglement="full")
                k_train = exact_statevector_gram(train_states, train_states, training=True)
                k_test = exact_statevector_gram(test_states, train_states, training=False)
                qsvc = build_qsvc(c=1.0, seed=seed)
                qsvc.fit(k_train, y_sub)
                m_q = score_predictions(y_test, qsvc.predict(k_test), qsvc.decision_function(k_test))
                records.append({
                    "seed": seed, "train_size": N, "pca_components": dim,
                    "model": f"QSVC — PCA {dim} / {dim}Q (reps=1, full)", "model_family": "quantum_qsvc",
                    "total_runtime": perf_counter() - t0_q, **m_q,
                })
                print(f"Seed {seed} | N={N} PCA={dim} -> Lin F1={m_lin['f1']:.4f}, QSVC F1={m_q['f1']:.4f}")

    df = pd.DataFrame(records)
    save_csv(df, out_dir, "sample_size_scaling_reproduced.csv")
    print(f"Saved {len(df)} scaling runs to {out_dir / 'sample_size_scaling_reproduced.csv'}")


if __name__ == "__main__":
    main()
