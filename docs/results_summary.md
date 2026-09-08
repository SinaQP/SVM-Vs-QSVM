# Research Results Summary

Canonical experimental results from Phase 12 synthesis for **Classical SVM vs Quantum Kernel SVM for Breast Cancer Classification**.

For the exhaustive 19-section research report, see [results/final/final_research_report.md](../results/final/final_research_report.md).

---

## 1. Canonical Model Performance
Mean $\pm$ Sample Standard Deviation across the five predefined outer splits (`SEEDS = [42, 123, 456, 789, 2026]`):

| Model | PCA Dims | Qubits | Kernel / Feature Map | Accuracy | Malignant F1 | ROC-AUC | Runtime (s) |
| :--- | :---: | :---: | :--- | :---: | :---: | :---: | :---: |
| **Classical SVM (Comparator)** | **2** | **0** | **Linear / RBF (Inner Selected)** | **0.9509 ± 0.0048** | **0.9339 ± 0.0068** | **0.9866 ± 0.0074** | **0.0060 ± 0.0016** |
| Tuned Linear SVM | 2 | 0 | Linear ($C \in \{0.1, 1.0\}$) | 0.9509 ± 0.0078 | 0.9341 ± 0.0093 | 0.9894 ± 0.0030 | 0.0048 ± 0.0007 |
| Tuned RBF SVM | 2 | 0 | RBF ($C \in \{10, 100\}, \gamma$) | 0.9456 ± 0.0096 | 0.9263 ± 0.0133 | 0.9810 ± 0.0119 | 0.0072 ± 0.0024 |
| **Tuned QSVC (Canonical)** | **2** | **2** | **ZZ Map (reps=1, full, $C$)** | **0.9070 ± 0.0237** | **0.8678 ± 0.0388** | **0.9644 ± 0.0244** | **0.2257 ± 0.0232** |
| **Classical SVM (Comparator)** | **4** | **0** | **Linear / RBF (Inner Selected)** | **0.9632 ± 0.0157** | **0.9493 ± 0.0227** | **0.9941 ± 0.0039** | **0.0075 ± 0.0040** |
| Tuned Linear SVM | 4 | 0 | Linear ($C \in \{0.01, 0.1, 1.0, 100\}$) | 0.9684 ± 0.0100 | 0.9565 ± 0.0143 | 0.9952 ± 0.0029 | 0.0083 ± 0.0061 |
| Tuned RBF SVM | 4 | 0 | RBF ($C \in \{10, 100\}, \gamma$) | 0.9561 ± 0.0139 | 0.9401 ± 0.0198 | 0.9935 ± 0.0045 | 0.0071 ± 0.0019 |
| **Tuned QSVC (Canonical)** | **4** | **4** | **ZZ Map (reps=1, full, $C=1.0$)** | **0.9053 ± 0.0423** | **0.8721 ± 0.0556** | **0.9581 ± 0.0227** | **0.6599 ± 0.0863** |

---

## 2. Feature-Map Ablation Dynamics (Phase 9)
* **Depth Sensitivity:** In 4-qubit QSVC, deeper circuits severe degrade classification:
  * `reps=1, full`: $\text{F1} = 0.8721 \pm 0.0556$, Effective Rank = 96.49
  * `reps=2, full`: $\text{F1} = 0.6816 \pm 0.0590$, Effective Rank = 123.66
  * `reps=3, full`: $\text{F1} = 0.5403 \pm 0.0523$, Effective Rank = 137.43
* **Conservative Interpretation:** The poor historical 4Q baseline result was strongly associated with the `reps=2, full` feature-map configuration. Reducing depth to `reps=1` substantially restored performance, indicating that circuit depth and over-parameterization in the 16-dimensional Hilbert space were major contributors to performance loss.

---

## 3. Sample-Size Scaling (Phase 10)
* **No Small-Data Quantum Advantage:** At $N=50$, Classical Linear SVM retained strong diagnostic capability (PCA 2 F1 = 0.9157, PCA 4 F1 = 0.9128), whereas QSVC suffered catastrophic degradation:
  * QSVC 2Q ($N=50$): $\text{F1} = 0.7398 \pm 0.0531$ (gap of $-0.1759$)
  * QSVC 4Q ($N=50$): $\text{F1} = 0.4994 \pm 0.2110$ (gap of $-0.4134$)
* Classical SVM dominated QSVC at every evaluated sample size ($N \in [50, 100, 200, 300, 455]$).

---

## 4. Kernel Geometry and Centered Kernel Alignment
* Classical RBF reference kernel vs Quantum Fidelity kernel:
  * **PCA 2 (2Q):** Mean CKA = $0.573 \pm 0.158$, Quantum Effective Rank = $7.35$, RBF Effective Rank = $6.09$.
  * **PCA 4 (4Q):** Mean CKA = $0.338 \pm 0.072$, Quantum Effective Rank = $96.49$, RBF Effective Rank = $18.42$.
* The 4-qubit quantum kernel departs markedly from classical RBF geometry (low CKA $0.338$), confirming geometric novelty. However, this geometric transformation did not translate to superior classification boundaries.

---

## 5. Statistical Inference (Phase 11)
Primary endpoint: Malignant F1 score paired by matching outer seed:

| Comparison | Mean Paired Diff | Left / Right Wins | Raw p-value | Holm-Adjusted p | Bootstrap 95% CI |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Classical PCA2 vs QSVC PCA2** | **+0.0662** | **5 / 0** | **0.0625** | **0.1875** | **[0.0388, 0.0977]** |
| **Classical PCA4 vs QSVC PCA4** | **+0.0772** | **5 / 0** | **0.0625** | **0.1875** | **[0.0445, 0.1092]** |
| **QSVC PCA2 vs QSVC PCA4** | **-0.0043** | **2 / 3** | **0.8125** | **0.8125** | **[-0.0291, 0.0201]** |

* Across all 5 evaluated outer splits, classical SVM outperformed QSVC without exception (5/5 wins).
* Due to $n=5$ overlapping splits, the minimum exact Wilcoxon p-value is bounded at $0.0625$ (Holm-adjusted to $0.1875$), classifying these findings as descriptive and exploratory rather than asymptotic proof.
