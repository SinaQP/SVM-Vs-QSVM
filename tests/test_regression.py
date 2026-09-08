"""Lightweight numerical regression test on outer split seed 42."""

import numpy as np
import pytest

from svm_vs_qsvm.classical import make_classical_model
from svm_vs_qsvm.data import get_outer_split, load_wdbc
from svm_vs_qsvm.kernels import exact_statevector_gram
from svm_vs_qsvm.metrics import score_predictions
from svm_vs_qsvm.preprocessing import fit_preprocessing, transform
from svm_vs_qsvm.quantum import build_qsvc, generate_statevectors


def test_seed42_numerical_reproducibility():
    """Verify refactored pipeline reproduces canonical seed 42 outer-test results."""
    data = load_wdbc()
    x_train_raw, x_test_raw, y_train, y_test, _, _ = get_outer_split(data, seed=42)

    # 1. Classical Linear SVM PCA 2
    x_train_c2, prep_c2 = fit_preprocessing(x_train_raw, dim=2, quantum=False)
    x_test_c2 = transform(x_test_raw, prep_c2)
    # Selected C for seed 42 PCA 2 is 0.1
    lin_model = make_classical_model("linear", c=0.1, seed=42)
    lin_model.fit(x_train_c2, y_train)
    m_lin2 = score_predictions(y_test, lin_model.predict(x_test_c2), lin_model.decision_function(x_test_c2))

    # Canonical values for seed 42 Linear PCA 2 (C=0.1): F1 = 0.930233, Acc = 0.947368
    assert np.isclose(m_lin2["f1"], 0.930233, atol=1e-4)
    assert np.isclose(m_lin2["accuracy"], 0.947368, atol=1e-4)

    # 2. QSVC PCA 2 / 2Q (reps=1, full, C=100.0 selected for seed 42)
    x_train_q2, prep_q2 = fit_preprocessing(x_train_raw, dim=2, quantum=True)
    x_test_q2 = transform(x_test_raw, prep_q2)
    states_train = generate_statevectors(x_train_q2, dim=2, reps=1, entanglement="full")
    states_test = generate_statevectors(x_test_q2, dim=2, reps=1, entanglement="full")
    k_train = exact_statevector_gram(states_train, states_train, training=True)
    k_test = exact_statevector_gram(states_test, states_train, training=False)
    qsvc = build_qsvc(c=100.0, seed=42)
    qsvc.fit(k_train, y_train)
    m_q2 = score_predictions(y_test, qsvc.predict(k_test), qsvc.decision_function(k_test))

    # Canonical values for seed 42 QSVC PCA 2 (C=100.0): F1 = 0.891566, Acc = 0.921053
    assert np.isclose(m_q2["f1"], 0.891566, atol=1e-4)
    assert np.isclose(m_q2["accuracy"], 0.921053, atol=1e-4)

    # Classical strictly outperforms quantum on seed 42
    assert m_lin2["f1"] > m_q2["f1"]
