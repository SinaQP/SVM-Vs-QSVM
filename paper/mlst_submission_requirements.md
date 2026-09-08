# Machine Learning: Science and Technology (MLST) — Submission Requirements and Guidelines

**Target Journal:** *Machine Learning: Science and Technology* (MLST)  
**Publisher:** IOP Publishing  
**ISSN:** 2632-2153  
**Verified Date:** September 2026  
**Official Journal URL:** https://iopscience.iop.org/journal/2632-2153  
**IOP Author Support & Guidelines:** https://publishingsupport.iopscience.iop.org/author-guidelines-for-conference-proceedings/ and https://publishingsupport.iopscience.iop.org/

---

## 1. Journal Scope and Editorial Mission
* *Machine Learning: Science and Technology* is a multidisciplinary open-access journal devoted to the application and development of machine learning techniques across the physical, chemical, biological, materials, and engineering sciences.
* **Topical Sections:** Includes a dedicated topical track on **Quantum Machine Learning and Quantum Algorithms** applied to scientific domains.
* **Empirical & Methodological Rigor:** The journal explicitly welcomes rigorous benchmarking, reproducibility evaluations, negative or null results that correct the literature, and ablation studies, provided they adhere to high methodological standards.

---

## 2. Article Type Selection
* **Selected Article Type:** **Paper** (Regular Original Research Paper).
* **Rationale:**
  * The manuscript presents a comprehensive, multi-phase controlled empirical benchmarking study (~5,600+ words, 6 tables, 7 figures, 35 references).
  * It is neither a rapid short communication (*Letter*), nor an encyclopedic literature synthesis (*Review*), nor a discussion of an existing publication (*Comment*).
  * A standard "Paper" accommodates full methodological depth, nested cross-validation protocols, kernel geometry diagnostics, and complete ablation data without artificial length truncation.
* **Length Constraints:** Regular papers in MLST have no rigid page limit; typical lengths range between 6,000 and 10,000 words.

---

## 3. Review Model and Peer Review Options
* **Default Review Model:** **Single-anonymous peer review** (reviewers know author identities; authors do not know reviewer identities).
* **Double-Anonymous Option:** IOP Publishing offers authors the option to choose double-anonymous review at initial submission if desired.
* **Simulated Internal Review Status:** Internal pre-submission reviews conducted during manuscript preparation are strictly marked as `INTERNAL SIMULATION — NOT ACTUAL PEER REVIEW`.

---

## 4. Submission File Requirements
* **Initial Submission:**
  * A single, comprehensive PDF containing the complete text, figures, and tables embedded in their logical locations for reviewer readability.
  * Supplementary Material document (PDF/ZIP) containing extended tabular scaling and fold-level data.
* **Accepted / Revised Submission (Production Package):**
  * LaTeX source package: `.tex` root manuscript, `.bib` bibliography file, and all figure source files (`.png`, `.pdf`, or `.eps`) in a standalone directory.
* **Figure Requirements:** High-resolution (minimum 300 DPI), vector PDF/EPS preferred or crisp PNG; self-contained captions with all abbreviations defined.
* **Table Requirements:** Standard LaTeX booktabs format, fully captioned, no vertical rules.

---

## 5. LaTeX and Formatting Guidelines
* **Flexible Initial Formatting:** IOP Publishing adheres to flexible initial submission formatting. The manuscript does not need to conform to final journal typography at initial submission as long as it is legible and clear.
* **Recommended Package Structure:** Standard LaTeX `article` or IOP LaTeX class (`iopart.cls`), with standard packages (`amsmath`, `amssymb`, `graphicx`, `booktabs`, `hyperref`, `cite`/`natbib`).
* **Equations and Math:** Standard LaTeX math syntax; consistent operator definitions and notation.

---

## 6. Open Access Policy and Article Processing Charge (APC)
* **Publication Model:** Fully Gold Open Access.
* **Licence:** Creative Commons Attribution (CC BY 4.0) licence upon publication.
* **Article Processing Charge (APC):** Standard APC is **£2,500** (GBP).
* **Discounts and Waivers:**
  * 25% discount for IOP member society members.
  * Institutional Transformative Agreements: IOP Publishing maintains agreements with hundreds of institutions globally covering 100% of APC costs.
  * Need-based waivers are available for corresponding authors from low- and lower-middle-income countries through Research4Life.

---

## 7. Research Data Policy
* **IOP Policy Level:** MLST operates under IOP's **Level 2 / Open Data** policy.
* **Requirements:**
  * A formal **Data Availability Statement (DAS)** is mandatory in the manuscript.
  * Raw benchmark data, processed partitions, and experimental outputs must be made accessible in a publicly available repository or via standard archival repositories.
* **Implementation in this Study:**
  * The study relies exclusively on the publicly accessible Wisconsin Diagnostic Breast Cancer (WDBC) benchmark dataset originating from the UCI Machine Learning Repository / Wolberg et al. (1995) and distributed through `scikit-learn`.
  * All derived experiment tables, fold partitions, metrics, and generated figures are publicly preserved in the project repository frozen at release `v1.0.0`.

---

## 8. Code Availability Policy
* **Policy:** IOP strongly encourages the sharing of code, scripts, and software artifacts essential for reproducing published results.
* **Implementation in this Study:**
  * A formal **Code Availability Statement** is included.
  * Full source code (`src/svm_vs_qsvm`), execution pipeline scripts (`scripts/`), tests (`tests/`), and execution logs are tracked in the public git repository and tagged at `v1.0.0`.

---

## 9. Supplementary Material Rules
* Electronic Supplementary Material (ESM) is accepted and published online alongside the accepted paper.
* Supplementary materials should contain non-essential but scientifically valuable corroborative data, such as:
  * Full hyperparameter search grids and fold-level selections.
  * Extended sample-size scaling tables ($N \in \{50, 100, 150, 200, 300, 455\}$).
  * Detailed runtime complexity breakdowns and environment profiling.
  * Supplementary diagnostic plots (paired differences, ROC curves).

---

## 10. Reference and Citation Guidelines
* **Style:** Numbered Vancouver style or standard author-year citation style. Numeric citation format (`[1]`, `[2]`) is standard for IOP LaTeX submissions.
* **Integrity:** Every cited work must have a verified entry in the `.bib` file with complete author list, title, journal/venue, volume, pages, year, and DOI.
* **Preprints:** arXiv preprints are permitted as citations where formally relevant, but peer-reviewed journal/conference citations are prioritized.

---

## 11. Mandatory Author Declarations
1. **Author Contributions:** Statement of author roles (e.g., using CRediT taxonomy).
2. **Funding Declaration:** Disclosure of all funding sources supporting the research.
3. **Competing Interests / Conflicts of Interest:** Explicit declaration of any financial or non-financial conflicts.
4. **Ethics Approval / Biomedical Research Statement:** Clarification that the research uses existing open-access benchmark data and did not involve prospective human participants or direct animal experimentation.
5. **Data and Code Availability Statements:** Embedded within the back matter.
