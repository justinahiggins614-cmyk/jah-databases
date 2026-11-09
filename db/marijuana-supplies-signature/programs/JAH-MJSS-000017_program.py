"""The Pipe Cleaning Kit — working program.

Computes the same quantities as the record demo: the design numbers for
this supply, from the figures in the record. Standard library only, no
network. Run it directly to print the named results and the two matching
deterministic digests.
"""
import hashlib, json, math, random

CLEANER_LENGTH_MM = 150
GRIP_MM = 30
STEM_AIRWAY_MM = 120
BRUSH_DIA_MM = 12
BRUSH_LEN_MM = 25
CLEANERS_PER_KIT = 24

def compute(seed):
    rng = random.Random(seed)
    residue = 100.0
    passes = 0
    total_cleaner_mm = 0
    while residue > 1.0 and passes < 12:
        removed = residue * rng.uniform(0.35, 0.55)
        residue -= removed
        passes += 1
        total_cleaner_mm += CLEANER_LENGTH_MM
    reach = CLEANER_LENGTH_MM - GRIP_MM
    coverage = round(100.0 * reach / STEM_AIRWAY_MM, 1)
    brush_area = round(math.pi * BRUSH_DIA_MM * BRUSH_LEN_MM, 1)
    out = {
        "cleaner_length_mm": CLEANER_LENGTH_MM,
        "usable_reach_mm": reach,
        "airway_length_mm": STEM_AIRWAY_MM,
        "airway_coverage_percent": coverage,
        "passes_to_clean": passes,
        "residue_remaining_percent": round(residue, 2),
        "cleaner_length_used_mm": total_cleaner_mm,
        "brush_contact_area_mm2": brush_area,
        "cleaners_in_kit": CLEANERS_PER_KIT,
    }
    return out


class PipeCleaningKit:
    """Model of the pipe cleaning kit."""

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
    PipeCleaningKit().run()
