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
| 42 | 0.9398 | 0.8701 | +0.0696 | 0.9639 | 0.8753 | +0.0886 | 0.8701 | 0.8753 | -0.0052 |
| 123 | 0.9412 | 0.8714 | +0.0698 | 0.9647 | 0.8354 | +0.1293 | 0.8714 | 0.8354 | +0.0360 |
| 456 | 0.9250 | 0.9024 | +0.0226 | 0.9136 | 0.8158 | +0.0978 | 0.9024 | 0.8158 | +0.0866 |
| 789 | 0.9333 | 0.8000 | +0.1333 | 0.9302 | 0.9091 | +0.0211 | 0.8000 | 0.9091 | -0.1091 |
| 2026 | 0.9302 | 0.8947 | +0.0355 | 0.9737 | 0.9247 | +0.0490 | 0.8947 | 0.9247 | -0.0300 |

*Note: Source data from `results/final/final_statistical_comparison.csv`. The exact Wilcoxon test for $n=5$ observations has a discrete lower bound of $p = 1/2^4 = 0.0625$ when all differences share the same sign. Overlapping 80/20 train/test partitions share data, introducing covariance across splits.*
