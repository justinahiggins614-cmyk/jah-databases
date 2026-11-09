"""Filter Tips (Crutches) — working program.

Computes the same quantities as the record demo: the design numbers for
this supply, from the figures in the record. Standard library only, no
network. Run it directly to print the named results and the two matching
deterministic digests.
"""
import hashlib, json, math, random

STRIP_LENGTH_MM = 50
STRIP_WIDTH_MM = 15
TIP_DIA_MM = 6
TIP_LENGTH_MM = 15
ACCORDION_FOLDS = 4
TIPS_PER_BOOKLET = 50

def compute(seed):
    rng = random.Random(seed)
    radius = TIP_DIA_MM / 2.0
    bore_area = round(math.pi * radius ** 2, 2)
    circumference = round(math.pi * TIP_DIA_MM, 2)
    strip_area = STRIP_LENGTH_MM * STRIP_WIDTH_MM
    booklet_area = STRIP_LENGTH_MM * STRIP_WIDTH_MM * TIPS_PER_BOOKLET
    fold_length = round(STRIP_LENGTH_MM * 0.25, 1)
    resistance = round(8.0 * 0.000018 * TIP_LENGTH_MM / (math.pi * (radius / 1000.0) ** 4), 1)
    draw_factor = round(rng.uniform(0.9, 1.1), 2)
    out = {
        "strip_length_mm": STRIP_LENGTH_MM,
        "strip_width_mm": STRIP_WIDTH_MM,
        "strip_area_mm2": strip_area,
        "tip_diameter_mm": TIP_DIA_MM,
        "tip_bore_area_mm2": bore_area,
        "tip_circumference_mm": circumference,
        "accordion_folds": ACCORDION_FOLDS,
        "folded_section_length_mm": fold_length,
        "tips_per_booklet": TIPS_PER_BOOKLET,
        "booklet_paper_area_mm2": booklet_area,
        "draw_resistance_proxy": resistance,
        "draw_factor": draw_factor,
    }
    return out


class FilterTips:
    """Model of filter tips (crutches)."""

    def __init__(self, seed=7):
        self.seed = seed

    def run(self):
        """Run the computation twice and print the named results."""
        first = compute(self.seed)
        second = compute(self.seed)
        for key, value in first.items():
            print(f"{key}: {value}")
        d1 = hashlib.sha256(json.dumps(first, sort_keys=True).encode()).hexdigest()
        d2 = hashlib.sha256(json.dumps(second, sort_keys=True).encode()).hexdigest()
        print(f"digest_run_1: {d1}")
        print(f"digest_run_2: {d2}")
        print("Deterministic: MATCH" if d1 == d2 else "Deterministic: MISMATCH")
        return first


if __name__ == "__main__":
    FilterTips().run()
