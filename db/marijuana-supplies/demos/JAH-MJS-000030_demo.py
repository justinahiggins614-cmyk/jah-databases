"""Demo: bubbler water, bowl, and chamber volumes — The Bubbler."""
import hashlib, math
def compute():
    ch_d = 45.0; water_h = 15.0; b_d = 18.0; b_h = 12.0; b_r = 3.0; ch_len = 60.0; rho = 0.15
    water_mm3 = math.pi * (ch_d / 2.0) ** 2 * water_h
    bowl_mm3 = math.pi * b_h / 3.0 * ((b_d / 2.0) ** 2 + (b_d / 2.0) * b_r + b_r * b_r)
    bowl_cm3 = bowl_mm3 / 1000.0
    cap = bowl_cm3 * rho
    chamber_mm3 = math.pi * (ch_d / 2.0) ** 2 * ch_len
    return {"water_volume_mL": round(water_mm3 / 1000.0, 2), "bowl_volume_cm3": round(bowl_cm3, 2), "capacity_g": round(cap, 2), "chamber_volume_mL": round(chamber_mm3 / 1000.0, 2), "bowl_diameter_mm": b_d}
def main():
    a = compute(); b = compute()
    sa = hashlib.sha256(repr(sorted(a.items())).encode()).hexdigest()
    sb = hashlib.sha256(repr(sorted(b.items())).encode()).hexdigest()
    for key in ["water_volume_mL", "bowl_volume_cm3", "capacity_g", "chamber_volume_mL", "bowl_diameter_mm"]:
        print(f"{key}: {a[key]}")
    print(f"Run 1 SHA-256: {sa}")
    print(f"Run 2 SHA-256: {sb}")
    print(f"Deterministic: {'MATCH' if sa == sb else 'MISMATCH'}")
if __name__ == "__main__":
    main()
