"""The Manual Herb Grinder — full working program.

Computes the same quantities as the record demo (manual grinder chamber volume),
as a documented module with a class and a run() method.
Run: python3 program.py
"""
import hashlib
import math


class SupplyCalculator:
    """Calculator for The Manual Herb Grinder."""

    def compute(self):
        """Return the computed quantities as a dict."""
        d = 63.0; h = 28.0; teeth = 49; screen_d = 56.0; turns = 12
        r = d / 2.0
        chamber_mm3 = math.pi * r * r * h
        chamber_cm3 = chamber_mm3 / 1000.0
        screen_area_mm2 = math.pi * (screen_d / 2.0) ** 2
        teeth_per_cm2 = teeth / (math.pi * r * r / 100.0)
        return {"chamber_volume_mm3": round(chamber_mm3, 2), "chamber_volume_cm3": round(chamber_cm3, 2), "screen_area_mm2": round(screen_area_mm2, 2), "teeth": teeth, "turns": turns, "teeth_per_cm2": round(teeth_per_cm2, 2)}

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
