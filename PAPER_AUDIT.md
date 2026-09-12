# PAPER AUDIT

> **Historical pre-correction audit retained for provenance.** Its methodology, citation, and disclosure findings motivated the remediation now recorded in `paper/corrected_result_provenance.md`, `paper/reference_integrity_audit.md`, `paper/ai_disclosure_audit.md`, and `paper/final_scientific_attack_test.md`. The current manuscript uses the corrected nested analysis at checkpoint `f4c8418`; do not treat the findings below as the final post-remediation disposition.

## Overall Assessment

**Rating: Serious integrity/technical issues found**

The manuscript is not safe to submit in its present form. Its strongest features are transparent reporting of negative results, fold-local preprocessing, paired seed alignment, release-tagged code/results, and unusually explicit discussion of statistical limitations. The central numerical summaries were independently reconciled to the frozen CSV outputs, and the repository validation and test suite passed (23/23 tests).

Those strengths are outweighed by four submission-level problems:

1. The bibliography contains one apparently non-existent composite article and several DOI/article-number records that resolve to different publications.
2. The selected quantum feature-map architecture was chosen using the same outer-test splits used for the final comparison. The resulting comparison is exploratory, not a leakage-free nested evaluation, despite repeated claims that it is “strict” and “leakage-free.”
3. The paper’s contribution—a careful negative benchmark on one small, standard dataset using standard models—does not clearly meet the target journal’s stated threshold of a significant conceptual/methodological advance or a state-of-the-art scientific application.
4. IOP requires disclosure when generative AI is used to edit or generate manuscript text, figures from data, or literature-search support. The manuscript contains no such disclosure. This becomes a definite policy violation if any listed use occurred.

No evidence of fabricated experimental results, image manipulation, participant-identification risk, or copied prose was found in this audit. The reference defects are serious, but they should not be characterized as deliberate fabrication without evidence about how they arose.

### Scope and evidence reviewed

- Submission PDF: `paper/mlst/manuscript.pdf` (20 pages)
- Supplement: `paper/mlst/supplementary/supplementary_material.pdf` (3 pages)
- LaTeX sources and 36-entry BibTeX database
- All principal result CSVs, manifests, figures, configuration files, notebook structure, validation scripts, tests, Git history, tag `v1.0.0`, and remote tag existence
- Current MLST author guidelines, current IOP generative-AI policy, UCI dataset record, Crossref/DataCite metadata, arXiv records, and publisher/DOI records where available

## Critical Issues

### 1. A bibliography entry appears to combine multiple real papers into a non-existent article

**Location:** References, `canatar2023spectral`; citations in Related Work (PDF p. 4; LaTeX line 96) and Kernel Geometry Analysis (PDF p. 11; line 302).

**Problem:** The entry “Spectral Bias and Task-Model Alignment in Quantum Machine Learning,” attributed to Canatar, Peters, Pehlevan, Wild, and “Romain Rish,” PRX Quantum 4, 020340 (2023), DOI `10.1103/PRXQuantum.4.020340`, could not be verified as a real publication. The DOI resolves to an unrelated article, “Classical Simulation of Short-Time Quantum Dynamics.” The title resembles “Spectral Bias and Task-Model Alignment Explain Generalization in Kernel Regression and Infinitely Wide Neural Networks,” while most authors resemble the separate arXiv paper “Bandwidth Enables Generalization in Quantum Kernel Models” (`arXiv:2206.06686`), whose fifth author is Ruslan Shaydulin, not “Romain Rish.”

**Why it matters:** A non-existent or composite reference is a direct research-integrity and desk-rejection risk. IOP states that references to non-existent sources are strong evidence of irresponsible AI use and usually result in rejection; it distinguishes this from a simple typo or accidental mixing of two existing records.[^1]

**Evidence:** DOI resolution, Crossref title/author search, and arXiv author/title searches disagree with every identifying field taken together. No exact-title record was found in Crossref or arXiv.

**Severity:** Critical

**Recommended action:** Determine which real paper supports each claim, read it in full, replace the composite entry with the correct primary source(s), and re-check every sentence currently citing this key. Do not merely substitute a plausible DOI.

### 2. Outer-test data were used to select the canonical QSVC architecture

**Location:** Abstract (PDF p. 1); Experimental Protocol (p. 5; lines 128 and 190); Feature-Map Ablation (pp. 8–9); Threats to Validity (p. 16; line 436); Conclusion (p. 17; line 447).

**Problem:** The `reps=1, full` architecture was chosen by comparing Phase 9 performance on the same five outer-test partitions later used for the “canonical” Phase 11 comparison. This is study-level test-set selection. The inner CV protects only the SVC hyperparameter `C`; it does not undo architecture selection on outer-test outcomes.

**Why it matters:** The final test estimates are optimistically selected for QSVC and are not independent estimates of the performance of a prespecified architecture. More importantly, the manuscript still calls the study a “strict nested cross-validation protocol,” a “controlled, leakage-free empirical comparison,” and says outer tests remained quarantined during “all ... hyperparameter selection.” Architecture is a model-selection choice, so those broad statements are false or materially misleading even though the limitation is disclosed elsewhere.

**Evidence:** The manuscript expressly states that Phase 9 architecture selection was informed by the same outer splits used in Phase 11. Git history also places the ablation work before the final tuning/evaluation protocol. Supporting documentation is internally contradictory: `docs/methodology.md` says outer-test metrics are never used to choose models or hyperparameters, while the manuscript says the map was selected using those metrics.

**Severity:** Critical

**Recommended action:** Either rerun a genuinely nested design in which feature-map architecture and `C` are selected entirely inside each outer-training set, or evaluate the already selected architecture on a new untouched external/holdout evaluation set. If no new evaluation is possible, remove all “leakage-free,” “strict nested,” and confirmatory language and present the entire performance study as exploratory.

