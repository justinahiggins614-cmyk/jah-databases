#!/usr/bin/env python3
"""Per-pair configs for the govf2 (group F, part 2) build drivers."""

PAIRS = {}

PAIRS["data-source-reliability"] = {
"docstring": '''"""Build the Data Source Reliability databases for JAH Databases
(governance track, group F: data governance for a million-database-scale
network, 2026-10-17).

Dedupe gate: none of the 8 governance slugs exist in data/manifest.json
(2,770 databases checked 2026-10-17); no other builder writing these slugs.
ID prefixes JAH-DSR- (public) and JAH-DSRS- (signature) verified free: zero
exact or substring hits in manifest id_prefix values and zero hits in all
shard record IDs of jah-databases-data-1. All 68 record titles checked
against the WHOLE system (exact dedupe index + live shard title corpus of
1,143,457 titles) BEFORE authoring.

So this build creates two NEW databases, 34 ladder-ordered records each:

  data-source-reliability           - The Data Source Reliability Database
      (public-harvest: real, fact-checked reliability knowledge - source
      history, correction rates, independent corroboration, known
      limitations, reputation scores, provenance, freshness, citation
      practice, agreement analysis, bias assessment, retraction handling,
      survey/sensor/derived/expert/archival reliability, composite indexes,
      decay, adversarial detection, confidence calibration, weighted
      consensus, audit trails, monitoring, baselines, dispute resolution,
      certification, dashboards)
  data-source-reliability-signature - The Data Source Reliability Signature
      Database (the Signature Reliability Doctrine; src signature, titles
      suffixed " (Signature Edition)", never presented as authentic public
      record)

34 records each, ladder-ordered 1-34 (ladder_tier foundations 1-10 /
compounded 11-21 / advanced 22-34).

Numerical cores: hand-computed 2026-10-17, machine-verified by the demos
(see demos_data_source_reliability.py). Every demo prints its real computed
values, asserts tight bounds (never float exact-equality), and ends with
the OK marker; the build machine-executes all 68 demos.

Writes (this builder's scope ONLY - a merger handles the rest):
  main repo : db/data-source-reliability/index.html + gen-...js
              db/data-source-reliability-signature/index.html + gen-...js
  shard repo: data/data-source-reliability/index.jsonl.gz + chunks/chunk-0000.jsonl.gz
              data/data-source-reliability-signature/... (same)
  build dir : code/data-source-reliability-build/{build.py, entries_*.py, demos_*.py}
  fragment  : ~/workspace/hidden_files/missing-builds/fragments/data-source-reliability.json

NEVER touches: data/manifest.json, api.json, index.html, README.md,
docs/AI_ACCESS.md. NEVER git commits or pushes.

Never the words "bat belt" anywhere. No website references. No Facebook.
"""''',
"pub_name": "The Data Source Reliability Database",
"pub_tagline": ("How much to trust what you read: source history, correction rates, independent "
    "corroboration, known limitations, and reputation scores for every kind of source - surveys, "
    "sensors, archives, experts, and machine-generated content - each source a scored, audited record."),
"pub_record_kind": "source reliability record",
"pub_prefix": "JAH-DSR-",
"pub_ai": "JAH Source Reliability Archivist",
"pub_role": ("Source reliability archivist - scoring how much to trust every kind of source: "
    "history, correction rates, corroboration, limitations, reputation; teaching progressively "
    "along the ladder from foundations through compounded to advanced; answers from many angles "
    "- provenance, freshness, agreement, bias, confidence - using only archive data from this system"),
"pub_search_ph": "Search source history, correction rates, corroboration, reputation, bias...",
"pub_chat_ph": "Ask about data source reliability...",
"pub_archive_blurb": ("Seeded public-record source reliability records, marching toward one million records. "
    "Presented in teaching-ladder order: foundations, compounded, advanced."),
"pub_fields": "Foundations \u00b7 Compounded \u00b7 Advanced - each tier opens on demand and loads only what you open",
"pub_gen_desc": "Generate clearly-labeled source reliability studies. Seeded archive records are the authoritative entries.",
"pub_gen_kind": "reliability-study",
"pub_gen_demo_kind": "reliability-demo",
"pub_greet": ("I am the JAH Source Reliability Archivist. Ask me about data source reliability - "
    "source history, correction rates, corroboration, limitations, and reputation scores."),
"sig_name": "The Data Source Reliability Signature Database",
"sig_tagline": ("The Signature Reliability Doctrine: every source weighed, every claim corroborated, "
    "every correction logged in the open - the full ladder from reliability foundations through "
    "source-type analysis to advanced governance, reframed as Signature science. Clearly labeled "
    "Signature-made, never presented as authentic public record."),
"sig_record_kind": "source reliability record",
"sig_prefix": "JAH-DSRS-",
"sig_ai": "JAH Source Reliability Archivist (Signature)",
"sig_role": ("Source reliability archivist - Signature editions: the Signature Reliability Doctrine, "
    "every source weighed and every claim corroborated, clearly labeled Signature-made and never "
    "presented as authentic public record; teaches progressively along the ladder from foundations "
    "through compounded to advanced; answers from many angles using only archive data from this system"),
"sig_search_ph": "Search source history, correction rates, corroboration, reputation, bias...",
"sig_chat_ph": "Ask about the Signature reliability doctrine...",
"sig_archive_blurb": ("Seeded Signature-original source reliability records, marching toward one million records. "
    "Presented in teaching-ladder order: foundations, compounded, advanced."),
"sig_fields": "Foundations \u00b7 Compounded \u00b7 Advanced - each tier opens on demand and loads only what you open",
"sig_gen_desc": "Generate clearly-labeled Signature reliability studies. Seeded archive records are the authoritative entries.",
"sig_gen_kind": "reliability-study",
"sig_gen_demo_kind": "reliability-demo",
"sig_greet": ("I am the JAH Source Reliability Archivist (Signature). Ask me about the Signature Reliability "
    "Doctrine - every source weighed, every claim corroborated."),
"pub_line": ("Public records - real, fact-checked reliability knowledge: source history records, "
    "correction-rate metrics, independent corroboration counts, known-limitation registers, "
    "reputation score models, primary vs secondary classification, provenance capture, freshness "
    "metrics, citation practice, cross-source agreement analysis, correction-lag measurement, bias "
    "assessment, retraction handling, sample vs census reliability, sensor data, survey data, "
    "derived data, expert opinion, archival records, composite indexes, reliability decay, "
    "adversarial-source detection, anonymous-source policy, confidence calibration, "
    "reliability-weighted consensus, audit trails, automated monitoring, machine-generated content "
    "reliability, domain baselines, dispute resolution, certification, and dashboards."),
"sig_line": ("Signature originals - the Signature Reliability Doctrine: every source weighed, every "
    "claim corroborated, every correction logged in the open; reputation earned in public and "
    "spent carefully. Clearly labeled Signature-made, never presented as authentic public record."),
"ladder": (" Records are ordered by the teaching ladder: Foundations (reliability overview, source "
    "history, correction rates, corroboration, limitations, reputation scores, primary vs secondary "
    "classification, provenance, freshness, citation practice) -> Compounded (agreement analysis, "
    "correction lag, bias assessment, retraction handling, sample vs census, sensor data, survey "
    "data, derived data, expert opinion, archival records, composite index) -> Advanced (reliability "
    "decay, adversarial detection, anonymous-source policy, confidence calibration, weighted "
    "consensus, audit trails, automated monitoring, machine-generated content, domain baselines, "
    "dispute resolution, certification, dashboard exemplar, self-audit and mastery)."),
}

