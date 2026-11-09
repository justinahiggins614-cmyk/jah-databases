"""Signature Carbon Filter — full working program.

Computes the same quantities as the record demo (carbon filter),
as a documented module with a class and a run() method.
Run: python3 program.py
"""
import hashlib
import math


class SupplyCalculator:
    """Calculator for Signature Carbon Filter."""

    def compute(self):
        """Return the computed quantities as a dict."""
        outer_d = 150.0; length = 400.0; bed_mm = 38.0; cfm = 402.0; months = 6.0
        outer_r = outer_d / 2.0; inner_r = outer_r - bed_mm
        carbon_vol = math.pi * (outer_r ** 2 - inner_r ** 2) * length / 1000000.0
        outer_area = math.pi * outer_d * length / 1000000.0
        flow_m3s = cfm * 0.000471947
        face_vel = flow_m3s / outer_area
        hours = months * 30.0 * 24.0
        return {"outer_diameter_mm": outer_d, "length_mm": length, "bed_mm": bed_mm, "carbon_volume_L": round(carbon_vol, 2), "outer_area_m2": round(outer_area, 4), "face_velocity_ms": round(face_vel, 2), "lifespan_months": months, "lifespan_hours": round(hours, 0)}

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