### 3. Multiple DOI/article records identify the wrong publications

**Location:** References, especially `schuld2021supervised`, `banchi2021generalization`, `bremner2016average`, `holmes2022connecting`, and `thanasilp2024exponential`.

**Problem:**

- `schuld2021supervised`: DOI `10.1103/PRXQuantum.2.040315` resolves to “Fast Simulation of Bosonic Qubits via Gaussian Functions in Phase Space,” not Maria Schuld’s paper. The cited Schuld work is verifiable as `arXiv:2101.11020`, not under the supplied PRX Quantum record.
- `banchi2021generalization`: DOI/article `10.1103/PhysRevLett.127.190501` identifies a different paper. The correct record for the stated title is PRX Quantum 2, 040321, DOI `10.1103/PRXQuantum.2.040321`.[^2]
- `bremner2016average`: the DOI and authors are real, but the published PRL title is “Average-Case Complexity Versus Approximate Simulation of Commuting Quantum Computations,” not the title in the bibliography.[^3]
- `holmes2022connecting`: the DOI is real, but the published title is “Connecting Ansatz Expressibility to Gradient Magnitudes and Barren Plateaus,” not the title supplied.[^4]
- `thanasilp2024exponential`: the DOI is real, but the published title is “Exponential concentration in quantum kernel methods”; the bibliography uses the earlier preprint title while presenting the Version of Record metadata.[^5]

**Why it matters:** These are not house-style imperfections. At least two DOI/article-number pairs lead readers to wholly unrelated papers, and the pattern undermines confidence that cited sources were actually checked.

**Evidence:** Direct DOI/Crossref metadata and arXiv records.

**Severity:** Critical

**Recommended action:** Rebuild the affected records from the publisher or Version of Record pages, then perform a second full bibliography audit. Preserve evidence of the checks (publisher URL, DOI resolution, title, authors, year, volume/article number).

## Major Issues

### 4. The manuscript is at high risk of an MLST scope/novelty desk rejection

**Location:** Title, Abstract, Summary of Contributions, Related Work, and submission positioning.

**Problem:** The paper applies standard PCA, SVC, Qiskit `zz_feature_map`, exact statevector fidelity kernels, standard metrics, and standard kernel diagnostics to a single 569-instance benchmark. The contributions are chiefly protocol discipline, reporting, and packaging. No new learning method, quantum circuit, estimator, theorem, dataset, or scientific/clinical finding is introduced.

**Why it matters:** MLST states that papers are expected either to make conceptual or methodological advances in machine learning motivated by scientific problems, or to advance the state of the art of ML-driven scientific applications. It also says incremental steps are usually insufficient.[^6] A controlled single-dataset negative benchmark may be useful, but the manuscript does not demonstrate that it crosses this threshold.

**Evidence:** The paper’s five claimed contributions are implementation/control choices and analyses rather than a new method. It does not outperform prior approaches, deliver external validation, or derive a new general result.

**Severity:** High

**Recommended action:** Before investing in stylistic revision, obtain an editorial presubmission-scope opinion or choose a venue that explicitly values reproducibility/negative benchmark studies. If retaining MLST, sharpen the methodological novelty and show why the result changes current QML benchmarking practice beyond this one dataset.

### 5. Inferential statistics are not valid confirmation and add limited information

**Location:** Abstract; Paired Inferential Statistical Analysis (PDF p. 14); Discussion; Conclusion.

**Problem:** There are only five split-level observations, the splits overlap heavily, and the tested architecture was selected on those same test outcomes. A Wilcoxon signed-rank test and bootstrap over five dependent split-level differences do not supply confirmatory uncertainty. The paper acknowledges all three facts, but still foregrounds exact and Holm-adjusted p-values in the abstract and labels the section “Inferential.”

**Why it matters:** Readers can easily interpret the positive bootstrap interval as evidence that conflicts with the non-significant Wilcoxon result. Neither procedure models the dependence or post-selection. The p-value calculation is arithmetically correct; the problem is the sampling interpretation.

**Evidence:** Recalculation reproduces `W=0`, raw `p=0.0625`, Holm `p=0.1875`, and the reported percentile intervals. Pairwise train overlap is 358–367 of 455 observations, as stated.

**Severity:** High

**Recommended action:** Treat these strictly as descriptive split summaries unless a new independent nested evaluation is run. If inference remains, justify the resampling unit and dependence correction, and avoid placing the exploratory p-values in the abstract as if they were confirmatory tests.

### 6. “Five outer cross-validation splits” is inaccurate terminology

**Location:** Conclusion (line 450), Threats to Validity (line 437), captions and surrounding prose.

**Problem:** The design uses five independently seeded stratified 80/20 repeated holdouts, not five folds of a cross-validation partition. Test sets overlap; each observation is not assigned once to one of five disjoint test folds.

**Why it matters:** Calling the design cross-validation can make the effective sample coverage and dependence sound stronger than they are.

**Evidence:** Stored split manifests show overlapping training and test membership.

**Severity:** High

**Recommended action:** Use “five repeated stratified holdout splits” consistently. Reserve “fold” for the five-fold inner CV.

### 7. Data/code availability claims overstate what the tagged release contains

**Location:** Data Availability Statement, PDF p. 17; line 460.

**Problem:** The statement says *all derived data*—including “Centered Kernel Alignment matrices” and model predictions—are in release `v1.0.0`. The tagged release contains per-seed CKA scalar summaries and a heatmap, but not the full classical and quantum Gram matrices. It contains canonical Phase 11 test predictions, not predictions for every ablation/scaling run. “All derived data” is therefore not accurate.

