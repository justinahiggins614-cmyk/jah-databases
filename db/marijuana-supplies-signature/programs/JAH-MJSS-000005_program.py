"""Signature Comet Spoon Pipe — full working program.

Computes the same quantities as the record demo (glass spoon pipe volumes),
as a documented module with a class and a run() method.
Run: python3 program.py
"""
import hashlib
import math


class SupplyCalculator:
    """Calculator for Signature Comet Spoon Pipe."""

    def compute(self):
        """Return the computed quantities as a dict."""
        length = 110.0; bowl_d = 22.0; bowl_h = 20.0; stem_d = 7.0; stem_l = 80.0
        bowl_mm3 = math.pi * (bowl_d / 2.0) ** 2 * bowl_h
        stem_mm3 = math.pi * (stem_d / 2.0) ** 2 * stem_l
        total_mm3 = bowl_mm3 + stem_mm3
        return {"bowl_volume_mm3": round(bowl_mm3, 2), "bowl_volume_cm3": round(bowl_mm3 / 1000.0, 2), "stem_volume_mm3": round(stem_mm3, 2), "stem_volume_cm3": round(stem_mm3 / 1000.0, 2), "total_volume_mm3": round(total_mm3, 2), "total_volume_cm3": round(total_mm3 / 1000.0, 2), "pipe_length_mm": length}

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
