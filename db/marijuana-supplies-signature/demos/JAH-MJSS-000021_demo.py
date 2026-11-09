import hashlib, json, math, random

TOOL_MASS_G = 18
TITANIUM_CP = 0.523
DELTA_T_K = 200
PICK_TIP_MM = 1
LOAD_FORCE_N = 0.5
TOOLS_IN_SET = 5

def compute(seed):
    rng = random.Random(seed)
    heat_j = round(TOOL_MASS_G * TITANIUM_CP * DELTA_T_K, 1)
    tip_radius_m = (PICK_TIP_MM / 2.0) / 1000.0
    tip_area_m2 = math.pi * tip_radius_m ** 2
    tip_pressure_pa = round(LOAD_FORCE_N / tip_area_m2, 1)
    load_g = round(TOOL_MASS_G * 0.02, 2)
    per_tool_j = round(heat_j / TOOLS_IN_SET, 1)
    cool_seconds = round(heat_j / 25.0, 1)
    wobble = round(rng.uniform(0.98, 1.02), 3)
    out = {
        "tool_mass_g": TOOL_MASS_G,
        "titanium_specific_heat_j_per_g_k": TITANIUM_CP,
        "temperature_change_k": DELTA_T_K,
        "heat_absorbed_j": heat_j,
        "heat_per_tool_j": per_tool_j,
        "pick_tip_pressure_pa": tip_pressure_pa,
        "typical_load_grams": load_g,
        "cooling_time_seconds": cool_seconds,
        "tools_in_set": TOOLS_IN_SET,
        "measurement_jitter": wobble,
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
