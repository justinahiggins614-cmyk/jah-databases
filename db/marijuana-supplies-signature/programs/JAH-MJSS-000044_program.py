"""Signature Grow Tent — full working program.

Computes the same quantities as the record demo (grow tent),
as a documented module with a class and a run() method.
Run: python3 program.py
"""
import hashlib
import math


class SupplyCalculator:
    """Calculator for Signature Grow Tent."""

    def compute(self):
        """Return the computed quantities as a dict."""
        l_ft = 5.0; w_ft = 5.0; h_ft = 6.5
        volume_ft3 = l_ft * w_ft * h_ft
        floor_ft2 = l_ft * w_ft
        fabric_ft2 = 2 * (l_ft * h_ft + w_ft * h_ft) + 2 * floor_ft2
        fan_cfm = 600.0
        exchanges = fan_cfm / volume_ft3
        seconds_per_exchange = 60.0 / exchanges
        return {"tent_ft": "5 x 5 x 6.5", "volume_ft3": round(volume_ft3, 1), "floor_ft2": round(floor_ft2, 1), "fabric_ft2": round(fabric_ft2, 1), "fan_cfm": fan_cfm, "exchanges_per_min": round(exchanges, 2), "seconds_per_exchange": round(seconds_per_exchange, 1)}

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
