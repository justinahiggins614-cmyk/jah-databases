"""The Ashtray with Poker — working program.

Computes the same quantities as the record demo: the design numbers for
this supply, from the figures in the record. Standard library only, no
network. Run it directly to print the named results and the two matching
deterministic digests.
"""
import hashlib, json, math, random

BOWL_DIA_MM = 110
BOWL_DEPTH_MM = 35
POKER_HEIGHT_MM = 60
POKER_FORCE_N = 2.0
ASH_ML_PER_SESSION = 4

def compute(seed):
    rng = random.Random(seed)
    radius = BOWL_DIA_MM / 2.0
    gross_ml = round(math.pi * radius ** 2 * BOWL_DEPTH_MM / 1000.0, 1)
    usable_ml = round(gross_ml * 0.8, 1)
    ash_capacity_g = round(usable_ml * 0.35, 1)
    torque_nm = round(POKER_FORCE_N * POKER_HEIGHT_MM / 1000.0, 3)
    sessions = int(usable_ml // ASH_ML_PER_SESSION)
    jitter = round(rng.uniform(0.95, 1.05), 3)
    out = {
        "bowl_diameter_mm": BOWL_DIA_MM,
        "bowl_depth_mm": BOWL_DEPTH_MM,
        "bowl_gross_volume_ml": gross_ml,
        "bowl_usable_volume_ml": usable_ml,
        "ash_capacity_grams": ash_capacity_g,
        "sessions_before_emptying": sessions,
        "poker_height_mm": POKER_HEIGHT_MM,
        "poker_torque_nm": torque_nm,
        "measurement_jitter": jitter,
    }
    return out


class AshtrayWithPoker:
    """Model of the ashtray with poker."""

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
    AshtrayWithPoker().run()
