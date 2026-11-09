"""Numeric check — Projectile motion scenario #11 (JAH-SIM-0000016).
Made for this page from the record's own numbers.
This program checks the arithmetic of the stored figures; its outputs
are check-sums, not physical quantities."""
import hashlib
def compute():
    run_spec_steps = 1; parameters_v0 = 45; parameters_angle_deg = 58
    total = round(run_spec_steps + parameters_v0 + parameters_angle_deg, 2)
    mean = round(total / 3, 2)
    first_plus_second = round(run_spec_steps + parameters_v0, 2)
    first_minus_second = round(run_spec_steps - parameters_v0, 2)
    first_times_second = round(run_spec_steps * parameters_v0, 2)
    return {"total": total, "mean": mean, "first_plus_second": first_plus_second, "first_minus_second": first_minus_second, "first_times_second": first_times_second}
def main():
    a = compute(); b = compute()
    sa = hashlib.sha256(repr(sorted(a.items())).encode()).hexdigest()
    sb = hashlib.sha256(repr(sorted(b.items())).encode()).hexdigest()
    for key in ["total", "mean", "first_plus_second", "first_minus_second", "first_times_second"]:
        print(f"{key}: {a[key]}")
    print(f"Run 1 SHA-256: {sa}")
    print(f"Run 2 SHA-256: {sb}")
    print(f"Deterministic: {'MATCH' if sa == sb else 'MISMATCH'}")
if __name__ == "__main__":
    main()