PAIRS["record-conflict-reconciliation"] = {
"docstring": '''"""Build the Record Conflict Reconciliation databases for JAH Databases
(governance track, group F: data governance for a million-database-scale
network, 2026-10-17).

Dedupe gate: none of the 8 governance slugs exist in data/manifest.json
(2,770 databases checked 2026-10-17); no other builder writing these slugs.
ID prefixes JAH-RCR- (public) and JAH-RCRS- (signature) verified free: zero
exact or substring hits in manifest id_prefix values and zero hits in all
shard record IDs of jah-databases-data-1. All 68 record titles checked
against the WHOLE system (exact dedupe index + live shard title corpus of
1,143,457 titles) BEFORE authoring.

So this build creates two NEW databases, 34 ladder-ordered records each:

  record-conflict-reconciliation           - The Record Conflict Reconciliation
      Database (public-harvest: real, fact-checked reconciliation knowledge -
      version identity, source-authority hierarchies, conflict taxonomy,
      detection rules, provenance tagging, confidence scoring, review
      triggers, merge policies, three-way merge, last-writer-wins,
      field-level resolution, temporal/unit/entity conflicts, duplicate
      detection, escalation, quorum resolution, human review queues,
      resolution logs, faulty-source handling, audit trails, decision
      records, discrepancy queues, SLAs, scale, schema drift, prediction,
      API contracts, metrics, policy versioning, disaster recovery)
  record-conflict-reconciliation-signature - The Record Conflict
      Reconciliation Signature Database (the Signature Reconciliation
      Doctrine; src signature, titles suffixed " (Signature Edition)",
      never presented as authentic public record)

34 records each, ladder-ordered 1-34 (ladder_tier foundations 1-10 /
compounded 11-21 / advanced 22-34).

Numerical cores: hand-computed 2026-10-17, machine-verified by the demos
(see demos_record_conflict_reconciliation.py). Every demo prints its real
computed values, asserts tight bounds (never float exact-equality), and
ends with the OK marker; the build machine-executes all 68 demos.

Writes (this builder's scope ONLY - a merger handles the rest):
  main repo : db/record-conflict-reconciliation/index.html + gen-...js
              db/record-conflict-reconciliation-signature/index.html + gen-...js
  shard repo: data/record-conflict-reconciliation/index.jsonl.gz + chunks/chunk-0000.jsonl.gz
              data/record-conflict-reconciliation-signature/... (same)
  build dir : code/record-conflict-reconciliation-build/{build.py, entries_*.py, demos_*.py}
  fragment  : ~/workspace/hidden_files/missing-builds/fragments/record-conflict-reconciliation.json

NEVER touches: data/manifest.json, api.json, index.html, README.md,
docs/AI_ACCESS.md. NEVER git commits or pushes.

Never the words "bat belt" anywhere. No website references. No Facebook.
"""''',
"pub_name": "The Record Conflict Reconciliation Database",
"pub_tagline": ("When records disagree: source-authority hierarchies, conflict case records, resolution "
    "decisions, and unresolved-discrepancy queues - every competing version heard, weighed, and resolved "
    "in writing, at any scale."),
"pub_record_kind": "conflict reconciliation record",
"pub_prefix": "JAH-RCR-",
"pub_ai": "JAH Conflict Reconciliation Archivist",
"pub_role": ("Conflict reconciliation archivist - resolving competing record versions: authority "
    "hierarchies, detection, three-way merge, quorum, escalation, and audit; teaching progressively "
    "along the ladder from foundations through compounded to advanced; answers from many angles "
    "- identity, authority, evidence, procedure - using only archive data from this system"),
"pub_search_ph": "Search conflict taxonomy, three-way merge, quorum, escalation, audit...",
"pub_chat_ph": "Ask about record conflict reconciliation...",
"pub_archive_blurb": ("Seeded public-record conflict reconciliation records, marching toward one million records. "
    "Presented in teaching-ladder order: foundations, compounded, advanced."),
"pub_fields": "Foundations \u00b7 Compounded \u00b7 Advanced - each tier opens on demand and loads only what you open",
"pub_gen_desc": "Generate clearly-labeled reconciliation studies. Seeded archive records are the authoritative entries.",
"pub_gen_kind": "reconciliation-study",
"pub_gen_demo_kind": "reconciliation-demo",
"pub_greet": ("I am the JAH Conflict Reconciliation Archivist. Ask me about record conflicts - competing "
    "versions, authority hierarchies, resolution decisions, and discrepancy queues."),
"sig_name": "The Record Conflict Reconciliation Signature Database",
"sig_tagline": ("The Signature Reconciliation Doctrine: every conflict heard, every version weighed by "
    "authority, every resolution written down with reasons - the full ladder from reconciliation "
    "foundations through resolution mechanics to advanced governance, reframed as Signature science. "
    "Clearly labeled Signature-made, never presented as authentic public record."),
"sig_record_kind": "conflict reconciliation record",
"sig_prefix": "JAH-RCRS-",
"sig_ai": "JAH Conflict Reconciliation Archivist (Signature)",
"sig_role": ("Conflict reconciliation archivist - Signature editions: the Signature Reconciliation Doctrine, "
    "every conflict heard and every resolution written with reasons, clearly labeled Signature-made and "
    "never presented as authentic public record; teaches progressively along the ladder from foundations "
    "through compounded to advanced; answers from many angles using only archive data from this system"),
"sig_search_ph": "Search conflict taxonomy, three-way merge, quorum, escalation, audit...",
"sig_chat_ph": "Ask about the Signature reconciliation doctrine...",
"sig_archive_blurb": ("Seeded Signature-original conflict reconciliation records, marching toward one million records. "
    "Presented in teaching-ladder order: foundations, compounded, advanced."),
"sig_fields": "Foundations \u00b7 Compounded \u00b7 Advanced - each tier opens on demand and loads only what you open",
"sig_gen_desc": "Generate clearly-labeled Signature reconciliation studies. Seeded archive records are the authoritative entries.",
"sig_gen_kind": "reconciliation-study",
"sig_gen_demo_kind": "reconciliation-demo",
"sig_greet": ("I am the JAH Conflict Reconciliation Archivist (Signature). Ask me about the Signature "
    "Reconciliation Doctrine - every conflict heard, every resolution written with reasons."),
"pub_line": ("Public records - real, fact-checked reconciliation knowledge: record version identity, "
    "source-authority hierarchies, conflict taxonomy, detection rules, provenance tagging, confidence "
    "scoring, manual review triggers, merge policies, conflict case record formats, three-way merge, "
    "last-writer-wins analysis, field-level resolution, temporal conflicts, unit and currency conflicts, "
    "entity resolution conflicts, duplicate vs true conflict distinction, escalation paths, quorum "
    "resolution, human-in-the-loop queues, automated resolution logs, faulty-source conflicts, "
    "reconciliation audit trails, resolution decision records, unresolved-discrepancy queues, conflict "
    "SLAs, reconciliation at million-database scale, schema-drift conflicts, conflict prediction, "
    "reconciliation API contracts, conflict metrics dashboards, policy versioning, and disaster recovery."),
"sig_line": ("Signature originals - the Signature Reconciliation Doctrine: every conflict heard, every "
    "version weighed by authority, every resolution written down with reasons; no silent merges, no lost "
    "versions. Clearly labeled Signature-made, never presented as authentic public record."),
"ladder": (" Records are ordered by the teaching ladder: Foundations (reconciliation overview, version "
    "identity, authority hierarchy, conflict taxonomy, detection rules, provenance tagging, confidence "
    "scoring, review triggers, merge policy, case record format) -> Compounded (three-way merge, "
    "last-writer-wins, field-level resolution, temporal conflicts, unit conflicts, entity resolution, "
    "duplicate vs true conflict, escalation, quorum resolution, human review queues, resolution log) -> "
    "Advanced (faulty-source conflicts, audit trail, decision records, discrepancy queues, conflict SLA, "
    "million-database scale, schema drift, conflict prediction, API contract, metrics dashboard, policy "
    "versioning, disaster recovery, self-audit and mastery)."),
}

