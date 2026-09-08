# Pre-Submission Scientific Revision Checklist

**Manuscript:** A Controlled Empirical Comparison of Classical and Quantum Kernel SVMs for Breast Cancer Classification  
**Target Release:** `v1.0.0` Frozen Canonical Benchmark  
**Date:** September 2026  
**Auditor:** Antigravity Scientific Peer Review Panel  

---

## 1. BLOCKING Revisions (Must Be Corrected Before Any Journal Submission)

These items represent scientific, theoretical, or statistical inaccuracies that would trigger immediate rejection or major critique by expert reviewers:

* [x] **[BLOCKING-1] Clarify Hilbert State Space vs. Operator Feature Space Dimensionality (Section 11)**
  * *Issue:* The manuscript currently states that statevectors reside in a $2^2=4$ or $2^4=16$ dimensional Hilbert space while reporting effective ranks of $7.35$ and $96.49$. Without mathematical explanation, effective ranks exceeding $2^n$ appear contradictory.
  * *Correction:* Explicitly define the fidelity kernel as an inner product in the density-operator feature space $\mathcal{B}(\mathcal{H}) \cong \mathcal{H} \otimes \mathcal{H}^*$, which has dimensionality $(2^n)^2 = 4^n$ ($16$ for 2Q, $256$ for 4Q). Explain that effective ranks of $7.35 \le 16$ and $96.49 \le 256$ are mathematically legitimate and descriptive of spectral entropy in this operator space.
  * *Location:* `paper/manuscript.md` (Section 11, lines 257–260).

* [x] **[BLOCKING-2] Soften Kernel Concentration Causal Claims (Section 8 & Section 15)**
  * *Issue:* Text attributing performance collapse solely to "exponential kernel concentration" overstates the empirical findings. The study evaluated only $n \in \{2, 4\}$ and depths $1$ to $3$, which cannot prove an asymptotic concentration theorem.
  * *Correction:* Adopt strictly conservative terminology: "concentration-like behavior," "geometry consistent with concentration phenomena," and "changes predicted by kernel concentration theory." Remove assertions claiming proof of exponential concentration.
  * *Location:* `paper/manuscript.md` (Section 8, line 191; Section 15.2, lines 339–340).

* [x] **[BLOCKING-3] Qualify Inferential Statistics and Bootstrap Intervals (Section 14)**
  * *Issue:* Non-parametric bootstrap intervals $[+0.0388, +0.0977]$ must not be presented as evidence of formal statistical significance when the underlying sample consists of only 5 overlapping splits with a minimum Wilcoxon $p = 0.0625$ ($p_{\text{Holm}} = 0.1875$).
  * *Correction:* Designate bootstrap intervals throughout the text as "exploratory split-level percentile bootstrap intervals." State clearly that the 5 random splits share ~60% of training data and do not constitute independent experimental replicates. Maintain the finding as "consistent descriptive superiority" rather than "statistically significant classical superiority."
  * *Location:* `paper/manuscript.md` (Section 14, lines 310–330; Abstract; Conclusion).

* [x] **[BLOCKING-4] Eliminate Asymptotic Claims Inferred from 2Q→4Q Runtimes (Section 13)**
  * *Issue:* Runtimes jumping from $0.226$s to $0.660$s for statevector simulation must not be described as proving exponential scaling.
  * *Correction:* Clarify that the ~2.9x wall-clock increase reflects classical statevector linear algebra across two specific dimensions ($2^2=4$ to $2^4=16$), which illustrates simulation overhead but cannot establish asymptotic complexity.
  * *Location:* `paper/manuscript.md` (Section 13, lines 302–307).

* [x] **[BLOCKING-5] Reiterate Secondary Metric Status for Accuracy and ROC-AUC (Section 10 & 14)**
  * *Issue:* Only Malignant F1 was pre-specified as the primary inferential endpoint. Accuracy, Precision, Recall, and ROC-AUC are secondary descriptive metrics.
  * *Correction:* Ensure secondary metrics are never characterized with the term "statistically significant."
  * *Location:* `paper/manuscript.md` (Section 10, lines 232–236; Section 14).

---

## 2. IMPORTANT Revisions (Substantially Strengthens Peer Review Defense)

These items enhance scholarly rigor, clarity of contribution, and protect against critical reviewer skepticism:

* [x] **[IMPORTANT-1] Add Explicit "1.1 Summary of Contributions" to Introduction (Section 1)**
  * *Issue:* The Introduction currently ends with broad statements without an enumerated summary of contributions.
  * *Correction:* Add a structured subsection clearly itemizing the 6 core methodological and empirical contributions (leakage-free nested protocol, multi-seed paired robustness, feature-map ablation, sample-size scaling, operator space CKA analysis, and transparent negative result).
  * *Location:* `paper/manuscript.md` (Section 1.1).

* [x] **[IMPORTANT-2] Clarify Centered Kernel Alignment (CKA) Interpretation (Section 12)**
  * *Issue:* Low CKA in 4Q ($\approx 0.338$) must not be interpreted as a "superior representation."
  * *Correction:* State explicitly that lower alignment indicates a *more distinct similarity metric*, but emphasize that this geometric departure failed to improve classification boundaries.
  * *Location:* `paper/manuscript.md` (Section 12, lines 276–278).

* [x] **[IMPORTANT-3] Strengthen Biomedical Scope Disclaimers (Section 4 & 16)**
  * *Issue:* Using cancer terminology risks reviewers misconstruing the work as an unvalidated clinical tool.
  * *Correction:* Reiterate that this study is strictly a methodological machine learning benchmark using a classical diagnostic dataset and does not establish clinical validity.
  * *Location:* `paper/manuscript.md` (Section 4, line 83; Section 16, line 365).

* [x] **[IMPORTANT-4] Abstract Optimization for Word Count and Focus (Abstract)**
  * *Issue:* The abstract should be concise (~180–250 words) and balanced, avoiding hype while clearly reporting the negative result, statistical limits, and runtime observations.
  * *Correction:* Review and tighten the abstract to ~220 words covering motivation, methods, core metrics, statistical constraints, and conclusions.
  * *Location:* `paper/manuscript.md` (Section Abstract, line 12).

* [x] **[IMPORTANT-5] Explicit Discussion of Why Classical SVM Won (Section 15.1)**
  * *Issue:* The discussion should deeply explain the inductive bias match between continuous FNA descriptors and classical RBF kernels.
  * *Correction:* Expand Section 15.1 to elaborate on the geometry of the WDBC dataset and the optimal inductive bias of RBF kernels.
  * *Location:* `paper/manuscript.md` (Section 15.1).

---

## 3. OPTIONAL Revisions (Post-Acceptance / Future Work Extensions)

These items are desirable enhancements that are not strictly required for initial journal submission:

* [ ] **[OPTIONAL-1] Trainable Quantum Kernels (Kernel Target Alignment)**
  * Evaluate parameterized feature maps where rotation angles are optimized to align with labels prior to SVM dual solving. (Acknowledged as Future Work).
* [ ] **[OPTIONAL-2] Physical QPU Noise Benchmarking**
  * Execute a subset of kernel matrix elements on an actual superconducting or ion-trap QPU to measure shot noise and gate infidelity. (Acknowledged as Future Work).
* [ ] **[OPTIONAL-3] External Biomedical Cohort Validation**
  * Evaluate the same protocol on independent breast cancer datasets (e.g., METABRIC, TCGA) or other disease domains. (Acknowledged as Future Work).
