"""Demo: the Complete Grinder System mix — public Manual Herb Grinder
(JAH-MJS-000001) MIXED with the Signature Helix Grinder (JAH-MJSS-000001).

The mix keeps the public record's four-piece layout with its kief screen
and takes the Signature design's helical tooth ring and larger body size.
Three boundless scales are computed from the same cylinder formula the
two source records use:

    V = pi * (d / 2) ** 2 * h

A1 — Basic (pocket):    40 mm diameter, 14 mm chamber, 24 helical teeth,
                         36 mm screen, 10 turns.
A2 — Improved (standard): 70 mm diameter, 30 mm chamber, 56 helical teeth,
                         62 mm screen, 8 turns.
A3 — Best (workshop):   100 mm diameter, 40 mm chamber, 90 helical teeth,
                         90 mm screen, 6 turns.

The demo also compares the mixed A2 chamber against the two source
records' own chambers (public A2: 87,282.87 mm3; Signature A2:
115,453.53 mm3) and reports the volume gain of the mix over the public
record. Run twice with SHA-256 digests; deterministic.

Source records:
  public    — wave1/data/marijuana-supplies/index.jsonl.gz, JAH-MJS-000001
  signature — wave1/data/marijuana-supplies-signature/index.jsonl.gz,
              JAH-MJSS-000001
Run: python3 grinder_mix_demo.py
"""

import hashlib
import math

# Source-record chambers, from the records' own expected outputs.
PUBLIC_A2_MM3 = 87282.87
SIGNATURE_A2_MM3 = 115453.53

SCALES = {
    "A1": {"d": 40.0, "h": 14.0, "teeth": 24, "screen_d": 36.0, "turns": 10},
    "A2": {"d": 70.0, "h": 30.0, "teeth": 56, "screen_d": 62.0, "turns": 8},
    "A3": {"d": 100.0, "h": 40.0, "teeth": 90, "screen_d": 90.0, "turns": 6},
}


def compute_scale(p):
    r = p["d"] / 2.0
    chamber_mm3 = math.pi * r * r * p["h"]
    chamber_cm3 = chamber_mm3 / 1000.0
    screen_area_mm2 = math.pi * (p["screen_d"] / 2.0) ** 2
    teeth_per_cm2 = p["teeth"] / (math.pi * r * r / 100.0)
    cutting_passes = p["teeth"] * p["turns"]
    return {
        "chamber_volume_mm3": round(chamber_mm3, 2),
        "chamber_volume_cm3": round(chamber_cm3, 2),
        "screen_area_mm2": round(screen_area_mm2, 2),
        "teeth": p["teeth"],
        "turns": p["turns"],
        "teeth_per_cm2": round(teeth_per_cm2, 2),
        "cutting_passes": cutting_passes,
    }


def compute():
    out = {}
    for name, p in SCALES.items():
        out[name] = compute_scale(p)
    a2 = out["A2"]["chamber_volume_mm3"]
    out["mix_gain_over_public_pct"] = round(
        (a2 - PUBLIC_A2_MM3) / PUBLIC_A2_MM3 * 100.0, 2)
    out["mix_vs_signature_pct"] = round(
        (a2 - SIGNATURE_A2_MM3) / SIGNATURE_A2_MM3 * 100.0, 2)
    out["total_cutting_passes_ladder"] = sum(
        out[n]["cutting_passes"] for n in ("A1", "A2", "A3"))
    return out


def main():
    a = compute()
    b = compute()
    sa = hashlib.sha256(repr(sorted(a.items())).encode()).hexdigest()
    sb = hashlib.sha256(repr(sorted(b.items())).encode()).hexdigest()
    for name in ("A1", "A2", "A3"):
        print(f"--- Mixed scale {name} ---")
        for key in ("chamber_volume_mm3", "chamber_volume_cm3",
                    "screen_area_mm2", "teeth", "turns",
                    "teeth_per_cm2", "cutting_passes"):
            print(f"{name} {key}: {a[name][key]}")
    print(f"public_A2_chamber_mm3: {PUBLIC_A2_MM3}")
    print(f"signature_A2_chamber_mm3: {SIGNATURE_A2_MM3}")
    print(f"mix_gain_over_public_pct: {a['mix_gain_over_public_pct']}")
    print(f"mix_vs_signature_pct: {a['mix_vs_signature_pct']}")
    print(f"total_cutting_passes_ladder: {a['total_cutting_passes_ladder']}")
    print(f"Run 1 SHA-256: {sa}")
    print(f"Run 2 SHA-256: {sb}")
    print(f"Deterministic: {'MATCH' if sa == sb else 'MISMATCH'}")


if __name__ == "__main__":
    main()
