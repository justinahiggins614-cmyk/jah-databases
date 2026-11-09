"""Demo: mini bong — The Mini Bong."""
import hashlib, math
def compute():
    height_mm = 152.4; tube_d = 25.0; base_d = 82.0; base_h = 50.0; water_depth = 31.75
    water_vol = math.pi * (base_d / 2.0) ** 2 * water_depth / 1000.0
    base_vol = math.pi * (base_d / 2.0) ** 2 * base_h / 1000.0
    tube_h = height_mm - base_h
    tube_vol = math.pi * (tube_d / 2.0) ** 2 * tube_h / 1000.0
    chamber_vol = base_vol + tube_vol
    water_frac = water_vol / chamber_vol
    return {"height_mm": height_mm, "water_depth_mm": water_depth, "water_volume_ml": round(water_vol, 1), "base_volume_ml": round(base_vol, 1), "tube_volume_ml": round(tube_vol, 1), "chamber_volume_ml": round(chamber_vol, 1), "water_fraction": round(water_frac, 3)}
def main():
    a = compute(); b = compute()
    sa = hashlib.sha256(repr(sorted(a.items())).encode()).hexdigest()
    sb = hashlib.sha256(repr(sorted(b.items())).encode()).hexdigest()
    print(f"height_mm: {a['height_mm']}")
    print(f"water_depth_mm: {a['water_depth_mm']}")
    print(f"water_volume_ml: {a['water_volume_ml']}")
    print(f"base_volume_ml: {a['base_volume_ml']}")
    print(f"tube_volume_ml: {a['tube_volume_ml']}")
    print(f"chamber_volume_ml: {a['chamber_volume_ml']}")
    print(f"water_fraction: {a['water_fraction']}")
    print(f"Run 1 SHA-256: {sa}")
    print(f"Run 2 SHA-256: {sb}")
    print(f"Deterministic: {'MATCH' if sa == sb else 'MISMATCH'}")
if __name__ == "__main__":
    main()
