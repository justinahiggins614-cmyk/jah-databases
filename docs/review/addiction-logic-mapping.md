# Review — `addiction-logic-mapping`

**Verdict: PARTIAL** (usable / partial / broken)

**Date:** 2026-11-02. **Mode:** package-only review; nothing merged, pushed, or deployed. **Manifest at review time:** 63047 databases.

## Specification

- Name: Addiction Logic Mapping Database
- Record kind: `reward logic map` — AI: LogicFrame Addiction Logic Mapping
- Tagline: Reward-pattern-to-logic mappings: Signature conceptual models of compulsive reward loops as logic structures.
- ID prefix: `JAH-ADLM-` — manifest record_count: 24 — source: project-three-named-r14
- Full-file-check census class: **NO-DEMO** (read: READABLE, org: ORGANIZED, steps 0/7, median body 668 chars)
- Index: `/home/hatch/workspace/jah-databases-data-1/data/addiction-logic-mapping/index.jsonl.gz`
- Primary sample source: chunks (1 files) (1 chunk files, 5 records sampled)

## Checks (evidence per check)

| Check | Result | Evidence |
|---|---|---|
| spec_present | PASS | manifest entry: name='Addiction Logic Mapping Database' record_kind='reward logic map' ai_name='LogicFrame Addiction Logic Mapping' id_prefix='JAH-ADLM-'; missing fields: none |
| index_loads | PASS | url->local: 24 records parsed from /home/hatch/workspace/jah-databases-data-1/data/addiction-logic-mapping/index.jsonl.gz |
| count_agrees | PASS | manifest record_count=24, index lines=24, chunk records=24 |
| records_parse | PASS | sampled 5 records (chunks (1 files), positions [0, 1, 2, 3, 4]); unparseable=none; with title=5/5; id-prefix mismatches=none |
| readable | PASS | readable 5/5 sampled (prose >=200 chars, garbled-token fraction <0.35); median sampled prose 668 chars; garbled 0 |
| demos_run | FAIL | no demo in any of the 5 sampled records (primary source: chunks (1 files)) |
| links_resolve | PARTIAL | page exists; markers exhaustive=True merger=True stCount=True old_loader=True; index file present locally (/home/hatch/workspace/jah-databases-data-1/data/addiction-logic-mapping/index.jsonl.gz) |
| citations_present | PASS | source/citations/src present in 5/5 sampled; JCC v1 code formable, e.g. JAHDB/addiction-logic-mapping#JAH-ADLM-000001+k=b7fee209 |

Demo totals (sampled): present 0, ran OK 0, output mismatch 0, failed 0, skipped 0.

## Notes

- images: 0/5 sampled records carry an image field

## What this verdict means

Partly usable: the data loads and reads, but at least one full-record step is missing (see the failed / partial checks above). Remediation is a fill for the missing step(s), not a rebuild — queue it in the full-file-check priority queue, do not re-audit the whole database by hand.

## How this extends the full-file-check program

The census assigns this database a class from a network-wide scan; review mode reads this one database end to end — spec, real files, executed demos, resolved links, per-record citations — and gives a verdict with evidence. It does not replace the census, the priority queue, or the fill waves.
