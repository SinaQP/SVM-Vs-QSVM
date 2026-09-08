"""Comprehensive repository and research artifact validation script."""

import json
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))


def validate_environment():
    print("[1/6] Checking Python environment and package imports...")
    import numpy
    import pandas
    import sklearn
    import scipy
    import qiskit
    import qiskit_machine_learning
    import matplotlib
    import yaml
    import svm_vs_qsvm
    print(f"  Python {sys.version.split()[0]}")
    print(f"  svm_vs_qsvm v{svm_vs_qsvm.__version__}")
    print(f"  qiskit v{qiskit.__version__}")
    print(f"  qiskit-machine-learning v{qiskit_machine_learning.__version__}")
    print("  Environment check: PASS")


def validate_configs():
    print("[2/6] Validating configuration files in configs/...")
    from svm_vs_qsvm.utils import load_config
    configs = ["base.yaml", "phase9_ablation.yaml", "phase10_scaling.yaml", "phase11_tuning.yaml"]
    for cfg in configs:
        p = ROOT / "configs" / cfg
        assert p.exists(), f"Missing config: {p}"
        data = load_config(p)
        assert isinstance(data, dict) and len(data) > 0, f"Empty or invalid config: {p}"
    print("  Configuration check: PASS")


def validate_notebook():
    print("[3/6] Checking notebook presence and structure...")
    nb_path = ROOT / "notebooks" / "svm_vs_qsvm_setup.ipynb"
    assert nb_path.exists(), f"Notebook missing at {nb_path}"
    assert nb_path.stat().st_size > 3_000_000, "Notebook size suspiciously small."
    print("  Notebook check: PASS")


def validate_frozen_artifacts():
    print("[4/6] Verifying integrity of frozen canonical results...")
    import phase12
    audit_df = phase12.audit_sources()
    assert len(audit_df) == 18, f"Expected 18 audited files, found {len(audit_df)}"
    assert (audit_df["size_bytes"] > 0).all(), "Found empty audited files"

    final_dir = ROOT / "results" / "final"
    expected_final_files = [
        "final_model_comparison.csv",
        "final_feature_map_summary.csv",
        "final_sample_size_summary.csv",
        "final_runtime_summary.csv",
        "final_statistical_comparison.csv",
        "final_kernel_comparison.csv",
        "final_f1_comparison.png",
        "final_roc_auc_comparison.png",
        "final_paired_f1_differences.png",
        "final_feature_map_ablation.png",
        "final_sample_size_scaling.png",
        "final_runtime_scaling.png",
        "final_kernel_heatmaps.png",
        "final_research_report.md",
        "final_validation.json",
    ]
    for fname in expected_final_files:
        fp = final_dir / fname
        assert fp.exists() and fp.stat().st_size > 0, f"Missing or empty canonical artifact: {fp}"
    print("  Frozen artifact check: PASS")


def validate_tests():
    print("[5/6] Running full test suite via pytest...")
    cmd = [sys.executable, "-m", "pytest", "-v"]
    result = subprocess.run(cmd, cwd=str(ROOT), capture_output=True, text=True)
    print(result.stdout)
    if result.returncode != 0:
        print(result.stderr, file=sys.stderr)
        raise RuntimeError("Pytest test suite failed!")
    print("  Test suite check: PASS")


def emit_validation_manifest():
    print("[6/6] Emitting repository validation manifest...")
    manifest = {
        "status": "PASS",
        "project": "Classical SVM vs Quantum Kernel SVM for Breast Cancer Classification",
        "phase": 13,
        "package": "svm_vs_qsvm",
        "python_version": sys.version.split()[0],
        "checks_passed": [
            "environment_and_imports",
            "centralized_configs",
            "notebook_relocation",
            "frozen_artifacts_integrity",
            "full_test_suite",
        ],
        "project_status": {
            "research_implementation": "COMPLETE",
            "experimental_study": "COMPLETE",
            "statistical_analysis": "COMPLETE",
            "final_synthesis": "COMPLETE",
            "repository_packaging": "COMPLETE",
            "physical_qpu_validation": "NOT PERFORMED",
            "independent_dataset_validation": "NOT PERFORMED",
            "paper_manuscript": "NOT PERFORMED",
        }
    }
    out_path = ROOT / "results" / "final" / "repository_validation.json"
    out_path.write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    print(f"Validation manifest saved to {out_path}")


def main():
    print("=== Repository Validation (Phase 13) ===")
    validate_environment()
    validate_configs()
    validate_notebook()
    validate_frozen_artifacts()
    validate_tests()
    emit_validation_manifest()
    print("=== All Repository Validation Checks Passed Successfully! ===")


if __name__ == "__main__":
    main()
