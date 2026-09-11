# Supplementary Material: A Controlled Empirical Comparison of Classical and Quantum Kernel SVMs for Breast Cancer Classification

**Target Venue:** *Machine Learning: Science and Technology* (IOP Publishing)  
**Author:** Sina Qasempour (Independent Researcher, Iran; qasempoursina@gmail.com; ORCID: https://orcid.org/0009-0006-8853-6740)  
**Repository Release:** `v1.0.0` ([https://github.com/SinaQP/SVM-Vs-QSVM](https://github.com/SinaQP/SVM-Vs-QSVM))  
**Primary Endpoint:** Malignant Class F1 Score (`pos_label=0`)

---

## Supplementary Section S1: Extended Sample-Size Scaling Evaluation

Models were trained on nested subsets $N_{\text{train}} \in \{50, 100, 200, 300, 455\}$ with preprocessing pipelines (`StandardScaler`, `PCA`, `MinMaxScaler`) independently refit on each subset and evaluated on fixed outer test partitions ($N_{\text{test}}=114$). All learning curves use fixed classifier settings: $C=1$ for every SVC, `gamma='scale'` for RBF, and `reps=1`, full entanglement for QSVC. They are separate from the inner-selected canonical comparison.

### Table S1: Complete Sample-Size Scaling Results ($n=5$ Splits, Mean ± SD)

| $N_{\text{train}}$ | Model Architecture | Family | Representation | Qubits | Accuracy | Precision | Recall | Malignant F1 | ROC-AUC | Runtime (s) |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **50** | Linear SVM | Classical | PCA 2 | 0 | 0.9333 ± 0.0354 | 0.8726 ± 0.0699 | 0.9667 ± 0.0271 | **0.9157 ± 0.0402** | 0.9874 ± 0.0087 | 0.0026 ± 0.0023 |
| 50 | RBF SVM | Classical | PCA 2 | 0 | 0.9263 ± 0.0282 | 0.9006 ± 0.0603 | 0.9048 ± 0.0532 | 0.9008 ± 0.0353 | 0.9839 ± 0.0072 | 0.0019 ± 0.0005 |
| 50 | QSVC (reps=1, full) | Quantum | PCA 2 | 2 | 0.8246 ± 0.0387 | 0.8242 ± 0.0957 | 0.6762 ± 0.0643 | **0.7398 ± 0.0531** | 0.8850 ± 0.0484 | 0.0766 ± 0.0287 |
| 50 | Linear SVM | Classical | PCA 4 | 0 | 0.9316 ± 0.0353 | 0.8857 ± 0.0893 | 0.9476 ± 0.0261 | **0.9128 ± 0.0395** | 0.9894 ± 0.0090 | 0.0017 ± 0.0005 |
| 50 | RBF SVM | Classical | PCA 4 | 0 | 0.9421 ± 0.0295 | 0.9197 ± 0.0607 | 0.9286 ± 0.0558 | 0.9222 ± 0.0385 | 0.9864 ± 0.0060 | 0.0019 ± 0.0004 |
| 50 | QSVC (reps=1, full) | Quantum | PCA 4 | 4 | 0.7263 ± 0.0716 | 0.6931 ± 0.1444 | 0.4095 ± 0.2146 | **0.4994 ± 0.2110** | 0.7636 ± 0.1082 | 0.1690 ± 0.0059 |
| **100** | Linear SVM | Classical | PCA 2 | 0 | 0.9474 ± 0.0175 | 0.9311 ± 0.0454 | 0.9286 ± 0.0412 | **0.9287 ± 0.0227** | 0.9884 ± 0.0067 | 0.0014 ± 0.0001 |
| 100 | RBF SVM | Classical | PCA 2 | 0 | 0.9246 ± 0.0237 | 0.9086 ± 0.0585 | 0.8905 ± 0.0686 | 0.8966 ± 0.0317 | 0.9849 ± 0.0092 | 0.0020 ± 0.0002 |
| 100 | QSVC (reps=1, full) | Quantum | PCA 2 | 2 | 0.8614 ± 0.0190 | 0.8679 ± 0.0647 | 0.7429 ± 0.0391 | **0.7983 ± 0.0207** | 0.9214 ± 0.0101 | 0.0779 ± 0.0095 |
| 100 | Linear SVM | Classical | PCA 4 | 0 | 0.9421 ± 0.0288 | 0.9246 ± 0.0675 | 0.9238 ± 0.0488 | **0.9222 ± 0.0355** | 0.9890 ± 0.0074 | 0.0015 ± 0.0001 |
| 100 | RBF SVM | Classical | PCA 4 | 0 | 0.9386 ± 0.0139 | 0.9256 ± 0.0380 | 0.9095 ± 0.0639 | 0.9155 ± 0.0217 | 0.9884 ± 0.0044 | 0.0020 ± 0.0003 |
| 100 | QSVC (reps=1, full) | Quantum | PCA 4 | 4 | 0.7947 ± 0.0332 | 0.8059 ± 0.0713 | 0.6048 ± 0.1722 | **0.6733 ± 0.0978** | 0.8628 ± 0.0326 | 0.2149 ± 0.0222 |
| **200** | Linear SVM | Classical | PCA 2 | 0 | 0.9421 ± 0.0159 | 0.9008 ± 0.0237 | 0.9476 ± 0.0310 | **0.9234 ± 0.0213** | 0.9867 ± 0.0079 | 0.0017 ± 0.0002 |
| 200 | RBF SVM | Classical | PCA 2 | 0 | 0.9316 ± 0.0157 | 0.9157 ± 0.0451 | 0.9000 ± 0.0391 | 0.9066 ± 0.0202 | 0.9864 ± 0.0045 | 0.0023 ± 0.0003 |
| 200 | QSVC (reps=1, full) | Quantum | PCA 2 | 2 | 0.8877 ± 0.0144 | 0.8821 ± 0.0521 | 0.8095 ± 0.0753 | **0.8406 ± 0.0259** | 0.9453 ± 0.0115 | 0.1102 ± 0.0065 |
| 200 | Linear SVM | Classical | PCA 4 | 0 | 0.9579 ± 0.0157 | 0.9432 ± 0.0262 | 0.9429 ± 0.0213 | **0.9429 ± 0.0210** | 0.9910 ± 0.0029 | 0.0018 ± 0.0003 |
| 200 | RBF SVM | Classical | PCA 4 | 0 | 0.9509 ± 0.0159 | 0.9311 ± 0.0382 | 0.9381 ± 0.0398 | 0.9337 ± 0.0216 | 0.9907 ± 0.0047 | 0.0024 ± 0.0001 |
| 200 | QSVC (reps=1, full) | Quantum | PCA 4 | 4 | 0.8579 ± 0.0287 | 0.8532 ± 0.0598 | 0.7476 ± 0.0686 | **0.7943 ± 0.0440** | 0.9298 ± 0.0148 | 0.3117 ± 0.0191 |
| **300** | Linear SVM | Classical | PCA 2 | 0 | 0.9439 ± 0.0268 | 0.9118 ± 0.0589 | 0.9429 ± 0.0361 | **0.9258 ± 0.0328** | 0.9892 ± 0.0038 | 0.0019 ± 0.0002 |
| 300 | RBF SVM | Classical | PCA 2 | 0 | 0.9333 ± 0.0133 | 0.9242 ± 0.0403 | 0.8952 ± 0.0494 | 0.9080 ± 0.0191 | 0.9864 ± 0.0047 | 0.0030 ± 0.0006 |
| 300 | QSVC (reps=1, full) | Quantum | PCA 2 | 2 | 0.9158 ± 0.0260 | 0.9193 ± 0.0448 | 0.8476 ± 0.0598 | **0.8807 ± 0.0388** | 0.9651 ± 0.0130 | 0.1466 ± 0.0062 |
| 300 | Linear SVM | Classical | PCA 4 | 0 | 0.9596 ± 0.0078 | 0.9441 ± 0.0240 | 0.9476 ± 0.0310 | **0.9453 ± 0.0112** | 0.9943 ± 0.0019 | 0.0019 ± 0.0001 |
| 300 | RBF SVM | Classical | PCA 4 | 0 | 0.9544 ± 0.0144 | 0.9493 ± 0.0444 | 0.9286 ± 0.0376 | 0.9377 ± 0.0188 | 0.9936 ± 0.0037 | 0.0031 ± 0.0003 |
| 300 | QSVC (reps=1, full) | Quantum | PCA 4 | 4 | 0.8877 ± 0.0259 | 0.8725 ± 0.0539 | 0.8190 ± 0.0598 | **0.8429 ± 0.0351** | 0.9489 ± 0.0156 | 0.4012 ± 0.0229 |
| **455** | Linear SVM | Classical | PCA 2 | 0 | 0.9474 ± 0.0152 | 0.9152 ± 0.0444 | 0.9476 ± 0.0261 | **0.9302 ± 0.0182** | 0.9897 ± 0.0026 | 0.0028 ± 0.0004 |
| 455 | RBF SVM | Classical | PCA 2 | 0 | 0.9439 ± 0.0159 | 0.9339 ± 0.0411 | 0.9143 ± 0.0271 | 0.9233 ± 0.0202 | 0.9864 ± 0.0040 | 0.0036 ± 0.0003 |
| 455 | QSVC (reps=1, full) | Quantum | PCA 2 | 2 | 0.9123 ± 0.0224 | 0.9313 ± 0.0269 | 0.8238 ± 0.0706 | **0.8726 ± 0.0376** | 0.9697 ± 0.0141 | 0.1996 ± 0.0103 |
| 455 | Linear SVM | Classical | PCA 4 | 0 | 0.9632 ± 0.0157 | 0.9493 ± 0.0344 | 0.9524 ± 0.0376 | **0.9501 ± 0.0211** | 0.9952 ± 0.0030 | 0.0027 ± 0.0001 |
| 455 | RBF SVM | Classical | PCA 4 | 0 | 0.9579 ± 0.0200 | 0.9448 ± 0.0436 | 0.9429 ± 0.0361 | 0.9430 ± 0.0259 | 0.9944 ± 0.0035 | 0.0037 ± 0.0001 |
| 455 | QSVC (reps=1, full) | Quantum | PCA 4 | 4 | 0.9053 ± 0.0423 | 0.8748 ± 0.0767 | 0.8762 ± 0.0832 | **0.8721 ± 0.0556** | 0.9581 ± 0.0227 | 0.5590 ± 0.0483 |

---

## Supplementary Section S2: Computational Complexity and Execution Profiling

`total_runtime` includes preprocessing, classifier fitting, and prediction; QSVC additionally includes exact statevector generation and both training and test Gram products. Inner-search and kernel-diagnostic time are excluded.

### Table S2: Execution Time, Computational Complexity, and Storage Footprint

| Pipeline Stage / Model Architecture | Platform / Implementation | Qubits | Mean Runtime (s) | Runtime Std (s) | Relative Cost | Time Complexity | Memory Complexity |
| :--- | :--- | :---: | :---: | :---: | :---: | :--- | :--- |
| **Linear SVM — PCA 2** | Scikit-Learn LibSVM (CPU) | 0 | **0.0048** | 0.0007 | $1.0\times$ (Ref) | Data/cache dependent; commonly $\mathcal{O}(dN_{tr}^2)$ to $\mathcal{O}(dN_{tr}^3)$ | Data plus implementation-dependent cache |
| **RBF SVM — PCA 2** | Scikit-Learn LibSVM (CPU) | 0 | **0.0072** | 0.0024 | $1.5\times$ | Same SVC bounds; pairwise RBF construction adds feature-distance work | Data plus implementation-dependent cache |
| **Linear SVM — PCA 4** | Scikit-Learn LibSVM (CPU) | 0 | **0.0083** | 0.0061 | $1.7\times$ | Data/cache dependent; commonly $\mathcal{O}(dN_{tr}^2)$ to $\mathcal{O}(dN_{tr}^3)$ | Data plus implementation-dependent cache |
| **RBF SVM — PCA 4** | Scikit-Learn LibSVM (CPU) | 0 | **0.0071** | 0.0019 | $1.5\times$ | Same SVC bounds; pairwise RBF construction adds feature-distance work | Data plus implementation-dependent cache |
| **QSVC — PCA 2 / 2Q** | Vectorized CPU Statevector Engine | 2 | **0.2257** | 0.0232 | $\sim 47\times$ | $\mathcal{O}((N_{tr}^2+N_{te}N_{tr})2^q)$ Gram products, then precomputed-kernel SVC | Train plus test kernels: 2,071,160 bytes |
| **QSVC — PCA 4 / 4Q** | Vectorized CPU Statevector Engine | 4 | **0.6599** | 0.0863 | $\sim 80\times$ | Same operation-count form with larger $q$ | Train plus test kernels: 2,071,160 bytes |
| *Historical 2Q QSVC (ComputeUncompute)* | Local circuit-pair sampler | 2 | *120.5* | 15.2 | $\sim 25,000\times$ | $\mathcal{O}(N_{tr}^2+N_{te}N_{tr})$ local circuit-pair evaluations | Train plus test Gram arrays |
| *Historical 4Q QSVC (ComputeUncompute)* | Local circuit-pair sampler | 4 | *455.0* | 40.0 | $\sim 55,000\times$ | $\mathcal{O}(N_{tr}^2+N_{te}N_{tr})$ local circuit-pair evaluations | Train plus test Gram arrays |

The two simulator regimes are reported separately. Neither is a physical-QPU timing, and no fixed hardware shot budget is inferred.

---

## Supplementary Section S3: Supplementary Diagnostic Figures

### Figure S1: Paired Split-Level F1 Differences
![Figure S1: Paired Split-Level F1 Differences](final_paired_f1_differences.png)
*Figure S1: Distribution of paired differences $\Delta = \text{F1}_{\text{Classical}} - \text{F1}_{\text{QSVC}}$ across five outer test splits. Classical models maintain an empirical advantage on 5 out of 5 splits in both PCA 2 and PCA 4.*

### Figure S2: ROC-AUC Comparison
![Figure S2: Outer Test ROC-AUC Comparison](final_roc_auc_comparison.png)
*Figure S2: Mean receiver operating characteristic area under curve (ROC-AUC) comparing classical and quantum models across 2-qubit and 4-qubit representations.*
