# Scholarly Venue Research, Fit Scoring, and Submission Strategy

**Manuscript:** A Controlled Empirical Comparison of Classical and Quantum Kernel SVMs for Breast Cancer Classification  
**Status:** Canonical Release `v1.0.0` Venue Analysis  
**Date:** September 2026  
**Source Data:** Official Journal Author Guidelines, Editorial Charters, and Published Policies (2024–2026)

---

## 1. Candidate Journal Profiles and Official Submission Guidelines

### 1. Machine Learning: Science and Technology (MLST) — IOP Publishing
* **Publisher & Scope:** IOP Publishing. Multidisciplinary, fully open-access journal bridging application of machine learning across scientific and physical domains with methodological advances in ML algorithms, robustness, and benchmarking. Welcomes QML empirical studies.
* **Expected Novelty Threshold:** High methodological and scientific rigor. Does **not** require positive algorithmic breakthroughs; explicitly welcomes rigorous benchmarking, reproducibility evaluations, and well-executed negative empirical results that clarify scientific boundaries.
* **Empirical Benchmark Suitability:** Exceptional. Frequently publishes controlled comparisons, ablation analyses, and baseline critiques in scientific ML.
* **Quantum-Specific Relevance:** High. Dedicated topical section on quantum machine learning and quantum algorithms applied to physical and natural sciences.
* **Methodological / Reproducibility Relevance:** Very high. Enforces strict data and code availability declarations; strongly supports open-source repository releases.
* **Open-Access Model & Current APC:** Fully Open Access (CC BY licence). Current APC: **£2,500** (25% discount for IOP members; institutional transformative agreements frequently cover 100% of APC).
* **Format & Constraints:** No rigid page limit for regular research papers (typical manuscript length: 6,000–10,000 words). Single-column or standard IOP LaTeX / Word formats.
* **Preprint Policy:** Fully permissive. Recommends posting preprints to arXiv.
* **Editorial Scope Alignment:** **Strong scope fit**. Directly aligns with MLST's editorial mission of rigorous scientific machine learning evaluation, empirical benchmarking, and open-science transparency.

---

### 2. IEEE Transactions on Quantum Engineering (IEEE TQE)
* **Publisher & Scope:** IEEE Quantum / IEEE Computer Society. Gold open-access journal covering the engineering applications of quantum phenomena, including quantum software, quantum algorithms, quantum architectures, and benchmarking.
* **Expected Novelty Threshold:** Moderate-to-high. Strongly values systematic engineering evaluation, computational profiling, reproducibility, and rigorous benchmarking over purely speculative theoretical claims.
* **Empirical Benchmark Suitability:** Very high. IEEE TQE explicitly values papers analyzing runtime scaling, memory footprints, gate counts, statevector overheads, and comparative classical software baselines.
* **Quantum-Specific Relevance:** Outstanding. Entirely focused on quantum computing and engineering.
* **Methodological / Reproducibility Relevance:** Very high. Strong emphasis on reproducible software artifacts, detailed execution parameters, and open data.
* **Open-Access Model & Current APC:** Gold Open Access (CC BY / CC BY-NC-ND). Current APC: **US$1,995** (5% discount for IEEE members, 20% for IEEE Society members; World Bank low-income waivers available).
* **Format & Constraints:** IEEE two-column Transactions template (LaTeX or Word). No strict page limit, but standard articles typically span 8–14 two-column pages.
* **Preprint Policy:** Permissive. Encourages arXiv preprints prior to and during review.
* **Editorial Scope Alignment:** **Strong engineering alignment**. Well-matched if framed around quantum software benchmarking, statevector simulation overhead, and computational profiling.

---

### 3. Quantum (quantum-journal.org)
* **Publisher & Scope:** Non-profit, community-run, open-access journal for quantum science. Covers quantum information, computation, and foundational physics.
* **Expected Novelty Threshold:** **Extremely High**. Editorial charter explicitly states: *"Quantum does not accept research that is merely correct but incrementally improves a limited technique. Original research must provide a very significant technical or conceptual contribution (or a strong combination of both)."*
* **Empirical Benchmark Suitability:** Low-to-Moderate for negative benchmarks on single tabular datasets. Benchmarking studies are typically considered only if they establish a broad, general theoretical principle or evaluate an extensive suite of models across dozens of datasets.
* **Quantum-Specific Relevance:** Exceptional. The premier community journal for quantum physics and quantum computing.
* **Methodological / Reproducibility Relevance:** Very high. Mandatory code/data availability, mandatory author contribution statements, and mandatory AI tool disclosure.
* **Open-Access Model & Current APC:** Fully Open Access. Exceptionally accessible APC: **€600** (with generous waiver policies for unfunded researchers).
* **Format & Constraints:** Prepared using the `quantumview` / `quantumarticle` LaTeX document class. Requires an arXiv posting in `quant-ph` prior to submission.
* **Preprint Policy:** Mandatory arXiv posting (`quant-ph`).
* **Editorial Screening Assessment:** **Higher editorial-threshold risk**. The editorial charter's requirement of a very significant theoretical or conceptual breakthrough presents a notable hurdle for empirical negative benchmarks on existing benchmark datasets.

