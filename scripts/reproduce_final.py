"""One-command reproduction of modern benchmark pipeline without historical slow ComputeUncompute."""

import argparse
from pathlib import Path
from time import perf_counter
import numpy as np
import pandas as pd

from svm_vs_qsvm.classical import make_classical_model
from svm_vs_qsvm.data import get_outer_split, load_wdbc
from svm_vs_qsvm.kernels import exact_statevector_gram
from svm_vs_qsvm.metrics import score_predictions
from svm_vs_qsvm.preprocessing import fit_preprocessing, transform
from svm_vs_qsvm.quantum import build_qsvc, generate_statevectors
from svm_vs_qsvm.utils import DEFAULT_SEEDS, load_config, model_name, save_csv


def parse_args():
    parser = argparse.ArgumentParser(description="Reproduce modern fast pipeline.")
    parser.add_argument("--output-dir", type=str, default="results/reproduced", help="Output directory.")
    parser.add_argument("--seeds", type=int, nargs="+", default=DEFAULT_SEEDS, help="Seeds to evaluate.")
    return parser.parse_args()


def main():
    args = parse_args()
    out_dir = Path(args.output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    print(f"Executing lightweight reproduction pipeline -> {out_dir}")

    data = load_wdbc()
    records = []

    for seed in args.seeds:
        for dim in [2, 4]:
            x_train_raw, x_test_raw, y_train, y_test, _, _ = get_outer_split(data, seed=seed)

            # Classical Linear SVM
            x_train_c, prep_c = fit_preprocessing(x_train_raw, dim=dim, quantum=False)
            x_test_c = transform(x_test_raw, prep_c)
            t0 = perf_counter()
            lin = make_classical_model("linear", c=1.0, seed=seed)
            lin.fit(x_train_c, y_train)
            m_lin = score_predictions(y_test, lin.predict(x_test_c), lin.decision_function(x_test_c))
            records.append({
                "seed": seed, "pca_components": dim, "model": f"Linear SVM — PCA {dim}",
                "runtime": perf_counter() - t0, **m_lin
            })

            # Fast exact statevector QSVC (reps=1, full)
            x_train_q, prep_q = fit_preprocessing(x_train_raw, dim=dim, quantum=True)
            x_test_q = transform(x_test_raw, prep_q)
            t0_q = perf_counter()
            train_states = generate_statevectors(x_train_q, dim=dim, reps=1, entanglement="full")
            test_states = generate_statevectors(x_test_q, dim=dim, reps=1, entanglement="full")
            k_train = exact_statevector_gram(train_states, train_states, training=True)
            k_test = exact_statevector_gram(test_states, train_states, training=False)
            qsvc = build_qsvc(c=1.0, seed=seed)
            qsvc.fit(k_train, y_train)
            m_q = score_predictions(y_test, qsvc.predict(k_test), qsvc.decision_function(k_test))
            records.append({
                "seed": seed, "pca_components": dim, "model": f"QSVC — PCA {dim} / {dim}Q (reps=1, full)",
                "runtime": perf_counter() - t0_q, **m_q
            })

            print(f"Seed {seed} | PCA {dim}: Lin F1={m_lin['f1']:.4f}, QSVC F1={m_q['f1']:.4f}")

    df = pd.DataFrame(records)
    save_csv(df, out_dir, "reproduced_model_summary.csv")
    print(f"Reproduction complete. Results saved to {out_dir / 'reproduced_model_summary.csv'}")


if __name__ == "__main__":
    main()
