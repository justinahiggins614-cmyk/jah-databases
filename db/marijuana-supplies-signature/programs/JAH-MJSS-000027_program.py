"""Signature Grove Tree Perc — full working program.

Computes the same quantities as the record demo (tree percolator slit area and chamber volumes),
as a documented module with a class and a run() method.
Run: python3 program.py
"""
import hashlib
import math


class SupplyCalculator:
    """Calculator for Signature Grove Tree Perc."""

    def compute(self):
        """Return the computed quantities as a dict."""
        arms = 12; slits = 8; w = 1.2; l = 9.0; d = 65.0; h = 400.0; water_h = 55.0
        slit_area = w * l
        total_slit = arms * slits * slit_area
        streams = arms * slits
        area = math.pi * (d / 2.0) ** 2
        water_mm3 = area * water_h
        chamber_mm3 = area * h
        return {"arms": arms, "slits_per_arm": slits, "slit_area_mm2": round(slit_area, 2), "total_slit_area_mm2": round(total_slit, 2), "bubble_streams": streams, "water_volume_mL": round(water_mm3 / 1000.0, 2), "chamber_volume_mL": round(chamber_mm3 / 1000.0, 2)}

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