**Why it matters:** Availability statements are formal publication assertions. Overclaiming artifacts that do not exist reduces reproducibility and credibility.

**Evidence:** The remote tag exists, and it contains the code, manifests, raw search/ablation/scaling tables, canonical predictions, and summaries. No Gram/CKA matrix data files are present; only `final_kernel_comparison.csv` and a plotted heatmap are stored.

**Severity:** High

**Recommended action:** Either deposit the claimed matrices/predictions and mint a corrected release, or narrow the statement to an exact inventory of what is actually archived. Prefer an immutable archival DOI (for example, Zenodo) over a mutable repository landing page.

### 8. The runtime comparison is not reproducible as a hardware benchmark

**Location:** Computational Execution Cost (PDF p. 13), Supplementary Table S2, reproducibility documentation.

**Problem:** The manuscript reports “standard x86_64 architecture” without CPU model, core/thread use, RAM, BLAS backend, operating system build, power state, number of timing repetitions/warm-ups, or isolation method. Supporting documentation says “Intel Core i7 / AMD Ryzen,” which is not a machine specification. The stated complexity row covers Gram multiplication but omits statevector-generation complexity even though generation is included in total time.

**Why it matters:** Ratios of 47–80× are hardware-, library-, and measurement-sensitive. Another researcher can reproduce the algorithms, but not meaningfully reproduce or compare those timings.

**Evidence:** Environment manifests preserve package versions but no specific CPU or timing protocol.

**Severity:** High

**Recommended action:** Add a complete hardware/software timing environment and protocol. Keep timing as implementation-specific profiling, not a general computational comparison.

### 9. Journal formatting/readability requirements are not met

**Location:** Entire PDF and Supplement.

**Problem:** The manuscript is compiled at 11 pt, while current MLST guidance asks for at least 12 pt for reviewer readability.[^6] Several wide tables are shrunk with `\resizebox{\textwidth}{!}`, producing very small text. Supplementary Table S1 is particularly dense. Supplement p. 1 has a large unused lower half; p. 2 packs two tiny tables; the long supplementary title does not satisfy IOP’s requested short supplementary-file title (maximum 30 characters), and no ≤30-word file description is included.[^6]

**Why it matters:** This can trigger a technical return and makes close review of numerical content unnecessarily difficult.

**Evidence:** Source uses `\documentclass[11pt,a4paper]{article}`; rendered PDF inspection confirms dense reduced tables and the supplement pagination issue.

**Severity:** High

**Recommended action:** Reformat only after scientific corrections: use at least 12 pt, redesign rather than scale wide tables, and supply the required short supplement title/description.

### 10. Most figures/tables are not explicitly cited by number in the prose

**Location:** Feature-map ablation, sample-size scaling, kernel geometry/alignment, runtime, statistical analysis, and supplement.

**Problem:** Automated label/reference checking found labels for `fig:ablation`, `fig:scaling`, `fig:heatmaps`, `fig:runtime`, `tab:ablation`, `tab:cka`, and `tab:paired_stat` that are never invoked with `\ref{...}`. The supplement similarly presents tables/figures without narrative cross-references.

**Why it matters:** IOP expects tables and figures to be numbered and referred to in the text.[^6] Merely placing an object under a nearby heading is weaker than explaining what the reader should inspect.

**Evidence:** Ten labels are defined in the main LaTeX source, but only three label keys are referenced.

**Severity:** High

**Recommended action:** Add an explicit first callout and interpretive sentence for every display item; consider moving nonessential material to the supplement.

### 11. The software citation does not match the software actually used

**Location:** `qiskit2023`; method section (line 150); environment manifest.

**Problem:** DOI `10.5281/zenodo.2573505` resolves in DataCite to `Qiskit/qiskit-metapackage: Qiskit 0.44.0` (2023), while the experiments used Qiskit 2.5.0. DataCite lists the version-specific Qiskit 2.5.0 record as DOI `10.5281/zenodo.21139412` (2026). The generic author/title in the BibTeX entry masks the version mismatch.

**Why it matters:** Version-sensitive APIs and circuit implementations are central to reproducibility.

**Evidence:** DataCite metadata and `results/phase11_manifest.json`.

**Severity:** High

**Recommended action:** Cite the exact Qiskit version used and separately cite Qiskit Machine Learning 0.9.0 or its software paper/release where appropriate.

### 12. Related work does not establish a sufficiently specific novelty gap

**Location:** Related Work, PDF pp. 3–4.

**Problem:** The section is broad but shallow. It summarizes kernel theory, concentration, small-data bounds, three oncology examples, and one broad benchmark. It does not systematically compare prior WDBC QSVC studies by split design, preprocessing, tuning, feature map, simulator/hardware, and outcome. It also omits a direct methodological comparison table in the manuscript.

**Why it matters:** Without a specific gap, the novelty reads as “we did a more careful benchmark,” which is difficult to distinguish from incremental replication.

**Evidence:** The repository has an internal novelty matrix, but its distinctions are not developed in the submitted manuscript.

**Severity:** High

**Recommended action:** Re-audit the literature after fixing the bibliography, then state precisely which prior result is being tested or corrected and which design defect this study resolves.

## Minor Issues

### 13. AI-like polish and templated emphasis reduce authorial credibility, but are not proof of AI authorship

**Location:** Throughout; especially lines 53–64, 68, 230–237, 295–299, 314–317, 350–355, 367–373, 396–403, and 422–455.

