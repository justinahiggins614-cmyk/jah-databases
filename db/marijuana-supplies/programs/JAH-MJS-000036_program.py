"""The Glass Ashtray — full working program.

Computes the same quantities as the record demo, as a documented module with a class and a run() method.
Run: python3 program.py
"""
import hashlib
import math


class SupplyCalculator:
    """Calculator for The Glass Ashtray."""

    def compute(self):
        """Return the computed quantities as a dict."""
        d = 110.0; h = 25.0; wall = 4.0; rests = 3; rho = 2.23; alpha = 3.3e-06; dT = 200.0
        cap_mm3 = math.pi * (d / 2.0) ** 2 * h
        cap_cm3 = cap_mm3 / 1000.0
        outer_mm3 = math.pi * (d / 2.0) ** 2 * (h + wall)
        inner_mm3 = math.pi * ((d - 2.0 * wall) / 2.0) ** 2 * h
        shell_cm3 = (outer_mm3 - inner_mm3) / 1000.0
        mass_g = shell_cm3 * rho
        expand_mm = alpha * d * dT
        return {"capacity_mm3": round(cap_mm3, 2), "capacity_cm3": round(cap_cm3, 2), "shell_volume_cm3": round(shell_cm3, 2), "glass_mass_g": round(mass_g, 2), "thermal_expansion_mm": round(expand_mm, 2), "rim_notches": rests}

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
