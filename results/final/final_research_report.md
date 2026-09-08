# Classical SVM vs Quantum Kernel SVM for Breast Cancer Classification
## Canonical Final Research Project Report

**Project Scope:** Controlled comparative benchmark of Classical Support Vector Machines (Linear and RBF kernels) against Quantum Support Vector Classifiers (QSVC with parameterized ZZ feature maps) on the Wisconsin Diagnostic Breast Cancer dataset.
**Methodological Integrity:** Frozen Phases 1–11 protocol, nested 5-fold inner cross-validation for hyperparameter tuning, leakage-free fold-specific preprocessing, strictly isolated 80/20 outer test splits evaluated across five fixed outer random seeds (`[42, 123, 456, 789, 2026]`), and exact statevector Gram matrix simulation.

---

## 1. Research Goal
The primary objective of this project is to rigorously evaluate whether quantum kernel methods provide a measurable empirical advantage in classification accuracy, F1 score, or sample efficiency over classical SVM baselines on real-world medical diagnostic data.

Specifically, the project investigates:
1. Classification accuracy, precision, recall, malignant F1 score, and ROC-AUC between classical and quantum kernel machines.
2. The role of quantum feature map architecture, circuit depth (`reps`), and entanglement topology (`linear` vs `full`).
3. The geometric structure of quantum fidelity kernels in comparison to classical Radial Basis Function (RBF) kernels.
4. Sample-size scaling and whether quantum kernels provide a "small-data" sample efficiency advantage.
5. The computational complexity and real-time execution costs of exact quantum statevector simulation versus classical optimization.

---

## 2. Dataset
- **Name:** Wisconsin Diagnostic Breast Cancer (WDBC)
- **Samples ($N$):** 569 patient records
- **Features:** 30 continuous features extracted from digitized images of fine needle aspirates (cell nucleus characteristics).
- **Target Classes:** Binary classification:
  - Label 0: Malignant (212 cases, 37.26%) — treated as the primary positive class (`pos_label=0`) across all metrics.
  - Label 1: Benign (357 cases, 62.74%).
- **Class Balance:** Moderate class imbalance (~1.68:1 benign to malignant), establishing Malignant F1 score as the primary evaluation metric.

---

## 3. Experimental Design
The experimental architecture utilizes a nested cross-validation design across five fixed random seeds (`[42, 123, 456, 789, 2026]`):
- **Outer Partition:** Stratified 80/20 train/test split per seed (455 training samples, 114 test samples). Outer test sets are strictly quarantined until final evaluation.
- **Inner Tuning (Phase 11):** 5-fold stratified cross-validation executed solely on the 455 training samples of each outer fold.
- **Leakage Protections:** `StandardScaler`, `PCA`, and quantum `MinMaxScaler` are fitted exclusively on training splits and applied via `transform` to validation/test sets. Fold-specific quantum kernels are recomputed per inner fold.
- **Model Selection Rule:** Predefined prior to evaluation based on inner-CV mean malignant F1 score. Ties broken by smaller regularization parameter $C$, then Linear over RBF.
- **Evaluation:** Each selected configuration is refit once on the complete 455-sample training set and evaluated on the held-out 114-sample test set.

---

## 4. Preprocessing
1. **Standardization:** Zero-mean, unit-variance standardization (`StandardScaler`) fitted strictly on training observations.
2. **Dimensionality Reduction:** Principal Component Analysis (`PCA`):
   - **PCA 2:** 2 principal components capturing 63.5% ± 0.6% of cumulative variance.
   - **PCA 4:** 4 principal components capturing 79.4% ± 0.4% of cumulative variance.
3. **Quantum Scaling:** For quantum feature maps, PCA components are scaled to $[0, \pi]$ using `MinMaxScaler(feature_range=(0, np.pi), clip=True)` fitted on training data.

---

