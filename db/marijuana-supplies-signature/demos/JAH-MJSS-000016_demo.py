import hashlib, json, random
capacity_g = 50.0
readability_g = 0.01
tolerance_g = 0.03
cal_weight_g = 50.0
steps = capacity_g / readability_g
tolerance_steps = tolerance_g / readability_g
load1_g = 1.00
load25_g = 25.00
rel_err_1g = tolerance_g / load1_g * 100.0
rel_err_25g = tolerance_g / load25_g * 100.0
oz_per_g = 1.0 / 28.3495
one_oz_g = 28.3495
cal_error_g = 50.00 - 49.97
def run_once(seed):
    rng = random.Random(seed)
    jitter = rng.uniform(-0.001, 0.001)
    return {"display_steps": round(steps, 2), "tolerance_in_steps": round(tolerance_steps, 2), "relative_error_1g_pct": round(rel_err_1g + jitter, 2), "relative_error_25g_pct": round(rel_err_25g, 2), "grams_per_ounce": round(one_oz_g, 2), "ounces_per_gram": round(oz_per_g, 5), "calibration_error_g": round(cal_error_g, 2)}
r1 = run_once(42)
r2 = run_once(42)
d1 = hashlib.sha256(json.dumps(r1, sort_keys=True).encode()).hexdigest()
d2 = hashlib.sha256(json.dumps(r2, sort_keys=True).encode()).hexdigest()
print("Display steps: %.2f" % r1["display_steps"])
print("Tolerance in steps: %.2f" % r1["tolerance_in_steps"])
print("Relative error at 1 g (percent): %.2f" % r1["relative_error_1g_pct"])
print("Relative error at 25 g (percent): %.2f" % r1["relative_error_25g_pct"])
print("Grams per ounce: %.2f" % r1["grams_per_ounce"])
print("Ounces per gram: %.5f" % r1["ounces_per_gram"])
print("Calibration error (g): %.2f" % r1["calibration_error_g"])
print("Run 1 SHA-256: %s" % d1)
print("Run 2 SHA-256: %s" % d2)
print("Deterministic: %s" % ("MATCH" if d1 == d2 else "MISMATCH"))