"""Demo: glass spoon pipe volumes — The Glass Spoon Pipe."""
import hashlib, math
def compute():
    length = 100.0; bowl_d = 20.0; bowl_h = 18.0; stem_d = 6.0; stem_l = 70.0
    bowl_mm3 = math.pi * (bowl_d / 2.0) ** 2 * bowl_h
    stem_mm3 = math.pi * (stem_d / 2.0) ** 2 * stem_l
    total_mm3 = bowl_mm3 + stem_mm3
    return {"bowl_volume_mm3": round(bowl_mm3, 2), "bowl_volume_cm3": round(bowl_mm3 / 1000.0, 2), "stem_volume_mm3": round(stem_mm3, 2), "stem_volume_cm3": round(stem_mm3 / 1000.0, 2), "total_volume_mm3": round(total_mm3, 2), "total_volume_cm3": round(total_mm3 / 1000.0, 2), "pipe_length_mm": length}
def main():
    a = compute(); b = compute()
    sa = hashlib.sha256(repr(sorted(a.items())).encode()).hexdigest()
    sb = hashlib.sha256(repr(sorted(b.items())).encode()).hexdigest()
    for key in ["bowl_volume_mm3", "bowl_volume_cm3", "stem_volume_mm3", "stem_volume_cm3", "total_volume_mm3", "total_volume_cm3", "pipe_length_mm"]:
        print(f"{key}: {a[key]}")
    print(f"Run 1 SHA-256: {sa}")
    print(f"Run 2 SHA-256: {sb}")
    print(f"Deterministic: {'MATCH' if sa == sb else 'MISMATCH'}")
if __name__ == "__main__":
    main()
