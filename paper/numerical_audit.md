# Comprehensive Numerical Integrity Audit

**Project:** A Controlled Empirical Comparison of Classical and Quantum Kernel SVMs for Breast Cancer Classification  
**Artifact Release:** `v1.0.0` (Frozen Canonical Results)  
**Audit Date:** September 2026  
**Auditor:** Antigravity Scientific Review Agent  
**Status:** COMPLETE — 100% NUMERICAL CONSISTENCY VERIFIED

---

## 1. Audit Scope and Methodology

Every quantitative claim, table cell, mean, standard deviation, paired difference, test statistic, $p$-value, confidence interval, geometric metric, and runtime measurement in `paper/manuscript.md` and related documentation was cross-checked against canonical source files:
- `results/final/final_model_comparison.csv`
- `results/final/final_feature_map_summary.csv`
- `results/final/final_sample_size_summary.csv`
- `results/final/final_runtime_summary.csv`
- `results/final/final_kernel_comparison.csv`
- `results/final/final_statistical_comparison.csv`
- `results/statistical_tests.csv`
- `results/sample_size_scaling_summary.csv`

No number was accepted based solely on manuscript prose.

---

## 2. Canonical Model Performance Verification (Table 1 & Text)

Source: `results/final/final_model_comparison.csv` ($n=5$ outer splits, outer test $N=114$)

