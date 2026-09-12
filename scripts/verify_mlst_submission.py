"""
Verification script for MLST submission package.
Audits numerical consistency, citation resolution, and file completeness.
"""

import os
import re
import pandas as pd
import numpy as np


OBSOLETE_RUNTIME_PATTERNS = (
    r"\b47\s*(?:--|-|–|—|\\textendash)\s*80\s*(?:times|[×x])\b",
    r"\b(?:47|80)\s+times\b",
)
FALSE_MONOTONIC_SAMPLE_PATTERNS = (
    r"\bsteadily improved\b",
    r"\bmonotonically improved\b",
    r"\bconsistently improved with sample size\b",
)


def authoritative_runtime_ratios(
    qsvc_summary: pd.DataFrame, runtime_summary: pd.DataFrame
) -> tuple[float, float]:
    """Return corrected mean QSVC/Linear-SVM runtime ratios for PCA 2 and 4."""
    ratios = []
    for pca in (2, 4):
        qsvc_row = qsvc_summary.loc[qsvc_summary["pca_components"] == pca]
        linear_row = runtime_summary.loc[
            runtime_summary["Stage / Architecture"]
            == f"Linear SVM PCA {pca} (CPU fit+predict)"
        ]
        assert len(qsvc_row) == len(linear_row) == 1, (
            f"Expected one corrected QSVC and one Linear SVM timing row for PCA {pca}"
        )
        ratios.append(
            float(qsvc_row.iloc[0]["runtime_mean"])
            / float(linear_row.iloc[0]["Runtime_Mean_s"])
        )
    return tuple(ratios)


def verify_runtime_ratio_language(
    text: str, qsvc_summary: pd.DataFrame, runtime_summary: pd.DataFrame
) -> tuple[float, float]:
    """Reject the audited stale ratio and require prose derived from stored timings."""
    ratios = authoritative_runtime_ratios(qsvc_summary, runtime_summary)
    for pattern in OBSOLETE_RUNTIME_PATTERNS:
        assert not re.search(pattern, text, flags=re.IGNORECASE), (
            "Obsolete canonical QSVC runtime-ratio wording found"
        )

    rounded = tuple(round(value) for value in ratios)
    expected = re.compile(
        rf"approximately\s+{rounded[0]}\s+and\s+{rounded[1]}\s+times\b"
        rf".*?\b2Q\b.*?\b4Q\b.*?respectively",
        flags=re.IGNORECASE | re.DOTALL,
    )
    assert expected.search(text), (
        "Canonical runtime prose does not report the rounded authoritative ratios "
        f"{rounded[0]} and {rounded[1]} times for 2Q and 4Q, respectively"
    )
    return ratios


def verify_sample_size_language(text: str, sample_summary: pd.DataFrame) -> list[float]:
    """Reject monotonic 2Q claims when the stored learning curve has a decline."""
    two_qubit = sample_summary.loc[
        (sample_summary["model_family"] == "Quantum")
        & (sample_summary["pca_components"] == 2)
    ].sort_values("train_size")
    assert two_qubit["train_size"].tolist() == [50, 100, 200, 300, 455]
    sequence = two_qubit["f1_mean"].astype(float).tolist()
    assert np.any(np.diff(sequence) < 0), (
        "Stored 2Q sample-size sequence is monotonic; update this focused check"
    )

    for pattern in FALSE_MONOTONIC_SAMPLE_PATTERNS:
        assert not re.search(pattern, text, flags=re.IGNORECASE), (
            "False monotonic QSVC sample-size wording found"
        )
    assert re.search(r"\b2Q\b.*?\bpeak(?:ed|s)?\b", text, re.IGNORECASE | re.DOTALL)
    assert re.search(r"\bdeclin(?:e|ed|es|ing)\b", text, re.IGNORECASE)
    assert re.search(r"N\s*=\s*300", text) and re.search(r"N\s*=\s*455", text)
    return sequence


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

    # Extract bibliographic entries while excluding BibTeX comments.
    bib_keys = set(
        re.findall(r"@(?!comment\b)\w+\s*\{\s*([^,\s]+)\s*,", bib_text, re.IGNORECASE)
    )

    missing_keys = cited_keys - bib_keys
    unused_keys = bib_keys - cited_keys
    print(f"Total cited keys in manuscript.tex: {len(cited_keys)}")
    print(f"Total bib entries in references.bib: {len(bib_keys)}")
    print(f"Missing keys: {missing_keys}")
    print(f"Unused keys: {unused_keys}")
    assert len(missing_keys) == 0, f"Unresolved citations found: {missing_keys}"
    assert len(unused_keys) == 0, f"Unused bibliography entries found: {unused_keys}"
    print("[OK] Citation Check: PASS (0 unresolved and 0 unused citation keys)")


