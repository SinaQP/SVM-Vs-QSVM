# Scientific Manuscript Notes & Literature Tracking

**Project:** Classical SVM vs Quantum Kernel SVM for Breast Cancer Classification  
**Release Target:** `v1.0.0` Frozen Canonical Baseline  
**Literature Review Status:** Complete (35 Verified Scholarly Citations, 0 Placeholders)  
**Document Purpose:** Working notes tracking literature synthesis, venue fit, reviewer defenses, softened claims, and novelty framing.

---

## 1. Literature Review Synthesis & Key Insights

The literature review resolved all 8 structured placeholders across 35 authentic, peer-reviewed and recognized scholarly references:

1. **Quantum Kernel Methods:**
   - Formalized by Havlíček et al. (2019) and Schuld & Killoran (2019). Schuld (2021) proved that all supervised quantum models are fundamentally kernel machines in quantum Hilbert spaces.
   - Provable quantum advantage exists only for target concepts with specific quantum-accessible algebraic or cryptographic structure (e.g., discrete logarithm problems as shown by Liu et al., 2021) or when classical kernels cannot compute the concept (Huang et al., 2021). For generic tabular data, no theoretical guarantee of superiority exists.

2. **Feature Maps & Circuit Architectures:**
   - Parameterized Pauli-Z expansion circuits (`ZZFeatureMap`) derive their theoretical interest from connections to Instantaneous Quantum Polynomial (IQP) sampling hardness (Bremner et al., 2016; Suzuki et al., 2020).
   - However, Hubregtsen et al. (2021) demonstrated that higher entanglement capacity does not correlate monotonically with classification accuracy. Data re-uploading (Pérez-Salinas et al., 2020) offers an alternative paradigm, but standard NISQ benchmarks typically rely on ZZ maps.

3. **Kernel Concentration & Untrainability:**
   - Thanasilp, Wang, Cerezo, Holmes (2024, *Nature Communications*) proved that as circuit depth or qubit count increases, parameterized quantum kernels suffer from **exponential kernel concentration**, causing off-diagonal overlaps to concentrate around constant values and the Gram matrix to collapse toward identity.
   - Kübler et al. (2021) analyzed the inductive bias of quantum kernels, showing that un-tuned quantum feature maps frequently fail to align with the data label distribution. Shaydulin & Wild (2022) established that input scaling directly governs the effective quantum kernel bandwidth.

4. **Small Datasets & Sample Efficiency:**
   - Theoretical generalization bounds (Caro et al., 2022; Banchi et al., 2021) prove that quantum models can generalize from small samples under bounded generator norms, leading to widespread conjectures of "small-data quantum advantage."
   - However, our empirical sample-size scaling ($N \in [50, 455]$) directly demonstrated that QSVC suffered severe performance loss at $N=50$ (F1 drops to $\approx 0.499$ in 4Q), while Classical Linear SVM retained strong diagnostic accuracy (F1 $\approx 0.913$). This provides critical empirical evidence that theoretical PAC bounds do not automatically translate into empirical sample efficiency on real tabular datasets.

5. **Biomedical QML & Prior Work on WDBC:**
   - Leither, Lubinski, Kubal, Johri (2026, arXiv:2608.11373) evaluated QML models against AutoML classical baselines across oncological datasets and found **no evidence of quantum advantage**.
   - Specific prior studies applying QSVM to the WDBC dataset (Wang, 2024; Azevedo et al., 2022; Chaudhry et al., 2024) frequently evaluated single train/test splits, reported classical RBF accuracies in the 93%–96% range, and found that quantum models achieve comparable or slightly lower performance on simulators (88%–92%). Our multi-seed, leakage-free benchmark confirms and formalizes this boundary.

6. **Benchmarking Methodology & Classical Baselines:**
   - Bowles, Ahmed, Schuld (2024, arXiv:2403.07059) systematically demonstrated that inadequate classical baselines, arbitrary single splits, and data leakage pervade published QML literature, creating false impressions of quantum advantage.
   - Cerezo et al. (2022), Preskill (2018), and Aaronson (2015) emphasize that empirical benchmarking must include rigorous classical tuning, leakage control, and end-to-end wall-clock cost tracking.

---

## 2. Novelty Framing

The literature review supports the distinct empirical and methodological contributions of this manuscript:

