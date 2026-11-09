"""Demo: recycler bong loop volumes and cycle time — The Recycler Bong."""
import hashlib, math
def compute():
    main_mL = 120.0; sec_mL = 60.0; up_d = 10.0; dr_d = 8.0; up_len = 180.0; dr_len = 150.0; draw = 1.2
    up_area = math.pi * (up_d / 2.0) ** 2
    dr_area = math.pi * (dr_d / 2.0) ** 2
    loop_mL = main_mL + sec_mL
    flow_mL_s = draw * 1000.0 / 60.0
    loop_time = loop_mL / flow_mL_s
    up_vol = up_area * up_len / 1000.0
    return {"main_water_mL": main_mL, "secondary_water_mL": sec_mL, "loop_water_mL": round(loop_mL, 2), "uptake_area_mm2": round(up_area, 2), "drain_area_mm2": round(dr_area, 2), "loop_time_s": round(loop_time, 2), "uptake_volume_mL": round(up_vol, 2)}
def main():
    a = compute(); b = compute()
    sa = hashlib.sha256(repr(sorted(a.items())).encode()).hexdigest()
    sb = hashlib.sha256(repr(sorted(b.items())).encode()).hexdigest()
    for key in ["main_water_mL", "secondary_water_mL", "loop_water_mL", "uptake_area_mm2", "drain_area_mm2", "loop_time_s", "uptake_volume_mL"]:
        print(f"{key}: {a[key]}")
    print(f"Run 1 SHA-256: {sa}")
    print(f"Run 2 SHA-256: {sb}")
    print(f"Deterministic: {'MATCH' if sa == sb else 'MISMATCH'}")
if __name__ == "__main__":
    main()
