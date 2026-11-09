"""Demo: chillum bore frustum volume and bowl capacity — The Chillum."""
import hashlib, math
def compute():
    L = 110.0; d_bowl = 18.0; d_mouth = 8.0; od_bowl = 22.0; od_mouth = 12.0; stone_d = 10.0; bowl_len = 30.0; pack = 0.15; rho = 2.23
    R = d_bowl / 2.0; r = d_mouth / 2.0
    bore_mm3 = (1.0 / 3.0) * math.pi * L * (R ** 2 + R * r + r ** 2)
    bore_cm3 = bore_mm3 / 1000.0
    stone_mm3 = (4.0 / 3.0) * math.pi * (stone_d / 2.0) ** 3
    free_mm3 = bore_mm3 - stone_mm3
    free_cm3 = free_mm3 / 1000.0
    Ro = od_bowl / 2.0; ro = od_mouth / 2.0
    outer_mm3 = (1.0 / 3.0) * math.pi * L * (Ro ** 2 + Ro * ro + ro ** 2)
    glass_cm3 = (outer_mm3 - bore_mm3) / 1000.0
    mass_g = glass_cm3 * rho
    d_end = d_bowl - (d_bowl - d_mouth) * bowl_len / L
    bowl_mm3 = (1.0 / 3.0) * math.pi * bowl_len * (R ** 2 + R * (d_end / 2.0) + (d_end / 2.0) ** 2)
    bowl_cm3 = bowl_mm3 / 1000.0
    capacity_g = bowl_cm3 * pack
    return {"bore_volume_mm3": round(bore_mm3, 2), "bore_volume_cm3": round(bore_cm3, 2), "stone_volume_mm3": round(stone_mm3, 2), "free_volume_cm3": round(free_cm3, 2), "glass_volume_cm3": round(glass_cm3, 2), "glass_mass_g": round(mass_g, 2), "bowl_volume_cm3": round(bowl_cm3, 2), "herb_capacity_g": round(capacity_g, 2)}
def main():
    a = compute(); b = compute()
    sa = hashlib.sha256(repr(sorted(a.items())).encode()).hexdigest()
    sb = hashlib.sha256(repr(sorted(b.items())).encode()).hexdigest()
    for key in ['bore_volume_mm3', 'bore_volume_cm3', 'stone_volume_mm3', 'free_volume_cm3', 'glass_volume_cm3', 'glass_mass_g', 'bowl_volume_cm3', 'herb_capacity_g']:
        print(f"{key}: {a[key]}")
    print(f"Run 1 SHA-256: {sa}")
    print(f"Run 2 SHA-256: {sb}")
    print(f"Deterministic: {'MATCH' if sa == sb else 'MISMATCH'}")
if __name__ == "__main__":
    main()
