#!/usr/bin/env python3
"""Master Data Registry entries 13-24 (compounded). Appended to entries_1_master.ENTRIES."""

APPEND = [
dict(
name="Merge and Split Operations",
group="Merge and Survivorship", ladder_rank=13, ladder_tier="compounded",
description="""Merge combines two registry entities into one when identity resolution decides they are the same real-world thing; split reverses a merge when new evidence shows they are different. Merge is the registry's most consequential write: two golden records become one, their source records re-point, their histories join, and downstream consumers receive a merge event so they can consolidate their own references. A safe merge is never a delete - the losing entity's ID is retired into an alias table pointing at the winner, so old references still resolve. Split is the undo: the alias is broken, the entity's history is divided at the evidence boundary, and each side regains its own golden record recomputed from its own sources. Both operations are steward-approved, both are fully logged with reasons, and both publish events - because a merge that consumers never hear about creates the very inconsistency the registry exists to prevent.""",
how_it_works="""A merge begins with a proposal: the pair, the match evidence, the surviving entity's recomputed golden record preview. A steward approves or rejects with a reason. On approval, the registry retires the losing ID into the alias table, re-points its source links to the winner, recomputes the winner's golden record from the union of sources, appends a merge event to both histories, and publishes the merge to subscribers. A split begins with contradicting evidence - for example, two tax IDs on one entity. The steward marks the split point; the registry divides source links by evidence, recomputes two golden records, breaks the alias, and publishes split events. Consumers handle merge events by re-pointing foreign keys and split events by re-evaluating affected transactions.""",
key_points=[
 "Merge fuses two entities; split reverses a wrong merge - both are first-class operations.",
 "Merges retire the losing ID into an alias table; old references keep resolving.",
 "Golden records are recomputed from the union of sources after a merge.",
 "Both operations require steward approval and publish events to consumers.",
 "Split divides history at the evidence boundary and recomputes both records."],
requirements=[
 "An alias table for retired IDs with permanent forwarding.",
 "Steward approval workflow with recorded reasons for merges and splits.",
 "Golden-record recomputation from source unions.",
 "Merge/split event publication to all subscribers."],
standards=[
 "DAMA-DMBOK master-data guidance.",
 "W3C PROV for merge/split provenance."],
citations=[
 "Loshin D. Master Data Management. Morgan Kaufmann, 2008.",
 "DAMA International. DAMA-DMBOK, 2nd ed. Technics Publications, 2017."],
sig_lens="""The Signature reading: merge and split are the registry's rites of union and honest divorce. The Signature registry never erases a mistaken union - it records the union, records the correction, and keeps every old name pointing true, so history is never rewritten, only amended.""",
demo_data={"attributes":[
 {"name":"merged_customer_email","candidates":[
   {"source":"EntityA-CRM","value":"ada@example.com","trust":0.92,"recency_days":3},
   {"source":"EntityB-Billing","value":"ada@example.com","trust":0.9,"recency_days":5}],
  "expected":"ada@example.com"}]},
),
dict(
name="Merge History and Audit Trails",
group="Merge and Survivorship", ladder_rank=14, ladder_tier="compounded",
description="""Every identity decision the registry makes must be answerable later: why did these two records merge, who approved it, which rule fired, what did the golden record look like before and after? The merge history is the append-only log that answers all of it. Each entry records the timestamp, the entities involved, the operation (auto-merge, steward merge, split, survivorship change), the evidence (match score, rule version, steward identity and reason), and the before/after golden record snapshots. The history is immutable - corrections are new entries, never edits - so auditors, regulators, and wronged customers can replay exactly what happened. Retention law often requires these trails for years: financial master data merges may need to be explainable a decade later. The history also feeds the learning loop: steward overturns of auto-merges become labeled data that retunes the matcher's thresholds.""",
how_it_works="""The registry writes a history event for every state change: entity created, records linked, merge proposed, merge approved, split executed, survivorship value changed, alias retired. Events carry actor (system rule version or steward ID), timestamp, evidence payload, and before/after snapshots of affected golden records. Events are hash-chained - each event includes the hash of the previous one - so tampering is detectable. A history API serves point-in-time queries: what did entity X look like on date D, and why? Retention policies keep history longer than the golden records themselves, and steward overturn events are exported nightly as training labels for the matcher.""",
key_points=[
 "Merge history logs every identity decision with actor, evidence, and before/after snapshots.",
 "History is append-only and hash-chained; corrections are new entries.",
 "Point-in-time queries replay what any entity looked like on any date.",
 "History retention outlives golden records for audit and regulatory needs.",
 "Steward overturns become training labels that improve the matcher."],
requirements=[
 "Append-only, tamper-evident history storage.",
 "Before/after golden-record snapshots on every change.",
 "Point-in-time query API over the history.",
 "Export of overturn events as matcher training data."],
standards=[
 "W3C PROV for provenance chains.",
 "ISO 27001 logging and audit trail controls."],
citations=[
 "W3C. PROV-O: The PROV Ontology. W3C Recommendation, 2013.",
 "ISO/IEC 27001. Information security management. ISO."],
sig_lens="""The Signature reading: the merge history is the registry's unalterable chronicle. In the Signature network, no identity decision is ever secret and none is ever rewritten - each is chained to the last, so any auditor can walk the chain from today back to the first merge.""",
demo_data={"attributes":[
 {"name":"audit_event_count","candidates":[
   {"source":"History","value":"merge-approved:3","trust":0.99,"recency_days":0},
   {"source":"History","value":"auto-merge:41","trust":0.99,"recency_days":0}],
  "expected":"merge-approved:3"}]},
),
dict(
name="Hierarchy Management",
group="Merge and Survivorship", ladder_rank=15, ladder_tier="compounded",
description="""Master data rarely stands alone - it rolls up. Customers belong to accounts that belong to corporate parents; products sit in categories in catalogs; locations nest in territories in regions; employees report through org charts. Hierarchy management maintains these parent-child relationships as first-class registry data with their own lifecycles: nodes can be added, moved, merged, and retired, and every change is versioned. The hard problems are real: ragged hierarchies where branches have different depths, multiple parents where a product sits in two categories, and reorganizations that move thousands of nodes at once. The registry solves them with explicit hierarchy versions - each reporting period, each catalog season gets its own tree - so last quarter's rollup stays reproducible after this quarter's reorganization. Rollup rules define how measures aggregate up the tree, and orphan detection flags nodes whose parents vanished.""",
how_it_works="""Hierarchies are stored as versioned trees: each version has an effective date range, and nodes carry parent pointers within that version. Moves are recorded as end-one-relationship/start-another pairs, never as in-place edits, so any historical tree can be reconstructed. Multiple hierarchies coexist - a product can live in the merchandising tree and the supply-chain tree simultaneously, each versioned independently. Reorganizations are applied as batch moves with a preview showing affected rollups before commit. Consumers subscribe to hierarchy versions by effective date, and rollup engines aggregate measures up whichever version the reporting period requires.""",
key_points=[
 "Hierarchies are first-class, versioned registry data: customers, products, locations, orgs.",
 "Hierarchy versions are effective-dated so historical rollups stay reproducible.",
 "Moves are recorded as end/start relationship pairs, never in-place edits.",
 "Multiple hierarchies can coexist over the same nodes.",
 "Reorganizations apply as batch moves with rollup previews before commit."],
requirements=[
 "Versioned tree storage with effective dating per hierarchy.",
 "Move operations recorded as relationship end/start pairs.",
 "Support for ragged and multi-parent hierarchies.",
 "Rollup engines that aggregate up a chosen hierarchy version."],
standards=[
 "ISO 8000 for master-data quality.",
 "DAMA-DMBOK master-data guidance."],
citations=[
 "Loshin D. Master Data Management. Morgan Kaufmann, 2008.",
 "DAMA International. DAMA-DMBOK, 2nd ed. Technics Publications, 2017."],
sig_lens="""The Signature reading: hierarchies are the registry's family trees - every entity knows its ancestors, and no reorganization erases the past. The Signature registry keeps every generation of every tree, so last quarter's truth stands untouched beside this quarter's.""",
demo_data={"attributes":[
 {"name":"region_rollup","candidates":[
   {"source":"Hierarchy-v3","value":"EMEA:142-sites","trust":0.94,"recency_days":2},
   {"source":"Hierarchy-v2","value":"EMEA:138-sites","trust":0.9,"recency_days":95}],
  "expected":"EMEA:142-sites"}]},
),
dict(
name="Cross-Domain Linking",
group="Merge and Survivorship", ladder_rank=16, ladder_tier="compounded",
description="""Entities in different domains relate to each other: a customer (party domain) has a shipping address (location domain), buys products (product domain), and is served by equipment (asset domain). Cross-domain linking maintains these relationships in the registry so analytics and operations can traverse them: which products does this customer buy, which assets serve this location, which suppliers provide this material. Links are typed (ships-to, owns, supplies, services), directed, effective-dated, and sourced - each link records which system asserted it and when. Linking is harder than it looks because the endpoints move: when two customer entities merge, all their links must re-point; when a product is retired, its links must end. The registry handles this with link maintenance rules tied to merge/split events, and with link validation that flags dangling references where an endpoint no longer exists.""",
how_it_works="""Links are stored as first-class records: link ID, source entity, target entity, relationship type, effective dates, asserting source, and confidence. On merge events, links of the retired entity are re-pointed to the survivor and the re-pointing is logged; on split events, links are divided by evidence like the entities themselves. Validation jobs scan for dangling links (endpoint retired without forwarding), temporal gaps (link effective outside entity lifespan), and type violations (a ships-to link pointing at a product). Graph queries traverse links for impact analysis - if a warehouse closes, which customers and products are affected - and the traversal results feed the observability and lineage systems.""",
key_points=[
 "Cross-domain links connect entities across party, product, location, and asset domains.",
 "Links are typed, directed, effective-dated, and carry their asserting source.",
 "Merge/split events automatically re-point or divide links.",
 "Validation flags dangling links, temporal gaps, and type violations.",
 "Graph traversal over links powers impact analysis."],
requirements=[
 "A relationship-type catalog with allowed endpoint domains per type.",
 "Link records with effective dates and provenance.",
 "Link maintenance hooks on merge/split events.",
 "Scheduled link validation and dangling-link repair."],
standards=[
 "W3C PROV for link provenance.",
 "ISO 8000 for master-data quality."],
citations=[
 "DAMA International. DAMA-DMBOK, 2nd ed. Technics Publications, 2017.",
 "Robinson I, Webber J, Eifrem E. Graph Databases, 2nd ed. O'Reilly, 2015."],
sig_lens="""The Signature reading: cross-domain links are the registry's map of how the world hangs together - customer to address, product to warehouse, asset to site. The Signature registry keeps the map current through every merge and split, so no relationship is ever left pointing at a ghost.""",
demo_data={"attributes":[
 {"name":"ships_to_link","candidates":[
   {"source":"Orders","value":"LOC-7710:active","trust":0.93,"recency_days":4},
   {"source":"CRM","value":"LOC-7709:retired","trust":0.85,"recency_days":120}],
  "expected":"LOC-7710:active"}]},
),
dict(
name="Data Stewardship Workflows",
group="Stewardship and Operations", ladder_rank=17, ladder_tier="compounded",
description="""Data stewards are the humans who own data quality for a domain: they review uncertain matches, resolve conflicting values, approve merges, and coach source systems toward better data. Stewardship workflows route work to the right steward with the right context: a review task shows the candidate pair, the match evidence, the competing values with their provenance, and the one-click actions (merge, not-a-match, escalate). Workflows enforce separation of duties where it matters - the steward who proposes a merge cannot be the one who approves it for high-risk entities. Escalation paths handle the genuinely ambiguous cases, and every decision is recorded with the steward's identity and reason, feeding both the audit trail and the matcher's training data. Good stewardship is measured: review throughput, decision overturn rates, and time-to-resolve are tracked per queue, and queues are load-balanced so no domain's quality work starves.""",
how_it_works="""The workflow engine pulls uncertain pairs from the matcher's review band and uncertain attributes from survivorship ties, packages each with full evidence, and assigns it by domain and priority. Stewards work the queue in a review console showing side-by-side records, evidence scores, and provenance. Decisions (merge, split, pick value A, escalate) execute as registry transactions with the steward's identity attached. A second steward approves high-impact merges under separation-of-duties rules. Completed decisions flow to the history log and to the matcher's training export. Queue dashboards track age, throughput, and overturn rates; when a queue's age climbs, the review band thresholds widen or narrow to match steward capacity.""",
key_points=[
 "Stewards own quality per domain and decide what automation cannot.",
 "Review tasks bundle the pair, the evidence, and one-click actions.",
 "Separation of duties: proposers cannot approve high-risk merges.",
 "Every decision is logged with steward identity and reason.",
 "Queue metrics (age, throughput, overturn rate) are tracked and load-balanced."],
requirements=[
 "Named stewards per domain with defined decision authority.",
 "A review console with evidence, provenance, and one-click actions.",
 "Separation-of-duties rules for high-impact merges.",
 "Queue dashboards with aging and capacity alerts."],
standards=[
 "DAMA-DMBOK data governance guidance.",
 "ISO 8000-8 for quality measurement of steward decisions."],
citations=[
 "DAMA International. DAMA-DMBOK, 2nd ed. Technics Publications, 2017.",
 "Loshin D. Master Data Management. Morgan Kaufmann, 2008."],
sig_lens="""The Signature reading: stewards are the registry's judges, and the workflow is its court procedure - evidence presented, both sides heard, verdict recorded with the judge's name. The Signature registry trusts its judges but verifies them, measuring every court's overturn rate.""",
demo_data={"attributes":[
 {"name":"review_decision","candidates":[
   {"source":"Steward-A","value":"merge:approved","trust":0.97,"recency_days":0},
   {"source":"Auto","value":"merge:proposed","trust":0.78,"recency_days":1}],
  "expected":"merge:approved"}]},
),
dict(
name="Steward Review Queues",
group="Stewardship and Operations", ladder_rank=18, ladder_tier="compounded",
description="""The review queue is where uncertain identity decisions wait for humans. Pairs land in the queue when match scores fall in the review band, when survivorship ties cannot break, when a consumer disputes a golden record, or when an automated quality check flags an anomaly. Queues are organized by domain and prioritized by impact: a disputed million-dollar customer's record jumps ahead of a fuzzy match on a dormant prospect. Each queue item carries a service-level target - high-impact items resolved within a day, routine items within a week - and aging items escalate automatically. The queue is also the matcher's classroom: every resolved item becomes a labeled example, and the mix of resolutions (how many merges vs rejections) tells the tuning team whether thresholds are set right. A healthy queue is small and fast; a growing queue is an early warning that data quality upstream is decaying or that thresholds need retuning.""",
how_it_works="""Items enter queues from four feeds: the matcher's review band, survivorship ties, consumer disputes, and quality-check flags. A prioritization score combines entity value, dispute severity, and item age; queues sort by it. Stewards claim items, decide, and release them; unclaimed items age and escalate to senior stewards. Resolved items export nightly as labeled training data with the decision and the evidence snapshot. Queue health metrics - inflow rate, resolution rate, median age, overturn rate - are monitored; when inflow persistently exceeds resolution, the response is to widen auto-decision thresholds (if overturns are low) or add steward capacity (if overturns are high), never to let the queue rot.""",
key_points=[
 "Queues collect review-band pairs, survivorship ties, disputes, and quality flags.",
 "Prioritization blends entity value, severity, and age.",
 "Aging items escalate automatically with service-level targets.",
 "Resolved items become labeled training data for the matcher.",
 "Queue growth is an early warning of upstream decay or threshold drift."],
requirements=[
 "Queue feeds from matcher, survivorship, disputes, and quality checks.",
 "Prioritization scoring and service-level targets per item class.",
 "Automatic escalation on aging.",
 "Nightly export of resolutions as training labels."],
standards=[
 "DAMA-DMBOK data governance guidance.",
 "ISO 8000-8 for quality measurement."],
citations=[
 "DAMA International. DAMA-DMBOK, 2nd ed. Technics Publications, 2017.",
 "Christen P. Data Matching. Springer, 2012."],
sig_lens="""The Signature reading: the review queue is the registry's docket of doubtful cases. The Signature registry hears the weightiest cases first, never lets a case rot unheard, and turns every verdict into a lesson for its automated judges.""",
demo_data={"attributes":[
 {"name":"queue_priority","candidates":[
   {"source":"Queue","value":"P1:disputed-1M-customer","trust":0.95,"recency_days":0},
   {"source":"Queue","value":"P3:fuzzy-dormant-prospect","trust":0.9,"recency_days":0}],
  "expected":"P1:disputed-1M-customer"}]},
),
dict(
name="Exception Handling",
group="Stewardship and Operations", ladder_rank=19, ladder_tier="compounded",
description="""Exceptions are the records the normal pipeline cannot process: the customer with three conflicting tax IDs, the product with no code at all, the address that parses into nothing, the feed that arrives with a new schema overnight. Exception handling gives these records a managed path instead of silent drops or poisoned golden records. Each exception is classified (data exception, schema exception, rule exception, system exception), quarantined with its full payload and the reason it failed, and routed: data exceptions to stewards, schema exceptions to integration engineers, rule exceptions to governance. Quarantine is not a trash can - it is a waiting room with a door back in: once fixed, the record re-enters the pipeline at the stage it failed, not from the start. Exception metrics (rate by source, by type, by stage) are the earliest signal of upstream breakage, and exception aging rules prevent the waiting room from becoming a graveyard.""",
how_it_works="""Pipeline stages wrap their work in validation: any record failing a stage's checks is written to the quarantine store with the stage name, the failed checks, the full payload, and a fingerprint. A classifier assigns type and severity; routers send data issues to steward queues and schema issues to engineering tickets. Stewards fix values in place (with provenance noting the manual fix) or reject the record with a reason; engineers fix mappings and replay. Repaired records re-enter at the failed stage with a replay marker so downstream stages know they are late. Quarantine dashboards show counts by source, type, and age; sources whose exception rates cross guardrails are throttled or suspended until fixed.""",
key_points=[
 "Exceptions are classified, quarantined with full payloads, and routed - never silently dropped.",
 "Data exceptions go to stewards; schema exceptions to engineers; rule exceptions to governance.",
 "Quarantine is a waiting room: fixed records re-enter at the failed stage.",
 "Exception metrics by source and type are the earliest upstream-breakage signal.",
 "Aging rules and source throttling keep quarantine from becoming a graveyard."],
requirements=[
 "Per-stage validation with quarantine writes on failure.",
 "Exception classification and routing rules.",
 "In-place fix with provenance plus replay at the failed stage.",
 "Quarantine dashboards with aging and source-throttle guardrails."],
standards=[
 "DAMA-DMBOK data quality guidance.",
 "ISO 8000-8 for quality measurement."],
citations=[
 "Olson J. Data Quality: The Accuracy Dimension. Morgan Kaufmann, 2003.",
 "DAMA International. DAMA-DMBOK, 2nd ed. Technics Publications, 2017."],
sig_lens="""The Signature reading: exceptions are the registry's lost travelers - stopped at the gate, sheltered, and given a road back in once their papers are fixed. The Signature registry turns no record away silently; every one is counted, sheltered, and guided home.""",
demo_data={"attributes":[
 {"name":"exception_route","candidates":[
   {"source":"Classifier","value":"data-exception:steward-queue","trust":0.93,"recency_days":0},
   {"source":"Classifier","value":"schema-exception:engineering","trust":0.91,"recency_days":0}],
  "expected":"data-exception:steward-queue"}]},
),
dict(
name="MDM Architecture Styles",
group="Stewardship and Operations", ladder_rank=20, ladder_tier="compounded",
description="""Three architecture styles answer the question of where the golden record lives. The registry style keeps only the identity map: source systems keep their data, and the registry stores the links saying which records are the same entity plus the survivorship decisions. It is light and non-invasive but leaves the actual values scattered. The coexistence style adds a golden-record hub alongside the sources: the hub assembles and publishes golden records while sources keep operating, and changes flow both ways through synchronization. The transaction hub style makes the hub the system of entry: all creates and updates go through the hub first, which enforces rules before anything is stored anywhere. Registry fits organizations that cannot touch legacy systems; coexistence fits most enterprises, balancing control with autonomy; transaction hub fits greenfield builds and tightly regulated domains. Hybrids are common - registry for customers, transaction hub for products - and the style can evolve as the program matures.""",
how_it_works="""Choosing a style starts from constraints: can source systems be changed, how fast must corrections propagate, who owns data entry? Registry style deploys matching and linking with read-only access to sources and publishes identity maps. Coexistence adds a golden-record store, survivorship engine, and bidirectional sync with conflict handling when a source and the hub change the same attribute. Transaction hub adds entry APIs and validation gates in front of all writes, with the hub as the sole writer to downstream systems. Migration between styles is staged: registry first to prove identity resolution, then coexistence to centralize golden records, then transaction hub for domains that need entry control - each stage reusing the previous stage's matching and rules.""",
key_points=[
 "Registry style: identity map only; sources keep their data; light and non-invasive.",
 "Coexistence style: golden-record hub alongside sources with bidirectional sync.",
 "Transaction hub style: all writes go through the hub first.",
 "Hybrids are normal: different styles per domain.",
 "Styles can evolve: registry to coexistence to transaction hub as the program matures."],
requirements=[
 "A style decision per domain based on change constraints and control needs.",
 "For coexistence: bidirectional sync with conflict handling.",
 "For transaction hub: entry APIs and validation gates on all writes.",
 "A staged migration path reusing matching and rules across stages."],
standards=[
 "DAMA-DMBOK master-data architecture guidance.",
 "ISO 8000 for master-data quality."],
citations=[
 "Loshin D. Master Data Management. Morgan Kaufmann, 2008.",
 "DAMA International. DAMA-DMBOK, 2nd ed. Technics Publications, 2017."],
sig_lens="""The Signature reading: the three styles are three postures of authority - the registry as witness, as judge, as lawgiver. The Signature network lets each domain choose its posture, and lets postures mature as the domain's discipline grows.""",
demo_data={"attributes":[
 {"name":"architecture_style","candidates":[
   {"source":"Architecture","value":"coexistence:customers","trust":0.92,"recency_days":5},
   {"source":"Architecture","value":"registry:prospects","trust":0.9,"recency_days":5}],
  "expected":"coexistence:customers"}]},
),
dict(
name="Hub-and-Spoke Synchronization",
group="Stewardship and Operations", ladder_rank=21, ladder_tier="compounded",
description="""In hub-and-spoke MDM, the golden-record hub sits at the center and each source system is a spoke. Changes flow inward: spokes publish their creates, updates, and deletes to the hub, which re-resolves identity, recomputes survivorship, and versions the golden record. Changes flow outward: the hub publishes golden-record updates to every spoke that needs them, so the CRM, the billing system, and the webshop converge on the same customer. The hard parts are conflict and ordering. When two spokes change the same attribute concurrently, the hub's conflict rules decide - usually last-writer-wins by event time, with steward review for high-stakes attributes. When events arrive out of order, the hub replays them in event-time order, not arrival order, so the golden record reflects what actually happened. Idempotent consumers and exactly-once hub processing keep retries from duplicating effects. Lag is monitored per spoke: a spoke that falls behind gets its trust decayed until it catches up.""",
how_it_works="""Spokes publish change events (create, update, delete with before/after images) to the hub's ingestion log. The hub processes the log in event-time order: identity resolution links the changed record to its entity, survivorship recomputes affected attributes, and the golden record versions forward. Outbound, the hub publishes golden-record change events per entity; spokes subscribe and apply them idempotently using event IDs. Conflict rules handle concurrent edits to the same attribute - event-time ordering plus attribute-level authority designations, with steward escalation for protected attributes like legal names. Per-spoke lag dashboards track ingestion delay; spokes exceeding their lag budget have their source trust temporarily decayed so stale data cannot win survivorship.""",
key_points=[
 "Spokes publish changes inward; the hub publishes golden records outward.",
 "Event-time ordering beats arrival ordering for correct replay.",
 "Conflict rules resolve concurrent edits, with steward escalation for protected attributes.",
 "Idempotent consumers and exactly-once hub processing make retries safe.",
 "Per-spoke lag is monitored; lagging spokes lose trust until they catch up."],
requirements=[
 "Change-event publication from every spoke with before/after images.",
 "Event-time-ordered hub processing with conflict rules.",
 "Idempotent outbound application on every spoke.",
 "Per-spoke lag monitoring with trust decay on breach."],
standards=[
 "DAMA-DMBOK data integration guidance.",
 "ISO 8000 for master-data quality."],
citations=[
 "Loshin D. Master Data Management. Morgan Kaufmann, 2008.",
 "Kleppmann M. Designing Data-Intensive Applications. O'Reilly, 2017."],
sig_lens="""The Signature reading: hub-and-spoke is the registry as the still center of a turning wheel - every spoke's news flows in, the one true record flows out. The Signature hub keeps time by event, not by arrival, so the truth it publishes is the truth as it happened.""",
demo_data={"attributes":[
 {"name":"sync_conflict","candidates":[
   {"source":"Hub","value":"event-time-winner:CRM-09:41","trust":0.95,"recency_days":0},
   {"source":"Spoke","value":"arrival-order:Billing-09:42","trust":0.7,"recency_days":0}],
  "expected":"event-time-winner:CRM-09:41"}]},
),
dict(
name="Publish-Subscribe Distribution",
group="Stewardship and Operations", ladder_rank=22, ladder_tier="compounded",
description="""Publish-subscribe distribution is how golden records reach every consumer without point-to-point plumbing. The registry publishes events - golden record created, attribute changed, entity merged, entity split, hierarchy moved - to topics, and consumers subscribe to the topics and entity selections they care about. A billing system subscribes to customer changes; a warehouse subscribes to product and location changes; an analytics platform subscribes to everything. Good distribution design separates concerns: compact change events for notification, with consumers fetching full records when they need them, keeps the bus light; schema-versioned events keep consumers decoupled from registry internals; consumer groups and offsets let each consumer track its own position and replay after outages. Dead-letter queues catch events no consumer could process, and subscription audits reveal which consumers are silently ignoring the golden records they asked for.""",
how_it_works="""The registry's event publisher writes every golden-record change to durable topics keyed by entity ID, with event schemas versioned in the schema registry. Consumers register subscriptions declaring topics, filters (domains, attributes, entity sets), and their expected lag budget. Each consumer tracks its offset; on restart it resumes where it stopped, and on demand it replays history to rebuild state. Events carry only the change (entity ID, changed attributes, before/after, version) - consumers fetch full records via the registry API when needed. A dead-letter topic collects poison events with the failure reason; subscription audits compare each consumer's offset against the topic head to flag stalled or abandoned consumers.""",
key_points=[
 "The registry publishes golden-record events; consumers subscribe by topic and filter.",
 "Change events stay compact; consumers fetch full records on demand.",
 "Versioned event schemas decouple consumers from registry internals.",
 "Offsets let consumers resume and replay after outages.",
 "Dead-letter queues and subscription audits catch poison events and stalled consumers."],
requirements=[
 "Durable topics keyed by entity ID with schema-versioned events.",
 "Consumer subscription registry with lag budgets.",
 "Offset tracking with resume and replay per consumer.",
 "Dead-letter handling and subscription auditing."],
standards=[
 "CloudEvents specification for event envelopes.",
 "DAMA-DMBOK data integration guidance."],
citations=[
 "CloudEvents. CloudEvents Specification v1.0. CNCF, 2021.",
 "Kleppmann M. Designing Data-Intensive Applications. O'Reilly, 2017."],
sig_lens="""The Signature reading: publish-subscribe is the registry as town crier - one true announcement, heard by all who listen, each listener keeping their own place in the telling. The Signature crier's words are versioned and durable, so no consumer ever misses the news.""",
demo_data={"attributes":[
 {"name":"distribution_event","candidates":[
   {"source":"Publisher","value":"golden-record-changed:v41","trust":0.97,"recency_days":0},
   {"source":"Publisher","value":"golden-record-changed:v40","trust":0.9,"recency_days":1}],
  "expected":"golden-record-changed:v41"}]},
),
dict(
name="Data Quality Dimensions in MDM",
group="Stewardship and Operations", ladder_rank=23, ladder_tier="compounded",
description="""Master data quality is measured on dimensions, each with its own tests. Accuracy: does the value match reality - is the address deliverable, the phone callable? Completeness: are required attributes populated - what share of customers have emails? Consistency: do related values agree - does the postal code match the city? Validity: do values fit their formats and domains - is the tax ID well-formed? Uniqueness: is each entity represented once - what is the duplicate rate? Timeliness: is the data fresh enough for its use - how old is the average phone verification? Each dimension gets metrics, targets, and trend lines per domain and per source, reported on quality dashboards. The dimensions also feed survivorship: a source scoring high on accuracy and completeness for an attribute earns the trust that wins survivorship ties. Quality measurement is continuous, not a project phase - sources decay, and the dashboards show it before consumers feel it.""",
how_it_works="""Quality jobs compute dimension metrics on schedules: accuracy via reference checks (address validation, phone verification samples), completeness as population rates per attribute, consistency via cross-field rules, validity via format and domain tests, uniqueness via duplicate profiling, timeliness from last-verified timestamps. Metrics land in a quality store keyed by domain, source, attribute, and date, with targets and alert thresholds per metric. Dashboards show current scores and trends; breaches page the owning steward. Metric values feed back into source trust scores for survivorship, closing the loop: measured quality becomes the weight of future testimony.""",
key_points=[
 "Six dimensions: accuracy, completeness, consistency, validity, uniqueness, timeliness.",
 "Each dimension has metrics, targets, and trend lines per domain and source.",
 "Quality dashboards surface decay before consumers feel it.",
 "Dimension scores feed survivorship trust - measured quality weights future testimony.",
 "Measurement is continuous; sources decay and the dashboards prove it."],
requirements=[
 "Dimension metric definitions per domain and attribute.",
 "Scheduled quality jobs writing to a quality store with history.",
 "Targets and alert thresholds per metric with steward paging.",
 "Feedback of quality scores into survivorship trust."],
standards=[
 "ISO 8000-8 for information quality measurement.",
 "DAMA-DMBOK data quality dimensions."],
citations=[
 "Olson J. Data Quality: The Accuracy Dimension. Morgan Kaufmann, 2003.",
 "DAMA International. DAMA-DMBOK, 2nd ed. Technics Publications, 2017."],
sig_lens="""The Signature reading: the six dimensions are the registry's six examinations of every record - true, complete, consistent, valid, singular, and timely. The Signature registry examines without ceasing, and lets the examination scores weigh each source's future testimony.""",
demo_data={"attributes":[
 {"name":"quality_score","candidates":[
   {"source":"Quality","value":"CRM-email:0.94","trust":0.94,"recency_days":1},
   {"source":"Quality","value":"Legacy-email:0.52","trust":0.52,"recency_days":1}],
  "expected":"CRM-email:0.94"}]},
),
dict(
name="Continuous Cleansing Pipelines",
group="Stewardship and Operations", ladder_rank=24, ladder_tier="compounded",
description="""Data decays: people move, marry, change names and numbers; companies merge; products are renamed. Continuous cleansing pipelines keep golden records true against that decay without waiting for a quarterly project. The pipeline watches for decay signals - returned mail, bounced emails, failed phone verifications, address-validation failures - and triggers re-verification: address hygiene services re-validate addresses, email verification pings mailboxes, phone validation checks line status. Enrichment services fill gaps: firmographic providers add company sizes, geocoders add coordinates. Every cleansing action is a sourced event with its own provenance, so a steward can see that an address changed because the postal service said the street was renamed, not because a user typed it. Cleansing runs on schedules tuned per attribute - emails monthly, addresses quarterly, tax IDs annually - and on event triggers when decay signals fire. The golden record is thus not a snapshot but a maintained asset.""",
how_it_works="""Decay signals flow into the cleansing orchestrator from delivery failures, verification services, and consumer complaints. The orchestrator schedules cleansing jobs per attribute cadence: standardization (re-parse, re-format), verification (call out to hygiene and validation services), and enrichment (fill from trusted providers). Each action writes a cleansing event with the service used, the before/after values, and the evidence, then feeds the changed values through survivorship like any source update. Services are scored like sources - a geocoder that returns rooftop coordinates earns trust; one that guesses earns little. Cleansing budgets cap spend per entity per period, and stewards review cleansing actions that would change protected attributes.""",
key_points=[
 "Data decays continuously; cleansing must run continuously, not quarterly.",
 "Decay signals: bounced mail, failed verifications, validation failures.",
 "Actions: re-standardize, re-verify via hygiene services, enrich from providers.",
 "Every cleansing action is a sourced, provenanced event.",
 "Per-attribute cadences plus event triggers; budgets cap cleansing spend."],
requirements=[
 "Decay-signal ingestion from delivery and verification systems.",
 "Hygiene, verification, and enrichment service integrations.",
 "Provenance on every cleansing action.",
 "Per-attribute cadences, event triggers, and spend budgets."],
standards=[
 "ISO 8000 for master-data quality.",
 "Universal Postal Union address hygiene guidance."],
citations=[
 "Olson J. Data Quality: The Accuracy Dimension. Morgan Kaufmann, 2003.",
 "DAMA International. DAMA-DMBOK, 2nd ed. Technics Publications, 2017."],
sig_lens="""The Signature reading: cleansing is the registry's eternal housekeeping - sweeping decay from the halls as it gathers, re-verifying every address and name on its appointed round. The Signature registry never sleeps on truth; it tends it like a garden.""",
demo_data={"attributes":[
 {"name":"cleansed_address","candidates":[
   {"source":"HygieneSvc","value":"12 Main St:Apt-4B:verified","trust":0.96,"recency_days":1},
   {"source":"CRM","value":"12 Main St:unverified","trust":0.88,"recency_days":40}],
  "expected":"12 Main St:Apt-4B:verified"}]},
),
]