## 5. Classical Models
- **Linear Support Vector Classifier (`SVC(kernel='linear')`):**
  - Hyperparameter grid: $C \in [0.01, 0.1, 1.0, 10.0, 100.0]$.
- **Radial Basis Function Support Vector Classifier (`SVC(kernel='rbf')`):**
  - Hyperparameter grid: $C \in [0.01, 0.1, 1.0, 10.0, 100.0]$, $\gamma \in [	ext{'scale'}, 	ext{'auto'}, 0.01, 0.1, 1.0]$.
- **Classical Inner-Selected Comparator:** Per outer seed, the classical model (Linear vs RBF) achieving highest inner-CV F1 is chosen as the canonical benchmark.

---

## 6. Quantum Kernel Method
- **Feature Map:** Quantum Second-Order Expansion (`zz_feature_map`) implemented in Qiskit:
  $$\mathcal{U}_{\Phi}(\mathbf{x}) = \prod_{d} U_{\Phi}(\mathbf{x}) H^{\otimes n}$$
  where single-qubit rotations encode $Z$-phase shifts and two-qubit gates encode pairwise interactions $\Phi_{i,j}(\mathbf{x}) = 2(\pi - x_i)(\pi - x_j)$.
- **Kernel Evaluation:** Exact statevector inner products:
  $$K_{i,j} = |\langle \psi(\mathbf{x}_i) | \psi(\mathbf{x}_j) \rangle|^2$$
  computed via vectorized matrix multiplication $\mathbf{K} = |\mathbf{\Psi} \mathbf{\Psi}^\dagger|^2$.
- **Gram Matrix Guarantees:** Explicit unit diagonal $K_{i,i} = 1.0$, symmetry, positive semi-definiteness ($eigvals \ge -10^{-10}$).
- **Classifier:** QSVC with precomputed Gram matrix and $C \in [0.01, 0.1, 1.0, 10.0, 100.0]$ selected via inner CV.
- **Canonical Architecture:** $\text{reps}=1$, $\text{entanglement}=\text{'full'}$ (empirically validated in Phase 9).

---

## 7. Robustness Design
Evaluated across five independent outer random splits (`[42, 123, 456, 789, 2026]`). All performance metrics report sample mean and sample standard deviation across these five splits. Paired differences are computed strictly within each matching outer split.

---

## 8. Feature-Map Ablation Synthesis (Phase 9)
In Phase 9, a 60-run controlled ablation evaluated circuit repetitions ($\text{reps} \in \{1, 2, 3\}$) and entanglement topologies ($\text{'linear'}$ vs $\text{'full'}$):
- **2-Qubit Architecture:**
  - Reps = 1: F1 = 0.8726 ± 0.0376, Effective Rank = 7.35
  - Reps = 2: F1 = 0.8327 ± 0.0283, Effective Rank = 6.33
  - Reps = 3: F1 = 0.8012 ± 0.0352, Effective Rank = 5.90
  *(Note: For 2 qubits, linear and full entanglement topologies are mathematically identical as there is only one qubit pair).*
- **4-Qubit Architecture:**
  - Reps = 1, Linear: F1 = 0.7957 ± 0.0688, Effective Rank = 70.29
  - Reps = 1, Full: **F1 = 0.8721 ± 0.0556**, Effective Rank = 96.49
  - Reps = 2, Linear: F1 = 0.7192 ± 0.0859, Effective Rank = 95.80
  - Reps = 2, Full: F1 = 0.6816 ± 0.0590, Effective Rank = 123.66
  - Reps = 3, Linear: F1 = 0.7055 ± 0.0493, Effective Rank = 93.63
  - Reps = 3, Full: F1 = 0.5403 ± 0.0523, Effective Rank = 137.43
- **Critical Finding:** The poor historical 4Q result was strongly associated with the reps=2/full feature-map configuration. The ablation study showed that reducing depth to reps=1 substantially restored performance, indicating that feature-map design was a major contributor to the observed degradation.

---

