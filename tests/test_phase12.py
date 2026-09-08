"""Focused unit and integration tests for Phase 12 Final Synthesis."""

import json
from pathlib import Path
import numpy as np
import pandas as pd
import pytest
import phase12

FINAL_DIR = Path("results/final")
RESULTS_DIR = Path("results")


def test_audit_all_sources_exist_and_non_empty():
    audit_df = phase12.audit_sources()
    assert len(audit_df) == 18
    assert (audit_df["size_bytes"] > 0).all()
    if "rows" in audit_df.columns:
        valid_rows = audit_df["rows"].dropna()
        assert (valid_rows > 0).all()


def test_final_model_comparison_integrity():
    df = pd.read_csv(FINAL_DIR / "final_model_comparison.csv")
    main_models = df[~df["Model"].str.contains("Supplementary")]
    assert len(main_models) == 4
    for col in ["Accuracy Mean", "Accuracy SD", "F1 Mean", "F1 SD", "ROC-AUC Mean", "ROC-AUC SD"]:
        assert np.isfinite(main_models[col]).all()
        assert (main_models[col] >= 0.0).all() and (main_models[col] <= 1.0).all()

    # Verify classical superiority on both PCA2 and PCA4
    c2 = main_models[(main_models["PCA Components"] == 2) & (main_models["Qubits"] == 0)].iloc[0]
    q2 = main_models[(main_models["PCA Components"] == 2) & (main_models["Qubits"] == 2)].iloc[0]
    assert c2["F1 Mean"] > q2["F1 Mean"]
    assert c2["Accuracy Mean"] > q2["Accuracy Mean"]

    c4 = main_models[(main_models["PCA Components"] == 4) & (main_models["Qubits"] == 0)].iloc[0]
    q4 = main_models[(main_models["PCA Components"] == 4) & (main_models["Qubits"] == 4)].iloc[0]
    assert c4["F1 Mean"] > q4["F1 Mean"]
    assert c4["Accuracy Mean"] > q4["Accuracy Mean"]


def test_cka_and_frobenius_alignment_properties():
    # Test on synthetic orthogonal and identical matrices
    K_id = np.eye(5)
    assert pytest.approx(phase12.cka(K_id, K_id)) == 1.0
    assert pytest.approx(phase12.frobenius_alignment(K_id, K_id)) == 1.0

    df_k = pd.read_csv(FINAL_DIR / "final_kernel_comparison.csv")
    assert len(df_k) == 10  # 5 seeds * 2 dims
    assert df_k["cka_alignment"].between(0.0, 1.0).all()
    assert df_k["frobenius_alignment"].between(0.0, 1.0).all()

    # PCA 2 CKA is higher than PCA 4 CKA
    cka_pca2_mean = df_k[df_k["pca_components"] == 2]["cka_alignment"].mean()
    cka_pca4_mean = df_k[df_k["pca_components"] == 4]["cka_alignment"].mean()
    assert cka_pca2_mean > cka_pca4_mean
    assert cka_pca2_mean > 0.50
    assert cka_pca4_mean < 0.40


def test_reproducibility_of_frozen_phase11_statistics():
    stat_df = pd.read_csv(FINAL_DIR / "final_statistical_comparison.csv")
    assert len(stat_df) == 3

    p2 = stat_df[stat_df["Comparison"] == "Classical PCA2 vs QSVC PCA2"].iloc[0]
    assert np.isclose(p2["Mean Paired Diff"], 0.066169, atol=1e-5)
    assert p2["Classical/Left Wins"] == 5
    assert p2["Quantum/Right Wins"] == 0
    assert np.isclose(p2["Raw p-value"], 0.0625, atol=1e-4)
    assert np.isclose(p2["Holm-Adjusted p-value"], 0.1875, atol=1e-4)

    p4 = stat_df[stat_df["Comparison"] == "Classical PCA4 vs QSVC PCA4"].iloc[0]
    assert np.isclose(p4["Mean Paired Diff"], 0.077191, atol=1e-5)
    assert p4["Classical/Left Wins"] == 5
    assert p4["Quantum/Right Wins"] == 0
    assert np.isclose(p4["Raw p-value"], 0.0625, atol=1e-4)
    assert np.isclose(p4["Holm-Adjusted p-value"], 0.1875, atol=1e-4)

    q_diff = stat_df[stat_df["Comparison"] == "QSVC PCA2 vs QSVC PCA4"].iloc[0]
    assert np.isclose(q_diff["Mean Paired Diff"], -0.004300, atol=1e-5)
    assert q_diff["Classical/Left Wins"] == 2
    assert q_diff["Quantum/Right Wins"] == 3
    assert np.isclose(q_diff["Raw p-value"], 0.8125, atol=1e-4)


def test_sample_size_scaling_reproduces_no_small_data_advantage():
    scaling = pd.read_csv(FINAL_DIR / "final_sample_size_summary.csv")
    n50 = scaling[scaling["train_size"] == 50]
    lin_pca2 = n50[n50["model"] == "Linear SVM — PCA 2"].iloc[0]["f1_mean"]
    q_pca2 = n50[n50["model"] == "QSVC — PCA 2 / 2Q (reps=1, full)"].iloc[0]["f1_mean"]
    assert lin_pca2 - q_pca2 > 0.15

    lin_pca4 = n50[n50["model"] == "Linear SVM — PCA 4"].iloc[0]["f1_mean"]
    q_pca4 = n50[n50["model"] == "QSVC — PCA 4 / 4Q (reps=1, full)"].iloc[0]["f1_mean"]
    assert lin_pca4 - q_pca4 > 0.35


def test_feature_map_ablation_reproduces_depth_degradation():
    ablation = pd.read_csv(FINAL_DIR / "final_feature_map_summary.csv")
    q4_full = ablation[(ablation["pca_dim"] == 4) & (ablation["entanglement"] == "full")]
    r1 = q4_full[q4_full["reps"] == 1].iloc[0]["F1 Mean"]
    r2 = q4_full[q4_full["reps"] == 2].iloc[0]["F1 Mean"]
    r3 = q4_full[q4_full["reps"] == 3].iloc[0]["F1 Mean"]
    assert r1 > r2 > r3
    assert r1 > 0.85
    assert r2 < 0.70
    assert r3 < 0.55


def test_final_validation_manifest_pass():
    val = json.loads((FINAL_DIR / "final_validation.json").read_text(encoding="utf-8"))
    assert val["status"] == "PASS"
    assert val["phase"] == 12
    assert val["failed_checks"] == 0
    assert val["tables_generated"] == 6
    assert val["figures_generated"] == 7
