"""Demo: silicone ashtray and lid volumes and heat storage — Signature Silicone Ashtray with Lid."""
import hashlib, math
def compute():
    d = 110.0; h = 32.0; wall = 5.0; lid_d = 114.0; lid_t = 6.0; rho = 1.15; cp = 1.46; dT = 200.0
    cap_mm3 = math.pi * ((d - 2.0 * wall) / 2.0) ** 2 * h
    cap_cm3 = cap_mm3 / 1000.0
    outer_mm3 = math.pi * (d / 2.0) ** 2 * (h + wall)
    body_cm3 = (outer_mm3 - cap_mm3) / 1000.0
    body_g = body_cm3 * rho
    lid_mm3 = math.pi * (lid_d / 2.0) ** 2 * lid_t
    lid_cm3 = lid_mm3 / 1000.0
    lid_g = lid_cm3 * rho
    total_g = body_g + lid_g
    heat_J = total_g * cp * dT
    return {"capacity_mm3": round(cap_mm3, 2), "capacity_cm3": round(cap_cm3, 2), "body_volume_cm3": round(body_cm3, 2), "body_mass_g": round(body_g, 2), "lid_volume_cm3": round(lid_cm3, 2), "lid_mass_g": round(lid_g, 2), "total_mass_g": round(total_g, 2), "heat_to_200C_J": round(heat_J, 2)}
def main():
    a = compute(); b = compute()
    sa = hashlib.sha256(repr(sorted(a.items())).encode()).hexdigest()
    sb = hashlib.sha256(repr(sorted(b.items())).encode()).hexdigest()
    for key in ['capacity_mm3', 'capacity_cm3', 'body_volume_cm3', 'body_mass_g', 'lid_volume_cm3', 'lid_mass_g', 'total_mass_g', 'heat_to_200C_J']:
        print(f"{key}: {a[key]}")
    print(f"Run 1 SHA-256: {sa}")
    print(f"Run 2 SHA-256: {sb}")
    print(f"Deterministic: {'MATCH' if sa == sb else 'MISMATCH'}")
if __name__ == "__main__":
    main()
