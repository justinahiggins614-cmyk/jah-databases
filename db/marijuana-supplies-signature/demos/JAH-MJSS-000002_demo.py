"""Demo: electric grinder battery energy — The Electric Herb Grinder."""
import hashlib
def compute():
    v = 3.7; cap_mah = 3000.0; motor_w = 6.0; grind_s = 5.0; load_g = 4.0
    battery_wh = v * (cap_mah / 1000.0)
    energy_per_grind_wh = motor_w * grind_s / 3600.0
    energy_per_grind_j = motor_w * grind_s
    grinds_per_charge = battery_wh / energy_per_grind_wh
    current_a = motor_w / v
    return {"battery_wh": round(battery_wh, 3), "energy_per_grind_Wh": round(energy_per_grind_wh, 5), "energy_per_grind_J": round(energy_per_grind_j, 2), "grinds_per_charge": round(grinds_per_charge, 1), "motor_current_A": round(current_a, 2), "load_g": load_g}
def main():
    a = compute(); b = compute()
    sa = hashlib.sha256(repr(sorted(a.items())).encode()).hexdigest()
    sb = hashlib.sha256(repr(sorted(b.items())).encode()).hexdigest()
    for key in ["battery_wh", "energy_per_grind_Wh", "energy_per_grind_J", "grinds_per_charge", "motor_current_A", "load_g"]:
        print(f"{key}: {a[key]}")
    print(f"Run 1 SHA-256: {sa}")
    print(f"Run 2 SHA-256: {sb}")
    print(f"Deterministic: {'MATCH' if sa == sb else 'MISMATCH'}")
if __name__ == "__main__":
    main()
