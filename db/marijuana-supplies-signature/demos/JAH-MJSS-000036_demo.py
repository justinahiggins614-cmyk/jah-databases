"""Demo: glass ashtray capacity and thermal expansion — Signature Glass Ashtray."""
import hashlib, math
def compute():
    d = 130.0; h = 30.0; wall = 5.0; rests = 4; rho = 2.23; alpha = 3.3e-06; dT = 200.0
    cap_mm3 = math.pi * (d / 2.0) ** 2 * h
    cap_cm3 = cap_mm3 / 1000.0
    outer_mm3 = math.pi * (d / 2.0) ** 2 * (h + wall)
    inner_mm3 = math.pi * ((d - 2.0 * wall) / 2.0) ** 2 * h
    shell_cm3 = (outer_mm3 - inner_mm3) / 1000.0
    mass_g = shell_cm3 * rho
    expand_mm = alpha * d * dT
    return {"capacity_mm3": round(cap_mm3, 2), "capacity_cm3": round(cap_cm3, 2), "shell_volume_cm3": round(shell_cm3, 2), "glass_mass_g": round(mass_g, 2), "thermal_expansion_mm": round(expand_mm, 2), "rim_notches": rests}
def main():
    a = compute(); b = compute()
    sa = hashlib.sha256(repr(sorted(a.items())).encode()).hexdigest()
    sb = hashlib.sha256(repr(sorted(b.items())).encode()).hexdigest()
    for key in ['capacity_mm3', 'capacity_cm3', 'shell_volume_cm3', 'glass_mass_g', 'thermal_expansion_mm', 'rim_notches']:
        print(f"{key}: {a[key]}")
    print(f"Run 1 SHA-256: {sa}")
    print(f"Run 2 SHA-256: {sb}")
    print(f"Deterministic: {'MATCH' if sa == sb else 'MISMATCH'}")
if __name__ == "__main__":
    main()
