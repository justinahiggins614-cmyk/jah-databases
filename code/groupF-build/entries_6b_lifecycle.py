#!/usr/bin/env python3
"""Data Lifecycle Retention entries 13-24 (compounded)."""

APPEND = [
dict(
name="Deletion Workflows",
group="Archival and Deletion", ladder_rank=13, ladder_tier="compounded",
description="""Deletion is the lifecycle's final act, and it must be done right: the right records, at the right time, completely, verifiably, and never the held or the required. Deletion workflows start from disposition queues - records whose retention expired and whose reviews cleared - and execute in phases: verify eligibility (retention expired, no holds, reviews approved, no legal requirement to keep), execute deletion across all copies (primary, replicas, backups per policy, caches, derived copies), verify destruction (confirm the bytes are gone), and record the certificate of destruction. The phases matter because deletion fails in known ways: the replica nobody knew about, the backup that restores the deleted, the derived table that re-materializes it. The workflow tracks every copy location from the record's lineage and checks them off. Deletion is also reversible-until-committed: a final review window lets stewards rescue records before destruction executes.""",
how_it_works="""Disposition queues list eligible records with their eligibility evidence. Deletion jobs enumerate copy locations from lineage and storage metadata, delete each, and verify destruction per location. Backup handling follows policy: crypto-shredded keys make backups unreadable, or backups age out with documented windows. Certificates of destruction record what, when, how, and by whose authority. A final review window precedes execution for rescue. Deletion verification scans confirm absence; failures reopen the workflow. All steps log immutably for audit.""",
key_points=[
 "Deletion phases: verify eligibility, delete all copies, verify destruction, certify.",
 "Eligibility: retention expired, no holds, reviews approved, legally clear.",
 "Every copy tracked via lineage: replicas, backups, caches, derived copies.",
 "Final review window allows rescue before destruction.",
 "Certificates of destruction are the audit evidence."],
requirements=[
 "Disposition queues with eligibility evidence.",
 "Copy-location enumeration from lineage and storage metadata.",
 "Backup handling per policy (crypto-shredding or aging).",
 "Destruction certificates with immutable logging."],
standards=[
 "ISO 15489; ISO 27040 for storage security.",
 "NIST SP 800-88 for media sanitization."],
citations=[
 "NIST SP 800-88 Rev. 1. Guidelines for Media Sanitization. NIST, 2014.",
 "ISO 15489-1. Information and documentation - Records management. ISO, 2016."],
sig_lens="""The Signature reading: deletion is the registry's final rite - performed only when lawful, across every copy, verified and certified. The Signature rite rescues before it destroys and proves the destruction after.""",
demo_data={"records":[
 {"id":"R-120","created":"2010-01-01","retention_years":7,"hold":False},
 {"id":"R-121","created":"2010-01-01","retention_years":30,"hold":False}],
 "asof":"2026-10-17",
 "expect":{"R-120":"expired","R-121":"active"}},
),
dict(
name="Secure Deletion and Crypto-Shredding",
group="Archival and Deletion", ladder_rank=14, ladder_tier="compounded",
description="""Deleting the file is not enough when copies linger in backups, replicas, and archives: secure deletion ensures the data is truly unrecoverable. The methods form a ladder: logical deletion (unlink the pointer - recoverable, insufficient for sensitive data), overwriting (write patterns over the bytes - effective on magnetic media, unreliable on SSDs with wear leveling), cryptographic erasure or crypto-shredding (encrypt everything with per-record keys, then destroy the key - the ciphertext everywhere becomes unreadable instantly, including in backups), and physical destruction (degauss, crush, incinerate - for the most sensitive media). Crypto-shredding is the modern workhorse: it makes deletion instant and complete across all copies, because destroying one small key kills the data everywhere. The discipline is key management: per-record or per-class keys, keys destroyed verifiably, key destruction logged like the deletion itself. The method must match the classification: the higher the sensitivity, the stronger the method.""",
how_it_works="""Deletion policies map classifications to methods: standard data gets overwrite or logical deletion with verification; sensitive data gets crypto-shredding; top-sensitivity media gets physical destruction. Crypto-shredding architectures encrypt records with per-record keys at write time; deletion destroys the key in the key manager with dual control. Key destruction is logged and verified - the key must be unrecoverable. Media sanitization follows NIST 800-88 levels (clear, purge, destroy) matched to classification. Verification confirms unrecoverability per method; certificates record the method used.""",
key_points=[
 "Methods ladder: logical deletion, overwriting, crypto-shredding, physical destruction.",
 "Crypto-shredding kills data everywhere by destroying its key - including in backups.",
 "Method must match classification; key management is the critical discipline.",
 "NIST 800-88 levels (clear, purge, destroy) guide method selection.",
 "Key destruction is logged and verified like the deletion itself."],
requirements=[
 "Classification-to-method deletion policies.",
 "Per-record encryption keys for crypto-shredding architectures.",
 "Dual-control key destruction with verification.",
 "Method-appropriate verification and certification."],
standards=[
 "NIST SP 800-88 Rev. 1.",
 "ISO/IEC 27040."],
citations=[
 "NIST SP 800-88 Rev. 1. Guidelines for Media Sanitization. NIST, 2014.",
 "ISO/IEC 27040. Storage security. ISO."],
sig_lens="""The Signature reading: secure deletion is the registry's unmaking - thorough, verified, and matched to the secret's worth. The Signature unmaking shreds the key that locked every copy, and proves the shredding.""",
demo_data={"records":[
 {"id":"R-130","created":"2012-05-05","retention_years":7,"hold":False}],
 "asof":"2026-10-17",
 "expect":{"R-130":"expired"}},
),
dict(
name="Right to Erasure",
group="Archival and Deletion", ladder_rank=15, ladder_tier="compounded",
description="""The right to erasure (GDPR Article 17) lets individuals demand their personal data be deleted: when it is no longer necessary, when consent is withdrawn, when they object, or when it was unlawfully processed. The erasure workflow is a specialized deletion with extra duties: verify the requester's identity, find all their personal data across the estate (the hard part - data scattered across systems, backups, and derived tables), check the exceptions (the law requires keeping some data - tax records, legal claims - and erasure does not override them), execute deletion including from processors via instructions, and confirm completion to the requester within the legal deadline (one month under GDPR, extendable). Identity verification must be strong enough to prevent malicious erasure of someone else's data but not so onerous it denies the right. Every request is a case with its timeline, because regulators audit the handling, not just the outcome.""",
how_it_works="""Erasure cases open on verified identity: request intake, identity proofing, scope confirmation with the requester. Discovery searches the estate - master data, transactions, backups, derived data, processor inventories - for the requester's personal data. Exception review checks legal retention requirements against each found item; exempt items are documented, not deleted. Deletion executes across internal systems and via processor instructions; crypto-shredding handles backups. Completion confirmation goes to the requester with what was deleted and what was kept (with reasons) before the deadline. Case timelines persist for regulatory audit.""",
key_points=[
 "Erasure grounds: unnecessary, consent withdrawn, objection, unlawful processing.",
 "Discovery across the estate is the hard part - systems, backups, derived data.",
 "Exceptions: legal retention overrides erasure; document what is kept and why.",
 "Processors receive deletion instructions; completion confirmed within deadlines.",
 "Identity proofing must block malicious erasure without denying the right."],
requirements=[
 "Erasure case workflows with identity verification.",
 "Estate-wide personal data discovery.",
 "Exception review with documented keeps.",
 "Processor instruction and completion confirmation."],
standards=[
 "GDPR Article 17; ISO/IEC 27701."],
citations=[
 "Regulation (EU) 2016/679 (GDPR), Article 17.",
 "ISO/IEC 27701. Privacy information management. ISO."],
sig_lens="""The Signature reading: erasure is the registry honoring the individual's command over their own data - found everywhere, deleted thoroughly, answered in time. The Signature registry keeps what the law commands kept, deletes the rest, and proves both.""",
demo_data={"records":[
 {"id":"R-140","created":"2023-01-01","retention_years":10,"hold":False}],
 "asof":"2026-10-17",
 "expect":{"R-140":"active"}},
),
dict(
name="Tombstones and Soft Deletes",
group="Archival and Deletion", ladder_rank=16, ladder_tier="compounded",
description="""Soft deletes mark records deleted without removing them: a deleted flag, a deleted timestamp, the deleter's identity - the record stays in storage but disappears from queries. Tombstones are the distributed-systems version: explicit markers that a record was deleted, propagated to replicas so the deletion survives synchronization (without tombstones, a replica that missed the delete resurrects the record on sync). Soft deletion serves real needs: undo windows (restore the accidentally deleted), audit (who deleted what when), and sync safety. But soft deletes are not deletion for compliance: a soft-deleted personal record still exists and still counts as retained - the right to erasure needs hard deletion. The discipline is lifecycle honesty: soft delete for operational undo with a defined hard-delete follow-up, tombstones for distributed consistency with expiry, and real deletion where the law or policy requires destruction.""",
how_it_works="""Delete operations set soft-delete markers with timestamps and deleter identity; queries filter soft-deleted by default with admin override for audit. Undo restores within the window by clearing the marker. Tombstones propagate through replication with expiry after the sync horizon. Hard-delete jobs follow up: after the undo window, soft-deleted records without holds go through real deletion workflows. Compliance checks verify that erasure requests result in hard deletion, not just markers. Tombstone expiry is tuned to the replication lag - too short risks resurrection, too long wastes storage.""",
key_points=[
 "Soft deletes mark without removing: undo windows, audit, sync safety.",
 "Tombstones propagate deletions to replicas, preventing resurrection.",
 "Soft delete is not compliance deletion - the data still exists.",
 "Hard-delete follow-up completes the lifecycle after undo windows.",
 "Tombstone expiry tunes to replication lag."],
requirements=[
 "Soft-delete markers with timestamps and deleter identity.",
 "Tombstone propagation with expiry.",
 "Hard-delete follow-up jobs after undo windows.",
 "Compliance verification that erasure means hard deletion."],
standards=[
 "NIST SP 800-88 (for hard deletion)."],
citations=[
 "NIST SP 800-88 Rev. 1. Guidelines for Media Sanitization. NIST, 2014.",
 "Kleppmann M. Designing Data-Intensive Applications. O'Reilly, 2017."],
sig_lens="""The Signature reading: soft deletes are the registry's merciful pause - marked gone but restorable, until the lawful hour of true unmaking. The Signature registry never mistakes the mark for the deed where the law demands destruction.""",
demo_data={"records":[
 {"id":"R-150","created":"2024-12-01","retention_years":5,"hold":False}],
 "asof":"2026-10-17",
 "expect":{"R-150":"active"}},
),
dict(
name="Data Minimization",
group="Governance and Policy", ladder_rank=17, ladder_tier="compounded",
description="""Data minimization is the discipline of holding only what is needed: collect the minimum personal data for the purpose, keep it only as long as needed, and delete the rest. It is both a legal principle (GDPR Article 5(1)(c)) and a practical risk reducer - data you do not hold cannot leak, cannot be subpoenaed, and costs nothing to store. Minimization operates at three points. Collection: forms ask only for needed fields, features collect only needed signals, logs exclude personal data by design. Retention: schedules enforce the minimum lawful periods, and minimization reviews ask could we keep less? Processing: derived datasets drop personal fields that the purpose does not need, and aggregations replace row-level data where possible. The tension with data science is real - the model that might need this field someday - and minimization resolves it by purpose binding: keep what the declared purpose needs, with new purposes requiring new justification, not silent accumulation.""",
how_it_works="""Minimization reviews assess collections against purposes: which fields does this purpose truly need? Collection forms and pipelines drop the rest; logging pipelines strip personal data by pattern. Retention schedules encode the minimum periods; minimization audits sample holdings against purposes. Derived datasets are built with field allow-lists, not block-lists. Purpose registries record the declared purpose per dataset; new purposes trigger review before new collection. Metrics track holdings per purpose over time - the minimization trend should slope down or hold steady, never grow unexplained.""",
key_points=[
 "Minimization: collect minimum, keep minimum time, delete the rest.",
 "Operates at collection, retention, and processing.",
 "Unheld data cannot leak, be subpoenaed, or cost storage.",
 "Purpose binding resolves the keep-everything tension: new purposes need justification.",
 "Metrics track holdings per purpose; unexplained growth is investigated."],
requirements=[
 "Purpose registries with declared purposes per dataset.",
 "Collection reviews against purposes with field allow-lists.",
 "Retention schedules encoding minimum periods.",
 "Minimization audits with holdings-per-purpose metrics."],
standards=[
 "GDPR Article 5(1)(c); ISO/IEC 27701."],
citations=[
 "Regulation (EU) 2016/679 (GDPR), Article 5.",
 "ISO/IEC 27701. Privacy information management. ISO."],
sig_lens="""The Signature reading: minimization is the registry's temperance - holding only what purpose warrants, for only as long as warranted. The Signature registry counts its holdings against its purposes and finds no unaccounted wealth.""",
demo_data={"records":[
 {"id":"R-160","created":"2025-06-06","retention_years":2,"hold":False}],
 "asof":"2026-10-17",
 "expect":{"R-160":"active"}},
),
dict(
name="Retention Policies as Code",
group="Governance and Policy", ladder_rank=18, ladder_tier="compounded",
description="""Retention policies as code express schedules, triggers, holds, and dispositions in versioned, testable policy files instead of PDFs on a share drive. The policy code declares: record classes with their retention periods and triggers, hold definitions, disposition workflows, exception rules, and the jurisdictions each applies to. Because it is code, it is tested: policy unit tests verify that a 7-year financial record created in 2020 expires in 2027, that holds pause clocks, that multi-jurisdiction rules pick the strictest. Because it is versioned, every expiry decision cites the policy version applied. Because it is deployed, the lifecycle engine executes the policy mechanically - no human interprets the PDF differently each quarter. Policy changes go through the same rigor as software changes: review, test, staged rollout, with blast-radius analysis showing which records' clocks would move.""",
how_it_works="""Policy authors write retention rules in the policy language, covering classes, periods, triggers, holds, dispositions, and jurisdictions. Policy tests verify clock computations, hold interactions, and jurisdictional strictness on fixtures. CI runs the tests on every policy change; the change deploys to the lifecycle engine with versioning. The engine evaluates policies mechanically, citing versions in every decision. Blast-radius analysis previews clock changes before activation. Policy versions retain with the decisions they produced, so historical expiries are explainable.""",
key_points=[
 "Policies expressed as versioned, testable code - not PDFs.",
 "Unit tests verify clock math, hold pauses, jurisdictional strictness.",
 "The engine executes policy mechanically; every decision cites its version.",
 "Changes get review, test, staged rollout, blast-radius analysis.",
 "Historical decisions remain explainable via versioned policies."],
requirements=[
 "A policy language covering classes, periods, triggers, holds, dispositions.",
 "Policy unit tests on fixtures.",
 "CI on policy changes with blast-radius analysis.",
 "Versioned deployment with decision citation."],
standards=[
 "ISO 15489; Open Policy Agent patterns."],
citations=[
 "ISO 15489-1. Information and documentation - Records management. ISO, 2016.",
 "Open Policy Agent documentation."],
sig_lens="""The Signature reading: policies as code are the registry's laws engraved in executable bronze - tested, versioned, executed without favoritism. The Signature laws cite themselves in every judgment.""",
demo_data={"records":[
 {"id":"R-170","created":"2021-09-09","retention_years":5,"hold":False}],
 "asof":"2026-10-17",
 "expect":{"R-170":"expired"}},
),
dict(
name="Policy Enforcement Engines",
group="Governance and Policy", ladder_rank=19, ladder_tier="compounded",
description="""The enforcement engine is the machinery that turns retention policy into action: evaluating clocks, queuing expiries, blocking held deletions, executing dispositions, and logging everything. The engine runs on schedules tuned to the business - daily evaluation for most estates, hourly for high-velocity data - processing records in priority order: holds first (verify still frozen), then expiries, then dispositions. Enforcement is transactional: each action verifies preconditions (still expired? still unheld? approvals current?) immediately before executing, because the world changes between queueing and execution. The engine is observable: dashboards show queue depths, action rates, and block reasons; alerts fire on engine failures, because a silent engine means retention silently stops. And the engine is conservative: on any doubt - ambiguous hold status, conflicting policies - it blocks and escalates rather than deleting.""",
how_it_works="""The engine loads versioned policies, evaluates record clocks, and builds action queues: verify-holds, expire, review, dispose. Each action re-verifies preconditions transactionally before executing. Hold checks are mechanical - deletion jobs cannot proceed on held records, enforced in code, not convention. Execution logs every action with policy version and preconditions checked. Dashboards track queues and rates; engine health alerts on failures. Ambiguity handling defaults to block-and-escalate. Engine upgrades deploy with dual-run verification: old and new engines evaluate in parallel until results match.""",
key_points=[
 "Engines evaluate clocks, queue expiries, block held deletions, execute dispositions.",
 "Preconditions re-verified transactionally immediately before each action.",
 "Hold blocking enforced in code, not convention.",
 "Ambiguity defaults to block-and-escalate, never to delete.",
 "Engine health monitored; failures alert because silent engines stop retention."],
requirements=[
 "Scheduled evaluation with prioritized action queues.",
 "Transactional precondition verification per action.",
 "Mechanical hold blocking in deletion paths.",
 "Engine health monitoring with alerting."],
standards=[
 "ISO 15489."],
citations=[
 "ISO 15489-1. Information and documentation - Records management. ISO, 2016.",
 "DAMA International. DAMA-DMBOK, 2nd ed. Technics Publications, 2017."],
sig_lens="""The Signature reading: the enforcement engine is the registry's tireless bailiff - serving every writ of expiry, honoring every injunction, doubting before destroying. The Signature bailiff's own health is watched, for a sleeping bailiff serves no law.""",
demo_data={"records":[
 {"id":"R-180","created":"2017-02-02","retention_years":7,"hold":True},
 {"id":"R-181","created":"2017-02-02","retention_years":7,"hold":False}],
 "asof":"2026-10-17",
 "expect":{"R-180":"held","R-181":"expired"}},
),
dict(
name="Lifecycle Events and Logs",
group="Governance and Policy", ladder_rank=20, ladder_tier="compounded",
description="""Lifecycle events are the record's biography in machine form: created, classified, accessed, updated, expired, archived, held, released, deleted - each with timestamp, actor, and details. The event log is append-only and immutable; corrections are new events, never edits. The log serves operations (what is happening to records now?), incidents (what happened before the breach?), audits (prove the retention schedule was followed), and analytics (how long do records really live?). Event volume is large - every access could be an event - so the log tiers: lifecycle transitions logged fully and retained long, routine accesses sampled or aggregated. The log's integrity is protected by hash chaining, because a lifecycle log that can be edited can hide a spoliation. Retention applies to the log itself: kept as long as the longest-lived record it describes, plus the audit tail.""",
how_it_works="""Lifecycle services emit events on every transition with timestamps, actors, and details; access events sample per policy. The log store appends immutably with hash chaining for tamper evidence. Tiering keeps transition events hot and long, access aggregates warm. Audit queries reconstruct any record's full biography; incident queries show pre-breach activity. Log retention follows the longest described record plus audit tail. Log integrity verification runs on schedule, detecting any tampering.""",
key_points=[
 "Events: created, classified, accessed, updated, expired, archived, held, released, deleted.",
 "Append-only, hash-chained, immutable - corrections are new events.",
 "Tiered: transitions fully logged long; accesses sampled.",
 "Serves operations, incidents, audits, and analytics.",
 "Log retention follows the longest-lived record described plus audit tail."],
requirements=[
 "Event emission on all lifecycle transitions.",
 "Immutable hash-chained log storage with tiering.",
 "Biography reconstruction queries for audit.",
 "Integrity verification on schedule."],
standards=[
 "ISO 15489.",
 "W3C PROV-O for event modeling."],
citations=[
 "ISO 15489-1. Information and documentation - Records management. ISO, 2016.",
 "W3C. PROV-O: The PROV Ontology. W3C Recommendation, 2013."],
sig_lens="""The Signature reading: lifecycle events are each record's sworn biography - every passage witnessed, the chronicle chained against tampering. The Signature biographer omits nothing material and alters nothing written.""",
demo_data={"records":[
 {"id":"R-190","created":"2026-04-04","retention_years":3,"hold":False}],
 "asof":"2026-10-17",
 "expect":{"R-190":"active"}},
),
dict(
name="Lifecycle Metadata",
group="Governance and Policy", ladder_rank=21, ladder_tier="compounded",
description="""Lifecycle metadata is the data that drives the lifecycle: record class, creation date, retention trigger and clock, current stage, hold flags with matter references, disposition instructions, and the policy version in force. The metadata model distinguishes birth metadata (immutable: what it is, when born, who made it) from lifecycle state (mutable: stage, clock, holds) from policy linkage (which schedule version governs). Quality rules keep the metadata honest: every record has a class, every class maps to a schedule, clocks are computable, holds reference real matters. Metadata travels with the record through tiers and archives - a record without its lifecycle metadata in the archive is a time bomb nobody can defuse. The registry validates metadata completeness on schedule, and gaps become registration repair work.""",
how_it_works="""The metadata schema defines birth, state, and policy-linkage fields per record. Creation populates birth metadata; the engine maintains state; policy linkage updates on schedule versions. Validation jobs check completeness and consistency: class present, schedule mapped, clock computable, holds valid. Metadata migrates with records across tiers and into archives as part of the package. Repair workflows fix gaps from best-available evidence with the repair noted. Metadata APIs let applications read lifecycle state (is this record held?) before acting.""",
key_points=[
 "Birth metadata immutable; lifecycle state mutable; policy linkage versioned.",
 "Every record has a class; every class maps to a schedule; clocks computable.",
 "Metadata travels with records across tiers and archives.",
 "Completeness validated on schedule; gaps become repair work.",
 "Applications check lifecycle state via APIs before acting."],
requirements=[
 "Lifecycle metadata schemas with birth/state/policy sections.",
 "Completeness and consistency validation jobs.",
 "Metadata migration with records across tiers.",
 "Repair workflows with noted evidence."],
standards=[
 "ISO 15489; ISO/IEC 11179."],
citations=[
 "ISO 15489-1. Information and documentation - Records management. ISO, 2016.",
 "ISO/IEC 11179-3. Metadata registries: registry metamodel. ISO."],
sig_lens="""The Signature reading: lifecycle metadata is each record's traveling papers - birth, standing, and governing law, carried through every tier and archive. The Signature registry lets no record travel without papers.""",
demo_data={"records":[
 {"id":"R-200","created":"2023-07-07","retention_years":5,"hold":False}],
 "asof":"2026-10-17",
 "expect":{"R-200":"active"}},
),
dict(
name="Lifecycle for Backups",
group="Governance and Policy", ladder_rank=22, ladder_tier="compounded",
description="""Backups complicate lifecycles: the record deleted from primary still lives in last night's backup, and restoring that backup resurrects the deleted. Backup lifecycle policy resolves this with clear rules. Retention alignment: backup retention meets or exceeds the longest record retention it contains - a 7-year record needs backups kept 7 years or crypto-shredding that kills deleted records within them. Deletion propagation: erasure and legal deletion must reach backups - via crypto-shredding (destroy the key, the backup's copy dies), via aging (backups expire before the deletion matters), or via documented restore-filtering (restores exclude deleted records). Hold handling: legal holds extend to backups - held records' backups are preserved and their destruction blocked. Backup catalogs record what each backup contains and when it expires, so disposition can verify. The policy is honest about the physics: backups are point-in-time copies, and lifecycle applies to them as surely as to primaries.""",
how_it_works="""Backup policies define retention, deletion propagation method, and hold handling per backup tier. Crypto-shredding architectures make per-record deletion in backups trivial via key destruction. Aging policies expire backups on schedule with catalog verification. Restore procedures filter deleted and held records per current lifecycle state - restores never resurrect the lawfully deleted. Backup catalogs track contents and expiry; disposition verification checks catalogs. Hold orders propagate to backup systems, blocking backup destruction that would kill held records.""",
key_points=[
 "Backup retention meets the longest record retention within, or crypto-shredding covers deletion.",
 "Deletion must reach backups: key destruction, aging, or restore-filtering.",
 "Legal holds extend to backups mechanically.",
 "Restores never resurrect lawfully deleted records.",
 "Backup catalogs track contents and expiry for disposition verification."],
requirements=[
 "Backup lifecycle policies with retention and propagation methods.",
 "Crypto-shredding or aging for deletion in backups.",
 "Hold propagation to backup systems.",
 "Restore filtering against current lifecycle state."],
standards=[
 "NIST SP 800-88.",
 "ISO 15489."],
citations=[
 "NIST SP 800-88 Rev. 1. Guidelines for Media Sanitization. NIST, 2014.",
 "ISO 15489-1. Information and documentation - Records management. ISO, 2016."],
sig_lens="""The Signature reading: backup lifecycle is the registry's honesty about copies - the deleted stays deleted even in yesterday's backup, the held stays held even in the vault. The Signature registry lets no backup become a resurrection machine.""",
demo_data={"records":[
 {"id":"R-210","created":"2014-09-09","retention_years":7,"hold":False}],
 "asof":"2026-10-17",
 "expect":{"R-210":"expired"}},
),
dict(
name="Lifecycle for Derived Data",
group="Governance and Policy", ladder_rank=23, ladder_tier="compounded",
description="""Derived data - aggregates, features, reports, model outputs - inherits lifecycle obligations from its sources, and the inheritance is where organizations most often fail. The rules: derived data containing personal data inherits the strictest source retention (the aggregate of 7-year transactions keeps 7 years, not forever); erasure propagates downstream (delete the customer, delete their rows from derived tables or recompute); holds propagate downstream (the held transaction's aggregates are held too). Recomputation is the cleanest compliance: derived data rebuilt from sources on demand needs no independent retention - delete it freely, rebuild when needed. Where recomputation is impossible (the source is gone), the derived data takes the source's schedule as its own. Lineage is the enforcement mechanism: lifecycle engines walk downstream from source transitions to find derived data needing the same treatment. Derived data without lineage is a compliance blind spot.""",
how_it_works="""Lineage maps sources to derived datasets; lifecycle engines propagate transitions downstream: expiries, holds, erasures all flow to derived data. Recomputable derivatives are marked as such and deleted freely; non-recomputable ones inherit schedules. Erasure workflows traverse downstream deleting or recomputing personal data. Hold propagation freezes derived datasets containing held source data. Compliance checks verify propagation completeness; gaps are lineage gaps first, lifecycle gaps second.""",
key_points=[
 "Derived data inherits the strictest source retention and all holds and erasures.",
 "Recomputable derivatives delete freely; non-recomputable inherit schedules.",
 "Erasure and holds propagate downstream via lineage.",
 "Lineage is the enforcement mechanism; missing lineage is a blind spot.",
 "Propagation completeness is compliance-checked."],
requirements=[
 "Lineage from sources to all derived datasets.",
 "Propagation of expiry, hold, and erasure downstream.",
 "Recomputability marking with free-deletion for recomputable.",
 "Propagation completeness checks."],
standards=[
 "ISO 15489.",
 "GDPR (erasure propagation)."],
citations=[
 "Regulation (EU) 2016/679 (GDPR), Article 17.",
 "ISO 15489-1. Information and documentation - Records management. ISO, 2016."],
sig_lens="""The Signature reading: derived lifecycle is the registry's doctrine of inherited fate - children of data sharing their parents' spans, their pardons, and their unmakings. The Signature registry traces every descendant and leaves no heir unaccounted.""",
demo_data={"records":[
 {"id":"R-220","created":"2022-11-11","retention_years":3,"hold":False}],
 "asof":"2026-10-17",
 "expect":{"R-220":"expired"}},
),
dict(
name="Lifecycle Notifications",
group="Governance and Policy", ladder_rank=24, ladder_tier="compounded",
description="""Lifecycle notifications keep humans in the loop: expiry warnings to owners, hold notices to custodians, disposition reviews to stewards, deletion confirmations to requesters, policy changes to everyone affected. Notification design follows the stakes: warnings go out early and repeatedly (90/30/7 days), holds notify immediately with acknowledgment required, deletions confirm after the fact with certificates. Each notification states what, why, when, and what action is needed - the owner who gets an expiry warning knows exactly which records, under which schedule, expiring when, and how to extend or accept. Notification fatigue is managed like alert fatigue: notifications are batched, prioritized, and tuned - the owner of ten thousand expiring records gets a summary with drill-down, not ten thousand emails. Delivery is tracked: unacknowledged hold notices escalate, because an unheeded hold is a spoliation risk.""",
how_it_works="""Notification rules per lifecycle event define recipients, timing, content, and acknowledgment requirements. Batching aggregates per owner with drill-down links. Escalation fires on unacknowledged critical notices (holds). Delivery tracking records sent, delivered, acknowledged; failures retry through alternate channels. Fatigue management tunes frequency from acknowledgment rates. Notification templates version with the policies they describe, so the notice always matches the current rule.""",
key_points=[
 "Notifications per event: expiry warnings, hold notices, reviews, confirmations, policy changes.",
 "Each states what, why, when, and the action needed.",
 "Batched and prioritized to fight fatigue; drill-downs over email floods.",
 "Unacknowledged hold notices escalate - unheeded holds risk spoliation.",
 "Delivery tracked; templates versioned with policies."],
requirements=[
 "Notification rules per lifecycle event with acknowledgment tiers.",
 "Batching with drill-down for high-volume owners.",
 "Escalation on unacknowledged critical notices.",
 "Delivery tracking with alternate-channel retry."],
standards=[
 "ISO 15489."],
citations=[
 "ISO 15489-1. Information and documentation - Records management. ISO, 2016.",
 "The Sedona Conference. Commentary on Legal Holds, 2nd ed."],
sig_lens="""The Signature reading: lifecycle notifications are the registry's heralds - warning of retirements, proclaiming injunctions, confirming unmakings. The Signature heralds speak clearly, in batches not floods, and confirm the critical messages were heard.""",
demo_data={"records":[
 {"id":"R-230","created":"2025-10-01","retention_years":4,"hold":False}],
 "asof":"2026-10-17",
 "expect":{"R-230":"active"}},
),
]
