"""Quantum feature map, statevector generation, and QSVC construction."""

import numpy as np
from qiskit.circuit.library import zz_feature_map
from qiskit.quantum_info import Statevector
from qiskit_machine_learning.algorithms import QSVC


def create_zz_feature_map(dim: int, reps: int = 1, entanglement: str = "full"):
    """Create parameterized Qiskit ZZFeatureMap circuit."""
    return zz_feature_map(
        feature_dimension=dim, reps=reps, entanglement=entanglement
    )


def generate_statevectors(
    x: np.ndarray, dim: int, reps: int = 1, entanglement: str = "full"
) -> np.ndarray:
    """Generate exact statevector complex amplitudes for a dataset."""
    feature_map = create_zz_feature_map(dim, reps=reps, entanglement=entanglement)
    return np.asarray([Statevector(feature_map.assign_parameters(row)).data for row in x])


def build_qsvc(c: float = 1.0, seed: int = 42) -> QSVC:
    """Construct QSVC classifier expecting precomputed Gram matrix."""
    return QSVC(quantum_kernel="precomputed", C=c, random_state=seed)
