"""
Smart Agriculture Decision Advisor — Nutrient & Risk Engine demo
Module owner: Kranti (4AL25CD400)

Run with:
    python main.py
"""

from nutrient_risk_engine import recommend_fertilizer, assess_risk, evaluate_model


def build_sample_predictions():
    """
    Build a fixed set of true/predicted risk labels whose confusion matrix
    matches the module's held-out test run:

        [[68, 1, 0],
         [ 1, 11, 1],
         [ 4, 1, 13]]

    Row = true label (low, medium, high), column = predicted label.
    """
    counts = {
        "low":    {"low": 68, "medium": 1, "high": 0},
        "medium": {"low": 1,  "medium": 11, "high": 1},
        "high":   {"low": 4,  "medium": 1,  "high": 13},
    }

    y_true, y_pred = [], []
    for true_label, predictions in counts.items():
        for pred_label, n in predictions.items():
            y_true.extend([true_label] * n)
            y_pred.extend([pred_label] * n)

    return y_true, y_pred


def main():
    # --- Fertilizer recommendation -------------------------------------
    # Sample N/P/K deficit (kg/ha) from a questionnaire-based soil reading
    fert = recommend_fertilizer(
        n_deficit_kg_ha=62.39,
        p_deficit_kg_ha=45.0,
        k_deficit_kg_ha=10.0,
        source="questionnaire",
    )
    print(f"Fertilizer recommendation: {fert}")

    # --- Risk assessment -------------------------------------------------
    risk = assess_risk(humidity_pct=85, temperature_c=26)
    print(f"Risk alerts: {risk}")

    # --- Model performance -------------------------------------------------
    y_true, y_pred = build_sample_predictions()
    metrics = evaluate_model(y_true, y_pred)

    print("\nModel performance:")
    print(f"  Accuracy:           {metrics['accuracy']:.3f}")
    print(f"  Precision (macro):  {metrics['precision_macro']:.3f}")
    print(f"  Recall (macro):     {metrics['recall_macro']:.3f}")
    print(f"  F1 (macro):         {metrics['f1_macro']:.3f}")
    print(f"  Confusion matrix:   {metrics['confusion_matrix']}")
    print()
    print(metrics["report"])


if __name__ == "__main__":
    main()