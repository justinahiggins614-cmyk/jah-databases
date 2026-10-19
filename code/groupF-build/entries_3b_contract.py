#!/usr/bin/env python3
"""Data Contract Registry entries 13-24 (compounded)."""

APPEND = [
dict(
name="Schema Evolution Histories",
group="Schemas and Compatibility", ladder_rank=13, ladder_tier="compounded",
description="""Every schema has a biography: born with twelve fields, gained an optional email in March, deprecated the fax field in June, split name into first and last in September. The evolution history records each version with its changes, reasons, authors, and compatibility verdicts - the full story of how the data's shape changed. Histories matter for three reasons. Debugging: when a pipeline breaks, the history shows what changed and when. Compliance: auditors ask what the schema was on a past date and who approved the change. Planning: the history reveals whether a schema is stabilizing or churning, which tells consumers how much defensive coding to maintain. The registry keeps histories immutable and queryable: list versions, diff any two, show the change requests behind each version, and replay what validation would have said on any date. A schema without a history is a rumor about the past.""",
how_it_works="""The schema registry stores every version with its full schema, change log, author, approval, and compatibility check results. Diff tooling renders version-to-version changes as field-level added/removed/renamed/retyped lists with migration notes. As-of queries reconstruct the schema effective on any date for historical debugging and audits. Churn metrics - versions per quarter, breaking-change rate - feed consumer confidence dashboards. Histories link to the contract's change requests, so each version's why is one click away. Retention keeps histories as long as the data they describe, because a ten-year-old dataset's schema history is still evidence.""",
key_points=[
 "Evolution histories record every version: changes, reasons, authors, compatibility verdicts.",
 "Histories serve debugging, compliance, and churn assessment.",
 "Immutable, queryable: diff versions, as-of reconstruct, link to change requests.",
 "Churn metrics tell consumers how much defensive coding to maintain.",
 "Histories retain as long as the data they describe."],
requirements=[
 "Immutable versioned schema storage with changelogs.",
 "Diff tooling with field-level change lists and migration notes.",
 "As-of schema reconstruction for any date.",
 "Churn metrics per schema feeding consumer dashboards."],
standards=[
 "Open Data Contract Standard (ODCS).",
 "Confluent Schema Registry versioning."],
citations=[
 "Open Data Contract Standard. ODCS specification. Linux Foundation / Bitol.",
 "Apache Avro Specification."],
sig_lens="""The Signature reading: evolution histories are the schema's biography - every version, every change, every reason, written indelibly. The Signature registry lets any schema's whole life be read, diffed, and questioned.""",
demo_data={"producer":{"fields":[
   {"name":"id","type":"string","required":True},
   {"name":"v","type":"integer","required":True}]},
 "consumer":{"requires":[
   {"name":"id","type":"string"},
   {"name":"v","type":"integer"}]},
 "expect":"compatible"},
),
dict(
name="Versioning Contracts",
group="Schemas and Compatibility", ladder_rank=14, ladder_tier="compounded",
description="""Contract versions let producers evolve while consumers stay safe: version 3 adds the optional loyalty_id, version 4 deprecates fax, and each consumer pins the version it builds against. Versioning follows semantic rules adapted for data: major for breaking changes (removed fields, tightened types), minor for backward-compatible additions, patch for description fixes and threshold tuning. The registry serves every published version - a consumer pinned to v2 gets v2's schema and validators even after v5 publishes - and versions carry effective dates, change logs, and migration guides. The discipline that makes versioning work is the support window: each version declares how long it is supported, producers dual-publish during migrations, and consumers get sunset notices with deadlines. A version without a support window is abandonware; a consumer without a pinned version is building on quicksand.""",
how_it_works="""Contract versions are numbered semantically with effective dates, change logs, and migration guides. The registry stores and serves all published versions; validators run per pinned version so old consumers keep passing. Support windows declare each version's lifetime; sunset notices go out on schedule with migration deadlines. Dual-publish periods emit both old and new shapes during migrations, letting consumers cut over safely. Version adoption dashboards show which consumers are on which versions, and stale-version alerts nudge laggards. Major versions require the full change process - impact analysis, consumer sign-off, migration plan - while minor versions need only notice.""",
key_points=[
 "Semantic versioning for contracts: major breaks, minor adds, patch clarifies.",
 "The registry serves every published version; consumers pin theirs.",
 "Support windows and sunset notices make versions trustworthy.",
 "Dual-publish periods let consumers migrate safely.",
 "Adoption dashboards reveal stale consumers needing nudges."],
requirements=[
 "Semantic version numbers with effective dates and migration guides.",
 "Per-version schema and validator storage with pinned serving.",
 "Declared support windows and sunset notice schedules.",
 "Dual-publish capability during migrations."],
standards=[
 "Open Data Contract Standard (ODCS).",
 "Semantic Versioning 2.0.0 (adapted)."],
citations=[
 "Preston-Werner T. Semantic Versioning 2.0.0.",
 "Open Data Contract Standard. ODCS specification. Linux Foundation / Bitol."],
sig_lens="""The Signature reading: contract versions are the covenant's editions - each complete, each supported for its sworn span, each sunset announced in advance. The Signature registry serves every edition ever published and never strands a pinned reader.""",
demo_data={"producer":{"fields":[
   {"name":"id","type":"string","required":True},
   {"name":"loyalty_id","type":"string","required":False}]},
 "consumer":{"requires":[
   {"name":"id","type":"string"}]},
 "expect":"compatible"},
),
dict(
name="Deprecation Notices",
group="Schemas and Compatibility", ladder_rank=15, ladder_tier="compounded",
description="""Deprecation notices are how producers retire fields, versions, and behaviors without ambushing consumers. A good notice names what is deprecated, why, what replaces it, the timeline (deprecated now, removed in v5 effective January), and the migration guide. Notices go to every subscribed consumer through their declared channels - and the registry tracks acknowledgment, because an unacknowledged notice is a future outage. The deprecation lifecycle mirrors reference data: announced, deprecated (still works, warnings emitted), removed (in the announced version). Warnings are the enforcement mechanism during the deprecated phase: consumers still on the old field see deprecation warnings in their validation reports, escalating in severity as the removal date approaches. What deprecation forbids is silent removal - the number-one cause of 3 AM pages in data platforms.""",
how_it_works="""Producers file deprecation notices with the target, reason, replacement, timeline, and migration guide. The registry publishes notices to subscribed consumers and tracks acknowledgments; unacknowledged notices escalate. During the deprecated phase, validators emit warnings on use of the deprecated element, with severity rising toward the removal date. Usage dashboards show deprecated-element consumption per consumer, letting producers see who still needs help migrating. On the removal date, the element leaves the new version while old versions keep serving it for their support window. Post-removal, the notice archive preserves the full history for anyone debugging a legacy pipeline.""",
key_points=[
 "Notices name the target, reason, replacement, timeline, and migration guide.",
 "Acknowledgment is tracked; unacknowledged notices escalate.",
 "Warnings during the deprecated phase escalate toward removal.",
 "Usage dashboards show who still consumes deprecated elements.",
 "Silent removal is forbidden - the top cause of data-platform pages."],
requirements=[
 "Deprecation notice workflow with acknowledgment tracking.",
 "Escalating warnings during the deprecated phase.",
 "Per-consumer usage dashboards for deprecated elements.",
 "Notice archives preserving full deprecation history."],
standards=[
 "Open Data Contract Standard (ODCS).",
 "Semantic Versioning deprecation practices."],
citations=[
 "Open Data Contract Standard. ODCS specification. Linux Foundation / Bitol.",
 "Preston-Werner T. Semantic Versioning 2.0.0."],
sig_lens="""The Signature reading: deprecation notices are the covenant's honorable farewells - announced, explained, with the successor named and the timeline sworn. The Signature registry never lets a field die unmourned or unannounced.""",
demo_data={"producer":{"fields":[
   {"name":"email","type":"string","required":False},
   {"name":"fax","type":"string","required":False}]},
 "consumer":{"requires":[
   {"name":"email","type":"string"}]},
 "expect":"compatible"},
),
dict(
name="Breaking Change Policies",
group="Schemas and Compatibility", ladder_rank=16, ladder_tier="compounded",
description="""Breaking changes - field removals, renames, type narrowings, new required fields - are sometimes necessary, and the breaking change policy makes them survivable. The policy requires: a business justification (why the break is worth the cost), an impact analysis (which consumers, which fields, what breaks), a migration plan (dual-publish period, migration guide, consumer testing support), consumer sign-off from affected parties, and a rollback plan if the migration fails. Breaking changes ship only in major versions, only on the announced schedule, and only after the migration window closes with consumers confirmed migrated or explicitly accepting the break. The policy also defines what is never acceptable: breaking changes in patch versions, unannounced breaks, and breaks without migration support. Organizations that enforce this policy find breaking changes become rare and boring; organizations that do not find every release is an adventure.""",
how_it_works="""Producers proposing breaking changes file a change case with justification, impact analysis from consumer dependency declarations, migration plan, and rollback plan. Affected consumers review and sign off (or formally accept the break with their own remediation plans). The change ships in a major version on the scheduled release train after the migration window, with dual-publish support during the window. The registry blocks breaking changes from minor/patch versions mechanically. Post-migration, the registry verifies no consumer still depends on the removed elements before the old version's support ends. Policy violations - unannounced breaks - trigger incident reviews with the producer's leadership, because the policy only works if violations have consequences.""",
key_points=[
 "Breaking changes need justification, impact analysis, migration plan, sign-off, rollback plan.",
 "They ship only in major versions, on schedule, after migration windows close.",
 "Never acceptable: breaks in patch versions, unannounced breaks, breaks without support.",
 "The registry blocks breaking changes from minor/patch versions mechanically.",
 "Violations trigger incident reviews - the policy needs consequences to work."],
requirements=[
 "Breaking-change case workflow with consumer sign-off.",
 "Impact analysis from consumer dependency declarations.",
 "Major-version-only enforcement with scheduled release trains.",
 "Post-migration verification before old-version support ends."],
standards=[
 "Open Data Contract Standard (ODCS).",
 "Semantic Versioning 2.0.0."],
citations=[
 "Open Data Contract Standard. ODCS specification. Linux Foundation / Bitol.",
 "Preston-Werner T. Semantic Versioning 2.0.0."],
sig_lens="""The Signature reading: breaking change policy is the covenant's law of necessary revolutions - justified, announced, migrated, and consented, never sprung in the night. The Signature registry makes revolutions rare, boring, and survivable.""",
demo_data={"producer":{"fields":[
   {"name":"id","type":"string","required":True}]},
 "consumer":{"requires":[
   {"name":"id","type":"string"},
   {"name":"legacy_code","type":"string"}]},
 "expect":"incompatible:missing-legacy_code"},
),
dict(
name="Contract Testing",
group="Evolution and Governance", ladder_rank=17, ladder_tier="compounded",
description="""Contract testing verifies that producers and consumers actually honor their contracts, continuously. Producer-side tests run against every delivery: schema conformance, quality rules, freshness SLAs - the contract's promises as executable assertions. Consumer-side tests (consumer-driven contracts) run against producer candidates: the consumer declares its expectations as tests, and the producer must pass them before deploying changes - catching the case where the producer's schema is technically compatible but semantically wrong for this consumer. Both sides run in CI: producers cannot deploy a pipeline change that breaks contract tests, consumers cannot deploy code that violates their declared dependencies. Test results publish to the contract's dashboard, giving both sides a shared, current view of compliance. The tests are versioned with the contract - when the contract changes, its tests change in the same commit.""",
how_it_works="""Contract tests are authored alongside the contract: producer assertions (schema, quality, freshness) and consumer expectations (the fields and behaviors each consumer needs). Producer CI runs the assertions against candidate deliveries; consumer CI runs consumer-driven tests against producer staging. Failures block deployment with the exact violated promise. Results publish to the contract dashboard with history, so trends are visible. Tests version with the contract in the same commit - a contract change without test updates fails lint. On incidents, the failing tests become the regression suite: the fix must make them pass before the incident closes.""",
key_points=[
 "Producer tests assert schema, quality, and freshness on every delivery.",
 "Consumer-driven tests let consumers verify producers meet their specific needs.",
 "Both sides run in CI; failures block deployment.",
 "Results publish to a shared compliance dashboard with history.",
 "Tests version with the contract; incidents add regression tests."],
requirements=[
 "Executable contract tests authored with the contract.",
 "Producer and consumer CI integration with deployment blocking.",
 "Shared compliance dashboards with test history.",
 "Test-contract co-versioning enforced by lint."],
standards=[
 "Open Data Contract Standard (ODCS).",
 "Consumer-driven contract testing practices."],
citations=[
 "Open Data Contract Standard. ODCS specification. Linux Foundation / Bitol.",
 "Newman S. Building Microservices, 2nd ed. O'Reilly, 2021."],
sig_lens="""The Signature reading: contract testing is the covenant's standing trial - every delivery examined, every deployment gated, every promise proven in the open. The Signature registry tries its covenants daily and publishes the verdicts.""",
demo_data={"producer":{"fields":[
   {"name":"order_id","type":"string","required":True},
   {"name":"total","type":"decimal","required":True}]},
 "consumer":{"requires":[
   {"name":"order_id","type":"string"},
   {"name":"total","type":"decimal"}]},
 "expect":"compatible"},
),
dict(
name="Contract Linting and CI",
group="Evolution and Governance", ladder_rank=18, ladder_tier="compounded",
description="""Contract linting catches contract defects before they become production incidents: missing semantic descriptions, types outside the vocabulary, quality promises without thresholds, SLAs without measurement methods, deprecations without successors, version bumps that do not match the change severity. The linter runs in CI on every contract change, with rules in tiers: errors block publication (a required field without a type), warnings need steward acknowledgment (a quality promise weaker than the baseline), and suggestions improve craft (a description that could name its unit). Lint rules are themselves versioned and governed - changing a rule is a proposal with justification, because a new lint error can block dozens of teams' releases. The CI pipeline also runs the compatibility checker, the test suite, and the blast-radius simulation, so a contract change arrives at the registry pre-verified. Linting turns contract review from folklore into engineering.""",
how_it_works="""The linter loads the contract document and runs its rule tiers: structural (required sections present), semantic (descriptions present and meaningful, types in vocabulary), promise (thresholds, measurements, remedies specified), and evolution (version bump matches change severity, deprecations have successors). Errors fail the build; warnings require acknowledgment comments; suggestions annotate the review. The CI pipeline chains lint, compatibility check, contract tests, and blast-radius simulation, publishing a verification report with the change. Lint rules version independently; rule changes announce with migration notes and a grace period before enforcement. Teams can add local rules for their domain's conventions, namespaced so they never collide with global rules.""",
key_points=[
 "Lint tiers: errors block, warnings need acknowledgment, suggestions improve craft.",
 "Rules cover structure, semantics, promises, and evolution discipline.",
 "CI chains lint, compatibility, tests, and blast-radius simulation.",
 "Lint rules are versioned and governed; new rules get grace periods.",
 "Local namespaced rules extend global rules for domain conventions."],
requirements=[
 "A contract linter with tiered rules run in CI.",
 "Chained verification: lint, compatibility, tests, blast radius.",
 "Versioned lint rules with announced grace periods.",
 "Namespaced local rule extensions."],
standards=[
 "Open Data Contract Standard (ODCS)."],
citations=[
 "Open Data Contract Standard. ODCS specification. Linux Foundation / Bitol.",
 "DAMA International. DAMA-DMBOK, 2nd ed. Technics Publications, 2017."],
sig_lens="""The Signature reading: linting is the covenant's scribe checking every clause before sealing - structure, meaning, promises, and lawful evolution. The Signature scribe blocks flawed covenants and teaches better drafting with every suggestion.""",
demo_data={"producer":{"fields":[
   {"name":"id","type":"string","required":True}]},
 "consumer":{"requires":[
   {"name":"id","type":"string"}]},
 "expect":"compatible"},
),
dict(
name="Contract Negotiation Workflows",
group="Evolution and Governance", ladder_rank=19, ladder_tier="compounded",
description="""Contracts are negotiated, not dictated: producers propose, consumers counter, and the registry mediates. The negotiation workflow starts with a draft contract from the producer - schema, quality bars, SLAs, change policy - and routes it to declared consumers for review. Consumers annotate: the fraud team needs freshness tightened to 1 hour, the warehouse team needs the weight field it did not know it needed. The producer responds: accepts, counters with cost (tighter freshness needs pipeline investment), or declines with reasons. Rounds continue until sign-off or declared impasse, which escalates to the domain council. The workflow records every round - proposals, counters, decisions - so the final contract's rationale is auditable and future renegotiations start from history, not amnesia. Time-boxing keeps negotiation from stalling delivery: drafts get review windows, and silence after the window is consent, documented.""",
how_it_works="""The negotiation workspace hosts the draft contract with per-section commenting for consumers. Rounds are structured: proposal, review window, counter-proposals, producer response, sign-off or escalation. Each round's state, comments, and decisions persist as the negotiation record. Time boxes govern: review windows of agreed length, after which silence is recorded as consent. Impasses escalate to the domain council with the full record attached; council decisions become precedent. Signed contracts publish with the negotiation record linked, so anyone can see why the freshness SLA is 2 hours (the fraud team's 1-hour ask was declined for stated cost reasons in round 3). Renegotiation opens a new round on the live contract rather than starting over.""",
key_points=[
 "Producers propose, consumers counter, the registry mediates - contracts are negotiated.",
 "Every round is recorded: proposals, counters, decisions, rationale.",
 "Time-boxed review windows; documented silence is consent.",
 "Impasses escalate to the domain council with the full record.",
 "Renegotiation opens new rounds on live contracts with history intact."],
requirements=[
 "A negotiation workspace with per-section commenting.",
 "Structured rounds with time boxes and recorded outcomes.",
 "Escalation paths with full record attachment.",
 "Negotiation records linked to published contracts."],
standards=[
 "Open Data Contract Standard (ODCS).",
 "DAMA-DMBOK data governance guidance."],
citations=[
 "Open Data Contract Standard. ODCS specification. Linux Foundation / Bitol.",
 "DAMA International. DAMA-DMBOK, 2nd ed. Technics Publications, 2017."],
sig_lens="""The Signature reading: negotiation is the covenant's honest bargaining - proposed openly, countered freely, decided on the record. The Signature registry mediates fairly, records everything, and lets silence, properly witnessed, be consent.""",
demo_data={"producer":{"fields":[
   {"name":"txn_id","type":"string","required":True},
   {"name":"amount","type":"decimal","required":True}]},
 "consumer":{"requires":[
   {"name":"txn_id","type":"string"},
   {"name":"amount","type":"decimal"}]},
 "expect":"compatible"},
),
dict(
name="Sign-off and Approval",
group="Evolution and Governance", ladder_rank=20, ladder_tier="compounded",
description="""Sign-off makes contracts binding: the named producer owner and the named consumer representatives approve the contract's promises, and their approvals are recorded with identity, timestamp, and scope. Approval is tiered by risk: standard contracts need producer owner plus consumer leads; high-impact contracts (financial reporting data, safety data) add domain council or compliance review. Sign-off covers the whole contract - schema, quality, SLAs, change policy, breach terms - not just the schema, because the expensive promises are usually the SLAs. Re-approval is triggered by defined events: major version bumps, SLA changes, ownership changes, and annually for critical contracts - a contract signed three reorganizations ago by people who left is not a contract. The approval record is the contract's legal backbone: in a breach dispute, it shows exactly who promised what, when.""",
how_it_works="""The approval workflow routes the final contract to the required signers per the risk tier, each signing with identity and timestamp over the contract's hash - so the signature covers the exact bytes approved. Scope statements record what each signer approved (the producer owner signs the promises; consumer leads sign the dependencies). Trigger events - major versions, SLA changes, ownership changes, annual review - open re-approval rounds; expired approvals flag the contract as needing renewal. The registry blocks publication of major versions without complete sign-off. Approval records are immutable and retained with the contract; disputes consult them as the authoritative record of who promised what.""",
key_points=[
 "Sign-off binds named humans to the contract's promises with identity and timestamp.",
 "Tiered by risk: standard needs owners and leads; high-impact adds council or compliance.",
 "Signatures cover the contract's hash - the exact bytes approved.",
 "Re-approval triggers: major versions, SLA changes, ownership changes, annual review.",
 "Approval records are the contract's legal backbone in breach disputes."],
requirements=[
 "Tiered approval workflows with named signers per risk tier.",
 "Hash-based signatures over exact contract bytes.",
 "Re-approval triggers with renewal flagging.",
 "Immutable approval records retained with contracts."],
standards=[
 "Open Data Contract Standard (ODCS).",
 "ISO/IEC 27001 accountability controls."],
citations=[
 "Open Data Contract Standard. ODCS specification. Linux Foundation / Bitol.",
 "DAMA International. DAMA-DMBOK, 2nd ed. Technics Publications, 2017."],
sig_lens="""The Signature reading: sign-off is the covenant's sealing - named hands on the exact words, witnessed and timestamped. The Signature registry seals covenants properly, renews the seals on schedule, and keeps every seal forever.""",
demo_data={"producer":{"fields":[
   {"name":"acct","type":"string","required":True},
   {"name":"bal","type":"decimal","required":True}]},
 "consumer":{"requires":[
   {"name":"acct","type":"string"},
   {"name":"bal","type":"decimal"}]},
 "expect":"compatible"},
),
dict(
name="Contract Enforcement at Runtime",
group="Evolution and Governance", ladder_rank=21, ladder_tier="compounded",
description="""A contract nobody enforces is a suggestion. Runtime enforcement checks every delivery against its contract as it flows: schema validation on ingest, quality rules on each batch, freshness monitors on the clock, availability probes on the endpoints. Enforcement acts on breach per the contract's consequence tiers: warn (notify both sides, data flows), quarantine (hold the delivery for review, downstream gets the last good), block (reject the delivery, downstream gets nothing but a clear signal). The enforcement points sit at the boundaries that matter: producer egress (catch breaches before they leave), registry ingest (the authoritative check), and consumer ingress (defense in depth). Enforcement is observable: every check's verdict is logged with the contract version, so disputes are settled by evidence. And enforcement is fair: producers get the same detailed failure reports consumers would need to debug, because the goal is fixed pipelines, not blame.""",
how_it_works="""Validation services compile each contract's schema and quality rules into executable checks deployed at enforcement points. Streaming checks run per record or window; batch checks run per delivery; freshness and availability monitors run on schedules. Verdicts (pass, warn, quarantine, block) execute the contracted consequence automatically and log with contract version and evidence. Quarantined deliveries wait in the holding store for producer fix or steward override; blocked deliveries notify consumers to engage their fallback playbooks. Enforcement dashboards show pass rates per contract with breach drill-downs; chronic breaches trigger the contract's incident process. Enforcement rules version with the contract - a new contract version deploys new checks atomically.""",
key_points=[
 "Enforcement checks every delivery: schema, quality, freshness, availability.",
 "Consequence tiers execute automatically: warn, quarantine, block.",
 "Enforcement points at producer egress, registry ingest, consumer ingress.",
 "Every verdict logs with contract version - disputes settled by evidence.",
 "Failure reports go to producers in debuggable detail; the goal is fixed pipelines."],
requirements=[
 "Executable checks compiled from contracts at enforcement points.",
 "Automatic consequence execution per contracted tiers.",
 "Verdict logging with contract versions.",
 "Enforcement dashboards with breach drill-downs and incident triggers."],
standards=[
 "Open Data Contract Standard (ODCS)."],
citations=[
 "Open Data Contract Standard. ODCS specification. Linux Foundation / Bitol.",
 "DAMA International. DAMA-DMBOK, 2nd ed. Technics Publications, 2017."],
sig_lens="""The Signature reading: runtime enforcement is the covenant's standing guard - checking every delivery at the gates, executing the sworn consequences without fear or favor. The Signature guard logs every verdict, so justice is always reviewable.""",
demo_data={"producer":{"fields":[
   {"name":"id","type":"string","required":True},
   {"name":"amt","type":"decimal","required":True}]},
 "consumer":{"requires":[
   {"name":"id","type":"string"}]},
 "expect":"compatible"},
),
dict(
name="Contract Schema Registries",
group="Evolution and Governance", ladder_rank=22, ladder_tier="compounded",
description="""Schema registries are the operational home of schemas: they store every version, enforce compatibility on registration, and serve schemas to producers and consumers at runtime. In streaming platforms, producers fetch the current schema to serialize and consumers fetch schemas by version to deserialize - the registry is in the critical path of every message. Registries support the standard formats (Avro, Protobuf, JSON Schema) with format-specific compatibility rules, subject naming strategies (topic-per-schema vs shared subjects), and schema IDs embedded in messages for efficient lookup. The registry's guarantees - immutable versions, compatibility enforcement, high availability - are what make mixed-version streaming safe. Schema registries also serve the contract registry: a data contract's schema section references registry subjects and versions, so the contract's promises and the registry's enforcement stay mechanically linked.""",
how_it_works="""Producers register schemas under subjects; the registry checks compatibility against the subject's mode and rejects violations. Each version gets an immutable ID; serialized messages embed the ID so consumers fetch the exact schema for deserialization. Consumers cache schemas locally with registry fallback. Subject naming strategies isolate schemas per topic or share them across topics per policy. The registry replicates for availability and backs up version history. Contract schemas reference registry subject/version pairs, and contract validation uses the registry's compatibility verdicts - one source of truth for schema evolution across contracts and streams.""",
key_points=[
 "Schema registries store versions, enforce compatibility, serve schemas at runtime.",
 "Message-embedded schema IDs let consumers deserialize with the exact version.",
 "Format-specific rules for Avro, Protobuf, JSON Schema.",
 "Immutable versions and high availability make mixed-version streaming safe.",
 "Data contracts reference registry subjects, linking promises to enforcement."],
requirements=[
 "Subject-based schema storage with immutable version IDs.",
 "Compatibility enforcement on registration per subject mode.",
 "High-availability serving with consumer-side caching.",
 "Contract-to-registry subject references."],
standards=[
 "Confluent Schema Registry API.",
 "Apache Avro / Protobuf / JSON Schema specifications."],
citations=[
 "Apache Avro Specification.",
 "Protocol Buffers Documentation. Google."],
sig_lens="""The Signature reading: schema registries are the covenant's armory of shapes - every version kept, every new shape inspected for lawful evolution, every message carrying its shape's seal. The Signature armory never issues a shape that would break the realm's readers.""",
demo_data={"producer":{"fields":[
   {"name":"sid","type":"integer","required":True},
   {"name":"payload","type":"json","required":True}]},
 "consumer":{"requires":[
   {"name":"sid","type":"integer"}]},
 "expect":"compatible"},
),
dict(
name="Contract-Driven Pipelines",
group="Evolution and Governance", ladder_rank=23, ladder_tier="compounded",
description="""Contract-driven pipelines generate their scaffolding from contracts instead of hand-writing it: the contract's schema produces the table definitions, its quality rules produce the validation steps, its freshness SLA produces the schedule and monitors, its delivery section produces the connectors. When the contract changes, the pipeline regenerates - the drift between documentation and implementation, the source of so many incidents, disappears because they are the same artifact. The pattern inverts the usual order: instead of building a pipeline and documenting it later (never), teams write the contract first and the pipeline follows. Testing follows too: contract tests become pipeline tests automatically. The approach shines in platform teams serving hundreds of pipelines - one contract change propagates to every generated pipeline consistently, and pipeline code reviews focus on business logic instead of boilerplate.""",
how_it_works="""Pipeline generators read the contract document and emit: DDL for tables, validation steps from quality rules, schedules and monitors from SLAs, connectors from delivery specs, and tests from the contract's test section. Generated code is checked in with the contract hash stamped, so drift is detectable - hand edits to generated sections fail CI. Contract changes trigger regeneration and a diff review; only the business-logic sections need human review. The generator versions with the contract standard, and pipeline definitions declare their generator version for reproducibility. Rollback regenerates from the previous contract version, making contract reverts safe.""",
key_points=[
 "Pipelines generate from contracts: DDL, validation, schedules, connectors, tests.",
 "Contract changes regenerate pipelines - documentation and implementation cannot drift.",
 "Contract-first ordering: write the promise, then build to it.",
 "Generated sections are stamped; hand edits to them fail CI.",
 "Rollback regenerates from the previous contract version safely."],
requirements=[
 "Pipeline generators consuming contract documents.",
 "Contract-hash stamping on generated code with drift detection.",
 "Regeneration workflows with diff review on contract change.",
 "Generator versioning declared in pipeline definitions."],
standards=[
 "Open Data Contract Standard (ODCS)."],
citations=[
 "Open Data Contract Standard. ODCS specification. Linux Foundation / Bitol.",
 "DAMA International. DAMA-DMBOK, 2nd ed. Technics Publications, 2017."],
sig_lens="""The Signature reading: contract-driven pipelines are covenants that build their own enforcement - the promise generating its tables, its tests, its watches. The Signature covenant is not paperwork about the pipeline; it is the pipeline's blueprint and soul.""",
demo_data={"producer":{"fields":[
   {"name":"eid","type":"string","required":True},
   {"name":"val","type":"decimal","required":True}]},
 "consumer":{"requires":[
   {"name":"eid","type":"string"},
   {"name":"val","type":"decimal"}]},
 "expect":"compatible"},
),
dict(
name="Consumer Impact Analysis",
group="Evolution and Governance", ladder_rank=24, ladder_tier="compounded",
description="""Before changing a contract, producers must know who will feel it: consumer impact analysis traces every dependency from the proposed change to the affected consumers, dashboards, models, and downstream contracts. The analysis starts from consumer dependency declarations - which versions, which fields, which SLAs each consumer needs - and walks the graph: this field removal breaks these three consumers' queries and this ML feature; this SLA relaxation invalidates that executive dashboard's freshness assumption. Impact is classified: breaking (consumer must change), degrading (consumer still works but worse), or neutral. The analysis also finds the silent consumers - teams using the data without declared dependencies, discovered through lineage and access logs - who are the ones actually ambushed by unannounced changes. No breaking change ships without a completed impact analysis signed by the affected consumers, because the analysis is what turns a producer's guess about blast radius into a measured fact.""",
how_it_works="""The registry maintains the dependency graph from consumer declarations, lineage traces, and access logs (catching the undeclared). Proposed changes run through the impact analyzer: affected fields map to dependent consumers, each classified breaking/degrading/neutral with the evidence. Silent consumers discovered via lineage get onboarding tasks - declare your dependency or accept unannounced-change risk explicitly. The analysis report attaches to the change case; affected consumers review and sign off or negotiate. Post-change, the registry verifies predicted impacts against actual incidents, tuning the analyzer. Impact analysis runs automatically on every contract change proposal, so no change proceeds on a producer's guess.""",
key_points=[
 "Impact analysis traces proposed changes through the dependency graph to affected consumers.",
 "Impacts classify as breaking, degrading, or neutral with evidence.",
 "Lineage and access logs reveal silent consumers without declared dependencies.",
 "No breaking change ships without completed, consumer-signed analysis.",
 "Predicted vs actual impact comparison tunes the analyzer over time."],
requirements=[
 "Dependency declarations plus lineage and access-log discovery.",
 "Automated impact analysis on every change proposal.",
 "Impact classification with evidence per affected consumer.",
 "Consumer sign-off on breaking impacts before shipping."],
standards=[
 "Open Data Contract Standard (ODCS).",
 "DAMA-DMBOK data governance guidance."],
citations=[
 "Open Data Contract Standard. ODCS specification. Linux Foundation / Bitol.",
 "DAMA International. DAMA-DMBOK, 2nd ed. Technics Publications, 2017."],
sig_lens="""The Signature reading: impact analysis is the covenant's surveyor - measuring exactly whose house stands on the ground about to move. The Signature registry never breaks ground without the survey, and never ambushes even the undeclared squatter.""",
demo_data={"producer":{"fields":[
   {"name":"uid","type":"string","required":True},
   {"name":"score","type":"decimal","required":True}]},
 "consumer":{"requires":[
   {"name":"uid","type":"string"}]},
 "expect":"compatible"},
),
]