## 9. Sample-Size Scaling Synthesis (Phase 10)
Scaling evaluation across training sample sizes $N \in [50, 100, 200, 300, 455]$ revealed:
- **No Small-Data Quantum Advantage:** At $N=50$, classical models achieved high diagnostic accuracy (Linear PCA2 F1 = 0.9157 ± 0.0402; Linear PCA4 F1 = 0.9128 ± 0.0395), whereas QSVC suffered severe performance loss:
  - QSVC 2Q: F1 = 0.7398 ± 0.0531 (a gap of -0.1759)
  - QSVC 4Q: F1 = 0.4994 ± 0.2110 (a gap of -0.4134, with recall falling to 0.4095)
- As sample size increased from 50 to 455, QSVC gradually recovered to F1 ~ 0.872, but at every single evaluated sample size, classical SVM maintained a commanding lead.

---

## 10. Nested Hyperparameter Tuning (Phase 11)
Nested cross-validation tuned the regularization parameter $C$ (and $\gamma$ for RBF) across 1,750 candidate/fold evaluations:
- Tuned vs Untuned deltas:
  - Linear SVM PCA2: $\Delta \text{F1} = +0.0039$, $\Delta \text{Accuracy} = +0.0035$
  - Linear SVM PCA4: $\Delta \text{F1} = +0.0064$, $\Delta \text{Accuracy} = +0.0053$
  - QSVC PCA2: $\Delta \text{F1} = -0.0048$, $\Delta \text{Accuracy} = -0.0053$
  - QSVC PCA4: $\Delta \text{F1} = 0.0000$, $\Delta \text{Accuracy} = 0.0000$
- **Conclusion:** Nested hyperparameter tuning did not alter the fundamental ranking or substantive conclusions. Classical SVM models retained their performance advantage over QSVC.

---

## 11. Final Model Performance
Canonical outer-test performance across the five frozen splits:

| Model | PCA Dims | Qubits | Feature Map / Kernel | Accuracy (Mean ± SD) | Precision (Mean ± SD) | Recall (Mean ± SD) | F1 Score (Mean ± SD) | ROC-AUC (Mean ± SD) | Total Runtime (s) |
| :--- | :---: | :---: | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Classical SVM (Comparator)** | **2** | **0** | **Linear / RBF (Inner Selected)** | **0.9509 ± 0.0048** | **0.9257 ± 0.0162** | **0.9429 ± 0.0213** | **0.9339 ± 0.0068** | **0.9866 ± 0.0074** | **0.0060 ± 0.0016** |
| Tuned Linear SVM | 2 | 0 | Linear ($C \in \{0.1, 1.0\}$) | 0.9509 ± 0.0078 | 0.9266 ± 0.0318 | 0.9429 ± 0.0213 | 0.9341 ± 0.0093 | 0.9894 ± 0.0030 | 0.0048 ± 0.0007 |
| Tuned RBF SVM | 2 | 0 | RBF ($C \in \{10, 100\}, \gamma \in \{0.01, 0.1, \text{scale}\}$) | 0.9456 ± 0.0096 | 0.9245 ± 0.0182 | 0.9286 ± 0.0238 | 0.9263 ± 0.0133 | 0.9810 ± 0.0119 | 0.0072 ± 0.0024 |
| **Tuned QSVC (Canonical)** | **2** | **2** | **ZZ Map (reps=1, full, $C \in \{10, 100\}$)** | **0.9070 ± 0.0237** | **0.9064 ± 0.0457** | **0.8381 ± 0.0832** | **0.8678 ± 0.0388** | **0.9644 ± 0.0244** | **0.2257 ± 0.0232** |
| **Classical SVM (Comparator)** | **4** | **0** | **Linear / RBF (Inner Selected)** | **0.9632 ± 0.0157** | **0.9547 ± 0.0235** | **0.9476 ± 0.0261** | **0.9493 ± 0.0227** | **0.9941 ± 0.0039** | **0.0075 ± 0.0040** |
| Tuned Linear SVM | 4 | 0 | Linear ($C \in \{0.01, 0.1, 1.0, 100.0\}$) | 0.9684 ± 0.0100 | 0.9671 ± 0.0255 | 0.9476 ± 0.0391 | 0.9565 ± 0.0143 | 0.9952 ± 0.0029 | 0.0083 ± 0.0061 |
| Tuned RBF SVM | 4 | 0 | RBF ($C \in \{10, 100\}, \gamma \in \{0.01, \text{scale}\}$) | 0.9561 ± 0.0139 | 0.9434 ± 0.0244 | 0.9381 ± 0.0398 | 0.9401 ± 0.0198 | 0.9935 ± 0.0045 | 0.0071 ± 0.0019 |
| **Tuned QSVC (Canonical)** | **4** | **4** | **ZZ Map (reps=1, full, $C=1.0$)** | **0.9053 ± 0.0423** | **0.8748 ± 0.0767** | **0.8762 ± 0.0832** | **0.8721 ± 0.0556** | **0.9581 ± 0.0227** | **0.6599 ± 0.0863** |

