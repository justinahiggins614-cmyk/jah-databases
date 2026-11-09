import hashlib, json, math, random
volume_ml = 946.0
fill_fraction = 0.75
diameter_cm = 9.5
vapour_g_per_m3 = 10.7
contents_ml = volume_ml * fill_fraction
headspace_ml = volume_ml - contents_ml
radius_cm = diameter_cm / 2.0
cross_area_cm2 = math.pi * radius_cm * radius_cm
height_cm = volume_ml / cross_area_cm2
headspace_m3 = headspace_ml / 1000000.0
vapour_g = headspace_m3 * vapour_g_per_m3
half_gallon_ratio = 1893.0 / 946.0
def run_once(seed):
    rng = random.Random(seed)
    jitter = rng.uniform(-0.1, 0.1)
    return {"contents_ml": round(contents_ml, 2), "headspace_ml": round(headspace_ml, 2), "jar_height_cm": round(height_cm + jitter, 2), "headspace_water_vapour_g": round(vapour_g, 5), "pint_volume_ml": 473.0, "half_gallon_to_quart_ratio": round(half_gallon_ratio, 2)}
r1 = run_once(42)
r2 = run_once(42)
d1 = hashlib.sha256(json.dumps(r1, sort_keys=True).encode()).hexdigest()
d2 = hashlib.sha256(json.dumps(r2, sort_keys=True).encode()).hexdigest()
print("Contents at 75 percent (ml): %.2f" % r1["contents_ml"])
print("Headspace (ml): %.2f" % r1["headspace_ml"])
print("Jar height from volume (cm): %.2f" % r1["jar_height_cm"])
print("Headspace water vapour (g): %.5f" % r1["headspace_water_vapour_g"])
print("Pint jar volume (ml): %.2f" % r1["pint_volume_ml"])
print("Half-gallon to quart ratio: %.2f" % r1["half_gallon_to_quart_ratio"])
print("Run 1 SHA-256: %s" % d1)
print("Run 2 SHA-256: %s" % d2)
print("Deterministic: %s" % ("MATCH" if d1 == d2 else "MISMATCH"))