**Problem:** The manuscript repeatedly uses formulaic signposting (“To address these methodological shortcomings,” “To guide this controlled comparative investigation,” “A vital theoretical distinction must be maintained,” “To maintain scientific rigor, we explicitly enumerate...”), Title Case lead-ins, exhaustive enumerations, and repeated words such as “controlled,” “canonical,” “explicitly,” “strict,” “comprehensive,” and “systematically.” Some passages sound polished but institutional rather than authored; others repeat caveats already stated several times.

**Why it matters:** Reviewers may infer AI assistance or defensive over-engineering. More importantly, repetitive assurance language can backfire when a key assurance (“leakage-free”) is not true.

**Evidence:** Stylistic pattern across otherwise technically dense sections; no detector score was used.

**Severity:** Medium

**Recommended action:** Later, replace assurance language with concrete methods/evidence, reduce repeated caveats, and vary paragraph structure. This is a writing-quality issue unless undisclosed AI use occurred.

### 14. Several descriptions are stronger than the design supports

**Location:** Lines 193, 233, 258, 370, 402, 447–455.

**Problem:** “Exhaustive” applies only to the small chosen grid; “collapse severely,” “substantial lead at every evaluated sample size,” and “highly consistent ... advantage” are rhetorically stronger than needed; “leakage-free” is inaccurate. “Sample efficiency” is inferred from five points and one nested subsample path per seed, not estimated through formal learning-curve modeling.

**Why it matters:** These phrases invite criticism for overclaiming even where the underlying numbers are correct.

**Evidence:** The manuscript itself limits generalization to the tested grid and five dependent splits.

**Severity:** Medium

**Recommended action:** Use design-bounded descriptive language and reserve “efficiency” for a prespecified learning-curve estimand.

### 15. Dataset provenance should cite the dataset record directly

**Location:** Dataset section and Data Availability Statement.

**Problem:** The paper cites the 1993 introductory article and scikit-learn, but not the UCI dataset record that it explicitly names. The current UCI record supplies DOI `10.24432/C5DW2B` and a CC BY 4.0 license.[^7]

**Why it matters:** Direct dataset citation supports provenance, licensing, and credit.

**Evidence:** UCI’s official record.

**Severity:** Medium

**Recommended action:** Add the UCI dataset citation and state the applicable license accurately.

### 16. “Patient observations” is more specific than the dataset record establishes

**Location:** Dataset section, line 107.

**Problem:** The UCI record describes 569 instances/cases derived from FNA images. “Patient observations” may imply verified one-patient-per-row clinical sampling information that is not documented in the manuscript.

**Why it matters:** Biomedical wording should not add undocumented clinical structure.

**Evidence:** UCI metadata describes instances and FNA-derived features, not a clinical cohort protocol.

**Severity:** Low

**Recommended action:** Use “instances” or “cases” unless patient-level uniqueness is verified from the source documentation.

### 17. One valid bibliography entry is never cited

**Location:** `thanasilp2023subtleties`.

**Problem:** There are 36 BibTeX entries but only 35 unique citation keys in the manuscript; this entry is unused.

**Why it matters:** Minor bibliography hygiene issue and a sign that automatic “all references verified” checks only tested key existence, not use or metadata validity.

**Evidence:** Citation-key comparison.

**Severity:** Low

**Recommended action:** Cite it where substantively needed after reading it, or remove it.

### 18. The abstract is dense and reads like a compressed audit trail

**Location:** Abstract, PDF p. 1.

**Problem:** At approximately 234 words it meets the journal’s 300-word limit, but it packs protocol, six numerical findings, inference caveats, selection caveats, geometry, runtime interpretation, and conclusion into one block.

**Why it matters:** It is technically complete but cognitively dense; the contribution and novelty are less visible than the audit details.

**Evidence:** Manual reading and word count.

**Severity:** Low

**Recommended action:** During revision, prioritize objective, design, primary result, and bounded implication; move secondary geometry/ablation detail to the main text.

## Citation / Reference Audit

### Inventory-level findings

- **36 BibTeX entries; 35 cited; 1 uncited.**
- **No in-text citation key is missing from the `.bib` file.** This syntactic check passes but does not validate references.
- **One apparent non-existent/composite reference:** `canatar2023spectral`.
- **Two DOI/article-number pairs resolve to unrelated papers:** `schuld2021supervised`, `banchi2021generalization`.
- **Three Version-of-Record title mismatches:** `bremner2016average`, `holmes2022connecting`, `thanasilp2024exponential`.
- **One software-version mismatch:** `qiskit2023` cites Qiskit 0.44.0 while the study used 2.5.0.
- **One direct dataset citation is missing:** UCI WDBC DOI `10.24432/C5DW2B`.

### Entry-by-entry audit