---

## 12. Kernel Geometry Analysis
Geometric properties of the training Gram matrices ($455 \times 455$) aggregated across seeds:
- **Quantum 2Q (reps=1, full):**
  - Off-diagonal similarity mean: $0.324 \pm 0.007$
  - Off-diagonal similarity SD: $0.291 \pm 0.004$
  - Effective rank: $7.35 \pm 0.21$
  - Condition number: $\sim 1.1 \times 10^{20}$ (rank deficient in $N=455$ space)
- **Quantum 4Q (reps=1, full):**
  - Off-diagonal similarity mean: $0.096 \pm 0.003$
  - Off-diagonal similarity SD: $0.101 \pm 0.005$
  - Effective rank: $96.49 \pm 5.41$
  - Condition number: $\sim 6.5 \times 10^{19}$
- **Interpretation:** In 4Q, the state space expands to $2^4 = 16$ dimensions, dispersing quantum statevectors across a broader manifold. This lowers the average inter-sample fidelity to $0.096$ and elevates effective rank to $96.5$.

---

## 13. Classical vs Quantum Kernel Comparison
Using the seed-specific tuned classical RBF kernel as a reference:
- **Centered Kernel Alignment (CKA):**
  - **PCA 2:** Mean CKA = $0.573 \pm 0.158$ (Seed 42: $0.713$, Frobenius Alignment: $0.858$). The 2-qubit quantum kernel shares moderate-to-high structural alignment with classical RBF geometry.
  - **PCA 4:** Mean CKA = $0.338 \pm 0.072$ (Seed 42: $0.335$, Frobenius Alignment: $0.716$). The 4-qubit quantum kernel departs markedly from classical RBF geometry.
- **Scientific Rationale:** The low CKA in 4Q confirms that the quantum feature map produces a distinct similarity metric. However, this distinct geometric transformation did not translate to superior diagnostic separation; instead, classification accuracy and F1 score lagged classical benchmarks.

---

## 14. Computational Cost and Scaling
- **Classical CPU SVM:** Total runtime $0.005$ to $0.008$ seconds per outer split ($N_{\text{train}}=455, N_{\text{test}}=114$).
- **Exact Statevector Simulation:**
  - 2Q: $0.226 \pm 0.023$ seconds (~45x classical runtime).
  - 4Q: $0.660 \pm 0.086$ seconds (~80x classical runtime).
  - Scaling: Simulation runtime scales with Hilbert dimension ($2^q$) and number of entanglement edges ($q(q-1)/2$).
- **Historical Circuit-Pair Execution (`ComputeUncompute`):** Required $120$ seconds (2Q) and $455$ seconds (4Q), being $\sim 25,000\times$ to $55,000\times$ slower than classical SVM.
- **Memory Footprint:** The precomputed Gram matrix scales as $O(N_{\text{train}}^2)$. Storing the $455 \times 455$ float64 training matrix and $114 \times 455$ test matrix requires $2.07$ MB of memory.

