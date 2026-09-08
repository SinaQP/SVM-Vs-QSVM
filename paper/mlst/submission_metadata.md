# Submission Metadata: Machine Learning: Science and Technology (MLST)

**Journal:** *Machine Learning: Science and Technology* (IOP Publishing)  
**Publisher:** IOP Publishing  
**Article Type:** Paper (Original Research Paper)  
**Submission Status:** Submission Metadata Complete and Verified

---

## 1. Article Identification

* **Proposed Title:**  
  *A Controlled Empirical Comparison of Classical and Quantum Kernel SVMs for Breast Cancer Classification*

* **Short Running Title:**  
  *Controlled Comparison of Classical and Quantum SVMs*

* **Alternative Titles Considered:**
  1. *Empirical Evaluation of Quantum and Classical Kernel Support Vector Machines on Diagnostic Breast Cancer Data*
  2. *Benchmarking Classical vs. Quantum Kernel Classifiers Under Leakage-Free Cross-Validation*
  3. *Investigating Quantum Kernel Geometry and Classification Performance: A Controlled Benchmark on the WDBC Dataset*
  4. *On the Empirical Performance of Quantum Kernel Support Vector Classifiers in Low-Dimensional Tabular Regimes*
  5. *Controlled Comparison of Classical and Quantum Support Vector Machines: An Empirical Case Study*

---

## 2. Abstract (228 words)

Quantum kernel methods map classical feature vectors into quantum state spaces, theoretically offering expressive representational capacity. However, rigorous empirical comparisons against properly tuned classical baselines under leakage-free evaluation protocols remain sparse. In this work, we conduct a controlled empirical comparison of classical Support Vector Machines (Linear and RBF kernels) and Quantum Support Vector Classifiers (QSVC) on the Wisconsin Diagnostic Breast Cancer benchmark. To operate within current noisy intermediate-scale quantum constraints, input features are projected to two and four dimensions using principal component analysis and encoded via parameterized two- and four-qubit second-order Pauli-Z feature maps. The experimental pipeline enforces strict isolation of training and testing data across five outer random splits, nested five-fold cross-validation for hyperparameter tuning, feature-map architectural ablation, and sample-size scaling. Across all evaluated dimensions, classical SVMs consistently outperform QSVC in malignant-class F1 score (0.934 vs. 0.868 in two dimensions; 0.949 vs. 0.872 in four dimensions) and classification accuracy (0.951 vs. 0.907; 0.963 vs. 0.905), winning on 5/5 outer test splits. Feature-map ablation reveals that QSVC performance degrades sharply with circuit depth, while sample-size scaling demonstrates no small-data quantum advantage. Furthermore, centered kernel alignment confirms that although the four-qubit quantum kernel induces a geometry substantially distinct from classical RBF similarity (CKA ≈ 0.338), this novelty does not translate into superior classification boundaries. While exact statevector simulation incurs substantial computational overhead, five overlapping outer splits limit formal asymptotic statistical inference. Under the evaluated conditions, no quantum advantage is observed.

---

## 3. Keywords (7 keywords)

1. Quantum machine learning
2. Support vector machines
3. Quantum kernel methods
4. ZZ feature map
5. Empirical benchmarking
6. Kernel alignment
7. Wisconsin Diagnostic Breast Cancer

---

## 4. Subject Classifications / Topical Categorization

* **Primary Subject Category:** Quantum Machine Learning and Quantum Algorithms
* **Secondary Subject Category:** Machine Learning in Biology, Medicine, and Healthcare
* **Methodological Focus:** Empirical Benchmarking, Supervised Learning, Reproducibility, Kernel Methods
* **PACS / Physics Subject Headings (if required):**
  * `03.67.Ac` (Quantum algorithms, protocols, and simulations)
  * `03.67.Lx` (Quantum computation architectures and implementations)
  * `87.85.M-` (Biomedical engineering: computer applications)

---

## 5. Author Information

* **Author:** Sina Qasempour
* **Affiliation:** Independent Researcher, Iran
* **Corresponding Author:** Sina Qasempour
* **Email:** qasempoursina@gmail.com
* **ORCID:** [https://orcid.org/0009-0006-8853-6740](https://orcid.org/0009-0006-8853-6740) (0009-0006-8853-6740)
* **Author Profile / Website:** [https://sina-qasempour-portfolio-website.vercel.app/](https://sina-qasempour-portfolio-website.vercel.app/)

---

## 6. Author Contributions (CRediT Taxonomy)

As a single-author study, all CRediT taxonomy roles were conducted by Sina Qasempour:
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

## 7. Repository and Code Availability

* **Project Repository:** [https://github.com/SinaQP/SVM-Vs-QSVM](https://github.com/SinaQP/SVM-Vs-QSVM)
* **Permanent Release Tag:** `v1.0.0`
* **Commit SHA (Generic Baseline):** `a512cc3`
* **Submission Branch:** `submission/mlst`
* **Code Availability Statement:**
  * *"All source code for classical SVM baselines, quantum kernel statevector simulation, nested cross-validation pipelines, feature-map ablation, sample-size scaling, and statistical testing is publicly available under the open-source repository https://github.com/SinaQP/SVM-Vs-QSVM frozen at release v1.0.0. The pipeline provides complete source code, experiment configurations, validation scripts, canonical results, and reproducibility artifacts, and is fully automated and verifiable via included automated test suites and execution scripts."*

---

## 8. Research Data Availability

* **Data Availability Statement:**
  * *"The Wisconsin Diagnostic Breast Cancer (WDBC) benchmark dataset analyzed in this study is openly available in the UCI Machine Learning Repository and distributed via the Python scikit-learn library. All derived data—including stratified split partitions, cross-validation fold assignments, model predictions, hyperparameter tuning records, and statistical comparison outputs—are available in the project repository release v1.0.0 (https://github.com/SinaQP/SVM-Vs-QSVM)."*

---

## 9. Author Declarations

* **Funding Statement:**
  * *"This research received no external funding."*
* **Conflict of Interest Statement:**
  * *"The author declares no conflict of interest."*
* **Ethics and Biomedical Research Statement:**
  * *"This study used a publicly available benchmark dataset and did not involve the recruitment of human participants or collection of new clinical data."*