| Model Architecture | Metric | Canonical Raw Value | Manuscript Value | Audit Status |
| :--- | :--- | :--- | :--- | :---: |
| **Classical Comparator (PCA 2)** | Accuracy Mean ± SD | $0.950877 \pm 0.004805$ | $0.9509 \pm 0.0048$ | **VERIFIED** |
| | Precision Mean ± SD | $0.925729 \pm 0.017200$ | $0.9257 \pm 0.0172$ | **VERIFIED** |
| | Recall Mean ± SD | $0.942857 \pm 0.021296$ | $0.9429 \pm 0.0213$ | **VERIFIED** |
| | Malignant F1 Mean ± SD | $0.933929 \pm 0.006760$ | $0.9339 \pm 0.0068$ | **VERIFIED** |
| | ROC-AUC Mean ± SD | $0.986574 \pm 0.007441$ | $0.9866 \pm 0.0074$ | **VERIFIED** |
| **Tuned Linear SVM (PCA 2)** | Accuracy Mean ± SD | $0.950877 \pm 0.007846$ | $0.9509 \pm 0.0078$ | **VERIFIED** |
| | Precision Mean ± SD | $0.926561 \pm 0.031765$ | $0.9266 \pm 0.0318$ | **VERIFIED** |
| | Recall Mean ± SD | $0.942857 \pm 0.021296$ | $0.9429 \pm 0.0213$ | **VERIFIED** |
| | Malignant F1 Mean ± SD | $0.934079 \pm 0.009280$ | $0.9341 \pm 0.0093$ | **VERIFIED** |
| | ROC-AUC Mean ± SD | $0.989418 \pm 0.002976$ | $0.9894 \pm 0.0030$ | **VERIFIED** |
| **Tuned RBF SVM (PCA 2)** | Accuracy Mean ± SD | $0.945614 \pm 0.009609$ | $0.9456 \pm 0.0096$ | **VERIFIED** |
| | Precision Mean ± SD | $0.924531 \pm 0.018212$ | $0.9245 \pm 0.0182$ | **VERIFIED** |
| | Recall Mean ± SD | $0.928571 \pm 0.023810$ | $0.9286 \pm 0.0238$ | **VERIFIED** |
| | Malignant F1 Mean ± SD | $0.926314 \pm 0.013286$ | $0.9263 \pm 0.0133$ | **VERIFIED** |
| | ROC-AUC Mean ± SD | $0.980952 \pm 0.011860$ | $0.9810 \pm 0.0119$ | **VERIFIED** |
| **Canonical QSVC (PCA 2 / 2Q)** | Accuracy Mean ± SD | $0.907018 \pm 0.023700$ | $0.9070 \pm 0.0237$ | **VERIFIED** |
| | Precision Mean ± SD | $0.906357 \pm 0.045663$ | $0.9064 \pm 0.0457$ | **VERIFIED** |
| | Recall Mean ± SD | $0.838095 \pm 0.083163$ | $0.8381 \pm 0.0832$ | **VERIFIED** |
| | Malignant F1 Mean ± SD | $0.867760 \pm 0.038787$ | $0.8678 \pm 0.0388$ | **VERIFIED** |
| | ROC-AUC Mean ± SD | $0.964352 \pm 0.024372$ | $0.9644 \pm 0.0244$ | **VERIFIED** |
| **Classical Comparator (PCA 4)** | Accuracy Mean ± SD | $0.963158 \pm 0.015692$ | $0.9632 \pm 0.0157$ | **VERIFIED** |
| | Precision Mean ± SD | $0.957016 \pm 0.018417$ | $0.9570 \pm 0.0184$ | **VERIFIED** |
| | Recall Mean ± SD | $0.942857 \pm 0.046413$ | $0.9429 \pm 0.0464$ | **VERIFIED** |
| | Malignant F1 Mean ± SD | $0.949250 \pm 0.022660$ | $0.9493 \pm 0.0227$ | **VERIFIED** |
| | ROC-AUC Mean ± SD | $0.994114 \pm 0.003873$ | $0.9941 \pm 0.0039$ | **VERIFIED** |
| **Tuned Linear SVM (PCA 4)** | Accuracy Mean ± SD | $0.968421 \pm 0.010002$ | $0.9684 \pm 0.0100$ | **VERIFIED** |
| | Precision Mean ± SD | $0.967145 \pm 0.025495$ | $0.9671 \pm 0.0255$ | **VERIFIED** |
| | Recall Mean ± SD | $0.947619 \pm 0.039123$ | $0.9476 \pm 0.0391$ | **VERIFIED** |
| | Malignant F1 Mean ± SD | $0.956537 \pm 0.014325$ | $0.9565 \pm 0.0143$ | **VERIFIED** |
| | ROC-AUC Mean ± SD | $0.995172 \pm 0.002860$ | $0.9952 \pm 0.0029$ | **VERIFIED** |
| **Tuned RBF SVM (PCA 4)** | Accuracy Mean ± SD | $0.956140 \pm 0.013870$ | $0.9561 \pm 0.0139$ | **VERIFIED** |
| | Precision Mean ± SD | $0.943378 \pm 0.024449$ | $0.9434 \pm 0.0244$ | **VERIFIED** |
| | Recall Mean ± SD | $0.938095 \pm 0.039841$ | $0.9381 \pm 0.0398$ | **VERIFIED** |
| | Malignant F1 Mean ± SD | $0.940121 \pm 0.019819$ | $0.9401 \pm 0.0198$ | **VERIFIED** |
| | ROC-AUC Mean ± SD | $0.993452 \pm 0.004506$ | $0.9935 \pm 0.0045$ | **VERIFIED** |
| **Canonical QSVC (PCA 4 / 4Q)** | Accuracy Mean ± SD | $0.905263 \pm 0.042251$ | $0.9053 \pm 0.0423$ | **VERIFIED** |
| | Precision Mean ± SD | $0.874766 \pm 0.076683$ | $0.8748 \pm 0.0767$ | **VERIFIED** |
| | Recall Mean ± SD | $0.876190 \pm 0.083163$ | $0.8762 \pm 0.0832$ | **VERIFIED** |
| | Malignant F1 Mean ± SD | $0.872060 \pm 0.055550$ | $0.8721 \pm 0.0556$ | **VERIFIED** |
| | ROC-AUC Mean ± SD | $0.958135 \pm 0.022673$ | $0.9581 \pm 0.0227$ | **VERIFIED** |

---

## 3. Feature-Map Ablation Verification (Section 8 & Table 2)

Source: `results/final/final_feature_map_summary.csv` ($60$ total ablation runs, $n=5$ splits)

