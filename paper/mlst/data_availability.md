# Research Data Availability Statement

**Manuscript Title:** A Controlled Empirical Comparison of Classical and Quantum Kernel SVMs for Breast Cancer Classification  
**Target Journal:** *Machine Learning: Science and Technology* (IOP Publishing)  
**Policy Compliance:** IOP Publishing Level 2 (Open Data Policy)

---

## Data Availability Statement

The empirical benchmarking conducted in this study utilizes the publicly available **Wisconsin Diagnostic Breast Cancer (WDBC)** dataset, originally compiled by Street, Wolberg, and Mangasarian (1993, 1995) at the University of Wisconsin and archived in the UCI Machine Learning Repository (Wolberg et al., 1995). The dataset is openly distributed and accessible via the `scikit-learn` Python library (`sklearn.datasets.load_breast_cancer`). The author claims no proprietary rights or ownership over the original diagnostic data.

The public GitHub repository contains the derived tables and records used in the manuscript, including historical split-level model results, tuning/ablation/scaling summaries, kernel-geometry summaries, final figures, corrected nested inner-search records, selected configurations, outer-test predictions and metrics, paired statistical comparisons, and validation manifests. Full Gram matrices are not deposited; the repository provides their aggregate diagnostics and illustrative heatmaps.

Historical artifacts remain preserved in release **`v1.0.0`** for provenance. The corrected authoritative outputs, configurations, predictions, validation artifacts, and reproducible analysis code supporting the submitted results are publicly available in the submission-associated archival release **`v1.1.0`**:
* **Repository URL:** [https://github.com/SinaQP/SVM-Vs-QSVM](https://github.com/SinaQP/SVM-Vs-QSVM)
* **Historical Release:** `v1.0.0`
* **Submission-Associated Archival Release:** [`v1.1.0`](https://github.com/SinaQP/SVM-Vs-QSVM/releases/tag/v1.1.0)
* **Historical Directories:** `results/` and `results/final/`
* **Authoritative Corrected QSVC Directory:** `results/corrected_nested/`
* **Data Format:** CSV, JSON, Markdown, and PNG.

No private, proprietary, or clinical patient-identifying data were generated or analyzed in this study.
