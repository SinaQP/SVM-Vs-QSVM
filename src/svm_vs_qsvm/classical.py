"""Classical SVM models, candidate generation, and selection logic."""

from itertools import product
from typing import Any, Dict, List, Union
import numpy as np
import pandas as pd
from sklearn.svm import SVC

from svm_vs_qsvm.utils import DEFAULT_C_VALUES, DEFAULT_GAMMA_VALUES, TIE_ATOL


def candidates(kernel: str) -> List[Dict[str, Any]]:
    """Return predefined candidate grid for specified kernel."""
    gammas = DEFAULT_GAMMA_VALUES if kernel == "rbf" else ["none"]
    return [{"C": c, "gamma": str(g)} for c, g in product(DEFAULT_C_VALUES, gammas)]


def make_classical_model(
    kernel: str, c: float, gamma: Union[str, float] = "scale", seed: int = 42
) -> SVC:
    """Instantiate SVC model with explicit seed and parameter handling."""
    gamma_val = (
        gamma
        if gamma in ("scale", "auto")
        else (float(gamma) if gamma != "none" else "scale")
    )
    return SVC(kernel=kernel, C=c, gamma=gamma_val, random_state=seed)


def select_candidate(candidate_summary: pd.DataFrame) -> Dict[str, Any]:
    """Select best candidate by inner-CV F1 score with predefined tie-breaking rules.
    
    Tie-breaking rule:
    1. Highest inner-CV mean F1 (within 1e-12 tolerance)
    2. Smaller regularization parameter C
    3. Parameter gamma order: none, scale, auto, 0.01, 0.1, 1.0
    """
    best = candidate_summary["inner_cv_f1_mean"].max()
    tied = candidate_summary.loc[
        np.isclose(candidate_summary.inner_cv_f1_mean, best, atol=TIE_ATOL, rtol=0)
    ].copy()
    gamma_order = {str(g): i for i, g in enumerate(["none"] + DEFAULT_GAMMA_VALUES)}
    tied["gamma_order"] = tied.gamma.map(gamma_order)
    return tied.sort_values(["C", "gamma_order"], kind="stable").iloc[0].drop("gamma_order").to_dict()


def summarize_candidates(raw: pd.DataFrame) -> pd.DataFrame:
    """Aggregate raw inner cross-validation fold scores across seeds and models."""
    return raw.groupby(
        ["seed", "model", "kernel", "pca_components", "C", "gamma"], sort=False
    ).agg(
        inner_cv_f1_mean=("inner_f1", "mean"),
        inner_cv_f1_std=("inner_f1", "std"),
        inner_cv_accuracy_mean=("inner_accuracy", "mean"),
        inner_cv_accuracy_std=("inner_accuracy", "std"),
        inner_cv_roc_auc_mean=("inner_roc_auc", "mean"),
        inner_cv_roc_auc_std=("inner_roc_auc", "std"),
        n_folds=("inner_fold", "nunique"),
    ).reset_index()


def choose_classical_comparator(selected: pd.DataFrame) -> pd.DataFrame:
    """Predefined classical comparator selection rule per seed and dimension.
    
    Selects Linear vs RBF based strictly on inner-CV F1 score.
    Ties broken by smaller C, then Linear over RBF.
    """
    chosen = []
    for (seed, dim), group in selected[selected.kernel != "quantum"].groupby(
        ["seed", "pca_components"]
    ):
        maximum = group.inner_cv_f1_mean.max()
        tied = group[
            np.isclose(group.inner_cv_f1_mean, maximum, atol=TIE_ATOL, rtol=0)
        ].copy()
        tied["family_order"] = (tied.kernel != "linear").astype(int)
        row = tied.sort_values(["selected_C", "family_order"], kind="stable").iloc[0]
        chosen.append({
            "seed": seed,
            "pca_components": dim,
            "model": row.model,
            "selected_C": row.selected_C,
            "selected_gamma": row.selected_gamma,
            "inner_cv_f1_mean": row.inner_cv_f1_mean,
        })
    return pd.DataFrame(chosen)
