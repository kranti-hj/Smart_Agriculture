"""
Fertilizer recommendation logic — Nutrient & Risk Engine
Module owner: Kranti (4AL25CD400)

Computes Urea / DAP / MOP dosage (kg/ha) from a soil-nutrient reading using
simple deficit-based rules, and attaches a confidence score based on how
the reading was obtained (SHC report, regional default, or questionnaire —
no live sensor is used).
"""

# Approximate nutrient content fractions used to convert an N/P/K deficit
# (kg/ha) into a fertilizer dosage (kg/ha).
UREA_N_FRACTION = 0.46
DAP_P_FRACTION = 0.46
MOP_K_FRACTION = 0.60

# Confidence assigned per input source (tiered input system).
SOURCE_CONFIDENCE = {
    "shc_upload": 0.95,
    "questionnaire": 0.85,
    "regional_default": 0.65,
}


def recommend_fertilizer(n_deficit_kg_ha, p_deficit_kg_ha, k_deficit_kg_ha,
                          source="questionnaire"):
    """
    Convert N/P/K deficits (kg/ha) into fertilizer dosages (kg/ha).

    n_deficit_kg_ha, p_deficit_kg_ha, k_deficit_kg_ha : float
        Shortfall of each nutrient versus the crop's target requirement.
    source : str
        Where the underlying soil reading came from — one of
        "shc_upload", "questionnaire", "regional_default".
    """
    urea_kg_per_ha = round(n_deficit_kg_ha / UREA_N_FRACTION, 2)
    dap_kg_per_ha = round(p_deficit_kg_ha / DAP_P_FRACTION, 2)
    mop_kg_per_ha = round(k_deficit_kg_ha / MOP_K_FRACTION, 2)

    confidence = SOURCE_CONFIDENCE.get(source, 0.5)

    return {
        "urea_kg_per_ha": urea_kg_per_ha,
        "dap_kg_per_ha": dap_kg_per_ha,
        "mop_kg_per_ha": mop_kg_per_ha,
        "confidence": confidence,
        "confidence_source": source,
    }