# Research Methodology

## 1. Overview and Problem Formulation
This project investigates whether quantum kernel methods provide an empirical performance, sample efficiency, or geometric advantage over tuned classical Support Vector Machines (Linear and RBF kernels) on real-world medical diagnostic data.

* **Dataset:** Wisconsin Diagnostic Breast Cancer (WDBC), comprising $N=569$ patient cases with 30 continuous cell nucleus features.
* **Classification Target:** Binary diagnostic classification:
  * **Label 0 (Malignant):** 212 cases (37.26%) — explicitly designated as the primary positive class (`pos_label=0`) across all precision, recall, F1, and ROC-AUC calculations.
  * **Label 1 (Benign):** 357 cases (62.74%).
* **Primary Metric:** Malignant F1 score, reflecting clinical priority for high malignant sensitivity and precision under moderate class imbalance (~1.68:1).

---

## 2. Partitioning Protocol and Data Isolation
To ensure methodological integrity and prevent data leakage:
1. **Outer Splits:** Five fixed random seeds (`SEEDS = [42, 123, 456, 789, 2026]`) generate stratified 80/20 train/test partitions (455 training samples, 114 test samples per split).
2. **Quarantine:** Outer test sets are strictly quarantined during all preprocessing fitting and hyperparameter selection. Outer-test labels, predictions, or metrics are never used to choose models or hyperparameter values.
3. **Inner Cross-Validation:** Within each outer split, a 5-fold stratified cross-validation is performed exclusively on the 455 training samples.

---

## 3. Preprocessing and Leakage Protection
All transformers are fitted strictly on the applicable training partition and applied out-of-sample via `transform()`:
1. **Standardization:** Zero-mean, unit-variance scaling via `StandardScaler()`.
2. **Dimensionality Reduction:** Principal Component Analysis (`PCA`):
   * **PCA 2:** 2 principal components capturing $63.5\% \pm 0.6\%$ cumulative variance.
   * **PCA 4:** 4 principal components capturing $79.4\% \pm 0.4\%$ cumulative variance.
3. **Quantum MinMax Scaling:** PCA components are mapped to $[0, \pi]$ using `MinMaxScaler(feature_range=(0, np.pi), clip=True)` fitted solely on training observations.

---

## 4. Classical Support Vector Machines
Classical models use standard LibSVM implementations via scikit-learn:
* **Linear SVM:** `SVC(kernel='linear')` evaluated over regularization grid $C \in \{0.01, 0.1, 1.0, 10.0, 100.0\}$.
* **RBF SVM:** `SVC(kernel='rbf')` evaluated over grid $C \in \{0.01, 0.1, 1.0, 10.0, 100.0\}$ and $\gamma \in \{\text{'scale'}, \text{'auto'}, 0.01, 0.1, 1.0\}$.
* **Classical Comparator Selection:** For each outer seed, the classical configuration (Linear vs RBF) achieving highest inner-CV mean malignant F1 is selected as the representative classical comparator.

---

## 5. Quantum Kernel Support Vector Classifier (QSVC)
* **Quantum Feature Map:** Second-Order Pauli-Z Expansion (`ZZFeatureMap`) implemented via Qiskit:
  $$\mathcal{U}_{\Phi}(\mathbf{x}) = \prod_{d=1}^{\text{reps}} \left( \prod_{i < j} U_{\Phi_{i,j}}(\mathbf{x}) \prod_{k=1}^n U_{\Phi_k}(\mathbf{x}) H^{\otimes n} \right)$$
  where single-qubit rotations encode feature values $\Phi_k(\mathbf{x}) = 2 x_k$, and two-qubit entangling gates encode pairwise interactions $\Phi_{i,j}(\mathbf{x}) = 2(\pi - x_i)(\pi - x_j)$.
* **Fidelity Kernel:** Evaluated as quantum state overlap fidelity:
  $$K_{i,j} = |\langle \psi(\mathbf{x}_i) | \psi(\mathbf{x}_j) \rangle|^2$$
* **Simulation Engine:** Exact statevector inner products via vectorized matrix multiplication $\mathbf{K} = |\mathbf{\Psi} \mathbf{\Psi}^\dagger|^2$. Gram diagonal is explicitly set to $K_{i,i} = 1.0$ on training matrices.
* **Simulation vs Hardware:** All simulations use exact, noiseless statevector linear algebra. This avoids shot noise and decoherence, establishing theoretical upper-bound performance for the evaluated feature-map family on classical CPUs.
* **Classifier:** Scikit-learn `SVC(kernel='precomputed')` wrapped via `QSVC`, with regularization parameter $C \in \{0.01, 0.1, 1.0, 10.0, 100.0\}$ chosen via inner CV.

---

## 6. Kernel Geometry and Alignment Metrics
* **Effective Rank:** Exponential of the Shannon entropy of normalized non-negative Gram eigenvalues:
  $$p_i = \frac{\lambda_i}{\sum_j \lambda_j}, \quad \text{Effective Rank} = \exp\left(-\sum_{i} p_i \ln p_i\right)$$
* **Centered Kernel Alignment (CKA):** Measures geometric similarity between quantum Gram matrix $\mathbf{K}$ and classical RBF reference matrix $\mathbf{L}$:
  $$\text{CKA}(\mathbf{K}, \mathbf{L}) = \frac{\langle \mathbf{K}_c, \mathbf{L}_c \rangle_F}{\|\mathbf{K}_c\|_F \|\mathbf{L}_c\|_F}$$
  where $\mathbf{K}_c = \mathbf{H}\mathbf{K}\mathbf{H}$ with centering matrix $\mathbf{H} = \mathbf{I} - \frac{1}{n}\mathbf{1}\mathbf{1}^T$.

---

## 7. Paired Inferential Statistical Analysis
* **Primary Endpoint:** Malignant F1 score paired within each matching outer split seed.
* **Hypothesis Testing:** Two-sided exact Wilcoxon signed-rank test.
* **Multiplicity Adjustment:** Step-down Holm-Bonferroni correction covering the three predefined primary comparisons:
  1. Classical PCA2 vs QSVC PCA2
  2. Classical PCA4 vs QSVC PCA4
  3. QSVC PCA2 vs QSVC PCA4
* **Bootstrap Intervals:** Pointwise percentile bootstrap (10,000 resamples, seed 42) resampling split-level paired differences.
* **Inferential Limitation:** Five overlapping outer splits share data and do not represent independent population draws. Tests are reported as exploratory statistics rather than asymptotic confirmatory proof.
