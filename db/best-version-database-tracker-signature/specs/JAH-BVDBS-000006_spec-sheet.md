# Best version of '1password': The 1Password Signature Database — Spec sheet

Record JAH-BVDBS-000006 — Signature edition, best-version-database-tracker-signature.
JCC v1 code: JAHDB/best-version-database-tracker-signature#JAH-BVDBS-000006

## Spec
- **Mechanism:** Best version of the database subject '1password': The 1Password Signature Database (1password-signature), holding 20 records. Why: BEST-VERSION RULE (deterministic, applied identically to every record): 1) the edition / file variant with the highest record_count (or, for files, the greatest byte size, i.e. the most complete variant) wins; 2) tie-break: the Signature edition wins over the public edition (for files: the manifest-declared local_index file wins); 3) final tie-break: alphabetical slug (or filename) order. Losing editions/variants are named with their counts on every record. Recompu

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