| Key | Status | Verification and claim-support assessment |
|---|---|---|
| `street1993nuclear` | Verified | DOI, authors, year, volume, and pages resolve; supports feature provenance. Add the separate UCI dataset record for the dataset itself. |
| `cortes1995support` | Verified | Correct foundational SVM record and appropriate support. |
| `scholkopf2002learning` | Verified | Real MIT Press book; appropriate foundational support. |
| `cristianini2000introduction` | Verified | DOI resolves to the stated Cambridge book; appropriate kernel-method support. |
| `guyon2002gene` | Verified, claim partly indirect | Correct record. Supports SVMs in cancer classification, but does not by itself justify the exact RBF search grid. |
| `chang2011libsvm` | Verified | Correct LIBSVM article and appropriate implementation support. The manuscript’s broad complexity range remains an approximation. |
| `pedregosa2011scikit` | Verified | Correct JMLR paper; supports library attribution, not every leakage-prevention prescription attributed nearby. |
| `havlicek2019supervised` | Verified | Correct Nature paper; supports quantum feature maps/kernels. |
| `schuld2019quantum` | Verified | Correct PRL paper; supports Hilbert-space kernel framing. |
| `schuld2021supervised` | Incorrect | Title/author refer to a real arXiv paper (`2101.11020`), but journal, volume, article number, and DOI point to an unrelated paper. Claims are potentially supportable after correct citation and re-reading. |
| `huang2021power` | Verified | Correct Nature Communications record; appropriate for data-dependent QML advantage and projected-kernel discussion. |
| `liu2021rigorous` | Verified | Correct Nature Physics record; supports existence of rigorous quantum speedup under specialized assumptions, not a generic practical advantage. Manuscript wording is adequately cautious. |
| `suzuki2020analysis` | Verified | Correct Quantum Machine Intelligence record and relevant feature-map support. |
| `bremner2016average` | Incorrect title | DOI/authors/year are real, but the published title is wrong. Substantive IQP/commuting-circuit support is broadly relevant. |
| `perezsalinas2020data` | Verified | Correct Quantum article; supports data re-uploading. |
| `hubregtsen2021evaluation` | Verified | Correct record; broadly supports non-monotonic relations among expressibility, entanglement, and accuracy. Avoid overstating it as a universal result. |
| `peters2021machine` | Verified, claim partly indirect | Correct npj Quantum Information record. Relevant to noisy hardware, but not the primary source for the local statevector implementation. |
| `qiskit2023` | Incorrect version | DOI is real but resolves to Qiskit 0.44.0; experiments report Qiskit 2.5.0. Replace with the exact release citation. |
| `thanasilp2024exponential` | Incorrect published title | DOI/authors/year/article are real; use the published title. Claims are appropriately bounded and substantively supported. |
| `thanasilp2023subtleties` | Verified but uncited | Correct-looking DOI record; not cited anywhere in the manuscript. |
| `kubler2021inductive` | Verified | Real NeurIPS 2021 paper; supports inductive-bias/alignment discussion. |
| `shaydulin2022importance` | Verified | Correct PRA record; supports bandwidth/input-scaling importance. |
| `holmes2022connecting` | Incorrect title | DOI/authors/year are real; published title is “...Gradient Magnitudes and Barren Plateaus.” Relevant to barren-plateau context, but it is not a quantum-kernel concentration paper. |
| `mcclean2018barren` | Verified | Correct Nature Communications record; appropriate barren-plateau foundation. |
| `caro2022generalization` | Verified | Correct Nature Communications record; supports generalization bounds. |
| `banchi2021generalization` | Incorrect venue/DOI | Stated title/authors are real, but the correct publication is PRX Quantum 2, 040321; supplied PRL DOI points elsewhere. |
| `canatar2023spectral` | Apparently non-existent/composite | No matching record; DOI points elsewhere; title/authors appear blended from other papers. Critical. |
| `leither2026benchmarking` | Verified preprint | arXiv `2608.11373`, posted 11 August 2026, title and authors match. Appropriate but very recent and not peer reviewed in the cited form. |
| `wang2024novel` | Verified | Correct Physica Scripta record and article number `056006`; relevant oncology QSVM comparison. |
| `azevedo2022quantum` | Verified | Correct Quantum Machine Intelligence record; manuscript correctly notes its different mammography task. |
| `bowles2024better` | Verified preprint | arXiv `2403.07059`, title/authors match. Supports benchmarking rigor. Avoid treating its recommendations as validation of this specific five-seed scheme. |
| `cerezo2022challenges` | Verified | Correct Nature Computational Science record; appropriate broad QML limitations context. |
| `preskill2018quantum` | Verified | Correct Quantum article; appropriate NISQ context, but does not specifically justify choosing 2 and 4 PCA dimensions. |
| `aaronson2015read` | Verified | Correct Nature Physics commentary; appropriate speedup caveat. |
| `tang2019quantum` | Verified | Correct STOC paper and DOI; appropriate dequantization example. |
| `cortes2012centered` | Verified | Correct JMLR article and URL; appropriate primary centered-alignment source. |

### Citation-content mismatches and missing citations

1. The effective-rank/spectral-learning claim currently depends partly on the non-existent `canatar2023spectral` entry. It needs a real primary source and a sentence-level support check.
2. The precise custom implementation and version-sensitive Qiskit behavior should be supported by exact Qiskit/Qiskit Machine Learning release documentation or software citation, not a Qiskit 0.44.0 record.
3. The WDBC dataset itself needs its official UCI dataset citation and license, not only the introductory paper and scikit-learn article.
4. The chosen numerical search grids, seed list, and selection family are design choices; citations to Bowles/Guyon should not imply those sources prescribe these exact values.

## AI-Related Risk Assessment

### Suspicious writing sections

| Location / identifier | Severity | Classification | Why it may look suspicious or weak |
|---|---:|---|---|
| Lines 53–64, “To address these methodological shortcomings...” and five contribution bullets | Medium | Polished / potentially templated | Dense promotional signposting, repeated “controlled,” and balanced five-part taxonomy resemble generated academic scaffolding. Content is concrete, so style alone is not an integrity concern. |
| Lines 67–77, seven RQs | Low–Medium | Academically over-structured | Several RQs simply partition analyses already decided (cost, geometry, alignment, stability) rather than expressing distinct hypotheses. This can look generated, but is mainly a structural issue. |
| Lines 230–237, “acute interaction,” “collapse severely,” “concentration-like” | Medium | Academically weak wording | Rhetorical intensity exceeds a small descriptive ablation. The later caveat is good; the strong wording is unnecessary. |
| Lines 295–299 and 396–403, numbered synthesis/limitations | Medium | Repetitive generated-prose risk | Restates table values and caveats in highly regular lead-in/value format. Content is accurate but over-produced. |
| Lines 314–317, “A vital theoretical distinction must be maintained” | Low | Polished | The explanation is substantive and mathematically useful; only the ceremonial transition sounds synthetic. |
| Lines 422–455, scope/limitations/conclusion | Medium | Repetitive generated-prose risk | The same boundary conditions and “no quantum advantage” conclusion recur in three adjacent sections. |

