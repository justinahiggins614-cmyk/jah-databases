#!/usr/bin/env python3
"""Data Lineage Registry entries 13-24 (compounded)."""

APPEND = [
dict(
name="Lineage Graphs",
group="Graphs and Nodes", ladder_rank=13, ladder_tier="compounded",
description="""The lineage graph is the registry's central structure: nodes for datasets, jobs, runs, and columns; edges for reads, writes, and derivations - a directed graph of everything data's journey. Graph thinking unlocks the queries tables cannot express: find all paths from this source to that report, find the nodes with the most downstream dependents (the load-bearing datasets), find cycles (which should not exist in batch lineage and indicate a bug when they do). The registry stores the graph in a graph database or graph-indexed store, with node properties (owner, classification, freshness) and edge properties (capture method, confidence, transformation). Graph algorithms run continuously: reachability for impact analysis, centrality for criticality ranking, community detection for estate segmentation. The graph is temporal - edges carry validity periods - so as-of queries see the graph as it was. A million-database network's lineage is a graph of graphs, federated but queryable as one.""",
how_it_works="""Lineage events assemble into the graph: nodes upserted by identity, edges added with properties and validity periods. Continuous algorithms compute reachability indexes, criticality scores, and estate segments. Temporal queries filter edges by validity for as-of views. Cycle detection alerts on batch cycles (bugs) while permitting declared streaming cycles. Federation links subgraphs across databases with cross-graph edges, keeping each database's graph authoritative locally. The graph API serves path queries, neighborhood queries, and algorithm results; visualization renders subgraphs around any node on demand.""",
key_points=[
 "Nodes: datasets, jobs, runs, columns. Edges: reads, writes, derivations.",
 "Path queries, centrality, community detection - graph algorithms on lineage.",
 "Temporal edges enable as-of graph views.",
 "Cycle detection catches batch bugs; streaming cycles are declared.",
 "Federation makes a million databases' graphs queryable as one."],
requirements=[
 "Graph storage with node/edge properties and temporal edges.",
 "Continuous reachability, criticality, and segmentation algorithms.",
 "Cycle detection with batch/streaming distinction.",
 "Federation with cross-graph edges."],
standards=[
 "OpenLineage specification.",
 "W3C PROV-O."],
citations=[
 "OpenLineage. OpenLineage Specification. Linux Foundation.",
 "Robinson I, Webber J, Eifrem E. Graph Databases, 2nd ed. O'Reilly, 2015."],
sig_lens="""The Signature reading: the lineage graph is the registry's great map of journeys - every road, every waystation, charted and queryable. The Signature map shows any path, names the load-bearing roads, and remembers every road as it was.""",
demo_data={"nodes":["a","b","c","d"],"edges":[["a","b"],["b","c"],["c","d"]],
 "formula":{"inputs":{"paths":1,"hops":3},"expr":"paths*hops","expected":3}},
),
dict(
name="Directed Acyclic Graphs in Lineage",
group="Graphs and Nodes", ladder_rank=14, ladder_tier="compounded",
description="""Batch lineage must be acyclic: data flows forward from sources through transformations to sinks, never looping back. The DAG property is what makes lineage reasoning sound - topological ordering gives the execution order, reachability terminates, and impact analysis cannot chase its own tail. When a cycle appears in batch lineage, it is a bug or a modeling error: a job reading its own output as input, or two jobs feeding each other. The registry detects cycles on ingestion and quarantines the offending edges for modeling review instead of letting them corrupt traversals. Streaming systems are the exception: feedback loops (a stream joining its own past output) are legitimate, so streaming edges carry a cycle-allowed flag with the loop's semantics documented. The DAG discipline also governs pipeline design: orchestrators topologically sort declared dependencies, and a dependency declaration that would create a cycle is rejected at authoring time.""",
how_it_works="""On edge ingestion, the registry runs incremental cycle detection restricted to batch edges; detected cycles quarantine the new edge and alert the owning team with the cycle path. Orchestrators validate declared dependencies for acyclicity before accepting pipeline definitions. Topological ordering serves execution order, backfill sequencing, and safe deletion order (delete downstream first). Streaming feedback edges are permitted with explicit cycle-allowed flags and documented loop semantics; traversals treat them with visited-set guards. Cycle metrics track frequency by estate area - recurring cycles indicate modeling problems worth fixing, not just quarantining.""",
key_points=[
 "Batch lineage must be acyclic; cycles are bugs or modeling errors.",
 "Cycle detection quarantines offending edges on ingestion.",
 "Topological order gives execution, backfill, and safe-deletion sequences.",
 "Streaming feedback loops are legitimate with explicit flags and guards.",
 "Orchestrators reject cyclic dependency declarations at authoring."],
requirements=[
 "Incremental cycle detection on batch edge ingestion.",
 "Quarantine and alerting with cycle paths.",
 "Topological ordering services for execution and backfill.",
 "Explicit cycle-allowed flags for legitimate streaming loops."],
standards=[
 "OpenLineage specification."],
citations=[
 "OpenLineage. OpenLineage Specification. Linux Foundation.",
 "Kleppmann M. Designing Data-Intensive Applications. O'Reilly, 2017."],
sig_lens="""The Signature reading: the DAG law is the registry's one-way decree for batch journeys - forward always, never back. The Signature registry arrests cycles at the border and permits only the declared, documented loops of streams.""",
demo_data={"nodes":["s1","s2","s3"],"edges":[["s1","s2"],["s2","s3"]],
 "formula":{"inputs":{"n":4,"e":3},"expr":"n-e","expected":1}},
),
dict(
name="Lineage Traversal: Upstream and Downstream",
group="Graphs and Nodes", ladder_rank=15, ladder_tier="compounded",
description="""Traversal is lineage's fundamental operation: upstream walks backward from a node to everything that feeds it; downstream walks forward to everything it feeds. Upstream traversal answers why is this number what it is and what broke it - walking back through transformations to the changed source or failed job. Downstream traversal answers who is affected - walking forward to every dashboard, model, and partner file that consumes this data. Effective traversal needs controls: depth limits (the full upstream of a warehouse table may be thousands of nodes), cycle guards, confidence filtering (show only high-confidence edges, or show inferred edges dashed), and temporal scoping (traverse the graph as of last Tuesday). The registry precomputes reachability indexes so traversals answer in milliseconds even on million-node graphs, and traversal results feed impact analysis, notification, and debugging workflows directly.""",
how_it_works="""The traversal engine walks the graph with configurable direction, depth, confidence thresholds, and as-of dates, using precomputed reachability indexes for speed. Results return as subgraphs with paths annotated - each path showing the chain of transformations. Change-aware traversal highlights nodes changed recently, focusing debugging on likely causes. Traversal APIs serve the debugging UI (upstream from failure), the notification service (downstream from incident), and the impact analyzer (downstream from proposed change). Saved traversals rerun on schedules - the downstream of this source, checked weekly for new consumers that should be notified of changes.""",
key_points=[
 "Upstream finds causes; downstream finds the affected.",
 "Controls: depth limits, cycle guards, confidence filters, temporal scoping.",
 "Reachability indexes keep traversals fast on million-node graphs.",
 "Change-aware traversal highlights recently changed nodes.",
 "Saved traversals rerun on schedules for ongoing awareness."],
requirements=[
 "Traversal engine with direction, depth, confidence, as-of controls.",
 "Precomputed reachability indexes.",
 "Change-aware highlighting of recently modified nodes.",
 "Saved traversals with scheduled reruns."],
standards=[
 "OpenLineage specification."],
citations=[
 "OpenLineage. OpenLineage Specification. Linux Foundation.",
 "Robinson I, Webber J, Eifrem E. Graph Databases, 2nd ed. O'Reilly, 2015."],
sig_lens="""The Signature reading: traversal is the registry walking the roads of journey - backward to find the cause, forward to warn the travelers. The Signature walker is swift, careful of doubtful paths, and remembers the roads worth walking again.""",
demo_data={"nodes":["src","mid","dst"],"edges":[["src","mid"],["mid","dst"]],
 "formula":{"inputs":{"up":2,"down":2},"expr":"up+down","expected":4}},
),
dict(
name="Impact Analysis",
group="Graphs and Nodes", ladder_rank=16, ladder_tier="compounded",
description="""Impact analysis predicts what a change will break before it is made: deprecating this column affects these 14 downstream columns in 6 datasets feeding 3 dashboards and 1 model. The analysis walks downstream from the proposed change through the lineage graph, classifying each affected node: breaking (will fail - a removed column), degrading (will run but worse - a freshness relaxation), or unaffected. It accounts for the subtle paths: the column flows through a view, into a feature table, into a model - three hops the proposer never considered. Impact reports go to the change's approval workflow with the affected owners listed, turning unknown unknowns into a reviewable list. After the change, the registry compares predicted vs actual impact, tuning the analyzer. The organizations that do impact analysis well make changes fearlessly; the ones that do not make changes fearfully or not at all.""",
how_it_works="""Proposed changes (schema edits, deprecations, SLA changes, source retirements) submit to the impact analyzer with the change description. The analyzer traverses downstream, applies impact rules per change type (removal breaks direct consumers; type narrowing breaks strict readers), and classifies each affected node with evidence paths. Reports list affected nodes, owners, and classifications, attaching to the change approval. Affected owners review and sign off or negotiate. Post-change, incident correlation checks whether predicted impacts materialized and whether unpredicted impacts occurred - both tune the rules. Analyses are cached per change proposal and invalidated when the graph changes beneath them.""",
key_points=[
 "Impact analysis walks downstream from proposed changes to affected nodes.",
 "Impacts classify as breaking, degrading, or unaffected with evidence paths.",
 "Subtle multi-hop paths are found mechanically, not by memory.",
 "Reports attach to change approvals with affected owners listed.",
 "Predicted vs actual comparison tunes the analyzer continuously."],
requirements=[
 "Impact analyzer with per-change-type rules.",
 "Downstream traversal with evidence paths.",
 "Approval workflow integration with owner sign-off.",
 "Predicted-vs-actual tuning loop."],
standards=[
 "OpenLineage specification."],
citations=[
 "OpenLineage. OpenLineage Specification. Linux Foundation.",
 "DAMA International. DAMA-DMBOK, 2nd ed. Technics Publications, 2017."],
sig_lens="""The Signature reading: impact analysis is the registry's surveyor walking ahead of every change - mapping exactly whose house stands on the moving ground. The Signature surveyor's maps are checked against reality and redrawn sharper each time.""",
demo_data={"nodes":["col","view","model"],"edges":[["col","view"],["view","model"]],
 "formula":{"inputs":{"affected":14,"datasets":6},"expr":"affected+datasets","expected":20}},
),
dict(
name="Root-Cause Analysis",
group="Graphs and Nodes", ladder_rank=17, ladder_tier="compounded",
description="""When data is wrong, root-cause analysis walks upstream to find why: the dashboard number dropped Tuesday - upstream traversal shows the source feed's schema changed Monday, the transformation started dropping the new field's rows, and the aggregate silently shrank. The method is systematic: start from the symptom (wrong node, wrong time), walk upstream collecting candidate causes (recent changes, failed runs, quality breaches), rank them by likelihood (recency, blast radius match, historical patterns), and verify by checking each candidate's evidence. The registry accelerates this with change correlation: it already knows which upstream nodes changed recently, which runs failed, which quality checks breached - so the candidate list is usually short. The analysis concludes with a verified cause, the fix, and the prevention: the lineage gap, missing test, or absent monitor that let the cause through. Every root cause becomes a regression: a test, a monitor, or a contract rule that would have caught it.""",
how_it_works="""Analysts start from the symptomatic node and time; the registry's diagnosis assistant traverses upstream gathering candidates - recent upstream changes, failed or late runs, quality breaches, source incidents - ranked by recency and blast-radius fit. Each candidate links to its evidence: the change diff, the failure log, the breach report. The analyst verifies by inspection and marks the confirmed cause; the registry records the diagnosis with the evidence chain. The fix executes (revert, backfill, patch), and the prevention item - test, monitor, or contract rule - is filed as work with an owner. Diagnosis records feed a knowledge base: recurring cause patterns become automated checks.""",
key_points=[
 "Systematic: symptom, upstream candidates, ranked likelihood, verified cause.",
 "Change correlation shortlists candidates from recent changes, failures, breaches.",
 "Analysis ends with fix plus prevention: test, monitor, or contract rule.",
 "Every root cause becomes a regression that would have caught it.",
 "Diagnosis knowledge bases turn patterns into automated checks."],
requirements=[
 "Diagnosis assistance with upstream candidate ranking.",
 "Evidence linking per candidate (diffs, logs, breach reports).",
 "Recorded diagnoses with evidence chains.",
 "Prevention work items with owners filed per diagnosis."],
standards=[
 "OpenLineage specification.",
 "Site Reliability Engineering post-mortem practices."],
citations=[
 "Beyer B et al. Site Reliability Engineering. O'Reilly, 2016.",
 "OpenLineage. OpenLineage Specification. Linux Foundation."],
sig_lens="""The Signature reading: root-cause analysis is the registry's inquest - walking backward from the body to the blow, ranking suspects by evidence, and ending with both cure and prevention. The Signature inquest wastes no second crisis on a solved mystery.""",
demo_data={"nodes":["feed","clean","agg","dash"],"edges":[["feed","clean"],["clean","agg"],["agg","dash"]],
 "formula":{"inputs":{"candidates":5,"verified":1},"expr":"candidates-verified","expected":4}},
),
dict(
name="Lineage and Data Quality",
group="Graphs and Nodes", ladder_rank=18, ladder_tier="compounded",
description="""Lineage and quality are two halves of trust: lineage says where data came from, quality says whether it is any good. Together they answer the questions neither answers alone: this number is wrong - where did the badness enter (lineage to the step, quality breach at that step)? This source is unreliable - what downstream is contaminated (quality scores propagated downstream through lineage)? The registry joins them by attaching quality verdicts to lineage nodes and edges: each run's quality results, each source's trust score, each transformation's validation outcomes. Quality-aware traversal then finds the nearest upstream quality failure from any symptom, and contamination analysis walks downstream from a bad source listing everything tainted. The combination also powers quality SLAs with teeth: a contract promises quality, lineage proves where it broke, and the breach routes to the responsible step's owner automatically.""",
how_it_works="""Quality systems publish their verdicts to the registry keyed by node and run; the graph stores them as node properties with history. Quality-aware traversal weights paths by quality - the nearest upstream failure is found by walking back to the first node with a breaching verdict. Contamination analysis walks downstream from failed nodes marking tainted datasets, which feed quarantine decisions. Contract enforcement consults lineage to route breaches to step owners. Quality lineage dashboards show the graph colored by quality - green paths, red nodes - making systemic quality problems visible at a glance.""",
key_points=[
 "Lineage plus quality answers: where did badness enter, what is contaminated.",
 "Quality verdicts attach to lineage nodes and edges with history.",
 "Quality-aware traversal finds the nearest upstream failure from any symptom.",
 "Contamination analysis walks downstream from bad sources.",
 "Breach routing uses lineage to find the responsible step's owner."],
requirements=[
 "Quality verdict publication keyed by node and run.",
 "Quality-colored graph views with history.",
 "Contamination analysis for quarantine decisions.",
 "Lineage-based breach routing to step owners."],
standards=[
 "OpenLineage (quality facets).",
 "ISO 8000-8 for quality measurement."],
citations=[
 "OpenLineage. OpenLineage Specification. Linux Foundation.",
 "DAMA International. DAMA-DMBOK, 2nd ed. Technics Publications, 2017."],
sig_lens="""The Signature reading: lineage and quality are the registry's two eyes - one sees the road, the other sees its condition. Together they find where the road broke and who travels the broken stretch.""",
demo_data={"nodes":["src","step","sink"],"edges":[["src","step"],["step","sink"]],
 "formula":{"inputs":{"pass_rate":97,"total":100},"expr":"pass_rate/total","expected":0.97}},
),
dict(
name="Lineage Metadata",
group="Transformations and Operations", ladder_rank=19, ladder_tier="compounded",
description="""Lineage metadata is data about the lineage itself: who captured this edge, by what method, with what confidence, when; who owns this node; what classification it carries; when the edge was valid. Without it, lineage edges are anonymous assertions - with it, they are evidence. The registry's metadata model covers identity (stable IDs for nodes and edges), provenance (capture method, actor, timestamp), ownership (team, steward, on-call), classification (sensitivity labels governing who may see the lineage), temporality (validity periods), and confidence (how much to trust this edge). Metadata governance keeps the model honest: required fields per node kind, controlled vocabularies for classifications, and validation that rejects edges missing their provenance. Metadata is also what makes lineage manageable at scale - ownership metadata routes alerts, classification metadata enforces access, temporal metadata enables as-of queries.""",
how_it_works="""The registry enforces a metadata schema per node and edge kind: required provenance fields, ownership, classification, validity. Capture integrations populate metadata automatically; declaration UIs require it from humans. Validation rejects metadata-poor edges to quarantine for enrichment. Classification metadata drives access control on lineage queries - analysts see only the lineage they are cleared for. Ownership metadata routes change notifications, incident alerts, and review tasks. Metadata quality dashboards track completeness per estate area; gaps become instrumentation or declaration work. Metadata versions with the graph, so historical queries see historical metadata.""",
key_points=[
 "Lineage metadata: identity, provenance, ownership, classification, temporality, confidence.",
 "Metadata turns edges from assertions into evidence.",
 "Required fields per kind with controlled vocabularies.",
 "Classification metadata enforces access control on lineage queries.",
 "Ownership metadata routes alerts, incidents, and reviews."],
requirements=[
 "Metadata schemas per node/edge kind with required fields.",
 "Automatic population from capture integrations.",
 "Validation rejecting metadata-poor edges to quarantine.",
 "Metadata quality dashboards with gap remediation."],
standards=[
 "OpenLineage facets.",
 "W3C PROV-O."],
citations=[
 "OpenLineage. OpenLineage Specification. Linux Foundation.",
 "W3C. PROV-O: The PROV Ontology. W3C Recommendation, 2013."],
sig_lens="""The Signature reading: lineage metadata is the registry's testimony about its testimony - who witnessed each journey, how, when, and how far to trust the telling. The Signature registry never offers an anonymous assertion.""",
demo_data={"nodes":["n1","n2"],"edges":[["n1","n2"]],
 "formula":{"inputs":{"fields":6,"filled":6},"expr":"filled/fields","expected":1.0}},
),
dict(
name="Lineage at Query Time",
group="Transformations and Operations", ladder_rank=20, ladder_tier="compounded",
description="""Not all lineage is captured from pipelines - much of it happens when analysts query: the ad-hoc SQL that builds a board deck, the notebook that trains a model, the BI tool's generated queries. Query-time lineage captures these by instrumenting query engines: parsing each query's tables and columns, attributing it to the user and session, and linking its outputs (result sets, extracts, published views) back to its inputs. The challenges are volume (thousands of queries a day), ephemerality (most queries are never rerun), and attribution (distinguishing the analyst's exploration from the production extract). The registry handles volume with sampling and aggregation - full lineage for queries that write, sampled for pure reads - handles ephemerality by keeping query lineage briefly unless it feeds a persisted output, and handles attribution through engine audit logs. Query-time lineage closes the biggest completeness gap: the shadow pipelines analysts build outside the orchestrated estate.""",
how_it_works="""Query engines emit parsed lineage per query: user, session, tables/columns read, destination (result, extract, published object). The registry stores full lineage for queries that write persisted outputs and sampled lineage for reads. Session stitching links an analyst's queries into investigation chains. Published objects (saved views, extracts, decks) get permanent lineage; ephemeral results age out. Anomaly detection flags queries reading unusual data volumes or sensitive tables, routing to review. Query lineage feeds the same graph as pipeline lineage, so downstream walks from a source include the analyst extracts nobody declared.""",
key_points=[
 "Query-time lineage captures analyst SQL, notebooks, and BI queries.",
 "Full lineage for queries that write; sampled for pure reads.",
 "Session stitching links investigations; published objects get permanent lineage.",
 "Closes the shadow-pipeline completeness gap.",
 "Anomaly detection flags unusual reads for review."],
requirements=[
 "Query engine instrumentation with parsing and attribution.",
 "Write-vs-read differentiated retention.",
 "Session stitching and published-object tracking.",
 "Anomaly detection on query patterns."],
standards=[
 "OpenLineage specification."],
citations=[
 "OpenLineage. OpenLineage Specification. Linux Foundation.",
 "DAMA International. DAMA-DMBOK, 2nd ed. Technics Publications, 2017."],
sig_lens="""The Signature reading: query-time lineage is the registry watching the analysts' own journeys - every question traced to its sources, every published answer permanently mapped. The Signature registry leaves no shadow pipeline uncharted.""",
demo_data={"nodes":["analyst_q","extract"],"edges":[["analyst_q","extract"]],
 "formula":{"inputs":{"queries":1000,"sampled":100},"expr":"sampled/queries","expected":0.1}},
),
dict(
name="Lineage in ETL Tools",
group="Transformations and Operations", ladder_rank=21, ladder_tier="compounded",
description="""ETL and ELT tools are lineage-rich environments: visual pipelines declare their sources, transformations, and targets explicitly, and modern tools export that structure. The registry integrates with ETL platforms at three depths. Shallow: import the pipeline definitions as declared lineage - nodes and edges from the visual graph. Deep: instrument job runs to capture runtime lineage - which partitions were actually read and written, with row counts and timing. Deepest: extract column mappings from transformation expressions for column-level lineage. The integration must handle the platform's idioms: visual tools' generated code, ELT's push-down SQL, CDC's change streams. Platform upgrades are a maintenance risk - the integration versions against the platform's API and is tested in CI against new releases. The payoff is comprehensive: the ETL estate, often the largest lineage source, becomes the most completely traced.""",
how_it_works="""Connectors per ETL platform import definitions (shallow), subscribe to run events (deep), and parse transformation expressions (deepest). The registry normalizes platform idioms into the standard graph model. Connector versions pin to platform versions with CI testing against new releases. CDC streams get special handling: change lineage per key range with compaction. ELT push-down SQL goes through the SQL parser for column lineage. Coverage dashboards per platform show definition vs runtime vs column completeness; gaps prioritize connector improvements.""",
key_points=[
 "Three integration depths: definitions, runtime runs, column mappings.",
 "Visual declarations import as lineage; runs add partitions, counts, timing.",
 "Platform idioms (generated code, push-down SQL, CDC) need dedicated handling.",
 "Connectors version against platform APIs with CI testing.",
 "The ETL estate becomes the most completely traced."],
requirements=[
 "Per-platform connectors at three depths.",
 "Normalization of platform idioms to the graph model.",
 "Version-pinned connectors with CI against platform releases.",
 "Coverage dashboards per platform and depth."],
standards=[
 "OpenLineage specification."],
citations=[
 "OpenLineage. OpenLineage Specification. Linux Foundation.",
 "DAMA International. DAMA-DMBOK, 2nd ed. Technics Publications, 2017."],
sig_lens="""The Signature reading: ETL integration is the registry learning each platform's dialect - reading its diagrams, watching its runs, parsing its expressions. The Signature registry speaks every platform's tongue and keeps every version's grammar.""",
demo_data={"nodes":["etl_job","target"],"edges":[["etl_job","target"]],
 "formula":{"inputs":{"defs":50,"runs":48},"expr":"runs/defs","expected":0.96}},
),
dict(
name="Lineage Storage",
group="Transformations and Operations", ladder_rank=22, ladder_tier="compounded",
description="""Lineage storage must serve millisecond traversals over billion-edge graphs while retaining history for years: the registry typically pairs a graph store for topology with a columnar store for event history. The graph store holds the current graph with indexes for reachability - the hot path for impact analysis and debugging. The event store holds every lineage event immutably, supporting as-of reconstruction and audits. The design separates concerns: graph mutations from event ingestion (events are the source of truth; the graph is a materialized view), hot current state from cold history (recent graph in fast storage, ancient in cheap), and topology from properties (structure indexed separately from metadata). Retention tiers match use: the current graph forever, run-level detail for years, sampled traces for months. Backup and disaster recovery treat lineage as critical infrastructure - losing the lineage graph blinds every debugging and compliance workflow at once.""",
how_it_works="""Ingested events append to the immutable event store and upsert into the graph store; the graph is rebuildable from events at any time. Reachability indexes precompute for fast traversal; temporal indexes serve as-of queries. Tiering moves aged run detail to cold storage while keeping topology hot. Retention policies per tier execute automatically with legal-hold overrides. Backup replicates both stores with tested restores; the graph rebuild from events is exercised regularly as the ultimate recovery drill. Storage metrics - edge counts, traversal latencies, rebuild times - are monitored as infrastructure health.""",
key_points=[
 "Graph store for topology plus event store for immutable history.",
 "Events are the source of truth; the graph is a materialized view.",
 "Hot current state, cold history; topology indexed separately from properties.",
 "Retention tiers: current graph forever, run detail for years, samples for months.",
 "Lineage is critical infrastructure with tested disaster recovery."],
requirements=[
 "Dual storage: graph store plus immutable event store.",
 "Reachability and temporal indexes for fast traversal and as-of.",
 "Automated tiering and retention with legal-hold overrides.",
 "Tested backup, restore, and graph-rebuild drills."],
standards=[
 "OpenLineage specification."],
citations=[
 "OpenLineage. OpenLineage Specification. Linux Foundation.",
 "Kleppmann M. Designing Data-Intensive Applications. O'Reilly, 2017."],
sig_lens="""The Signature reading: lineage storage is the registry's vault and map-room - the immutable chronicle in the vault, the living map on the table, each rebuildable from the other. The Signature vault is never lost and never lies.""",
demo_data={"nodes":["events","graph"],"edges":[["events","graph"]],
 "formula":{"inputs":{"edges":1000000000,"ms":12},"expr":"ms","expected":12}},
),
dict(
name="Lineage Visualization",
group="Transformations and Operations", ladder_rank=23, ladder_tier="compounded",
description="""Lineage graphs are useless if humans cannot read them: visualization turns million-node graphs into comprehensible views. The core patterns are neighborhood views (this node plus N hops, the debugging default), path views (all paths between two nodes, the impact default), and estate views (aggregated by system or domain, the governance default). Good visualization collapses aggressively - a thousand-table warehouse becomes one system node until the analyst drills in - and encodes meaning in visuals: color by health or quality, thickness by volume, dashed edges for inferred lineage, badges for recent changes. Interaction matters more than rendering: search any node, expand on click, filter by confidence or time, save views for recurring investigations. The visualization is also the trust interface for non-engineers - the executive's about panel, the auditor's evidence view - so it must render journeys as stories, not hairballs.""",
how_it_works="""The visualization service renders subgraphs on demand: neighborhood, path, and estate queries from the graph API, with layout algorithms that keep views readable. Collapsing rules aggregate by system, domain, or owner with drill-down; visual encodings map health, volume, confidence, and recency. Saved views persist queries for recurring investigations and shared links. About-panels embed simplified journey views in dashboards and catalogs. Performance budgets keep renders under seconds through subgraph limits and progressive loading; the service degrades gracefully to lists when graphs exceed render limits.""",
key_points=[
 "Neighborhood, path, and estate views for debugging, impact, and governance.",
 "Aggressive collapsing with drill-down keeps views readable.",
 "Visual encodings: health color, volume thickness, dashed inferred edges, change badges.",
 "Saved views and shared links for recurring investigations.",
 "About-panels bring lineage stories to non-engineers."],
requirements=[
 "On-demand subgraph rendering with layout algorithms.",
 "Collapsing rules with drill-down by system/domain/owner.",
 "Visual encoding standards for health, volume, confidence, recency.",
 "Saved views, shared links, and embedded about-panels."],
standards=[
 "OpenLineage specification."],
citations=[
 "OpenLineage. OpenLineage Specification. Linux Foundation.",
 "Robinson I, Webber J, Eifrem E. Graph Databases, 2nd ed. O'Reilly, 2015."],
sig_lens="""The Signature reading: visualization is the registry telling its stories in pictures - journeys drawn as roads, health as color, doubt as dashes. The Signature storyteller never shows a hairball where a clear road will do.""",
demo_data={"nodes":["center","n1","n2"],"edges":[["center","n1"],["center","n2"]],
 "formula":{"inputs":{"hops":2,"nodes_shown":25},"expr":"nodes_shown-hops","expected":23}},
),
dict(
name="Lineage APIs",
group="Transformations and Operations", ladder_rank=24, ladder_tier="compounded",
description="""Lineage APIs let every system ask the graph: upstream of X, downstream of Y, path from A to B, impact of changing C, why is this number what it is. The API surface covers traversal (with direction, depth, confidence, as-of controls), search (find nodes by name, owner, tag), impact (proposed change to affected list), explanation (node to human-readable journey), and subscription (notify me when this node's upstream changes). Design rules: responses include confidence and capture method per edge so callers judge trust; traversals page through large results; as-of parameters make every query reproducible; and write APIs (for declared lineage) validate before accepting. The APIs are the integration point for the contract registry (impact analysis), the observability system (contamination tracing), the catalog (about-panels), and custom tooling - lineage becomes infrastructure other systems build on.""",
how_it_works="""The API gateway fronts traversal, search, impact, explanation, and subscription services over the graph store. Responses carry edge confidence and capture methods; large traversals page with cursors. As-of parameters pin every query to a graph version for reproducibility. Declared-lineage writes validate metadata before acceptance. Subscriptions watch nodes or subgraphs and emit change notifications. Rate limits protect the graph store; client libraries wrap the APIs with retry and pagination. API versioning follows the registry's compatibility discipline.""",
key_points=[
 "Traversal, search, impact, explanation, subscription - the lineage API surface.",
 "Responses carry confidence and capture method per edge.",
 "Paged traversals and as-of parameters for scale and reproducibility.",
 "Subscriptions notify on upstream changes.",
 "The APIs make lineage infrastructure for contracts, observability, catalogs."],
requirements=[
 "Versioned APIs over the graph store with pagination.",
 "Confidence and capture-method metadata in responses.",
 "As-of parameters on every query.",
 "Subscription service with change notifications."],
standards=[
 "OpenLineage specification.",
 "OpenAPI Specification."],
citations=[
 "OpenLineage. OpenLineage Specification. Linux Foundation.",
 "OpenAPI Initiative. OpenAPI Specification v3.1."],
sig_lens="""The Signature reading: lineage APIs are the registry's open gates - any rightful system may ask the roads, and receive answers with each road's trustworthiness sworn. The Signature gates answer swiftly and never hide a doubtful path.""",
demo_data={"nodes":["q1","q2"],"edges":[["q1","q2"]],
 "formula":{"inputs":{"p50_ms":40,"p99_ms":180},"expr":"p99_ms-p50_ms","expected":140}},
),
]
