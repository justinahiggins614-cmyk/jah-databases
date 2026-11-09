"""Signature Mini Bong — full working program.

Computes the same quantities as the record demo (mini bong),
as a documented module with a class and a run() method.
Run: python3 program.py
"""
import hashlib
import math


class SupplyCalculator:
    """Calculator for Signature Mini Bong."""

    def compute(self):
        """Return the computed quantities as a dict."""
        height_mm = 177.8; tube_d = 28.0; base_d = 90.0; base_h = 55.0; water_depth = 35.0
        water_vol = math.pi * (base_d / 2.0) ** 2 * water_depth / 1000.0
        base_vol = math.pi * (base_d / 2.0) ** 2 * base_h / 1000.0
        tube_h = height_mm - base_h
        tube_vol = math.pi * (tube_d / 2.0) ** 2 * tube_h / 1000.0
        chamber_vol = base_vol + tube_vol
        water_frac = water_vol / chamber_vol
        return {"height_mm": height_mm, "water_depth_mm": water_depth, "water_volume_ml": round(water_vol, 1), "base_volume_ml": round(base_vol, 1), "tube_volume_ml": round(tube_vol, 1), "chamber_volume_ml": round(chamber_vol, 1), "water_fraction": round(water_frac, 3)}

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