**Distinction required by the evidence:** The prose contains markers of AI-assisted drafting, but these markers do not establish authorship or misconduct. The genuine integrity concern is the combination of polished assurance language, a composite reference, multiple wrong DOI mappings, and no AI disclosure *if* AI actually generated or edited manuscript content or references.

### Current IOP policy

IOP currently permits authors to use generative AI to edit human-written text, generate text that the authors critically revise, generate figures from existing data, and support literature searching. Every such use must be disclosed in the Acknowledgements with the model, version, and use. Authors remain responsible for accuracy, originality, and plagiarism checks.[^1]

IOP prohibits AI authorship, fabrication/manipulation of data, AI generation of reference lists, uploading actual reviewer reports to generative-AI tools, AI generation of substantive reviewer responses, and hidden prompts intended to manipulate review.[^1]

### Policy classification for this submission

- **Definitely prohibited:** AI authorship; fabricated/manipulated results; AI-generated reference lists; hidden reviewer-manipulation prompts. No AI author or hidden prompt was found, and no result manipulation was evidenced. Whether the bibliography was AI-generated is unknown.
- **Permitted with disclosure:** AI editing/generation of manuscript text, AI-generated figures based on existing data, and AI-supported literature search. The current Acknowledgements contain no disclosure.
- **Normally permitted without an AI-specific concern:** Deterministic Matplotlib plots produced by repository code from measured CSV data. These are not generative-AI figures.
- **Requires author confirmation:** Whether any generative AI was used; which model/version; whether it generated or merely located references; whether prompts/drafts were retained; and whether the provider’s terms grant only the rights IOP permits.

**Recommended action:** If any covered AI use occurred, add a precise disclosure before submission. If an AI generated any reference-list content, manually rebuild and verify the entire bibliography; disclosure does not cure prohibited reference generation.

## Plagiarism / Originality Risk

- **No apparent issue:** No passage was identified for which there is evidence of verbatim copying or too-close paraphrase.
- **Needs citation:** Dataset licensing/provenance and version-specific software behavior need direct primary citations as noted above.
- **Potential originality concern:** The paper’s protocol contribution may be established good practice rather than a novel method. That is a novelty/positioning problem, not plagiarism.
- **Requires manual plagiarism-checking:** A repository and open-web review cannot search subscription corpora, theses, conference submissions, or all published text. Run iThenticate or the journal’s accepted similarity workflow before submission, then manually inspect matches. Do not treat a similarity percentage alone as proof.

## Methodology Review

### Defensible components

- Malignant label 0 is consistently treated as the positive class, and decision scores are correctly oriented for ROC-AUC.
- Preprocessing is fitted on training partitions only; inner CV refits StandardScaler, PCA, MinMaxScaler, and quantum kernels per fold.
- Classical Linear/RBF family and hyperparameters are selected using inner malignant-F1 only, with deterministic tie rules.
- Quantum `C` is tuned inside inner CV.
- Test partitions and seeds are aligned for paired descriptive comparison.
- Exact statevector kernels are clearly distinguished from noisy sampling and hardware execution.
- Raw candidate/fold results, selected configurations, predictions, and summary artifacts are persisted.
- Claims about concentration and causality are mostly bounded appropriately.

### Non-defensible or only exploratory components

- The final QSVC architecture is selected on the outer-test splits and evaluated again on them.
- Five overlapping repeated holdouts do not provide five independent experimental replicates.
- The bootstrap over five dependent split-level effects and Wilcoxon test do not support confirmatory population inference.
- Sample-size “efficiency” uses one nested subset path per outer seed and fixed hyperparameters; it is a descriptive learning-curve exercise.
- No external dataset/cohort tests generalization.
- Runtime comparisons lack hardware/timing protocol and exclude search costs from the headline total.
- The comparison establishes only that tested classical SVMs outperform this selected ZZ-map implementation under these conditions. It does not test broad “classical versus quantum ML” superiority.

### Research question assessment

The objective is clear and meaningful as a reproducibility benchmark. The method answers a narrow descriptive question about this dataset and implementation. It does not support confirmatory statistical claims, broad quantum-advantage conclusions, clinical claims, or a general scaling claim. The paper mostly acknowledges these boundaries, but its “strict/leakage-free/canonical” framing contradicts them.

## Results Integrity

### Confirmed

- Central means and sample standard deviations in the main performance table match `final_model_comparison.csv` at displayed precision.
- Ablation, sample-size, CKA, effective-rank, runtime, paired-difference, Wilcoxon, Holm, and bootstrap values checked in the repository agree with their underlying summary files at displayed precision.
- The classical comparator has higher malignant F1 on all five stored matched splits for PCA 2 and PCA 4.
- No suspiciously perfect model result occurs.
- The repository validation script passes, submission-package check passes, and 23 tests pass.

### Integrity limitations

- Correct arithmetic does not repair post-selection on outer tests.
- “All derived data” is not deposited as claimed.
- The manuscript’s internal automated citation check only confirms that citation keys resolve inside BibTeX; it failed to catch wrong DOI metadata and a composite reference.
- The old notebook contains historical 2-repetition experiments before the final 1-repetition configuration. These are labeled as phases, but a new reproducer can confuse historical checkpoints with canonical results unless the final reproduction path is followed exactly.

## Figures, Tables, and Data

