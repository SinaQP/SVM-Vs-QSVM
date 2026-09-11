# Comprehensive Novelty and Prior Art Audit Matrix

**Project:** A Controlled Empirical Comparison of Classical and Quantum Kernel SVMs for Breast Cancer Classification  
**Status:** Frozen Canonical Benchmark `v1.0.0` Novelty Assessment  
**Document Purpose:** Direct head-to-head comparison of our experimental design and contributions against the closest related publications in quantum machine learning, classical kernel methods, and biomedical benchmarking.

---

## 1. Explicit Contribution Statement

This work does **not** propose a new quantum algorithm, variational circuit family, or theoretical complexity bound. Its contribution is a reproducible methodological benchmark and kernel-geometry case study yielding a scoped negative quantum-advantage result on one tabular biomedical dataset.

Specifically, the paper contributes:
1. **Controlled Nested Protocol:** Outer/inner evaluation across 5 fixed random seeds, ensuring that preprocessing transformers (`StandardScaler`, `PCA`, and `MinMaxScaler`) and quantum Gram matrices are refit within the relevant training partition. The same outer splits are reused across phases, including architecture selection and final evaluation, so the final comparison is descriptive rather than independently confirmatory.
2. **Multi-Seed Robustness with Paired Statistical Controls:** Moving beyond single-split evaluations by reporting paired split-level differences, exact Wilcoxon signed-rank tests, Holm-Bonferroni family-wise error adjustments, and exploratory split-level percentile bootstrap intervals.
3. **Controlled Feature-Map Ablation (60 quantum runs):** Comparison of repetition count and entanglement topology across 2- and 4-qubit regimes, documenting associations between architecture, geometry diagnostics, and predictive performance without assigning a single causal mechanism.
4. **Empirical Sample-Size Scaling Analysis ($N_{\text{train}} \in [50, 455]$):** Fixed-hyperparameter learning curves showing no QSVC advantage in the evaluated low-data regimes.
5. **Operator Feature Space Geometry and CKA Analysis:** Spectral decomposition and centered kernel alignment against tuned classical RBF kernels, showing that lower 4Q alignment ($\text{CKA} \approx 0.338$) did not coincide with superior predictive performance.
6. **Transparent Negative Quantum Advantage Finding:** Providing a rigorous, hype-free negative empirical result that clearly delineates the practical limits of NISQ-era quantum kernel classifiers on low-dimensional continuous tabular data.
7. **Complete Reproducible Release:** A frozen `v1.0.0` artifact suite containing automated test validation, raw per-fold logs, configuration files, and executed notebook pipelines.

---

## 2. Comparative Prior Art Matrix

