"""The Isopropyl Alcohol Cleaning Soak — working program.

Computes the same quantities as the record demo: the design numbers for
this supply, from the figures in the record. Standard library only, no
network. Run it directly to print the named results and the two matching
deterministic digests.
"""
import hashlib, json, math, random

ALCOHOL_PERCENT = 91
ALCOHOL_VOLUME_ML = 250
SALT_GRAMS = 18
SOAK_LIGHT_MIN = 30
SOAK_HEAVY_MIN = 720
SHAKE_SECONDS = 90

def compute(seed):
    rng = random.Random(seed)
    water_fraction = 1.0 - ALCOHOL_PERCENT / 100.0
    pure_alcohol_ml = round(ALCOHOL_VOLUME_ML * ALCOHOL_PERCENT / 100.0, 1)
    water_ml = round(ALCOHOL_VOLUME_ML * water_fraction, 1)
    salt_ratio = round(SALT_GRAMS / ALCOHOL_VOLUME_ML, 3)
    k = 0.02 + 0.0006 * ALCOHOL_PERCENT
    eff_light = round(100.0 * (1.0 - math.exp(-k * SOAK_LIGHT_MIN)), 1)
    eff_heavy = round(100.0 * (1.0 - math.exp(-k * SOAK_HEAVY_MIN)), 1)
    evap_ml_per_hour = round(ALCOHOL_VOLUME_ML * 0.04 * rng.uniform(0.9, 1.1), 1)
    shakes = SHAKE_SECONDS // 30
    out = {
        "alcohol_percent": ALCOHOL_PERCENT,
        "solution_volume_ml": ALCOHOL_VOLUME_ML,
        "pure_alcohol_ml": pure_alcohol_ml,
        "water_in_solution_ml": water_ml,
        "salt_grams": SALT_GRAMS,
        "salt_grams_per_ml": salt_ratio,
        "shake_blocks_of_30s": shakes,
        "resin_dissolved_light_soak_percent": eff_light,
        "resin_dissolved_heavy_soak_percent": eff_heavy,
        "evaporation_ml_per_hour": evap_ml_per_hour,
    }
    return out


class AlcoholCleaningSoak:
    """Model of the isopropyl alcohol cleaning soak."""

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
    AlcoholCleaningSoak().run()
