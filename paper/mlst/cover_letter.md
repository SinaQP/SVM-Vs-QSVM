# Cover Letter

**To:** The Editors, *Machine Learning: Science and Technology*
**Date:** September 2026
**Subject:** Original Research Paper — *A Controlled Empirical Comparison of Classical and Quantum Kernel SVMs for Breast Cancer Classification*

Dear Editors,

Please consider the manuscript **“A Controlled Empirical Comparison of Classical and Quantum Kernel SVMs for Breast Cancer Classification”** for publication as an Original Research Paper in *Machine Learning: Science and Technology*.

Quantum kernels provide a principled way to use quantum state overlaps as similarity measures for classical machine-learning tasks. Their empirical value, however, can only be assessed against carefully selected classical comparators and under evaluation protocols that isolate preprocessing and hyperparameter selection from held-out testing. The submitted study addresses this methodological need through a controlled comparison of linear and radial-basis-function support vector classifiers with quantum support vector classifiers (QSVCs) on the Wisconsin Diagnostic Breast Cancer benchmark.

The experiment uses five predefined stratified 80/20 splits of the 569-sample dataset. Within every outer-training set, standardization, principal-component reduction, quantum input scaling, and quantum Gram matrices are recomputed fold-locally. Five-fold inner cross-validation selects the classical model family and hyperparameters and jointly selects QSVC repetition count, entanglement topology, and regularization parameter. Each frozen choice is then refitted on the full outer-training partition and evaluated once on the outer test set. Quantum kernels are evaluated exactly by classical CPU statevector simulation. Complementary exploratory analyses examine feature-map sensitivity, fixed-hyperparameter sample-size behavior, kernel geometry, and measured execution cost; they do not select the final architecture.

Under these conditions, the inner-selected classical comparator had higher malignant-class F1 on all five matched splits. Mean F1 was 0.934 versus 0.868 in two dimensions and 0.949 versus 0.872 in four dimensions. The two-sided exact Wilcoxon tests yielded raw p-values of 0.0625 and Holm-adjusted p-values of 0.1875. We therefore present the paired results as consistent descriptive evidence, not statistically significant population-level confirmation. The manuscript discloses that the outer splits overlap and that, although final selection is outer-test-isolated, the work remains a post hoc analysis of a dataset and partitions examined during development.

The architecture and geometry analyses add context beyond a model leaderboard. Within the tested four-qubit full-entanglement maps, malignant-class F1 decreased from approximately 0.872 at one repetition to 0.540 at three repetitions. We describe this association conservatively as concentration-like behavior rather than proof of an asymptotic concentration mechanism. Centered kernel alignment with the selected RBF kernels was lower for the four-qubit comparison than for the two-qubit comparison (0.338 versus 0.573), yet the more divergent kernel geometry did not improve predictive performance. Fixed-hyperparameter learning curves likewise showed no small-data QSVC advantage in this setting. Runtime results are explicitly limited to the recorded CPU statevector implementation and are not presented as estimates of physical quantum-hardware performance.

The contribution is not a new quantum algorithm or a universal claim about quantum learning. It is a reproducible negative-result benchmark that integrates fully nested model selection, paired multi-split reporting, feature-map sensitivity, sample-size analysis, kernel-geometry diagnostics, and computational provenance while making the statistical and experimental limitations visible. We believe this combination is relevant to MLST readers working on quantum machine learning, empirical methodology, and reproducible comparisons of emerging computational technologies.

The code, historical result tables, corrected nested-selection outputs, per-split records, configurations, figures, and validation scripts are available at [https://github.com/SinaQP/SVM-Vs-QSVM](https://github.com/SinaQP/SVM-Vs-QSVM). Release `v1.0.0` preserves the historical benchmark and checkpoint `f4c8418` records the corrected authority layer; a new archival release containing both is required before submission. The manuscript and supplementary material identify the benchmark as non-clinical and distinguish exact statevector simulation from physical QPU execution.

This research received no external funding. I declare no conflict of interest. The study used a publicly available benchmark dataset and did not recruit human participants or collect new clinical data. The author should confirm originality, exclusive submission status, and approval of the final version immediately before submission.

Thank you for considering this work.

Sincerely,

**Sina Qasempour**
Independent Researcher, Iran
Corresponding author
Email: qasempoursina@gmail.com
ORCID: https://orcid.org/0009-0006-8853-6740
Repository: https://github.com/SinaQP/SVM-Vs-QSVM