---

## 15. Statistical Analysis
Frozen inferential testing on the primary endpoint (Malignant F1 Score):

| Comparison | Mean Paired Diff | Median Paired Diff | Wins / Losses / Ties | Wilcoxon W | Raw p-value | Holm-Adjusted p-value | Bootstrap 95% CI |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Classical PCA2 vs QSVC PCA2** | **+0.0662** | **+0.0698** | **5 / 0 / 0** | **0.0** | **0.0625** | **0.1875** | **[0.0388, 0.0977]** |
| **Classical PCA4 vs QSVC PCA4** | **+0.0772** | **+0.0886** | **5 / 0 / 0** | **0.0** | **0.0625** | **0.1875** | **[0.0445, 0.1092]** |
| **QSVC PCA2 vs QSVC PCA4** | **-0.0043** | **-0.0154** | **2 / 3 / 0** | **6.0** | **0.8125** | **0.8125** | **[-0.0291, 0.0201]** |

**Critical Statistical Interpretation:**
Across the five predefined outer splits, the observed paired differences consistently favored the classical models (5 wins out of 5 splits for both PCA 2 and PCA 4). However, because $n=5$ overlapping splits do not constitute independent draws and the minimum possible two-sided exact Wilcoxon p-value for $n=5$ is $0.0625$ (adjusted to $0.1875$ by Holm), these findings remain descriptive and exploratory rather than asymptotic formal proof.

---

## 16. Research Questions Answered
- **RQ1: Does the quantum kernel improve classification accuracy?**
  No. On this dataset, Classical SVM achieved higher accuracy than QSVC across both feature dimensions (PCA 2: $0.9509$ vs $0.9070$; PCA 4: $0.9684$ Linear / $0.9632$ Comparator vs $0.9053$). Classical models won on 5/5 outer splits.
- **RQ2: Are there meaningful F1 / ROC-AUC differences?**
  Yes. Classical models demonstrated a consistent +0.0662 F1 advantage in PCA 2 and +0.0772 F1 advantage in PCA 4. Classical ROC-AUC exceeded 0.989 (PCA2) and 0.994 (PCA4), compared to 0.964 and 0.958 for QSVC.
- **RQ3: How does QSVC behave with 2 vs 4 features/qubits?**
  With optimal shallow feature maps ($\text{reps}=1, \text{full}$), QSVC performance was virtually flat between 2Q and 4Q (F1: $0.8678$ vs $0.8721$, paired difference $-0.0043$). In contrast, classical models gained substantial predictive power from 4 features (F1: $0.9341 \to 0.9565$).
- **RQ4: What is the effect of increasing features/qubits on computational cost?**
  Statevector simulation runtime increased from $0.226$s to $0.660$s (~2.9x), reflecting the exponential growth of statevector dimension ($2^2=4$ to $2^4=16$) and quadratic growth of two-qubit interaction terms (1 to 6).
- **RQ5: What similarity geometry does the quantum feature map generate?**
  In 2Q, the quantum kernel maintains moderate off-diagonal similarity ($0.324$) and effective rank $7.35$. In 4Q, similarity concentrates near zero ($0.096$) and effective rank surges to $96.5$.
- **RQ6: How different is it from classical RBF geometry?**
  Centered Kernel Alignment (CKA) is moderate in 2Q ($0.573$), but drops substantially in 4Q ($0.338$). The quantum kernel constructs a geometry fundamentally distinct from RBF, but this geometry does not improve class separation.
- **RQ7: How much more expensive is QSVC?**
  Statevector simulation is $\sim 45\times$ (2Q) to $\sim 80\times$ (4Q) slower than classical LibSVM. Historical circuit-pair simulation is $\sim 25,000\times$ to $55,000\times$ slower.
