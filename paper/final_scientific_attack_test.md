# Final Scientific Attack Test

Audit date: 12 September 2026. This is an adversarial repository/manuscript review, not an editorial acceptance prediction.

1. **Was the outer test used to select the final QSVC architecture? — NO.** The corrected authoritative pipeline selects repetition count, topology, and $C$ exclusively from five-fold inner CV on each outer-training set and freezes the choice before outer evaluation.
2. **Was $C$ selected without outer-test access? — YES.** It belongs to the same inner search.
3. **Was preprocessing inner-fold-local? — YES.** Standardization, PCA, MinMax scaling, statevectors, and Gram matrices are recomputed per fold.
4. **Was exploratory Phase 9 kept separate from final selection? — YES.** It is explicitly titled and described as an exploratory outer-test sensitivity analysis.
5. **Did the corrected analysis reproduce the previously reported final numbers? — YES.** `corrected_vs_historical.csv` records zero aggregate difference; corrected 2Q/4Q F1 values are 0.867760 and 0.872060.
6. **Are the five outer splits independent? — NO.** They overlap; inferential calculations are labeled exploratory and dependent.
7. **Is the study confirmatory? — NO.** Procedural selection is corrected, but the analysis remains post hoc with study-level adaptivity.
8. **Are all primary references real? — YES, after correction.** The fresh 36-entry audit found and repaired false/composite metadata.
9. **Are DOI/article mappings correct? — YES.** Final audit: zero DOI or article-number mismatch.
10. **Does every central citation support its claim? — YES, directly or with explicit qualification.** Universal, causal, and implementation-specific extrapolations were removed.
11. **Does the paper claim universal classical superiority? — NO.** The conclusion is restricted to WDBC, PCA 2/4, 2Q/4Q, exact statevectors, and tested ZZ maps.
12. **Does it claim physical-QPU runtime? — NO.** Timings are explicitly CPU statevector measurements.
13. **Is AI assistance handled according to current IOP policy? — YES.** The author-confirmed inventory names OpenAI Codex (GPT-5.6 Sol) and Google Antigravity (3.8 Flash), records the activity scope, distinguishes AI assistance from programmatic result generation, retains human responsibility, and assigns no AI authorship.

## Residual reviewer attacks

- **Incremental scope:** one small familiar dataset and no new algorithm remain the largest editorial risks. The contribution is framed as protocol integration and reproducibility, not algorithmic novelty.
- **Dependent inference:** five overlapping partitions cannot support population-level confirmation. The manuscript reports raw and Holm-adjusted $p>0.05$, labels bootstrap intervals exploratory, and states that nonsignificance does not establish equivalence.
- **Post hoc adaptivity:** corrected selection removes direct procedural test reuse but cannot make previously explored partitions independent. This is disclosed explicitly.
- **Release provenance:** `v1.0.0` predates the corrected authority layer. A new archival release is required before submission.

## Disposition

Scientific/methodological remediation: **PASS**. Submission readiness: **FAIL pending a new archival release and an independent final human audit.**
