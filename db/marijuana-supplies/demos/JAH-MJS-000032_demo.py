"""Demo: metal bowl cup volume, metal mass, and screen area — The Metal Bowl."""
import hashlib, math
def compute():
    R = 10.0; r = 4.0; h = 16.0; oR = 12.0; o_r = 6.0; o_h = 18.0; rho_metal = 8.5; scr = 15.0; joint = 14.0; rho_pack = 0.15
    cup_mm3 = math.pi * h / 3.0 * (R * R + R * r + r * r)
    cup_cm3 = cup_mm3 / 1000.0
    cap = cup_cm3 * rho_pack
    outer_mm3 = math.pi * o_h / 3.0 * (oR * oR + oR * o_r + o_r * o_r)
    metal_cm3 = (outer_mm3 - cup_mm3) / 1000.0
    mass = metal_cm3 * rho_metal
    screen_area = math.pi * (scr / 2.0) ** 2
    return {"cup_volume_cm3": round(cup_cm3, 2), "capacity_g": round(cap, 2), "metal_volume_cm3": round(metal_cm3, 2), "mass_g": round(mass, 2), "screen_area_mm2": round(screen_area, 2), "joint_mm": joint}
def main():
    a = compute(); b = compute()
    sa = hashlib.sha256(repr(sorted(a.items())).encode()).hexdigest()
    sb = hashlib.sha256(repr(sorted(b.items())).encode()).hexdigest()
    for key in ["cup_volume_cm3", "capacity_g", "metal_volume_cm3", "mass_g", "screen_area_mm2", "joint_mm"]:
        print(f"{key}: {a[key]}")
    print(f"Run 1 SHA-256: {sa}")
    print(f"Run 2 SHA-256: {sb}")
    print(f"Deterministic: {'MATCH' if sa == sb else 'MISMATCH'}")
if __name__ == "__main__":
    main()
