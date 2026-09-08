# Simulated Peer Review Reports

> [!IMPORTANT]
> **INTERNAL SIMULATION — NOT ACTUAL PEER REVIEW**
> This document records an internal reviewer simulation conducted by the research team for quality auditing and stress-testing. It does not represent actual external peer review by any scholarly journal or conference, and the manuscript has not been externally reviewed or accepted.

**Manuscript Title:** A Controlled Empirical Comparison of Classical and Quantum Kernel SVMs for Breast Cancer Classification  
**Target Submission:** Scholarly Journal Submission  
**Simulation Mode:** Rigorous, Uncharitable Multi-Disciplinary Expert Review Panel

---

## Reviewer A: Quantum Kernel and QML Specialist

### Reviewer Profile
* **Expertise:** Quantum Information, Quantum Machine Learning, Quantum Kernel Theory, Barren Plateaus & Concentration of Measure.
* **Reviewing Philosophy:** Highly attentive to quantum theoretical precision, feature-map properties, operator algebraic formulations, mathematical validity of Hilbert/operator spaces, and hardware vs. simulation distinctions.

---

### Summary
The manuscript presents an empirical benchmarking study comparing classical SVMs and Quantum Support Vector Classifiers using parameterized second-order Pauli-Z expansion (`ZZFeatureMap`) on a 2-qubit and 4-qubit projection of the Wisconsin Diagnostic Breast Cancer (WDBC) dataset. The paper systematically ablates circuit depth and entanglement, measures sample-size scaling, analyzes Centered Kernel Alignment (CKA), and reports a consistent absence of quantum advantage. The empirical rigor is commendable, but the theoretical exposition of quantum kernel feature spaces and concentration of measure requires critical mathematical corrections.

### Strengths
1. **Thorough Circuit Ablation:** Evaluating $\text{reps} \in \{1, 2, 3\}$ and linear vs. full entanglement across multiple seeds provides valuable empirical insight into why deeper ZZ feature maps fail.
2. **Geometric Diagnostics:** The use of Centered Kernel Alignment (CKA) and spectral entropy to characterize the Gram matrix geometry provides deeper insight than raw classification accuracies alone.
3. **Simulation vs. Hardware Distinction:** The authors correctly distinguish between classical statevector linear algebra simulation and physical quantum processor execution, avoiding false claims about physical QPU speedups.
4. **Honest Negative Result:** Transparent reporting of negative results in QML is essential for scientific integrity in the field.

### Major Concerns
1. **Operator Space vs. State Space Contradiction (Section 11):**  
   The authors state that for 2 qubits, statevectors reside in a $2^2=4$ dimensional Hilbert space, yet report an effective rank of $7.35$. For 4 qubits, they state the Hilbert space is $2^4=16$ dimensional, yet report an effective rank of $96.49$. In linear algebra, the rank of a Gram matrix cannot exceed the dimension of the underlying feature vectors. The authors have omitted the crucial distinction between the pure state Hilbert space $\mathcal{H} = \mathbb{C}^{2^n}$ and the density operator feature space $\mathcal{B}(\mathcal{H})$ (or state space $\mathcal{H} \otimes \mathcal{H}^*$), whose dimension is $(2^n)^2 = 4^n$ ($16$ for 2Q, $256$ for 4Q). Without explicitly defining the feature map as mapping into this $4^n$-dimensional operator space, the reported effective ranks appear mathematically impossible.
2. **Over-Attribution to Exponential Kernel Concentration:**  
   The authors frequently invoke "exponential kernel concentration" to explain the degradation in deeper circuits. However, the study only measures $n=2$ and $n=4$ qubits, and depths $1$ to $3$. In 4Q, the off-diagonal standard deviation remains $\sim 0.101$, which is non-zero and does not establish asymptotic concentration to the identity matrix. The authors must soften their language: they have observed empirical behavior *consistent with* concentration phenomena, not *proven* exponential concentration.
3. **Limited Feature Map Architecture:**  
   The study exclusively evaluates the fixed, non-trainable `ZZFeatureMap`. It is widely known in QML theory (e.g., Kübler et al., 2021; Huang et al., 2021) that fixed fidelity kernels without problem-specific data alignment frequently fail. The authors should explicitly discuss whether trainable quantum kernels (kernel target alignment) or projected quantum kernels could alter these conclusions.