PAIRS["database-cost-accounting"] = {
"docstring": '''"""Build the Database Cost Accounting databases for JAH Databases
(governance track, group F: data governance for a million-database-scale
network, 2026-10-17).

Dedupe gate: none of the 8 governance slugs exist in data/manifest.json
(2,770 databases checked 2026-10-17); no other builder writing these slugs.
ID prefixes JAH-DCA- (public) and JAH-DCAS- (signature) verified free: zero
exact or substring hits in manifest id_prefix values and zero hits in all
shard record IDs of jah-databases-data-1. All 68 record titles checked
against the WHOLE system (exact dedupe index + live shard title corpus of
1,143,457 titles) BEFORE authoring.

So this build creates two NEW databases, 34 ladder-ordered records each:

  database-cost-accounting           - The Database Cost Accounting Database
      (public-harvest: real, fact-checked cost knowledge - storage, compute,
      bandwidth, indexing, generation, retrieval cost models; fixed vs
      variable costs; allocation principles; per-record units; cost ledgers;
      shared-cost allocation; tiering; index rebuilds; batch costing; SLA
      tradeoffs; cache economics; compression; backup/DR; inter-shard
      transfer; anomaly detection; TCO at scale; budgeting; chargeback;
      data-quality cost; governance overhead; marginal cost per million;
      pipeline comparisons; energy/carbon accounting; cost audits; budget
      variance; optimization playbooks; dashboards)
  database-cost-accounting-signature - The Database Cost Accounting Signature
      Database (the Signature Cost Doctrine; src signature, titles suffixed
      " (Signature Edition)", never presented as authentic public record)

34 records each, ladder-ordered 1-34 (ladder_tier foundations 1-10 /
compounded 11-21 / advanced 22-34).

Numerical cores: hand-computed 2026-10-17, machine-verified by the demos
(see demos_database_cost_accounting.py). Every demo prints its real computed
values, asserts tight bounds (never float exact-equality), and ends with
the OK marker; the build machine-executes all 68 demos.

Writes (this builder's scope ONLY - a merger handles the rest):
  main repo : db/database-cost-accounting/index.html + gen-...js
              db/database-cost-accounting-signature/index.html + gen-...js
  shard repo: data/database-cost-accounting/index.jsonl.gz + chunks/chunk-0000.jsonl.gz
              data/database-cost-accounting-signature/... (same)
  build dir : code/database-cost-accounting-build/{build.py, entries_*.py, demos_*.py}
  fragment  : ~/workspace/hidden_files/missing-builds/fragments/database-cost-accounting.json

NEVER touches: data/manifest.json, api.json, index.html, README.md,
docs/AI_ACCESS.md. NEVER git commits or pushes.

Never the words "bat belt" anywhere. No website references. No Facebook.
"""''',
"pub_name": "The Database Cost Accounting Database",
"pub_tagline": ("What every database really costs: storage, compute, bandwidth, indexing, generation, and "
    "retrieval cost records per database - with allocation models, ledgers, and the Signature-grade "
    "discipline of accounting for every byte and every query."),
"pub_record_kind": "cost accounting record",
"pub_prefix": "JAH-DCA-",
"pub_ai": "JAH Cost Accounting Archivist",
"pub_role": ("Cost accounting archivist - pricing every byte and every query: storage, compute, bandwidth, "
    "indexing, generation, and retrieval costs per database with allocation models; teaching progressively "
    "along the ladder from foundations through compounded to advanced; answers from many angles "
    "- unit costs, ledgers, budgets, tradeoffs - using only archive data from this system"),
"pub_search_ph": "Search storage costs, TCO, chargeback, budgets, optimization...",
"pub_chat_ph": "Ask about database cost accounting...",
"pub_archive_blurb": ("Seeded public-record cost accounting records, marching toward one million records. "
    "Presented in teaching-ladder order: foundations, compounded, advanced."),
"pub_fields": "Foundations \u00b7 Compounded \u00b7 Advanced - each tier opens on demand and loads only what you open",
"pub_gen_desc": "Generate clearly-labeled cost accounting studies. Seeded archive records are the authoritative entries.",
"pub_gen_kind": "cost-study",
"pub_gen_demo_kind": "cost-demo",
"pub_greet": ("I am the JAH Cost Accounting Archivist. Ask me about database costs - storage, compute, bandwidth, "
    "indexing, generation, retrieval, budgets, and optimization."),
"sig_name": "The Database Cost Accounting Signature Database",
"sig_tagline": ("The Signature Cost Doctrine: every byte priced, every query accounted, every dollar attributed - "
    "the full ladder from cost foundations through allocation mechanics to advanced financial governance, "
    "reframed as Signature science. Clearly labeled Signature-made, never presented as authentic public record."),
"sig_record_kind": "cost accounting record",
"sig_prefix": "JAH-DCAS-",
"sig_ai": "JAH Cost Accounting Archivist (Signature)",
"sig_role": ("Cost accounting archivist - Signature editions: the Signature Cost Doctrine, every byte priced and "
    "every dollar attributed, clearly labeled Signature-made and never presented as authentic public record; "
    "teaches progressively along the ladder from foundations through compounded to advanced; answers from many "
    "angles using only archive data from this system"),
"sig_search_ph": "Search storage costs, TCO, chargeback, budgets, optimization...",
"sig_chat_ph": "Ask about the Signature cost doctrine...",
"sig_archive_blurb": ("Seeded Signature-original cost accounting records, marching toward one million records. "
    "Presented in teaching-ladder order: foundations, compounded, advanced."),
"sig_fields": "Foundations \u00b7 Compounded \u00b7 Advanced - each tier opens on demand and loads only what you open",
"sig_gen_desc": "Generate clearly-labeled Signature cost studies. Seeded archive records are the authoritative entries.",
"sig_gen_kind": "cost-study",
"sig_gen_demo_kind": "cost-demo",
"sig_greet": ("I am the JAH Cost Accounting Archivist (Signature). Ask me about the Signature Cost Doctrine - "
    "every byte priced, every query accounted, every dollar attributed."),
"pub_line": ("Public records - real, fact-checked cost knowledge: storage cost models, compute cost models, "
    "bandwidth and egress models, indexing costs, generation costs, retrieval costs, fixed vs variable cost "
    "analysis, cost allocation principles, per-record cost units, per-database cost ledgers, shared-cost "
    "allocation models, storage tiering economics, index rebuild costs, generation batch costing, retrieval "
    "SLA cost tradeoffs, cache cost-benefit analysis, compression savings, backup and disaster-recovery costs, "
    "inter-shard transfer costs, cost anomaly detection, total cost of ownership at scale, "
    "forecasting-driven budgeting, chargeback and showback models, cost of data quality, cost of governance "
    "overhead, marginal cost per million records, public vs Signature pipeline comparisons, energy and carbon "
    "cost accounting, cost audit records, budget variance records, cost optimization playbooks, and cost "
    "dashboards."),
"sig_line": ("Signature originals - the Signature Cost Doctrine: every byte priced, every query accounted, "
    "every dollar attributed; waste is a finding, not a rounding error. Clearly labeled Signature-made, "
    "never presented as authentic public record."),
"ladder": (" Records are ordered by the teaching ladder: Foundations (cost overview, storage, compute, "
    "bandwidth, indexing, generation, retrieval, fixed vs variable, allocation principles, per-record unit) -> "
    "Compounded (cost ledger, shared-cost allocation, tiering, index rebuilds, batch costing, SLA tradeoffs, "
    "cache economics, compression, backup/DR, inter-shard transfer, anomaly detection) -> Advanced (TCO at "
    "scale, budgeting, chargeback, data-quality cost, governance overhead, marginal cost per million, pipeline "
    "comparison, energy/carbon accounting, cost audit, budget variance, optimization playbook, dashboard "
    "exemplar, self-audit and mastery)."),
}

