"""Demo: rolling paper area — Rolling Papers."""
import hashlib
def compute():
    length = 78.0; width = 44.0; leaves = 32; gsm = 12.0; gum = 4.0
    sheet_mm2 = length * width
    sheet_cm2 = sheet_mm2 / 100.0
    booklet_mm2 = sheet_mm2 * leaves
    booklet_m2 = booklet_mm2 / 1000000.0
    booklet_g = booklet_m2 * gsm
    gum_mm2 = length * gum
    return {"sheet_area_mm2": round(sheet_mm2, 1), "sheet_area_cm2": round(sheet_cm2, 2), "booklet_area_m2": round(booklet_m2, 4), "booklet_mass_g": round(booklet_g, 3), "gum_area_mm2": round(gum_mm2, 1), "leaves": leaves}
def main():
    a = compute(); b = compute()
    sa = hashlib.sha256(repr(sorted(a.items())).encode()).hexdigest()
    sb = hashlib.sha256(repr(sorted(b.items())).encode()).hexdigest()
    for key in ["sheet_area_mm2", "sheet_area_cm2", "booklet_area_m2", "booklet_mass_g", "gum_area_mm2", "leaves"]:
        print(f"{key}: {a[key]}")
    print(f"Run 1 SHA-256: {sa}")
    print(f"Run 2 SHA-256: {sb}")
    print(f"Deterministic: {'MATCH' if sa == sb else 'MISMATCH'}")
if __name__ == "__main__":
    main()