### Minor Concerns
1. In Section 7.1, provide the exact definition of the bandwidth scaling factor in relation to Shaydulin & Wild (2022).
2. The runtime ratio between 2Q and 4Q statevector simulation ($\sim 2.9\times$) should not be conflated with asymptotic computational complexity.

### Questions for Authors
1. Can you confirm that the effective rank computation was performed on the Gram matrix $\mathbf{K}$ whose entries are $K_{ij} = \text{Tr}[\rho_i \rho_j]$, and update the text to explicitly reference the $4^n$-dimensional operator feature space?
2. Did you test any alternative feature maps (e.g., Pauli-$Y$ or Pauli-$X$ rotations, or alternative entanglement topologies) to confirm that the observed failure is characteristic of generic fixed ansatzes?

### Recommendation
**Major Revision** (Pending theoretical clarification of the operator feature space and softening of concentration claims).

### Confidence
**5 / 5** (High expertise in quantum kernel methods and spectral theory).

---

## Reviewer B: Classical ML and Statistical Methodology Specialist

### Reviewer Profile
* **Expertise:** Statistical Learning Theory, Cross-Validation Methodology, Experimental Statistics, Resampling Methods, Benchmarking Standards.
* **Reviewing Philosophy:** Skeptical of small-sample claims, vigilant regarding data leakage, insists on rigorous multiple-testing control, and demands precision regarding dependent vs. independent observations.

---

### Summary
This paper addresses a pervasive problem in the quantum machine learning literature: the proliferation of claims based on single train/test splits, default classical baselines, and data leakage. The authors design a controlled benchmark on the WDBC dataset incorporating nested cross-validation, fold-isolated preprocessing, and paired multi-seed evaluation. Classical SVMs consistently outperform the quantum classifier. The experimental hygiene is significantly higher than typical QML literature, but the inferential statistical presentation must be held to strict classical ML standards.

### Strengths
1. **Leakage Prevention:** Strict isolation of `StandardScaler`, `PCA`, and `MinMaxScaler` within inner training folds and outer training splits completely eliminates data leakage. This is a model of methodological hygiene.
2. **Nested Classical Hyperparameter Selection:** Designation of the classical comparator via inner-CV Malignant F1 prevents post-hoc selection bias.
3. **Sample-Size Scaling Protocol:** Evaluating $N \in [50, 455]$ with refit preprocessing rigorously tests small-sample generalization claims.
4. **Primary vs. Secondary Endpoint Discipline:** Pre-specifying Malignant F1 as the primary inferential metric is good practice.

### Major Concerns
1. **Statistical Power Floor and Framing of Non-Rejection:**  
   With $n=5$ outer splits, the minimum achievable two-sided exact Wilcoxon $p$-value when all differences share the same sign is $(1/2)^4 = 0.0625$, which inflates to $0.1875$ under Holm-Bonferroni correction. The authors cannot reject the null hypothesis at $\alpha = 0.05$. While the authors acknowledge this limitation in Section 14, other sections of the text describe classical SVMs as "statistically outperforming" QSVC. The manuscript must be rigorously consistent: the empirical evidence shows consistent descriptive superiority (5/5 split wins), but cannot establish formal asymptotic statistical significance.
2. **Interpretation of Bootstrap Confidence Intervals:**  
   The reported 95% bootstrap confidence intervals ($[+0.0388, +0.0977]$ for PCA 2) are based on resampling over only $n=5$ observed split differences. Furthermore, the 5 outer splits are overlapping (sharing ~60% of training data). Resampling 5 dependent values does not overcome sample dependence or small sample size. These intervals must be explicitly identified as *exploratory split-level percentile bootstrap intervals* rather than standard inferential confidence intervals.
3. **Split Re-use for Architectural Freezing:**  
   The feature-map architecture ($\text{reps}=1, \text{full}$) was selected based on Phase 9 ablation conducted on the same 5 outer splits later used for Phase 11 evaluation. While the test data were not used for parameter fitting, using the same splits to choose the architecture introduces mild split-level information reuse. This threat to validity must be explicitly highlighted.

### Minor Concerns
1. Ensure secondary metrics (Accuracy, Precision, Recall, ROC-AUC) are never described with the word "significant."
2. The PCA variance reduction (retaining 63.5% in 2 dims, 79.4% in 4 dims) means substantial feature information is discarded; mention how this affects the classical-quantum comparison.

### Questions for Authors
1. Why were 5 splits chosen rather than 10 or 20 outer folds (e.g., repeated stratified $5\times 2$ CV), which would have provided greater statistical power?
2. Did you verify that the inner cross-validation folds did not encounter empty minority classes in the smaller sample-size experiments?

