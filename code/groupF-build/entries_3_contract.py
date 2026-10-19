#!/usr/bin/env python3
"""Authored records for the Data Contract Registry databases (group F, part 1).
Public = real, fact-checked data-contract knowledge (Open Data Contract Standard,
schema registries, compatibility, SLAs). Signature = expanded Signature treatment.
Property of Justin Addam Higgins (JAH)."""

SIG_TAIL = ("Signature interpretation - original Signature-system treatment "
            "by Justin Addam Higgins; clearly labeled Signature-made, never "
            "presented as authentic public record.")

ENTRIES = [
dict(
name="What a Data Contract Is",
group="Contract Basics", ladder_rank=1, ladder_tier="foundations",
description="""A data contract is a formal agreement between a data producer and its consumers: the producer promises the data will look a certain way, mean certain things, arrive on a schedule, and meet quality bars - and the consumers build on those promises. Without contracts, every pipeline change is a potential ambush: a renamed column breaks three dashboards, a new nullability breaks a fraud model, a late feed breaks the morning report. With contracts, changes are negotiated: the producer announces, versions, and migrates; consumers declare what they depend on and get warned before it moves. A contract names the dataset, its owner, its schema (fields, types, meanings), its quality promises (freshness, completeness, validity rules), its delivery promises (schedule, format, access method), and its change policy (how breaking changes are announced and migrated). Contracts turn data sharing from tribal knowledge into engineering.""",
how_it_works="""Authoring a contract starts with the producer documenting the dataset as it actually is: schema, semantics, delivery cadence, quality characteristics. Consumers review and add their dependencies and requirements - the fraud team needs the transaction feed by 6 AM with less than 0.1 percent nulls in the amount field. Negotiation resolves conflicts, and both sides sign: the producer commits to the promises, the consumers commit to the pinned version and the migration windows. The signed contract publishes to the registry, where validation services enforce it: incoming data is checked against the schema and quality rules, breaches alert both sides, and the contract's change policy governs every evolution. Contracts are living documents - reviewed on schedule and on every incident - not write-once paperwork.""",
key_points=[
 "A data contract is a producer-consumer agreement: schema, semantics, schedule, quality, change policy.",
 "Without contracts, pipeline changes are ambushes; with them, changes are negotiated.",
 "Contracts name owners, schemas, quality bars, delivery promises, and change rules.",
 "Validation services enforce contracts; breaches alert both sides.",
 "Contracts are living: reviewed on schedule and after every incident."],
requirements=[
 "Named producers and consumers with declared dependencies.",
 "Documented schema, semantics, delivery, and quality promises.",
 "A signed publication in the contract registry.",
 "Validation enforcing the contract with breach alerting."],
standards=[
 "Open Data Contract Standard (ODCS).",
 "DAMA-DMBOK data governance guidance."],
citations=[
 "Open Data Contract Standard. ODCS specification. Linux Foundation / Bitol.",
 "DAMA International. DAMA-DMBOK, 2nd ed. Technics Publications, 2017."],
sig_lens="""The Signature reading: a data contract is a sworn covenant between maker and user of data - promises written, signed, and enforced. The Signature registry treats every contract as law: made openly, kept strictly, changed only by due process.""",
demo_data={"producer":{"fields":[
   {"name":"order_id","type":"string","required":True},
   {"name":"amount","type":"decimal","required":True},
   {"name":"currency","type":"string","required":True},
   {"name":"note","type":"string","required":False}]},
 "consumer":{"requires":[
   {"name":"order_id","type":"string"},
   {"name":"amount","type":"decimal"}]},
 "expect":"compatible"},
),
dict(
name="Producer and Consumer Roles",
group="Contract Basics", ladder_rank=2, ladder_tier="foundations",
description="""Every data contract has two sides with distinct duties. The producer owns the data's creation: it guarantees the schema, the semantics, the delivery schedule, and the quality bars, and it announces changes before making them. The producer also owns the consequences of breaking promises - the contract's breach terms say what happens when the feed is late or the schema breaks. The consumer owns its dependencies: it declares which contract version it builds against, handles the announced migration windows, and reports breaches instead of silently working around them. In practice the same team is often both: the warehouse team consumes raw feeds as a consumer and produces curated tables as a producer, holding contracts on both sides. The registry records both roles per contract with named humans behind them, because contracts between anonymous teams are unenforceable. Role clarity is what makes the whole system work: when something breaks, the contract says exactly whose promise broke.""",
how_it_works="""Contract authoring names the producer team and owner, the consumer teams and their contacts, and the dependency declarations (which version, which fields, what SLAs the consumer needs). The producer's duties - schema stability, schedule, quality, change notice - are written as testable promises with metrics. The consumer's duties - version pinning, migration participation, breach reporting - are written as obligations. The registry tracks the role graph: which teams produce what, who consumes it, and where a team is both. When a breach fires, the alert routes to the producer's on-call with the consumer impact attached; when a consumer ignores a migration window, the registry flags the stale dependency. Quarterly, role assignments are re-confirmed - teams change, and orphaned contracts get new owners or are retired.""",
key_points=[
 "Producers guarantee schema, semantics, schedule, quality, and change notice.",
 "Consumers declare versions, honor migration windows, and report breaches.",
 "Teams are often both producer and consumer, holding contracts on both sides.",
 "The registry names the humans behind each role - anonymous contracts are unenforceable.",
 "When something breaks, the contract identifies exactly whose promise broke."],
requirements=[
 "Named producer owners and consumer contacts per contract.",
 "Testable producer promises with metrics.",
 "Consumer dependency declarations with version pins.",
 "Quarterly re-confirmation of role assignments."],
standards=[
 "Open Data Contract Standard (ODCS).",
 "DAMA-DMBOK data governance guidance."],
citations=[
 "Open Data Contract Standard. ODCS specification. Linux Foundation / Bitol.",
 "DAMA International. DAMA-DMBOK, 2nd ed. Technics Publications, 2017."],
sig_lens="""The Signature reading: producers and consumers are the registry's two sworn parties - the maker bound to deliver, the user bound to declare. The Signature registry writes both names in the covenant, so no promise is ever orphaned and no breach ever anonymous.""",
demo_data={"producer":{"fields":[
   {"name":"user_id","type":"string","required":True},
   {"name":"email","type":"string","required":True}]},
 "consumer":{"requires":[
   {"name":"user_id","type":"string"},
   {"name":"email","type":"string"},
   {"name":"phone","type":"string"}]},
 "expect":"incompatible:missing-phone"},
),
dict(
name="The Open Data Contract Standard",
group="Contract Basics", ladder_rank=3, ladder_tier="foundations",
description="""The Open Data Contract Standard (ODCS) is the open specification for writing data contracts as machine-readable documents, maintained as a Linux Foundation project. An ODCS contract describes the dataset (name, version, description, owner), the schema (tables or objects with columns, types, constraints, and semantic descriptions), the data quality promises (freshness, completeness, validity rules with thresholds), the delivery and access details (frequency, format, location, credentials model), the support and SLAs, the pricing if any, and the roles and sign-offs. Because the contract is a structured document (YAML/JSON), tooling can consume it directly: validators check data against it, catalogs index it, CI pipelines lint it, and change management diffs it. ODCS gives the industry a common language so a contract written for one platform's tooling is readable by another's - the alternative is every organization inventing its own contract format and its own tooling from scratch.""",
how_it_works="""Teams author ODCS YAML documents, usually starting from a template for their platform, filling in schema from the actual dataset, quality rules from measured baselines, and SLAs from operational commitments. The contract lints in CI: schema references resolve, quality thresholds are sane, required sections are present. On merge, the contract publishes to the registry, which indexes it for discovery and wires validators to enforce it. Consumers reference the contract by name and version in their own pipeline definitions. Version bumps follow the contract's change policy; diffs between versions show consumers exactly what moved. The standard evolves through its open governance, and the registry tracks which ODCS version each contract uses.""",
key_points=[
 "ODCS is the open, machine-readable specification for data contracts (Linux Foundation).",
 "Contracts cover schema, quality, delivery, support, SLAs, roles, sign-offs.",
 "Structured YAML/JSON lets validators, catalogs, and CI consume contracts directly.",
 "A common language avoids every organization inventing its own format.",
 "The registry tracks which ODCS version each contract uses."],
requirements=[
 "ODCS documents authored from templates with real schema and measured quality bars.",
 "CI linting of contracts before publication.",
 "Registry indexing and validator wiring on publish.",
 "Version bumps following the contract's change policy."],
standards=[
 "Open Data Contract Standard (ODCS).",
 "YAML 1.2 / JSON for contract serialization."],
citations=[
 "Open Data Contract Standard. ODCS specification. Linux Foundation / Bitol.",
 "DAMA International. DAMA-DMBOK, 2nd ed. Technics Publications, 2017."],
sig_lens="""The Signature reading: ODCS is the common tongue of covenants - one format every tool can read, every registry can enforce. The Signature registry speaks it fluently and keeps every contract's dialect version on record.""",
demo_data={"producer":{"fields":[
   {"name":"event_id","type":"string","required":True},
   {"name":"ts","type":"timestamp","required":True},
   {"name":"payload","type":"json","required":False}]},
 "consumer":{"requires":[
   {"name":"event_id","type":"string"},
   {"name":"ts","type":"timestamp"}]},
 "expect":"compatible"},
),
dict(
name="Schema Guarantees",
group="Contract Basics", ladder_rank=4, ladder_tier="foundations",
description="""The schema guarantee is the contract's core promise: the data will have these fields, with these types, these meanings, and these constraints - and anything else is a breach. A schema guarantee lists every field with its name, data type, nullability, and semantic description (not just amount: decimal, but amount: decimal - the transaction total in the order's currency, minor units per ISO 4217). It states the key structure: primary keys, uniqueness constraints, and the grain of each record (one row per order line). It pins the field order for positional formats and the naming convention for the dataset. The guarantee also covers what is not in the schema: producers promise not to add undeclared fields to strict consumers without notice, and consumers promise not to depend on undeclared fields they happen to observe. Schema guarantees are tested continuously - every batch, every stream window - because a guarantee nobody checks is a wish.""",
how_it_works="""The producer declares the schema in the contract with types, nullability, descriptions, keys, and grain. Validation services compile the schema into checks run against every delivery: field presence, type conformance, nullability, key uniqueness, and grain (no duplicate keys, no missing expected keys). Failures quarantine the delivery and alert both sides with the exact violated guarantee. Schema registries version the schemas; consumers pin versions. Strict-mode consumers get extra protection: undeclared fields in the data are flagged even when declared fields all pass, catching the producer's silent additions before they become dependencies.""",
key_points=[
 "Schema guarantees pin fields, types, nullability, meanings, keys, and grain.",
 "Semantic descriptions make types meaningful (which currency? which units?).",
 "Producers promise no undeclared additions; consumers promise no undeclared dependencies.",
 "Every delivery is validated against the guarantee; breaches quarantine and alert.",
 "Strict mode flags undeclared fields before they become silent dependencies."],
requirements=[
 "Full schema declarations with semantic descriptions and key structure.",
 "Validation compiled from the schema run on every delivery.",
 "Quarantine and alerting on guarantee violations.",
 "Schema versioning with consumer version pins."],
standards=[
 "Open Data Contract Standard (ODCS).",
 "JSON Schema / Avro / Protobuf for schema expression."],
citations=[
 "Open Data Contract Standard. ODCS specification. Linux Foundation / Bitol.",
 "Apache Avro Specification."],
sig_lens="""The Signature reading: the schema guarantee is the covenant's first commandment - these fields, these types, these meanings, forever until lawfully changed. The Signature registry tests the commandment on every delivery and quarantines the oath-breakers.""",
demo_data={"producer":{"fields":[
   {"name":"sku","type":"string","required":True},
   {"name":"qty","type":"integer","required":True},
   {"name":"price","type":"decimal","required":True}]},
 "consumer":{"requires":[
   {"name":"sku","type":"string"},
   {"name":"qty","type":"integer"},
   {"name":"price","type":"decimal"},
   {"name":"discount","type":"decimal"}]},
 "expect":"incompatible:missing-discount"},
),
dict(
name="Field Definitions and Types",
group="Contract Basics", ladder_rank=5, ladder_tier="foundations",
description="""Field definitions are where contracts succeed or fail in practice. A good definition has four parts: the name (stable, snake_case, never renamed without a version bump), the type (from a controlled type vocabulary - string, integer, decimal(p,s), timestamp with zone, boolean, array, struct - never ambiguous text), the semantics (what the field means in business terms, with units and code-list references), and the constraints (nullable or not, allowed values, ranges, formats, uniqueness). Type discipline matters because types are promises about operations: a decimal(12,2) promises exact arithmetic; a timestamp promises zone-aware ordering; a string promises nothing. The contract's type vocabulary is itself reference data - the registry defines the allowed types once, so decimal means the same in every contract. Definitions also record the field's provenance (derived from which source fields by what formula) and its sensitivity classification, so downstream systems know what they are handling.""",
how_it_works="""Authors define fields using the registry's type vocabulary, writing the four parts for each field. The contract linter checks definitions: names match the naming convention, types come from the vocabulary, decimals carry precision and scale, timestamps declare zone handling, code-list fields reference registry lists, and constraints are satisfiable (a range that excludes all values fails lint). Type changes are classified by the compatibility rules: widening (integer to decimal) is backward compatible, narrowing is breaking. The published definitions feed validators, documentation, and code generators that produce typed client bindings - so the contract's types become the consumers' types, mechanically.""",
key_points=[
 "Four parts per field: name, type, semantics, constraints.",
 "Types come from a controlled vocabulary - decimal(12,2), zoned timestamps, never ambiguous text.",
 "Semantics name units and code lists; constraints name nullability, ranges, formats.",
 "Definitions record provenance and sensitivity classification.",
 "Published definitions generate typed client bindings for consumers."],
requirements=[
 "A registry-wide type vocabulary used by all contracts.",
 "Four-part definitions enforced by the contract linter.",
 "Code-list fields referencing registry lists.",
 "Compatibility classification of type changes."],
standards=[
 "Open Data Contract Standard (ODCS).",
 "ISO/IEC 11179 for field metadata."],
citations=[
 "Open Data Contract Standard. ODCS specification. Linux Foundation / Bitol.",
 "ISO/IEC 11179-3. Metadata registries: registry metamodel. ISO."],
sig_lens="""The Signature reading: field definitions are the covenant's lexicon - every word defined four ways, every type sworn from the controlled vocabulary. The Signature registry lets no ambiguous text slip into a promise.""",
demo_data={"producer":{"fields":[
   {"name":"ts","type":"timestamp","required":True},
   {"name":"ok","type":"boolean","required":True}]},
 "consumer":{"requires":[
   {"name":"ts","type":"timestamp"},
   {"name":"ok","type":"boolean"}]},
 "expect":"compatible"},
),
dict(
name="Required vs Optional Fields",
group="Contract Basics", ladder_rank=6, ladder_tier="foundations",
description="""Nullability is a contract promise with teeth: a required field must be present and non-null in every record; an optional field may be absent or null, and consumers must handle both. The discipline is to require only what the producer can truly guarantee - every required field the producer cannot always populate becomes a breach factory, quarantining good data over a field nobody needed. Conversely, marking everything optional pushes the burden to consumers, who must defensively code around missing data they actually need. The healthy pattern: require the keys and the fields consumers' correctness depends on, make the rest optional, and document the expected population rate for optional fields (this field is present in 92 percent of records) so consumers can plan. Changing nullability is a compatibility event: required-to-optional is safe for readers, optional-to-required breaks every consumer that handled nulls - and every producer that ever emits them.""",
how_it_works="""Contracts declare nullability per field with population-rate expectations for optional fields. Validators enforce requiredness on every record: a null in a required field fails the record (quarantine or reject per policy). Population-rate monitors track optional fields against their documented rates; a drop signals upstream decay before it becomes a breach. Nullability changes go through the compatibility check: relaxing (required to optional) is backward compatible and needs only notice; tightening (optional to required) is breaking and needs a migration plan with a dual-publish period. Consumers declare their null-handling in their dependency manifests so producers can see who would break.""",
key_points=[
 "Required: present and non-null in every record, enforced by validation.",
 "Optional: may be absent; consumers must handle absence.",
 "Require only what the producer can truly guarantee - required fields are breach factories otherwise.",
 "Optional fields carry documented population rates so consumers can plan.",
 "Tightening nullability is breaking; relaxing it is safe."],
requirements=[
 "Per-field nullability with population-rate expectations for optional fields.",
 "Requiredness enforced on every record with quarantine on violation.",
 "Population-rate monitoring against documented rates.",
 "Compatibility classification of nullability changes."],
standards=[
 "Open Data Contract Standard (ODCS).",
 "JSON Schema / Avro nullability semantics."],
citations=[
 "Open Data Contract Standard. ODCS specification. Linux Foundation / Bitol.",
 "Apache Avro Specification."],
sig_lens="""The Signature reading: required and optional are the covenant's must and may - must is enforced on every record, may is honored with documented odds. The Signature registry never lets a must become a wish, nor a may become a trap.""",
demo_data={"producer":{"fields":[
   {"name":"id","type":"string","required":True},
   {"name":"nick","type":"string","required":False}]},
 "consumer":{"requires":[
   {"name":"id","type":"string"}]},
 "expect":"compatible"},
),
dict(
name="Semantic Descriptions",
group="Contract Basics", ladder_rank=7, ladder_tier="foundations",
description="""Types say how data is stored; semantics say what it means. amount: decimal(12,2) is a type; amount: the order total in the order's currency, inclusive of tax, exclusive of shipping, in minor units per ISO 4217 is semantics. Without semantics, integrations guess - and guesses about money, dates, and identifiers are where the expensive bugs live. Good semantic descriptions answer: what real-world thing does this field measure, in what unit, under what definition, with what edge cases? They name the code lists fields draw from, the business rules that compute derived fields (with formulas), and the known quirks (this timestamp is the warehouse scan time, not the order time; it lags reality by up to 4 hours). Semantics are written for the consumer who has never met the producer's team - the new analyst, the partner's engineer, the model reading the field in three years. The registry treats semantic descriptions as required, not decorative: contracts without them fail lint.""",
how_it_works="""Authors write semantic descriptions answering the standard questions: what is measured, in what unit, under what definition, with what edge cases and lag? Derived fields include their formulas; coded fields reference registry lists; timestamps state what event they mark and their known lag. The linter requires descriptions on every field and flags weasel words (misc, other, various) for steward review. Descriptions publish to the data catalog, where search indexes them - analysts find fields by meaning, not just by name. When semantics change (the amount field starts including shipping), it is a contract change with a version bump and migration notes, because every consumer's interpretation just changed.""",
key_points=[
 "Semantics answer: what is measured, in what unit, under what definition, with what edge cases?",
 "Derived fields carry formulas; coded fields reference lists; timestamps name their event and lag.",
 "Written for the stranger: the new analyst, the partner engineer, the future model.",
 "Weasel words (misc, other) fail lint and go to steward review.",
 "Semantic changes are contract changes with version bumps."],
requirements=[
 "Semantic descriptions required on every field, enforced by lint.",
 "Formulas on derived fields; list references on coded fields.",
 "Catalog indexing of descriptions for meaning-based search.",
 "Version bumps on semantic changes."],
standards=[
 "Open Data Contract Standard (ODCS).",
 "ISO/IEC 11179 for semantic metadata."],
citations=[
 "Open Data Contract Standard. ODCS specification. Linux Foundation / Bitol.",
 "ISO/IEC 11179-3. Metadata registries: registry metamodel. ISO."],
sig_lens="""The Signature reading: semantic descriptions are the covenant's plain speech - what each field truly means, in words a stranger can trust. The Signature registry demands plain speech on every field and rejects weasel words at the gate.""",
demo_data={"producer":{"fields":[
   {"name":"amount","type":"decimal","required":True},
   {"name":"currency","type":"string","required":True}]},
 "consumer":{"requires":[
   {"name":"amount","type":"decimal"},
   {"name":"currency","type":"string"}]},
 "expect":"compatible"},
),
dict(
name="Data Quality Promises",
group="Contract Basics", ladder_rank=8, ladder_tier="foundations",
description="""Beyond schema, contracts promise quality: the feed will be at most 2 hours stale, amount will be non-null in 99.9 percent of records, email will match its format in 99 percent, duplicate order IDs will be zero. Quality promises are written as measurable rules with thresholds, because unmeasurable promises (data will be good) are unenforceable. Each promise names the rule, the threshold, the measurement window, and the consequence: warn, quarantine, or block. The producer commits to monitoring the promises and reporting the measurements; the consumer commits to the thresholds as its planning basis. Baselines come from history: promises are set from measured reality plus a committed improvement margin, not from wishes. When a promise is breached, the contract's incident process fires - notification, root cause, remediation, and a decision whether the promise or the pipeline needs to change.""",
how_it_works="""Authors write quality promises as rules with thresholds, windows, and severities, baselined from historical measurements. The producer's quality jobs compute the metrics on every delivery and publish them to the contract's quality dashboard. Breach policies execute per severity: warnings notify, quarantine holds the delivery for review, blocks reject it. Consumers read the dashboards as their planning basis and subscribe to breach alerts. Promise reviews happen on schedule and after incidents: sustained over-performance tightens the promise, repeated breaches trigger either pipeline fixes or promise renegotiation - the contract adapts to reality instead of pretending.""",
key_points=[
 "Quality promises are measurable rules with thresholds, windows, and consequences.",
 "Baselines come from measured history plus committed improvement, not wishes.",
 "Consequences tier: warn, quarantine, block.",
 "Producers monitor and publish measurements; consumers plan against thresholds.",
 "Reviews tighten over-performing promises and renegotiate repeatedly breached ones."],
requirements=[
 "Measurable quality rules with thresholds and severities per contract.",
 "Producer quality jobs publishing measurements per delivery.",
 "Breach policies: warn, quarantine, block with alerting.",
 "Scheduled promise reviews with renegotiation paths."],
standards=[
 "Open Data Contract Standard (ODCS).",
 "ISO 8000-8 for quality measurement."],
citations=[
 "Open Data Contract Standard. ODCS specification. Linux Foundation / Bitol.",
 "DAMA International. DAMA-DMBOK, 2nd ed. Technics Publications, 2017."],
sig_lens="""The Signature reading: quality promises are the covenant's sworn measures - each a number, each watched, each breach answered. The Signature registry sets promises from truth, tightens what excels, and renegotiates what reality will not bear.""",
demo_data={"producer":{"fields":[
   {"name":"order_id","type":"string","required":True},
   {"name":"email","type":"string","required":False}]},
 "consumer":{"requires":[
   {"name":"order_id","type":"string"}]},
 "expect":"compatible"},
),
dict(
name="Freshness SLAs",
group="SLAs and Promises", ladder_rank=9, ladder_tier="foundations",
description="""Freshness SLAs promise how current the data will be: the sales feed lands by 6 AM daily with data through midnight; the fraud stream lags reality by at most 5 minutes; the inventory snapshot refreshes hourly. A freshness SLA has three parts: the timeliness promise (data through time T available by time T plus lag), the measurement method (watermarks, max event timestamps, row-count reconciliation), and the remedy (credits, escalation, or the consumer's right to fall back to the previous good snapshot). Freshness is the most commonly breached promise because it depends on every upstream system being healthy - so contracts define degraded modes in advance: if the feed is late, the producer publishes a status with the expected recovery time, and consumers switch to their documented fallback instead of failing. Freshness dashboards show each contract's lag against its SLA in real time, and chronic lateness renegotiates the SLA or fixes the pipeline - the number must stay honest.""",
how_it_works="""Contracts declare freshness SLAs with the timeliness promise, measurement method, and remedy. Producers emit watermarks or heartbeat events; the registry's freshness monitor computes actual lag per contract and publishes it live. Breaches trigger the contracted remedy: notifications with recovery ETAs, automatic fallback signals to consumers, escalation per the support terms. Degraded-mode playbooks, written in advance, tell consumers exactly what to do when data is late - use the last good snapshot, pause the dependent job, or proceed with a staleness flag. Chronic breach reviews examine whether the SLA was unrealistic or the pipeline is under-resourced, and the contract is amended to match reality.""",
key_points=[
 "Freshness SLAs promise data-through-T available by T-plus-lag, with measurement and remedy.",
 "Watermarks and heartbeats let monitors compute actual lag live.",
 "Degraded modes are defined in advance: status, ETA, consumer fallback.",
 "Chronic lateness renegotiates the SLA or fixes the pipeline - the number stays honest.",
 "Freshness is the most breached promise; plan for breach, not just success."],
requirements=[
 "Freshness SLAs with promise, measurement, and remedy per contract.",
 "Producer watermarks or heartbeats for lag computation.",
 "Live freshness dashboards with breach alerting.",
 "Pre-written degraded-mode playbooks per consumer."],
standards=[
 "Open Data Contract Standard (ODCS).",
 "DAMA-DMBOK data quality guidance."],
citations=[
 "Open Data Contract Standard. ODCS specification. Linux Foundation / Bitol.",
 "DAMA International. DAMA-DMBOK, 2nd ed. Technics Publications, 2017."],
sig_lens="""The Signature reading: freshness SLAs are the covenant's sworn hours - the data will be this fresh, measured live, with the remedy written before the breach. The Signature registry watches the clock for every promise and keeps every number honest.""",
demo_data={"producer":{"fields":[
   {"name":"sale_id","type":"string","required":True},
   {"name":"sold_at","type":"timestamp","required":True}]},
 "consumer":{"requires":[
   {"name":"sale_id","type":"string"},
   {"name":"sold_at","type":"timestamp"}]},
 "expect":"compatible"},
),
dict(
name="Availability SLAs",
group="SLAs and Promises", ladder_rank=10, ladder_tier="foundations",
description="""Availability SLAs promise the data and its access paths will be reachable: the API serves 99.9 percent of the time, the bulk download completes daily, the registry's validation endpoint answers in under 200 milliseconds at p99. Availability covers the delivery mechanisms, not just the data's existence - a feed that exists but cannot be fetched is unavailable. The SLA defines the measurement window, the exclusions (scheduled maintenance windows, declared disasters), and the error budget: 99.9 percent monthly allows about 43 minutes of downtime, and the budget is spent deliberately on risky changes or conserved for stability. Consumers design to the SLA: retries with backoff, caching of the last good copy, and circuit breakers that stop hammering a struggling producer. Breach remedies are contractual - service credits, escalation, or the right to terminate - which is why availability promises are set from measured history, not marketing.""",
how_it_works="""Contracts declare availability targets per access path with measurement windows, exclusions, and error budgets. Synthetic probes exercise every path on a schedule, recording successes, latencies, and failures into the availability store. Burn-rate alerts fire when the error budget is being consumed too fast, paging the producer before the budget empties. Consumers implement the contracted resilience patterns: retries, caches, circuit breakers - verified in chaos exercises. Monthly availability reports show budget consumption per path; breaches trigger the contracted remedies automatically. SLA reviews adjust targets to measured reality: a path that cannot hold 99.9 percent gets 99.5 percent and an improvement plan, not a fictional 99.9.""",
key_points=[
 "Availability covers access paths, not just data existence.",
 "Error budgets quantify allowed downtime: 99.9 percent monthly is about 43 minutes.",
 "Burn-rate alerts page producers before budgets empty.",
 "Consumers build retries, caches, and circuit breakers to the SLA.",
 "Targets come from measured history; fictional nines are forbidden."],
requirements=[
 "Availability targets per access path with windows and exclusions.",
 "Synthetic probes recording into an availability store.",
 "Burn-rate alerting on error-budget consumption.",
 "Contracted remedies executed automatically on breach."],
standards=[
 "Open Data Contract Standard (ODCS).",
 "Site Reliability Engineering (error budgets)."],
citations=[
 "Beyer B et al. Site Reliability Engineering. O'Reilly, 2016.",
 "Open Data Contract Standard. ODCS specification. Linux Foundation / Bitol."],
sig_lens="""The Signature reading: availability SLAs are the covenant's sworn uptime - measured by unblinking probes, budgeted like coin, defended by burn-rate alarms. The Signature registry promises only the nines it has earned.""",
demo_data={"producer":{"fields":[
   {"name":"k","type":"string","required":True},
   {"name":"v","type":"string","required":False}]},
 "consumer":{"requires":[
   {"name":"k","type":"string"}]},
 "expect":"compatible"},
),
dict(
name="Schema Compatibility Rules",
group="Schemas and Compatibility", ladder_rank=11, ladder_tier="foundations",
description="""Compatibility rules decide which schema changes are safe and which break consumers. Backward compatibility: a new schema can read data written under the old schema - adding an optional field is backward compatible because old readers ignore it. Forward compatibility: an old schema can read data written under the new schema - adding an optional field is forward compatible too, because new writers omit it for old readers. Full compatibility is both. Breaking changes are the rest: removing a field, renaming a field, tightening a type, making an optional field required. The registry enforces a compatibility mode per contract - backward, forward, full, or none - and rejects schema registrations that violate it. The discipline saves the most pain in streaming systems, where old and new writers and readers coexist for weeks: with full compatibility enforced, mixed-version operation just works.""",
how_it_works="""Each contract declares its compatibility mode. Schema changes are checked against the current schema by the compatibility checker: additions of optional fields pass; removals, renames, type narrowings, and required-additions fail under backward mode. Failed registrations are rejected with the exact violated rule and the migration path (deprecate first, dual-publish, then remove). Compatibility is verified mechanically by the schema registry on every registration - no human judgment in the hot path. Consumers declare the versions they support so producers can see the mixed-version window they must maintain. Emergency overrides exist but require council approval and a recorded rollback plan.""",
key_points=[
 "Backward compatible: new schema reads old data. Forward compatible: old schema reads new data.",
 "Safe: adding optional fields. Breaking: removals, renames, narrowings, new required fields.",
 "The registry enforces a compatibility mode per contract and rejects violations.",
 "Mechanical checking on every registration - no human judgment in the hot path.",
 "Mixed-version windows in streaming make compatibility discipline essential."],
requirements=[
 "A declared compatibility mode per contract.",
 "Mechanical compatibility checking on schema registration.",
 "Rejection messages with the violated rule and migration path.",
 "Consumer version-support declarations showing the mixed-version window."],
standards=[
 "Open Data Contract Standard (ODCS).",
 "Confluent Schema Registry compatibility rules; Avro resolution rules."],
citations=[
 "Apache Avro Specification (schema resolution).",
 "Open Data Contract Standard. ODCS specification. Linux Foundation / Bitol."],
sig_lens="""The Signature reading: compatibility rules are the covenant's laws of change - what may evolve freely, what needs a migration, what is forbidden outright. The Signature registry enforces the laws mechanically, rejecting lawless schemas at the gate.""",
demo_data={"producer":{"fields":[
   {"name":"a","type":"string","required":True},
   {"name":"b","type":"integer","required":False}]},
 "consumer":{"requires":[
   {"name":"a","type":"string"}]},
 "expect":"compatible"},
),
dict(
name="Backward vs Forward Compatibility",
group="Schemas and Compatibility", ladder_rank=12, ladder_tier="foundations",
description="""Backward and forward compatibility protect different directions of change, and confusing them causes real outages. Backward compatibility protects readers: when the producer adds an optional field, existing consumers keep working because they ignore what they do not know. This is the common case - producers evolve, consumers lag - so most contracts enforce backward compatibility. Forward compatibility protects writers: when the producer adds an optional field, old data (written before the field existed) can still be read by new consumers, because missing optionals get defaults. This matters when consumers upgrade before producers, or when historical data must be readable by new code. Full compatibility demands both, which is the strictest useful mode: it guarantees any reader can read any writer's data within the version window. The practical rule: default to backward, require full for streams and shared topics, and treat forward-only as a special case for consumer-first upgrades.""",
how_it_works="""The compatibility checker tests both directions mechanically. For backward: can a reader on the old schema parse records written with the new schema? Optional additions pass; removals and renames fail. For forward: can a reader on the new schema parse records written with the old schema? Optional additions pass (defaults fill in); new required fields fail. The registry records the direction tested and the result with every schema version. Mixed-version matrices show which reader/writer pairs are safe, and deployment tooling consults the matrix before rolling out producers or consumers. When a breaking change is truly needed, the contract's migration process - not a compatibility exception - is the path.""",
key_points=[
 "Backward protects readers when producers evolve (the common case).",
 "Forward protects writers when consumers upgrade first or history must stay readable.",
 "Full compatibility is both - the strictest useful mode for streams and shared topics.",
 "Checked mechanically in both directions on every schema version.",
 "Breaking changes go through migration, never through compatibility exceptions."],
requirements=[
 "Declared compatibility mode per contract with direction tested.",
 "Mechanical bidirectional checks on every schema version.",
 "Mixed-version safety matrices consulted by deployment tooling.",
 "Migration processes for genuinely breaking changes."],
standards=[
 "Confluent Schema Registry compatibility types.",
 "Apache Avro schema resolution rules."],
citations=[
 "Apache Avro Specification (schema resolution).",
 "Kleppmann M. Designing Data-Intensive Applications. O'Reilly, 2017."],
sig_lens="""The Signature reading: backward and forward are the covenant's two directions of time - protecting those who read the past and those who write the future. The Signature registry guards both directions and keeps the matrix of safe passages.""",
demo_data={"producer":{"fields":[
   {"name":"x","type":"string","required":True}]},
 "consumer":{"requires":[
   {"name":"x","type":"string"},
   {"name":"y","type":"integer"}]},
 "expect":"incompatible:missing-y"},
),
]
