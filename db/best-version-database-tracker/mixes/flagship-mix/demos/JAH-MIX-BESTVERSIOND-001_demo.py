"""Numeric check — Flagship Mix — Best version of '15-minute-cities': Signature 15 Minute Citi × Be (JAH-MIX-BESTVERSIOND-001).
Made for this page from the record's own numbers.
This program checks the arithmetic of the stored figures; its outputs
are check-sums, not physical quantities."""
import hashlib
def compute():
    a_ladder_rank = 1; b_ladder_rank = 1; a_provenance_editions_count = 2; b_provenance_editions_count = 2
    total = round(a_ladder_rank + b_ladder_rank + a_provenance_editions_count + b_provenance_editions_count, 2)
    mean = round(total / 4, 2)
    first_plus_second = round(a_ladder_rank + b_ladder_rank, 2)
    first_minus_second = round(a_ladder_rank - b_ladder_rank, 2)
    first_times_second = round(a_ladder_rank * b_ladder_rank, 2)
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