| Comparison Field | **Havlíček et al. (2019)** [*Nature*] | **Suzuki et al. (2020)** [*QMI*] | **Huang et al. (2021)** [*Nat. Commun.*] | **Peters et al. (2021)** [*npj Quant. Inf.*] | **Azevedo et al. (2022)** [*QMI*] | **Wang (2024)** [*Physica Scripta*] | **Bowles et al. (2024)** [*arXiv*] | **Leither et al. (2026)** [*arXiv*] | **Present Manuscript (2026)** |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **What they studied** | Supervised learning with quantum feature spaces | Pauli expansion feature map design and classification accuracy | Theoretical power of data & projected quantum kernels | High-dimensional data classification on noisy quantum processors | Quantum transfer learning on breast cancer images | Genetic algorithm feature selection for QSVM | Systematic meta-benchmarking critique of QML practices | Benchmarking QML vs AutoML on oncological datasets | Controlled empirical comparison of classical SVM vs QSVC |
| **Dataset** | Synthetic 2-qubit toroidal data | Artificial 2D datasets, Breast Cancer (WDBC) | Synthetic classification tasks with discrete log structure | Synthetic Gaussian clusters, Breast cancer subsets | Full-field mammograms | Breast-cancer data with feature selection | Six benchmark tasks yielding 160 derived datasets | Multiple oncological cohorts (tabular, omics, spatial) | Wisconsin Diagnostic Breast Cancer (WDBC, $N=569$) |
| **Quantum model** | QSVM with $U_{\Phi}(\mathbf{x})$ 2-qubit circuit | QSVM with custom Pauli feature maps | Projected quantum kernels & classical shadow kernels | QSVC with ZZ feature map on IBM hardware | Hybrid ResNet-18 + 4-qubit VQC linear head | QSVM with parameterized rotations (QSVMF) | Diverse published QML models (QNN, QSVC) | Red Cedar QML framework (QSVC, QNN) | QSVC with Second-Order Pauli-Z (`zz_feature_map`) |
| **Classical baseline** | Linear / RBF SVM (default parameters) | Classical SVM (RBF) | Kernel ridge regression, RBF SVM | Classical SVM (Linear, RBF) | Classical linear SVM & ResNet-18 baseline | Standard SVM with GA feature selection | Properly tuned classical ML (XGBoost, SVM, RF) | AutoML neural networks & classical tabular models | Tuned Linear SVM & Tuned RBF SVM (nested CV selected) |
| **Feature preprocessing** | Synthetic coordinates | Direct scaling to $[0, 2\pi]$ | Problem-specific mathematical embedding | Standardization + PCA projection | ResNet latent vector extraction + PCA | GA-driven subset selection + normalization | Varied; surveyed literature practices | Standardized AutoML preprocessing | Training-only `StandardScaler` + `PCA` + `MinMaxScaler([0, \pi])` |
| **Validation design** | Single train/test holdout | Standard train/test split | PAC theoretical bounds + empirical validation | Train/test split evaluated on simulator & QPU | Single holdout split (train / val / test) | Train/test split on selected features | Multi-fold cross-validation analysis | Multi-fold CV vs AutoML baselines | 5-fold inner CV nested inside 5 fixed outer splits (80/20) |
| **Number of splits/seeds** | 1 split | 1 split | Synthetic seeds | 1 split (multi-shot repetitions) | 1 split | 1 split | Multiple splits across benchmark survey | Multi-fold runs across datasets | 5 fixed outer seeds (`[42, 123, 456, 789, 2026]`) |
| **Hyperparameter tuning** | Untuned / fixed default | Manual exploration | Theoretical tuning | Fixed $C$, untuned bandwidth | Classical Adam optimizer for VQC | GA optimization of feature mask; default SVM | Rigorous grid/random search | Automated hyperparameter optimization (AutoML) | Inner 5-fold CV for $C \in \{0.01..100\}$ & $\gamma$ candidates |
| **Kernel analysis** | Experimental fidelity verification | Pauli coefficient analysis | Spectral bias & projected kernel decay | Fidelity matrix condition number under noise | None (variational circuit output) | None | Broad model benchmarking | Not the focus | CKA vs tuned RBF, uncentered Frobenius alignment, spectral effective rank |
| **Sample-size analysis** | None | None | Generalization bounds ($N$ scaling) | None | None | None | Discussed theoretically | Evaluated across cohort sizes | Nested scaling at $N \in \{50, 100, 200, 300, 455\}$ |
| **Main result** | Strong accuracy on engineered synthetic data | Feature-map results on synthetic and WDBC tasks | Theoretical separation and projected-kernel analysis | Proof-of-concept hardware execution of kernel matrices | Hybrid quantum transfer learning on mammograms | QSVM with multi-objective feature selection | Out-of-the-box classical methods generally stronger across the benchmark | No evidence of quantum advantage in evaluated oncology settings | Classical comparator has higher F1 than QSVC (0.949 vs 0.872 in 4D; 5/5 splits) |
| **What our manuscript adds** | Paired WDBC case study with fold-local preprocessing | Nested tuning, multi-split statistics, and CKA | Small-scale empirical context, not validation of asymptotic theory | CPU statevector timing and architecture ablation | A distinct tabular kernel benchmark | Explicit selection records and kernel diagnostics | A reproducible single-dataset case study | More granular WDBC kernel diagnostics | **Controlled synthesis of methodology, geometry, and a scoped negative result** |

---

## 3. Differentiated Novelty Synthesis

When evaluated against the prior art:

1. **Versus breast-cancer QML studies:**
   Wang (2024) combines QSVM with multi-objective feature selection, while Azevedo et al. (2022) studies full-field mammograms; neither is a like-for-like version of this fixed WDBC kernel comparison. The present work adds paired split records, fold-local preprocessing, architecture ablation, and Gram-matrix diagnostics, but does not claim to supersede studies with different modalities or objectives.

2. **Versus General Benchmarking Critiques (Bowles et al. 2024, Leither et al. 2026):**
   Bowles et al. provide a broad QML benchmark, and Leither et al. compare quantum and classical models across oncology tasks. This paper complements those broader studies with one reproducible WDBC case study and detailed kernel diagnostics. The observed concentration-like geometry is associated with, but does not causally explain, the performance gap.

3. **Conclusion:**
   The manuscript's novelty is a reproducible combination of nested model selection, paired multi-split reporting, fixed-hyperparameter learning curves, feature-map ablation, and kernel-geometry diagnostics for this specific benchmark.
