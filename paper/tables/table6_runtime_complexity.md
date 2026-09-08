# Table 6: Computational Cost, Runtime, and Complexity Scaling

Execution time benchmarks measured per outer train/test evaluation ($N_{\text{train}}=455, N_{\text{test}}=114$) on consumer x86_64 hardware. Runtimes denote sample mean $\pm$ sample standard deviation across outer splits ($n=5$).

| Pipeline Stage / Model Architecture | Execution Environment | Qubits | Mean Runtime (s) | Runtime Std (s) | Relative Cost vs Classical Linear | Theoretical Computational Complexity | Memory Footprint Complexity |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| **Linear SVM — PCA 2** | Scikit-Learn LibSVM (CPU) | 0 | **0.0048** | 0.0007 | $1.0\times$ (Ref) | $\mathcal{O}(N_{\text{train}} \cdot d)$ to $\mathcal{O}(N_{\text{train}}^2 \cdot d)$ | $\mathcal{O}(N_{\text{train}} \cdot d)$ feature matrix |
| **RBF SVM — PCA 2** | Scikit-Learn LibSVM (CPU) | 0 | **0.0072** | 0.0024 | $1.5\times$ | $\mathcal{O}(N_{\text{train}}^2 \cdot d)$ | $\mathcal{O}(N_{\text{train}} \cdot d)$ |
| **Linear SVM — PCA 4** | Scikit-Learn LibSVM (CPU) | 0 | **0.0083** | 0.0061 | $1.7\times$ | $\mathcal{O}(N_{\text{train}} \cdot d)$ to $\mathcal{O}(N_{\text{train}}^2 \cdot d)$ | $\mathcal{O}(N_{\text{train}} \cdot d)$ feature matrix |
| **RBF SVM — PCA 4** | Scikit-Learn LibSVM (CPU) | 0 | **0.0071** | 0.0019 | $1.5\times$ | $\mathcal{O}(N_{\text{train}}^2 \cdot d)$ | $\mathcal{O}(N_{\text{train}} \cdot d)$ |
| **QSVC — PCA 2 / 2Q** | Exact Statevector Matrix Engine (CPU) | 2 | **0.2257** | 0.0232 | $\sim 47\times$ | $\mathcal{O}(N \cdot 2^q + N_{\text{train}}^2 \cdot 2^q)$ | $\mathcal{O}(N_{\text{train}}^2)$ float64 Gram (2.07 MB) |
| **QSVC — PCA 4 / 4Q** | Exact Statevector Matrix Engine (CPU) | 4 | **0.6599** | 0.0863 | $\sim 80\times$ | $\mathcal{O}(N \cdot 2^q + N_{\text{train}}^2 \cdot 2^q)$ | $\mathcal{O}(N_{\text{train}}^2)$ float64 Gram (2.07 MB) |
| *Historical 2Q QSVC (ComputeUncompute)* | Pairwise Statevector Sampler (CPU) | 2 | *120.5* | 15.2 | $\sim 25,000\times$ | $\mathcal{O}(N_{\text{train}}^2)$ circuit pair executions | $\mathcal{O}(N_{\text{train}}^2)$ float64 Gram |
| *Historical 4Q QSVC (ComputeUncompute)* | Pairwise Statevector Sampler (CPU) | 4 | *455.0* | 40.0 | $\sim 55,000\times$ | $\mathcal{O}(N_{\text{train}}^2)$ circuit pair executions | $\mathcal{O}(N_{\text{train}}^2)$ float64 Gram |

*Note: Source data from `results/final/final_runtime_summary.csv`. Exact statevector simulation evaluates mathematical inner products directly on CPU and does not account for physical quantum processor (QPU) compilation, execution latencies, readout error mitigation, or shot-noise variance.*
