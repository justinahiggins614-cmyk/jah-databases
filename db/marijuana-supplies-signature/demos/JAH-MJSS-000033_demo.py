"""Demo: ceramic bowl volume and heat storage — Signature Ceramic Bowl."""
import hashlib, math
def compute():
    d = 24.0; h = 18.0; wall = 3.5; joint = 18.0; rho = 2.4; cp = 0.85; dT = 200.0; pack = 0.15
    bowl_mm3 = math.pi * (d / 2.0) ** 2 * h
    bowl_cm3 = bowl_mm3 / 1000.0
    capacity_g = bowl_cm3 * pack
    outer_d = d + 2.0 * wall; outer_h = h + wall
    shell_mm3 = math.pi * (outer_d / 2.0) ** 2 * outer_h - bowl_mm3
    shell_cm3 = shell_mm3 / 1000.0
    mass_g = shell_cm3 * rho
    heat_J = mass_g * cp * dT
    return {"bowl_volume_mm3": round(bowl_mm3, 2), "bowl_volume_cm3": round(bowl_cm3, 2), "herb_capacity_g": round(capacity_g, 2), "shell_volume_cm3": round(shell_cm3, 2), "ceramic_mass_g": round(mass_g, 2), "heat_to_200C_J": round(heat_J, 2), "joint_mm": joint}
def main():
    a = compute(); b = compute()
    sa = hashlib.sha256(repr(sorted(a.items())).encode()).hexdigest()
    sb = hashlib.sha256(repr(sorted(b.items())).encode()).hexdigest()
    for key in ['bowl_volume_mm3', 'bowl_volume_cm3', 'herb_capacity_g', 'shell_volume_cm3', 'ceramic_mass_g', 'heat_to_200C_J', 'joint_mm']:
        print(f"{key}: {a[key]}")
    print(f"Run 1 SHA-256: {sa}")
    print(f"Run 2 SHA-256: {sb}")
    print(f"Deterministic: {'MATCH' if sa == sb else 'MISMATCH'}")
if __name__ == "__main__":
    main()
