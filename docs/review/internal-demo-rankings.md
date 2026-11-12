# Review — `internal-demo-rankings`

**Verdict: BROKEN** (usable / partial / broken)

**Date:** 2026-11-02. **Mode:** package-only review; nothing merged, pushed, or deployed. **Manifest at review time:** 63047 databases.

## Specification

- Name: Internal Demo Rankings Database
- Record kind: `demo ranking` — AI: JAH Rank Auditor
- Tagline: Internal quality rankings for every simulation, program, and demo. Hidden from the public grid.
- ID prefix: `JAH-RANK-` — manifest record_count: 1724 — source: signature
- Full-file-check census class: **NO-DEMO** (read: EMPTY-BODY, org: BROKEN-LOADER, steps 0/7, median body 75 chars)
- Index: `/home/hatch/workspace/jah-databases/data/internal-demo-rankings/index.jsonl.gz`
- Primary sample source: chunks (18 files) (18 chunk files, 12 records sampled)

## Checks (evidence per check)

| Check | Result | Evidence |
|---|---|---|
| spec_present | PASS | manifest entry: name='Internal Demo Rankings Database' record_kind='demo ranking' ai_name='JAH Rank Auditor' id_prefix='JAH-RANK-'; missing fields: none |
| index_loads | PASS | local: 1724 records parsed from /home/hatch/workspace/jah-databases/data/internal-demo-rankings/index.jsonl.gz |
| count_agrees | PASS | manifest record_count=1724, index lines=1724, chunk records=1724 |
| records_parse | FAIL | sampled 12 records (chunks (18 files), positions [0, 1, 2, 3, 4, 50, 100, 150, 200, 250, 300, 350]); unparseable=none; with title=0/12; id-prefix mismatches=none |
| readable | FAIL | readable 0/12 sampled (prose >=200 chars, garbled-token fraction <0.35); median sampled prose 0 chars; garbled 0 |
| demos_run | FAIL | no demo in any of the 12 sampled records (primary source: chunks (18 files)) |
| links_resolve | PARTIAL | page exists; markers exhaustive=True merger=True stCount=True old_loader=True; index file present locally (/home/hatch/workspace/jah-databases/data/internal-demo-rankings/index.jsonl.gz) |
| citations_present | PASS | source/citations/src present in 12/12 sampled; JCC v1 code formable, e.g. JAHDB/internal-demo-rankings#JAH-RANK-00000001+k=166884b6 |

Demo totals (sampled): present 0, ran OK 0, output mismatch 0, failed 0, skipped 0.

## Notes

- index rows are title-only (id/t/g) AND chunk records carry no readable prose either (median sampled chunk prose 0 chars) — the gap is in the stored records, not just the index
- images: 0/12 sampled records carry an image field

## What this verdict means

Broken for use: the index does not load, records do not parse, or sampled records carry no readable prose. Do not serve this database to an outside AI until the failing check is fixed and review mode re-run.

## How this extends the full-file-check program

The census assigns this database a class from a network-wide scan; review mode reads this one database end to end — spec, real files, executed demos, resolved links, per-record citations — and gives a verdict with evidence. It does not replace the census, the priority queue, or the fill waves.
