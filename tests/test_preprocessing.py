"""Tests for preprocessing isolation, leakage protection, and scaling behavior."""

import numpy as np
import pytest
from sklearn.datasets import load_breast_cancer

from svm_vs_qsvm.data import get_outer_split, split_indices
from svm_vs_qsvm.preprocessing import fit_preprocessing, transform


def test_preprocessing_fit_isolation():
    """Verify that fit_preprocessing fits strictly on training data."""
    data = load_breast_cancer()
    train_idx, test_idx = split_indices(data.target, seed=42)
    x_train_raw = data.data[train_idx]
    x_test_raw = data.data[test_idx]

    train_transformed, fitted = fit_preprocessing(x_train_raw, dim=4, quantum=True)
    scaler, pca, q_scaler = fitted

    # StandardScaler mean should exactly equal training sample mean
    np.testing.assert_allclose(scaler.mean_, x_train_raw.mean(axis=0))
    # Number of samples seen must equal training samples only
    assert scaler.n_samples_seen_ == len(train_idx)
    assert pca.n_samples_ == len(train_idx)
    assert q_scaler.n_samples_seen_ == len(train_idx)

    # State before transform
    mean_before = scaler.mean_.copy()
    pca_comp_before = pca.components_.copy()
    q_min_before = q_scaler.data_min_.copy()

    # Transform test set (even with extreme values) must not modify internal fitted state
    test_transformed = transform(x_test_raw * 1000.0, fitted)
    np.testing.assert_array_equal(scaler.mean_, mean_before)
    np.testing.assert_array_equal(pca.components_, pca_comp_before)
    np.testing.assert_array_equal(q_scaler.data_min_, q_min_before)


def test_quantum_minmax_scaler_bounds():
    """Verify quantum features are bounded in [0, pi]."""
    data = load_breast_cancer()
    x_train, x_test, _, _, _, _ = get_outer_split(data, seed=42)
    train_transformed, fitted = fit_preprocessing(x_train, dim=2, quantum=True)
    test_transformed = transform(x_test, fitted)

    assert train_transformed.shape == (len(x_train), 2)
    assert test_transformed.shape == (len(x_test), 2)

    assert np.all(train_transformed >= 0.0)
    assert np.all(train_transformed <= np.pi + 1e-12)
    assert np.all(test_transformed >= 0.0)
    assert np.all(test_transformed <= np.pi + 1e-12)
