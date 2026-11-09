"""Demo: water pipe water and chamber volumes — The Water Pipe (Bong)."""
import hashlib, math
def compute():
    tube_d = 55.0; height = 320.0; water_h = 55.0; down_d = 12.0; bubble_d = 3.0
    area_mm2 = math.pi * (tube_d / 2.0) ** 2
    water_mm3 = area_mm2 * water_h
    chamber_h = height - water_h
    chamber_mm3 = area_mm2 * chamber_h
    bubble_r = bubble_d / 2.0
    bubble_vol_mm3 = (4.0 / 3.0) * math.pi * bubble_r ** 3
    bubble_area_mm2 = 4.0 * math.pi * bubble_r ** 2
    pressure_pa = 1000.0 * 9.81 * (water_h / 1000.0)
    return {"water_volume_mm3": round(water_mm3, 1), "water_volume_mL": round(water_mm3 / 1000.0, 1), "chamber_volume_mL": round(chamber_mm3 / 1000.0, 1), "bubble_volume_mm3": round(bubble_vol_mm3, 2), "bubble_surface_mm2": round(bubble_area_mm2, 2), "draw_pressure_Pa": round(pressure_pa, 1)}
def main():
    a = compute(); b = compute()
    sa = hashlib.sha256(repr(sorted(a.items())).encode()).hexdigest()
    sb = hashlib.sha256(repr(sorted(b.items())).encode()).hexdigest()
    for key in ["water_volume_mm3", "water_volume_mL", "chamber_volume_mL", "bubble_volume_mm3", "bubble_surface_mm2", "draw_pressure_Pa"]:
        print(f"{key}: {a[key]}")
    print(f"Run 1 SHA-256: {sa}")
    print(f"Run 2 SHA-256: {sb}")
    print(f"Deterministic: {'MATCH' if sa == sb else 'MISMATCH'}")
if __name__ == "__main__":
    main()
