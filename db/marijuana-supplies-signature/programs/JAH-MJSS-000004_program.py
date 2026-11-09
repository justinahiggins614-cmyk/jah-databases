"""Signature Zephyr Desktop Vaporizer — full working program.

Computes the same quantities as the record demo (desktop vaporizer balloon fill),
as a documented module with a class and a run() method.
Run: python3 program.py
"""
import hashlib
import math


class SupplyCalculator:
    """Calculator for Signature Zephyr Desktop Vaporizer."""

    def compute(self):
        """Return the computed quantities as a dict."""
        heater_w = 120.0; heatup_s = 150.0; airflow = 7.0; fill_s = 30.0; balloon_l = 3.5; temp_c = 190.0
        heatup_energy_j = heater_w * heatup_s
        fill_min = fill_s / 60.0
        filled_l = airflow * fill_min
        fill_fraction = filled_l / balloon_l
        fills_per_hour = 3600.0 / fill_s
        return {"heatup_energy_J": round(heatup_energy_j, 1), "heatup_energy_Wh": round(heatup_energy_j / 3600.0, 2), "filled_volume_L": round(filled_l, 2), "balloon_volume_L": balloon_l, "fill_fraction": round(fill_fraction, 2), "target_temp_C": temp_c}

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