PAIRS["capacity-growth-forecasting"] = {
"docstring": '''"""Build the Capacity Growth Forecasting databases for JAH Databases
(governance track, group F: data governance for a million-database-scale
network, 2026-10-17).

Dedupe gate: none of the 8 governance slugs exist in data/manifest.json
(2,770 databases checked 2026-10-17); no other builder writing these slugs.
ID prefixes JAH-CGF- (public) and JAH-CGFS- (signature) verified free: zero
exact or substring hits in manifest id_prefix values and zero hits in all
shard record IDs of jah-databases-data-1. All 68 record titles checked
against the WHOLE system (exact dedupe index + live shard title corpus of
1,143,457 titles) BEFORE authoring.

So this build creates two NEW databases, 34 ladder-ordered records each:

  capacity-growth-forecasting            - The Capacity Growth Forecasting Database
      (public-harvest: real, fact-checked forecasting knowledge - record count
      projections, storage requirement forecasts, throughput estimates,
      hardware constraint mapping, growth rate measurement, linear and
      compounding models, seasonal patterns, horizon selection, forecast
      histories, accuracy tracking, headroom policy, ingestion/query/index
      capacity, shard split forecasting, backfill planning, burst reserves,
      fleet forecasting, procurement, million-scale projection, logistic
      models, constraint-bound forecasts, Monte Carlo simulation, scenarios,
      confidence intervals, cliff detection, shrinkage, cost-linked planning,
      governance, dashboards, model selection)
  capacity-growth-forecasting-signature  - The Capacity Growth Forecasting Signature
      Database (the Signature Foresight Doctrine; src signature, titles
      suffixed " (Signature Edition)", never presented as authentic public
      record)

34 records each, ladder-ordered 1-34 (ladder_tier foundations 1-10 /
compounded 11-21 / advanced 22-34).

Numerical cores: hand-computed 2026-10-17, machine-verified by the demos
(see demos_capacity_growth_forecasting.py). Every demo prints its real
computed values, asserts tight bounds (never float exact-equality), and
ends with the OK marker; the build machine-executes all 68 demos.

Writes (this builder's scope ONLY - a merger handles the rest):
  main repo : db/capacity-growth-forecasting/index.html + gen-...js
              db/capacity-growth-forecasting-signature/index.html + gen-...js
  shard repo: data/capacity-growth-forecasting/index.jsonl.gz + chunks/chunk-0000.jsonl.gz
              data/capacity-growth-forecasting-signature/... (same)
  build dir : code/capacity-growth-forecasting-build/{build.py, entries_*.py, demos_*.py}
  fragment  : ~/workspace/hidden_files/missing-builds/fragments/capacity-growth-forecasting.json

NEVER touches: data/manifest.json, api.json, index.html, README.md,
docs/AI_ACCESS.md. NEVER git commits or pushes.

Never the words "bat belt" anywhere. No website references. No Facebook.
"""''',
"pub_name": "The Capacity Growth Forecasting Database",
"pub_tagline": ("See the future of every database: projected record counts, storage requirements, throughput "
    "estimates, hardware constraints, and forecast histories - the foresight discipline that buys capacity "
    "before it is needed and never after it is too late."),
"pub_record_kind": "growth forecast record",
"pub_prefix": "JAH-CGF-",
"pub_ai": "JAH Growth Forecasting Archivist",
"pub_role": ("Growth forecasting archivist - projecting record counts, storage, throughput, and hardware "
    "constraints with measured accuracy; teaching progressively along the ladder from foundations through "
    "compounded to advanced; answers from many angles - projections, models, scenarios, confidence - using "
    "only archive data from this system"),
"pub_search_ph": "Search projections, capacity models, forecasts, scenarios...",
"pub_chat_ph": "Ask about capacity growth forecasting...",
"pub_archive_blurb": ("Seeded public-record growth forecasting records, marching toward one million records. "
    "Presented in teaching-ladder order: foundations, compounded, advanced."),
"pub_fields": "Foundations \u00b7 Compounded \u00b7 Advanced - each tier opens on demand and loads only what you open",
"pub_gen_desc": "Generate clearly-labeled growth forecast studies. Seeded archive records are the authoritative entries.",
"pub_gen_kind": "forecast-study",
"pub_gen_demo_kind": "forecast-demo",
"pub_greet": ("I am the JAH Growth Forecasting Archivist. Ask me about capacity growth - projections, models, "
    "scenarios, and constraints."),
"sig_name": "The Capacity Growth Forecasting Signature Database",
"sig_tagline": ("The Signature Foresight Doctrine: measure the growth, model the curve, price the future, and "
    "buy the capacity before the cliff - the full ladder from forecasting foundations through simulation to "
    "advanced foresight governance, reframed as Signature science. Clearly labeled Signature-made, never "
    "presented as authentic public record."),
"sig_record_kind": "growth forecast record",
"sig_prefix": "JAH-CGFS-",
"sig_ai": "JAH Growth Forecasting Archivist (Signature)",
"sig_role": ("Growth forecasting archivist - Signature editions: the Signature Foresight Doctrine, clearly "
    "labeled Signature-made and never presented as authentic public record; teaches progressively along "
    "the ladder from foundations through compounded to advanced; answers from many angles using only "
    "archive data from this system"),
"sig_search_ph": "Search projections, capacity models, forecasts, scenarios...",
"sig_chat_ph": "Ask about the Signature foresight doctrine...",
"sig_archive_blurb": ("Seeded Signature-original growth forecasting records, marching toward one million records. "
    "Presented in teaching-ladder order: foundations, compounded, advanced."),
"sig_fields": "Foundations \u00b7 Compounded \u00b7 Advanced - each tier opens on demand and loads only what you open",
"sig_gen_desc": "Generate clearly-labeled Signature forecast studies. Seeded archive records are the authoritative entries.",
"sig_gen_kind": "forecast-study",
"sig_gen_demo_kind": "forecast-demo",
"sig_greet": ("I am the JAH Growth Forecasting Archivist (Signature). Ask me about the Signature Foresight "
    "Doctrine - measure the growth, model the curve, buy before the cliff."),
"pub_line": ("Public records - real, fact-checked forecasting knowledge: record count projection models, "
    "storage requirement forecasting, throughput estimates, hardware constraint mapping, growth rate "
    "measurement, linear projection models, compounding growth models, seasonal growth patterns, forecast "
    "horizon selection, forecast history records, forecast accuracy tracking, capacity headroom policy, "
    "ingestion pipeline capacity, query load forecasting, index growth projection, shard split forecasting, "
    "backfill capacity planning, burst capacity reserves, multi-database fleet forecasting, "
    "forecast-driven procurement, million-database scale projection, logistic (S-curve) growth models, "
    "constraint-bound forecasting, Monte Carlo capacity simulation, what-if scenario modeling, forecast "
    "confidence intervals, capacity cliff detection, decommissioning and shrinkage forecasts, cost-linked "
    "capacity planning, forecast governance, capacity dashboards, and forecast model selection."),
"sig_line": ("Signature originals - the Signature Foresight Doctrine: measure the growth, model the curve, "
    "price the future, and buy the capacity before the cliff; a forecast without a confidence interval is "
    "a wish, and a wish is not a plan. Clearly labeled Signature-made, never presented as authentic "
    "public record."),
"ladder": (" Records are ordered by the teaching ladder: Foundations (forecasting overview, record count "
    "projection, storage requirements, throughput estimates, hardware constraints, growth rate measurement, "
    "linear model, compounding model, seasonal patterns, horizon selection) -> Compounded (forecast history, "
    "accuracy tracking, headroom policy, ingestion capacity, query load, index growth, shard splits, "
    "backfill, burst reserves, fleet forecasting, procurement) -> Advanced (million-scale projection, "
    "logistic model, constraint-bound forecasts, Monte Carlo simulation, scenarios, confidence intervals, "
    "cliff detection, shrinkage, cost-linked planning, governance, dashboards, model selection, self-audit "
    "and mastery)."),
}

