"""Demo: ash-catcher bowl volumes and water fill — Signature Ash-Catcher Bowl."""
import hashlib, math
def compute():
    bowl_d = 22.0; bowl_h = 18.0; ch_d = 34.0; water_h = 25.0; fill = 0.60; pack = 0.15; joint = 18.0
    bowl_mm3 = math.pi * (bowl_d / 2.0) ** 2 * bowl_h
    bowl_cm3 = bowl_mm3 / 1000.0
    capacity_g = bowl_cm3 * pack
    ch_mm3 = math.pi * (ch_d / 2.0) ** 2 * water_h
    ch_cm3 = ch_mm3 / 1000.0
    water_ml = ch_cm3 * fill
    trap_mm2 = math.pi * (ch_d / 2.0) ** 2
    return {"bowl_volume_mm3": round(bowl_mm3, 2), "bowl_volume_cm3": round(bowl_cm3, 2), "herb_capacity_g": round(capacity_g, 2), "chamber_volume_cm3": round(ch_cm3, 2), "water_ml": round(water_ml, 2), "water_mass_g": round(water_ml, 2), "trap_area_mm2": round(trap_mm2, 2), "joint_mm": joint}
def main():
    a = compute(); b = compute()
    sa = hashlib.sha256(repr(sorted(a.items())).encode()).hexdigest()
    sb = hashlib.sha256(repr(sorted(b.items())).encode()).hexdigest()
    for key in ['bowl_volume_mm3', 'bowl_volume_cm3', 'herb_capacity_g', 'chamber_volume_cm3', 'water_ml', 'water_mass_g', 'trap_area_mm2', 'joint_mm']:
        print(f"{key}: {a[key]}")
    print(f"Run 1 SHA-256: {sa}")
    print(f"Run 2 SHA-256: {sb}")
    print(f"Deterministic: {'MATCH' if sa == sb else 'MISMATCH'}")
if __name__ == "__main__":
    main()
