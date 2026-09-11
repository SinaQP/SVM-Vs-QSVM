# Submission Metadata: Machine Learning: Science and Technology (MLST)

**Journal:** *Machine Learning: Science and Technology* (IOP Publishing)  
**Publisher:** IOP Publishing  
**Article Type:** Paper (Original Research Paper)  
**Submission Status:** Scientifically verified; final author confirmation required before submission

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

## 2. Abstract

Quantum kernels offer flexible similarity measures, but evidence for their practical value depends on controlled comparisons with tuned classical baselines. We compare linear and radial-basis-function support vector classifiers with fixed ZZ-feature-map quantum support vector classifiers (QSVCs) on the Wisconsin Diagnostic Breast Cancer benchmark (569 samples and 30 features), treating malignant label 0 as positive. The design uses five predefined stratified 80/20 splits, fold-local preprocessing, five-fold inner cross-validation for model hyperparameters, exact statevector fidelity kernels after principal-component reduction to two or four dimensions, feature-map ablation, and fixed-hyperparameter sample-size analysis. Mean malignant-class F1 was 0.934 for the inner-selected classical comparator versus 0.868 for QSVC in two dimensions, and 0.949 versus 0.872 in four dimensions; the classical comparator was higher on all five matched splits. The corresponding two-sided exact Wilcoxon tests gave raw $p=0.0625$ and Holm-adjusted $p=0.1875$. Because the outer splits overlap and the feature-map architecture was selected using these same splits, these statistics are descriptive rather than independent confirmation. Within the tested ZZ maps, deeper full-entanglement configurations were associated with lower F1 (0.872 at one repetition and 0.540 at three repetitions in four qubits), and no small-data QSVC advantage was observed. The four-qubit kernel had lower alignment with the classical RBF kernel than the two-qubit kernel (CKA 0.338 versus 0.573), but greater geometric divergence did not improve classification. Timings measure classical CPU statevector simulation, not quantum hardware. Under these experimental conditions, no quantum advantage was observed.

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
