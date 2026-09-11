"""Run only the corrected fully nested QSVC evaluation."""

from pathlib import Path
import argparse
import sys

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import corrected_nested


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", default="results/corrected_nested")
    args = parser.parse_args()
    result = corrected_nested.run_all(args.output_dir)
    print(result["summary"].to_string(index=False))


if __name__ == "__main__":
    main()