PAIRS["database-federation"] = {
"docstring": '''"""Build the Database Federation databases for JAH Databases
(governance track, group F: data governance for a million-database-scale
network, 2026-10-17).

Dedupe gate: none of the 8 governance slugs exist in data/manifest.json
(2,770 databases checked 2026-10-17); no other builder writing these slugs.
ID prefixes JAH-DFED- (public) and JAH-DFEDS- (signature) verified free:
zero exact or substring hits in manifest id_prefix values and zero hits in
all shard record IDs of jah-databases-data-1. (JAH-DBF- was rejected: it
substring-collides with the existing JAH-DB prefix.) All 68 record titles
checked against the WHOLE system (exact dedupe index + live shard title
corpus of 1,143,457 titles) BEFORE authoring.

So this build creates two NEW databases, 34 ladder-ordered records each:

  database-federation            - The Database Federation Database
      (public-harvest: real, fact-checked federation knowledge - federated
      query patterns (scatter-gather, broadcast, chained), cross-database
      join contracts, schema mapping, identity resolution, membership,
      capability advertisement, routing, distributed search architecture,
      result merging, consistency models, federated auth, rate limiting,
      federated caching, partial failure handling, query costing, schema
      evolution, onboarding/offboarding, global optimizer, distributed
      transactions, reconciliation, governance charter, SLAs, provenance,
      analytics pipelines, multi-region topology, security, audits,
      dashboards, anti-patterns)
  database-federation-signature  - The Database Federation Signature Database
      (the Signature Federation Doctrine; src signature, titles suffixed
      " (Signature Edition)", never presented as authentic public record)

34 records each, ladder-ordered 1-34 (ladder_tier foundations 1-10 /
compounded 11-21 / advanced 22-34).

Numerical cores: hand-computed 2026-10-17, machine-verified by the demos
(see demos_database_federation.py). Every demo prints its real computed
values, asserts tight bounds (never float exact-equality), and ends with
the OK marker; the build machine-executes all 68 demos.

Writes (this builder's scope ONLY - a merger handles the rest):
  main repo : db/database-federation/index.html + gen-...js
              db/database-federation-signature/index.html + gen-...js
  shard repo: data/database-federation/index.jsonl.gz + chunks/chunk-0000.jsonl.gz
              data/database-federation-signature/... (same)
  build dir : code/database-federation-build/{build.py, entries_*.py, demos_*.py}
  fragment  : ~/workspace/hidden_files/missing-builds/fragments/database-federation.json

NEVER touches: data/manifest.json, api.json, index.html, README.md,
docs/AI_ACCESS.md. NEVER git commits or pushes.

Never the words "bat belt" anywhere. No website references. No Facebook.
"""''',
"pub_name": "The Database Federation Database",
"pub_tagline": ("Many databases, one query: federated query patterns, cross-database join contracts, "
    "distributed-search architectures, and federation membership - the discipline of asking questions "
    "that no single database can answer alone."),
"pub_record_kind": "federation record",
"pub_prefix": "JAH-DFED-",
"pub_ai": "JAH Federation Archivist",
"pub_role": ("Federation archivist - federated query patterns, join contracts, distributed search, and "
    "membership governance; teaching progressively along the ladder from foundations through compounded "
    "to advanced; answers from many angles - patterns, contracts, topologies, failures - using only "
    "archive data from this system"),
"pub_search_ph": "Search federated queries, join contracts, membership, topologies...",
"pub_chat_ph": "Ask about database federation...",
"pub_archive_blurb": ("Seeded public-record federation records, marching toward one million records. "
    "Presented in teaching-ladder order: foundations, compounded, advanced."),
"pub_fields": "Foundations \u00b7 Compounded \u00b7 Advanced - each tier opens on demand and loads only what you open",
"pub_gen_desc": "Generate clearly-labeled federation studies. Seeded archive records are the authoritative entries.",
"pub_gen_kind": "federation-study",
"pub_gen_demo_kind": "federation-demo",
"pub_greet": ("I am the JAH Federation Archivist. Ask me about database federation - query patterns, join "
    "contracts, distributed search, and membership."),
"sig_name": "The Database Federation Signature Database",
"sig_tagline": ("The Signature Federation Doctrine: many databases, one question, zero confusion - the full "
    "ladder from federation foundations through distributed mechanics to advanced federation governance, "
    "reframed as Signature science. Clearly labeled Signature-made, never presented as authentic public "
    "record."),
"sig_record_kind": "federation record",
"sig_prefix": "JAH-DFEDS-",
"sig_ai": "JAH Federation Archivist (Signature)",
"sig_role": ("Federation archivist - Signature editions: the Signature Federation Doctrine, clearly labeled "
    "Signature-made and never presented as authentic public record; teaches progressively along the ladder "
    "from foundations through compounded to advanced; answers from many angles using only archive data "
    "from this system"),
"sig_search_ph": "Search federated queries, join contracts, membership, topologies...",
"sig_chat_ph": "Ask about the Signature federation doctrine...",
"sig_archive_blurb": ("Seeded Signature-original federation records, marching toward one million records. "
    "Presented in teaching-ladder order: foundations, compounded, advanced."),
"sig_fields": "Foundations \u00b7 Compounded \u00b7 Advanced - each tier opens on demand and loads only what you open",
"sig_gen_desc": "Generate clearly-labeled Signature federation studies. Seeded archive records are the authoritative entries.",
"sig_gen_kind": "federation-study",
"sig_gen_demo_kind": "federation-demo",
"sig_greet": ("I am the JAH Federation Archivist (Signature). Ask me about the Signature Federation Doctrine - "
    "many databases, one question, zero confusion."),
"pub_line": ("Public records - real, fact-checked federation knowledge: federated query patterns "
    "(scatter-gather, broadcast, chained), cross-database join contracts, schema mapping, identity "
    "resolution across databases, federation membership records, capability advertisement, query routing "
    "rules, distributed search architecture, result merging and ranking, consistency models in federation, "
    "federated authentication, rate limiting across members, caching federated results, partial failure "
    "handling, federated query cost estimation, schema evolution in federation, membership onboarding and "
    "offboarding, global query optimizer, distributed transactions, eventual consistency reconciliation, "
    "federation governance charter, inter-member SLA contracts, cross-database provenance, federated "
    "analytics pipelines, multi-region federation topology, federation security model, federation audits, "
    "federation health dashboards, and federation anti-patterns."),
"sig_line": ("Signature originals - the Signature Federation Doctrine: many databases, one question, zero "
    "confusion; a federation is a promise between databases, and promises need contracts, witnesses, and "
    "consequences. Clearly labeled Signature-made, never presented as authentic public record."),
"ladder": (" Records are ordered by the teaching ladder: Foundations (federation overview, scatter-gather, "
    "broadcast, chained patterns, join contracts, schema mapping, identity resolution, membership, "
    "capability advertisement, routing rules) -> Compounded (distributed search, result merging, "
    "consistency models, federated auth, rate limiting, federated caching, partial failure, query costing, "
    "schema evolution, onboarding, offboarding) -> Advanced (global optimizer, distributed transactions, "
    "reconciliation, governance charter, SLAs, provenance, analytics pipelines, multi-region topology, "
    "security model, audit, health dashboard, anti-patterns, self-audit and mastery)."),
}

