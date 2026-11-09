"""The Inline Duct Fan — full working program.

Computes the same quantities as the record demo (inline duct fan),
as a documented module with a class and a run() method.
Run: python3 program.py
"""
import hashlib
import math


class SupplyCalculator:
    """Calculator for The Inline Duct Fan."""

    def compute(self):
        """Return the computed quantities as a dict."""
        d_in = 6.0; cfm = 402.0; power_w = 40.0; tent_ft3 = 104.0
        d_m = d_in * 0.0254
        duct_area = math.pi * (d_m / 2.0) ** 2
        flow_m3s = cfm * 0.000471947
        velocity = flow_m3s / duct_area
        exchanges = cfm / tent_ft3
        energy_day = power_w * 24.0 / 1000.0
        return {"duct_diameter_in": d_in, "duct_area_m2": round(duct_area, 5), "airflow_cfm": cfm, "velocity_ms": round(velocity, 2), "exchanges_per_min": round(exchanges, 2), "power_w": power_w, "energy_kwh_per_day": round(energy_day, 2)}

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
