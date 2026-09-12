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

The repository contains the historical split-level results and tuning/ablation/scaling summaries, kernel-geometry summaries and heatmaps, final figures, and the corrected nested inner-search records, selected configurations, predictions, metrics, paired comparisons, and validation manifests. Full Gram matrices are not deposited. Historical artifacts remain preserved in release `v1.0.0`; the corrected authority layer is recorded at commit `f4c8418` and is planned for archival release `v1.1.0` before submission:
* **Repository URL:** [https://github.com/SinaQP/SVM-Vs-QSVM](https://github.com/SinaQP/SVM-Vs-QSVM)
* **Historical Release:** `v1.0.0`
* **Proposed Corrected Release:** `v1.1.0` (not yet created)

---

## 7. Code Availability

All software implementations for classical SVM baselines, quantum-kernel statevector simulation, nested cross-validation, feature-map ablation, sample-size scaling, corrected joint QSVC selection, and statistical testing are available in the open-source repository [https://github.com/SinaQP/SVM-Vs-QSVM](https://github.com/SinaQP/SVM-Vs-QSVM). Release `v1.0.0` preserves the historical implementation; the corrected code and artifacts will be archived in proposed release `v1.1.0`. The computational pipeline includes:
* Complete source code (`src/svm_vs_qsvm`)
* Experiment configuration files (`configs/`)
* Reproducibility and validation scripts (`scripts/`)
* Canonical results and artifacts (`results/final/`)
* Corrected authoritative QSVC artifacts (`results/corrected_nested/`)
* Automated test suites (`tests/`)

---

## 8. Acknowledgments

"The author acknowledges the developers and maintainers of Python, scikit-learn, Qiskit, NumPy, SciPy, and matplotlib, whose open-source software made this reproducible benchmark possible."

Generative-AI tools were used during this work for coding and debugging assistance, methodological and statistical review, literature and citation support, scientific writing and editing, visualization workflows, and repository and documentation tasks. The tools were OpenAI Codex (GPT-5.6 Sol) and Google Antigravity (3.8 Flash). Research figures were generated conventionally with Python/Matplotlib from stored numerical artifacts; AI assistance concerned plotting code, workflow, captions, and review rather than direct image synthesis. Reported numerical results were obtained by executing the repository's reproducible computational workflows and checked against stored result artifacts. The author reviewed the generated code, analyses, citations, and manuscript content, made the final scientific decisions, and takes full responsibility for the work. No AI system is credited with authorship.
