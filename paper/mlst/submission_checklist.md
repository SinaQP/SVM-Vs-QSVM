# Pre-Submission Checklist: Machine Learning: Science and Technology (MLST)

**Manuscript:** *A Controlled Empirical Comparison of Classical and Quantum Kernel SVMs for Breast Cancer Classification*  
**Target Journal:** *Machine Learning: Science and Technology* (IOP Publishing)  
**Article Type:** Paper (Original Research Paper)  
**Status Date:** September 2026  
**Canonical Research Release:** `v1.0.0` (Frozen)

---

## Summary of Checklist Status

| Classification | Count | Description |
| :--- | :---: | :--- |
| **READY** | 24 | Fully verified, scientifically validated, author attribution confirmed, and formatted in compliance with MLST/IOP standards. |
| **NEEDS USER INPUT** | 0 | All author, institutional, funding, ethics, and disclosure fields have been provided and verified. |
| **BLOCKING** | 0 | No blocking scientific, numerical, methodological, or repository issues exist. |

---

## 1. Scientific & Methodological Integrity (READY)

- [x] **Data Leakage Quarantine:** All preprocessing transformers (`StandardScaler`, `PCA`, `MinMaxScaler`) and quantum Gram matrices are refit strictly inside each training split. Outer test partitions ($N=114$) remain completely isolated.
- [x] **Primary Endpoint Framing:** Malignant-class F1 score (`pos_label=0`) is consistently reported as the primary inferential endpoint.
- [x] **Secondary Metrics Distinction:** Test Accuracy, Precision, Recall, and ROC-AUC are explicitly reported as descriptive indicators and not claimed as confirmatory test statistics.
- [x] **Multi-Seed Robustness:** Evaluated across 5 fixed random seeds (`[42, 123, 456, 789, 2026]`) with paired analysis.
- [x] **Statistical Significance Bounds:** No false claims of statistical significance are made; exact raw Wilcoxon $p = 0.0625$, Holm-adjusted $p = 0.1875$, discrete small-sample power limits ($n=5$), and split overlap dependence are transparently stated.
- [x] **Exploratory Bootstrap Qualification:** Percentile bootstrap intervals are explicitly labeled as exploratory split-level diagnostics.
- [x] **Operator Feature Space Formulation:** Mathematical capacity is correctly formulated in the $4^n$-dimensional density-operator feature space ($\mathcal{B}(\mathcal{H}) \cong \mathbb{C}^{2^n \times 2^n}$), not bounded by $2^n$.
- [x] **Complexity Separation:** Measured CPU wall-clock runtime is strictly separated from quantum Hilbert space dimensions, Gram matrix storage $\mathcal{O}(N^2)$, and general asymptotic complexity. No false claims of exponential scaling laws from two qubit dimensions are asserted.
- [x] **Hardware Simulation Clarification:** Classical statevector simulation is clearly distinguished from physical quantum hardware execution, accounting for shot noise, gate infidelities, and device queue latencies.
- [x] **Empirical Negative Scope:** Claims are strictly bounded to the evaluated conditions (WDBC dataset, PCA 2 and 4 dimensions, fixed ZZ feature-map family); potential quantum utility on alternative embeddings or quantum data remains open.

---

## 2. Manuscript Artifacts & Packaging (READY)

- [x] **Generic Manuscript Preserved:** `paper/manuscript.md` remains the uncorrupted, venue-neutral scientific source of truth.
- [x] **Submission Directory Created:** Standalone `paper/mlst/` directory created with complete submission structure.
- [x] **LaTeX Source Document:** `paper/mlst/manuscript.tex` created with full article structure, mathematical formulations, confirmed author metadata, and embedded tables/figures.
- [x] **Bibliography Database:** `paper/mlst/references.bib` created with all 35 verified peer-reviewed/canonical entries and 0 unresolved citation keys.
- [x] **Main Publication Figures:** 5 primary 300-DPI figures copied to `paper/mlst/figures/`:
  - `final_f1_comparison.png` (Figure 1: Malignant F1 Comparison)
  - `final_feature_map_ablation.png` (Figure 2: Feature-Map Ablation Dynamics)
  - `final_sample_size_scaling.png` (Figure 3: Sample-Size Scaling Dynamics)
  - `final_kernel_heatmaps.png` (Figure 4: Kernel Alignment Heatmaps)
  - `final_runtime_scaling.png` (Figure 5: Runtime Scaling Comparison)
- [x] **Supplementary Material:** Extended scaling and complexity tables, along with diagnostic figures (`final_paired_f1_differences.png`, `final_roc_auc_comparison.png`), compiled in `paper/mlst/supplementary/`.
- [x] **Data Availability Statement:** Formal IOP Level 2 compliant DAS created in `paper/mlst/data_availability.md` and embedded in `manuscript.tex`.
- [x] **Code Availability Statement:** Clear statement linking to public GitHub release `v1.0.0` with automated test suites and validation scripts.

---

## 3. Administrative & Author Attribution (READY)

- [x] **Author Identification:**
  - Author: Sina Qasempour
  - Affiliation: Independent Researcher, Iran (no university or institutional department affiliation)
- [x] **Corresponding Author Identification:**
  - Corresponding Author: Sina Qasempour
  - Email: `qasempoursina@gmail.com`
- [x] **ORCID Identifier (Requirement Satisfied):**
  - Verified ORCID: `https://orcid.org/0009-0006-8853-6740` (`0009-0006-8853-6740`)
- [x] **Author Contributions (CRediT):**
  - All 11 CRediT roles assigned to single author Sina Qasempour across all manuscript files
- [x] **Funding Declaration:**
  - Confirmed: *"This research received no external funding."*
- [x] **Conflicts of Interest:**
  - Confirmed: *"The author declares no conflict of interest."*
- [x] **Ethics and Biomedical Statement:**
  - Confirmed: *"This study used a publicly available benchmark dataset and did not involve the recruitment of human participants or collection of new clinical data."* (No artificial IRB exemption claimed)

---

## 4. Submission Blocking Issues (BLOCKING)

* **Current Blocking Issues:** **NONE (0)**.
* No numerical inconsistencies exist.
* No data leakage is present.
* No unverified citations exist.
* All repository unit tests pass (`23/23`).
* Empirical research remains frozen at `v1.0.0`.
