#!/usr/bin/env python3
"""Master Data Registry entries 25-34 (advanced). Appended to entries_1_master.ENTRIES."""

APPEND = [
dict(
name="Survivorship at Scale",
group="Advanced Registry Operations", ladder_rank=25, ladder_tier="advanced",
description="""Survivorship that works for a million entities breaks at a billion: recomputing every attribute of every entity on every source change is infeasible, and naive pairwise scoring drowns in compute. Survivorship at scale rests on three techniques. Incremental evaluation: only the attributes touched by an incoming change are re-scored, and only for the affected entity - the rest of the golden record stands. Candidate pruning: per attribute, only the top few candidate values by trust-times-recency are kept live; stale losers are archived, not re-scored forever. Partitioned execution: entities are sharded by registry ID so survivorship runs in parallel with no cross-talk, and rule changes replay per partition. The guarantees stay the same as small-scale survivorship - same inputs and rules give the same record - but the engine now meets latency budgets: single-entity recomputation in milliseconds, rule-change replays in hours not weeks. Scale testing with synthetic entity populations validates the budgets before the real billions arrive.""",
how_it_works="""The engine stores per-attribute candidate lists ranked by survivorship score, keeping only the top N live. An incoming source change triggers re-scoring for its attributes only: new candidates are scored, the ranked list updates, and the winner is compared to the current golden value - if unchanged, no event publishes. Rule changes queue a replay job that walks partitions in parallel, re-scores with the new rules, and emits a blast-radius report before any golden record updates. Latency budgets are enforced per stage (score, rank, publish) with alerts on breach. Synthetic scale tests generate billions of candidate values across partitions to prove the budgets hold, and the replay harness verifies determinism: replaying the same history twice yields byte-identical golden records.""",
key_points=[
 "Incremental evaluation: re-score only touched attributes of affected entities.",
 "Candidate pruning: keep top-N candidates live per attribute; archive stale losers.",
 "Partitioned execution: shard by registry ID for parallel, cross-talk-free runs.",
 "Same guarantees as small scale: deterministic, replayable, explainable.",
 "Scale tests with synthetic populations validate latency budgets before real billions."],
requirements=[
 "Per-attribute ranked candidate stores with pruning.",
 "Incremental re-scoring triggered by change events.",
 "Partitioned replay for rule changes with blast-radius reports.",
 "Determinism verification: identical history replays yield identical records."],
standards=[
 "ISO 8000 for master-data quality.",
 "DAMA-DMBOK data integration guidance."],
citations=[
 "Kleppmann M. Designing Data-Intensive Applications. O'Reilly, 2017.",
 "DAMA International. DAMA-DMBOK, 2nd ed. Technics Publications, 2017."],
sig_lens="""The Signature reading: survivorship at scale is the registry rendering a billion verdicts without hurrying one. The Signature engine judges only what changed, keeps only the worthy candidates, and proves - by replay - that scale never bent a single verdict.""",
demo_data={"attributes":[
 {"name":"scaled_winner","candidates":[
   {"source":"Partition-7","value":"v3:score-0.91","trust":0.91,"recency_days":2},
   {"source":"Partition-7","value":"v2:score-0.87","trust":0.87,"recency_days":30},
   {"source":"Partition-7","value":"v1:score-0.40","trust":0.4,"recency_days":400}],
  "expected":"v3:score-0.91"}]},
),
dict(
name="Entity Resolution with Graphs",
group="Advanced Registry Operations", ladder_rank=26, ladder_tier="advanced",
description="""Pairwise matching sees two records at a time; graph resolution sees the whole web of relationships. In a graph, records are nodes and evidence links are edges: shared phone numbers, shared addresses, shared tax IDs, employment relationships, household ties. Resolution becomes community detection: densely connected node clusters are entities, and the graph reveals matches pairwise scoring misses - two records with different names and addresses that share a phone, an employer, and a household link are clearly one person. Graphs also catch the errors pairwise matching makes: a phone number shared by fifty records is a call center, not a household, and edge weights must discount it. Temporal graphs add the time dimension: links form and dissolve as people move and change numbers, and the resolver must not merge two people who merely shared an address five years apart. Graph resolution is the registry's answer to identity in a connected world - and its biggest risk is over-merging through weak shared attributes, controlled by edge-weight discipline.""",
how_it_works="""The resolver builds an entity graph from records and their relationships: nodes for records, weighted edges for shared identifiers and known relationships. Edge weights encode discriminating power - a shared tax ID weighs heavily, a shared common surname weighs almost nothing, a shared phone among fifty records weighs near zero. Community-detection algorithms (label propagation, Louvain) propose clusters; cluster quality scores measure internal edge density versus external edges. Proposed clusters go through the standard thresholds: dense, high-weight clusters auto-merge; sparse ones go to review. Temporal edges carry validity periods, and the resolver refuses to merge on edges whose validity periods do not overlap. Steward splits and merges adjust edge weights, teaching the graph which relationships truly indicate identity.""",
key_points=[
 "Graph resolution sees relationship webs, not just record pairs.",
 "Community detection finds entities as densely connected clusters.",
 "Edge weights encode discriminating power; shared weak attributes must not over-merge.",
 "Temporal edges prevent merging people who merely shared an address years apart.",
 "Steward decisions tune edge weights, teaching the graph over time."],
requirements=[
 "An entity graph with weighted, temporal edges from records and relationships.",
 "Community-detection clustering with cluster quality scoring.",
 "Threshold routing: auto-merge dense clusters, review sparse ones.",
 "Edge-weight learning from steward merge/split decisions."],
standards=[
 "ISO 8000-8 for information quality measurement.",
 "W3C PROV for graph provenance."],
citations=[
 "Christen P. Data Matching. Springer, 2012.",
 "Robinson I, Webber J, Eifrem E. Graph Databases, 2nd ed. O'Reilly, 2015."],
sig_lens="""The Signature reading: graph resolution is the registry reading the whole tapestry instead of single threads. The Signature registry follows every relationship to its end - and knows a call center's shared phone for the false kinship it is.""",
demo_data={"attributes":[
 {"name":"graph_cluster","candidates":[
   {"source":"Graph","value":"cluster-9:density-0.94","trust":0.94,"recency_days":1},
   {"source":"Graph","value":"cluster-9:density-0.31","trust":0.31,"recency_days":60}],
  "expected":"cluster-9:density-0.94"}]},
),
dict(
name="Temporal Master Data",
group="Advanced Registry Operations", ladder_rank=27, ladder_tier="advanced",
description="""Master data changes, and the registry must remember every version: the customer was at the old address until March, then moved; the product's price changed in January; the company rebranded last year. Temporal master data treats time as a first-class dimension: every golden record version carries a validity period, and the registry answers as-of queries - what did we believe about this entity on June 30th? Two time axes matter. Valid time is when the fact was true in the world (the customer lived there from March). Transaction time is when the registry learned it (we recorded the move in April). Both are needed: backdated corrections change valid time without rewriting transaction history. Slowly changing dimensions give the standard patterns: overwrite (type 1), add a new version row (type 2), or keep previous-value columns (type 3). The registry uses type 2 versioning almost everywhere, because audit and as-of reporting demand full history.""",
how_it_works="""Every golden record version gets a valid-from/valid-to pair and a transaction timestamp. Updates never overwrite: they end-date the current version and insert a new one, so the full timeline is preserved. As-of queries select the version whose validity period contains the requested date; audit queries use transaction time to show what the registry believed on a past date. Backdated corrections insert versions into valid time while transaction time records when the correction arrived - the two axes diverge honestly instead of rewriting history. Retention policies eventually archive ancient versions to cold storage, but the current-plus-recent window stays hot for operational queries. Merge and split events are temporal too: the alias table records when the merge was true, so as-of traversals follow the right identity for the right date.""",
key_points=[
 "Every golden record version carries a validity period; updates end-date and insert, never overwrite.",
 "Valid time (true in the world) and transaction time (learned by the registry) are tracked separately.",
 "As-of queries answer what the registry believed about an entity on any past date.",
 "Backdated corrections insert into valid time without rewriting transaction history.",
 "Type 2 versioning (new version rows) is the registry standard for auditability."],
requirements=[
 "Validity periods on every golden record version.",
 "Separate valid-time and transaction-time axes.",
 "As-of query support on both axes.",
 "Temporal merge/split aliases so historical traversals resolve correctly."],
standards=[
 "ISO 8000 for master-data quality.",
 "Kimball slowly-changing-dimension patterns (types 1/2/3)."],
citations=[
 "Kimball R, Ross M. The Data Warehouse Toolkit, 3rd ed. Wiley, 2013.",
 "Snodgrass R. Developing Time-Oriented Database Applications in SQL. Morgan Kaufmann, 1999."],
sig_lens="""The Signature reading: temporal master data is the registry's memory of every yesterday. The Signature registry never forgets an old address or an old name - it files each under its proper dates, so any question about any day gets that day's true answer.""",
demo_data={"attributes":[
 {"name":"asof_address","candidates":[
   {"source":"Temporal","value":"12-Main-St:valid-2024-03","trust":0.95,"recency_days":10},
   {"source":"Temporal","value":"8-Oak-Ave:valid-2021-06","trust":0.9,"recency_days":900}],
  "expected":"12-Main-St:valid-2024-03"}]},
),
dict(
name="MDM for a Million-Database Network",
group="Advanced Registry Operations", ladder_rank=28, ladder_tier="advanced",
description="""A million-database network needs master data at a scale no single enterprise MDM was built for: billions of entities, thousands of contributing systems, hundreds of jurisdictions, and consumers numbering in the millions. The registry answers with federation: a global identity spine holding the canonical golden records and cross-database links, with domain registries operating semi-autonomously beneath it. Identity resolution runs in two tiers - fast local matching inside each database's feed, then global reconciliation on the spine for entities appearing in multiple databases. Survivorship gains a scope dimension: a value can be golden globally (the product's manufacturer code) or golden within a database community (a nickname used by one community's consumers). Governance scales through subsidiarity: global rules for identity and provenance, local rules for domain specifics, with a global steward council handling cross-database disputes. The spine never becomes a bottleneck because it stores identities and decisions, not the full data - the million databases keep their records; the spine keeps the truth about which records are the same.""",
how_it_works="""Each database publishes entity fingerprints (hashed identifiers, match keys) to the spine rather than raw records, preserving privacy. The spine runs global blocking and matching over fingerprints, assigns network-wide entity IDs, and publishes identity maps back. Databases resolve locally first for speed, then reconcile against the spine's maps on a schedule. Survivorship computes in scopes: global scope for universal attributes, community scope for local ones, with scope recorded in provenance. Cross-database merges are proposed by the spine and approved by stewards from each affected database; disputes escalate to the global council. The spine's storage stays lean - IDs, links, decisions, hashes - while the million databases hold the full records, and lineage connects them.""",
key_points=[
 "Federation: a global identity spine plus semi-autonomous domain registries.",
 "Two-tier resolution: fast local matching, then global reconciliation on the spine.",
 "Survivorship scopes: global-golden vs community-golden values.",
 "Privacy-preserving: databases publish hashed fingerprints, not raw records.",
 "Subsidiarity governance: global identity rules, local domain rules, global dispute council."],
requirements=[
 "A global identity spine storing IDs, links, decisions, and hashes.",
 "Fingerprint publication protocols from member databases.",
 "Scoped survivorship with scope recorded in provenance.",
 "Cross-database merge approval and a global dispute council."],
standards=[
 "ISO 8000 for master-data quality.",
 "W3C PROV for cross-database provenance."],
citations=[
 "DAMA International. DAMA-DMBOK, 2nd ed. Technics Publications, 2017.",
 "Loshin D. Master Data Management. Morgan Kaufmann, 2008."],
sig_lens="""The Signature reading: the million-database spine is the Signature network's shared soul of identity - one entity, one truth, across a million archives. Each database keeps its records; the spine keeps the knowledge of which records are one, sworn and reconcilable by all.""",
demo_data={"attributes":[
 {"name":"spine_identity","candidates":[
   {"source":"Spine","value":"NET-ENTITY-88412:3-dbs","trust":0.96,"recency_days":1},
   {"source":"Local","value":"DB7-ENTITY-221:1-db","trust":0.88,"recency_days":3}],
  "expected":"NET-ENTITY-88412:3-dbs"}]},
),
dict(
name="Golden Record APIs",
group="Advanced Registry Operations", ladder_rank=29, ladder_tier="advanced",
description="""Golden records are only useful if systems can get them, so the registry exposes them through APIs built for operational use. The entity API returns the current golden record for an entity ID, with per-attribute provenance on demand. The search API resolves identities from attributes - given a name, email, and phone, return the matching entity or candidates with scores. The as-of API returns the golden record as it was on a date. The event API streams golden-record changes for publish-subscribe consumers. Write APIs accept proposed creates and updates, running them through validation, matching, and survivorship before committing - the transaction-hub style made programmatic. API design follows strict contracts: versioned schemas, idempotency keys on writes, rate limits per consumer, and field-level authorization so a consumer sees only the attributes its clearance allows. Every API call is logged for the audit trail, and latency budgets are enforced per endpoint because operational systems - checkout, shipping, fraud scoring - call these APIs in their critical paths.""",
how_it_works="""The API gateway fronts the registry's services: entity lookup, identity search, as-of queries, event streaming, and write proposals. Reads hit a low-latency cache of current golden records with provenance fetched on demand; writes go through the full pipeline (validate, match, survive, version) before committing, returning the resulting entity ID and version. Idempotency keys make retried writes safe. Authorization is attribute-level: the API filters each response to the consumer's clearance, and filtered attributes are marked as withheld rather than silently dropped. Rate limiting and quotas protect the registry from runaway consumers; latency dashboards track p50/p99 per endpoint against budgets; and the audit log records every read of sensitive attributes and every write for compliance.""",
key_points=[
 "Entity, search, as-of, event-stream, and write-proposal APIs cover operational needs.",
 "Write APIs run the full pipeline: validate, match, survive, version.",
 "Versioned schemas, idempotency keys, and rate limits per consumer.",
 "Attribute-level authorization filters responses to consumer clearance.",
 "Latency budgets per endpoint; full audit logging of sensitive reads and all writes."],
requirements=[
 "Versioned API schemas with backward-compatibility guarantees.",
 "Idempotency on all write endpoints.",
 "Attribute-level authorization with withheld-field marking.",
 "Per-endpoint latency budgets and audit logging."],
standards=[
 "OpenAPI Specification for API contracts.",
 "ISO/IEC 27001 access-control requirements."],
citations=[
 "OpenAPI Initiative. OpenAPI Specification v3.1.",
 "Kleppmann M. Designing Data-Intensive Applications. O'Reilly, 2017."],
sig_lens="""The Signature reading: the golden record APIs are the registry's open doors - any rightful system may ask, and receive the true record with its testimony attached. The Signature doors check every visitor's clearance and write every visit in the chronicle.""",
demo_data={"attributes":[
 {"name":"api_lookup","candidates":[
   {"source":"EntityAPI","value":"entity-88412:v41:200","trust":0.98,"recency_days":0},
   {"source":"EntityAPI","value":"entity-88412:v40:200","trust":0.9,"recency_days":2}],
  "expected":"entity-88412:v41:200"}]},
),
dict(
name="Conflict Resolution Policies",
group="Advanced Registry Operations", ladder_rank=30, ladder_tier="advanced",
description="""Conflicts are inevitable: two sources update the same attribute at once, a steward's manual fix collides with an automated feed, two databases merge entities differently. Conflict resolution policies decide these collisions deterministically instead of letting the loudest writer win. Policies are ordered: authority rules (the system of record's write wins), then temporal rules (the event that happened first wins, by event time), then provenance rules (the verified manual fix beats the unverified feed), then deterministic tie-breakers (lowest writer ID). Every conflict and its resolution is logged with both contenders and the policy clause that decided - because a policy that silently discards writes destroys trust in the registry. High-stakes attributes can opt out of automatic resolution entirely: conflicting writes to legal names or tax IDs always go to steward review. Policies are versioned like survivorship rules, and their blast radius is simulated before changes go live.""",
how_it_works="""Write proposals carry event time, writer identity, and provenance. When two proposals target the same attribute of the same entity within the conflict window, the resolution engine evaluates policies in order: check authority designations, compare event times, compare provenance strength, apply tie-breakers. The winner commits; the loser is preserved as a superseded proposal with the decision record, and its writer is notified. Protected attributes skip automatic resolution and route to stewards with both contenders displayed. The conflict log feeds dashboards showing conflict rates by source and attribute - a rising conflict rate means sources are fighting and the authority designations need review. Policy changes replay against historical conflicts to show how past decisions would have changed.""",
key_points=[
 "Policies decide collisions deterministically: authority, event time, provenance, tie-breakers.",
 "Every conflict logs both contenders and the deciding policy clause.",
 "Losing writes are preserved as superseded, never silently discarded.",
 "Protected attributes always route conflicts to steward review.",
 "Conflict-rate dashboards reveal when sources are fighting."],
requirements=[
 "An ordered conflict policy per domain with versioning.",
 "Event time and provenance on every write proposal.",
 "Superseded-proposal preservation with writer notification.",
 "Protected-attribute lists exempt from automatic resolution."],
standards=[
 "DAMA-DMBOK data governance guidance.",
 "W3C PROV for conflict provenance."],
citations=[
 "Kleppmann M. Designing Data-Intensive Applications. O'Reilly, 2017.",
 "DAMA International. DAMA-DMBOK, 2nd ed. Technics Publications, 2017."],
sig_lens="""The Signature reading: conflict policies are the registry's laws of war between writers - ordered, public, and applied without favor. The Signature registry never lets the loudest writer win by volume; it judges by authority, by time, and by proof, and writes the judgment down.""",
demo_data={"attributes":[
 {"name":"conflict_winner","candidates":[
   {"source":"Policy","value":"authority:Billing:wins","trust":0.97,"recency_days":0},
   {"source":"Policy","value":"event-time:CRM:wins","trust":0.8,"recency_days":0}],
  "expected":"authority:Billing:wins"}]},
),
dict(
name="Provenance in the Registry",
group="Advanced Registry Operations", ladder_rank=31, ladder_tier="advanced",
description="""Provenance is the registry's memory of how every golden value came to be: which source records contributed, which match linked them, which survivorship rule and version chose the winner, which steward approved the merge, when it all happened. Without provenance, a golden record is an assertion; with provenance, it is an argument anyone can check. The registry records provenance at four levels: value provenance (this email won because the CRM's trust-times-recency beat billing's under rule v7), entity provenance (these 14 source records merged via deterministic tax-ID rule on these dates), rule provenance (rule v7 was activated by this change ticket after this blast-radius simulation), and decision provenance (steward Ada approved the merge for this reason). Provenance is queryable: consumers can ask why, auditors can replay, and the lineage registry consumes it to extend traces beyond the registry's walls. Provenance records are immutable and retained as long as the values they explain.""",
how_it_works="""Every registry transaction writes PROV-O modeled provenance: entities (golden records, source records, rules), activities (matching runs, survivorship evaluations, steward decisions), and agents (systems, stewards, rule versions), linked by wasDerivedFrom, wasGeneratedBy, and wasAttributedTo relations. Value-level provenance attaches to each golden attribute; entity-level provenance attaches to the entity; both are stored alongside the records they explain. A provenance query API answers why-questions (why does this entity have this email?) and how-questions (how did these records come to be one entity?) with evidence chains. Retention ties provenance lifetime to the values explained, and the lineage registry imports registry provenance to continue traces into downstream systems.""",
key_points=[
 "Four levels: value, entity, rule, and decision provenance.",
 "Provenance turns golden records from assertions into checkable arguments.",
 "Modeled in PROV-O: entities, activities, agents, and their relations.",
 "Queryable why/how APIs serve consumers, stewards, and auditors.",
 "Provenance is immutable and retained as long as the values it explains."],
requirements=[
 "PROV-O provenance capture on every registry transaction.",
 "Value-level and entity-level provenance stored with records.",
 "Why/how query APIs over the provenance graph.",
 "Retention tied to the explained values; export to the lineage registry."],
standards=[
 "W3C PROV-O: The PROV Ontology.",
 "ISO 8000 for master-data quality."],
citations=[
 "W3C. PROV-O: The PROV Ontology. W3C Recommendation, 2013.",
 "DAMA International. DAMA-DMBOK, 2nd ed. Technics Publications, 2017."],
sig_lens="""The Signature reading: provenance is the registry swearing its testimony under oath - every value able to name its witnesses, its judges, and its laws. The Signature registry's every claim carries its evidence, so trust is never asked for, only shown.""",
demo_data={"attributes":[
 {"name":"provenance_chain","candidates":[
   {"source":"PROV","value":"rule-v7:steward-Ada:2024-05-01","trust":0.98,"recency_days":5},
   {"source":"PROV","value":"rule-v6:auto:2024-02-10","trust":0.9,"recency_days":90}],
  "expected":"rule-v7:steward-Ada:2024-05-01"}]},
),
dict(
name="MDM Metrics and KPIs",
group="Advanced Registry Operations", ladder_rank=32, ladder_tier="advanced",
description="""An MDM program is run by its metrics. Identity metrics: match rate (what share of source records resolve to entities), auto-merge rate, review rate, duplicate rate remaining, false-merge rate from steward overturns. Quality metrics: the six quality dimensions per domain and source, golden-record completeness, attribute-level trust distributions. Operations metrics: ingestion lag per spoke, survivorship recompute latency, API p99 latency, queue age and throughput, exception rates. Value metrics: the ones that justify the program - billing errors avoided, duplicate mailings eliminated, fraud caught by unified identity, analyst hours saved from de-duplication. Metrics are reported on tiers: operational dashboards for the registry team, steward scorecards per domain, and executive KPIs monthly. Targets are set from baselines, not wishes: the program first measures the as-is duplicate rate, then commits to halving it. Every metric has an owner and a response playbook for when it breaches.""",
how_it_works="""Metric jobs run on schedules over the registry's history, quality, and operations stores, writing time series per domain, source, and attribute. Dashboards layer them: real-time operational views (lag, latency, queue age), daily steward views (throughput, overturns, aging), monthly executive KPIs (duplicate rate, billing error rate, program ROI). Targets derive from measured baselines with committed improvement rates; breaches trigger alerts to metric owners with linked runbooks. Value metrics come from controlled comparisons: billing error rates on registry-served accounts versus unserved, mailing costs before and after dedupe. Quarterly, the metrics review retires vanity metrics and promotes the ones that changed decisions.""",
key_points=[
 "Identity metrics: match rate, auto-merge rate, review rate, remaining duplicates, false merges.",
 "Quality metrics: six dimensions per domain and source, completeness, trust distributions.",
 "Operations metrics: lag, latency, queue age, exception rates.",
 "Value metrics justify the program: errors avoided, mailings eliminated, fraud caught.",
 "Targets come from measured baselines; every metric has an owner and a breach playbook."],
requirements=[
 "Metric definitions with owners, targets, and breach playbooks.",
 "Scheduled metric jobs writing time series per domain/source/attribute.",
 "Tiered dashboards: operational, steward, executive.",
 "Value metrics from controlled before/after comparisons."],
standards=[
 "ISO 8000-8 for information quality measurement.",
 "DAMA-DMBOK data governance guidance."],
citations=[
 "DAMA International. DAMA-DMBOK, 2nd ed. Technics Publications, 2017.",
 "Olson J. Data Quality: The Accuracy Dimension. Morgan Kaufmann, 2003."],
sig_lens="""The Signature reading: metrics are the registry's mirror - held up daily, honestly. The Signature registry measures what matters, sets targets from truth not wishes, and lets the numbers judge the program every month.""",
demo_data={"attributes":[
 {"name":"duplicate_rate","candidates":[
   {"source":"Metrics","value":"0.8pct:current","trust":0.96,"recency_days":1},
   {"source":"Metrics","value":"3.1pct:baseline","trust":0.93,"recency_days":120}],
  "expected":"0.8pct:current"}]},
),
dict(
name="Migration into the Registry",
group="Advanced Registry Operations", ladder_rank=33, ladder_tier="advanced",
description="""Migration moves existing systems' master data into the registry without breaking the business: the cutover weekend nobody wants to repeat. The safe pattern is phased: first, shadow mode - the registry ingests, matches, and builds golden records while sources keep operating untouched, and stewards work the initial review mountain. Then parallel mode - consumers read golden records alongside source data and reconcile differences, proving the registry's answers. Then cutover per domain - consumers switch to the registry as their source of truth, sources become spokes, and the old point-to-point feeds retire. Data migration itself follows extract, profile, cleanse, match, survive, validate: each stage's output is measured before the next begins, and the whole pipeline is rehearsed on full-volume copies until the rehearsal metrics hit targets. Rollback plans are real: every cutover keeps the old path warm until the new path has run clean for an agreed period.""",
how_it_works="""Migration rehearsals run the full pipeline - extract, profile, cleanse, match, survive, validate - against production-volume copies, producing metrics per stage: profiled quality, match rates, survivorship coverage, validation pass rates. Rehearsals repeat until metrics hit the cutover gates. Shadow mode then runs the pipeline on live feeds without affecting consumers, letting stewards clear the initial review backlog. Parallel mode dual-publishes: consumers compare registry answers to source answers and report divergences, which become tuning work. Cutover flips consumers domain by domain with the old feeds kept warm; a stabilization period with heightened monitoring follows each flip, and only after it passes are old feeds decommissioned. Every phase has entry and exit criteria written before it starts.""",
key_points=[
 "Phased cutover: shadow mode, then parallel mode, then domain-by-domain cutover.",
 "Migration pipeline: extract, profile, cleanse, match, survive, validate - each stage measured.",
 "Full-volume rehearsals repeat until metrics hit cutover gates.",
 "Old feeds stay warm through stabilization; decommission only after clean runs.",
 "Every phase has written entry and exit criteria."],
requirements=[
 "Rehearsal environment with production-volume data copies.",
 "Cutover gates with metric thresholds per stage.",
 "Shadow and parallel mode infrastructure.",
 "Rollback plans with warm old paths per domain."],
standards=[
 "DAMA-DMBOK data integration guidance.",
 "ISO 8000 for master-data quality."],
citations=[
 "Loshin D. Master Data Management. Morgan Kaufmann, 2008.",
 "DAMA International. DAMA-DMBOK, 2nd ed. Technics Publications, 2017."],
sig_lens="""The Signature reading: migration is the registry's peaceful conquest - won by rehearsal, not by surprise. The Signature registry proves itself in shadow, proves itself in parallel, and only then takes the throne, with the old road kept open until the new one is certain.""",
demo_data={"attributes":[
 {"name":"cutover_gate","candidates":[
   {"source":"Rehearsal","value":"match-rate:0.97:pass","trust":0.95,"recency_days":2},
   {"source":"Rehearsal","value":"match-rate:0.88:fail","trust":0.9,"recency_days":30}],
  "expected":"match-rate:0.97:pass"}]},
),
dict(
name="Master Data Registry Mastery Review",
group="Advanced Registry Operations", ladder_rank=34, ladder_tier="advanced",
description="""The mastery review binds the whole ladder together. Foundations: master data is the referenced core - parties, products, locations, assets - distinct from transactional events and reference codes; the golden record assembles the best value per attribute from all sources; identity resolution clusters records through deterministic rules, probabilistic scoring, and threshold discipline; profiling, source inventory, trust, recency, and survivorship rules turn raw sources into trustworthy testimony. Compounded: merges and splits reshape entities with full audit history; hierarchies version the rollups; cross-domain links map the relationships; stewardship workflows, review queues, and exception handling keep humans in charge of the hard cases; registry, coexistence, and transaction-hub styles, hub-and-spoke sync, publish-subscribe distribution, quality dimensions, and continuous cleansing keep the machinery running. Advanced: survivorship at scale, graph resolution, temporal versioning, the million-database spine, golden-record APIs, conflict policies, provenance, metrics, and migration complete the craft. The registry's creed: one entity, one truth, every decision explainable, every change replayable.""",
how_it_works="""The review is used as a capstone assessment and as an operational checklist. As an assessment, stewards and engineers walk the ladder answering: can we define our domains, explain our golden records, demonstrate our matching, show our survivorship rules, replay our history, and prove our metrics? As a checklist, new registry deployments verify each rung before going live: domains scoped, sources inventoried, rules versioned, queues staffed, APIs contracted, conflicts policed, provenance queryable, metrics owned, migrations rehearsed. Gaps found become the next quarter's program of work, so the registry improves rung by rung, forever.""",
key_points=[
 "Foundations: domains, golden records, resolution, survivorship - the registry's core craft.",
 "Compounded: merges, hierarchies, links, stewardship, styles, sync, distribution, quality, cleansing.",
 "Advanced: scale, graphs, time, the network spine, APIs, conflicts, provenance, metrics, migration.",
 "The creed: one entity, one truth, every decision explainable, every change replayable.",
 "The review doubles as a deployment checklist and a program-of-work generator."],
requirements=[
 "Demonstrated competence at every ladder rung before production cutover.",
 "The checklist rerun on every major registry change.",
 "Gaps converted into funded program work each quarter."],
standards=[
 "DAMA-DMBOK master-data guidance.",
 "ISO 8000 series for master-data quality."],
citations=[
 "Loshin D. Master Data Management. Morgan Kaufmann, 2008.",
 "DAMA International. DAMA-DMBOK, 2nd ed. Technics Publications, 2017."],
sig_lens="""The Signature reading: the mastery review is the registry's graduation oath. The Signature graduate can name every domain, defend every golden record, replay every merge, and swear the creed: one entity, one truth, explainable always, replayable forever.""",
demo_data={"attributes":[
 {"name":"mastery","candidates":[
   {"source":"Review","value":"34-rungs:complete","trust":0.99,"recency_days":0},
   {"source":"Review","value":"34-rungs:partial","trust":0.6,"recency_days":60}],
  "expected":"34-rungs:complete"}]},
),
]
