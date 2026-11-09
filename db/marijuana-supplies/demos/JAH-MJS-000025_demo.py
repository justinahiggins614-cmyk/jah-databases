"""Demo: beaker bong water and chamber volumes — The Beaker Bong."""
import hashlib, math
def compute():
    R = 50.0; r = 25.0; base_h = 70.0; water_h = 40.0; neck_d = 50.0; neck_h = 230.0
    r_water = R - (R - r) * (water_h / base_h)
    water_mm3 = math.pi * water_h / 3.0 * (R * R + R * r_water + r_water * r_water)
    base_mm3 = math.pi * base_h / 3.0 * (R * R + R * r + r * r)
    neck_mm3 = math.pi * (neck_d / 2.0) ** 2 * neck_h
    air_mm3 = (base_mm3 - water_mm3) + neck_mm3
    return {"water_volume_mL": round(water_mm3 / 1000.0, 2), "base_volume_mL": round(base_mm3 / 1000.0, 2), "neck_volume_mL": round(neck_mm3 / 1000.0, 2), "chamber_air_mL": round(air_mm3 / 1000.0, 2), "water_depth_mm": water_h, "base_diameter_mm": 2 * R}
def main():
    a = compute(); b = compute()
    sa = hashlib.sha256(repr(sorted(a.items())).encode()).hexdigest()
    sb = hashlib.sha256(repr(sorted(b.items())).encode()).hexdigest()
    for key in ["water_volume_mL", "base_volume_mL", "neck_volume_mL", "chamber_air_mL", "water_depth_mm", "base_diameter_mm"]:
        print(f"{key}: {a[key]}")
    print(f"Run 1 SHA-256: {sa}")
    print(f"Run 2 SHA-256: {sb}")
    print(f"Deterministic: {'MATCH' if sa == sb else 'MISMATCH'}")
if __name__ == "__main__":
    main()
