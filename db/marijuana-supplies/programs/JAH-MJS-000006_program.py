"""The Water Pipe (Bong) — full working program.

Computes the same quantities as the record demo (water pipe water and chamber volumes),
as a documented module with a class and a run() method.
Run: python3 program.py
"""
import hashlib
import math


class SupplyCalculator:
    """Calculator for The Water Pipe (Bong)."""

    def compute(self):
        """Return the computed quantities as a dict."""
        tube_d = 50.0; height = 300.0; water_h = 50.0; down_d = 12.0; bubble_d = 4.0
        area_mm2 = math.pi * (tube_d / 2.0) ** 2
        water_mm3 = area_mm2 * water_h
        chamber_h = height - water_h
        chamber_mm3 = area_mm2 * chamber_h
        bubble_r = bubble_d / 2.0
        bubble_vol_mm3 = (4.0 / 3.0) * math.pi * bubble_r ** 3
        bubble_area_mm2 = 4.0 * math.pi * bubble_r ** 2
        pressure_pa = 1000.0 * 9.81 * (water_h / 1000.0)
        return {"water_volume_mm3": round(water_mm3, 1), "water_volume_mL": round(water_mm3 / 1000.0, 1), "chamber_volume_mL": round(chamber_mm3 / 1000.0, 1), "bubble_volume_mm3": round(bubble_vol_mm3, 2), "bubble_surface_mm2": round(bubble_area_mm2, 2), "draw_pressure_Pa": round(pressure_pa, 1)}

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
