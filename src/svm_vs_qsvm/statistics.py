"""Paired split-level statistical testing, Holm adjustments, and bootstrap intervals."""

from typing import List, Optional, Tuple
import numpy as np
import pandas as pd
from scipy.stats import PermutationMethod, wilcoxon

from svm_vs_qsvm.utils import BOOTSTRAP_SEED, N_BOOTSTRAP, SEEDS


def signed_rank_wilcoxon(
    differences: np.ndarray,
) -> Tuple[Optional[float], Optional[float], str, int]:
    """Two-sided Wilcoxon signed-rank test handling exact n=5 resolution."""
    diffs = np.asarray(differences, dtype=float)
    nonzero = diffs[diffs != 0]
    if len(nonzero) < len(diffs):
        return None, np.nan, "untested_zeros", len(diffs)
    if len(nonzero) == 5:
        result = wilcoxon(nonzero, alternative="two-sided", method=PermutationMethod())
        return float(result.statistic), float(result.pvalue), "exact", len(diffs)
    result = wilcoxon(nonzero, alternative="two-sided")
    return float(result.statistic), float(result.pvalue), "scipy_default", len(diffs)


def holm_adjust(p_values: List[float]) -> List[float]:
    """Step-down Holm-Bonferroni correction preserving original input order and NaNs."""
    indexed = [(i, p) for i, p in enumerate(p_values) if p is not None and not np.isnan(p)]
    if not indexed:
        return list(p_values)
    indexed.sort(key=lambda item: item[1])
    m = len(indexed)
    adjusted_pairs: List[Tuple[int, float]] = []
    running_max = 0.0
    for rank, (orig_i, p) in enumerate(indexed):
        adj = min(1.0, (m - rank) * p)
        running_max = max(running_max, adj)
        adjusted_pairs.append((orig_i, running_max))
    out = list(p_values)
    for orig_i, adj_p in adjusted_pairs:
        out[orig_i] = float(adj_p)
    return out


def bootstrap_interval(
    differences: np.ndarray, n: int = N_BOOTSTRAP, seed: int = BOOTSTRAP_SEED, alpha: float = 0.05
) -> Tuple[float, float]:
    """Pointwise percentile bootstrap resamples the observed split differences."""
    diffs = np.asarray(differences, dtype=float)
    rng = np.random.default_rng(seed)
    indices = rng.integers(0, len(diffs), size=(n, len(diffs)))
    means = np.sort(np.mean(diffs[indices], axis=1))
    lower = float(np.percentile(means, 100 * (alpha / 2)))
    upper = float(np.percentile(means, 100 * (1 - alpha / 2)))
    return lower, upper


def pair_results(outer: pd.DataFrame, choices: pd.DataFrame) -> pd.DataFrame:
    """Pair outer-test results for classical comparator vs QSVC aligned strictly by seed."""
    aligned = []
    comparisons = [
        ("Classical PCA2 vs QSVC PCA2", 2, "classical", "quantum"),
        ("Classical PCA4 vs QSVC PCA4", 4, "classical", "quantum"),
        ("QSVC PCA2 vs QSVC PCA4", None, "q2", "q4"),
    ]
    for name, dim, left_kind, right_kind in comparisons:
        for seed in SEEDS:
            if left_kind == "classical":
                left_model = choices[(choices.seed == seed) & (choices.pca_components == dim)].iloc[0].model
                left = outer[(outer.seed == seed) & (outer.model == left_model)].iloc[0]
            elif left_kind == "q2":
                left = outer[(outer.seed == seed) & (outer.kernel == "quantum") & (outer.pca_components == 2)].iloc[0]
            if right_kind == "quantum":
                right = outer[(outer.seed == seed) & (outer.kernel == "quantum") & (outer.pca_components == dim)].iloc[0]
            elif right_kind == "q4":
                right = outer[(outer.seed == seed) & (outer.kernel == "quantum") & (outer.pca_components == 4)].iloc[0]
            for metric in ["f1", "accuracy", "roc_auc"]:
                aligned.append({
                    "comparison": name,
                    "metric": metric,
                    "seed": seed,
                    "left_model": left.model,
                    "right_model": right.model,
                    "left_score": float(left[f"outer_{metric}"]),
                    "right_score": float(right[f"outer_{metric}"]),
                    "difference": float(left[f"outer_{metric}"]) - float(right[f"outer_{metric}"]),
                })
    return pd.DataFrame(aligned)


def compute_paired_effects(pairs: pd.DataFrame) -> pd.DataFrame:
    """Summarize paired differences: mean, median, std, wins, and losses."""
    records = []
    for (name, metric), group in pairs.groupby(["comparison", "metric"], sort=False):
        diffs = group["difference"].values
        wins = int(np.sum(diffs > 0))
        losses = int(np.sum(diffs < 0))
        ties = int(np.sum(diffs == 0))
        records.append({
            "comparison": name,
            "metric": metric,
            "n_splits": len(diffs),
            "mean_paired_difference": float(np.mean(diffs)),
            "median_paired_difference": float(np.median(diffs)),
            "std_paired_difference": float(np.std(diffs, ddof=1)),
            "min_paired_difference": float(np.min(diffs)),
            "max_paired_difference": float(np.max(diffs)),
            "left_wins": wins,
            "right_wins": losses,
            "ties": ties,
        })
    return pd.DataFrame(records)