PAIRS["knowledge-versioning"] = {
"docstring": '''"""Build the Knowledge Versioning databases for JAH Databases
(governance track, group F: data governance for a million-database-scale
network, 2026-10-17).

Dedupe gate: none of the 8 governance slugs exist in data/manifest.json
(2,770 databases checked 2026-10-17); no other builder writing these slugs.
ID prefixes JAH-KV- (public) and JAH-KVS- (signature) verified free: zero
exact or substring hits in manifest id_prefix values and zero hits in all
shard record IDs of jah-databases-data-1. All 68 record titles checked
against the WHOLE system (exact dedupe index + live shard title corpus of
1,143,457 titles) BEFORE authoring.

So this build creates two NEW databases, 34 ladder-ordered records each:

  knowledge-versioning            - The Knowledge Versioning Database
      (public-harvest: real, fact-checked versioning knowledge - semantic
      versioning for knowledge, concept/definition/rule/relationship change
      histories, diffs, deprecation notices, supersession chains, branching,
      merging, rollback, versioned queries, notifications, ontology
      migration, breaking-change policy, compatibility matrices, snapshots,
      cryptographic sealing, distributed consensus, versioned API contracts,
      deprecation analytics, lineage graphs, audits, dashboards,
      anti-patterns)
  knowledge-versioning-signature  - The Knowledge Versioning Signature Database
      (the Signature Version Doctrine; src signature, titles suffixed
      " (Signature Edition)", never presented as authentic public record)

34 records each, ladder-ordered 1-34 (ladder_tier foundations 1-10 /
compounded 11-21 / advanced 22-34).

Numerical cores: hand-computed 2026-10-17, machine-verified by the demos
(see demos_knowledge_versioning.py). Every demo prints its real computed
values, asserts tight bounds (never float exact-equality), and ends with
the OK marker; the build machine-executes all 68 demos.

Writes (this builder's scope ONLY - a merger handles the rest):
  main repo : db/knowledge-versioning/index.html + gen-...js
              db/knowledge-versioning-signature/index.html + gen-...js
  shard repo: data/knowledge-versioning/index.jsonl.gz + chunks/chunk-0000.jsonl.gz
              data/knowledge-versioning-signature/... (same)
  build dir : code/knowledge-versioning-build/{build.py, entries_*.py, demos_*.py}
  fragment  : ~/workspace/hidden_files/missing-builds/fragments/knowledge-versioning.json

NEVER touches: data/manifest.json, api.json, index.html, README.md,
docs/AI_ACCESS.md. NEVER git commits or pushes.

Never the words "bat belt" anywhere. No website references. No Facebook.
"""''',
"pub_name": "The Knowledge Versioning Database",
"pub_tagline": ("Knowledge with a memory: semantic versioning for concepts, definitions, rules, and "
    "relationships - change histories, diffs, and deprecation notices, so nothing the system knows "
    "ever changes silently."),
"pub_record_kind": "versioning record",
"pub_prefix": "JAH-KV-",
"pub_ai": "JAH Versioning Archivist",
"pub_role": ("Knowledge versioning archivist - semantic versioning for knowledge: change histories of "
    "concepts, definitions, rules, and relationships with diffs and deprecation notices; teaching "
    "progressively along the ladder from foundations through compounded to advanced; answers from many "
    "angles - versions, diffs, migrations, compatibility - using only archive data from this system"),
"pub_search_ph": "Search versions, diffs, deprecations, migrations...",
"pub_chat_ph": "Ask about knowledge versioning...",
"pub_archive_blurb": ("Seeded public-record versioning records, marching toward one million records. "
    "Presented in teaching-ladder order: foundations, compounded, advanced."),
"pub_fields": "Foundations \u00b7 Compounded \u00b7 Advanced - each tier opens on demand and loads only what you open",
"pub_gen_desc": "Generate clearly-labeled versioning studies. Seeded archive records are the authoritative entries.",
"pub_gen_kind": "versioning-study",
"pub_gen_demo_kind": "versioning-demo",
"pub_greet": ("I am the JAH Versioning Archivist. Ask me about knowledge versioning - versions, diffs, "
    "deprecations, and migrations."),
"sig_name": "The Knowledge Versioning Signature Database",
"sig_tagline": ("The Signature Version Doctrine: every change recorded, every diff readable, every "
    "deprecation announced - the full ladder from versioning foundations through distributed mechanics to "
    "advanced version governance, reframed as Signature science. Clearly labeled Signature-made, never "
    "presented as authentic public record."),
"sig_record_kind": "versioning record",
"sig_prefix": "JAH-KVS-",
"sig_ai": "JAH Versioning Archivist (Signature)",
"sig_role": ("Knowledge versioning archivist - Signature editions: the Signature Version Doctrine, clearly "
    "labeled Signature-made and never presented as authentic public record; teaches progressively along "
    "the ladder from foundations through compounded to advanced; answers from many angles using only "
    "archive data from this system"),
"sig_search_ph": "Search versions, diffs, deprecations, migrations...",
"sig_chat_ph": "Ask about the Signature version doctrine...",
"sig_archive_blurb": ("Seeded Signature-original versioning records, marching toward one million records. "
    "Presented in teaching-ladder order: foundations, compounded, advanced."),
"sig_fields": "Foundations \u00b7 Compounded \u00b7 Advanced - each tier opens on demand and loads only what you open",
"sig_gen_desc": "Generate clearly-labeled Signature versioning studies. Seeded archive records are the authoritative entries.",
"sig_gen_kind": "versioning-study",
"sig_gen_demo_kind": "versioning-demo",
"sig_greet": ("I am the JAH Versioning Archivist (Signature). Ask me about the Signature Version Doctrine - "
    "every change recorded, every diff readable, every deprecation announced."),
"pub_line": ("Public records - real, fact-checked versioning knowledge: semantic versioning for knowledge, "
    "concept change histories, definition versioning, rule versioning, relationship versioning, version "
    "identifiers and labels, change types (major/minor/patch), version timestamps and provenance, reading "
    "version diffs, concept/definition/rule/relationship diff records, deprecation notices, supersession "
    "chains, version branching, merging divergent versions, rollback procedures, versioned (time-travel) "
    "queries, change notification systems, ontology version migration, breaking change policy, version "
    "compatibility matrices, knowledge graph snapshots, cryptographic version sealing, distributed version "
    "consensus, versioned API contracts, deprecation analytics, knowledge lineage graphs, version audits, "
    "version dashboards, and versioning anti-patterns."),
"sig_line": ("Signature originals - the Signature Version Doctrine: every change recorded, every diff "
    "readable, every deprecation announced; knowledge that changes silently is not knowledge but rumor "
    "with a database. Clearly labeled Signature-made, never presented as authentic public record."),
"ladder": (" Records are ordered by the teaching ladder: Foundations (versioning overview, semantic "
    "versioning, concept history, definition versioning, rule versioning, relationship versioning, "
    "identifiers, change types, timestamps, reading diffs) -> Compounded (concept diff, definition diff, "
    "rule diff, relationship diff, deprecation notices, supersession chains, branching, merging, "
    "rollback, time-travel queries, notifications) -> Advanced (ontology migration, breaking-change "
    "policy, compatibility matrix, snapshots, cryptographic sealing, distributed consensus, API "
    "contracts, deprecation analytics, lineage graph, audit, dashboard, anti-patterns, self-audit and "
    "mastery)."),
}

