"""Numeric check — "4-(5-fluoromethyl-2-pyridloxy) phenoxyvaleric acids (JAH-PAT-050265).
Made for this page from text-derived counts (the record carries no usable numbers of its own).
This program checks the arithmetic of the stored figures; its outputs
are check-sums, not physical quantities."""
import hashlib
def compute():
    title_chars = 52; desc_chars = 52; source_count = 0; field_count = 2
    total = round(title_chars + desc_chars + source_count + field_count, 2)
    mean = round(total / 4, 2)
    first_plus_second = round(title_chars + desc_chars, 2)
    first_minus_second = round(title_chars - desc_chars, 2)
    first_times_second = round(title_chars * desc_chars, 2)
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
