# Submission Metadata: Machine Learning: Science and Technology (MLST)

**Journal:** *Machine Learning: Science and Technology* (IOP Publishing)  
**Publisher:** IOP Publishing  
**Intended Article Type:** Benchmark (subject to editor and submission-portal classification)
**Submission Status:** Ready for independent read-only audit; not ready for submission

---

## 1. Article Identification

* **Article-type basis:** MLST's current official guidance defines Benchmarks as studies that compare methods, models, algorithms, codes, or software on a consistent problem or dataset and report comparative outcomes. This controlled same-dataset comparison is therefore prepared for that intended type; the journal retains classification authority. Official source (accessed 12 September 2026): https://publishingsupport.iopscience.iop.org/journals/machine-learning-science-and-technology/about-machine-learning-science-technology/.

* **Proposed Title:**  
  *A Controlled Empirical Comparison of Classical and Quantum Kernel SVMs for Breast Cancer Classification*

* **Short Running Title:**  
  *Controlled Comparison of Classical and Quantum SVMs*

* **Alternative Titles Considered:**
  1. *Empirical Evaluation of Quantum and Classical Kernel Support Vector Machines on Diagnostic Breast Cancer Data*
  2. *Benchmarking Classical vs. Quantum Kernel Classifiers Under Fully Nested Model Selection*
  3. *Investigating Quantum Kernel Geometry and Classification Performance: A Controlled Benchmark on the WDBC Dataset*
  4. *On the Empirical Performance of Quantum Kernel Support Vector Classifiers in Low-Dimensional Tabular Regimes*
  5. *Controlled Comparison of Classical and Quantum Support Vector Machines: An Empirical Case Study*

---

## 2. Abstract

Quantum kernels offer flexible similarity measures, but evidence for their practical value depends on controlled comparisons with tuned classical baselines. We compared linear and radial-basis-function support vector classifiers with ZZ-feature-map quantum support vector classifiers (QSVCs) on the Wisconsin Diagnostic Breast Cancer benchmark (569 samples and 30 features), treating malignant label 0 as positive. Across five predefined, overlapping stratified 80/20 partitions, preprocessing was fitted within each inner fold; QSVC repetition count, entanglement topology, and $C$ were jointly selected by five-fold inner cross-validation, frozen, refitted on the full outer-training set, and evaluated once on its outer test set. Mean malignant-class F1 was 0.934 for the inner-selected classical comparator versus 0.868 for QSVC after PCA to two dimensions, and 0.949 versus 0.872 after PCA to four dimensions; the classical comparator was higher on all five aligned splits. Exact Wilcoxon tests gave raw $p=0.0625$ and Holm-adjusted $p=0.1875$, so these dependent split-level results are descriptive and do not establish equivalence or population-level superiority. Exploratory ablation and fixed-hyperparameter sample-size analyses contextualized feature-map sensitivity but did not select the final architectures. Under the evaluated WDBC, PCA 2/4, 2Q/4Q, exact-statevector, and tested ZZ-feature-map conditions, no quantum advantage was observed.

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
* **Historical Release Tag:** `v1.0.0`
* **Corrected Nested Checkpoint:** `f4c8418`
* **Submission Branch:** `submission/mlst`
* **Code Availability Statement:**
  * *"All source code is available at https://github.com/SinaQP/SVM-Vs-QSVM. Release v1.0.0 preserves the historical benchmark and checkpoint f4c8418 records the corrected nested-selection authority layer. A new archival release containing the corrected outputs and documentation is required before submission."*

---

## 8. Research Data Availability

* **Data Availability Statement:**
  * *"The WDBC benchmark dataset is openly available through UCI and scikit-learn. Historical derived data are in release v1.0.0; corrected selections, predictions, and paired statistics are recorded at checkpoint f4c8418. A new archival release is required before submission."*

---

## 9. Author Declarations

* **Funding Statement:**
  * *"This research received no external funding."*
* **Conflict of Interest Statement:**
  * *"The author declares no conflict of interest."*
* **Ethics and Biomedical Research Statement:**
  * *"This study used a publicly available benchmark dataset and did not involve the recruitment of human participants or collection of new clinical data."*
* **Generative-AI Disclosure:**
  * *"OpenAI Codex (GPT-5.6 Sol) and Google Antigravity (3.8 Flash) assisted with coding/debugging, methodology and statistics review, literature/citation support, writing/editing, visualization workflows, and repository/documentation tasks. Research figures and reported numerical results were generated by executing the repository's programmatic workflows on stored data and artifacts, not supplied as conversational AI outputs. The author reviewed the work, made the final scientific decisions, and accepts full responsibility; no AI system is an author."*
