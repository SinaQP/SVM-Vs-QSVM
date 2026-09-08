# Table 4: Kernel Geometry and Centered Kernel Alignment (CKA) Analysis

Geometric comparison of training Gram matrices ($N=455$) between seed-specific tuned Classical RBF kernels and Canonical Quantum Fidelity Kernels ($\text{reps}=1, \text{full}$) across the five outer splits.

### Summary Statistics (Mean ± SD across 5 outer splits)

| Representation / Qubits | Centered Kernel Alignment (CKA) | Frobenius Alignment | Classical RBF Effective Rank | Quantum Kernel Effective Rank | Classical RBF Off-Diagonal Mean | Quantum Kernel Off-Diagonal Mean | Classical RBF Off-Diagonal Std | Quantum Kernel Off-Diagonal Std |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **PCA 2 / 2Q** | **0.5732 ± 0.1578** | **0.8344 ± 0.0327** | 6.52 ± 3.86 | **7.35 ± 0.21** | 0.4895 ± 0.2396 | **0.3244 ± 0.0071** | 0.2816 ± 0.0504 | **0.2908 ± 0.0039** |
| **PCA 4 / 4Q** | **0.3375 ± 0.0718** | **0.7162 ± 0.0119** | 6.97 ± 5.06 | **96.49 ± 5.41** | 0.4765 ± 0.1901 | **0.0961 ± 0.0032** | 0.2512 ± 0.0298 | **0.1015 ± 0.0046** |

### Per-Seed Detailed Measurements

| Outer Seed | PCA Dims | Qubits | Selected RBF $\gamma$ | CKA Alignment | Frobenius Alignment | Classical RBF Effective Rank | Quantum Kernel Effective Rank | Quantum Off-Diag Mean | Quantum Off-Diag Std |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 42 | 2 | 2 | 0.100 | 0.7130 | 0.8580 | 10.57 | 7.47 | 0.3180 | 0.2925 |
| 123 | 2 | 2 | 0.100 | 0.7029 | 0.8579 | 10.74 | 7.26 | 0.3282 | 0.2923 |
| 456 | 2 | 2 | scale (0.0517) | 0.6321 | 0.8561 | 6.58 | 7.19 | 0.3293 | 0.2931 |
| 789 | 2 | 2 | 0.010 | 0.4410 | 0.8087 | 2.37 | 7.16 | 0.3311 | 0.2922 |
| 2026 | 2 | 2 | 0.010 | 0.3770 | 0.7912 | 2.35 | 7.64 | 0.3154 | 0.2837 |
| 42 | 4 | 4 | 0.010 | 0.3353 | 0.7153 | 3.31 | 90.76 | 0.0994 | 0.1072 |
| 123 | 4 | 4 | scale (0.0418) | 0.4202 | 0.7321 | 12.41 | 92.67 | 0.0982 | 0.1038 |
| 456 | 4 | 4 | scale (0.0418) | 0.3914 | 0.7209 | 12.49 | 96.99 | 0.0962 | 0.1010 |
| 789 | 4 | 4 | 0.010 | 0.2474 | 0.7000 | 3.33 | 104.80 | 0.0911 | 0.0947 |
| 2026 | 4 | 4 | 0.010 | 0.2933 | 0.7125 | 3.30 | 97.21 | 0.0957 | 0.1007 |

*Note: Source data from `results/final/final_kernel_comparison.csv`. Effective rank is defined as $\exp(H(p))$ where $H(p)$ is the spectral Shannon entropy of normalized eigenvalues.*
