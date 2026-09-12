# Table 5: Paired Statistical Hypothesis Testing on Primary Endpoint (Malignant F1 Score)

Inferential evaluation across matching outer test splits ($n=5$). Pairwise differences are computed strictly as $\Delta = \text{Model}_{\text{Left}} - \text{Model}_{\text{Right}}$ per random seed. Multiplicity is controlled using step-down Holm-Bonferroni correction across the three predefined primary hypotheses.

| Comparison | Evaluated Metric | $n$ Outer Splits | Mean Paired Diff ($\bar{\Delta}$) | Median Paired Diff | Std of Paired Diff | Left Wins / Right Wins / Ties | Wilcoxon Signed-Rank $W$ | Exact Raw $p$-value | Holm-Adjusted $p$-value | Bootstrap 95% CI [Low, High] | Methodological Classification |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| **Classical PCA2 vs QSVC PCA2** | Malignant F1 | 5 | **+0.0662** | +0.0698 | 0.0392 | **5 / 0 / 0** | 0.0 | 0.0625 | 0.1875 | **[+0.0388, +0.0977]** | Exploratory (Bounded Power) |
| **Classical PCA4 vs QSVC PCA4** | Malignant F1 | 5 | **+0.0772** | +0.0886 | 0.0417 | **5 / 0 / 0** | 0.0 | 0.0625 | 0.1875 | **[+0.0445, +0.1092]** | Exploratory (Bounded Power) |
| **QSVC PCA2 vs QSVC PCA4** | Malignant F1 | 5 | **-0.0043** | -0.0154 | 0.0317 | 2 / 3 / 0 | 6.0 | 0.8125 | 0.8125 | [-0.0291, +0.0201] | Exploratory (No Difference) |

### Per-Seed Paired Observations

| Seed | Classical PCA2 F1 | QSVC PCA2 F1 | Paired Diff (PCA2) | Classical PCA4 F1 | QSVC PCA4 F1 | Paired Diff (PCA4) | QSVC PCA2 F1 | QSVC PCA4 F1 | Paired Diff (QSVC 2Q - 4Q) |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 42 | 0.9302 | 0.8916 | +0.0387 | 0.9512 | 0.9070 | +0.0442 | 0.8916 | 0.9070 | -0.0154 |
| 123 | 0.9412 | 0.9176 | +0.0235 | 0.9767 | 0.9524 | +0.0244 | 0.9176 | 0.9524 | -0.0347 |
| 456 | 0.9268 | 0.8533 | +0.0735 | 0.9136 | 0.8250 | +0.0886 | 0.8533 | 0.8250 | +0.0283 |
| 789 | 0.9412 | 0.8158 | +0.1254 | 0.9512 | 0.8462 | +0.1051 | 0.8158 | 0.8462 | -0.0304 |
| 2026 | 0.9302 | 0.8605 | +0.0698 | 0.9535 | 0.8298 | +0.1237 | 0.8605 | 0.8298 | +0.0307 |

*Note: Source data from `results/corrected_nested/corrected_statistical_comparison.csv`, `results/corrected_nested/qsvc_outer_test_results.csv`, and the inner-selected classical rows in `results/tuned_outer_test_results.csv`. The exact Wilcoxon test for $n=5$ observations has a discrete lower bound of $p = 1/2^4 = 0.0625$ when all differences share the same sign. Overlapping 80/20 train/test partitions share data, introducing covariance across splits.*
