# Corrected Novelty and Closest-Work Matrix

## Defensible contribution

This manuscript does **not** introduce a new algorithm. Its contribution is a rigorous, reproducible benchmarking protocol and case study: fully nested classical and quantum model selection; fold-local preprocessing; five aligned outer partitions; exploratory feature-map and sample-size analyses kept separate from final selection; quantum-kernel geometry, effective-rank, and CKA diagnostics; computational profiling; dependence-aware statistical caution; and transparent correction of a discovered selection-bias issue. The result is a scoped, reproducible negative quantum-advantage benchmark for WDBC rather than a universal ranking of classical and quantum learning.

“NR” below means the source did not report the field in a form that supports a precise entry; it is used instead of inference.

| Field | Havlíček et al. 2019 | Suzuki et al. 2020 | Peters et al. 2021 | Azevedo et al. 2022 | Wang 2024 | Bowles et al. 2024 | Leither et al. 2026 | Present study |
|---|---|---|---|---|---|---|---|---|
| Dataset | Engineered synthetic classification | Synthetic tasks and WDBC | Synthetic high-dimensional data and breast-cancer subset | Full-field mammograms | Breast-cancer tabular data | 6 tasks / 160 derived datasets | Multiple oncology tabular, omics, spatial tasks | WDBC |
| Sample count | Task-specific | WDBC 569; other task-specific | Task-specific | Study-specific image cohort | Study-specific | Dataset-specific | Cohort-specific | 569 |
| Quantum model | Quantum-kernel SVM | Pauli-feature-map quantum classifier | Noisy-hardware QSVC | ResNet features + 4Q variational model | QSVM with feature selection | Multiple QML families | Multiple QML families | Exact-statevector fidelity QSVC |
| Classical baseline | Linear/RBF SVM | RBF SVM | Linear/RBF SVM | Classical transfer-learning/SVM comparators | SVM feature-selection comparators | Tuned classical ML families | AutoML/classical models | Inner-selected linear or RBF SVC |
| Preprocessing | Problem-specific | Input scaling | Standardization/PCA | Deep feature extraction/PCA | Normalization/feature selection | Dataset/model-specific | Automated/task-specific | Inner-fold StandardScaler, PCA, MinMaxScaler |
| Dimensionality reduction | No | Task-specific | PCA | PCA after ResNet | Feature selection | Dataset-specific | Dataset-specific | PCA 2 and 4 |
| Qubits | Small demonstration circuits | Task-specific small circuits | Hardware/task-specific | 4 | NR | Model-specific | Model-specific | 2 and 4 |
| Feature-map selection | Fixed demonstration map | Map design/manual study | Fixed/task-specific | Fixed ansatz | Coupled to feature selection | Varies by model | Automated/model-specific | Joint inner-CV reps/topology search |
| Hyperparameter selection | Limited/fixed | Manual/task-specific | Largely fixed | Training validation | Optimization includes feature subset | Tuned benchmark procedures | Automated optimization | Joint architecture/$C$ inner CV; classical grids |
| Seeds/splits | Limited holdout | Limited holdout | Holdout/repeated hardware runs | Holdout | Holdout | Multiple CV evaluations | Multi-fold evaluations | 5 predefined outer splits |
| Nested CV? | No | No | No | No | Not reported | Protocol-dependent | Task-dependent | Yes for authoritative comparison |
| Held-out evaluation? | Yes | Yes | Yes | Yes | Yes | Yes | Yes | One outer-test evaluation after frozen inner choice |
| Sample-size analysis? | No | No | No | No | No | Broad scale discussion | Across heterogeneous cohorts | Fixed-setting curves at 50,100,200,300,455 |
| Kernel geometry? | Fidelity demonstration | Feature-map analysis | Noise/conditioning | No | No | Not a central per-dataset analysis | Not central | Off-diagonal moments, effective rank, heatmaps |
| Statistical analysis? | Limited | Limited | Hardware uncertainty | Study-specific | Study-specific | Comparative multi-task analysis | Cross-task analysis | Paired exact Wilcoxon, Holm, exploratory interval |
| Reproducibility artifacts? | Published methods/code lineage | Published methods | Hardware implementation details | Study artifacts | Study artifacts | Benchmark code/artifacts | Framework/artifacts | Code, raw searches, predictions, configs, validators |
| Main conclusion | Quantum feature spaces can support classification and motivate hard kernels | Map design affects classification | Proof-of-concept noisy-processor learning | Hybrid breast-cancer imaging application | Feature-selection/QSVM method reported | Classical methods generally strong; design matters | No evaluated oncology quantum advantage | No advantage under evaluated WDBC conditions |
| What this manuscript adds | Fully nested WDBC comparison plus geometry and paired audit trail | Outer-test-isolated architecture selection and broader diagnostics | Separates ideal CPU timing from hardware claims | Different tabular task and kernel focus | Controls feature-map/$C$ selection and reports geometry | Deep single-dataset case study with raw per-seed provenance | More granular WDBC architecture, scaling, geometry, and selection records | Integrated protocol is the contribution; no algorithmic novelty claimed |

## MLST scope reassessment

**Classification: PLAUSIBLE FIT.** MLST's current official scope includes quantum computing, kernel methods, benchmark studies, and articles emphasizing codes/datasets and reproducibility. The work is scientifically relevant to QML evaluation and fits the journal's benchmark-article concept because it supplies technical detail and auditable artifacts.

- Strongest reason for review: the paper combines a fully nested QML/classical comparison with unusually explicit feature-map sensitivity, kernel geometry, computational provenance, and a reproducible negative result.
- Strongest desk-rejection risk: one small, familiar tabular dataset and no new algorithm may be judged incremental despite the protocol depth.
- Current mitigation: the title, abstract, contribution statement, related-work comparison, limitations, and conclusion frame the article as a methodological/reproducibility benchmark; claims are restricted to WDBC, PCA 2/4, 2Q/4Q, and tested ZZ maps.

Official scope source checked 11 September 2026: https://publishingsupport.iopscience.iop.org/journals/machine-learning-science-and-technology/about-machine-learning-science-technology/. No acceptance probability is inferred.
