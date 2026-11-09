"""Numeric check — JAH-OLY-000004 (JAH-OLY-000004).
Made for this page from the record's own numbers.
This program checks the arithmetic of the stored figures; its outputs
are check-sums, not physical quantities."""
import hashlib
def compute():
    margin = 22.5; totals_jah_ai_dom_028 = 190.599999999999994; totals_jah_ai_dom_051 = 213.099999999999994
    total = round(margin + totals_jah_ai_dom_028 + totals_jah_ai_dom_051, 2)
    mean = round(total / 3, 2)
    first_plus_second = round(margin + totals_jah_ai_dom_028, 2)
    first_minus_second = round(margin - totals_jah_ai_dom_028, 2)
    first_times_second = round(margin * totals_jah_ai_dom_028, 2)
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
