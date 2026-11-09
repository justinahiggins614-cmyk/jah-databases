"""Demo: pre-rolled cone volume — Pre-Rolled Cones."""
import hashlib, math
def compute():
    h = 109.0; R = 6.0; r = 3.5; tip = 24.0; rho = 0.15
    vol_mm3 = (math.pi * h / 3.0) * (R * R + R * r + r * r)
    vol_cm3 = vol_mm3 / 1000.0
    mass_g = vol_cm3 * rho
    bobbin_m = 5000.0
    cones_per_bobbin = bobbin_m * 1000.0 / h
    return {"cone_volume_mm3": round(vol_mm3, 2), "cone_volume_cm3": round(vol_cm3, 2), "capacity_g": round(mass_g, 2), "filter_tip_mm": tip, "cones_per_5000m_bobbin": round(cones_per_bobbin, 0)}
def main():
    a = compute(); b = compute()
    sa = hashlib.sha256(repr(sorted(a.items())).encode()).hexdigest()
    sb = hashlib.sha256(repr(sorted(b.items())).encode()).hexdigest()
    for key in ["cone_volume_mm3", "cone_volume_cm3", "capacity_g", "filter_tip_mm", "cones_per_5000m_bobbin"]:
        print(f"{key}: {a[key]}")
    print(f"Run 1 SHA-256: {sa}")
    print(f"Run 2 SHA-256: {sb}")
    print(f"Deterministic: {'MATCH' if sa == sb else 'MISMATCH'}")
if __name__ == "__main__":
    main()
