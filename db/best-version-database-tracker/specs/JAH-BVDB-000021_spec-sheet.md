# Best version of '7zip': The 7-Zip Signature Database — Spec sheet

Record JAH-BVDB-000021 — Public edition, best-version-database-tracker.
JCC v1 code: JAHDB/best-version-database-tracker#JAH-BVDB-000021

## Spec
- **Mechanism:** Best version of the database subject '7zip': The 7-Zip Signature Database (7zip-signature), holding 20 records. Why: BEST-VERSION RULE (deterministic, applied identically to every record): 1) the edition / file variant with the highest record_count (or, for files, the greatest byte size, i.e. the most complete variant) wins; 2) tie-break: the Signature edition wins over the public edition (for files: the manifest-declared local_index file wins); 3) final tie-break: alphabetical slug (or filename) order. Losing editions/variants are named with their counts on every record. Recompute: compare th

## Key figures
- **generator.hard cap:** 1000000000000000
- **ladder rank:** 6
- **million march.target:** 1000000
- **provenance.editions count:** 2

## Official demo output
- **total:** 1000008
- **mean:** 333336
- **first plus second:** 8
- **first minus second:** -4
- **first times second:** 12

Free forever. Part of The 'Merica-L Internet.