"""Build publication-quality figures, tables, and final report from existing results."""

import argparse
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import phase12


def parse_args():
    parser = argparse.ArgumentParser(description="Build canonical final figures and research synthesis.")
    parser.add_argument("--results-dir", type=str, default="results", help="Directory of source results.")
    return parser.parse_args()


def main():
    args = parse_args()
    print("Executing Phase 12 validation and synthesis...")
    val = phase12.validate_phase12()
    print(f"Validation status: {val['status']}")
    print(f"Audited source files: {val['total_source_files_audited']}")
    print(f"Tables generated: {val['tables_generated']}, Figures generated: {val['figures_generated']}")


if __name__ == "__main__":
    main()
