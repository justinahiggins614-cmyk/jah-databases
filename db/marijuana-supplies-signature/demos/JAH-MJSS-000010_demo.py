import hashlib, json, math, random
roller_diameter_mm = 12.0
roller_length_mm = 70.0
paper_width_mm = 44.0
density_g_per_cm3 = 0.25
circumference_mm = math.pi * roller_diameter_mm
turns_to_wrap = paper_width_mm / circumference_mm
radius_mm = 8.0 / 2.0
cross_area_mm2 = math.pi * radius_mm * radius_mm
volume_cm3 = cross_area_mm2 * roller_length_mm / 1000.0
mass_g = volume_cm3 * density_g_per_cm3
king_volume_cm3 = cross_area_mm2 * 110.0 / 1000.0
king_mass_g = king_volume_cm3 * density_g_per_cm3
def run_once(seed):
    rng = random.Random(seed)
    jitter = rng.uniform(-0.01, 0.01)
    return {"roller_circumference_mm": round(circumference_mm, 2), "turns_to_wrap_paper": round(turns_to_wrap, 2), "roll_volume_cm3": round(volume_cm3 + jitter, 2), "roll_mass_g": round(mass_g, 2), "king_size_mass_g": round(king_mass_g, 2), "king_to_standard_ratio": round(king_mass_g / mass_g, 2)}
r1 = run_once(42)
r2 = run_once(42)
d1 = hashlib.sha256(json.dumps(r1, sort_keys=True).encode()).hexdigest()
d2 = hashlib.sha256(json.dumps(r2, sort_keys=True).encode()).hexdigest()
print("Roller circumference (mm): %.2f" % r1["roller_circumference_mm"])
print("Turns to wrap paper: %.2f" % r1["turns_to_wrap_paper"])
print("Roll volume (cm3): %.2f" % r1["roll_volume_cm3"])
print("Roll mass (g): %.2f" % r1["roll_mass_g"])
print("King-size mass (g): %.2f" % r1["king_size_mass_g"])
print("King to standard ratio: %.2f" % r1["king_to_standard_ratio"])
print("Run 1 SHA-256: %s" % d1)
print("Run 2 SHA-256: %s" % d2)
print("Deterministic: %s" % ("MATCH" if d1 == d2 else "MISMATCH"))