# Reference Integrity and Claim-Support Audit

Audit date: 12 September 2026. Scope: every one of the 36 scholarly/software entries in `paper/bibliography.bib` and the mirrored `paper/mlst/references.bib`, plus every substantive citation use in the manuscript. Metadata was rechecked from scratch against Crossref/DOI records and, where applicable, official publisher, MIT Press, JMLR, NeurIPS, arXiv, and PyPI records. “Qualified” means the source supports the narrowed wording now used, not a stronger causal or universal claim.

| Citation key | Existence | Authors | Title | Venue | Year | DOI/arXiv | Metadata status | Claim support status | Action taken |
|---|---:|---:|---:|---|---:|---|---|---|---|
| street1993nuclear | Yes | Yes | Yes | SPIE Proceedings 1905 | 1993 | 10.1117/12.148698 | Corrected type/venue | Supported | Set SPIE proceedings title and type |
| cortes1995support | Yes | Yes | Yes | Machine Learning 20(3) | 1995 | 10.1007/BF00994018 | Verified | Supported | None |
| scholkopf2002learning | Yes | Yes | Yes | MIT Press | 2002 edition | ISBN 978-0-262-19475-3 | Verified | Supported | None |
| cristianini2000introduction | Yes | Yes | Yes | Cambridge University Press | 2000 | 10.1017/CBO9780511801389 | Verified | Supported | None |
| guyon2002gene | Yes | Yes | Yes | Machine Learning 46(1--3) | 2002 | 10.1023/A:1012487302797 | Corrected issue | Qualified | Set issue 1--3; limited use to SVM/cancer context |
| chang2011libsvm | Yes | Yes | Yes | ACM TIST 2(3) | 2011 | 10.1145/1961189.1961199 | Verified | Qualified | Removed universal runtime bound from literature claim |
| pedregosa2011scikit | Yes | Yes | Yes | JMLR 12(85) | 2011 | Official JMLR record | Verified | Supported | Removed citation from project-specific leakage claim |
| havlicek2019supervised | Yes | Yes | Yes | Nature 567(7747) | 2019 | 10.1038/s41586-019-0980-2 | Verified | Supported | None |
| schuld2019quantum | Yes | Yes | Yes | Physical Review Letters 122(4) | 2019 | 10.1103/PhysRevLett.122.040504 | Verified | Supported | None |
| schuld2021supervised | Yes | Yes | Yes | arXiv | 2021 | arXiv:2101.11020 | Corrected publication type/identifier | Qualified | Removed false PRX Quantum metadata; cite as preprint |
| huang2021power | Yes | Yes | Yes | Nature Communications 12(1) | 2021 | 10.1038/s41467-021-22539-9 | Verified | Qualified | Scoped theoretical-advantage wording |
| liu2021rigorous | Yes | Yes | Yes | Nature Physics 17(9) | 2021 | 10.1038/s41567-021-01287-z | Verified | Supported (background) | None |
| suzuki2020analysis | Yes | Yes | Yes | Quantum Machine Intelligence 2(1) | 2020 | 10.1007/s42484-020-00020-y | Verified | Supported | None |
| bremner2016average | Yes | Yes | Corrected | Physical Review Letters 117(8) | 2016 | 10.1103/PhysRevLett.117.080501 | Corrected title | Qualified | Restored publisher title; retained conditional complexity wording |
| perezsalinas2020data | Yes | Yes | Yes | Quantum 4 | 2020 | 10.22331/q-2020-02-06-226 | Verified | Supported | None |
| hubregtsen2021evaluation | Yes | Corrected | Yes | Quantum Machine Intelligence 3(1) | 2021 | 10.1007/s42484-021-00038-w | Corrected author spelling | Qualified | Pichlmayr → Pichlmeier; no monotonic-causality claim |
| peters2021machine | Yes | Yes | Yes | npj Quantum Information 7(1) | 2021 | 10.1038/s41534-021-00498-9 | Verified | Qualified | Used only for simulator/hardware distinction and future work |
| qiskit2026 | Yes | Yes | Yes | PyPI software release | 2026 | Official 2.5.0 URL | Corrected software record | Supported | Replaced mismatched Zenodo/Qiskit-version citation with 2.5.0 release |
| thanasilp2024exponential | Yes | Yes | Corrected | Nature Communications 15(1) | 2024 | 10.1038/s41467-024-49287-w | Corrected title | Qualified | Use only for conditional/asymptotic concentration context |
| thanasilp2023subtleties | Yes | Corrected | Yes | Quantum Machine Intelligence 5(1) | 2023 | 10.1007/s42484-023-00103-6 | Corrected composite metadata | Supported (background) | Restored Samson Wang, QMI 5:21 and DOI |
| kubler2021inductive | Yes | Yes | Yes | NeurIPS 34 | 2021 | Official proceedings record | Verified | Qualified | Used for inductive bias/task alignment, not causal proof |
| shaydulin2022importance | Yes | Yes | Yes | Physical Review A 106(4) | 2022 | 10.1103/PhysRevA.106.042407 | Verified | Supported | None |
| holmes2022connecting | Yes | Yes | Corrected | PRX Quantum 3(1) | 2022 | 10.1103/PRXQuantum.3.010313 | Corrected title | Qualified | Used for barren-plateau distinction, not kernel diagnosis |
| mcclean2018barren | Yes | Yes | Yes | Nature Communications 9(1) | 2018 | 10.1038/s41467-018-07090-4 | Verified | Supported | None |
| caro2022generalization | Yes | Yes | Yes | Nature Communications 13(1) | 2022 | 10.1038/s41467-022-32550-3 | Verified | Qualified | Explicitly deny automatic comparative advantage |
| banchi2021generalization | Yes | Yes | Yes | PRX Quantum 2(4) | 2021 | 10.1103/PRXQuantum.2.040321 | Corrected DOI/article | Qualified | PRL mismatch replaced by PRX Quantum 2, 040321 |
| canatar2021spectral | Yes | Corrected | Corrected | Nature Communications 12(1) | 2021 | 10.1038/s41467-021-23103-1 | Replaced composite/nonexistent entry | Qualified | Cite as classical kernel-regression theory |
| leither2026benchmarking | Yes | Yes | Yes | arXiv | 2026 | arXiv:2608.11373 | Verified preprint | Supported | None |
| wang2024novel | Yes | Yes | Yes | Physica Scripta 99(5) | 2024 | 10.1088/1402-4896/ad36ef | Verified | Qualified | Describe different feature-selection objective |
| azevedo2022quantum | Yes | Yes | Yes | Quantum Machine Intelligence 4(1) | 2022 | 10.1007/s42484-022-00062-4 | Verified | Supported | Distinguish mammography from WDBC |
| bowles2024better | Yes | Yes | Yes | arXiv | 2024 | arXiv:2403.07059 | Verified preprint | Supported | None |
| cerezo2022challenges | Yes | Yes | Yes | Nature Computational Science 2(9) | 2022 | 10.1038/s43588-022-00311-3 | Verified | Supported | None |
| preskill2018quantum | Yes | Yes | Yes | Quantum 2 | 2018 | 10.22331/q-2018-08-06-79 | Verified | Qualified | Used for NISQ context, not measured runtime |
| aaronson2015read | Yes | Yes | Yes | Nature Physics 11(4) | 2015 | 10.1038/nphys3272 | Verified | Qualified | Used only for broad speedup caveats |
| tang2019quantum | Yes | Yes | Yes | ACM STOC 2019 | 2019 | 10.1145/3313276.3316310 | Verified | Supported | None |
| cortes2012centered | Yes | Yes | Yes | JMLR 13(28) | 2012 | Official JMLR record | Verified | Supported | None |

