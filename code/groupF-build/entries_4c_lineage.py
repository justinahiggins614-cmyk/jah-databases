#!/usr/bin/env python3
"""Data Lineage Registry entries 25-34 (advanced)."""

APPEND = [
dict(
name="Fine-Grained Lineage",
group="Advanced Lineage Topics", ladder_rank=25, ladder_tier="advanced",
description="""Fine-grained lineage traces data below the column: which rows, which array elements, which JSON fields contributed to an output. A fraud score's lineage at fine grain shows it came from these three transactions' amounts, not just the transactions table's amount column. The techniques are taint tracking (labels follow values through transformations), provenance polynomials (algebraic expressions of input contributions), and per-key lineage in streaming (this output key came from these input keys). The cost is real - fine-grained lineage multiplies storage and capture overhead - so it is deployed where the value justifies it: regulated calculations that must show their exact inputs, ML features that must document training rows, and debugging of the hardest data bugs. The registry supports fine grain as an overlay: the coarse graph stays complete, and fine-grained traces attach to the edges that need them, queryable on demand rather than materialized everywhere.""",
how_it_works="""Capture integrations support fine-grained modes: taint labels propagated by instrumented engines, provenance polynomials emitted by database engines that support them, per-key lineage from streaming state. The registry stores fine-grained traces as edge attachments, indexed by output for on-demand queries. Query APIs answer which-inputs-contributed for a specific output value with the contributing inputs ranked. Retention is shorter than coarse lineage - fine grain ages out unless pinned by investigation or regulation. Cost dashboards show the overhead per pipeline, letting teams choose fine grain only where it pays.""",
key_points=[
 "Fine-grained lineage traces rows, array elements, JSON fields - below the column.",
 "Techniques: taint tracking, provenance polynomials, per-key streaming lineage.",
 "Deployed where value justifies cost: regulated calculations, ML features, hard bugs.",
 "Overlay model: coarse graph complete, fine traces attached on demand.",
 "Cost dashboards guide where fine grain pays."],
requirements=[
 "Fine-grained capture modes in instrumented engines.",
 "Edge-attached trace storage with on-demand queries.",
 "Shorter retention with investigation pinning.",
 "Cost monitoring per pipeline."],
standards=[
 "OpenLineage (fine-grained facets).",
 "W3C PROV-O."],
citations=[
 "OpenLineage. OpenLineage Specification. Linux Foundation.",
 "Cheney J et al. Provenance in databases: why, how, and where. Foundations and Trends in Databases, 2009."],
sig_lens="""The Signature reading: fine-grained lineage is the registry's magnifying glass - brought out where the law or the mystery demands it, showing exactly which rows spoke. The Signature glass is used where it matters, not everywhere at ruinous cost.""",
demo_data={"nodes":["t1","t2","score"],"edges":[["t1","score"],["t2","score"]],
 "formula":{"inputs":{"rows_in":3,"rows_used":3},"expr":"rows_used/rows_in","expected":1.0}},
),
dict(
name="Lineage Across Organizations",
group="Advanced Lineage Topics", ladder_rank=26, ladder_tier="advanced",
description="""Data crosses organizational boundaries - partners send feeds, vendors provide enrichment, regulators receive reports - and lineage must cross with it, without leaking what each side keeps private. Cross-organization lineage exchanges traces at the boundary: the partner's feed arrives with its lineage manifest (sources, transformations, quality attestations) while the partner's internal graph stays private. Trust frameworks govern the exchange: mutually recognized lineage formats (OpenLineage), attestation standards (what the sender warrants about the trace), and verification (the receiver spot-checks). The hard problems are identity (matching entities across organizations' graphs), confidentiality (lineage can reveal business processes), and liability (who warrants the trace's accuracy). The registry handles them with boundary nodes - the partner feed as a node with its manifest, internal detail hidden - and with lineage manifests as contractual deliverables, warranted like the data itself.""",
how_it_works="""Boundary integrations exchange OpenLineage manifests with each data delivery: sources, transformations, quality attestations, and contact for questions. The registry stores manifests as boundary nodes linked to internal graphs, with confidentiality flags controlling visibility. Attestation standards define what senders warrant; verification spot-checks compare manifest claims against observed data. Identity resolution across organizations uses agreed keys or privacy-preserving record linkage. Manifests are contractual: the data sharing agreement warrants their accuracy, and manifest breaches trigger the same incident process as data breaches.""",
key_points=[
 "Lineage crosses boundaries via manifests; internal graphs stay private.",
 "Trust frameworks: common formats, attestation standards, verification.",
 "Boundary nodes link partner feeds to internal graphs with confidentiality flags.",
 "Manifests are contractual deliverables, warranted like the data.",
 "Identity across organizations uses agreed keys or privacy-preserving linkage."],
requirements=[
 "Boundary manifest exchange with data deliveries.",
 "Attestation standards with verification spot-checks.",
 "Confidentiality-flagged boundary nodes.",
 "Contractual manifest warranties with breach processes."],
standards=[
 "OpenLineage specification.",
 "W3C PROV-O."],
citations=[
 "OpenLineage. OpenLineage Specification. Linux Foundation.",
 "DAMA International. DAMA-DMBOK, 2nd ed. Technics Publications, 2017."],
sig_lens="""The Signature reading: cross-organization lineage is the registry's diplomacy - traces exchanged at the border with honor, interiors kept private, warrants sworn like treaties. The Signature diplomat trusts but verifies every manifest.""",
demo_data={"nodes":["partner_feed","internal"],"edges":[["partner_feed","internal"]],
 "formula":{"inputs":{"manifest_fields":8,"verified":8},"expr":"verified/manifest_fields","expected":1.0}},
),
dict(
name="Lineage for ML Features",
group="Advanced Lineage Topics", ladder_rank=27, ladder_tier="advanced",
description="""ML features need lineage with special rigor: a model's behavior is determined by its training data, so the training data's lineage is the model's pedigree. Feature lineage traces each feature from raw sources through transformations to the feature store, with the exact code versions, parameters, and time windows used. Training lineage records which feature snapshots trained which model version - because retraining on different data makes a different model, and debugging a model starts with diffing its training lineage. The registry also tracks feature drift lineage: when a feature's upstream changes, the affected models are found by downstream traversal and retraining is triggered. Regulatory pressure is growing: high-stakes models must document their data lineage for audit. The discipline extends to labels (where did the ground truth come from?) and to evaluation data (kept strictly separate from training, with lineage proving the separation).""",
how_it_works="""Feature pipelines emit lineage like any pipeline, with feature definitions versioned and snapshots identified. Training jobs record their input snapshots, code, parameters, and random seeds as lineage; model versions link to their training lineage permanently. Drift monitors watch feature upstreams; changes trigger downstream model impact analysis and retraining workflows. Label lineage tracks ground-truth sources with their own quality. Train/eval separation is enforced by lineage checks - evaluation data must have no lineage overlap with training data. Model cards and audit packages render the lineage automatically.""",
key_points=[
 "Feature lineage: raw sources to feature store with code versions and windows.",
 "Training lineage: which snapshots trained which model version, permanently linked.",
 "Upstream changes trigger model impact analysis and retraining.",
 "Label lineage and train/eval separation are enforced by lineage checks.",
 "Model cards render lineage automatically for audit."],
requirements=[
 "Versioned feature definitions with snapshot identification.",
 "Training lineage with inputs, code, parameters, seeds.",
 "Drift-triggered impact analysis and retraining workflows.",
 "Lineage-enforced train/eval separation."],
standards=[
 "OpenLineage specification."],
citations=[
 "OpenLineage. OpenLineage Specification. Linux Foundation.",
 "Sculley D et al. Hidden technical debt in machine learning systems. NeurIPS, 2015."],
sig_lens="""The Signature reading: ML lineage is the registry's pedigree book for thinking machines - every feature's ancestry, every model's training, sworn and permanent. The Signature registry lets no model forget where it learned.""",
demo_data={"nodes":["raw","features","model_v3"],"edges":[["raw","features"],["features","model_v3"]],
 "formula":{"inputs":{"features":42,"drifted":2},"expr":"features-drifted","expected":40}},
),
dict(
name="Lineage for a Million-Database Network",
group="Advanced Lineage Topics", ladder_rank=28, ladder_tier="advanced",
description="""A million databases' lineage is a graph of graphs: each database captures its internal lineage authoritatively, and cross-database flows - replication, federation queries, shared features - link the graphs with boundary edges. The federation principles mirror the reference-data federation: local authority, standard interchange (OpenLineage), a shared catalog indexing what lineage exists where, and trust frameworks for cross-database traces. The scale challenges are real: global traversals must not scan a million graphs, so the registry maintains a summary graph - database-level nodes with flow summaries - for coarse queries, drilling into database graphs on demand. Privacy holds: databases expose lineage summaries and boundary manifests, not internal detail. The network's lineage answers the ultimate questions: where did this number come from (across databases), what breaks if this database goes dark (across the network), and can we prove it (with chained manifests).""",
how_it_works="""Each database runs its lineage registry and publishes summaries plus boundary manifests to the network catalog. The summary graph links databases by data flows with volumes and freshness. Global traversals start at the summary level and drill into database graphs via their APIs. Cross-database impact analysis walks the summary graph then expands affected databases. Manifest chains provide audit evidence across boundaries. Trust frameworks govern manifest warranties; verification spot-checks cross-database claims. The catalog indexes lineage by subject so investigators find relevant graphs without scanning the network.""",
key_points=[
 "Graph of graphs: local authority, boundary edges, federated queries.",
 "Summary graph for coarse global traversals; drill-down on demand.",
 "Privacy: summaries and manifests exposed, internals kept local.",
 "Manifest chains provide cross-database audit evidence.",
 "Catalog indexing finds relevant graphs without scanning the network."],
requirements=[
 "Per-database lineage registries with summary publication.",
 "Network catalog with summary graph and drill-down.",
 "Boundary manifests with warranty frameworks.",
 "Cross-database impact analysis workflows."],
standards=[
 "OpenLineage specification."],
citations=[
 "OpenLineage. OpenLineage Specification. Linux Foundation.",
 "DAMA International. DAMA-DMBOK, 2nd ed. Technics Publications, 2017."],
sig_lens="""The Signature reading: network lineage is a million maps bound in one atlas - each database charting its own lands, the atlas showing the roads between. The Signature atlas answers any journey's question without demanding every map at once.""",
demo_data={"nodes":["db1","db2","db3"],"edges":[["db1","db2"],["db2","db3"]],
 "formula":{"inputs":{"dbs":1000000,"summarized":1000000},"expr":"summarized/dbs","expected":1.0}},
),
dict(
name="Lineage Completeness Metrics",
group="Advanced Lineage Topics", ladder_rank=29, ladder_tier="advanced",
description="""Lineage coverage is measured, not assumed: what share of datasets have upstream lineage, what share of jobs emit lineage, what share of edges carry high-confidence capture, what share of critical paths are fully traced? Completeness metrics run per estate area, per platform, per data tier - because the executive dashboard's lineage matters more than the sandbox's. The metrics drive the instrumentation program: the lowest-coverage critical area gets the next integration project. Trend lines show whether completeness is improving or rotting as new uninstrumented systems appear. Targets are set by tier: tier-1 data (financial, safety, regulated) needs complete high-confidence lineage; tier-3 sandbox data needs best effort. Completeness reports go to data owners quarterly with the gaps named - sunlight is the best instrumentation incentive. A lineage program that does not measure completeness is flying blind about its own blind spots.""",
how_it_works="""Completeness jobs scan the estate: datasets with/without upstream lineage, jobs with/without emission, edges by capture method and confidence, critical paths fully traced or not. Metrics aggregate by area, platform, and tier with targets per tier. Dashboards show coverage maps with the gaps highlighted; the instrumentation backlog prioritizes by tier times gap. Quarterly reports to owners name their gaps with remediation guidance. Trend analysis flags rotting areas where new systems outpace instrumentation. Completeness gates block tier-1 promotions: a dataset cannot be declared production-critical without complete lineage.""",
key_points=[
 "Measured per area, platform, tier: upstream coverage, emission rates, confidence mix.",
 "Targets by tier: tier-1 needs complete high-confidence lineage.",
 "Metrics drive the instrumentation backlog prioritized by tier times gap.",
 "Quarterly gap reports to owners; sunlight incentivizes instrumentation.",
 "Completeness gates block tier-1 promotion without full lineage."],
requirements=[
 "Completeness scanning jobs with tiered targets.",
 "Coverage dashboards with gap highlighting.",
 "Prioritized instrumentation backlog.",
 "Promotion gates requiring lineage completeness."],
standards=[
 "OpenLineage specification.",
 "ISO 8000-8 for quality measurement."],
citations=[
 "OpenLineage. OpenLineage Specification. Linux Foundation.",
 "DAMA International. DAMA-DMBOK, 2nd ed. Technics Publications, 2017."],
sig_lens="""The Signature reading: completeness metrics are the registry's survey of its own maps - charted waters measured, blank spots named, owners notified. The Signature surveyor admits no blind spot and prioritizes the critical waters first.""",
demo_data={"nodes":["tier1","tier2"],"edges":[["tier1","tier2"]],
 "formula":{"inputs":{"covered":940,"total":1000},"expr":"covered/total","expected":0.94}},
),
dict(
name="Lineage Staleness",
group="Advanced Lineage Topics", ladder_rank=30, ladder_tier="advanced",
description="""Lineage rots: pipelines are rewritten without updating declarations, jobs are retired leaving ghost edges, schemas change under static mappings. Stale lineage is worse than missing lineage - it confidently shows a journey that no longer exists, sending debuggers down dead roads. The registry fights staleness four ways. Freshness signals: edges carry last-confirmed timestamps, refreshed by each run's emission - an edge unconfirmed for months is suspect. Change detection: schema and pipeline changes trigger lineage re-validation. Ghost hunting: jobs that stopped emitting get their edges flagged after a grace period. Re-verification: declared edges expire and require human re-confirmation. Staleness dashboards show the age distribution of edge confirmations per area; areas with aging lineage get re-instrumentation or re-declaration sprints. The rule is simple: lineage nobody confirms is lineage nobody should trust.""",
how_it_works="""Every edge carries a last-confirmed timestamp updated by run emissions, change detections, and human confirmations. Staleness policies per tier define confirmation freshness requirements; breaching edges get suspect flags visible in all views. Ghost detection compares emitting jobs against edge sources, flagging edges from silent jobs. Declared edges carry expiry dates with re-confirmation workflows. Staleness dashboards show confirmation-age distributions; remediation sprints target the oldest areas. Suspect edges are excluded from high-stakes queries (compliance evidence, impact analysis) until re-confirmed.""",
key_points=[
 "Stale lineage misleads worse than missing lineage - it shows journeys that no longer exist.",
 "Edges carry last-confirmed timestamps; unconfirmed edges become suspect.",
 "Ghost detection flags edges from jobs that stopped emitting.",
 "Declared edges expire and require human re-confirmation.",
 "Suspect edges are excluded from compliance and impact queries."],
requirements=[
 "Last-confirmed timestamps on all edges with tiered freshness policies.",
 "Suspect flagging visible in every lineage view.",
 "Ghost detection with grace periods.",
 "Declared-edge expiry with re-confirmation workflows."],
standards=[
 "OpenLineage specification."],
citations=[
 "OpenLineage. OpenLineage Specification. Linux Foundation.",
 "DAMA International. DAMA-DMBOK, 2nd ed. Technics Publications, 2017."],
sig_lens="""The Signature reading: staleness is the registry's war against its own decay - every road re-walked on schedule, ghost roads marked, unconfirmed paths distrusted. The Signature registry would rather admit a blank than show a lie.""",
demo_data={"nodes":["old_edge","new_edge"],"edges":[["old_edge","new_edge"]],
 "formula":{"inputs":{"days":400,"limit":90},"expr":"days-limit","expected":310}},
),
dict(
name="Privacy and Lineage",
group="Advanced Lineage Topics", ladder_rank=31, ladder_tier="advanced",
description="""Lineage itself can leak: the trace showing that a sensitive source feeds a shared dataset reveals the sensitive source's existence and use; column lineage can expose which individuals' data flows where. Privacy-aware lineage applies the same protections to traces as to data: classification labels on nodes and edges, access control on lineage queries (analysts see only the lineage they are cleared for), redaction of sensitive node details in shared views, and purpose limitation on lineage use. The tension is real: debugging needs full traces, privacy needs minimal exposure. The registry resolves it with tiered visibility - full lineage for the owning team and incident responders, summarized lineage for general consumers, redacted lineage for external parties - and with audit logging of lineage access itself. Lineage retention follows data retention: when personal data is deleted, its fine-grained traces go too, keeping only the coarse evidence the law requires.""",
how_it_works="""Nodes and edges carry classification labels inherited from their data; lineage queries enforce access control against the caller's clearance. Views tier by audience: full, summarized, redacted. Sensitive details (exact queries, individual identifiers in traces) redact automatically in lower tiers. Lineage access is audit-logged like data access. Retention policies cascade: personal-data deletion triggers fine-grained trace deletion with coarse evidence preserved per legal requirements. Privacy impact assessments cover new lineage capture, and data-protection reviews approve cross-boundary lineage sharing.""",
key_points=[
 "Lineage can leak: traces reveal sensitive sources and individual data flows.",
 "Classification labels and access control apply to lineage queries.",
 "Tiered visibility: full for owners, summarized for consumers, redacted for external.",
 "Lineage access is audit-logged like data access.",
 "Retention cascades: personal-data deletion removes fine-grained traces."],
requirements=[
 "Classification inheritance for lineage nodes and edges.",
 "Access-controlled lineage queries with tiered views.",
 "Automatic redaction in lower tiers.",
 "Audit logging of lineage access and cascading retention."],
standards=[
 "W3C PROV-O.",
 "ISO/IEC 27701 privacy controls."],
citations=[
 "W3C. PROV-O: The PROV Ontology. W3C Recommendation, 2013.",
 "ISO/IEC 27701. Privacy information management. ISO."],
sig_lens="""The Signature reading: privacy in lineage is the registry guarding its own maps - the roads shown only to the cleared, the sensitive ways redacted, every viewing recorded. The Signature guard protects the map as fiercely as the territory.""",
demo_data={"nodes":["pii_src","shared"],"edges":[["pii_src","shared"]],
 "formula":{"inputs":{"tiers":3,"cleared":1},"expr":"tiers-cleared","expected":2}},
),
dict(
name="Lineage Provenance",
group="Advanced Lineage Topics", ladder_rank=32, ladder_tier="advanced",
description="""Lineage provenance records how the lineage itself was built: which integration captured this edge, what code version ran, what confidence it assigned, which human declared that mapping, when each confirmation happened. When two traces disagree - the pipeline's instrumentation says X, the SQL parser says Y - provenance adjudicates: instrumented beats parsed, recent beats stale, verified beats inferred. Provenance also enables lineage debugging: the graph shows a wrong edge, and provenance shows which integration produced it, leading to the bug. The registry models lineage provenance in PROV-O like all its provenance, stores it with the edges, and exposes it in every lineage view - the evidence behind the evidence. Provenance completeness is monitored: edges without provenance are quarantined, because an untraceable trace is a rumor.""",
how_it_works="""Capture integrations emit provenance with every edge: integration ID and version, capture method, confidence, actor, timestamp. The registry stores provenance alongside edges and shows it in lineage views (the evidence toggle). Disagreement resolution uses provenance tiers automatically, flagging conflicts for review when tiers tie. Provenance queries answer how-was-this-edge-built for debugging. Completeness monitoring quarantines provenance-poor edges. Provenance versions with edge updates, keeping the full history of how each trace evolved.""",
key_points=[
 "Lineage provenance: which integration, what version, what method, what confidence, who, when.",
 "Provenance adjudicates disagreeing traces by tier.",
 "Powers lineage debugging: wrong edge leads to the buggy integration.",
 "Exposed in every view as the evidence behind the evidence.",
 "Provenance-poor edges are quarantined as rumors."],
requirements=[
 "Provenance emission from all capture integrations.",
 "PROV-O modeling with tier-based disagreement resolution.",
 "Evidence toggles in lineage views.",
 "Completeness monitoring with quarantine."],
standards=[
 "W3C PROV-O.",
 "OpenLineage specification."],
citations=[
 "W3C. PROV-O: The PROV Ontology. W3C Recommendation, 2013.",
 "OpenLineage. OpenLineage Specification. Linux Foundation."],
sig_lens="""The Signature reading: lineage provenance is the registry swearing to its own testimony - each trace able to name its witness and its method. The Signature registry quarantines rumors and adjudicates disagreements by the rank of witnesses.""",
demo_data={"nodes":["edge","prov"],"edges":[["edge","prov"]],
 "formula":{"inputs":{"with_prov":999,"total":1000},"expr":"with_prov/total","expected":0.999}},
),
dict(
name="Automated Lineage Discovery",
group="Advanced Lineage Topics", ladder_rank=33, ladder_tier="advanced",
description="""Automated discovery finds lineage nobody declared: scanning query logs to map table reads, scanning code repositories to parse pipeline logic, correlating schemas to propose hidden dependencies, watching network traffic to find undeclared feeds. Discovery is how the registry conquers the dark estate - the spreadsheets, scripts, and shadow pipelines that predate instrumentation. The pipeline runs continuously: new queries, new code, new connections are discovered, proposed as lineage edges with confidence, and queued for confirmation. High-confidence discoveries auto-accept (with audit); the rest go to human review. Discovery also finds the dead: datasets nobody reads, pipelines nobody runs, feeds nobody consumes - the estate's ghosts, candidates for retirement. The discovered graph is marked as such - discovered edges carry their method and confidence - so it never masquerades as instrumented truth. Discovery never sleeps, because the dark estate never stops growing.""",
how_it_works="""Discovery jobs scan query logs, code repos, schema catalogs, and connection metadata on schedules. Proposed edges carry method and confidence; auto-acceptance applies above the confidence bar with audit logging, human review below it. Confirmed discoveries convert to declared lineage with the confirmer recorded. Ghost detection flags unreferenced datasets and unrunnable pipelines for retirement review. Discovery coverage metrics track the dark estate's shrinkage; newly dark areas (a team stood up an uninstrumented pipeline) trigger onboarding. Discovered edges are visually distinct in all views.""",
key_points=[
 "Discovery scans logs, code, schemas, and connections for undeclared lineage.",
 "Proposed edges carry confidence; high-confidence auto-accepts with audit.",
 "Finds the dead too: unread datasets and unrunnable pipelines for retirement.",
 "Discovered edges are marked distinct from instrumented truth.",
 "Continuous operation - the dark estate never stops growing."],
requirements=[
 "Discovery jobs across logs, repos, catalogs, connections.",
 "Confidence-thresholded auto-acceptance with audit.",
 "Human review queues for low-confidence proposals.",
 "Ghost detection with retirement workflows."],
standards=[
 "OpenLineage specification."],
citations=[
 "OpenLineage. OpenLineage Specification. Linux Foundation.",
 "DAMA International. DAMA-DMBOK, 2nd ed. Technics Publications, 2017."],
sig_lens="""The Signature reading: discovery is the registry's lantern in the dark estate - finding undeclared roads, marking them honestly, and naming the ghosts for retirement. The Signature lantern never sleeps and never mistakes its light for the sun.""",
demo_data={"nodes":["dark","found"],"edges":[["dark","found"]],
 "formula":{"inputs":{"proposed":200,"confirmed":170},"expr":"confirmed/proposed","expected":0.85}},
),
dict(
name="Data Lineage Registry Mastery Review",
group="Advanced Lineage Topics", ladder_rank=34, ladder_tier="advanced",
description="""The mastery review binds the ladder. Foundations: lineage is the record of data's journey, serving trust, debugging, compliance, and AI governance; source nodes are watched headwaters; transformation steps are versioned waystations; sink nodes tell their stories; derivation formulas are sworn mathematics; column lineage traces fields; table lineage maps the estate; OpenLineage is the common script; capture comes by instrumentation, parsing, inference, and declaration; batch lineage chronicles runs; streaming lineage charts rivers. Compounded: lineage graphs with temporal edges; DAG discipline for batch; upstream/downstream traversal; impact analysis ahead of change; root-cause inquests; quality joined to lineage; lineage metadata as testimony; query-time capture of shadow work; ETL integration at three depths; dual storage of events and graphs; visualization as storytelling; APIs as open gates. Advanced: fine-grained overlays, cross-organization diplomacy, ML pedigrees, the million-database atlas, completeness surveys, staleness wars, privacy guards, provenance of provenance, and the ever-burning lantern of discovery. The creed: every journey recorded, every trace checkable, no data without a story.""",
how_it_works="""The review serves as capstone assessment and deployment checklist: can the team capture lineage, traverse it, analyze impact, diagnose causes, and prove compliance? New lineage programs verify each rung: integrations emitting, graphs assembling, traversals fast, metadata complete, privacy guarded. Gaps become the quarter's program of work. The review repeats as the estate grows - mastery is keeping the maps current, not drawing them once.""",
key_points=[
 "Foundations: journeys, sources, steps, sinks, formulas, columns, tables, OpenLineage, capture, batch, streams.",
 "Compounded: graphs, DAGs, traversal, impact, root cause, quality, metadata, query capture, ETL, storage, visualization, APIs.",
 "Advanced: fine grain, cross-org, ML, network atlas, completeness, staleness, privacy, provenance, discovery.",
 "The creed: every journey recorded, every trace checkable, no data without a story.",
 "Mastery is keeping the maps current as the estate grows."],
requirements=[
 "Demonstrated competence at every rung before program launch.",
 "Checklist rerun on major changes and estate growth.",
 "Gaps converted to funded program work."],
standards=[
 "OpenLineage specification.",
 "W3C PROV-O."],
citations=[
 "OpenLineage. OpenLineage Specification. Linux Foundation.",
 "DAMA International. DAMA-DMBOK, 2nd ed. Technics Publications, 2017."],
sig_lens="""The Signature reading: the mastery review is graduation as keeper of journeys. The Signature graduate can trace any number to its source, warn every traveler of broken roads, and swear the creed: every journey recorded, every trace checkable, no data without a story.""",
demo_data={"nodes":["start","end"],"edges":[["start","end"]],
 "formula":{"inputs":{"rungs":34,"complete":34},"expr":"complete/rungs","expected":1.0}},
),
]
