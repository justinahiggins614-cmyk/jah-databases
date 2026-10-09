# Signature Website Creator Database — VIRTUAL ARCHIVE (honest disclosure)

This database's archive is **virtual and deterministic** — it is not copied from
files, because the source (Signature Website Creator) has no stored archive of
its own either: its "1 Million Website Options" catalog is generated
deterministically on demand, the same way.

How it works:
- The archive index is the deterministic option space: every website option is
  identified by a seed (1 … 1,000,000) plus an option family.
- Any record can be materialized at any time — in the browser on the Archive
  tab, or via the Generator tab — by running the page's generator with that
  seed. The same seed always yields the same full website-option entry.
- The generator's full entry schema is documented in the page's About tab and
  validated by the 40-record harness (all fields present, deterministic).

There is no hidden file of records and none is claimed. "One click opens the
FULL record" means the page builds the complete entry for the seed you clicked —
the same complete entry it shows for generated records.
