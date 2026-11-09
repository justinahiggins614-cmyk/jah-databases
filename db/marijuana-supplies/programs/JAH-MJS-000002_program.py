"""The Electric Herb Grinder — full working program.

Computes the same quantities as the record demo (electric grinder battery energy),
as a documented module with a class and a run() method.
Run: python3 program.py
"""
import hashlib
import math


class SupplyCalculator:
    """Calculator for The Electric Herb Grinder."""

    def compute(self):
        """Return the computed quantities as a dict."""
        v = 3.7; cap_mah = 2000.0; motor_w = 5.0; grind_s = 6.0; load_g = 3.0
        battery_wh = v * (cap_mah / 1000.0)
        energy_per_grind_wh = motor_w * grind_s / 3600.0
        energy_per_grind_j = motor_w * grind_s
        grinds_per_charge = battery_wh / energy_per_grind_wh
        current_a = motor_w / v
        return {"battery_wh": round(battery_wh, 3), "energy_per_grind_Wh": round(energy_per_grind_wh, 5), "energy_per_grind_J": round(energy_per_grind_j, 2), "grinds_per_charge": round(grinds_per_charge, 1), "motor_current_A": round(current_a, 2), "load_g": load_g}

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
