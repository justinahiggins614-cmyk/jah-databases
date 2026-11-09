"""Numeric check — Flagship Mix — Relay of Signals × Signature Comic Store Field Guide: The Core De (JAH-MIX-COMICS-001).
Made for this page from the record's own numbers.
This program checks the arithmetic of the stored figures; its outputs
are check-sums, not physical quantities."""
import hashlib
def compute():
    a_chunk = 1; a_pg = 22
    total = round(a_chunk + a_pg, 2)
    mean = round(total / 2, 2)
    first_plus_second = round(a_chunk + a_pg, 2)
    first_minus_second = round(a_chunk - a_pg, 2)
    first_times_second = round(a_chunk * a_pg, 2)
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
