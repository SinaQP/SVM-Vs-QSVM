# Rules for this research project

- Preserve existing notebook work and user changes. Keep `svm_vs_qsvm_setup.ipynb` as the main research entry point; avoid unrelated restructuring.
- Keep each research phase within the user's requested scope. Do not start hardware, noise, dataset, feature-map, or paper-writing extensions without a request.
- Treat malignant label 0 as the positive class for precision, recall, F1, and ROC-AUC. Orient decision scores accordingly.
- Preserve outer seeds `[42, 123, 456, 789, 2026]` and stratified 80/20 splits. Never use outer-test scores or predictions to select hyperparameters or the classical comparator.
- Fit all preprocessing on the applicable training partition only. During inner CV, refit StandardScaler, PCA, and quantum MinMaxScaler inside every fold; quantum kernels must be specific to that fold.
- Predefine search spaces, selection metrics, numerical tie rules, statistical comparison families, and bootstrap seeds before evaluation. Persist every candidate/fold result, selected configuration, and outer result.
- Align statistical comparisons by identical seed. Report paired effects and uncertainty, small-sample limitations, overlapping-split dependence, and any reuse of test data in earlier research decisions. Do not claim equivalence from a nonsignificant test.
- Distinguish CPU SVM cost, exact statevector kernel simulation cost, and historical ComputeUncompute circuit-pair cost. Simulation time is not quantum-hardware time.
- Make claims only from measured results. Avoid unsupported causal explanations or universal claims about quantum advantage.
- Execute the notebook sequentially after implementation; verify result completeness, reproducibility, and rendered figures. Record failed runs honestly and retain useful failure details.
- Use focused validation for consequential numerical logic and leakage protections. Do not add unrelated dependencies or tests.
- Do not delegate to sub-agents unless explicitly requested by the user.
- Return a concise results report and a proposed commit message; do not create a Git commit unless asked.
