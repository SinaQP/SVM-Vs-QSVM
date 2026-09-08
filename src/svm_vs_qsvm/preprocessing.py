"""Leakage-safe preprocessing and dimensionality reduction."""

from typing import Optional, Tuple
import numpy as np
from sklearn.decomposition import PCA
from sklearn.preprocessing import MinMaxScaler, StandardScaler


def fit_preprocessing(
    x_train: np.ndarray, dim: int, quantum: bool = False
) -> Tuple[np.ndarray, Tuple[StandardScaler, PCA, Optional[MinMaxScaler]]]:
    """Fit scaler, PCA, and quantum scaler strictly on training observations only.
    
    Args:
        x_train: Training feature matrix.
        dim: Number of principal components.
        quantum: If True, fits MinMaxScaler(feature_range=(0, pi), clip=True).
        
    Returns:
        Tuple of (transformed training features, fitted transformers tuple).
    """
    scaler = StandardScaler()
    train_std = scaler.fit_transform(x_train)
    pca = PCA(n_components=dim)
    train_pca = pca.fit_transform(train_std)
    q_scaler = MinMaxScaler(feature_range=(0, np.pi), clip=True) if quantum else None
    train = q_scaler.fit_transform(train_pca) if quantum else train_pca
    assert int(scaler.n_samples_seen_) == pca.n_samples_ == len(x_train)
    if quantum:
        assert q_scaler.n_samples_seen_ == len(x_train)
    return train, (scaler, pca, q_scaler)


def transform(
    x: np.ndarray,
    preprocessing: Tuple[StandardScaler, PCA, Optional[MinMaxScaler]],
) -> np.ndarray:
    """Transform out-of-sample data using pre-fitted transformers without re-fitting."""
    scaler, pca, q_scaler = preprocessing
    values = pca.transform(scaler.transform(x))
    return q_scaler.transform(values) if q_scaler is not None else values
