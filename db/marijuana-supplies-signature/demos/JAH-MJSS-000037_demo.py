"""Demo: ceramic ashtray capacity and heat storage — Signature Ceramic Ashtray."""
import hashlib, math
def compute():
    d = 140.0; h = 37.0; depth = 30.0; wall = 7.0; rests = 4; rho = 2.4; cp = 0.85; dT = 200.0
    outer_mm3 = math.pi * (d / 2.0) ** 2 * h
    cap_mm3 = math.pi * ((d - 2.0 * wall) / 2.0) ** 2 * depth
    cap_cm3 = cap_mm3 / 1000.0
    shell_mm3 = outer_mm3 - cap_mm3
    shell_cm3 = shell_mm3 / 1000.0
    mass_g = shell_cm3 * rho
    heat_J = mass_g * cp * dT
    return {"outer_volume_mm3": round(outer_mm3, 2), "capacity_mm3": round(cap_mm3, 2), "capacity_cm3": round(cap_cm3, 2), "shell_volume_cm3": round(shell_cm3, 2), "ceramic_mass_g": round(mass_g, 2), "heat_to_200C_J": round(heat_J, 2), "rim_notches": rests}
def main():
    a = compute(); b = compute()
    sa = hashlib.sha256(repr(sorted(a.items())).encode()).hexdigest()
    sb = hashlib.sha256(repr(sorted(b.items())).encode()).hexdigest()
    for key in ['outer_volume_mm3', 'capacity_mm3', 'capacity_cm3', 'shell_volume_cm3', 'ceramic_mass_g', 'heat_to_200C_J', 'rim_notches']:
        print(f"{key}: {a[key]}")
    print(f"Run 1 SHA-256: {sa}")
    print(f"Run 2 SHA-256: {sb}")
    print(f"Deterministic: {'MATCH' if sa == sb else 'MISMATCH'}")
if __name__ == "__main__":
    main()