- All main and supplementary figures appear to be code-generated from project results; no reused photograph or third-party figure requiring permission was identified.
- Axes, metric ranges, model labels, and error-bar descriptions are generally present.
- Captions usually state the estimand and limitation (for example, sample SD rather than confidence intervals).
- Several displays rely on color, although labels/positions also convey categories. Line-style/marker redundancy should be checked in grayscale.
- Main and supplementary tables are visually dense and reduced below comfortable review size.
- Seven main display labels and the supplementary displays lack explicit prose references.
- Heatmaps show only 50 samples and correctly say the aggregate CKA uses all 455; this is an appropriate illustrative/analysis distinction.
- No full Gram matrices underlying the heatmaps/CKA are archived despite the availability statement.

## Academic Writing Quality

The prose is grammatically strong and technically literate. Its main weaknesses are over-structuring, repetitive self-assurance, excessive reuse of caveats, dense abstracting, and occasional loaded words (“acute,” “collapse,” “exhaustive”). The paper often tells the reader that it is rigorous rather than allowing the protocol and evidence to demonstrate rigor. Later revision should prioritize accuracy and compression, not merely stylistic polish.

Terminology is mostly consistent, with three important exceptions:

1. Repeated holdout splits are sometimes called cross-validation splits.
2. “Leakage-free” conflicts with feature-map selection on outer-test outcomes.
3. “Canonical” can sound prespecified even though the architecture was selected after Phase 9 test results.

## Reproducibility Assessment

**Assessment: Partially reproducible; algorithms/results are reproducible, the submission claims and timings are not fully reproducible.**

Another researcher can obtain the dataset through scikit-learn, inspect fixed seeds and split indices, rerun the main scripts, and verify the frozen numeric outputs. The remote `v1.0.0` tag exists, the package versions and dataset/implementation hashes are recorded, and the test suite passes.

Reproducibility is weakened by:

- absence of a precise hardware/timing protocol;
- no archived full kernel matrices despite claiming them;
- no immutable archival DOI cited for the repository release;
- an incorrect Qiskit version citation;
- wrong/non-existent scholarly metadata;
- the notebook’s long historical sequence and mixed earlier/final configurations;
- no newly executed full notebook run was performed during this read-only audit because it would regenerate and overwrite tracked result artifacts. Validation of frozen outputs and all focused tests was performed instead.

## Novelty Assessment

**Novelty is clear at the level of packaging and protocol discipline, but weak at the scientific-method level.**

The manuscript’s useful contribution is a transparent negative case study showing that a common low-dimensional ZZ fidelity kernel does not outperform tuned classical SVMs on WDBC under the tested conditions. The operator-space explanation, geometry diagnostics, and explicit dependence caveats improve the work.

However, these elements are applications of existing methods, not a new method. The study does not demonstrate a new quantum phenomenon, introduce a benchmark suite, or overturn a specific published WDBC result under matched conditions. The novelty statement therefore risks appearing exaggerated for MLST. A more suitable claim is likely “auditable replication/negative benchmark” unless the scope is expanded with independent datasets or a genuinely new methodological contribution.

## Related-Work Quality

The section includes foundational SVM/kernel work, core quantum-kernel papers, concentration/generalization theory, empirical benchmarking, and selected oncology applications. Its organization is sensible.

Its weaknesses are:

- a critical composite/non-existent citation and several corrupted publication records;
- inadequate comparison of this protocol against prior WDBC-specific QSVC studies;
- dependence on preprints for the newest broad benchmarking evidence;
- no manuscript-level evidence matrix linking prior design limitations to the claimed contribution;
- only limited discussion of trainable/projected kernels and other classical baselines that define the boundary of the negative result.

The section must be re-audited after references are repaired. A longer bibliography is not automatically better; source accuracy and direct relevance matter more.

## Confidentiality / Ethical Concerns

- The study uses a public benchmark and collects no new participant data. No names, IDs, images of identifiable participants, or private clinical records are included.
- The ethics statement is broadly adequate for a methodological secondary-data benchmark, subject to the author’s institutional/journal requirements.
- The corresponding author’s email and ORCID are ordinary submission metadata, not an inappropriate disclosure.
- The UCI dataset is CC BY 4.0 and requires attribution; cite the dataset DOI and license explicitly.[^7]
- Repository code is licensed, but the availability statement should distinguish project code/results from third-party dataset rights.
- IOP warns that uploading manuscript material to generative-AI systems can expose third-party rights/confidential material. No actual confidential peer-review report was supplied here, but the author should confirm that any AI provider terms are compatible with IOP’s rights requirements.[^1]

## Internal Consistency

### Confirmed inconsistencies

1. **Leakage claim:** lines 123–125 and the conclusion say outer tests were quarantined during all selection / the comparison is leakage-free; lines 128, 190, and 436 admit feature-map architecture selection on those outer tests.
2. **Design name:** “outer cross-validation splits” versus the actual overlapping repeated holdouts.
3. **Data availability:** claims full CKA matrices and all derived data, but only per-seed scalar summaries/heatmap and selected prediction files are archived.
4. **Software citation:** Qiskit 0.44.0 citation versus Qiskit 2.5.0 execution manifest.
5. **Supporting documentation:** `docs/methodology.md` says outer-test metrics never select models, contradicting the manuscript’s Phase 9 selection disclosure.
6. **Reference metadata:** multiple title/DOI/article-number conflicts described above.

### Items checked with no material inconsistency found

- Dataset size 569, feature count 30, and class counts 212/357.
- Outer train/test sizes 455/114 and inner sizes 364/91.
- Positive-class definition and ROC-AUC direction.
- PCA dimensionalities and reported explained-variance summaries.
- Five seeds `[42, 123, 456, 789, 2026]`.
- Core F1, ROC-AUC, ablation, CKA, effective-rank, runtime, and statistical values.
- Figure/CSV values at displayed precision.

