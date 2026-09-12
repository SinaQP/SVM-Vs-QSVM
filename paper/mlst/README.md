# MLST Submission Package

**Manuscript:** *A Controlled Empirical Comparison of Classical and Quantum Kernel SVMs for Breast Cancer Classification*  
**Target Journal:** *Machine Learning: Science and Technology* (IOP Publishing)  
**Intended Article Type:** Benchmark (subject to editor and submission-portal classification)
**Status:** Remediation complete and ready for independent read-only audit; not ready for submission

---

## Directory Structure

```text
paper/mlst/
├── manuscript.tex              # Main LaTeX manuscript prepared for MLST
├── manuscript.pdf              # Compiled submission PDF (text, tables, figures embedded)
├── references.bib              # 35-entry BibTeX database; 35 cited keys, 0 unresolved or unused keys
├── cover_letter.md             # Journal-specific cover letter
├── cover_letter.txt            # Plain-text cover-letter copy
├── cover_letter_notes.md       # Cover-letter claim and framing notes
├── figures/                    # Main manuscript publication figures (300 DPI)
│   ├── final_f1_comparison.png
│   ├── final_feature_map_ablation.png
│   ├── final_sample_size_scaling.png
│   ├── final_kernel_heatmaps.png
│   └── final_runtime_scaling.png
├── supplementary/              # Supplementary material document, tables, and figures
│   ├── supplementary_material.tex
│   ├── supplementary_material.pdf
│   ├── supplementary_material.md
│   ├── final_paired_f1_differences.png
│   └── final_roc_auc_comparison.png
├── submission_metadata.md      # Official submission metadata (title, abstract, keywords, classifications)
├── data_availability.md        # Formal Level 2 Data Availability Statement
├── author_declarations.md      # Author declarations (Ethics, Funding, COI, CRediT taxonomy)
├── submission_checklist.md     # Pre-submission checklist (READY / NEEDS USER REVIEW / BLOCKING)
└── README.md                   # This overview document
```

---

## Compilation Instructions

The LaTeX manuscript can be compiled using standard TeX engines (e.g., `tectonic`, `pdflatex`, or Overleaf):

### Using Tectonic (Recommended, Zero Configuration):
```bash
tectonic manuscript.tex
```

### Using Standard TeX Live / MiKTeX:
```bash
pdflatex manuscript.tex
bibtex manuscript
pdflatex manuscript.tex
pdflatex manuscript.tex
```

### Overleaf Submission:
Upload the entire contents of `paper/mlst/` (including `figures/` and `references.bib`) as a new project on Overleaf.

## Current IOP guidance used

The reviewer-format source uses 12-point body text in line with IOP's current request for a reasonable font size of at least 12 point: https://publishingsupport.iopscience.iop.org/questions/article-format/. MLST's current article-type page defines Benchmarks as comparative performance studies conducted on a consistent problem or dataset; this package therefore records Benchmark as the intended type, subject to editorial and portal classification: https://publishingsupport.iopscience.iop.org/journals/machine-learning-science-and-technology/about-machine-learning-science-technology/.

---

## Preservation of Generic Research Assets

* The canonical venue-neutral manuscript remains intact at `paper/manuscript.md`.
* All underlying empirical research, canonical tables, and frozen artifacts remain untouched at `v1.0.0` (`results/final/`).
