# Usage counts: The 1Password Database (1password) — Spec sheet

Record JAH-DUCS-000011 — Signature edition, database-usage-counts-signature.
JCC v1 code: JAHDB/database-usage-counts-signature#JAH-DUCS-000011

## Spec
- **Mechanism:** Usage figures for The 1Password Database (1password). USAGE METRICS (all derived from the live manifest data/manifest.json and the data-file inventory; no invented numbers): record_count = the database's record_count field; edition_siblings = other databases in the same edition group (same subject root after stripping signature-/public-/-signature/-public affixes) minus 1; topic_cluster = number of databases sharing the same record_kind; link_count = edition siblings + xdb_pulls entries + (1 if the entry carries a page or page_url); usage_score = round(record_count * (1 + log10(1 + link_count)

## Key figures
- **generator.hard cap:** 1000000000000000
- **ladder rank:** 11
- **million march.target:** 1000000

## Official demo output
- **total:** 1000011
- **mean:** 500005.5
- **first plus second:** 1000011
- **first minus second:** -999989
- **first times second:** 11000000

Free forever. Part of The 'Merica-L Internet.