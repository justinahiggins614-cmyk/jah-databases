import hashlib, json, math, random

CHAMBER_DIA_MM = 70
WATER_DEPTH_MM = 16
PERC_SLITS = 12
BUBBLES_PER_SLIT = 8
VAPOUR_TEMP_C = 220
WATER_TEMP_C = 20

def compute(seed):
    rng = random.Random(seed)
    radius = CHAMBER_DIA_MM / 2.0
    water_ml = round(math.pi * radius ** 2 * WATER_DEPTH_MM / 1000.0, 1)
    bubble_dia_mm = 3.0
    bubble_area = math.pi * bubble_dia_mm ** 2
    bubbles = PERC_SLITS * BUBBLES_PER_SLIT
    total_bubble_area = round(bubbles * bubble_area, 1)
    water_kg = water_ml / 1000.0
    vapour_drop_c = 85.0
    heat_j = round(water_kg * 4186.0 * vapour_drop_c, 1)
    out_temp = VAPOUR_TEMP_C - vapour_drop_c
    splash_margin = round(rng.uniform(4.0, 6.0), 1)
    out = {
        "chamber_diameter_mm": CHAMBER_DIA_MM,
        "water_depth_mm": WATER_DEPTH_MM,
        "water_volume_ml": water_ml,
        "percolator_slits": PERC_SLITS,
        "bubbles_per_draw": bubbles,
        "total_bubble_area_mm2": total_bubble_area,
        "vapour_in_temp_c": VAPOUR_TEMP_C,
        "vapour_out_temp_c": out_temp,
        "heat_absorbed_by_water_j": heat_j,
        "splash_margin_mm": splash_margin,
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