## Submission Risk Score

| Risk | Score (0–10) | Rationale |
|---|---:|---|
| Academic integrity risk | **6/10** | No evidence of data fabrication or plagiarism, but a composite reference, multiple false DOI mappings, overbroad availability claims, and potentially undisclosed AI use create real integrity exposure. |
| Citation risk | **8/10** | At least one apparently non-existent record, two DOIs pointing to unrelated papers, three published-title mismatches, one software-version mismatch, and a missing dataset citation. |
| Methodology risk | **8/10** | Outer-test architecture selection invalidates confirmatory evaluation; five dependent holdouts and no external validation sharply limit inference. Strong preprocessing controls prevent an even higher score. |
| Writing-quality risk | **5/10** | Grammar and technical clarity are good, but prose is repetitive, over-structured, defensive, and occasionally overclaims. |
| Reproducibility risk | **5/10** | Code, seeds, manifests, raw tables, and tests are strong; hardware timing, claimed matrices, exact software citation, and mixed notebook history remain deficient. |
| AI-policy risk | **7/10** | Conditional on actual AI use: IOP requires disclosure and forbids AI-generated reference lists. The manuscript has no disclosure and contains citation patterns consistent with unverified generation, but authorship method is not proven. |
| Overall rejection risk | **9/10** | Current MLST submission faces probable desk/reviewer rejection from citation integrity, post-selection evaluation, and weak journal-level novelty/scope, plus avoidable format noncompliance. |

## Priority Fix List

### P0 — Must fix before submission

- [ ] Resolve and replace the non-existent/composite `canatar2023spectral` citation after reading the real source(s).
- [ ] Correct every wrong DOI/title/venue/article-number record, especially Schuld, Banchi, Bremner, Holmes, and Thanasilp.
- [ ] Manually verify all 36 references against primary publisher/arXiv records and preserve a verification log.
- [ ] Decide whether to rerun a genuinely nested/independent evaluation. If not, remove all claims that the full comparison is leakage-free, strict nested CV, or confirmatory.
- [ ] Correct the Data Availability Statement or deposit the artifacts it claims.
- [ ] Confirm whether generative AI was used. If yes, add the IOP-required model/version/use disclosure; if AI generated references, rebuild the list manually.
- [ ] Reassess venue fit against MLST’s stated novelty threshold before submission.

### P1 — Strongly recommended

- [ ] Replace “outer cross-validation splits” with “repeated stratified holdout splits.”
- [ ] Reframe or remove inferential p-values/bootstraps unless supported by a valid independent design.
- [ ] Add exact CPU/RAM/OS/BLAS/timing protocol details.
- [ ] Cite the UCI WDBC dataset DOI and CC BY 4.0 license.
- [ ] Cite Qiskit 2.5.0 and Qiskit Machine Learning 0.9.0 accurately.
- [ ] Add explicit prose callouts for every figure and table.
- [ ] Reformat to at least 12 pt and redesign wide tables for legibility.
- [ ] Supply an IOP-compliant short supplementary title and description.
- [ ] Strengthen the prior-work comparison around WDBC-specific and controlled QML benchmarks.
- [ ] Use an immutable archival repository DOI for the exact submission release.

### P2 — Improvements / polish

- [ ] Reduce repeated claims of rigor and repeated limitation lists.
- [ ] Replace loaded wording such as “collapse severely,” “acute interaction,” and “exhaustive” with bounded descriptions.
- [ ] Simplify the abstract and foreground the actual contribution/novelty.
- [ ] Use “instances” or “cases” rather than “patient observations” unless patient uniqueness is documented.
- [ ] Remove the uncited bibliography entry or cite it substantively.
- [ ] Check all figures in grayscale and add redundant markers/line styles where needed.
- [ ] Run an authorized similarity check and manually review matches.

## Sources

[^1]: IOP Publishing, “[Generative AI Tools](https://publishingsupport.iopscience.iop.org/questions/generative-ai-tools/),” current policy accessed 11 September 2026.
[^2]: Banchi, Pereira, and Pirandola, “[Generalization in Quantum Machine Learning: A Quantum Information Standpoint](https://doi.org/10.1103/PRXQuantum.2.040321),” *PRX Quantum* 2, 040321 (2021).
[^3]: Bremner, Montanaro, and Shepherd, “[Average-Case Complexity Versus Approximate Simulation of Commuting Quantum Computations](https://doi.org/10.1103/PhysRevLett.117.080501),” *Physical Review Letters* 117, 080501 (2016).
[^4]: Holmes et al., “[Connecting Ansatz Expressibility to Gradient Magnitudes and Barren Plateaus](https://doi.org/10.1103/PRXQuantum.3.010313),” *PRX Quantum* 3, 010313 (2022).
[^5]: Thanasilp et al., “[Exponential concentration in quantum kernel methods](https://doi.org/10.1038/s41467-024-49287-w),” *Nature Communications* 15, 5200 (2024).
[^6]: IOP Publishing, “[Machine Learning: Science and Technology — Author Guidelines](https://publishingsupport.iopscience.iop.org/journals/machine-learning-science-and-technology/),” accessed 11 September 2026.
[^7]: UCI Machine Learning Repository, “[Breast Cancer Wisconsin (Diagnostic)](https://doi.org/10.24432/C5DW2B),” dataset record and CC BY 4.0 license.

**Verdict:** The empirical files appear numerically coherent, but the submission has serious reference-integrity, evaluation-design, and journal-fit defects.

**Safe to submit now:** No

**Most important issue:** The “canonical” QSVC architecture was selected on the same outer-test splits used for final evaluation, while the paper still describes the comparison as leakage-free.
