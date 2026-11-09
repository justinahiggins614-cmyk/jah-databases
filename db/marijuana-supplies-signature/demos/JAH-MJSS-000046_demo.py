"""Demo: inline duct fan — Signature Inline Duct Fan."""
import hashlib, math
def compute():
    d_in = 8.0; cfm = 807.0; power_w = 60.0; tent_ft3 = 162.5
    d_m = d_in * 0.0254
    duct_area = math.pi * (d_m / 2.0) ** 2
    flow_m3s = cfm * 0.000471947
    velocity = flow_m3s / duct_area
    exchanges = cfm / tent_ft3
    energy_day = power_w * 24.0 / 1000.0
    return {"duct_diameter_in": d_in, "duct_area_m2": round(duct_area, 5), "airflow_cfm": cfm, "velocity_ms": round(velocity, 2), "exchanges_per_min": round(exchanges, 2), "power_w": power_w, "energy_kwh_per_day": round(energy_day, 2)}
def main():
    a = compute(); b = compute()
    sa = hashlib.sha256(repr(sorted(a.items())).encode()).hexdigest()
    sb = hashlib.sha256(repr(sorted(b.items())).encode()).hexdigest()
    print(f"duct_diameter_in: {a['duct_diameter_in']}")
    print(f"duct_area_m2: {a['duct_area_m2']}")
    print(f"airflow_cfm: {a['airflow_cfm']}")
    print(f"velocity_ms: {a['velocity_ms']}")
    print(f"exchanges_per_min: {a['exchanges_per_min']}")
    print(f"power_w: {a['power_w']}")
    print(f"energy_kwh_per_day: {a['energy_kwh_per_day']}")
    print(f"Run 1 SHA-256: {sa}")
    print(f"Run 2 SHA-256: {sb}")
    print(f"Deterministic: {'MATCH' if sa == sb else 'MISMATCH'}")
if __name__ == "__main__":
    main()
