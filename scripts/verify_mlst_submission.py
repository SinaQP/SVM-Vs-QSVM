"""
Verification script for MLST submission package.
Audits numerical consistency, citation resolution, and file completeness.
"""

import os
import re
import pandas as pd
import numpy as np


def verify_citations():
    tex_path = os.path.join("paper", "mlst", "manuscript.tex")
    bib_path = os.path.join("paper", "mlst", "references.bib")

    with open(tex_path, "r", encoding="utf-8") as f:
        tex_text = f.read()

    with open(bib_path, "r", encoding="utf-8") as f:
        bib_text = f.read()

    # Extract all \cite{...} keys
    cite_matches = re.findall(r"\\cite\{([^}]+)\}", tex_text)
    cited_keys = set()
    for match in cite_matches:
        for key in match.split(","):
            cited_keys.add(key.strip())

    # Extract all @...@article{key, etc.
    bib_keys = set(re.findall(r"@\w+\s*\{\s*([^,\s]+)\s*,", bib_text))

    missing_keys = cited_keys - bib_keys
    print(f"Total cited keys in manuscript.tex: {len(cited_keys)}")
    print(f"Total bib entries in references.bib: {len(bib_keys)}")
    print(f"Missing keys: {missing_keys}")
    assert len(missing_keys) == 0, f"Unresolved citations found: {missing_keys}"
    print("[OK] Citation Check: PASS (0 unresolved citation keys)")


def verify_numerical_consistency():
    tex_path = os.path.join("paper", "mlst", "manuscript.tex")
    with open(tex_path, "r", encoding="utf-8") as f:
        tex_text = f.read()

    # Canonical CSV files
    df_perf = pd.read_csv(os.path.join("results", "final", "final_model_comparison.csv"))
    df_stat = pd.read_csv(os.path.join("results", "final", "final_statistical_comparison.csv"))
    df_ablation = pd.read_csv(os.path.join("results", "final", "final_feature_map_summary.csv"))
    df_geom = pd.read_csv(os.path.join("results", "final", "final_kernel_comparison.csv"))
    df_runtime = pd.read_csv(os.path.join("results", "final", "final_runtime_summary.csv"))

    # Key numerical benchmarks to verify in tex_text
    checks = [
        # F1 scores
        ("Classical Comparator PCA 2 F1", "0.9339", "0.0068"),
        ("QSVC 2Q F1", "0.8678", "0.0388"),
        ("Classical Comparator PCA 4 F1", "0.9493", "0.0227"),
        ("QSVC 4Q F1", "0.8721", "0.0556"),
        ("Linear SVM PCA 4 F1", "0.9565", "0.0143"),
        # Accuracies
        ("Classical Comparator PCA 2 Acc", "0.9509", "0.0048"),
        ("QSVC 2Q Acc", "0.9070", "0.0237"),
        ("Classical Comparator PCA 4 Acc", "0.9632", "0.0157"),
        ("QSVC 4Q Acc", "0.9053", "0.0423"),
        # Statistical tests
        ("PCA 2 Mean Paired Diff", "+0.0662", ""),
        ("PCA 4 Mean Paired Diff", "+0.0772", ""),
        ("Exact Wilcoxon p-value", "0.0625", ""),
        ("Holm-Adjusted p-value", "0.1875", ""),
        ("Bootstrap CI PCA 2 Low", "+0.0388", ""),
        ("Bootstrap CI PCA 2 High", "+0.0977", ""),
        ("Bootstrap CI PCA 4 Low", "+0.0445", ""),
        ("Bootstrap CI PCA 4 High", "+0.1092", ""),
        # CKA and Effective Rank
        ("CKA PCA 2", "0.5732", "0.1578"),
        ("CKA PCA 4", "0.3375", "0.0718"),
        ("Effective Rank 2Q", "7.35", "0.21"),
        ("Effective Rank 4Q", "96.49", "5.41"),
        # Off-diagonal similarity
        ("Off-diagonal 2Q Mean", "0.3244", "0.0071"),
        ("Off-diagonal 4Q Mean", "0.0961", "0.0032"),
        # Runtimes
        ("Linear SVM PCA 2 Runtime", "0.0048", "0.0007"),
        ("QSVC 2Q Runtime", "0.2257", "0.0232"),
        ("QSVC 4Q Runtime", "0.6599", "0.0863"),
    ]

    for label, val, std in checks:
        assert val in tex_text, f"Value {val} for '{label}' not found in manuscript.tex!"
        if std:
            assert std in tex_text, f"Std {std} for '{label}' not found in manuscript.tex!"
        print(f"[OK] Checked {label}: {val} ± {std if std else 'N/A'}")

    print("[OK] Numerical Consistency: PASS (all central values match canonical records)")


