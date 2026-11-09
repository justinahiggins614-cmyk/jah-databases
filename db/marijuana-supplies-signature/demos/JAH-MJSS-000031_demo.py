"""Demo: glass bowl cup volume and joint areas — Signature Precision Glass Bowl."""
import hashlib, math
def compute():
    joint = 18.0; R = 13.0; r = 5.0; h = 20.0; hole = 3.5; s_len = 40.0; s_bore = 9.0; rho = 0.15
    cup_mm3 = math.pi * h / 3.0 * (R * R + R * r + r * r)
    cup_cm3 = cup_mm3 / 1000.0
    cap = cup_cm3 * rho
    a14 = math.pi * (14.0 / 2.0) ** 2
    a18 = math.pi * (18.0 / 2.0) ** 2
    ratio = a18 / a14
    hole_area = math.pi * (hole / 2.0) ** 2
    stem_mm3 = math.pi * (s_bore / 2.0) ** 2 * s_len
    return {"cup_volume_cm3": round(cup_cm3, 2), "capacity_g": round(cap, 2), "joint_area_14mm_mm2": round(a14, 2), "joint_area_18mm_mm2": round(a18, 2), "area_ratio": round(ratio, 2), "hole_area_mm2": round(hole_area, 2), "stem_volume_mL": round(stem_mm3 / 1000.0, 2)}
def main():
    a = compute(); b = compute()
    sa = hashlib.sha256(repr(sorted(a.items())).encode()).hexdigest()
    sb = hashlib.sha256(repr(sorted(b.items())).encode()).hexdigest()
    for key in ["cup_volume_cm3", "capacity_g", "joint_area_14mm_mm2", "joint_area_18mm_mm2", "area_ratio", "hole_area_mm2", "stem_volume_mL"]:
        print(f"{key}: {a[key]}")
    print(f"Run 1 SHA-256: {sa}")
    print(f"Run 2 SHA-256: {sb}")
    print(f"Deterministic: {'MATCH' if sa == sb else 'MISMATCH'}")
if __name__ == "__main__":
    main()
