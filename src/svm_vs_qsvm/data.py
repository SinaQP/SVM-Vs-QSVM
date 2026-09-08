"""Data loading, partitioning, and subsetting utilities."""

from typing import Dict, List, Tuple
import numpy as np
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import StratifiedKFold, train_test_split


def load_wdbc():
    """Load the Wisconsin Diagnostic Breast Cancer (WDBC) dataset.
    
    Returns:
        sklearn.utils.Bunch: Dataset containing data (569, 30), target (569,),
        feature_names, and target_names (['malignant', 'benign']).
        Label 0 corresponds to malignant, Label 1 to benign.
    """
    return load_breast_cancer()


def split_indices(y: np.ndarray, seed: int, test_size: float = 0.20) -> Tuple[np.ndarray, np.ndarray]:
    """Generate reproducible stratified outer train/test partition indices."""
    return train_test_split(
        np.arange(len(y)),
        test_size=test_size,
        random_state=seed,
        stratify=y,
    )


def get_outer_split(
    data=None, seed: int = 42, test_size: float = 0.20
) -> Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    """Return train/test data arrays and partition indices for an outer seed."""
    if data is None:
        data = load_wdbc()
    train_idx, test_idx = split_indices(data.target, seed, test_size=test_size)
    x_train, x_test = data.data[train_idx], data.data[test_idx]
    y_train, y_test = data.target[train_idx], data.target[test_idx]
    return x_train, x_test, y_train, y_test, train_idx, test_idx


def get_inner_folds(
    x_train: np.ndarray, y_train: np.ndarray, seed: int, n_splits: int = 5
) -> List[Tuple[np.ndarray, np.ndarray]]:
    """Return inner stratified K-fold train/validation indices."""
    folds = StratifiedKFold(n_splits=n_splits, shuffle=True, random_state=seed)
    return list(folds.split(x_train, y_train))


def generate_nested_stratified_subsets(
    y_train: np.ndarray, train_sizes: List[int], seed: int
) -> Dict[int, np.ndarray]:
    """Generate strictly nested stratified training subset index arrays.
    
    Ensures smaller sample sizes are strict subsets of larger sizes while
    preserving the empirical training class ratio.
    """
    idx0 = np.where(y_train == 0)[0]
    idx1 = np.where(y_train == 1)[0]
    rng0 = np.random.RandomState(seed)
    rng1 = np.random.RandomState(seed)
    shuffled_idx0 = rng0.permutation(idx0)
    shuffled_idx1 = rng1.permutation(idx1)

    p0 = len(idx0) / len(y_train)
    subsets: Dict[int, np.ndarray] = {}

    for N in train_sizes:
        if N == len(y_train):
            sub_idx = np.arange(len(y_train))
        else:
            n0 = int(round(N * p0))
            n1 = N - n0
            sub_idx = np.concatenate([shuffled_idx0[:n0], shuffled_idx1[:n1]])
        subsets[N] = sub_idx

    return subsets
