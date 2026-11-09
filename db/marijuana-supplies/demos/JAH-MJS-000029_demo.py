"""Demo: gravity bong displaced volume and waterfall drain rate — The Gravity Bong."""
import hashlib, math
def compute():
    vol = 2000.0; d = 105.0; lift = 180.0; hole = 6.0; col = 200.0
    displaced = math.pi * (d / 2.0) ** 2 * lift / 1000.0
    v = math.sqrt(2.0 * 9.81 * (col / 1000.0))
    hole_area = math.pi * (hole / 2.0) ** 2
    flow = hole_area * v * 1000.0 / 1000.0
    drain_time = vol / flow
    return {"chamber_volume_mL": vol, "displaced_volume_mL": round(displaced, 2), "lift_mm": lift, "drain_velocity_m_s": round(v, 2), "drain_flow_mL_per_s": round(flow, 2), "drain_time_s": round(drain_time, 2)}
def main():
    a = compute(); b = compute()
    sa = hashlib.sha256(repr(sorted(a.items())).encode()).hexdigest()
    sb = hashlib.sha256(repr(sorted(b.items())).encode()).hexdigest()
    for key in ["chamber_volume_mL", "displaced_volume_mL", "lift_mm", "drain_velocity_m_s", "drain_flow_mL_per_s", "drain_time_s"]:
        print(f"{key}: {a[key]}")
    print(f"Run 1 SHA-256: {sa}")
    print(f"Run 2 SHA-256: {sb}")
    print(f"Deterministic: {'MATCH' if sa == sb else 'MISMATCH'}")
if __name__ == "__main__":
    main()
