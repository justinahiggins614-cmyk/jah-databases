"""Signature Ember Pocket Vaporizer — full working program.

Computes the same quantities as the record demo (portable vaporizer heating energy),
as a documented module with a class and a run() method.
Run: python3 program.py
"""
import hashlib
import math


class SupplyCalculator:
    """Calculator for Signature Ember Pocket Vaporizer."""

    def compute(self):
        """Return the computed quantities as a dict."""
        herb_g = 0.3; t0 = 20.0; t1 = 185.0; cp = 1.7; battery_wh = 12.0; oven_g = 14.0; oven_cp = 0.9
        q_herb_j = herb_g * cp * (t1 - t0)
        q_oven_j = oven_g * oven_cp * (t1 - t0)
        q_total_j = q_herb_j + q_oven_j
        q_total_wh = q_total_j / 3600.0
        sessions = battery_wh / q_total_wh
        temp_rise_c = t1 - t0
        return {"herb_heat_J": round(q_herb_j, 2), "oven_heat_J": round(q_oven_j, 2), "total_heat_J": round(q_total_j, 2), "total_heat_Wh": round(q_total_wh, 4), "sessions_per_charge": round(sessions, 1), "temp_rise_C": temp_rise_c}

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
