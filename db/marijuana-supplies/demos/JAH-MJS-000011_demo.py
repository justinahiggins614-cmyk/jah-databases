import hashlib, json, random
fuel_mass_g = 8.0
energy_mj_per_kg = 49.5
burn_rate_g_per_s = 0.05
flame_temp_c = 1430.0
soft_temp_c = 1000.0
energy_kj = fuel_mass_g / 1000.0 * energy_mj_per_kg * 1000.0
burn_seconds = fuel_mass_g / burn_rate_g_per_s
power_w = burn_rate_g_per_s / 1000.0 * energy_mj_per_kg * 1000000.0
flame_temp_f = flame_temp_c * 9.0 / 5.0 + 32.0
soft_temp_f = soft_temp_c * 9.0 / 5.0 + 32.0
butane_for_10kj_g = 10.0 / (energy_mj_per_kg * 1000.0) * 1000.0
def run_once(seed):
    rng = random.Random(seed)
    jitter = rng.uniform(-0.5, 0.5)
    return {"tank_energy_kj": round(energy_kj, 2), "burn_seconds": round(burn_seconds, 2), "power_w": round(power_w, 2), "flame_temp_f": round(flame_temp_f + jitter, 2), "soft_flame_temp_f": round(soft_temp_f, 2), "butane_for_10kj_g": round(butane_for_10kj_g, 3)}
r1 = run_once(42)
r2 = run_once(42)
d1 = hashlib.sha256(json.dumps(r1, sort_keys=True).encode()).hexdigest()
d2 = hashlib.sha256(json.dumps(r2, sort_keys=True).encode()).hexdigest()
print("Tank energy (kJ): %.2f" % r1["tank_energy_kj"])
print("Burn time (s): %.2f" % r1["burn_seconds"])
print("Power while lit (W): %.2f" % r1["power_w"])
print("Flame temperature (F): %.2f" % r1["flame_temp_f"])
print("Soft flame temperature (F): %.2f" % r1["soft_flame_temp_f"])
print("Butane for 10 kJ (g): %.3f" % r1["butane_for_10kj_g"])
print("Run 1 SHA-256: %s" % d1)
print("Run 2 SHA-256: %s" % d2)
print("Deterministic: %s" % ("MATCH" if d1 == d2 else "MISMATCH"))