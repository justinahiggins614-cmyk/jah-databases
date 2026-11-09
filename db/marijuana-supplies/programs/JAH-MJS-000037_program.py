"""The Ceramic Ashtray — full working program.

Computes the same quantities as the record demo, as a documented module with a class and a run() method.
Run: python3 program.py
"""
import hashlib
import math


class SupplyCalculator:
    """Calculator for The Ceramic Ashtray."""

    def compute(self):
        """Return the computed quantities as a dict."""
        L = 120.0; W = 120.0; H = 35.0; inner = 108.0; depth = 25.0; rests = 4; rho = 2.4; cp = 0.85; dT = 200.0
        outer_mm3 = L * W * H
        cap_mm3 = inner * inner * depth
        cap_cm3 = cap_mm3 / 1000.0
        shell_mm3 = outer_mm3 - cap_mm3
        shell_cm3 = shell_mm3 / 1000.0
        mass_g = shell_cm3 * rho
        heat_J = mass_g * cp * dT
        return {"outer_volume_mm3": round(outer_mm3, 2), "capacity_mm3": round(cap_mm3, 2), "capacity_cm3": round(cap_cm3, 2), "shell_volume_cm3": round(shell_cm3, 2), "ceramic_mass_g": round(mass_g, 2), "heat_to_200C_J": round(heat_J, 2), "rim_notches": rests}

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
