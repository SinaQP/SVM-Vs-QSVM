# Comprehensive Novelty and Prior Art Audit Matrix

**Project:** A Controlled Empirical Comparison of Classical and Quantum Kernel SVMs for Breast Cancer Classification  
**Status:** Frozen Canonical Benchmark `v1.0.0` Novelty Assessment  
**Document Purpose:** Direct head-to-head comparison of our experimental design and contributions against the closest related publications in quantum machine learning, classical kernel methods, and biomedical benchmarking.

---

## 1. Explicit Contribution Statement

This work does **not** propose a new quantum algorithm, a new variational quantum circuit family, or a new theoretical complexity bound. Rather, its authentic scientific contribution is an **exhaustive, leakage-free methodological benchmarking and kernel-geometry evaluation study** yielding a transparent, highly controlled negative quantum-advantage result on tabular biomedical data. 

Specifically, the paper contributes:
1. **Leakage-Free Nested Protocol:** Rigorous outer/inner nested cross-validation across 5 fixed random seeds, ensuring that preprocessing transformers (`StandardScaler`, `PCA`, and `MinMaxScaler`) and quantum Gram matrices are strictly refit within each training partition, eliminating subtle forms of data leakage prevalent in prior QML studies.
2. **Multi-Seed Robustness with Paired Statistical Controls:** Moving beyond single-split evaluations by reporting paired split-level differences, exact Wilcoxon signed-rank tests, Holm-Bonferroni family-wise error adjustments, and exploratory split-level percentile bootstrap intervals.
3. **Controlled Feature-Map Ablation (60 quantum runs):** Systematic isolation of circuit depth ($\text{reps} \in \{1, 2, 3\}$) and entanglement topology (`linear` vs. `full`) across both 2-qubit and 4-qubit regimes, demonstrating that circuit depth is the primary driver of performance degradation.
4. **Empirical Sample-Size Scaling Analysis ($N_{\text{train}} \in [50, 455]$):** Direct empirical testing of the "small-data quantum advantage" conjecture, demonstrating that QSVC exhibits its most acute performance deficit in low-data regimes.
5. **Operator Feature Space Geometry and CKA Analysis:** Spectral decomposition and Centered Kernel Alignment (CKA) against classical RBF kernels, explaining that while 4Q quantum kernels construct a geometrically distinct representation ($\text{CKA} \approx 0.338$), this geometric novelty does not translate into superior classification boundaries.
6. **Transparent Negative Quantum Advantage Finding:** Providing a rigorous, hype-free negative empirical result that clearly delineates the practical limits of NISQ-era quantum kernel classifiers on low-dimensional continuous tabular data.
7. **Complete Reproducible Release:** A frozen `v1.0.0` artifact suite containing automated test validation, raw per-fold logs, configuration files, and executed notebook pipelines.

---

## 2. Comparative Prior Art Matrix

