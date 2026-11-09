"""Demo: pipe screens — The Pipe Screens (Metal/Glass)."""
import hashlib, math
def compute():
    d = 15.9; wire = 0.25; pitch = 0.8
    area = math.pi * (d / 2.0) ** 2
    open_frac = (1.0 - wire / pitch) ** 2
    open_area = area * open_frac
    holes = int((d / pitch) ** 2)
    daisy_d = 12.0
    daisy_area = math.pi * (daisy_d / 2.0) ** 2
    return {"screen_diameter_mm": d, "screen_area_mm2": round(area, 2), "open_fraction": round(open_frac, 3), "open_area_mm2": round(open_area, 2), "mesh_openings": holes, "daisy_diameter_mm": daisy_d, "daisy_area_mm2": round(daisy_area, 2)}
def main():
    a = compute(); b = compute()
    sa = hashlib.sha256(repr(sorted(a.items())).encode()).hexdigest()
    sb = hashlib.sha256(repr(sorted(b.items())).encode()).hexdigest()
    print(f"screen_diameter_mm: {a['screen_diameter_mm']}")
    print(f"screen_area_mm2: {a['screen_area_mm2']}")
    print(f"open_fraction: {a['open_fraction']}")
    print(f"open_area_mm2: {a['open_area_mm2']}")
    print(f"mesh_openings: {a['mesh_openings']}")
    print(f"daisy_diameter_mm: {a['daisy_diameter_mm']}")
    print(f"daisy_area_mm2: {a['daisy_area_mm2']}")
    print(f"Run 1 SHA-256: {sa}")
    print(f"Run 2 SHA-256: {sb}")
    print(f"Deterministic: {'MATCH' if sa == sb else 'MISMATCH'}")
if __name__ == "__main__":
    main()