---

### 4. Quantum Machine Intelligence (QMI) — Springer Nature
* **Publisher & Scope:** Springer Nature. Peer-reviewed journal dedicated exclusively to the intersection of quantum computing and artificial intelligence / machine learning.
* **Expected Novelty Threshold:** Moderate. Highly receptive to domain-specific QML benchmarks, empirical comparisons, and feature-map evaluations on classical datasets.
* **Empirical Benchmark Suitability:** High. QMI published several foundational works cited directly in our paper, including Suzuki et al. (2020) on feature maps, Hubregtsen et al. (2021) on entanglement ablation, and Azevedo et al. (2022) on breast cancer classification.
* **Quantum-Specific Relevance:** Perfect thematic fit (100% focused on quantum machine learning).
* **Methodological / Reproducibility Relevance:** High. Standard Springer Nature open research policies.
* **Open-Access Model & Current APC:** Hybrid journal (subscription publication with Open Choice OA option). Authors can publish at **no APC cost** under the traditional subscription model, or choose OA (covered by Springer transformative agreements).
* **Format & Constraints:** Standard Springer Nature LaTeX / Word format. No rigid page constraints.
* **Preprint Policy:** Permissive. arXiv preprints welcomed.
* **Editorial Scope Alignment:** **Strong thematic fit**. Directly continues discussions and methodologies established in prior QMI publications.

---

### 5. ACM Transactions on Quantum Computing (ACM TQC)
* **Publisher & Scope:** Association for Computing Machinery. Scholarly journal publishing high-impact research across quantum computing, algorithms, complexity, software, and simulation.
* **Expected Novelty Threshold:** High. Demands substantial algorithmic or computer-science contributions.
* **Empirical Benchmark Suitability:** Moderate. Favors algorithmic innovations, software architecture frameworks, or extensive benchmarking over single-dataset studies.
* **Quantum-Specific Relevance:** High. Dedicated ACM quantum journal.
* **Methodological / Reproducibility Relevance:** Very high. Integrated with ACM Digital Library artifacts and reproducibility badges.
* **Open-Access Model & Current APC:** Fully Open Access as of 2026. Authors at institutions with **ACM Open** agreements publish at **no cost**; standard APC applies for non-participating institutions.
* **Format & Constraints:** ACM Primary Article Template (LaTeX/Word).
* **Preprint Policy:** Permissive.
* **Editorial Screening Assessment:** **Moderate scope fit / potential desk-screening concern** if viewed by computer science editors as an applied benchmark rather than a general quantum computing software contribution.

---

### 6. Patterns (Cell Press)
* **Publisher & Scope:** Cell Press / Elsevier. Open-access data science journal focusing on reproducible pipelines, benchmarking datasets, and methodological best practices in data-driven science.
* **Expected Novelty Threshold:** High for data-science methodology and reproducibility. Receptive to well-constructed negative results that correct literature misconceptions.
* **Empirical Benchmark Suitability:** Very high.
* **Quantum-Specific Relevance:** Moderate (general data science, not quantum-focused).
* **Open-Access Model & Current APC:** Fully Open Access. High APC: **~$3,700+ USD**.
* **Editorial Screening Assessment:** **Moderate fit**. Data science and reproducibility align well, though editors may prefer broader multi-cohort benchmarks across multiple domains.

---

## 2. Qualitative Venue Fit Matrix

Each journal is evaluated on an objective 1–5 scale across eight key dimensions:
* **Scope Fit:** Alignment with empirical ML, quantum kernels, and tabular benchmarking.
* **Novelty Fit:** Acceptance of rigorous negative results and benchmarking vs. requiring new algorithmic theorems.
* **Methodological Fit:** Receptiveness to nested CV, paired statistics, and leakage-prevention protocols.
* **Quantum Relevance:** Readership interest in quantum kernels and NISQ constraints.
* **Biomedical / Tabular Fit:** Appropriateness of using WDBC as a benchmark case study.
* **Reproducibility Fit:** Valuation of frozen releases, test suites, and open-source software.
* **Editorial Charter Fit:** Alignment with published editorial guidelines and scope criteria.
* **Cost Accessibility:** Affordability of APC (or availability of waiver/transformative agreements).

