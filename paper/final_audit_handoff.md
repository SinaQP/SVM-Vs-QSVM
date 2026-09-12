# Independent Read-Only Audit Handoff

Prepared 12 September 2026. This document supplies factual provenance for a different auditor. It does not recommend acceptance or submission.

## Repository state

- **Validated package baseline before targeted remediation:** `3d1ac55277ed01e907ff577f78b36b291393a4ab`
- **Methodology correction commit:** `f4c8418` — `fix(methodology): fully nest QSVC architecture and C selection`
- **Manuscript remediation commit:** `4dca177798739227d5c2b22e3a0ddcd2922a7729` — `docs(paper): remediate manuscript after nested QSVC correction`
- **Targeted residual-reporting remediation:** `HEAD` — `docs(paper): correct residual reporting and MLST submission inconsistencies`
- **Historical release:** `v1.0.0`
- **Proposed corrected release:** `v1.1.0` (not tagged or created)

Because a commit cannot embed its own hash, `HEAD` above identifies the targeted remediation commit containing this handoff; an auditor should run `git rev-parse HEAD` and verify the stated commit message. The earlier hashes remain the scientific and manuscript provenance chain.

## Targeted residual corrections

- Replaced the stale 47--80-times runtime sentence with ratios computed from the authoritative mean timings: 45.112153 for 2Q and 70.511848 for 4Q, reported as approximately 45 and 71 times.
- Replaced the false monotonic sample-size statement with the recorded 2Q behavior: F1 peaks at 0.880692 for $N=300$ and declines to 0.872555 for $N=455$.
- Replaced “outer cross-validation splits” with “repeated stratified outer holdout splits,” removed the unneeded uncited `thanasilp2023subtleties` record, and narrowed the Hubregtsen statement to the source's weak-correlation finding.
- Updated both reviewer PDFs to a 12-point base size under current official IOP formatting guidance. Dense supplementary tables now use dedicated landscape pages.
- Recorded Benchmark as the intended MLST article type under the journal's current definition, subject to portal availability and editorial classification.
- Added artifact-backed verifier checks and four regression tests for the two audited reporting-error classes.

## Authority map

- **Authoritative final QSVC selection, predictions, metrics, timings, paired comparisons, and validation:** `results/corrected_nested/`
- **Authoritative classical selected choices:** `results/selected_classical_comparators.csv`
- **Authoritative classical per-seed outer-test results:** selected rows in `results/tuned_outer_test_results.csv`
- **Authoritative classical aggregate summary:** classical rows in `results/final/final_model_comparison.csv`
- **Historical exploratory/frozen outputs:** `results/final/`, including `final_feature_map_summary.csv`, `final_sample_size_summary.csv`, `final_kernel_comparison.csv`, and historical runtime/result summaries. Phase 9 ablation and fixed-setting scaling are contextual analyses, not the final QSVC-selection source.
- **Corrected provenance narrative:** `paper/corrected_result_provenance.md`
- **Historical integrity check:** `git diff v1.0.0 -- results/final` returned no changes.

## Final publication artifacts

- **Main source:** `paper/mlst/manuscript.tex`
- **Main PDF:** `paper/mlst/manuscript.pdf` — 23 A4 pages
- **Supplementary source:** `paper/mlst/supplementary/supplementary_material.tex`
- **Supplementary PDF:** `paper/mlst/supplementary/supplementary_material.pdf` — 7 A4 pages (portrait text/figures and landscape data tables)
- **AI disclosure audit:** `paper/ai_disclosure_audit.md`
- **Primary disclosure location:** Acknowledgments in the main manuscript; mirrored in the Markdown source and author declarations, with concise submission metadata.

Both PDFs were rebuilt with Tectonic at a 12-point base size and inspected page by page. No clipping, unresolved references, duplicate disclosure, underfull/overfull box warnings, or unreadable tables were found. The main PDF contains the author name Sina Qasempour, affiliation Independent Researcher, Iran, email `qasempoursina@gmail.com`, and ORCID `0009-0006-8853-6740`.

## Validation results

- **Full test suite:** PASS — 33/33 tests (`33 passed in 28.67s`) using `.venv/Scripts/python.exe`, Python 3.12.14.
- **Repository validation:** PASS — `python scripts/validate_project.py`; all six stages passed, its embedded suite passed 33/33, and the frozen validation manifest was preserved.
- **MLST verification:** PASS — `python scripts/verify_mlst_submission.py`; file completeness, author metadata, citations (35 cited/35 stored, none unresolved or unused), corrected numerical authority, methodological language, authoritative runtime ratios, and non-monotonic sample-size wording checks passed.
- **Corrected nested stored-artifact validation:** PASS — 11/11 recorded output hashes matched; 1,125 inner candidate/fold rows, 10 selected configurations/outer evaluations, and 1,140 predictions were present; implementation and configuration hashes matched; zero failed corrected runs.
- **Method controls covered by tests/manifest:** outer-test inputs cannot enter selection, all selections are frozen before outer evaluation, preprocessing is refitted on each inner-training fold, the 2Q grid is nonredundant, and deterministic tie-breaking is enforced.
- **Final numerical consistency:** PASS — 0 discrepancies.

Validated headline values:

| Quantity | Value |
|---|---:|
| QSVC2 accuracy / F1 / ROC-AUC | 0.907018 / 0.867760 / 0.964352 |
| QSVC4 accuracy / F1 / ROC-AUC | 0.905263 / 0.872060 / 0.958135 |
| PCA2 classical minus QSVC mean F1; W; raw p; Holm p | +0.066169; 0; 0.0625; 0.1875 |
| PCA4 classical minus QSVC mean F1; W; raw p; Holm p | +0.077191; 0; 0.0625; 0.1875 |

## Generative-AI disclosure facts

The author-confirmed tools are OpenAI Codex (GPT-5.6 Sol) and Google Antigravity (3.8 Flash). The detailed activity inventory, current official IOP policy source/access date, computational-result provenance distinction, figure classification, human responsibility, and final disclosure text are in `paper/ai_disclosure_audit.md`. Scientific figures are conventional Python/Matplotlib plots of stored numerical artifacts; no scientific figure was found to have been directly synthesized by a generative-image model.

## Known limitations for independent assessment

- One WDBC benchmark dataset.
- Five overlapping repeated stratified holdout splits.
- Post hoc study-level adaptivity despite corrected outer-test-isolated final selection.
- Limited inferential resolution at $n=5$; split-level Wilcoxon and bootstrap summaries are exploratory and dependent.
- Exact noiseless CPU statevector simulation only.
- No physical QPU execution.
- No new quantum algorithm, classifier, theorem, or dataset.

## Scope boundary

No new scientific experiment was run during targeted remediation. Historical `v1.0.0` artifacts remain preserved. No push, tag, GitHub release, archival upload, journal submission, or APC action has been performed. The appropriate next state is **READY FOR FINAL READ-ONLY RE-AUDIT**; the independent auditor must reach its own conclusions.