| Comparison Field | **Havlíček et al. (2019)** [*Nature*] | **Suzuki et al. (2020)** [*QMI*] | **Huang et al. (2021)** [*Nat. Commun.*] | **Peters et al. (2021)** [*npj Quant. Inf.*] | **Azevedo et al. (2022)** [*QMI*] | **Wang (2024)** [*Physica Scripta*] | **Bowles et al. (2024)** [*arXiv*] | **Leither et al. (2026)** [*arXiv*] | **Present Manuscript (2026)** |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **What they studied** | Supervised learning with quantum feature spaces | Pauli expansion feature map design and classification accuracy | Theoretical power of data & projected quantum kernels | High-dimensional data classification on noisy quantum processors | Quantum transfer learning on breast cancer images | Genetic algorithm feature selection for QSVM | Systematic meta-benchmarking critique of QML practices | Benchmarking QML vs AutoML on oncological datasets | Controlled empirical comparison of classical SVM vs QSVC |
| **Dataset** | Synthetic 2-qubit toroidal data | Artificial 2D datasets, Breast Cancer (WDBC) | Synthetic classification tasks with discrete log structure | Synthetic Gaussian clusters, Breast cancer subsets | Breast Histopathology Image Dataset | Wisconsin Diagnostic Breast Cancer (WDBC) | 100+ public tabular & image datasets | Multiple oncological cohorts (tabular, omics, spatial) | Wisconsin Diagnostic Breast Cancer (WDBC, $N=569$) |
| **Quantum model** | QSVM with $U_{\Phi}(\mathbf{x})$ 2-qubit circuit | QSVM with custom Pauli feature maps | Projected quantum kernels & classical shadow kernels | QSVC with ZZ feature map on IBM hardware | Hybrid ResNet-18 + 4-qubit VQC linear head | QSVM with parameterized rotations (QSVMF) | Diverse published QML models (QNN, QSVC) | Red Cedar QML framework (QSVC, QNN) | QSVC with Second-Order Pauli-Z (`zz_feature_map`) |
| **Classical baseline** | Linear / RBF SVM (default parameters) | Classical SVM (RBF) | Kernel ridge regression, RBF SVM | Classical SVM (Linear, RBF) | Classical linear SVM & ResNet-18 baseline | Standard SVM with GA feature selection | Properly tuned classical ML (XGBoost, SVM, RF) | AutoML neural networks & classical tabular models | Tuned Linear SVM & Tuned RBF SVM (nested CV selected) |
| **Feature preprocessing** | Synthetic coordinates | Direct scaling to $[0, 2\pi]$ | Problem-specific mathematical embedding | Standardization + PCA projection | ResNet latent vector extraction + PCA | GA-driven subset selection + normalization | Varied; surveyed literature practices | Standardized AutoML preprocessing | Training-only `StandardScaler` + `PCA` + `MinMaxScaler([0, \pi])` |
| **Validation design** | Single train/test holdout | Standard train/test split | PAC theoretical bounds + empirical validation | Train/test split evaluated on simulator & QPU | Single holdout split (train / val / test) | Train/test split on selected features | Multi-fold cross-validation analysis | Multi-fold CV vs AutoML baselines | 5-fold inner CV nested inside 5 fixed outer splits (80/20) |
| **Number of splits/seeds** | 1 split | 1 split | Synthetic seeds | 1 split (multi-shot repetitions) | 1 split | 1 split | Multiple splits across benchmark survey | Multi-fold runs across datasets | 5 fixed outer seeds (`[42, 123, 456, 789, 2026]`) |
| **Hyperparameter tuning** | Untuned / fixed default | Manual exploration | Theoretical tuning | Fixed $C$, untuned bandwidth | Classical Adam optimizer for VQC | GA optimization of feature mask; default SVM | Rigorous grid/random search | Automated hyperparameter optimization (AutoML) | Inner 5-fold CV for $C \in \{0.01..100\}$ & $\gamma$ candidates |
| **Kernel analysis** | Experimental fidelity verification | Pauli coefficient analysis | Spectral bias & projected kernel decay | Fidelity matrix condition number under noise | None (variational circuit output) | None | Survey of kernel alignments across datasets | None (black-box model evaluation) | CKA vs tuned RBF, Frobenius alignment, Spectral Effective Rank |
| **Sample-size analysis** | None | None | Generalization bounds ($N$ scaling) | None | None | None | Discussed theoretically | Evaluated across cohort sizes | Nested scaling at $N \in \{50, 100, 200, 300, 455\}$ |
| **Main result** | 100% test accuracy on engineered synthetic data | Custom feature map achieves ~90% on WDBC | Theoretical separation; projected kernels avoid concentration | Proof-of-concept hardware execution of kernel matrices | QML matches classical transfer learning (~90%) | High accuracy (94–98%) via GA feature selection | Most reported quantum advantages disappear under proper baselines | No empirical quantum advantage across oncological tasks | Classical SVM consistently beats QSVC (F1: 0.949 vs 0.872; 5/5 wins) |
| **What our manuscript adds** | Methodological rigor, real tabular data, leakage isolation | Nested cross-validation, multi-seed statistical testing, CKA | Empirical tabular validation of theoretical concentration caveats | Wall-clock execution tracking, depth ablation, leakage protection | Multi-seed confidence intervals, exact statevector baselines | Leakage-free preprocessing, depth ablation, kernel geometry | Concrete, fully reproducible single-study case demonstration | In-depth geometric and spectral mechanism analysis on WDBC | **Complete synthesis of methodology, geometry, and negative advantage** |

---

## 3. Differentiated Novelty Synthesis

When evaluated against the prior art:

1. **Versus WDBC QML Literature (Wang 2024, Azevedo 2022, Chaudhry 2024):**
   Prior studies on this specific dataset evaluated single splits, applied global preprocessing (e.g. global PCA or global feature selection across the full dataset prior to partitioning), and did not isolate fold-level transformations. Furthermore, none of these works conducted circuit depth ablations across matching seeds or analyzed the geometry of the resulting Gram matrices using CKA and spectral effective rank. Our work directly supersedes these studies in methodological rigor.

2. **Versus General Benchmarking Critiques (Bowles et al. 2024, Leither et al. 2026):**
   While Bowles et al. established the meta-level critique that QML benchmarks are plagued by poor baselines and leakage, and Leither et al. demonstrated across multiple datasets that QML fails against AutoML, neither paper provided a granular, mechanistic investigation of the *kernel geometry* on a continuous tabular dataset. Our paper complements these broad surveys by providing a fine-grained, reproducible case study dissecting *why* the quantum kernel fails: namely, that deeper feature maps scatter states excessively across the operator feature space, and while the resulting 4-qubit geometry is distinct from classical RBF ($\text{CKA} \approx 0.338$), this distinctness does not align with the class-separating manifold.

3. **Conclusion:**
   The novelty of this manuscript lies not in claiming a groundbreaking new model, but in providing an exemplary, reproducible negative-result benchmark that sets a standard for methodological hygiene in NISQ-era quantum machine learning research.
