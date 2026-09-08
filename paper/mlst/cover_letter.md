# Cover Letter

**To:**  
The Editors-in-Chief and Editorial Office  
*Machine Learning: Science and Technology*  
IOP Publishing  

**Date:** September 2026  
**Subject:** Submission of Original Research Paper — *A Controlled Empirical Comparison of Classical and Quantum Kernel SVMs for Breast Cancer Classification*  

Dear Editor-in-Chief and Editorial Office,

Please find enclosed our manuscript entitled **"A Controlled Empirical Comparison of Classical and Quantum Kernel SVMs for Breast Cancer Classification"**, which we submit for consideration as an **Original Research Paper** in *Machine Learning: Science and Technology*.

Quantum kernel methods represent an active and rapidly expanding research direction in machine learning. By embedding classical data into quantum state spaces via parameterized quantum circuits, these methods theoretically exploit high-dimensional Hilbert spaces to separate non-linear data distributions. However, empirical demonstrations of practical quantum advantage require strong classical baselines, leakage-free evaluation, robust validation across multiple random splits, and careful scientific interpretation. In the existing literature, empirical evaluations on tabular benchmarks frequently rely on single train/test partitions, omit classical hyperparameter optimization, or inadvertently introduce data leakage through global dimensionality reduction, making it difficult to determine whether reported performance differences reflect genuine quantum capabilities or methodological artifacts.

To address these methodological challenges, this work presents a controlled empirical comparison between classical Support Vector Machine baselines (Linear and Radial Basis Function kernels) and Quantum Support Vector Classifiers (QSVC). Using the Wisconsin Diagnostic Breast Cancer (WDBC) benchmark dataset, input features are projected to two and four dimensions via principal component analysis and encoded through parameterized two- and four-qubit second-order Pauli-Z (ZZ) feature maps evaluated with fidelity-based quantum kernels. The study systematically evaluates five complementary dimensions: predictive classification performance, architectural feature-map sensitivity, sample-size scaling dynamics, kernel similarity geometry, and computational execution cost under exact statevector simulation.

Under the investigated experimental conditions, our empirical findings demonstrate that properly tuned classical SVM baselines consistently achieved stronger predictive performance than quantum kernel classifiers across all evaluated dimensions. Classical SVMs outperformed QSVC across all five outer test splits in both two- and four-dimensional representations, achieving mean malignant-class F1 scores of 0.934 vs. 0.868 in two dimensions and 0.949 vs. 0.872 in four dimensions. Furthermore, feature-map architectural ablation revealed that deeper quantum circuits exhibited sensitivity and performance degradation, while sample-size scaling showed no small-data quantum advantage. In addition, Centered Kernel Alignment (CKA) confirmed that although the four-qubit quantum kernel produced a similarity geometry distinct from the classical RBF kernel (CKA ≈ 0.338), this geometric novelty did not translate into improved classification performance. Importantly, we do not claim that quantum methods are generally inferior or that quantum advantage is impossible; rather, our findings establish an empirical baseline demonstrating that under the investigated experimental conditions, geometric distinction alone does not guarantee superior classification boundaries over standard classical regularization and kernel learning.

The methodological strength of this study centers on rigorous protocol design and reproducibility. The experimental pipeline enforces strict leakage-controlled preprocessing, refitting all standardizers, PCA projections, and quantum Gram matrices strictly inside each training partition. All evaluations are conducted across five predefined, matched random splits with nested five-fold cross-validation for hyperparameter tuning, paired non-parametric statistical analysis, and transparent disclosure of small-sample statistical power bounds. To support verifiable science and open benchmarking, the complete implementation, configurations, test suites, and reproducibility artifacts are publicly available in an open-source repository release at https://github.com/SinaQP/SVM-Vs-QSVM (frozen at release v1.0.0).

We believe *Machine Learning: Science and Technology* is the ideal venue for this manuscript. The journal is widely recognized for bridging machine learning methodology, physical sciences, quantum technologies, and reproducible empirical research. Our study directly aligns with MLST's scope by combining machine learning methodology, rigorous empirical benchmarking, quantum machine learning, reproducibility, and biomedical benchmark evaluation. Rather than presenting exaggerated claims of quantum supremacy or novel algorithmic variants tested against default baselines, this paper contributes a careful, standardized baseline that clarifies when and why quantum kernels do—or do not—provide practical classification utility.

In accordance with IOP Publishing editorial policies, the author confirms that:
1. This manuscript is an original work, has not been published previously, and is not currently under consideration for publication elsewhere.
2. The author approves the final version of the manuscript and agrees to its submission to *Machine Learning: Science and Technology*.
3. This research received no external funding.
4. The author declares no conflict of interest or competing financial interests.
5. This study used a publicly available benchmark dataset and did not involve the recruitment of human participants or collection of new clinical data.

Thank you for your time, consideration, and editorial assessment of this manuscript.

Sincerely,

**Sina Qasempour**  
Independent Researcher, Iran  
Corresponding Author  
Email: qasempoursina@gmail.com  
ORCID: https://orcid.org/0009-0006-8853-6740  
Repository: https://github.com/SinaQP/SVM-Vs-QSVM  
