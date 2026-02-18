"""
CELPIP Scoring Service.

Listening & Reading: raw score → CELPIP band (1–12)
Writing & Speaking: dimensional scores averaged → band
"""


# Approximate conversion table (raw correct / total → CELPIP band)
# Based on publicly available score conversion guidance
LISTENING_CONVERSION = {
    38: 12, 37: 12, 36: 11, 35: 11, 34: 10, 33: 10,
    32: 9, 31: 9, 30: 8, 29: 8, 28: 7, 27: 7,
    26: 6, 25: 6, 24: 5, 22: 5, 20: 4, 18: 3,
    15: 2, 10: 1,
}

READING_CONVERSION = {
    38: 12, 37: 12, 36: 11, 35: 11, 34: 10, 33: 10,
    32: 9, 31: 9, 30: 8, 29: 8, 28: 7, 27: 7,
    26: 6, 25: 6, 24: 5, 22: 5, 20: 4, 18: 3,
    15: 2, 10: 1,
}


def raw_to_band(raw: int, conversion: dict) -> int:
    """Convert raw score to CELPIP band using step-down lookup."""
    for threshold in sorted(conversion.keys(), reverse=True):
        if raw >= threshold:
            return conversion[threshold]
    return 1


def calculate_listening_score(correct: int, total: int = 38) -> float:
    return float(raw_to_band(correct, LISTENING_CONVERSION))


def calculate_reading_score(correct: int, total: int = 38) -> float:
    return float(raw_to_band(correct, READING_CONVERSION))


def calculate_writing_score(dimensions: dict) -> float:
    """Average of content, coherence, vocabulary, readability, task_fulfillment."""
    values = [v for v in dimensions.values() if v is not None]
    if not values:
        return 0.0
    return round(sum(values) / len(values), 1)


def calculate_speaking_score(dimensions: dict) -> float:
    """Average of content, vocabulary, listenability, task_fulfillment."""
    values = [v for v in dimensions.values() if v is not None]
    if not values:
        return 0.0
    return round(sum(values) / len(values), 1)


def clb_level(band: float) -> str:
    mapping = {
        12: "CLB 12 — Advanced",
        11: "CLB 11 — Advanced",
        10: "CLB 10 — Highly Effective",
        9: "CLB 9 — Effective",
        8: "CLB 8 — Good",
        7: "CLB 7 — Adequate",
        6: "CLB 6 — Developing",
        5: "CLB 5 — Developing",
        4: "CLB 4 — Basic",
        3: "CLB 3 — Basic",
        2: "CLB 2 — Beginner",
        1: "CLB 1 — Beginner",
    }
    return mapping.get(int(band), "N/A")