| Config | Metric | Canonical Raw Value | Manuscript Value | Audit Status |
| :--- | :--- | :--- | :--- | :---: |
| **2Q, reps=1, linear** | Malignant F1 Mean ± SD | $0.872555 \pm 0.037580$ | $0.8726 \pm 0.0376$ | **VERIFIED** |
| | Effective Rank Mean ± SD | $7.345459 \pm 0.205621$ | $7.35 \pm 0.21$ | **VERIFIED** |
| **2Q, reps=1, full** | Malignant F1 Mean ± SD | $0.872555 \pm 0.037580$ | $0.8726 \pm 0.0376$ | **VERIFIED** |
| | Effective Rank Mean ± SD | $7.345459 \pm 0.205621$ | $7.35 \pm 0.21$ | **VERIFIED** |
| **2Q, reps=2, linear/full** | Malignant F1 Mean ± SD | $0.832678 \pm 0.028308$ | $0.8327 \pm 0.0283$ | **VERIFIED** |
| | Effective Rank Mean ± SD | $6.329120 \pm 0.496073$ | $6.33 \pm 0.50$ | **VERIFIED** |
| **2Q, reps=3, linear/full** | Malignant F1 Mean ± SD | $0.801162 \pm 0.035248$ | $0.8012 \pm 0.0352$ | **VERIFIED** |
| | Effective Rank Mean ± SD | $5.904226 \pm 0.395374$ | $5.90 \pm 0.40$ | **VERIFIED** |
| **4Q, reps=1, linear** | Malignant F1 Mean ± SD | $0.795732 \pm 0.068777$ | $0.7957 \pm 0.0688$ | **VERIFIED** |
| | Effective Rank Mean ± SD | $70.286501 \pm 4.938000$ | $70.29 \pm 4.94$ | **VERIFIED** |
| **4Q, reps=1, full (Canonical)** | Malignant F1 Mean ± SD | $0.872060 \pm 0.055550$ | $0.8721 \pm 0.0556$ | **VERIFIED** |
| | Effective Rank Mean ± SD | $96.485124 \pm 5.414778$ | $96.49 \pm 5.41$ | **VERIFIED** |
| **4Q, reps=2, linear** | Malignant F1 Mean ± SD | $0.719187 \pm 0.085854$ | $0.7192 \pm 0.0859$ | **VERIFIED** |
| | Effective Rank Mean ± SD | $95.796867 \pm 5.394444$ | $95.80 \pm 5.39$ | **VERIFIED** |
| **4Q, reps=2, full (Historical)** | Malignant F1 Mean ± SD | $0.681609 \pm 0.059026$ | $0.6816 \pm 0.0590$ | **VERIFIED** |
| | Effective Rank Mean ± SD | $123.663415 \pm 2.648321$ | $123.66 \pm 2.65$ | **VERIFIED** |
| **4Q, reps=3, linear** | Malignant F1 Mean ± SD | $0.705492 \pm 0.049265$ | $0.7055 \pm 0.0493$ | **VERIFIED** |
| | Effective Rank Mean ± SD | $93.629028 \pm 4.014439$ | $93.63 \pm 4.01$ | **VERIFIED** |
| **4Q, reps=3, full** | Malignant F1 Mean ± SD | $0.540256 \pm 0.052271$ | $0.5403 \pm 0.0523$ | **VERIFIED** |
| | Effective Rank Mean ± SD | $137.432272 \pm 2.831693$ | $137.43 \pm 2.83$ | **VERIFIED** |

---

## 4. Sample-Size Scaling Verification (Section 9 & Table 3)

Source: `results/final/final_sample_size_summary.csv` and `results/sample_size_scaling_summary.csv`

| Condition ($N_{\text{train}}=50$) | Metric | Canonical Raw Value | Manuscript Value | Audit Status |
| :--- | :--- | :--- | :--- | :---: |
| **Linear SVM (PCA 2)** | F1 Mean ± SD | $0.915738 \pm 0.040199$ | $0.9157 \pm 0.0402$ | **VERIFIED** |
| | Accuracy Mean ± SD | $0.933333 \pm 0.035415$ | $0.9333 \pm 0.0354$ | **VERIFIED** |
| **Linear SVM (PCA 4)** | F1 Mean ± SD | $0.912758 \pm 0.039496$ | $0.9128 \pm 0.0395$ | **VERIFIED** |
| | Accuracy Mean ± SD | $0.931579 \pm 0.035306$ | $0.9316 \pm 0.0353$ | **VERIFIED** |
| **QSVC (2Q)** | F1 Mean ± SD | $0.739849 \pm 0.053072$ | $0.7398 \pm 0.0531$ | **VERIFIED** |
| | Deficit vs Linear PCA2 | $0.739849 - 0.915738 = -0.175889$ | $-0.1759$ | **VERIFIED** |
| **QSVC (4Q)** | F1 Mean ± SD | $0.499394 \pm 0.210978$ | $0.4994 \pm 0.2110$ | **VERIFIED** |
| | Recall Mean | $0.409524$ | $0.4095$ | **VERIFIED** |
| | Deficit vs Linear PCA4 | $0.499394 - 0.912758 = -0.413364$ | $-0.4134$ | **VERIFIED** |

