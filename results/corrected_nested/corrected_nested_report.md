# Corrected fully nested QSVC results

## Outcome

The corrected selection procedure chose the historical effective architecture and the same `C` for every outer split. For 2Q, `linear` is only a nonredundant spelling change: it is algebraically identical to `full` because there is one qubit pair. Consequently, corrected and historical outer metrics are equal within the prespecified `1e-12` numerical tolerance.

| Representation | Accuracy mean | F1 mean | ROC-AUC mean | Historical F1 mean | Corrected - historical F1 |
| --- | ---: | ---: | ---: | ---: | ---: |
| PCA2/2Q | 0.907018 | 0.867760 | 0.964352 | 0.867760 | +0.000000 |
| PCA4/4Q | 0.905263 | 0.872060 | 0.958135 | 0.872060 | +0.000000 |

## Explicit audit questions

1. **Did the previous architecture selection make QSVC performance look better?** Not in the measured corrected comparison: the corrected inner procedure independently selected the same effective configurations and produced zero F1 change.
2. **If yes, by how much?** Not applicable; measured mean delta F1 is 0.000000 for both representations.
3. **Did it make QSVC performance look worse?** No measured change was observed.
4. **Did the primary scientific conclusion change?** No. The nested classical comparator retained higher F1 on every one of the five aligned splits for both representations.
5. **Does corrected QSVC ever outperform the nested classical comparator?** No: 0/5 splits for 2Q and 0/5 for 4Q.
6. **How often are repetitions selected?** reps=1: 10/10; reps=2: 0/10; reps=3: 0/10.
7. **For 4Q, how often is each topology selected?** linear: 0/5; full: 5/5.
8. **How stable are selected C values?** 4Q selected C=1 on 5/5 splits. 2Q varied: C=1 on 1/5, C=10 on 2/5, and C=100 on 2/5.

## Classical gaps and paired inference

- PCA2: classical-minus-QSVC mean F1 gap was +0.066169 historically and +0.066169 after correction. Exact Wilcoxon W=0.0, raw p=0.0625, Holm p=0.1875; exploratory split-level percentile interval [0.038832, 0.097665].
- PCA4: classical-minus-QSVC mean F1 gap was +0.077191 historically and +0.077191 after correction. Exact Wilcoxon W=0.0, raw p=0.0625, Holm p=0.1875; exploratory split-level percentile interval [0.044480, 0.109223].

## Interpretation limits

The absence of a measured score change does not retrospectively validate the historical procedure. That procedure still had outer-test reuse for architecture selection and could have produced selection-induced optimism. The corrected procedure removes that direct algorithmic path.

The corrected nested analysis removes direct test-set involvement in architecture and hyperparameter selection, but remains a post hoc reanalysis of a dataset and partition set previously examined during exploratory development. With n=5 overlapping splits, the Wilcoxon tests and bootstrap intervals are exploratory; a nonsignificant test is not evidence of equivalence.
