"""Demo: fabric grow pot — Signature Fabric Grow Pot."""
import hashlib, math
def compute():
    d_cm = 33.0; h_cm = 30.0; density = 0.45
    vol_cm3 = math.pi * (d_cm / 2.0) ** 2 * h_cm
    vol_L = vol_cm3 / 1000.0
    vol_gal = vol_L / 3.78541
    side_area = math.pi * d_cm * h_cm
    bottom_area = math.pi * (d_cm / 2.0) ** 2
    total_area = side_area + bottom_area
    mass_kg = vol_cm3 * density / 1000.0
    return {"diameter_cm": d_cm, "height_cm": h_cm, "volume_L": round(vol_L, 2), "volume_gal": round(vol_gal, 2), "fabric_area_cm2": round(total_area, 1), "mix_mass_kg": round(mass_kg, 2)}
def main():
    a = compute(); b = compute()
    sa = hashlib.sha256(repr(sorted(a.items())).encode()).hexdigest()
    sb = hashlib.sha256(repr(sorted(b.items())).encode()).hexdigest()
    print(f"diameter_cm: {a['diameter_cm']}")
    print(f"height_cm: {a['height_cm']}")
    print(f"volume_L: {a['volume_L']}")
    print(f"volume_gal: {a['volume_gal']}")
    print(f"fabric_area_cm2: {a['fabric_area_cm2']}")
    print(f"mix_mass_kg: {a['mix_mass_kg']}")
    print(f"Run 1 SHA-256: {sa}")
    print(f"Run 2 SHA-256: {sb}")
    print(f"Deterministic: {'MATCH' if sa == sb else 'MISMATCH'}")
if __name__ == "__main__":
    main()
