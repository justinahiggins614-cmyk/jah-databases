import hashlib, json, math, random

INSIDE_L_MM = 210
INSIDE_W_MM = 165
INSIDE_H_MM = 100
LOCK_DIGITS = 3
SEAL_COUNT = 2
TRAY_COMPARTMENTS = 6

def compute(seed):
    rng = random.Random(seed)
    inside_ml = INSIDE_L_MM * INSIDE_W_MM * INSIDE_H_MM
    inside_litres = round(inside_ml / 1000000.0, 2)
    outside_ml = 235 * 190 * 127
    wall_volume_ml = round((outside_ml - inside_ml) / 1000.0, 1)
    combinations = 10 ** LOCK_DIGITS
    brute_seconds = combinations * 1
    brute_minutes = round(brute_seconds / 60.0, 1)
    per_compartment_ml = round(inside_ml / TRAY_COMPARTMENTS / 1000.0, 1)
    seal_force_n = round(SEAL_COUNT * 12.5 * rng.uniform(0.95, 1.05), 1)
    out = {
        "inside_volume_ml": inside_ml,
        "inside_volume_litres": inside_litres,
        "shell_volume_ml": wall_volume_ml,
        "lock_digits": LOCK_DIGITS,
        "lock_combinations": combinations,
        "brute_force_seconds_at_1_per_s": brute_seconds,
        "brute_force_minutes": brute_minutes,
        "tray_compartments": TRAY_COMPARTMENTS,
        "volume_per_compartment_ml": per_compartment_ml,
        "seal_closing_force_n": seal_force_n,
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
