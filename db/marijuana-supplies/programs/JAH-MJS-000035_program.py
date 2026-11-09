"""The Carb Cap — full working program.

Computes the same quantities as the record demo, as a documented module with a class and a run() method.
Run: python3 program.py
"""
import hashlib
import math


class SupplyCalculator:
    """Calculator for The Carb Cap."""

    def compute(self):
        """Return the computed quantities as a dict."""
        cap_d = 30.0; wall = 2.0; inlet_d = 2.0; banger_d = 25.0; rho = 2.23; cp = 0.83; dT = 175.0
        r = cap_d / 2.0; ri = r - wall
        dome_mm3 = (2.0 / 3.0) * math.pi * r ** 3
        shell_mm3 = (2.0 / 3.0) * math.pi * (r ** 3 - ri ** 3)
        shell_cm3 = shell_mm3 / 1000.0
        mass_g = shell_cm3 * rho
        heat_J = mass_g * cp * dT
        inlet_mm2 = math.pi * (inlet_d / 2.0) ** 2
        mouth_mm2 = math.pi * (banger_d / 2.0) ** 2
        ratio_pct = 100.0 * inlet_mm2 / mouth_mm2
        return {"dome_volume_mm3": round(dome_mm3, 2), "shell_volume_cm3": round(shell_cm3, 2), "cap_mass_g": round(mass_g, 2), "heat_to_175C_J": round(heat_J, 2), "inlet_area_mm2": round(inlet_mm2, 2), "banger_mouth_mm2": round(mouth_mm2, 2), "inlet_ratio_pct": round(ratio_pct, 2), "banger_mm": banger_d}

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