def verify_numerical_consistency():
    tex_path = os.path.join("paper", "mlst", "manuscript.tex")
    with open(tex_path, "r", encoding="utf-8") as f:
        tex_text = f.read()
    supplementary_tex_path = os.path.join(
        "paper", "mlst", "supplementary", "supplementary_material.tex"
    )
    with open(supplementary_tex_path, "r", encoding="utf-8") as f:
        submission_text = tex_text + "\n" + f.read()

    # Historical sources remain authoritative for classical, ablation, geometry,
    # and historical runtime results. Corrected nested outputs are authoritative
    # for final QSVC metrics, corrected-run timings, and paired comparisons.
    df_perf = pd.read_csv(os.path.join("results", "final", "final_model_comparison.csv"))
    df_ablation = pd.read_csv(os.path.join("results", "final", "final_feature_map_summary.csv"))
    df_geom = pd.read_csv(os.path.join("results", "final", "final_kernel_comparison.csv"))
    df_runtime = pd.read_csv(os.path.join("results", "final", "final_runtime_summary.csv"))
    df_sample = pd.read_csv(os.path.join("results", "final", "final_sample_size_summary.csv"))
    corrected_dir = os.path.join("results", "corrected_nested")
    df_qsvc = pd.read_csv(os.path.join(corrected_dir, "qsvc_outer_test_results.csv"))
    df_qsvc_summary = pd.read_csv(os.path.join(corrected_dir, "qsvc_outer_test_summary.csv"))
    df_stat = pd.read_csv(os.path.join(corrected_dir, "corrected_statistical_comparison.csv"))
    df_selected = pd.read_csv(os.path.join(corrected_dir, "qsvc_selected_configurations.csv"))

    assert len(df_qsvc) == 10 and set(df_qsvc["pca_components"]) == {2, 4}
    assert set(df_qsvc["selection_status"]) == {"FROZEN_BEFORE_OUTER_EVALUATION"}
    assert len(df_selected) == 10

    for pca in (2, 4):
        row = df_qsvc_summary.loc[df_qsvc_summary["pca_components"] == pca].iloc[0]
        for metric in ("accuracy", "precision", "recall", "f1", "roc_auc"):
            mean_token = f'{row[f"{metric}_mean"]:.4f}'
            sd_token = f'{row[f"{metric}_sd"]:.4f}'
            assert mean_token in submission_text, (
                f"Corrected QSVC PCA {pca} {metric} mean {mean_token} is stale/missing"
            )
            assert sd_token in submission_text, (
                f"Corrected QSVC PCA {pca} {metric} SD {sd_token} is stale/missing"
            )

    for _, row in df_stat.iloc[:2].iterrows():
        tokens = (
            f'{row["mean_paired_f1_difference"]:+.4f}',
            f'{row["median_paired_f1_difference"]:+.4f}',
            f'{row["p_raw"]:.4f}',
            f'{row["p_holm"]:.4f}',
            f'{row["bootstrap_ci_low"]:+.4f}',
            f'{row["bootstrap_ci_high"]:+.4f}',
        )
        for token in tokens:
            assert token in submission_text, (
                f"Corrected paired-statistic token {token} is stale/missing for {row['comparison']}"
            )

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
        ("CKA PCA 2", "0.5732", "0.1548"),
        ("CKA PCA 4", "0.3375", "0.0704"),
        ("Effective Rank 2Q", "7.35", "0.21"),
        ("Effective Rank 4Q", "96.49", "5.41"),
        # Off-diagonal similarity
        ("Off-diagonal 2Q Mean", "0.3244", "0.0071"),
        ("Off-diagonal 4Q Mean", "0.0961", "0.0032"),
        # Runtimes
        ("Linear SVM PCA 2 Runtime", "0.0048", "0.0007"),
        ("QSVC 2Q Runtime", "0.2181", "0.0096"),
        ("QSVC 4Q Runtime", "0.5846", "0.0257"),
    ]

    for label, val, std in checks:
        assert val in submission_text, (
            f"Value {val} for '{label}' not found in manuscript or supplement!"
        )
        if std:
            assert std in submission_text, (
                f"Std {std} for '{label}' not found in manuscript or supplement!"
            )
        print(f"[OK] Checked {label}: {val} ± {std if std else 'N/A'}")

    print("[OK] Numerical Consistency: PASS (final QSVC/statistics match corrected_nested)")

    for source_path in (
        os.path.join("paper", "mlst", "manuscript.tex"),
        os.path.join("paper", "manuscript.md"),
    ):
        with open(source_path, "r", encoding="utf-8") as f:
            source_text = f.read()
        ratios = verify_runtime_ratio_language(source_text, df_qsvc_summary, df_runtime)
        sequence = verify_sample_size_language(source_text, df_sample)
        print(
            f"[OK] Reporting consistency in {source_path}: "
            f"runtime ratios={ratios[0]:.6f}, {ratios[1]:.6f}; "
            f"2Q F1 sequence={[round(value, 6) for value in sequence]}"
        )
    print("[OK] Reporting Consistency: PASS (runtime and sample-size prose match artifacts)")


def verify_methodological_language():
    files = [
        os.path.join("paper", "mlst", "manuscript.tex"),
        os.path.join("paper", "mlst", "cover_letter.md"),
        os.path.join("paper", "mlst", "supplementary", "supplementary_material.tex"),
    ]
    text = "\n".join(open(path, encoding="utf-8").read() for path in files)
    stale_phrases = [
        "leakage-free",
        "architecture selection reused those splits",
        "Based on controlled architectural ablation",
        "Full (Canonical)",
        "independent confirmation",
    ]
    for phrase in stale_phrases:
        assert phrase.lower() not in text.lower(), f"Stale methodological wording: {phrase}"
    required = [
        "Authoritative Nested QSVC Selection",
        "jointly searches",
        "Study-level adaptivity",
        "exploratory sensitivity analysis",
    ]
    for phrase in required:
        assert phrase.lower() in text.lower(), f"Required corrected wording missing: {phrase}"
    print("[OK] Methodological Language: PASS")


def verify_file_presence():
    required_files = [
        os.path.join("paper", "mlst", "manuscript.tex"),
        os.path.join("paper", "mlst", "manuscript.pdf"),
        os.path.join("paper", "mlst", "references.bib"),
        os.path.join("paper", "mlst", "cover_letter.md"),
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
        os.path.join("paper", "mlst", "supplementary", "supplementary_material.pdf"),
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
    verify_methodological_language()
    print("--- All Verification Steps Passed Successfully ---")
