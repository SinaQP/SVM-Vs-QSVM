"""Run nested hyperparameter tuning and outer-test evaluation."""

import argparse
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import phase11


def parse_args():
    parser = argparse.ArgumentParser(description="Run nested CV hyperparameter tuning.")
    parser.add_argument("--output-dir", type=str, default="results/reproduced", help="Output directory.")
    return parser.parse_args()


def main():
    args = parse_args()
    out_dir = Path(args.output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    print(f"Starting nested tuning pipeline saving to {out_dir}...")
    manifest = phase11.run_all(directory=str(out_dir))
    print(f"Completed Phase 11 tuning run: manifest saved.")


if __name__ == "__main__":
    main()
