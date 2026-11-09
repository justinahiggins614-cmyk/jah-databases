import hashlib, json, random
ball_ft = 20.0
burn_min_per_ft = 2.5
cm_per_ft = 30.48
lighting_cm = 3.0
wick_flame_f = 1650.0
butane_flame_f = 3500.0
total_minutes = ball_ft * burn_min_per_ft
ball_cm = ball_ft * cm_per_ft
lightings = ball_cm / lighting_cm
burn_cm_per_min = cm_per_ft / burn_min_per_ft
burn_cm_per_s = burn_cm_per_min / 60.0
seconds_per_lighting = lighting_cm / burn_cm_per_s
spool_minutes = 250.0 * burn_min_per_ft
def run_once(seed):
    rng = random.Random(seed)
    jitter = rng.uniform(-0.1, 0.1)
    return {"total_burn_minutes": round(total_minutes, 2), "lightings_per_ball": round(lightings, 2), "burn_rate_cm_per_min": round(burn_cm_per_min + jitter, 2), "seconds_per_lighting": round(seconds_per_lighting, 2), "wick_to_butane_temp_ratio": round(wick_flame_f / butane_flame_f, 2), "spool_burn_hours": round(spool_minutes / 60.0, 2)}
r1 = run_once(42)
r2 = run_once(42)
d1 = hashlib.sha256(json.dumps(r1, sort_keys=True).encode()).hexdigest()
d2 = hashlib.sha256(json.dumps(r2, sort_keys=True).encode()).hexdigest()
print("Total burn time (minutes): %.2f" % r1["total_burn_minutes"])
print("Lightings per ball: %.2f" % r1["lightings_per_ball"])
print("Burn rate (cm per minute): %.2f" % r1["burn_rate_cm_per_min"])
print("Seconds per lighting: %.2f" % r1["seconds_per_lighting"])
print("Wick to butane temperature ratio: %.2f" % r1["wick_to_butane_temp_ratio"])
print("250 ft spool burn time (hours): %.2f" % r1["spool_burn_hours"])
print("Run 1 SHA-256: %s" % d1)
print("Run 2 SHA-256: %s" % d2)
print("Deterministic: %s" % ("MATCH" if d1 == d2 else "MISMATCH"))