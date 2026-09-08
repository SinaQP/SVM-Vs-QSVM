# Author Declarations and Statements

**Manuscript Title:** A Controlled Empirical Comparison of Classical and Quantum Kernel SVMs for Breast Cancer Classification  
**Target Journal:** *Machine Learning: Science and Technology* (MLST), IOP Publishing  
**Status:** Complete Submission Declarations

---

## 1. Authors and Affiliations

* **Author:**
  * **Name:** Sina Qasempour
  * **Affiliation:** Independent Researcher, Iran
  * **ORCID:** [https://orcid.org/0009-0006-8853-6740](https://orcid.org/0009-0006-8853-6740) (0009-0006-8853-6740)
  * **Email:** qasempoursina@gmail.com
  * **Author Profile / Website:** [https://sina-qasempour-portfolio-website.vercel.app/](https://sina-qasempour-portfolio-website.vercel.app/)

* **Corresponding Author:**
  * **Name:** Sina Qasempour
  * **Affiliation:** Independent Researcher, Iran
  * **Email:** qasempoursina@gmail.com

---

## 2. Author Contributions (CRediT Taxonomy)

As this is a single-author study, all research, implementation, and manuscript preparation roles were conducted by Sina Qasempour:

* **Conceptualization:** Sina Qasempour
* **Methodology:** Sina Qasempour
* **Software:** Sina Qasempour
* **Validation:** Sina Qasempour
* **Formal Analysis:** Sina Qasempour
* **Investigation:** Sina Qasempour
* **Data Curation:** Sina Qasempour
* **Writing – Original Draft:** Sina Qasempour
* **Writing – Review & Editing:** Sina Qasempour
* **Visualization:** Sina Qasempour
* **Project Administration:** Sina Qasempour

---

## 3. Funding and Financial Support

"This research received no external funding."

---

## 4. Conflicts of Interest / Competing Interests

"The author declares no conflict of interest."

---

## 5. Ethics Approval and Biomedical Research Statement

"This study used a publicly available benchmark dataset and did not involve the recruitment of human participants or collection of new clinical data."

---

## 6. Research Data Availability

The empirical benchmarking conducted in this study utilizes the publicly available **Wisconsin Diagnostic Breast Cancer (WDBC)** dataset, originally compiled by Street, Wolberg, and Mangasarian (1993, 1995) at the University of Wisconsin and archived in the UCI Machine Learning Repository (Wolberg et al., 1995). The dataset is openly distributed and accessible via the `scikit-learn` Python library (`sklearn.datasets.load_breast_cancer`). The author claims no proprietary rights or ownership over the original diagnostic data.

All derived data generated during this research—including stratified outer train/test partition indices, inner cross-validation fold assignments, tuned hyperparameter configurations, raw per-fold performance logs, Centered Kernel Alignment (CKA) matrices, effective rank diagnostics, sample-size scaling subsets, and paired statistical difference tables—are fully openly accessible without restriction in the project's public GitHub repository release **`v1.0.0`**:
* **Repository URL:** [https://github.com/SinaQP/SVM-Vs-QSVM](https://github.com/SinaQP/SVM-Vs-QSVM)
* **Release Tag:** `v1.0.0`

---

## 7. Code Availability

All software implementations for classical SVM baselines, quantum kernel statevector simulation, nested cross-validation, feature-map ablation, sample-size scaling, and statistical testing are publicly available under the open-source repository [https://github.com/SinaQP/SVM-Vs-QSVM](https://github.com/SinaQP/SVM-Vs-QSVM) tagged at release **`v1.0.0`**. The computational pipeline includes:
* Complete source code (`src/svm_vs_qsvm`)
* Experiment configuration files (`configs/`)
* Reproducibility and validation scripts (`scripts/`)
* Canonical results and artifacts (`results/final/`)
* Automated test suites (`tests/`)

---

## 8. Acknowledgments

"The author acknowledges the developers and maintainers of Python, scikit-learn, Qiskit, NumPy, SciPy, and matplotlib, whose open-source software made this reproducible benchmark possible."
