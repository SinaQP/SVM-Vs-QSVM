# Draft Release Notes: v1.1.0

**Methodological correction and submission-ready reproducibility update.** These notes are a draft and have not been published.

## What changed

The original exploratory workflow examined outer-test performance during feature-map architecture exploration. The authoritative final procedure has now been rerun so that QSVC repetition count, entanglement topology, and regularization parameter $C$ are jointly selected entirely within five-fold inner cross-validation for each outer-training partition. Preprocessing and quantum Gram matrices are recomputed fold-locally, the selected configuration is frozen, and the outer test is evaluated once.

The exploratory ablation and fixed-hyperparameter sample-size study remain available as contextual analyses, but they no longer provide the selection basis for the final QSVC comparison.

## Result

The corrected nested procedure independently selected the same effective configurations and produced predictive metrics identical to the historical report within numerical precision. The substantive conclusion is unchanged: under the evaluated WDBC, PCA 2/4, 2Q/4Q, exact-statevector, and tested ZZ-feature-map conditions, no quantum advantage was observed.

## Why release v1.1.0

Public release `v1.0.0` predates the methodological correction. Version `v1.1.0` is proposed so the corrected model-selection procedure, authoritative artifacts, and remediated journal package can be archived together before submission while the historical release remains preserved.

## Included updates

- New `results/corrected_nested/` search records, frozen selections, outer-test predictions and metrics, corrected paired comparisons, provenance reports, and validation manifests.
- Corrected nested implementation, runner, configuration, and expanded regression/methodology tests.
- Revised manuscript, supplementary material, tables, metadata, declarations, cover letter, and final PDFs.
- Updated methodology, results, reproducibility, numerical, citation, and reference-integrity documentation.
- Generative-AI disclosure and detailed disclosure audit.
- Updated project and MLST submission validation.

No historical `results/final/` artifacts are rewritten by this release. No tag, hosted release, archive upload, or journal submission has yet been performed.
