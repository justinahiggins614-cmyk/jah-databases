import hashlib, json, random
length_cm = 20.0
width_cm = 14.0
thickness_cm = 2.0
carbon_g = 10.0
capacity_g_per_g = 0.2
life_years = 1.5
face_area_cm2 = length_cm * width_cm
lining_area_cm2 = face_area_cm2 * 2.0
volume_cm3 = length_cm * width_cm * thickness_cm
volume_l = volume_cm3 / 1000.0
duffle_l = 50.8 * 27.9 * 27.9 / 1000.0
duffle_ratio = duffle_l / volume_l
trap_capacity_g = carbon_g * capacity_g_per_g
life_days = life_years * 365.0
loading_g_per_day = trap_capacity_g / life_days
def run_once(seed):
    rng = random.Random(seed)
    jitter = rng.uniform(-1.0, 1.0)
    return {"lining_area_cm2": round(lining_area_cm2, 2), "pouch_volume_l": round(volume_l + jitter / 100.0, 2), "duffle_volume_l": round(duffle_l, 2), "duffle_to_pouch_ratio": round(duffle_ratio, 2), "odour_trap_capacity_g": round(trap_capacity_g, 2), "average_loading_g_per_day": round(loading_g_per_day, 5)}
r1 = run_once(42)
r2 = run_once(42)
d1 = hashlib.sha256(json.dumps(r1, sort_keys=True).encode()).hexdigest()
d2 = hashlib.sha256(json.dumps(r2, sort_keys=True).encode()).hexdigest()
print("Carbon lining area (cm2): %.2f" % r1["lining_area_cm2"])
print("Pouch volume (L): %.2f" % r1["pouch_volume_l"])
print("Duffle volume (L): %.2f" % r1["duffle_volume_l"])
print("Duffle to pouch ratio: %.2f" % r1["duffle_to_pouch_ratio"])
print("Odour trap capacity (g): %.2f" % r1["odour_trap_capacity_g"])
print("Average loading (g per day): %.5f" % r1["average_loading_g_per_day"])
print("Run 1 SHA-256: %s" % d1)
print("Run 2 SHA-256: %s" % d2)
print("Deterministic: %s" % ("MATCH" if d1 == d2 else "MISMATCH"))