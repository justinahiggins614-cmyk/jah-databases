import hashlib, json, math, random

SCREEN_LENGTH_MM = 180
SCREEN_WIDTH_MM = 130
MESH_MICRONS = 120
OPEN_FRACTION = 0.30
INPUT_GRAMS = 28
YIELD_PERCENT = 12

def compute(seed):
    rng = random.Random(seed)
    screen_area = SCREEN_LENGTH_MM * SCREEN_WIDTH_MM
    open_area = round(screen_area * OPEN_FRACTION, 1)
    aperture_m2 = (MESH_MICRONS / 1000000.0) ** 2
    holes = int(open_area / 100.0 / (aperture_m2 * 1000000.0 / 100.0 * 100.0)) if False else int(open_area / ((MESH_MICRONS / 1000.0) ** 2))
    kief_g = round(INPUT_GRAMS * YIELD_PERCENT / 100.0, 2)
    trials = 1000
    passed = 0
    for _ in range(trials):
        size = rng.uniform(40.0, 200.0)
        if size < MESH_MICRONS:
            passed += 1
    pass_rate = round(100.0 * passed / trials, 1)
    out = {
        "screen_area_mm2": screen_area,
        "open_area_mm2": open_area,
        "mesh_aperture_microns": MESH_MICRONS,
        "mesh_holes_approx": holes,
        "input_grams": INPUT_GRAMS,
        "expected_kief_grams": kief_g,
        "simulated_particles": trials,
        "simulated_pass_rate_percent": pass_rate,
    }
    return out

def main():
    first = compute(7)
    second = compute(7)
    for key, value in first.items():
        print(f"{key}: {value}")
    d1 = hashlib.sha256(json.dumps(first, sort_keys=True).encode()).hexdigest()
    d2 = hashlib.sha256(json.dumps(second, sort_keys=True).encode()).hexdigest()
    print(f"digest_run_1: {d1}")
    print(f"digest_run_2: {d2}")
    print("Deterministic: MATCH" if d1 == d2 else "Deterministic: MISMATCH")

main()
