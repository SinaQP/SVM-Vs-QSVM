# Cover Letter Framing Notes

**Manuscript:** *A Controlled Empirical Comparison of Classical and Quantum Kernel SVMs for Breast Cancer Classification*
**Target journal:** *Machine Learning: Science and Technology*
**Author:** Sina Qasempour, Independent Researcher, Iran

## Framing rationale

The letter presents the work as a controlled, reproducible case study rather than a new algorithm or a universal verdict on quantum machine learning. Its publication value rests on the combination of nested hyperparameter selection, paired evaluation, architecture ablation, fixed-hyperparameter learning curves, kernel-geometry diagnostics, transparent simulation cost, and a fully auditable negative result.

The principal result is reported numerically, but the inferential boundary appears immediately beside it: $n=5$, overlapping splits, raw exact Wilcoxon $p=0.0625$, and Holm-adjusted $p=0.1875$. Final QSVC architecture and $C$ are selected within the nested inner folds. Because the dataset and partitions were examined during exploratory development, the study remains post hoc rather than confirmatory.

The letter distinguishes the sample-size study from the canonical comparison. The learning curves use fixed settings ($C=1$ for all SVCs, `gamma='scale'` for RBF, and `reps=1`, full entanglement for QSVC). This prevents the $N=455$ learning-curve values from being confused with inner-selected final-model values.

## Claims intentionally avoided

- No claim that quantum kernels are generally inferior or that quantum advantage is impossible.
- No “first,” “state-of-the-art,” or new-algorithm claim.
- No claim of statistical significance from five dependent split pairs.
- No claim that feature-map depth caused the performance decrease or that this experiment proves asymptotic kernel concentration.
- No claim that lower CKA identifies a better or intrinsically nonclassical representation.
- No claim that exact statevector runtime estimates physical-QPU runtime or establishes an asymptotic scaling law.
- No clinical-performance, deployment, or decision-support claim.
- No direct performance ranking against breast-cancer studies that use different data modalities or validation protocols.

## Defensible novelty statement

The strongest defensible contribution is the integrated design: a WDBC benchmark combining fold-local preprocessing, fully nested classical and QSVC model selection, paired multi-split reporting, exploratory ZZ-feature-map ablation, fixed-hyperparameter sample-size analysis, and effective-rank/CKA diagnostics. It identifies a concrete setting in which geometric divergence and increased circuit complexity did not produce predictive advantage, while retaining complete records for independent audit.

## Issues a human author should review

- Confirm that “Original Research Paper” is the exact article-type label offered by the current MLST submission portal.
- Confirm the originality and not-under-consideration declarations immediately before submission.
- Decide whether to mention suggested editors or reviewers; none are proposed in this package.
- Perform the final author read-through of both PDFs, verify that historical release `v1.0.0` remains accessible, and create/verify proposed archival release `v1.1.0` before submission.
