"""The Silicone Ashtray with Lid — full working program.

Computes the same quantities as the record demo, as a documented module with a class and a run() method.
Run: python3 program.py
"""
import hashlib
import math


class SupplyCalculator:
    """Calculator for The Silicone Ashtray with Lid."""

    def compute(self):
        """Return the computed quantities as a dict."""
        d = 100.0; h = 28.0; wall = 4.0; lid_d = 104.0; lid_t = 5.0; rho = 1.15; cp = 1.46; dT = 200.0
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
