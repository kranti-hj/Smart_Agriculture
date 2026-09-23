"""
Model performance evaluation — Nutrient & Risk Engine
Module owner: Kranti (4AL25CD400)

Wraps sklearn.metrics to report accuracy, macro precision/recall/F1,
the confusion matrix, and a full per-class classification report for the
risk-level classifier (low / medium / high).
"""

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    classification_report,
)

LABELS = ["low", "medium", "high"]


def evaluate_model(y_true, y_pred, labels=LABELS):
    """
    Compute standard classification metrics for the given true/predicted
    risk-level labels.
    """
    accuracy = accuracy_score(y_true, y_pred)
    precision_macro = precision_score(y_true, y_pred, labels=labels,
                                       average="macro", zero_division=0)
    recall_macro = recall_score(y_true, y_pred, labels=labels,
                                 average="macro", zero_division=0)
    f1_macro = f1_score(y_true, y_pred, labels=labels,
                         average="macro", zero_division=0)
    cm = confusion_matrix(y_true, y_pred, labels=labels)
    report = classification_report(y_true, y_pred, labels=labels,
                                    target_names=labels, zero_division=0)

    return {
        "accuracy": accuracy,
        "precision_macro": precision_macro,
        "recall_macro": recall_macro,
        "f1_macro": f1_macro,
        "confusion_matrix": cm.tolist(),
        "report": report,
    }