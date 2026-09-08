# Table 3: Sample-Size Scaling Evaluation (Phase 10)

Predictive performance across nested training subsets $N_{\text{train}} \in \{50, 100, 200, 300, 455\}$ evaluated on held-out outer test partitions ($N_{\text{test}}=114$). Metrics are reported as sample mean $\pm$ sample standard deviation across the five outer random splits ($n=5$).

| $N_{\text{train}}$ | Model | Family | PCA Dims | Qubits | Accuracy | Malignant F1 Score | ROC-AUC | Runtime (s) |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **50** | Linear SVM | Classical | 2 | 0 | 0.9333 ± 0.0354 | 0.9157 ± 0.0402 | 0.9874 ± 0.0087 | 0.0026 ± 0.0023 |
| 50 | RBF SVM | Classical | 2 | 0 | 0.9263 ± 0.0282 | 0.9008 ± 0.0353 | 0.9839 ± 0.0072 | 0.0019 ± 0.0005 |
| 50 | QSVC (reps=1, full) | Quantum | 2 | 2 | 0.8246 ± 0.0387 | 0.7398 ± 0.0531 | 0.8850 ± 0.0484 | 0.0766 ± 0.0287 |
| 50 | Linear SVM | Classical | 4 | 0 | 0.9316 ± 0.0353 | 0.9128 ± 0.0395 | 0.9894 ± 0.0090 | 0.0017 ± 0.0005 |
| 50 | RBF SVM | Classical | 4 | 0 | 0.9421 ± 0.0295 | 0.9222 ± 0.0385 | 0.9864 ± 0.0060 | 0.0019 ± 0.0004 |
| 50 | QSVC (reps=1, full) | Quantum | 4 | 4 | 0.7263 ± 0.0716 | 0.4994 ± 0.2110 | 0.7636 ± 0.1082 | 0.1690 ± 0.0059 |
| **100** | Linear SVM | Classical | 2 | 0 | 0.9474 ± 0.0175 | 0.9287 ± 0.0227 | 0.9884 ± 0.0067 | 0.0014 ± 0.0001 |
| 100 | RBF SVM | Classical | 2 | 0 | 0.9246 ± 0.0237 | 0.8966 ± 0.0317 | 0.9849 ± 0.0092 | 0.0020 ± 0.0002 |
| 100 | QSVC (reps=1, full) | Quantum | 2 | 2 | 0.8614 ± 0.0190 | 0.7983 ± 0.0207 | 0.9214 ± 0.0101 | 0.0779 ± 0.0095 |
| 100 | Linear SVM | Classical | 4 | 0 | 0.9421 ± 0.0288 | 0.9222 ± 0.0355 | 0.9890 ± 0.0074 | 0.0015 ± 0.0001 |
| 100 | RBF SVM | Classical | 4 | 0 | 0.9386 ± 0.0139 | 0.9155 ± 0.0217 | 0.9884 ± 0.0044 | 0.0020 ± 0.0003 |
| 100 | QSVC (reps=1, full) | Quantum | 4 | 4 | 0.7947 ± 0.0332 | 0.6733 ± 0.0978 | 0.8628 ± 0.0326 | 0.2149 ± 0.0222 |
| **200** | Linear SVM | Classical | 2 | 0 | 0.9421 ± 0.0159 | 0.9234 ± 0.0213 | 0.9867 ± 0.0079 | 0.0017 ± 0.0002 |
| 200 | RBF SVM | Classical | 2 | 0 | 0.9316 ± 0.0157 | 0.9066 ± 0.0202 | 0.9864 ± 0.0045 | 0.0023 ± 0.0003 |
| 200 | QSVC (reps=1, full) | Quantum | 2 | 2 | 0.8877 ± 0.0144 | 0.8406 ± 0.0259 | 0.9453 ± 0.0115 | 0.1102 ± 0.0065 |
| 200 | Linear SVM | Classical | 4 | 0 | 0.9579 ± 0.0157 | 0.9429 ± 0.0210 | 0.9910 ± 0.0029 | 0.0018 ± 0.0003 |
| 200 | RBF SVM | Classical | 4 | 0 | 0.9509 ± 0.0159 | 0.9337 ± 0.0216 | 0.9907 ± 0.0047 | 0.0024 ± 0.0001 |
| 200 | QSVC (reps=1, full) | Quantum | 4 | 4 | 0.8579 ± 0.0287 | 0.7943 ± 0.0440 | 0.9298 ± 0.0148 | 0.3117 ± 0.0191 |
| **300** | Linear SVM | Classical | 2 | 0 | 0.9439 ± 0.0268 | 0.9258 ± 0.0328 | 0.9892 ± 0.0038 | 0.0019 ± 0.0002 |
| 300 | RBF SVM | Classical | 2 | 0 | 0.9333 ± 0.0133 | 0.9080 ± 0.0191 | 0.9864 ± 0.0047 | 0.0030 ± 0.0006 |
| 300 | QSVC (reps=1, full) | Quantum | 2 | 2 | 0.9158 ± 0.0260 | 0.8807 ± 0.0388 | 0.9651 ± 0.0130 | 0.1466 ± 0.0062 |
| 300 | Linear SVM | Classical | 4 | 0 | 0.9596 ± 0.0078 | 0.9453 ± 0.0112 | 0.9943 ± 0.0019 | 0.0019 ± 0.0001 |
| 300 | RBF SVM | Classical | 4 | 0 | 0.9544 ± 0.0144 | 0.9377 ± 0.0188 | 0.9936 ± 0.0037 | 0.0031 ± 0.0003 |
| 300 | QSVC (reps=1, full) | Quantum | 4 | 4 | 0.8877 ± 0.0259 | 0.8429 ± 0.0351 | 0.9489 ± 0.0156 | 0.4012 ± 0.0229 |
| **455** | Linear SVM | Classical | 2 | 0 | 0.9474 ± 0.0152 | 0.9302 ± 0.0182 | 0.9897 ± 0.0026 | 0.0028 ± 0.0004 |
| 455 | RBF SVM | Classical | 2 | 0 | 0.9439 ± 0.0159 | 0.9233 ± 0.0202 | 0.9864 ± 0.0040 | 0.0036 ± 0.0003 |
| 455 | QSVC (reps=1, full) | Quantum | 2 | 2 | 0.9123 ± 0.0224 | 0.8726 ± 0.0376 | 0.9697 ± 0.0141 | 0.2000 ± 0.0103 |
| 455 | Linear SVM | Classical | 4 | 0 | 0.9632 ± 0.0157 | 0.9501 ± 0.0211 | 0.9952 ± 0.0030 | 0.0027 ± 0.0001 |
| 455 | RBF SVM | Classical | 4 | 0 | 0.9579 ± 0.0200 | 0.9430 ± 0.0259 | 0.9944 ± 0.0035 | 0.0037 ± 0.0001 |
| 455 | QSVC (reps=1, full) | Quantum | 4 | 4 | 0.9053 ± 0.0423 | 0.8721 ± 0.0556 | 0.9581 ± 0.0227 | 0.5590 ± 0.0483 |

*Note: Source data from `results/final/final_sample_size_summary.csv`. Preprocessing (StandardScaler, PCA, quantum MinMaxScaler) is strictly fitted on each training subset $N_{\text{train}}$.*
