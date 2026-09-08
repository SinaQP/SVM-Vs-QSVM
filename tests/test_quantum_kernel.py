"""Tests for quantum Gram matrix properties, spectral diagnostics, and CKA."""

import numpy as np
import pytest

from svm_vs_qsvm.kernels import (
    compute_centered_kernel_alignment,
    compute_frobenius_alignment,
    compute_kernel_diagnostics,
    compute_offdiag_statistics,
    exact_statevector_gram,
)
from svm_vs_qsvm.quantum import generate_statevectors


def test_exact_statevector_gram_mathematical_properties():
    """Verify symmetry, unit diagonal, positive semi-definiteness, and bounds."""
    # Synthetic 2D inputs in [0, pi]
    x_sample = np.array([
        [0.2, 0.5],
        [1.1, 2.3],
        [2.8, 0.9],
        [0.4, 1.7],
    ])
    states = generate_statevectors(x_sample, dim=2, reps=1, entanglement="full")
    gram = exact_statevector_gram(states, states, training=True)

    # 1. Symmetry
    np.testing.assert_allclose(gram, gram.T, atol=1e-12)

    # 2. Unit diagonal
    np.testing.assert_allclose(np.diag(gram), 1.0, atol=1e-12)

    # 3. Finite bounds in [0, 1]
    assert np.isfinite(gram).all()
    assert gram.min() >= -1e-10
    assert gram.max() <= 1.0 + 1e-10

    # 4. Positive semi-definiteness (eigenvalues >= -1e-10)
    eigvals = np.linalg.eigvalsh(gram)
    assert eigvals.min() >= -1e-10


def test_diagnostics_and_offdiag_statistics():
    """Verify kernel spectral diagnostics and off-diagonal dispersion calculations."""
    K = np.array([
        [1.0, 0.4, 0.2],
        [0.4, 1.0, 0.5],
        [0.2, 0.5, 1.0],
    ])
    diag = compute_kernel_diagnostics(K)
    assert diag["effective_rank"] > 1.0
    assert diag["kernel_condition_number"] > 0.0
    assert diag["kernel_minimum_eigenvalue"] >= 0.0

    offdiag = compute_offdiag_statistics(K)
    assert pytest.approx(offdiag["offdiag_mean"]) == (0.4 + 0.2 + 0.5) / 3
    assert offdiag["offdiag_min"] == 0.2
    assert offdiag["offdiag_max"] == 0.5


def test_centered_kernel_alignment_properties():
    """Verify CKA is 1 for identical matrices and non-negative."""
    K_id = np.eye(6)
    assert pytest.approx(compute_centered_kernel_alignment(K_id, K_id)) == 1.0
    assert pytest.approx(compute_frobenius_alignment(K_id, K_id)) == 1.0
