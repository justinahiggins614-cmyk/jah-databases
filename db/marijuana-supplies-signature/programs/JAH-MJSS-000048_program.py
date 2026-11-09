"""Signature Drying Rack — full working program.

Computes the same quantities as the record demo (drying rack),
as a documented module with a class and a run() method.
Run: python3 program.py
"""
import hashlib
import math


class SupplyCalculator:
    """Calculator for Signature Drying Rack."""

    def compute(self):
        """Return the computed quantities as a dict."""
        tiers = 8; d_mm = 600.0; chamber_h = 170.0; length_mm = 1700.0; capacity_kg = 4.0
        tier_area = math.pi * (d_mm / 2.0) ** 2 / 1000000.0
        total_area = tier_area * tiers
        tier_vol = tier_area * (chamber_h / 1000.0) * 1000.0
        total_vol = tier_vol * tiers
        per_tier_kg = capacity_kg / tiers
        return {"tiers": tiers, "diameter_mm": d_mm, "chamber_height_mm": chamber_h, "hanging_length_mm": length_mm, "tier_area_m2": round(tier_area, 4), "total_area_m2": round(total_area, 3), "tier_volume_L": round(tier_vol, 1), "total_volume_L": round(total_vol, 1), "capacity_kg": capacity_kg, "per_tier_kg": round(per_tier_kg, 2)}

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