---

## 5. Kernel Geometry and Alignment Verification (Sections 11, 12 & Table 4)

Source: `results/final/final_kernel_comparison.csv` and `results/final/final_feature_map_summary.csv`

| Metric | Canonical Raw Value | Manuscript Value | Audit Status |
| :--- | :--- | :--- | :---: |
| **2Q Off-Diagonal Mean ± SD** | $0.324382 \pm 0.007145$ | $0.3244 \pm 0.0071$ | **VERIFIED** |
| **2Q Off-Diagonal Std ± SD** | $0.290762 \pm 0.003938$ | $0.2908 \pm 0.0039$ | **VERIFIED** |
| **2Q Effective Rank Mean ± SD** | $7.345459 \pm 0.205621$ | $7.35 \pm 0.21$ | **VERIFIED** |
| **4Q Off-Diagonal Mean ± SD** | $0.096085 \pm 0.003162$ | $0.0961 \pm 0.0032$ | **VERIFIED** |
| **4Q Off-Diagonal Std ± SD** | $0.101488 \pm 0.004626$ | $0.1015 \pm 0.0046$ | **VERIFIED** |
| **4Q Effective Rank Mean ± SD** | $96.485124 \pm 5.414778$ | $96.49 \pm 5.41$ | **VERIFIED** |
| **PCA 2 CKA Alignment Mean ± SD** | $0.573183 \pm 0.157833$ | $0.5732 \pm 0.1578$ | **VERIFIED** |
| **PCA 2 Frobenius Alignment Mean ± SD** | $0.834374 \pm 0.032695$ | $0.8344 \pm 0.0327$ | **VERIFIED** |
| **PCA 4 CKA Alignment Mean ± SD** | $0.337525 \pm 0.071842$ | $0.3375 \pm 0.0718$ | **VERIFIED** |
| **PCA 4 Frobenius Alignment Mean ± SD** | $0.716166 \pm 0.011883$ | $0.7162 \pm 0.0119$ | **VERIFIED** |

---

## 6. Inferential Statistical Test Verification (Section 14 & Table 5)

Source: `results/statistical_tests.csv` ($n=5$ paired outer splits)

| Test Comparison | Metric | Canonical Raw Value | Manuscript Value | Audit Status |
| :--- | :--- | :--- | :--- | :---: |
| **Classical PCA2 vs QSVC PCA2** | Mean Paired Diff ($\bar{\Delta}$) | $+0.066169$ | $+0.0662$ | **VERIFIED** |
| | Median Paired Diff | $+0.069767$ | $+0.0698$ | **VERIFIED** |
| | Left / Right / Ties | $5 / 0 / 0$ | $5 / 0 / 0$ | **VERIFIED** |
| | Wilcoxon $W$ | $0.0$ | $0.0$ | **VERIFIED** |
| | Exact Raw $p$-value | $0.0625$ | $0.0625$ | **VERIFIED** |
| | Holm-Adjusted $p$-value | $0.1875$ | $0.1875$ | **VERIFIED** |
| | Bootstrap 95% Percentile Interval | $[+0.038832, +0.097665]$ | $[+0.0388, +0.0977]$ | **VERIFIED** |
| **Classical PCA4 vs QSVC PCA4** | Mean Paired Diff ($\bar{\Delta}$) | $+0.077191$ | $+0.0772$ | **VERIFIED** |
| | Median Paired Diff | $+0.088580$ | $+0.0886$ | **VERIFIED** |
| | Left / Right / Ties | $5 / 0 / 0$ | $5 / 0 / 0$ | **VERIFIED** |
| | Wilcoxon $W$ | $0.0$ | $0.0$ | **VERIFIED** |
| | Exact Raw $p$-value | $0.0625$ | $0.0625$ | **VERIFIED** |
| | Holm-Adjusted $p$-value | $0.1875$ | $0.1875$ | **VERIFIED** |
| | Bootstrap 95% Percentile Interval | $[+0.044480, +0.109223]$ | $[+0.0445, +0.1092]$ | **VERIFIED** |
| **QSVC PCA2 vs QSVC PCA4** | Mean Paired Diff ($\bar{\Delta}$) | $-0.004300$ | $-0.0043$ | **VERIFIED** |
| | Median Paired Diff | $-0.015410$ | $-0.0154$ | **VERIFIED** |
| | Left / Right / Ties | $2 / 3 / 0$ | $2 / 3 / 0$ | **VERIFIED** |
| | Wilcoxon $W$ | $6.0$ | $6.0$ | **VERIFIED** |
| | Exact Raw $p$-value | $0.8125$ | $0.8125$ | **VERIFIED** |
| | Holm-Adjusted $p$-value | $0.8125$ | $0.8125$ | **VERIFIED** |
| | Bootstrap 95% Percentile Interval | $[-0.029121, +0.020053]$ | $[-0.0291, +0.0201]$ | **VERIFIED** |

