"""
Nutrient & Risk Engine package — Smart Agriculture Decision Advisor
Module owner: Kranti (4AL25CD400)

Exposes the main functions so they can be imported directly from the
package, e.g.:

    from nutrient_risk_engine import recommend_fertilizer, assess_risk, evaluate_model
"""

from .fertilizer import recommend_fertilizer
from .risk_assessment import assess_risk
from .matrics_evaluation import evaluate_model

__all__ = ["recommend_fertilizer", "assess_risk", "evaluate_model"]