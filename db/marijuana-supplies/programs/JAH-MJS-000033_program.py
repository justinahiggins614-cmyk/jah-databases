"""The Ceramic Bowl — full working program.

Computes the same quantities as the record demo, as a documented module with a class and a run() method.
Run: python3 program.py
"""
import hashlib
import math


class SupplyCalculator:
    """Calculator for The Ceramic Bowl."""

    def compute(self):
        """Return the computed quantities as a dict."""
        d = 22.0; h = 16.0; wall = 3.0; joint = 14.0; rho = 2.4; cp = 0.85; dT = 200.0; pack = 0.15
        bowl_mm3 = math.pi * (d / 2.0) ** 2 * h
        bowl_cm3 = bowl_mm3 / 1000.0
        capacity_g = bowl_cm3 * pack
        outer_d = d + 2.0 * wall; outer_h = h + wall
        shell_mm3 = math.pi * (outer_d / 2.0) ** 2 * outer_h - bowl_mm3
        shell_cm3 = shell_mm3 / 1000.0
        mass_g = shell_cm3 * rho
        heat_J = mass_g * cp * dT
        return {"bowl_volume_mm3": round(bowl_mm3, 2), "bowl_volume_cm3": round(bowl_cm3, 2), "herb_capacity_g": round(capacity_g, 2), "shell_volume_cm3": round(shell_cm3, 2), "ceramic_mass_g": round(mass_g, 2), "heat_to_200C_J": round(heat_J, 2), "joint_mm": joint}

    def run(self):
        """Compute twice, print named results and SHA-256 digests."""
        a = self.compute()
        b = self.compute()
        sa = hashlib.sha256(repr(sorted(a.items())).encode()).hexdigest()
        sb = hashlib.sha256(repr(sorted(b.items())).encode()).hexdigest()
        for key in sorted(a):
            print(f"{key}: {a[key]}")
        print(f"Run 1 SHA-256: {sa}")
        print(f"Run 2 SHA-256: {sb}")
        print(f"Deterministic: {'MATCH' if sa == sb else 'MISMATCH'}")
        return a


if __name__ == "__main__":
    SupplyCalculator().run()
