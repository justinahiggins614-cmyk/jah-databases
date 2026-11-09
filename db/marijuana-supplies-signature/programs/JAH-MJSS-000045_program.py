"""Signature Fabric Grow Pot — full working program.

Computes the same quantities as the record demo (fabric grow pot),
as a documented module with a class and a run() method.
Run: python3 program.py
"""
import hashlib
import math


class SupplyCalculator:
    """Calculator for Signature Fabric Grow Pot."""

    def compute(self):
        """Return the computed quantities as a dict."""
        d_cm = 33.0; h_cm = 30.0; density = 0.45
        vol_cm3 = math.pi * (d_cm / 2.0) ** 2 * h_cm
        vol_L = vol_cm3 / 1000.0
        vol_gal = vol_L / 3.78541
        side_area = math.pi * d_cm * h_cm
        bottom_area = math.pi * (d_cm / 2.0) ** 2
        total_area = side_area + bottom_area
        mass_kg = vol_cm3 * density / 1000.0
        return {"diameter_cm": d_cm, "height_cm": h_cm, "volume_L": round(vol_L, 2), "volume_gal": round(vol_gal, 2), "fabric_area_cm2": round(total_area, 1), "mix_mass_kg": round(mass_kg, 2)}

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
