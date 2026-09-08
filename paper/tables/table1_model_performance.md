# Table 1: Canonical Outer-Test Model Performance Comparison

Canonical performance across the five frozen outer test splits (`seeds = [42, 123, 456, 789, 2026]`, 80/20 stratified split, $N_{\text{train}}=455, N_{\text{test}}=114$). Metrics are reported as sample mean $\pm$ sample standard deviation ($n=5$). Malignant label 0 is designated as the primary positive class for Precision, Recall, F1, and ROC-AUC.

| Model | Representation | Qubits | Kernel / Feature Map Architecture | Accuracy | Precision | Recall | Malignant F1 | ROC-AUC | Runtime (s) |
| :--- | :---: | :---: | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Classical SVM (Comparator)** | **PCA 2** | **0** | **Linear / RBF (Inner-CV Selected)** | **0.9509 ± 0.0048** | **0.9257 ± 0.0172** | **0.9429 ± 0.0213** | **0.9339 ± 0.0068** | **0.9866 ± 0.0074** | **0.0065 ± 0.0029** |
| Tuned Linear SVM | PCA 2 | 0 | Linear ($C \in \{0.1, 1.0\}$) | 0.9509 ± 0.0078 | 0.9266 ± 0.0318 | 0.9429 ± 0.0213 | 0.9341 ± 0.0093 | 0.9894 ± 0.0030 | 0.0048 ± 0.0007 |
| Tuned RBF SVM | PCA 2 | 0 | RBF ($C \in \{10, 100\}, \gamma \in \{0.01, 0.1, \text{scale}\}$) | 0.9456 ± 0.0096 | 0.9245 ± 0.0182 | 0.9286 ± 0.0238 | 0.9263 ± 0.0133 | 0.9810 ± 0.0119 | 0.0072 ± 0.0024 |
| **Tuned QSVC (Canonical)** | **PCA 2** | **2** | **ZZ Feature Map (reps=1, full, $C \in \{10, 100\}$)** | **0.9070 ± 0.0237** | **0.9064 ± 0.0457** | **0.8381 ± 0.0832** | **0.8678 ± 0.0388** | **0.9644 ± 0.0244** | **0.2257 ± 0.0232** |
| **Classical SVM (Comparator)** | **PCA 4** | **0** | **Linear / RBF (Inner-CV Selected)** | **0.9632 ± 0.0157** | **0.9570 ± 0.0184** | **0.9429 ± 0.0464** | **0.9493 ± 0.0227** | **0.9941 ± 0.0039** | **0.0088 ± 0.0060** |
| Tuned Linear SVM | PCA 4 | 0 | Linear ($C \in \{0.01, 0.1, 1.0, 100.0\}$) | 0.9684 ± 0.0100 | 0.9671 ± 0.0255 | 0.9476 ± 0.0391 | 0.9565 ± 0.0143 | 0.9952 ± 0.0029 | 0.0083 ± 0.0061 |
| Tuned RBF SVM | PCA 4 | 0 | RBF ($C \in \{10, 100\}, \gamma \in \{0.01, \text{scale}\}$) | 0.9561 ± 0.0139 | 0.9434 ± 0.0244 | 0.9381 ± 0.0398 | 0.9401 ± 0.0198 | 0.9935 ± 0.0045 | 0.0071 ± 0.0019 |
| **Tuned QSVC (Canonical)** | **PCA 4** | **4** | **ZZ Feature Map (reps=1, full, $C=1.0$)** | **0.9053 ± 0.0423** | **0.8748 ± 0.0767** | **0.8762 ± 0.0832** | **0.8721 ± 0.0556** | **0.9581 ± 0.0227** | **0.6599 ± 0.0863** |

*Note: Source data from `results/final/final_model_comparison.csv`. Classical comparator is selected per seed via 5-fold inner cross-validation without access to test data.*
