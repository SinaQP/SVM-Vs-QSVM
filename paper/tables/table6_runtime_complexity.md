# Table 6: Computational Cost, Runtime, and Complexity Scaling

Execution time benchmarks measured per outer train/test evaluation ($N_{\text{train}}=455, N_{\text{test}}=114$) on consumer x86_64 hardware. Runtimes denote sample mean $\pm$ sample standard deviation across outer splits ($n=5$). `total_runtime` includes preprocessing, classifier fit, and prediction; QSVC additionally includes exact statevector generation and train/test Gram products. Inner search and kernel diagnostics are excluded.

| Pipeline Stage / Model Architecture | Execution Environment | Qubits | Mean Runtime (s) | Runtime Std (s) | Relative Cost vs Classical Linear | Theoretical Computational Complexity | Memory Footprint Complexity |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| **Linear SVM — PCA 2** | Scikit-Learn LibSVM (CPU) | 0 | **0.0048** | 0.0007 | $1.0\times$ (Ref) | Data/cache dependent; commonly $\mathcal{O}(dN_{tr}^2)$ to $\mathcal{O}(dN_{tr}^3)$ | Data plus implementation-dependent kernel cache |
| **RBF SVM — PCA 2** | Scikit-Learn LibSVM (CPU) | 0 | **0.0072** | 0.0024 | $1.5\times$ | Same SVC bounds; pairwise RBF construction adds feature-distance work | Data plus implementation-dependent kernel cache |
| **Linear SVM — PCA 4** | Scikit-Learn LibSVM (CPU) | 0 | **0.0083** | 0.0061 | $1.7\times$ | Data/cache dependent; commonly $\mathcal{O}(dN_{tr}^2)$ to $\mathcal{O}(dN_{tr}^3)$ | Data plus implementation-dependent kernel cache |
| **RBF SVM — PCA 4** | Scikit-Learn LibSVM (CPU) | 0 | **0.0071** | 0.0019 | $1.5\times$ | Same SVC bounds; pairwise RBF construction adds feature-distance work | Data plus implementation-dependent kernel cache |
| **QSVC — PCA 2 / 2Q** | Exact Statevector Matrix Engine (CPU) | 2 | **0.2181** | 0.0096 | $\sim 45\times$ | Gram products: $\mathcal{O}((N_{tr}^2+N_{te}N_{tr})2^q)$, then precomputed-kernel SVC | Train plus test kernels: 2,071,160 bytes |
| **QSVC — PCA 4 / 4Q** | Exact Statevector Matrix Engine (CPU) | 4 | **0.5846** | 0.0257 | $\sim 71\times$ | Same operation-count form with larger $q$ | Train plus test kernels: 2,071,160 bytes |
| *Historical 2Q QSVC (ComputeUncompute)* | Local circuit-pair sampler (CPU) | 2 | *120.5* | 15.2 | $\sim 25,000\times$ | $\mathcal{O}(N_{tr}^2+N_{te}N_{tr})$ local circuit-pair evaluations | Train plus test Gram arrays |
| *Historical 4Q QSVC (ComputeUncompute)* | Local circuit-pair sampler (CPU) | 4 | *455.0* | 40.0 | $\sim 55,000\times$ | $\mathcal{O}(N_{tr}^2+N_{te}N_{tr})$ local circuit-pair evaluations | Train plus test Gram arrays |

*Note: Classical and historical `ComputeUncompute` timings come from `results/final/final_runtime_summary.csv`; corrected final QSVC timings come from `results/corrected_nested/qsvc_outer_test_summary.csv`. These CPU-simulation regimes are separate and neither is a physical-QPU timing. The 2,071,160-byte value is combined training- and test-kernel storage.*