| Venue | Scope Fit (1–5) | Novelty Fit (1–5) | Methodological Fit (1–5) | Quantum Relevance (1–5) | Biomedical / Tabular Fit (1–5) | Reproducibility Fit (1–5) | Editorial Charter Fit (1–5) | Cost Accessibility (1–5) | Total Score (/40) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **IOP Machine Learning: Science and Technology (MLST)** | **5** | **5** | **5** | **4** | **4** | **5** | **5** | **4** | **37 / 40** |
| **Springer Quantum Machine Intelligence (QMI)** | **5** | **5** | **4** | **5** | **4** | **4** | **5** | **5** (Hybrid/Free) | **37 / 40** |
| **IEEE Transactions on Quantum Engineering (TQE)** | **4** | **4** | **5** | **5** | **3** | **5** | **4** | **4** ($1,995) | **34 / 40** |
| **Quantum (quantum-journal.org)** | **4** | **2** | **4** | **5** | **3** | **5** | **2** | **5** (€600) | **30 / 40** |
| **ACM Transactions on Quantum Computing (TQC)** | **4** | **3** | **4** | **5** | **3** | **4** | **3** | **3** (ACM Open) | **29 / 40** |
| **Patterns (Cell Press)** | **4** | **4** | **5** | **3** | **4** | **5** | **3** | **2** (~$3,700+) | **30 / 40** |

---

## 3. Detailed Hypothesis Evaluation and Strategic Recommendations

### Evaluation of Core Hypotheses:

1. **Hypothesis 1: IOP MLST is the strongest natural scientific fit.**
   * **Verdict: CONFIRMED.** MLST operates precisely at the interface of scientific application and machine learning methodology. Its editorial board explicitly welcomes rigorous empirical benchmarks and negative results that counteract hype in emerging fields. The manuscript's focus on leakage elimination, multi-seed stability, and geometric alignment aligns perfectly with MLST reviewer expectations.

2. **Hypothesis 2: IEEE TQE is a viable quantum-engineering alternative.**
   * **Verdict: CONFIRMED.** TQE is well-suited if the paper emphasizes the computational profiling aspect: wall-clock runtime vs. LibSVM, exact statevector vs. ComputeUncompute pair evaluations, memory complexity, and NISQ hardware feasibility.

3. **Hypothesis 3: Quantum is aspirational due to strict conceptual advance thresholds.**
   * **Verdict: CONFIRMED.** While *Quantum* is the most prestigious open-access quantum journal and offers a low €600 APC, its editorial guidelines explicitly disqualify papers that are "merely correct" without a "very significant technical or conceptual contribution." A negative empirical benchmark on a single tabular dataset faces a higher editorial threshold unless accompanied by a general mathematical proof or a novel algorithm.

4. **Additional Finding: Springer QMI is an equally compelling primary/secondary target.**
   * **Verdict: HIGHLY VIABLE.** QMI has published the exact lineage of papers this manuscript engages with (Suzuki 2020, Hubregtsen 2021, Azevedo 2022). Furthermore, as a hybrid journal, it provides a **zero-cost publication route** under the traditional subscription model if APC funding is unavailable.

---

## 4. Final Submission Tier Recommendation

### **Primary Target: Machine Learning: Science and Technology (IOP)**
* **Why:** Highest alignment between the manuscript's core identity (a rigorous empirical machine learning methodology study) and the journal's editorial charter. Receptive to negative results; respects statistical rigor and open-science releases; broad multidisciplinary visibility.

### **Secondary Target: Quantum Machine Intelligence (Springer) OR IEEE Trans. Quantum Engineering (TQE)**
* **Why (QMI):** Direct thematic audience. The exact readership studying feature maps and breast cancer QML. Zero-cost hybrid publication option.
* **Why (TQE):** Premier engineering venue if the authors prefer an IEEE audience emphasizing computational cost, software benchmarking, and NISQ execution trade-offs.

### **Aspirational Target: Quantum (quantum-journal.org)**
* **Why:** High prestige, community-run, low APC (€600). However, submission requires navigating a higher editorial threshold due to the absence of a novel theoretical algorithm or physical hardware demonstration.
