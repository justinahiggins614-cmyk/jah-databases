"""Demo: drying rack — Signature Drying Rack."""
import hashlib, math
def compute():
    tiers = 8; d_mm = 600.0; chamber_h = 170.0; length_mm = 1700.0; capacity_kg = 4.0
    tier_area = math.pi * (d_mm / 2.0) ** 2 / 1000000.0
    total_area = tier_area * tiers
    tier_vol = tier_area * (chamber_h / 1000.0) * 1000.0
    total_vol = tier_vol * tiers
    per_tier_kg = capacity_kg / tiers
    return {"tiers": tiers, "diameter_mm": d_mm, "chamber_height_mm": chamber_h, "hanging_length_mm": length_mm, "tier_area_m2": round(tier_area, 4), "total_area_m2": round(total_area, 3), "tier_volume_L": round(tier_vol, 1), "total_volume_L": round(total_vol, 1), "capacity_kg": capacity_kg, "per_tier_kg": round(per_tier_kg, 2)}
def main():
    a = compute(); b = compute()
    sa = hashlib.sha256(repr(sorted(a.items())).encode()).hexdigest()
    sb = hashlib.sha256(repr(sorted(b.items())).encode()).hexdigest()
    print(f"tiers: {a['tiers']}")
    print(f"diameter_mm: {a['diameter_mm']}")
    print(f"chamber_height_mm: {a['chamber_height_mm']}")
    print(f"hanging_length_mm: {a['hanging_length_mm']}")
    print(f"tier_area_m2: {a['tier_area_m2']}")
    print(f"total_area_m2: {a['total_area_m2']}")
    print(f"tier_volume_L: {a['tier_volume_L']}")
    print(f"total_volume_L: {a['total_volume_L']}")
    print(f"capacity_kg: {a['capacity_kg']}")
    print(f"per_tier_kg: {a['per_tier_kg']}")
    print(f"Run 1 SHA-256: {sa}")
    print(f"Run 2 SHA-256: {sb}")
    print(f"Deterministic: {'MATCH' if sa == sb else 'MISMATCH'}")
if __name__ == "__main__":
    main()
