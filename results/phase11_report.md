## Phase 11 — Executed research report

Implemented nested tuning for four classical and two fixed-map quantum configurations; all candidate/fold scores, predictions, selected configurations, diagnostics, and paired statistics are persisted.

**Nested-CV design.** Five fixed stratified 80/20 outer splits; five shuffled stratified inner folds per seed. All scalers and PCA are fitted inside each fold. Malignant label 0 is positive. All choices are frozen before Phase 11 outer evaluation. The classical comparison is an inner-selected Linear/RBF procedure per seed, so it can choose different kernels across seeds.

**Selected hyperparameters by model/seed**

| model | seed | selected_C | selected_gamma |
| --- | --- | --- | --- |
| Linear SVM — PCA 2 | 42 | 0.1000 | none |
| RBF SVM — PCA 2 | 42 | 10.0000 | 0.1 |
| QSVC — PCA 2 / 2Q (reps=1, full) | 42 | 100.0000 | none |
| Linear SVM — PCA 4 | 42 | 1.0000 | none |
| RBF SVM — PCA 4 | 42 | 100.0000 | 0.01 |
| QSVC — PCA 4 / 4Q (reps=1, full) | 42 | 1.0000 | none |
| Linear SVM — PCA 2 | 123 | 1.0000 | none |
| RBF SVM — PCA 2 | 123 | 10.0000 | 0.1 |
| QSVC — PCA 2 / 2Q (reps=1, full) | 123 | 100.0000 | none |
| Linear SVM — PCA 4 | 123 | 100.0000 | none |
| RBF SVM — PCA 4 | 123 | 10.0000 | scale |
| QSVC — PCA 4 / 4Q (reps=1, full) | 123 | 1.0000 | none |
| Linear SVM — PCA 2 | 456 | 1.0000 | none |
| RBF SVM — PCA 2 | 456 | 100.0000 | scale |
| QSVC — PCA 2 / 2Q (reps=1, full) | 456 | 1.0000 | none |
| Linear SVM — PCA 4 | 456 | 10.0000 | none |
| RBF SVM — PCA 4 | 456 | 10.0000 | scale |
| QSVC — PCA 4 / 4Q (reps=1, full) | 456 | 1.0000 | none |
| Linear SVM — PCA 2 | 789 | 0.1000 | none |
| RBF SVM — PCA 2 | 789 | 10.0000 | 0.01 |
| QSVC — PCA 2 / 2Q (reps=1, full) | 789 | 10.0000 | none |
| Linear SVM — PCA 4 | 789 | 0.0100 | none |
| RBF SVM — PCA 4 | 789 | 100.0000 | 0.01 |
| QSVC — PCA 4 / 4Q (reps=1, full) | 789 | 1.0000 | none |
| Linear SVM — PCA 2 | 2026 | 0.1000 | none |
| RBF SVM — PCA 2 | 2026 | 10.0000 | 0.01 |
| QSVC — PCA 2 / 2Q (reps=1, full) | 2026 | 10.0000 | none |
| Linear SVM — PCA 4 | 2026 | 0.1000 | none |
| RBF SVM — PCA 4 | 2026 | 10.0000 | 0.01 |
| QSVC — PCA 4 / 4Q (reps=1, full) | 2026 | 1.0000 | none |

**Classical comparators selected using inner CV**

| seed | pca_components | model | selected_C | selected_gamma | inner_cv_f1_mean |
| --- | --- | --- | --- | --- | --- |
| 42 | 2 | Linear SVM — PCA 2 | 0.1000 | none | 0.9410 |
| 42 | 4 | Linear SVM — PCA 4 | 1.0000 | none | 0.9559 |
| 123 | 2 | Linear SVM — PCA 2 | 1.0000 | none | 0.9319 |
| 123 | 4 | Linear SVM — PCA 4 | 100.0000 | none | 0.9482 |
| 456 | 2 | RBF SVM — PCA 2 | 100.0000 | scale | 0.9319 |
| 456 | 4 | RBF SVM — PCA 4 | 10.0000 | scale | 0.9590 |
| 789 | 2 | Linear SVM — PCA 2 | 0.1000 | none | 0.9407 |
| 789 | 4 | RBF SVM — PCA 4 | 100.0000 | 0.01 | 0.9491 |
| 2026 | 2 | RBF SVM — PCA 2 | 10.0000 | 0.01 | 0.9390 |
| 2026 | 4 | Linear SVM — PCA 4 | 0.1000 | none | 0.9607 |

**Tuned outer-test results: mean ± sample SD**

| Model | accuracy | f1 | roc_auc |
| --- | --- | --- | --- |
| Linear SVM — PCA 2 | 0.9509 ± 0.0078 | 0.9341 ± 0.0093 | 0.9894 ± 0.0030 |
| RBF SVM — PCA 2 | 0.9456 ± 0.0096 | 0.9263 ± 0.0133 | 0.9810 ± 0.0119 |
| QSVC — PCA 2 / 2Q (reps=1, full) | 0.9070 ± 0.0237 | 0.8678 ± 0.0388 | 0.9644 ± 0.0244 |
| Linear SVM — PCA 4 | 0.9684 ± 0.0100 | 0.9565 ± 0.0143 | 0.9952 ± 0.0029 |
| RBF SVM — PCA 4 | 0.9561 ± 0.0139 | 0.9401 ± 0.0198 | 0.9935 ± 0.0045 |
| QSVC — PCA 4 / 4Q (reps=1, full) | 0.9053 ± 0.0423 | 0.8721 ± 0.0556 | 0.9581 ± 0.0227 |

**Did tuning change the ranking?** The ordering of individual models changed.

