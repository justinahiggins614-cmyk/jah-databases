"""Demo: carbon filter — The Carbon Filter."""
import hashlib, math
def compute():
    outer_d = 100.0; length = 300.0; bed_mm = 38.0; cfm = 205.0; months = 4.5
    outer_r = outer_d / 2.0; inner_r = outer_r - bed_mm
    carbon_vol = math.pi * (outer_r ** 2 - inner_r ** 2) * length / 1000000.0
    outer_area = math.pi * outer_d * length / 1000000.0
    flow_m3s = cfm * 0.000471947
    face_vel = flow_m3s / outer_area
    hours = months * 30.0 * 24.0
    return {"outer_diameter_mm": outer_d, "length_mm": length, "bed_mm": bed_mm, "carbon_volume_L": round(carbon_vol, 2), "outer_area_m2": round(outer_area, 4), "face_velocity_ms": round(face_vel, 2), "lifespan_months": months, "lifespan_hours": round(hours, 0)}
def main():
    a = compute(); b = compute()
    sa = hashlib.sha256(repr(sorted(a.items())).encode()).hexdigest()
    sb = hashlib.sha256(repr(sorted(b.items())).encode()).hexdigest()
    print(f"outer_diameter_mm: {a['outer_diameter_mm']}")
    print(f"length_mm: {a['length_mm']}")
    print(f"bed_mm: {a['bed_mm']}")
    print(f"carbon_volume_L: {a['carbon_volume_L']}")
    print(f"outer_area_m2: {a['outer_area_m2']}")
    print(f"face_velocity_ms: {a['face_velocity_ms']}")
    print(f"lifespan_months: {a['lifespan_months']}")
    print(f"lifespan_hours: {a['lifespan_hours']}")
    print(f"Run 1 SHA-256: {sa}")
    print(f"Run 2 SHA-256: {sb}")
    print(f"Deterministic: {'MATCH' if sa == sb else 'MISMATCH'}")
if __name__ == "__main__":
    main()
