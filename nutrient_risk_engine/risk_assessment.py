"""
Weather / pest risk assessment — Nutrient & Risk Engine
Module owner: Kranti (4AL25CD400)

Rule-based alerts derived from weather and soil-moisture readings
(no live sensor feed required — works from questionnaire / regional data).
"""

# Simple threshold rules: (condition, alert_name, severity)
FUNGAL_HUMIDITY_THRESHOLD = 80      # %
FUNGAL_TEMP_RANGE = (20, 30)        # deg C, favourable for fungal growth
PEST_DRY_SPELL_DAYS = 10


def assess_risk(humidity_pct, temperature_c, dry_spell_days=0):
    """
    Evaluate weather-driven crop risks and return alerts as
    (risk_name, severity) tuples.
    """
    alerts = []

    if (humidity_pct >= FUNGAL_HUMIDITY_THRESHOLD and
            FUNGAL_TEMP_RANGE[0] <= temperature_c <= FUNGAL_TEMP_RANGE[1]):
        alerts.append(("fungal_disease_risk", "high"))
    elif humidity_pct >= FUNGAL_HUMIDITY_THRESHOLD - 15:
        alerts.append(("fungal_disease_risk", "moderate"))

    if dry_spell_days >= PEST_DRY_SPELL_DAYS:
        alerts.append(("pest_infestation_risk", "moderate"))

    return {"alerts": alerts}