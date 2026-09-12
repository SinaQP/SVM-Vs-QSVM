# Corrected Result Provenance

## Authority boundary

- Historical exploratory and Phase 9--13 artifacts remain immutable under `results/final/` and related historical paths.
- The authoritative source for final QSVC outer-test metrics, predictions, selected configurations, inner-search records, and paired statistical comparisons is `results/corrected_nested/`.
- Methodological correction checkpoint: `f4c8418` (`fix(methodology): fully nest QSVC architecture and C selection`).

## Selection lineage

For each seed (42, 123, 456, 789, 2026), the outer training partition alone generated five inner folds. Standardization, PCA, quantum range scaling, state preparation, and Gram matrices were fitted/recomputed per inner fold. Repetition count, entanglement topology (where distinct), and $C$ were selected jointly by mean malignant-class F1 with deterministic tie-breaking. The frozen choice was refitted on all 455 outer-training observations before one evaluation of the 114-observation outer test set.

The selected 2Q values were `(reps=1, linear, C=100)`, `(1, linear, 100)`, `(1, linear, 1)`, `(1, linear, 10)`, and `(1, linear, 10)` in seed order. Linear and full are algebraically equivalent in 2Q. All 4Q seeds selected `(reps=1, full, C=1)`.

## Authoritative outputs

| Claim family | Source |
|---|---|
| Aggregate corrected QSVC metrics | `qsvc_outer_test_summary.csv` |
| Per-seed corrected metrics | `qsvc_outer_test_results.csv` |
| Predictions and label orientation | `qsvc_outer_test_predictions.csv` |
| Frozen configurations | `qsvc_selected_configurations.csv` |
| Full inner search | `qsvc_inner_search_raw.csv` |
| Paired statistics | `corrected_statistical_comparison.csv` |
| Historical numerical comparison | `corrected_vs_historical.csv` |
| Machine-readable validation | `corrected_nested_validation.json` |

Aggregate accuracy/F1/ROC-AUC are 0.907018/0.867760/0.964352 for 2Q and 0.905263/0.872060/0.958135 for 4Q. These equal the historical reported values to numerical precision. Corrected classical-minus-QSVC mean paired F1 differences are +0.066169 (PCA 2) and +0.077191 (PCA 4), with the inferential caveats recorded in the manuscript.

## Reproducibility boundary

The notebook preserves the historical executed narrative and is not the authority for corrected selection. The corrected pipeline and validation records are additive and do not rewrite notebook outputs or `results/final/`. A new archival release containing checkpoint `f4c8418` and the documentation remediation must be minted before submission; `v1.0.0` alone does not contain the corrected authority layer.