PAIRS["human-curation-review"] = {
"docstring": '''"""Build the Human Curation Review databases for JAH Databases
(governance track, group F: data governance for a million-database-scale
network, 2026-10-17).

Dedupe gate: none of the 8 governance slugs exist in data/manifest.json
(2,770 databases checked 2026-10-17); no other builder writing these slugs.
ID prefixes JAH-HCR- (public) and JAH-HCRS- (signature) verified free: zero
exact or substring hits in manifest id_prefix values and zero hits in all
shard record IDs of jah-databases-data-1. All 68 record titles checked
against the WHOLE system (exact dedupe index + live shard title corpus of
1,143,457 titles) BEFORE authoring.

So this build creates two NEW databases, 34 ladder-ordered records each:

  human-curation-review            - The Human Curation Review Database
      (public-harvest: real, fact-checked curation knowledge - editorial
      workflows, subject-matter-expert review queues, correction records,
      approval chains, roles, SLAs, taxonomies, standards, onboarding,
      triage, fact-checking, copyediting, disagreement resolution,
      verification, analytics, workload balancing, sampling, escalation,
      feedback, metrics, governance board, bias detection, inter-rater
      reliability, calibration, automation boundaries, controversial topics,
      correction propagation, reputation, audits, incidents, cost models,
      anti-patterns)
  human-curation-review-signature  - The Human Curation Review Signature Database
      (the Signature Curation Doctrine; src signature, titles suffixed
      " (Signature Edition)", never presented as authentic public record)

34 records each, ladder-ordered 1-34 (ladder_tier foundations 1-10 /
compounded 11-21 / advanced 22-34).

Numerical cores: hand-computed 2026-10-17, machine-verified by the demos
(see demos_human_curation_review.py). Every demo prints its real computed
values, asserts tight bounds (never float exact-equality), and ends with
the OK marker; the build machine-executes all 68 demos.

Writes (this builder's scope ONLY - a merger handles the rest):
  main repo : db/human-curation-review/index.html + gen-...js
              db/human-curation-review-signature/index.html + gen-...js
  shard repo: data/human-curation-review/index.jsonl.gz + chunks/chunk-0000.jsonl.gz
              data/human-curation-review-signature/... (same)
  build dir : code/human-curation-review-build/{build.py, entries_*.py, demos_*.py}
  fragment  : ~/workspace/hidden_files/missing-builds/fragments/human-curation-review.json

NEVER touches: data/manifest.json, api.json, index.html, README.md,
docs/AI_ACCESS.md. NEVER git commits or pushes.

Never the words "bat belt" anywhere. No website references. No Facebook.
"""''',
"pub_name": "The Human Curation Review Database",
"pub_tagline": ("People who make knowledge trustworthy: editorial workflows, subject-matter-expert review "
    "queues, correction records, and approval chains - the human layer that automation assists but never "
    "replaces."),
"pub_record_kind": "curation record",
"pub_prefix": "JAH-HCR-",
"pub_ai": "JAH Curation Archivist",
"pub_role": ("Human curation archivist - editorial workflows, SME review queues, correction records, and "
    "approval chains; teaching progressively along the ladder from foundations through compounded to "
    "advanced; answers from many angles - workflows, quality, governance, cost - using only archive data "
    "from this system"),
"pub_search_ph": "Search editorial workflows, review queues, corrections, approvals...",
"pub_chat_ph": "Ask about human curation review...",
"pub_archive_blurb": ("Seeded public-record curation records, marching toward one million records. "
    "Presented in teaching-ladder order: foundations, compounded, advanced."),
"pub_fields": "Foundations \u00b7 Compounded \u00b7 Advanced - each tier opens on demand and loads only what you open",
"pub_gen_desc": "Generate clearly-labeled curation studies. Seeded archive records are the authoritative entries.",
"pub_gen_kind": "curation-study",
"pub_gen_demo_kind": "curation-demo",
"pub_greet": ("I am the JAH Curation Archivist. Ask me about human curation - editorial workflows, review "
    "queues, corrections, and approvals."),
"sig_name": "The Human Curation Review Signature Database",
"sig_tagline": ("The Signature Curation Doctrine: automation proposes, humans dispose - the full ladder from "
    "curation foundations through quality mechanics to advanced editorial governance, reframed as Signature "
    "science. Clearly labeled Signature-made, never presented as authentic public record."),
"sig_record_kind": "curation record",
"sig_prefix": "JAH-HCRS-",
"sig_ai": "JAH Curation Archivist (Signature)",
"sig_role": ("Human curation archivist - Signature editions: the Signature Curation Doctrine, clearly "
    "labeled Signature-made and never presented as authentic public record; teaches progressively along "
    "the ladder from foundations through compounded to advanced; answers from many angles using only "
    "archive data from this system"),
"sig_search_ph": "Search editorial workflows, review queues, corrections, approvals...",
"sig_chat_ph": "Ask about the Signature curation doctrine...",
"sig_archive_blurb": ("Seeded Signature-original curation records, marching toward one million records. "
    "Presented in teaching-ladder order: foundations, compounded, advanced."),
"sig_fields": "Foundations \u00b7 Compounded \u00b7 Advanced - each tier opens on demand and loads only what you open",
"sig_gen_desc": "Generate clearly-labeled Signature curation studies. Seeded archive records are the authoritative entries.",
"sig_gen_kind": "curation-study",
"sig_gen_demo_kind": "curation-demo",
"sig_greet": ("I am the JAH Curation Archivist (Signature). Ask me about the Signature Curation Doctrine - "
    "automation proposes, humans dispose."),
"pub_line": ("Public records - real, fact-checked curation knowledge: editorial workflow stages, "
    "subject-matter-expert review queues, correction records, approval chains, reviewer roles and "
    "permissions, review SLAs, correction taxonomy, editorial standards, reviewer onboarding, triage and "
    "prioritization, fact-check procedures, copyediting standards, SME disagreement resolution, "
    "correction verification, approval chain analytics, reviewer workload balancing, quality sampling, "
    "escalation procedures, reviewer feedback loops, curation metrics, editorial governance board, bias "
    "detection in reviews, inter-rater reliability, calibration sessions, review automation boundaries, "
    "controversial topic handling, correction propagation, reviewer reputation systems, curation audits, "
    "editorial incident response, curation cost models, and curation anti-patterns."),
"sig_line": ("Signature originals - the Signature Curation Doctrine: automation proposes, humans dispose; "
    "the machine's speed serves the human's judgment, never the reverse. Clearly labeled Signature-made, "
    "never presented as authentic public record."),
"ladder": (" Records are ordered by the teaching ladder: Foundations (curation overview, workflow stages, "
    "SME queues, correction records, approval chains, roles, SLAs, correction taxonomy, editorial "
    "standards, reviewer onboarding) -> Compounded (triage, fact-checking, copyediting, disagreement "
    "resolution, correction verification, chain analytics, workload balancing, quality sampling, "
    "escalation, feedback loops, metrics dashboard) -> Advanced (governance board, bias detection, "
    "inter-rater reliability, calibration, automation boundaries, controversial topics, correction "
    "propagation, reputation system, audit, incident response, cost model, anti-patterns, self-audit and "
    "mastery)."),
}
