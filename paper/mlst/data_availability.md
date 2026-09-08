# Research Data Availability Statement

**Manuscript Title:** A Controlled Empirical Comparison of Classical and Quantum Kernel SVMs for Breast Cancer Classification  
**Target Journal:** *Machine Learning: Science and Technology* (IOP Publishing)  
**Policy Compliance:** IOP Publishing Level 2 (Open Data Policy)

---

## Data Availability Statement

The empirical benchmarking conducted in this study utilizes the publicly available **Wisconsin Diagnostic Breast Cancer (WDBC)** dataset, originally compiled by Street, Wolberg, and Mangasarian (1993, 1995) at the University of Wisconsin and archived in the UCI Machine Learning Repository (Wolberg et al., 1995). The dataset is openly distributed and accessible via the `scikit-learn` Python library (`sklearn.datasets.load_breast_cancer`). The authors claim no proprietary rights or ownership over the original diagnostic data.

All derived data generated during this research—including stratified outer train/test partition indices, inner cross-validation fold assignments, tuned hyperparameter configurations, raw per-fold performance logs, Centered Kernel Alignment (CKA) matrices, effective rank diagnostics, sample-size scaling subsets, and paired statistical difference tables—are fully openly accessible without restriction.

These artifacts are permanently archived in the project's public GitHub repository release **`v1.0.0`**:
* **Repository URL:** [https://github.com/SinaQP/SVM-Vs-QSVM](https://github.com/SinaQP/SVM-Vs-QSVM)
* **Release Tag:** `v1.0.0`
* **Canonical Data Directory:** `results/` and `results/final/`
* **Data Format:** Comma-Separated Values (CSV) and serialized NumPy archives.

No private, proprietary, or clinical patient-identifying data were generated or analyzed in this study.
