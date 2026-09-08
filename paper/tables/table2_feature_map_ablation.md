# Table 2: Quantum Feature-Map Ablation Study (Phase 9)

Controlled ablation across circuit repetitions ($\text{reps} \in \{1, 2, 3\}$), entanglement topologies ($\text{'linear'}$ vs $\text{'full'}$), and qubit dimensions ($q \in \{2, 4\}$) across five outer splits ($n=60$ quantum evaluations). Metrics denote sample mean $\pm$ sample standard deviation ($n=5$).

| Qubits ($q$) | Circuit Reps | Entanglement Topology | Outer Malignant F1 | Outer ROC-AUC | Outer Accuracy | Mean Off-Diagonal Fidelity | Off-Diagonal Std | Gram Effective Rank | Statevector Simulation (s) |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 2 | 1 | Linear | 0.8726 ± 0.0376 | 0.9697 ± 0.0141 | 0.9123 ± 0.0224 | 0.3244 ± 0.0071 | 0.2908 ± 0.0039 | 7.35 ± 0.21 | 0.212 ± 0.012 |
| 2 | 1 | Full | 0.8726 ± 0.0376 | 0.9697 ± 0.0141 | 0.9123 ± 0.0224 | 0.3244 ± 0.0071 | 0.2908 ± 0.0039 | 7.35 ± 0.21 | 0.214 ± 0.011 |
| 2 | 2 | Linear | 0.8327 ± 0.0283 | 0.9414 ± 0.0240 | 0.8842 ± 0.0169 | 0.4311 ± 0.0302 | 0.2795 ± 0.0033 | 6.33 ± 0.50 | 0.375 ± 0.023 |
| 2 | 2 | Full (Baseline) | 0.8327 ± 0.0283 | 0.9414 ± 0.0240 | 0.8842 ± 0.0169 | 0.4311 ± 0.0302 | 0.2795 ± 0.0033 | 6.33 ± 0.50 | 0.373 ± 0.022 |
| 2 | 3 | Linear | 0.8012 ± 0.0352 | 0.9204 ± 0.0250 | 0.8596 ± 0.0215 | 0.4818 ± 0.0249 | 0.2677 ± 0.0015 | 5.90 ± 0.40 | 0.495 ± 0.035 |
| 2 | 3 | Full | 0.8012 ± 0.0352 | 0.9204 ± 0.0250 | 0.8596 ± 0.0215 | 0.4818 ± 0.0249 | 0.2677 ± 0.0015 | 5.90 ± 0.40 | 0.471 ± 0.029 |
| 4 | 1 | Linear | 0.7957 ± 0.0688 | 0.9263 ± 0.0303 | 0.8596 ± 0.0345 | 0.0818 ± 0.0041 | 0.1306 ± 0.0072 | 70.29 ± 4.94 | 0.407 ± 0.031 |
| **4** | **1** | **Full (Selected)** | **0.8721 ± 0.0556** | **0.9581 ± 0.0227** | **0.9053 ± 0.0423** | **0.0961 ± 0.0032** | **0.1015 ± 0.0046** | **96.49 ± 5.41** | **0.575 ± 0.045** |
| 4 | 2 | Linear | 0.7192 ± 0.0859 | 0.8935 ± 0.0442 | 0.8140 ± 0.0423 | 0.0829 ± 0.0035 | 0.1057 ± 0.0046 | 95.80 ± 5.39 | 0.703 ± 0.062 |
| 4 | 2 | Full (Baseline) | 0.6816 ± 0.0590 | 0.8546 ± 0.0482 | 0.7789 ± 0.0364 | 0.0811 ± 0.0015 | 0.0845 ± 0.0019 | 123.66 ± 2.65 | 1.026 ± 0.094 |
| 4 | 3 | Linear | 0.7055 ± 0.0493 | 0.8700 ± 0.0311 | 0.7965 ± 0.0413 | 0.0977 ± 0.0025 | 0.1080 ± 0.0031 | 93.63 ± 4.01 | 1.006 ± 0.088 |
| 4 | 3 | Full | 0.5403 ± 0.0523 | 0.7872 ± 0.0340 | 0.7228 ± 0.0295 | 0.0778 ± 0.0018 | 0.0770 ± 0.0017 | 137.43 ± 2.83 | 1.475 ± 0.125 |

*Note: For 2 qubits, linear and full entanglement topologies are algebraically identical as there is only one interaction edge $(0,1)$. In 4 qubits, full entanglement includes all 6 pairs. Source data from `results/final/final_feature_map_summary.csv`.*
