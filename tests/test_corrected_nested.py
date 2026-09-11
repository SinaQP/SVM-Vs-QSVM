"""Leakage-regression tests for corrected joint QSVC selection."""

from dataclasses import replace
import inspect

import numpy as np
import pandas as pd
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import StratifiedKFold

import corrected_nested as c
from svm_vs_qsvm.data import split_indices


def _tiny_fake_kernel(monkeypatch):
    monkeypatch.setattr(
        c, "generate_statevectors",
        lambda x, dim, reps, entanglement: np.asarray(x, dtype=float),
    )
    monkeypatch.setattr(
        c, "exact_statevector_gram",
        lambda left, right, training=False: left @ right.T,
    )


def test_selection_api_cannot_accept_outer_test_data_or_labels():
    parameters = set(inspect.signature(c.inner_search_qsvc).parameters)
    assert parameters == {"x_outer_train", "y_outer_train", "seed", "dim"}
    assert "y_outer_test" not in parameters and "x_outer_test" not in parameters


def test_two_qubit_grid_is_nonredundant_and_tie_break_is_deterministic():
    assert c.architecture_grid(2) == [(1, "linear"), (2, "linear"), (3, "linear")]
    summary = pd.DataFrame([
        {"inner_cv_f1_mean": 0.9, "reps": 2, "entanglement": "linear", "C": 0.01},
        {"inner_cv_f1_mean": 0.9 + 5e-13, "reps": 1, "entanglement": "full", "C": 0.01},
        {"inner_cv_f1_mean": 0.9, "reps": 1, "entanglement": "linear", "C": 10.0},
        {"inner_cv_f1_mean": 0.9, "reps": 1, "entanglement": "linear", "C": 0.1},
    ])
    chosen = c.select_candidate(summary)
    assert (chosen["reps"], chosen["entanglement"], chosen["C"]) == (1, "linear", 0.1)


def test_every_inner_fold_refits_preprocessing_only_on_inner_train(monkeypatch):
    data = load_breast_cancer()
    train_idx, _ = split_indices(data.target, 42)
    x, y = data.data[train_idx], data.target[train_idx]
    folds = list(StratifiedKFold(5, shuffle=True, random_state=42).split(x, y))
    calls = []
    original = c.fit_preprocessing

    def observed(values, dim, quantum):
        expected_fit, _ = folds[len(calls)]
        np.testing.assert_array_equal(values, x[expected_fit])
        transformed, fitted = original(values, dim, quantum)
        assert fitted[0].n_samples_seen_ == len(expected_fit)
        assert fitted[1].n_samples_ == len(expected_fit)
        assert fitted[2].n_samples_seen_ == len(expected_fit)
        calls.append(fitted)
        return transformed, fitted

    monkeypatch.setattr(c, "fit_preprocessing", observed)
    _tiny_fake_kernel(monkeypatch)
    raw, _ = c.inner_search_qsvc(x, y, 42, 2)
    assert len(calls) == 5
    assert len({id(item[0]) for item in calls}) == 5
    assert len(raw) == 75
    assert raw.groupby("kernel_cache_id").C.nunique().eq(5).all()


def test_masking_or_changing_outer_test_labels_cannot_change_selection(monkeypatch):
    data = load_breast_cancer()
    train_idx, test_idx = split_indices(data.target, 42)
    _tiny_fake_kernel(monkeypatch)
    _, first = c.inner_search_qsvc(data.data[train_idx], data.target[train_idx], 42, 2)
    altered = data.target.copy()
    altered[test_idx] = 1 - altered[test_idx]
    _, second = c.inner_search_qsvc(data.data[train_idx], altered[train_idx], 42, 2)
    assert first == second


def test_outer_evaluation_requires_frozen_selection():
    selection = c.FrozenSelection(42, 2, 2, 1, "linear", 1.0, 0.8, 0.01, 5)
    assert selection.selection_status == "FROZEN_BEFORE_OUTER_EVALUATION"
    invalid = replace(selection, selection_status="NOT_FROZEN")
    try:
        c.evaluate_outer_once(
            np.zeros((4, 3)), np.array([0, 0, 1, 1]),
            np.zeros((2, 3)), np.array([0, 1]), np.array([4, 5]), invalid,
        )
    except ValueError as error:
        assert "not frozen" in str(error)
    else:
        raise AssertionError("Outer evaluation accepted a non-frozen selection")


def test_run_all_freezes_all_selections_before_first_outer_call(monkeypatch, tmp_path):
    selections = tuple(
        c.FrozenSelection(seed, dim, dim, 1, "linear", 1.0, 0.8, 0.01, 5)
        for seed in c.SEEDS for dim in c.DIMS
    )
    raw = pd.DataFrame({"placeholder": [1]})
    splits = [
        {"seed": seed, "outer_train_ids": list(range(455)), "outer_test_ids": list(range(455, 569))}
        for seed in c.SEEDS
    ]
    events = []

    def fake_select_all(data):
        events.append("all_selections_complete")
        return raw, selections, splits

    def fake_evaluate(*args):
        checkpoint = tmp_path / "qsvc_selected_configurations.csv"
        assert checkpoint.exists()
        assert events[0] == "all_selections_complete"
        events.append("outer_evaluation")
        raise RuntimeError("stop after proving call order")

    monkeypatch.setattr(c, "select_all", fake_select_all)
    monkeypatch.setattr(c, "evaluate_outer_once", fake_evaluate)
    try:
        c.run_all(tmp_path)
    except RuntimeError as error:
        assert "call order" in str(error)
    assert events[:2] == ["all_selections_complete", "outer_evaluation"]

