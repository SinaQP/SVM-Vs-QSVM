"""Kernel evaluation, diagnostics, alignment, and CKA metrics."""

from typing import Any, Dict
import numpy as np
from sklearn.metrics.pairwise import rbf_kernel


def exact_statevector_gram(
    states_left: np.ndarray, states_train: np.ndarray, training: bool = False
) -> np.ndarray:
    """Compute exact quantum fidelity Gram matrix via inner products.
    
    K_{i,j} = |<psi(x_i) | psi(x_j)>|^2
    """
    matrix = np.abs(states_left @ states_train.conj().T) ** 2
    if training:
        np.fill_diagonal(matrix, 1.0)
    assert np.isfinite(matrix).all(), "Gram matrix contains non-finite values."
    assert matrix.min() >= -1e-10 and matrix.max() <= 1 + 1e-10, "Gram values outside [0, 1]."
    return matrix


def compute_rbf_gram(x_left: np.ndarray, x_train: np.ndarray, gamma: Any) -> np.ndarray:
    """Compute classical RBF kernel Gram matrix."""
    return rbf_kernel(x_left, x_train, gamma=gamma)


def compute_kernel_diagnostics(matrix: np.ndarray) -> Dict[str, float]:
    """Compute spectral diagnostics on square symmetric Gram matrix."""
    assert np.allclose(matrix, matrix.T, atol=1e-10, rtol=0), "Gram matrix is not symmetric."
    eigenvalues = np.linalg.eigvalsh((matrix + matrix.T) / 2)
    assert eigenvalues.min() >= -1e-10, f"Negative eigenvalue detected: {eigenvalues.min()}"
    positive = np.clip(eigenvalues, 0, None)
    probabilities = positive[positive > 0] / positive.sum()
    return {
        "kernel_condition_number": float(np.linalg.cond(matrix)),
        "effective_rank": float(np.exp(-np.sum(probabilities * np.log(probabilities)))),
        "kernel_minimum_eigenvalue": float(eigenvalues.min()),
    }


def compute_offdiag_statistics(matrix: np.ndarray) -> Dict[str, float]:
    """Compute dispersion statistics over all off-diagonal entries of Gram matrix."""
    n = matrix.shape[0]
    off_diag = matrix[~np.eye(n, dtype=bool)]
    return {
        "offdiag_mean": float(np.mean(off_diag)),
        "offdiag_std": float(np.std(off_diag)),
        "offdiag_min": float(np.min(off_diag)),
        "offdiag_max": float(np.max(off_diag)),
        "offdiag_median": float(np.median(off_diag)),
        "offdiag_q25": float(np.percentile(off_diag, 25)),
        "offdiag_q75": float(np.percentile(off_diag, 75)),
    }


def center_kernel(K: np.ndarray) -> np.ndarray:
    """Center Gram matrix K in feature space: K_c = H K H."""
    n = K.shape[0]
    H = np.eye(n) - np.ones((n, n)) / n
    return H @ K @ H


def compute_centered_kernel_alignment(K1: np.ndarray, K2: np.ndarray) -> float:
    """Compute Centered Kernel Alignment (CKA) between two Gram matrices."""
    K1_c = center_kernel(K1)
    K2_c = center_kernel(K2)
    hsic_12 = np.sum(K1_c * K2_c)
    hsic_11 = np.sum(K1_c * K1_c)
    hsic_22 = np.sum(K2_c * K2_c)
    denom = np.sqrt(hsic_11 * hsic_22)
    if denom == 0.0:
        return 0.0
    return float(np.clip(hsic_12 / denom, 0.0, 1.0))


def compute_frobenius_alignment(K1: np.ndarray, K2: np.ndarray) -> float:
    """Compute normalized Frobenius inner product alignment between two Gram matrices."""
    frob_12 = np.sum(K1 * K2)
    frob_11 = np.sum(K1 * K1)
    frob_22 = np.sum(K2 * K2)
    denom = np.sqrt(frob_11 * frob_22)
    if denom == 0.0:
        return 0.0
    return float(np.clip(frob_12 / denom, 0.0, 1.0))
