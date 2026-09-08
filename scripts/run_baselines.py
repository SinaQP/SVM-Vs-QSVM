"""Run classical SVM baseline models across seeds.

Outputs results to results/reproduced/ by default to protect canonical artifacts.
"""

import argparse
from pathlib import Path
from time import perf_counter
import numpy as np
import pandas as pd

from svm_vs_qsvm.classical import make_classical_model
from svm_vs_qsvm.data import get_outer_split, load_wdbc
from svm_vs_qsvm.metrics import score_predictions
from svm_vs_qsvm.preprocessing import fit_preprocessing, transform
from svm_vs_qsvm.utils import DEFAULT_SEEDS, load_config, model_name, save_csv


def parse_args():
    parser = argparse.ArgumentParser(description="Run classical SVM baselines.")
    parser.add_argument("--config", type=str, default="configs/base.yaml", help="Path to configuration file.")
    parser.add_argument("--output-dir", type=str, default="results/reproduced", help="Directory for output files.")
    parser.add_argument("--seeds", type=int, nargs="+", default=DEFAULT_SEEDS, help="Random seeds to evaluate.")
    return parser.parse_args()


def main():
    args = parse_args()
    config = load_config(args.config)
    print(f"Loaded config from {args.config}")
    out_dir = Path(args.output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    data = load_wdbc()
    records = []

    for seed in args.seeds:
        for dim in config.get("pca_components", [2, 4]):
            x_train_raw, x_test_raw, y_train, y_test, _, _ = get_outer_split(data, seed=seed)
            x_train, prep = fit_preprocessing(x_train_raw, dim=dim, quantum=False)
            x_test = transform(x_test_raw, prep)

            for kernel in ["linear", "rbf"]:
                start = perf_counter()
                model = make_classical_model(kernel=kernel, c=1.0, gamma="scale", seed=seed)
                fit_start = perf_counter()
                model.fit(x_train, y_train)
                fit_time = perf_counter() - fit_start

                pred_start = perf_counter()
                preds = model.predict(x_test)
                scores = model.decision_function(x_test)
                pred_time = perf_counter() - pred_start
                total_runtime = perf_counter() - start

                m = score_predictions(y_test, preds, scores)
                records.append({
                    "seed": seed,
                    "model": model_name(kernel, dim),
                    "kernel": kernel,
                    "pca_components": dim,
                    "n_features": dim,
                    "fit_time": fit_time,
                    "prediction_time": pred_time,
                    "total_runtime": total_runtime,
                    **m,
                })
                print(f"Seed {seed} | {model_name(kernel, dim)}: F1={m['f1']:.4f}, Accuracy={m['accuracy']:.4f}")

    df = pd.DataFrame(records)
    save_csv(df, out_dir, "classical_baselines_reproduced.csv")
    print(f"Saved {len(df)} runs to {out_dir / 'classical_baselines_reproduced.csv'}")


if __name__ == "__main__":
    main()