1. **Methodological Rigor and Leakage Elimination:** Unlike prior studies that fitted PCA or scaling globally before splitting, our pipeline enforces strict fold-specific transformations and nested 5-fold cross-validation inside an isolated 80/20 outer test harness.
2. **Multi-Seed Stability:** We evaluate 5 predefined outer seeds (`[42, 123, 456, 789, 2026]`), providing paired split-level confidence intervals and demonstrating that classical superiority is directionally stable (5/5 wins).
3. **Controlled Feature-Map Ablation (60 Quantum Runs):** We systematically isolate the effect of circuit repetitions (`reps` $\in \{1, 2, 3\}$) and entanglement (`linear` vs. `full`), demonstrating that shallower architectures are essential to avoid performance collapse in 4 qubits.
4. **Sample-Size Scaling Analysis ($N=50$ to $455$):** We empirically test the "small-data quantum advantage" conjecture across 5 training subsets, documenting that QSVC experiences its greatest performance deficit in low-data regimes.
5. **Geometric Dissection via CKA and Spectral Entropy:** We measure Centered Kernel Alignment and effective rank, proving that while 4Q quantum kernels depart substantially from RBF geometry ($\text{CKA} \approx 0.338$), geometric novelty does not translate into superior classification.
6. **Transparent Negative Quantum Advantage Result:** We present a rigorous, reproducible negative finding, avoiding hype and providing realistic bounds for NISQ-era tabular machine learning.

---

## 3. Claims Softened During Literature Review

To ensure absolute scientific accuracy and avoid reviewer rejection:

1. **Kernel Concentration Wording:**
   - *Initial phrasing:* "Circuit depth caused barren plateaus and kernel concentration."
   - *Softened phrasing:* "Deeper feature-map configurations were strongly associated with degraded predictive performance and excessive spectral entropy, displaying empirical symptoms consistent with the exponential kernel concentration phenomena analyzed by Thanasilp et al. (2024)."
2. **Statistical Inferential Claims:**
   - *Initial phrasing:* "Classical SVM statistically outperformed QSVC."
   - *Softened phrasing:* "Classical SVMs achieved higher malignant F1 scores across all five evaluated outer splits (5/5 wins, bootstrap 95% CI $[+0.0388, +0.0977]$ for PCA 2 and $[+0.0445, +0.1092]$ for PCA 4). However, because $n=5$ overlapping splits do not represent independent observations and the minimum possible two-sided exact Wilcoxon $p$-value is bounded at $0.0625$ (Holm-adjusted to $0.1875$), these findings represent consistent descriptive empirical evidence rather than formal asymptotic proof."
3. **Accuracy and ROC-AUC Wording:**
   - Described strictly as descriptive comparative metrics ("higher", "lower", "observed difference") without using the word "statistically significant", as formal inferential testing was restricted to the primary endpoint (Malignant F1).
4. **Biomedical Framing:**
   - Explicitly clarified that the study is a methodological machine-learning experiment on a benchmark dataset and does **not** establish clinical diagnostic validity.

---

## 4. Potential Target Venues

| Venue | Category | Scope Fit | Key Reviewer Expectations |
| :--- | :--- | :--- | :--- |
| **Quantum** (Open Access) | Quantum Information / QML | Welcomes rigorous, reproducible negative results; strong focus on methodological soundness. | Must provide open-source code and clear distinction between statevector and physical QPU. |
| **IEEE Transactions on Quantum Engineering (TQE)** | Applied Quantum Computing | Focuses on engineering benchmarks, empirical algorithmic evaluations, and reproducible pipelines. | High valuation of end-to-end runtime tracking, complexity analysis, and leakage control. |
| **Machine Learning: Science and Technology (IOP)** | Applied Machine Learning | Focuses on the application of ML methods to scientific and physical domains, including QML benchmarks. | Requires strong classical baselines, careful ablation, and disciplined statistical reporting. |
| **Patterns (Cell Press)** | Data Science & Benchmarking | Focuses on reproducible data science pipelines, rigorous benchmarking, and open science practices. | Highly receptive to controlled studies correcting exaggerated literature claims. |
| **NeurIPS (Datasets & Benchmarks Track)** | Conference Benchmark Track | Focuses on open benchmark datasets, rigorous baselines, and negative results with broad community impact. | Strict requirements for open artifacts, test suite validation, and thorough limitations analysis. |

---

## 5. Reviewer Defenses Summary

| Potential Reviewer Critique | Evidence-Backed Defense Strategy |
| :--- | :--- |
| **"Why evaluate only 2 and 4 qubits?"** | Cite Preskill (2018) and Peters et al. (2021): NISQ tabular applications operating on compressed feature spaces are the dominant paradigm in current biomedical QML literature. We demonstrate that in this regime, QSVC fails to match simple linear baselines. |
| **"Could an optimized or trained feature map win?"** | Cite Kübler et al. (2021) and Shaydulin & Wild (2022): Generic fixed feature maps lack problem alignment. We acknowledge that kernel target alignment (KTA) or projected quantum kernels (Huang et al., 2021) represent critical future directions. |
| **"Why is statevector simulation used instead of physical hardware?"** | Statevector simulation provides an exact, noiseless mathematical upper bound. Physical hardware noise (gate errors, decoherence, measurement shot noise) would further degrade QSVC performance. |
| **"Is the small sample of 5 splits statistically sufficient?"** | Cite Bowles et al. (2024): 5-seed nested CV is substantially more rigorous than the single-split protocols common in the literature. We transparently report exact $p$-values and bootstrap CIs without overstating formal significance. |
