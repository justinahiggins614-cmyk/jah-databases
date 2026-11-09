"""Demo: desktop vaporizer balloon fill — The Desktop Vaporizer."""
import hashlib
def compute():
    heater_w = 100.0; heatup_s = 180.0; airflow = 4.0; fill_s = 45.0; balloon_l = 3.0; temp_c = 190.0
    heatup_energy_j = heater_w * heatup_s
    fill_min = fill_s / 60.0
    filled_l = airflow * fill_min
    fill_fraction = filled_l / balloon_l
    fills_per_hour = 3600.0 / fill_s
    return {"heatup_energy_J": round(heatup_energy_j, 1), "heatup_energy_Wh": round(heatup_energy_j / 3600.0, 2), "filled_volume_L": round(filled_l, 2), "balloon_volume_L": balloon_l, "fill_fraction": round(fill_fraction, 2), "target_temp_C": temp_c}
def main():
    a = compute(); b = compute()
    sa = hashlib.sha256(repr(sorted(a.items())).encode()).hexdigest()
    sb = hashlib.sha256(repr(sorted(b.items())).encode()).hexdigest()
    for key in ["heatup_energy_J", "heatup_energy_Wh", "filled_volume_L", "balloon_volume_L", "fill_fraction", "target_temp_C"]:
        print(f"{key}: {a[key]}")
    print(f"Run 1 SHA-256: {sa}")
    print(f"Run 2 SHA-256: {sb}")
    print(f"Deterministic: {'MATCH' if sa == sb else 'MISMATCH'}")
if __name__ == "__main__":
    main()
