# Pre-Submission Checklist: Machine Learning: Science and Technology (MLST)

**Manuscript:** *A Controlled Empirical Comparison of Classical and Quantum Kernel SVMs for Breast Cancer Classification*
**Target journal:** *Machine Learning: Science and Technology* (IOP Publishing)
**Article type:** Paper (Original Research Paper; author to confirm in the portal)
**Status date:** September 2026
**Research provenance:** historical release `v1.0.0` (frozen); corrected nested checkpoint `f4c8418`

## Status Summary

| Classification | Count | Meaning |
| :--- | :---: | :--- |
| **READY** | 29 | Verified from repository evidence, manuscript sources, compiled PDFs, or automated checks. |
| **NEEDS USER REVIEW** | 3 | Requires the author's judgment or confirmation in the submission portal. |
| **BLOCKING** | 0 | No unresolved scientific, numerical, methodological, citation, disclosure, packaging, or build issue. |

## Scientific and Methodological Integrity

- [x] **READY — Leakage protection:** `StandardScaler`, PCA, quantum `MinMaxScaler`, and Gram matrices are fitted or computed within the relevant training partition.
- [x] **READY — Endpoint orientation:** malignant label 0 is the predefined positive class for precision, recall, F1, and ROC-AUC.
- [x] **READY — Comparator fairness:** classical Linear/RBF selection and QSVC regularization use inner cross-validation within each outer training split.
- [x] **READY — Corrected QSVC selection:** feature-map architecture and $C$ are jointly selected by inner-only CV before each outer-test evaluation; prior Phase 9 outer-test ablation is retained only as exploratory provenance.
- [x] **READY — Study-level adaptivity disclosure:** reuse of the dataset and five outer partitions during exploratory development is disclosed; the corrected procedure is not presented as independent confirmatory validation.
- [x] **READY — Scaling-study separation:** fixed `C=1`, RBF `gamma='scale'`, and QSVC `reps=1, full` settings are distinguished from the inner-selected canonical comparison.
- [x] **READY — Paired statistics:** exact two-sided Wilcoxon results, Holm adjustment, paired differences, and 5/5 directional wins match frozen records.
- [x] **READY — Small-sample limits:** `n=5`, overlapping split dependence, minimum attainable exact two-sided p-value, and exploratory bootstrap intervals are stated.
- [x] **READY — Quantum scope:** exact CPU statevector simulation, historical local `ComputeUncompute`, and physical-QPU execution are explicitly separated.
- [x] **READY — Complexity and storage:** QSVC Gram costs, data-dependent LibSVM bounds, runtime scope, and combined train-plus-test kernel storage are correctly qualified.
- [x] **READY — Claim discipline:** conclusions are bounded to WDBC, PCA 2/4, the evaluated ZZ feature maps, the recorded software stack, and the observed splits; no clinical or generalized quantum-advantage claim is made.

## Manuscript and Submission Artifacts

- [x] **READY — Source synchronization:** `paper/manuscript.md` and `paper/mlst/manuscript.tex` agree on methods, results, figure order, limitations, and conclusions.
- [x] **READY — Bibliography:** 35 cited keys resolve against 36 bibliography entries; no unresolved manuscript citation keys remain.
- [x] **READY — Main figures:** five primary figures are present, legible, correctly numbered, and described conservatively.
- [x] **READY — Supplement:** extended sample-size, complexity, and diagnostic material is synchronized with the frozen CSV files.
- [x] **READY — Main PDF:** rebuilt successfully; 20 pages visually inspected page by page with no clipping or unresolved references.
- [x] **READY — Supplementary PDF:** rebuilt successfully; 4 pages visually inspected page by page with no clipping or unresolved references.
- [x] **READY — Cover letter:** within the 500--800-word target, journal-specific, numerically accurate, and free of unsupported novelty or clinical claims.
- [x] **READY — Availability statements:** data and code availability text identifies the public WDBC source, repository, release tag, and validation path.
- [x] **READY — Review records:** numerical, citation, novelty, scientific-review, reviewer-simulation, and paper-notes files reflect the final audit.

## Author and Administrative Information

- [x] **READY — Author:** Sina Qasempour; single-author attribution is consistent.
- [x] **READY — Correspondence:** `qasempoursina@gmail.com` is consistent across submission artifacts.
- [x] **READY — ORCID:** `0009-0006-8853-6740` is consistent across submission artifacts.
- [x] **READY — Affiliation:** Independent Researcher, Iran; no unsupported institutional department is claimed.
- [x] **READY — Declarations:** funding, conflict-of-interest, ethics/biomedical, and CRediT statements are present and internally consistent.
- [x] **READY — Generative-AI disclosure:** the Acknowledgments name OpenAI Codex (GPT-5.6 Sol) and Google Antigravity (3.8 Flash), describe the confirmed activity scope, distinguish programmatic results/figures from conversational outputs, retain human responsibility, and assign no AI authorship.
- [ ] **NEEDS USER REVIEW — Final PDF read-through:** the author should read both rendered PDFs once in their normal PDF viewer and confirm names, equations, tables, captions, and page flow before upload.
- [ ] **NEEDS USER REVIEW — Portal metadata:** confirm the portal's current article-type label, subject categories, keywords, and any required classification fields.
- [ ] **NEEDS USER REVIEW — Submission attestations:** confirm originality, author agreement, disclosure, data/code availability, and any journal-specific legal attestations at submission time.

## Automated and Repository Validation

- [x] **READY — Unit/regression tests:** 29/29 tests pass in the declared project virtual environment.
- [x] **READY — Repository validator:** all six stages of `scripts/validate_project.py` pass, including frozen-artifact integrity.
- [x] **READY — Submission verifier:** file completeness, author metadata, citation resolution, and numerical consistency all pass in `scripts/verify_mlst_submission.py`.

## Blocking Issues

**BLOCKING — none.** No historical experiment was rerun, no frozen historical result was regenerated, and no submission was performed during this review. An independent read-only audit remains required before submission.
