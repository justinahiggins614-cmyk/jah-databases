"""Demo: manual grinder chamber volume — The Manual Herb Grinder."""
import hashlib, math
def compute():
    d = 70.0; h = 30.0; teeth = 56; screen_d = 62.0; turns = 8
    r = d / 2.0
    chamber_mm3 = math.pi * r * r * h
    chamber_cm3 = chamber_mm3 / 1000.0
    screen_area_mm2 = math.pi * (screen_d / 2.0) ** 2
    teeth_per_cm2 = teeth / (math.pi * r * r / 100.0)
    return {"chamber_volume_mm3": round(chamber_mm3, 2), "chamber_volume_cm3": round(chamber_cm3, 2), "screen_area_mm2": round(screen_area_mm2, 2), "teeth": teeth, "turns": turns, "teeth_per_cm2": round(teeth_per_cm2, 2)}
def main():
    a = compute(); b = compute()
    sa = hashlib.sha256(repr(sorted(a.items())).encode()).hexdigest()
    sb = hashlib.sha256(repr(sorted(b.items())).encode()).hexdigest()
    for key in ["chamber_volume_mm3", "chamber_volume_cm3", "screen_area_mm2", "teeth", "turns", "teeth_per_cm2"]:
        print(f"{key}: {a[key]}")
    print(f"Run 1 SHA-256: {sa}")
    print(f"Run 2 SHA-256: {sb}")
    print(f"Deterministic: {'MATCH' if sa == sb else 'MISMATCH'}")
if __name__ == "__main__":
    main()