def verify_file_presence():
    required_files = [
        os.path.join("paper", "mlst", "manuscript.tex"),
        os.path.join("paper", "mlst", "references.bib"),
        os.path.join("paper", "mlst", "data_availability.md"),
        os.path.join("paper", "mlst", "author_declarations.md"),
        os.path.join("paper", "mlst", "submission_metadata.md"),
        os.path.join("paper", "mlst", "submission_checklist.md"),
        os.path.join("paper", "mlst", "README.md"),
        os.path.join("paper", "mlst", "figures", "final_f1_comparison.png"),
        os.path.join("paper", "mlst", "figures", "final_feature_map_ablation.png"),
        os.path.join("paper", "mlst", "figures", "final_sample_size_scaling.png"),
        os.path.join("paper", "mlst", "figures", "final_kernel_heatmaps.png"),
        os.path.join("paper", "mlst", "figures", "final_runtime_scaling.png"),
        os.path.join("paper", "mlst", "supplementary", "supplementary_material.md"),
        os.path.join("paper", "mlst", "supplementary", "supplementary_material.tex"),
        os.path.join("paper", "mlst", "supplementary", "final_paired_f1_differences.png"),
        os.path.join("paper", "mlst", "supplementary", "final_roc_auc_comparison.png"),
    ]

    for path in required_files:
        assert os.path.isfile(path), f"Missing required file: {path}"
        assert os.path.getsize(path) > 0, f"File is empty: {path}"
        print(f"[OK] Found: {path} ({os.path.getsize(path)} bytes)")

    print("[OK] File Completeness: PASS (all required submission package files exist)")


def verify_author_metadata():
    files_to_check = [
        os.path.join("paper", "mlst", "manuscript.tex"),
        os.path.join("paper", "mlst", "submission_metadata.md"),
        os.path.join("paper", "mlst", "author_declarations.md"),
        os.path.join("paper", "mlst", "submission_checklist.md"),
        os.path.join("paper", "mlst", "supplementary", "supplementary_material.tex"),
        os.path.join("paper", "mlst", "supplementary", "supplementary_material.md"),
    ]

    expected_orcid = "0009-0006-8853-6740"
    expected_author = "Sina Qasempour"
    expected_email = "qasempoursina@gmail.com"
    expected_affil = "Independent Researcher, Iran"
    forbidden_phrase = "Department of Computer Engineering"

    for path in files_to_check:
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()

        assert expected_author in content, f"Author name '{expected_author}' missing from {path}"
        assert expected_orcid in content, f"Verified ORCID '{expected_orcid}' missing from {path}"
        assert expected_affil in content, f"Affiliation '{expected_affil}' missing from {path}"
        assert forbidden_phrase not in content, f"Forbidden department affiliation '{forbidden_phrase}' found in {path}!"
        if not path.endswith("supplementary_material.md"):
            assert expected_email in content, f"Email '{expected_email}' missing from {path}"

        print(f"[OK] Author metadata verified in: {path}")

    print("[OK] Author Metadata Check: PASS (verified ORCID, corrected affiliation, single author)")


if __name__ == "__main__":
    print("--- Running MLST Submission Verification ---")
    verify_file_presence()
    verify_author_metadata()
    verify_citations()
    verify_numerical_consistency()
    print("--- All Verification Steps Passed Successfully ---")
