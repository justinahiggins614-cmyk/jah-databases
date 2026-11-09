"""Demo: portable vaporizer heating energy — The Portable Dry-Herb Vaporizer."""
import hashlib
def compute():
    herb_g = 0.25; t0 = 20.0; t1 = 190.0; cp = 1.7; battery_wh = 10.0; oven_g = 12.0; oven_cp = 0.9
    q_herb_j = herb_g * cp * (t1 - t0)
    q_oven_j = oven_g * oven_cp * (t1 - t0)
    q_total_j = q_herb_j + q_oven_j
    q_total_wh = q_total_j / 3600.0
    sessions = battery_wh / q_total_wh
    temp_rise_c = t1 - t0
    return {"herb_heat_J": round(q_herb_j, 2), "oven_heat_J": round(q_oven_j, 2), "total_heat_J": round(q_total_j, 2), "total_heat_Wh": round(q_total_wh, 4), "sessions_per_charge": round(sessions, 1), "temp_rise_C": temp_rise_c}
def main():
    a = compute(); b = compute()
    sa = hashlib.sha256(repr(sorted(a.items())).encode()).hexdigest()
    sb = hashlib.sha256(repr(sorted(b.items())).encode()).hexdigest()
    for key in ["herb_heat_J", "oven_heat_J", "total_heat_J", "total_heat_Wh", "sessions_per_charge", "temp_rise_C"]:
        print(f"{key}: {a[key]}")
    print(f"Run 1 SHA-256: {sa}")
    print(f"Run 2 SHA-256: {sb}")
    print(f"Deterministic: {'MATCH' if sa == sb else 'MISMATCH'}")
if __name__ == "__main__":
    main()
