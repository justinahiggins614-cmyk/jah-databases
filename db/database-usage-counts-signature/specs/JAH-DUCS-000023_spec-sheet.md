# Usage counts: 3D Media Database (3d-media) — Spec sheet

Record JAH-DUCS-000023 — Signature edition, database-usage-counts-signature.
JCC v1 code: JAHDB/database-usage-counts-signature#JAH-DUCS-000023

## Spec
- **Mechanism:** Usage figures for 3D Media Database (3d-media). USAGE METRICS (all derived from the live manifest data/manifest.json and the data-file inventory; no invented numbers): record_count = the database's record_count field; edition_siblings = other databases in the same edition group (same subject root after stripping signature-/public-/-signature/-public affixes) minus 1; topic_cluster = number of databases sharing the same record_kind; link_count = edition siblings + xdb_pulls entries + (1 if the entry carries a page or page_url); usage_score = round(record_count * (1 + log10(1 + link_count)) + 10

## Key figures
- **generator.hard cap:** 1000000000000000
- **ladder rank:** 8
- **million march.target:** 1000000

## Official demo output
- **total:** 1000008
- **mean:** 500004
- **first plus second:** 1000008
- **first minus second:** -999992
- **first times second:** 8000000

Free forever. Part of The 'Merica-L Internet.