### Recommendation
**Minor Revision** (Empirical design is solid; requires textual qualification of statistical limits and bootstrap wording).

### Confidence
**5 / 5** (High expertise in statistical validation and ML benchmarking).

---

## Reviewer C: Applied and Biomedical ML Specialist

### Reviewer Profile
* **Expertise:** Biomedical Informatics, Diagnostic Machine Learning, Clinical Decision Support, Cancer Classification Benchmarks.
* **Reviewing Philosophy:** Focused on whether the clinical problem formulation is sound, whether evaluation metrics reflect medical reality, and ensuring the paper does not over-promise medical utility.

---

### Summary
The paper evaluates classical and quantum kernel SVMs on the Wisconsin Diagnostic Breast Cancer (WDBC) benchmark dataset. The authors designate Malignant (Class 0) as the positive class, focusing on Malignant F1, Precision, and Recall. The paper demonstrates that classical linear and RBF SVMs outperform quantum kernel classifiers across all evaluated sample sizes and dimensions. The authors are commendably clear that this is a methodological benchmark rather than a clinical study.

### Strengths
1. **Correct Diagnostic Framing:** Designating Malignant as the positive class (`pos_label=0`) and focusing on Malignant F1 and Recall reflects proper medical priority (minimizing false negatives in cancer detection).
2. **Clinical Disclaimers:** Explicitly stating in Section 4 and Section 16 that this study does not constitute a clinical validation prevents over-interpretation.
3. **Explanation of Tabular Feature Properties:** The discussion correctly notes that continuous morphometric descriptors from fine needle aspirates exhibit strong linear and low-order non-linear structure that classical RBF kernels capture efficiently.

### Major Concerns
1. **Clinical Relevance of PCA Compression:**  
   In modern clinical bioinformatics, diagnostic models utilize all available morphometric or genomic features. Compressing 30 features down to 2 or 4 principal components to accommodate quantum simulator limits discards 20%–36% of the clinical variance. The authors must ensure the manuscript does not claim to establish optimal breast cancer classification benchmarks, but rather benchmark performance *under low-dimensional NISQ constraints*.
2. **Single Tabular Dataset Scope:**  
   The WDBC dataset is over 30 years old ($N=569$) and has known simple linear separability. The finding that quantum kernels fail on WDBC cannot be generalized to complex multi-omic, histological image, or spatial biology cancer datasets. The authors should strengthen the Discussion by citing modern multi-cancer benchmarks (such as Leither et al., 2026) to contextualize their results within broader oncological QML.

### Minor Concerns
1. Replace any ambiguous terms like "medical prediction" or "diagnostic efficacy" with "classification performance on the WDBC benchmark."
2. Clarify that while Classical Linear SVM achieves 0.956 F1 on PCA 4, a classical SVM trained on all 30 uncompressed features typically achieves >0.97 F1, illustrating the cost of quantum-mandated dimensionality reduction.

### Questions for Authors
1. Did you examine false-negative cases specifically to understand which types of malignant tumors the quantum classifier misclassified?
2. Would the pipeline be applicable to other tabular biomedical datasets (e.g., diabetes, heart disease) with similar dimensionality constraints?

### Recommendation
**Accept with Minor Revisions** (Methodological benchmark is clear and honest; minor framing adjustments needed for biomedical context).

### Confidence
**4 / 5** (Strong expertise in applied biomedical ML; moderate in quantum theory).

---

## 4. Synthesis of Panel Recommendations

| Reviewer | Perspective | Initial Verdict | Core Prerequisite for Acceptance |
| :--- | :--- | :---: | :--- |
| **Reviewer A** | Quantum Information / QML | **Major Revision** | Clarify $4^n$ operator feature space vs. $2^n$ state space for effective rank; soften kernel concentration causal claims. |
| **Reviewer B** | Classical ML / Statistics | **Minor Revision** | Qualify bootstrap CIs as exploratory split-level intervals; state clearly that overlapping splits limit asymptotic inference. |
| **Reviewer C** | Applied Biomedical ML | **Minor Revision** | Reiterate low-dimensional NISQ constraint; ensure benchmark is not confused with clinical diagnostic tool. |

**Overall Consensus:** The paper is scientifically valuable and ready for publication following targeted textual revisions addressing theoretical operator-space definitions, conservative concentration language, and statistical power boundaries.
