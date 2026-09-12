# Generative-AI Disclosure Audit

Audit date: 12 September 2026.

## Current official IOP Publishing policy

Official source: https://publishingsupport.iopscience.iop.org/questions/generative-ai-tools/ (accessed 12 September 2026).

IOP Publishing permits authors to use generative-AI tools to edit or generate text, support literature review, and generate figures from existing data, provided authors critically review the output. Use for any of those activities must be disclosed in the manuscript Acknowledgments. The disclosure should name the model and version and explain how it was used. Authors remain fully responsible for accuracy, integrity, originality, claims, and references; AI tools cannot qualify for authorship. Generative AI may not fabricate or alter original research data or results, and authors may not substitute an AI-generated reference list for author verification.

Coding assistance is not a separately enumerated policy category. Because this project also used generative AI for policy-listed manuscript, literature, and visualization activities, disclosure is mandatory in any event; the coding, debugging, methodology, statistics, and repository assistance is included truthfully in the required description of how the named tools were used.

## Author-confirmed tools and activity inventory

The following inventory was confirmed directly by Sina Qasempour on 12 September 2026.

| Activity | OpenAI Codex — GPT-5.6 Sol | Google Antigravity — 3.8 Flash |
|---|---|---|
| Coding and debugging | Assisted with classical SVM and QSVC workflows, preprocessing, kernel evaluation, corrected nested selection, validation utilities, research scripts, Python debugging, Qiskit/scikit-learn integration, and repository issues | Assisted as a local implementation agent with Python/notebook pipelines, plotting, corrected nested evaluation, validation code, runtime and integration debugging |
| Experiment design and methodology review | Assisted with nested CV, leakage prevention, architecture/$C$ selection, multi-seed evaluation, ablation, sample-size analysis, methodological auditing, preprocessing isolation, statistical framing, kernel interpretation, and limitations | Assisted with baseline/QSVC pipelines, ablation, multi-seed and sample-size workflows, nested tuning, corrected selection, preprocessing isolation, runtime methodology, kernel geometry, limitations, and reproducibility |
| Statistical analysis | Assisted with paired comparisons, exact Wilcoxon tests, Holm adjustment, exploratory bootstrap summaries, metric orientation, implementation review, and interpretation | Assisted with metric aggregation, paired differences, exact Wilcoxon tests, Holm correction, exploratory bootstrap calculations, and table validation |
| Literature and citation support | Assisted with identifying QML, quantum-kernel, SVM, statistics, benchmarking, and biomedical-QML literature and with bibliography, DOI/article, and claim-to-source checks | Assisted with literature-review searches and bibliography preparation, metadata review, DOI/article mismatch detection, and claim-to-citation verification |
| Manuscript writing and editing | Assisted with drafting/restructuring methodology and submission materials and with scientific-language, limitation, abstract, discussion, conclusion, and claim-strength revisions | Assisted with manuscript, literature review, methodology, results, supplementary and submission-document drafting and repeated scientific/editorial revision |
| Visualization | Partly assisted with plotting code, workflow, captions, and provenance review | Assisted with plotting workflows for ablation, sample size, kernel geometry, runtime, F1, ROC-AUC, and captions |
| Repository and documentation | Assisted with organization, validation scripts, methodology/reproducibility documentation, audits, submission preparation, and release planning | Assisted with repository refactoring, configurations, tests, reproducibility scripts, result reports, audits, manuscript packaging, and validation |
| AI-assisted text retained after human revision | Partly | Partly |
| Scientific results supplied as conversational answers | No | No |
| Human review/verification | Yes | Yes |

## Figure classification

All research figures in the submission are category B: conventional programmatic plots generated from stored numerical result artifacts using Python/Matplotlib. AI tools assisted with plotting code, workflow, captions, and review, but no evidence was found that a scientific figure was directly synthesized by a generative image model. `phase12.py` contains the figure-generation and `savefig` calls for the final F1, ROC-AUC, paired-difference, sample-size, ablation, kernel-heatmap, and runtime figures.

## Scientific-result provenance and responsibility

Generative AI assisted with code, methodology, analysis implementation, writing, and review. It did not supply the reported empirical values as free-form answers. The repository's computational pipeline loaded WDBC, generated the predefined splits, fitted fold-local preprocessing, executed the classical models and exact statevector kernels, computed metrics and paired statistics, and persisted the result artifacts. The human author directed the work, reviewed or validated the code, numerical outputs, citations, methodology, claims, and submission files, made the final scientific decisions, and accepts full responsibility.

## Final disclosure text

> Generative-AI tools were used during this work for coding and debugging assistance, methodological and statistical review, literature and citation support, scientific writing and editing, visualization workflows, and repository and documentation tasks. The tools were OpenAI Codex (GPT-5.6 Sol) and Google Antigravity (3.8 Flash). Research figures were generated conventionally with Python/Matplotlib from stored numerical artifacts; AI assistance concerned plotting code, workflow, captions, and review rather than direct image synthesis. Reported numerical results were obtained by executing the repository's reproducible computational workflows and checked against stored result artifacts. The author reviewed the generated code, analyses, citations, and manuscript content, made the final scientific decisions, and takes full responsibility for the work. No AI system is credited with authorship.

## Unresolved items

None. The author-confirmed inventory resolves the previous tool/model/version and activity-scope placeholder.
