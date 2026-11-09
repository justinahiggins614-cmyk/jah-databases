"""Demo: straight-tube bong water and chamber volumes — Signature Lance Straight Tube."""
import hashlib, math
def compute():
    d = 55.0; h = 340.0; water_h = 50.0; foot = 80.0
    area = math.pi * (d / 2.0) ** 2
    water_mm3 = area * water_h
    total_mm3 = area * h
    air_mm3 = total_mm3 - water_mm3
    pressure_pa = 1000.0 * 9.81 * (water_h / 1000.0)
    return {"water_volume_mL": round(water_mm3 / 1000.0, 2), "tube_volume_mL": round(total_mm3 / 1000.0, 2), "chamber_air_mL": round(air_mm3 / 1000.0, 2), "draw_pressure_Pa": round(pressure_pa, 2), "water_depth_mm": water_h, "tube_diameter_mm": d}
def main():
    a = compute(); b = compute()
    sa = hashlib.sha256(repr(sorted(a.items())).encode()).hexdigest()
    sb = hashlib.sha256(repr(sorted(b.items())).encode()).hexdigest()
    for key in ["water_volume_mL", "tube_volume_mL", "chamber_air_mL", "draw_pressure_Pa", "water_depth_mm", "tube_diameter_mm"]:
        print(f"{key}: {a[key]}")
    print(f"Run 1 SHA-256: {sa}")
    print(f"Run 2 SHA-256: {sb}")
    print(f"Deterministic: {'MATCH' if sa == sb else 'MISMATCH'}")
if __name__ == "__main__":
    main()