## Findings and disposition

The fresh audit found eleven materially incorrect or incomplete records: Street (type/venue), Guyon (issue), Schuld 2021 (false journal/DOI), Bremner (title), Hubregtsen (author spelling), Qiskit (version-inconsistent software citation), Thanasilp 2024 (title), Thanasilp 2023 (author/venue/DOI composite), Holmes (title), Banchi (journal/article/DOI), and the wholly composite Canatar record. Both BibTeX files and the Markdown reference list now agree.

Primary audit endpoints included the DOI records for all DOI-bearing publications; the official JMLR pages for `pedregosa2011scikit` and `cortes2012centered`; the official NeurIPS proceedings page for `kubler2021inductive`; the arXiv records for `schuld2021supervised`, `bowles2024better`, and `leither2026benchmarking`; the MIT Press catalog for `scholkopf2002learning`; and the exact PyPI 2.5.0 release record for `qiskit2026`. The Cambridge book DOI record was used for `cristianini2000introduction`.

Final state: **0 fabricated references; 0 composite references; 0 DOI mismatches; 0 article-number mismatches; 0 unresolved citation keys.** All central claim uses are either supported directly or explicitly qualified. No source is used to assert universal classical superiority, physical-QPU timing, clinical validity, or a causal concentration diagnosis.
