"""Classical SVM vs Quantum SVM for Breast Cancer Classification.

A reproducible research benchmark comparing classical Support Vector Machines
(Linear, RBF) against Quantum Support Vector Classifiers (QSVC) with
parameterized ZZ feature maps on the Wisconsin Diagnostic Breast Cancer dataset.
"""

__version__ = "1.0.0"

from svm_vs_qsvm.classical import (
    candidates,
    choose_classical_comparator,
    make_classical_model,
    select_candidate,
    summarize_candidates,
)
from svm_vs_qsvm.data import (
    generate_nested_stratified_subsets,
    get_inner_folds,
    get_outer_split,
    load_wdbc,
    split_indices,
)
from svm_vs_qsvm.kernels import (
    compute_centered_kernel_alignment,
    compute_frobenius_alignment,
    compute_kernel_diagnostics,
    compute_offdiag_statistics,
    compute_rbf_gram,
    exact_statevector_gram,
)
from svm_vs_qsvm.metrics import (
    compute_classification_metrics,
    score_predictions,
)
from svm_vs_qsvm.preprocessing import (
    fit_preprocessing,
    transform,
)
from svm_vs_qsvm.quantum import (
    build_qsvc,
    create_zz_feature_map,
    generate_statevectors,
)
from svm_vs_qsvm.statistics import (
    bootstrap_interval,
    compute_paired_effects,
    holm_adjust,
    pair_results,
    signed_rank_wilcoxon,
)
from svm_vs_qsvm.utils import (
    DEFAULT_C_VALUES,
    DEFAULT_GAMMA_VALUES,
    DEFAULT_SEEDS,
    load_config,
    model_name,
)

__all__ = [
    "__version__",
    "load_wdbc",
    "split_indices",
    "get_outer_split",
    "get_inner_folds",
    "generate_nested_stratified_subsets",
    "fit_preprocessing",
    "transform",
    "candidates",
    "make_classical_model",
    "select_candidate",
    "summarize_candidates",
    "choose_classical_comparator",
    "create_zz_feature_map",
    "generate_statevectors",
    "build_qsvc",
    "exact_statevector_gram",
    "compute_rbf_gram",
    "compute_kernel_diagnostics",
    "compute_offdiag_statistics",
    "compute_centered_kernel_alignment",
    "compute_frobenius_alignment",
    "score_predictions",
    "compute_classification_metrics",
    "signed_rank_wilcoxon",
    "holm_adjust",
    "bootstrap_interval",
    "pair_results",
    "compute_paired_effects",
    "load_config",
    "model_name",
    "DEFAULT_SEEDS",
    "DEFAULT_C_VALUES",
    "DEFAULT_GAMMA_VALUES",
]
