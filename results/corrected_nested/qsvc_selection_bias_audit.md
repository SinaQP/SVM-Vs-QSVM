# QSVC selection-bias audit

## Finding

The historical canonical QSVC estimate contains **outer-test reuse for architecture selection**. Phase 9 evaluated the investigated ZZ-feature-map architectures on the five outer test partitions and recorded outer-test accuracy, malignant-class F1, and ROC-AUC in `results/quantum_feature_map_ablation.csv`. The reported Phase 9 comparison favored `reps=1`; for 4Q it also favored full entanglement. Those observations informed the fixed `reps=1, full` canonical architecture used later.

## Exact leakage pathway

1. `configs/phase9_ablation.yaml` prespecified `reps in {1,2,3}` and `entanglement in {linear,full}`. `scripts/run_ablation.py` fitted preprocessing on each outer-training partition, but then transformed the corresponding outer test features, fitted a QSVC at fixed `C=1`, and called `score_predictions(y_test, ...)` for every architecture. Thus architecture comparisons included outer-test malignant F1 and other outer-test metrics.
2. The Phase 9 aggregate results showed the highest mean tested F1 at `reps=1` for both representations and at full entanglement for 4Q. For 2Q, linear and full are algebraically equivalent because both contain the single available qubit pair; the historical files nevertheless contain both spellings.
3. In `phase11.py`, `model_name()` and `statevectors()` hard-coded `reps=1, full`. The quantum `inner_search()` varied only `C`. Therefore the Phase 9 test-informed architecture propagated into every Phase 11 inner search, outer refit, prediction, and saved result.
4. `phase12.py` read the Phase 11 outputs and labeled `reps=1, full` as the canonical tuned QSVC in the final synthesis. The manuscript methodology likewise states that the architecture was selected from the Phase 9 outer-split ablation and that only `C` was later selected within inner folds.

## Why inner tuning of C did not remove the bias

Inner cross-validation in Phase 11 correctly isolated the selection of `C`, and its preprocessing was fold-local. It did not re-select feature-map depth or entanglement. Conditioning the Phase 11 procedure on an architecture already chosen after inspecting the same outer-test outcomes leaves a **test-informed architecture selection** path. Later tuning of a different hyperparameter cannot make that earlier choice independent of the test data. The historical canonical QSVC estimate is consequently susceptible to **selection-induced optimism**; the direction and magnitude must be measured rather than assumed.

## Classical comparator audit criterion

The classical comparator is reusable only if its model family (linear versus RBF), `C`, and RBF `gamma` reproduce exactly from inner-fold malignant F1 within each outer-training partition, without outer-test ranking. The corrected pipeline performs this verification against the raw Phase 11 candidate/fold table before reusing the saved classical outer results.

## Corrected procedural boundary

For every predefined seed, the corrected procedure jointly selects repetitions, nonredundant entanglement topology, and `C` using five-fold stratified inner CV on outer-training data only. StandardScaler, PCA, and the `[0, pi]` MinMaxScaler are refitted on each inner-training fold. All ten seed/representation selections are frozen and persisted before any corrected outer-test evaluation begins. Each selected procedure is then refitted on the complete outer-training partition and evaluated once on its outer test partition.

For 2Q, only the canonical `linear` spelling is evaluated: `linear` and `full` generate the same sole pair and are not independent architectures. For 4Q, both are evaluated. Selection uses mean inner malignant-class F1 only; numerical ties within `1e-12` are resolved by lower repetitions, linear before full, then smaller `C`.

## Remaining study-level adaptivity

The corrected algorithm removes direct test-set involvement from architecture and hyperparameter selection. It does not erase the broader history of exploratory work. **The corrected nested analysis removes direct test-set involvement in architecture and hyperparameter selection, but remains a post hoc reanalysis of a dataset and partition set previously examined during exploratory development.** This procedural correction therefore should not automatically be described as fully independent confirmatory evidence.

