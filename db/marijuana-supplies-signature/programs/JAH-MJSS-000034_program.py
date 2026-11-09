"""Signature Ash-Catcher Bowl — full working program.

Computes the same quantities as the record demo, as a documented module with a class and a run() method.
Run: python3 program.py
"""
import hashlib
import math


class SupplyCalculator:
    """Calculator for Signature Ash-Catcher Bowl."""

    def compute(self):
        """Return the computed quantities as a dict."""
        bowl_d = 22.0; bowl_h = 18.0; ch_d = 34.0; water_h = 25.0; fill = 0.60; pack = 0.15; joint = 18.0
        bowl_mm3 = math.pi * (bowl_d / 2.0) ** 2 * bowl_h
        bowl_cm3 = bowl_mm3 / 1000.0
        capacity_g = bowl_cm3 * pack
        ch_mm3 = math.pi * (ch_d / 2.0) ** 2 * water_h
        ch_cm3 = ch_mm3 / 1000.0
        water_ml = ch_cm3 * fill
        trap_mm2 = math.pi * (ch_d / 2.0) ** 2
        return {"bowl_volume_mm3": round(bowl_mm3, 2), "bowl_volume_cm3": round(bowl_cm3, 2), "herb_capacity_g": round(capacity_g, 2), "chamber_volume_cm3": round(ch_cm3, 2), "water_ml": round(water_ml, 2), "water_mass_g": round(water_ml, 2), "trap_area_mm2": round(trap_mm2, 2), "joint_mm": joint}

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