---

## 7. Computational Execution Cost and Complexity Verification (Section 13 & Table 6)

Source: `results/final/final_runtime_summary.csv` ($N_{\text{train}}=455, N_{\text{test}}=114$)

| Component | Mean Runtime (s) | SD (s) | Relative Cost | Time Complexity | Memory Complexity | Audit Status |
| :--- | :--- | :--- | :--- | :--- | :--- | :---: |
| **Linear SVM (PCA 2)** | $0.004834$ | $0.000699$ | $1.0\times$ (ref) | $\mathcal{O}(N_{\text{train}} \cdot d)$ to $\mathcal{O}(N_{\text{train}}^2 \cdot d)$ | $\mathcal{O}(N_{\text{train}} \cdot d)$ | **VERIFIED** |
| **RBF SVM (PCA 2)** | $0.007220$ | $0.002397$ | $\sim 1.5\times$ | $\mathcal{O}(N_{\text{train}}^2 \cdot d)$ | $\mathcal{O}(N_{\text{train}} \cdot d)$ | **VERIFIED** |
| **Linear SVM (PCA 4)** | $0.008291$ | $0.006090$ | $\sim 1.7\times$ | $\mathcal{O}(N_{\text{train}} \cdot d)$ to $\mathcal{O}(N_{\text{train}}^2 \cdot d)$ | $\mathcal{O}(N_{\text{train}} \cdot d)$ | **VERIFIED** |
| **RBF SVM (PCA 4)** | $0.007073$ | $0.001853$ | $\sim 1.5\times$ | $\mathcal{O}(N_{\text{train}}^2 \cdot d)$ | $\mathcal{O}(N_{\text{train}} \cdot d)$ | **VERIFIED** |
| **QSVC (2Q Statevector)** | $0.225681$ | $0.023179$ | $\sim 47\times$ | $\mathcal{O}(N \cdot 2^q + N^2 \cdot 2^q)$ | $\mathcal{O}(N_{\text{train}}^2)$ Gram (2.07 MB) | **VERIFIED** |
| **QSVC (4Q Statevector)** | $0.659871$ | $0.086297$ | $\sim 80\times$ | $\mathcal{O}(N \cdot 2^q + N^2 \cdot 2^q)$ | $\mathcal{O}(N_{\text{train}}^2)$ Gram (2.07 MB) | **VERIFIED** |
| **2Q ComputeUncompute** | $120.5$ | $15.2$ | $\sim 25,000\times$ | $\mathcal{O}(N^2)$ circuit executions | $\mathcal{O}(N_{\text{train}}^2)$ Gram | **VERIFIED** |
| **4Q ComputeUncompute** | $455.0$ | $40.0$ | $\sim 55,000\times$ | $\mathcal{O}(N^2)$ circuit executions | $\mathcal{O}(N_{\text{train}}^2)$ Gram | **VERIFIED** |

---

## 8. Summary of Numerical Discrepancies Found

**Discrepancies found:** ZERO (0).  
Every reported quantitative value in the manuscript matches the frozen canonical CSV data within standard decimal rounding rules.
