# Independent Read-Only Audit Handoff

Prepared 12 September 2026. This document supplies factual provenance for a different auditor. It does not recommend acceptance or submission.

## Repository state

- **Current validated scientific HEAD at handoff preparation:** `4dca177798739227d5c2b22e3a0ddcd2922a7729`
- **Methodology correction commit:** `f4c8418` — `fix(methodology): fully nest QSVC architecture and C selection`
- **Manuscript remediation commit:** `4dca177798739227d5c2b22e3a0ddcd2922a7729` — `docs(paper): remediate manuscript after nested QSVC correction`
- **Historical release:** `v1.0.0`
- **Proposed corrected release:** `v1.1.0` (not tagged or created)

The handoff file is added in a subsequent documentation-only commit so it can contain the exact remediation hash. An auditor should run `git rev-parse HEAD` to identify the checkout containing this file and use the remediation hash above as the validated scientific/package baseline.

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
- **Main PDF:** `paper/mlst/manuscript.pdf` — 20 A4 pages
- **Supplementary source:** `paper/mlst/supplementary/supplementary_material.tex`
- **Supplementary PDF:** `paper/mlst/supplementary/supplementary_material.pdf` — 4 A4 pages
- **AI disclosure audit:** `paper/ai_disclosure_audit.md`
- **Primary disclosure location:** Acknowledgments in the main manuscript; mirrored in the Markdown source and author declarations, with concise submission metadata.

Both PDFs were rebuilt with Tectonic and inspected page by page. No clipping, unresolved references, duplicate disclosure, or overfull boxes were found. The main PDF contains the author name Sina Qasempour, affiliation Independent Researcher, Iran, email `qasempoursina@gmail.com`, and ORCID `0009-0006-8853-6740`.

## Validation results

- **Full test suite:** PASS — 29/29 tests (`29 passed in 51.87s`) using `.venv/Scripts/python.exe`, Python 3.12.14.
- **Repository validation:** PASS — `python scripts/validate_project.py`; its embedded suite also passed 29/29 and the frozen validation manifest was preserved.
- **MLST verification:** PASS — `python scripts/verify_mlst_submission.py`; file completeness, author metadata, citations, corrected numerical authority, and methodological-language checks passed.
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

No new scientific experiment was run during manuscript remediation. Historical `v1.0.0` artifacts remain preserved. No push, tag, GitHub release, archival upload, journal submission, or APC action has been performed. The appropriate next state is **READY FOR INDEPENDENT AUDIT**; the independent auditor must reach its own conclusions.
