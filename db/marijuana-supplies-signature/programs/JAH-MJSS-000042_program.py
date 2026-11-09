"""Signature Pipe Screens (Metal/Glass) — full working program.

Computes the same quantities as the record demo (pipe screens),
as a documented module with a class and a run() method.
Run: python3 program.py
"""
import hashlib
import math


class SupplyCalculator:
    """Calculator for Signature Pipe Screens (Metal/Glass)."""

    def compute(self):
        """Return the computed quantities as a dict."""
        d = 19.05; wire = 0.3; pitch = 0.9
        area = math.pi * (d / 2.0) ** 2
        open_frac = (1.0 - wire / pitch) ** 2
        open_area = area * open_frac
        holes = int((d / pitch) ** 2)
        daisy_d = 14.0
        daisy_area = math.pi * (daisy_d / 2.0) ** 2
        return {"screen_diameter_mm": d, "screen_area_mm2": round(area, 2), "open_fraction": round(open_frac, 3), "open_area_mm2": round(open_area, 2), "mesh_openings": holes, "daisy_diameter_mm": daisy_d, "daisy_area_mm2": round(daisy_area, 2)}

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