- **RQ8: Are results stable across seeds?**
  Yes. Classical superiority was observed across all five evaluated outer seeds without exception.

---

## 17. Main Findings
1. Classical Support Vector Machines outperformed Quantum Support Vector Classifiers across all evaluated metrics and configurations on the Wisconsin Diagnostic Breast Cancer dataset.
2. The quantum feature map is highly sensitive to depth and entanglement topology. Shallow architectures ($\text{reps}=1, \text{full}$) are required to avoid geometric degradation in 4Q.
3. QSVC exhibited no small-sample efficiency advantage. The performance deficit was largest at $N=50$.
4. Increasing qubit count from 2 to 4 did not yield classification gains for QSVC, whereas classical models benefited from the increased variance captured by 4 PCA components.
5. Quantum kernel computation incurs severe computational overhead relative to classical SVM optimization.

---

## 18. Limitations Table

| Dimension | Experimental Limitation | Scientific Consequence |
| :--- | :--- | :--- |
| **Dataset Scope** | Single tabular biomedical dataset (WDBC, $N=569$) | Conclusions cannot be generalized to image, speech, or inherently quantum data. |
| **Dimensionality** | PCA compression to 2 and 4 dimensions | Information loss from truncation (captures 63.5% and 79.4% variance). |
| **Qubit Scale** | Limited to 2 and 4 qubits | Does not evaluate regimes where classical simulation becomes intractable ($q \ge 40$). |
| **Feature Map Family** | Only standard ZZ Second-Order Expansion evaluated | Custom, data-reuploading, or trained quantum embeddings might yield different geometry. |
| **Sample Overlap** | 5 overlapping 80/20 outer splits | Splits are statistically dependent; violates independence assumptions of standard tests. |
| **Hypothesis Re-use** | Feature map selected on outer splits during Phase 9 | Prevents treating Phase 11 statistical testing as formal confirmatory hypothesis tests. |
| **Inferential Power** | Small sample of outer splits ($n=5$) | Minimum exact Wilcoxon p-value is bounded at 0.0625; unable to reject null at $\alpha=0.05$. |
| **Simulation Fidelity** | Ideal exact statevector simulation (noise-free) | Ignores physical NISQ hardware noise, decoherence, and finite measurement shot noise. |
| **Memory Complexity** | Precomputed Gram matrix scales as $O(N^2)$ | Prohibitive for large-scale biomedical datasets without randomized Nyström approximations. |

---

## 19. Conclusions

### Supported Conclusions:
1. On the Wisconsin Diagnostic Breast Cancer dataset compressed to 2 and 4 PCA components, Classical SVM baselines (Linear and RBF) achieve superior classification performance compared to evaluated QSVC models.
2. Classical models outperform QSVC across all five outer cross-validation splits in malignant F1 score and classification accuracy.
3. QSVC performance is acutely sensitive to circuit depth and entanglement; $\text{reps}=1$ full entanglement is strictly superior to deeper configurations.
4. QSVC exhibits no small-data sample efficiency advantage on this dataset.
5. Quantum kernel simulation is orders of magnitude more computationally demanding than classical SVM training.

### Explicitly Unsupported (Rejected) Claims:
1. *Quantum machine learning is universally inferior to classical ML.* (Rejected: Limited to this dataset, feature map, and qubit scale).
2. *Quantum advantage in kernel classification is theoretically impossible.* (Rejected: Theoretically possible on engineered or discrete logarithmic problems).
3. *These models possess clinical diagnostic validity.* (Rejected: Diagnostic models require extensive clinical validation, external validation cohorts, and full feature preservation).
4. *The results provide formal statistical proof.* (Rejected: Five overlapping splits limit formal inferential certainty).
5. *Statevector CPU runtimes represent physical quantum hardware runtimes.* (Rejected: Physical QPUs execute circuits with shot noise, device latency, and measurement overhead).
