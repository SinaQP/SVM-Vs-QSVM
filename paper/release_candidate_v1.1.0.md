# Release Candidate Plan: v1.1.0

**Release purpose:** Methodological correction and submission-ready reproducibility update.  
**Previous release:** `v1.0.0`  
**Proposed release:** `v1.1.0`  
**State:** Draft plan only; no tag, archival release, or upload has been created.

## Scope

Release `v1.1.0` will add the fully nested QSVC evaluation introduced at methodology checkpoint `f4c8418`. For every predefined outer split, QSVC repetition count, entanglement topology, and $C$ are jointly selected using only fold-local inner-cross-validation data. The frozen configuration is then refitted on the full outer-training partition and evaluated once on the outer test partition.

The corrected nested procedure selected the same effective configurations as the historical report and reproduced its final predictive metrics within numerical precision. The correction changes the evidentiary basis for the final models, not the observed headline result. It also makes explicit that the outer-test ablation is exploratory and not a model-selection stage.

Historical release `v1.0.0` remains preserved. This update is additive; it does not rewrite the frozen historical experiment outputs or imply fabrication, retraction, or replacement of the underlying dataset.

## Key changes

- Fully nested QSVC architecture and $C$ selection.
- Outer-test-isolated final model selection with fold-local preprocessing and Gram-matrix construction.
- Corrected nested selection, prediction, metric, statistical, and validation artifacts.
- Clear separation of exploratory feature-map ablation and fixed-setting learning curves from the authoritative final comparison.
- Revised manuscript, supplementary material, tables, declarations, metadata, and reproducibility documentation.
- Refreshed citation and reference-integrity audits.
- Truthful generative-AI disclosure naming OpenAI Codex (GPT-5.6 Sol) and Google Antigravity (3.8 Flash).
- Expanded tests and submission-validation coverage.

## Intended release contents

- Source and configuration: `corrected_nested.py`, `scripts/run_corrected_nested.py`, other tracked research source, and `configs/*.yaml`.
- Tests and validation: `tests/test_corrected_nested.py`, the existing test suite, `scripts/validate_project.py`, and `scripts/verify_mlst_submission.py`.
- Corrected authority layer: every tracked file under `results/corrected_nested/`.
- Classical authority layer: `results/selected_classical_comparators.csv`, `results/tuned_outer_test_results.csv`, and supporting classical tuning records already tracked in the repository.
- Historical artifacts: the unchanged tracked records under `results/final/` and related exploratory outputs, retained for provenance.
- Publication package: `paper/manuscript.md`, `paper/mlst/manuscript.tex`, `paper/mlst/manuscript.pdf`, supplementary sources and PDF, bibliography files, tables, figures, declarations, metadata, and cover-letter materials.
- Reproducibility and audit documentation, including `paper/corrected_result_provenance.md`, `paper/ai_disclosure_audit.md`, citation/reference audits, validation checklists, these release documents, and the independent-audit handoff.

## Exclusions

The release must exclude `.venv/`, `env/`, `venv/`, `tmp/`, Python caches and bytecode, `.pytest_cache/`, notebook checkpoints, IDE metadata, OS metadata, local reproduction scratch output, secrets or credentials, and transient LaTeX files (`*.aux`, `*.bbl`, `*.blg`, `*.log`, `*.out`).

## Pre-release gates

- Independent read-only scientific audit completed by a different auditor.
- Full project tests, project validation, MLST package verification, corrected-artifact hash/row validation, numerical consistency, and PDF visual inspection all pass on the intended release commit.
- The author performs the final manuscript read-through and confirms submission metadata and declarations.
- Release contents are checked for ignored/local files and secrets.
- Only after these gates: create tag/release `v1.1.0`, archive it if desired, update persistent identifiers, and then consider journal submission.

No push, tag, GitHub release, archive upload, or journal submission is part of this plan's preparation.
