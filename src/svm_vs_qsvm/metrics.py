"""Diagnostic classification metrics with malignant class (0) as positive."""

from typing import Dict, Union
import numpy as np
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score, roc_auc_score


def score_predictions(
    y_true: Union[np.ndarray, list],
    predictions: Union[np.ndarray, list],
    decision_scores: Union[np.ndarray, list],
) -> Dict[str, float]:
    """Compute standard classification metrics oriented to malignant class 0.
    
    All models operate on binary classes [0, 1]. In scikit-learn SVC, higher decision
    values indicate class 1 (benign); therefore decision_scores are negated to ensure
    higher scores indicate class 0 (malignant) for proper ROC-AUC calculation.
    """
    y_arr = np.asarray(y_true)
    pred_arr = np.asarray(predictions)
    score_arr = np.asarray(decision_scores)
    return {
        "accuracy": float(accuracy_score(y_arr, pred_arr)),
        "precision": float(precision_score(y_arr, pred_arr, pos_label=0, zero_division=0)),
        "recall": float(recall_score(y_arr, pred_arr, pos_label=0, zero_division=0)),
        "f1": float(f1_score(y_arr, pred_arr, pos_label=0, zero_division=0)),
        "roc_auc": float(roc_auc_score(y_arr == 0, -score_arr)),
    }


def compute_classification_metrics(
    y_true: Union[np.ndarray, list],
    predictions: Union[np.ndarray, list],
    decision_scores: Union[np.ndarray, list],
) -> Dict[str, float]:
    """Alias for score_predictions."""
    return score_predictions(y_true, predictions, decision_scores)