PCA 2: the largest classical mean F1 minus quantum mean F1 was +0.0577 before tuning and +0.0663 after tuning. This ranking description does not select the inferential comparator.
PCA 4: the largest classical mean F1 minus quantum mean F1 was +0.0780 before tuning and +0.0845 after tuning. This ranking description does not select the inferential comparator.

**Tuned versus C=1: outer-test means only**

| model | delta_accuracy | delta_f1 | delta_roc_auc | untuned_f1_rank | tuned_f1_rank |
| --- | --- | --- | --- | --- | --- |
| Linear SVM — PCA 2 | 0.0035 | 0.0039 | -0.0003 | 3 | 3 |
| Linear SVM — PCA 4 | 0.0053 | 0.0064 | -0.0001 | 1 | 1 |
| QSVC — PCA 2 / 2Q (reps=1, full) | -0.0053 | -0.0048 | -0.0054 | 5 | 6 |
| QSVC — PCA 4 / 4Q (reps=1, full) | 0.0000 | 0.0000 | 0.0000 | 6 | 5 |
| RBF SVM — PCA 2 | 0.0018 | 0.0030 | -0.0055 | 4 | 4 |
| RBF SVM — PCA 4 | -0.0018 | -0.0029 | -0.0010 | 2 | 2 |

**Paired F1 effects** (left minus right; classical minus quantum, or 2Q minus 4Q)

| comparison | mean_paired_difference | median_paired_difference | std_paired_difference | min_paired_difference | max_paired_difference |
| --- | --- | --- | --- | --- | --- |
| Classical PCA2 vs QSVC PCA2 | 0.0662 | 0.0698 | 0.0392 | 0.0235 | 0.1254 |
| Classical PCA4 vs QSVC PCA4 | 0.0772 | 0.0886 | 0.0417 | 0.0244 | 0.1237 |
| QSVC PCA2 vs QSVC PCA4 | -0.0043 | -0.0154 | 0.0317 | -0.0347 | 0.0307 |

**Wilcoxon, Holm correction, bootstrap intervals, and wins**

| comparison | wilcoxon_statistic | p_raw | p_holm | bootstrap_ci_low | bootstrap_ci_high | left_wins | right_wins | ties |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Classical PCA2 vs QSVC PCA2 | 0.0000 | 0.0625 | 0.1875 | 0.0388 | 0.0977 | 5 | 0 | 0 |
| Classical PCA4 vs QSVC PCA4 | 0.0000 | 0.0625 | 0.1875 | 0.0445 | 0.1092 | 5 | 0 | 0 |
| QSVC PCA2 vs QSVC PCA4 | 6.0000 | 0.8125 | 0.8125 | -0.0291 | 0.0201 | 2 | 3 | 0 |

- Classical PCA2 vs QSVC PCA2: exact; Exploratory: five overlapping splits do not establish independent observations.
- Classical PCA4 vs QSVC PCA4: exact; Exploratory: five overlapping splits do not establish independent observations.
- QSVC PCA2 vs QSVC PCA4: exact; Exploratory: five overlapping splits do not establish independent observations.

**Statistical-power limitation.** There are only five paired split-level observations. With five nonzero pairs, the smallest conventional two-sided exact Wilcoxon p-value is 0.0625, even when every difference has the same sign. Holm covers the three predefined F1 comparisons. Accuracy and ROC-AUC are descriptive secondary outcomes. A nonsignificant p-value is not evidence of equivalence.

The 95% pointwise percentile bootstrap intervals resample the five observed split-level differences (10,000 resamples, seed 42). They are exploratory intervals over these splits, not precise population intervals or simultaneous multiplicity-adjusted intervals. The splits reuse patients and training observations, so their differences are dependent; neither ordinary Wilcoxon assumptions nor independent-observation bootstrap coverage are established. A bootstrap interval excluding zero and a nonsignificant exact test need not agree with this very small sample.

**Research interpretation.** These comparisons concern this dataset, preprocessing, fixed feature maps, and exact simulator only. Earlier feature-map selection used the same five test splits; nested hyperparameter tuning does not erase that prior selection bias. Phase 11 avoids new test-driven selection but is not independent confirmation. No universal claim about classical superiority or quantum advantage follows.

**Computational fairness.** `fit_time` and `prediction_time` measure the classifier only; `total_runtime` also includes preprocessing and, for QSVC, statevector generation plus Gram products. `search_runtime` records inner tuning separately, and `diagnostic_time` records kernel diagnostics separately. These phase-local costs separate classical CPU SVM computation from exact statevector simulation. Simulation time is not physical-device runtime; historical ComputeUncompute timings are not pooled. The RBF and QSVC candidate grids differ in size as specified, so this is not an equal-search-budget benchmark.

**Validation and failed runs.** PASS: 1750 candidate/fold rows, 30 final evaluations, 3420 saved predictions, and 0 failed Phase 11 model runs. The separate notebook execution log records full sequential execution.

**Problems and next recommended step.** Limited power, overlapping splits, and prior feature-map selection constrain interpretation. Freeze this protocol before a future independent validation study; do not expand the present phase. Hardware, noise, new datasets/maps, trainable kernels, paper writing, and repository restructuring remain outside this phase.

Methods: [scikit-learn nested CV](https://scikit-learn.org/stable/auto_examples/model_selection/plot_nested_cross_validation_iris.html), [SciPy Wilcoxon handling of ties and zeros](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.wilcoxon.html), [QSVC precomputed kernel API](https://qiskit-community.github.io/qiskit-machine-learning/stubs/qiskit_machine_learning.algorithms.QSVC.html).
