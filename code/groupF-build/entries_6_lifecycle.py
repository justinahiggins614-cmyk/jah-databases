#!/usr/bin/env python3
"""Authored records for the Data Lifecycle Retention databases (group F, part 1).
Public = real, fact-checked lifecycle/retention knowledge (retention schedules,
legal holds, deletion, GDPR erasure). Signature = expanded Signature treatment.
Property of Justin Addam Higgins (JAH)."""

SIG_TAIL = ("Signature interpretation - original Signature-system treatment "
            "by Justin Addam Higgins; clearly labeled Signature-made, never "
            "presented as authentic public record.")

ENTRIES = [
dict(
name="What the Record Lifecycle Is",
group="Lifecycle Stages", ladder_rank=1, ladder_tier="foundations",
description="""Every record lives a life: created, used, revised, expired, archived, and finally deleted - or preserved forever when the law or history demands it. The record lifecycle is the managed journey through these stages, with rules governing each transition. Creation captures the record with its metadata and classification. Active use is the working life: reads, updates, sharing under access controls. Revision versions the changes. Expiration ends the active life per the retention schedule. Archival moves the record to long-term storage with its context intact. Deletion destroys it securely when nothing requires keeping it. Legal holds can freeze any record at any stage. Managing the lifecycle matters because unmanaged records either accumulate forever (cost, risk, and legal exposure growing with every terabyte) or vanish when needed (the contract nobody can find during litigation). The lifecycle registry governs the journey for every record class in the network.""",
how_it_works="""Each record class gets a lifecycle definition: stages, transition rules, retention periods, archival specs, deletion methods, and hold procedures. Records carry lifecycle metadata - created date, stage, retention clock, holds - updated by lifecycle events. A lifecycle engine evaluates transitions on schedule: expiring records queue for review or auto-archive, archived records queue for disposition, held records are skipped. Transitions execute with verification: archival confirms readability before deleting the original, deletion confirms destruction. The engine logs every transition with the rule applied, building the lifecycle history auditors require.""",
key_points=[
 "Stages: creation, active use, revision, expiration, archival, deletion - holds freeze any stage.",
 "Unmanaged records accumulate forever (cost and risk) or vanish when needed.",
 "Each record class gets a lifecycle definition with rules per transition.",
 "Lifecycle engines evaluate transitions on schedule with verification.",
 "Every transition logs with the rule applied for audit."],
requirements=[
 "Lifecycle definitions per record class with stage rules.",
 "Lifecycle metadata on records: stage, retention clock, holds.",
 "Scheduled transition evaluation with verification.",
 "Transition logging with applied rules."],
standards=[
 "ISO 15489 for records management.",
 "DAMA-DMBOK data governance guidance."],
citations=[
 "ISO 15489-1. Information and documentation - Records management. ISO, 2016.",
 "DAMA International. DAMA-DMBOK, 2nd ed. Technics Publications, 2017."],
sig_lens="""The Signature reading: the lifecycle is every record's appointed journey - born, working, aging, archived, released - with holds that stay execution like royal pardons. The Signature registry shepherds each record through its seasons and verifies every passage.""",
demo_data={"records":[
 {"id":"R-001","created":"2020-01-15","retention_years":6,"hold":False},
 {"id":"R-002","created":"2024-06-01","retention_years":7,"hold":True}],
 "asof":"2026-10-17",
 "expect":{"R-001":"expired","R-002":"held"}},
),
dict(
name="Creation and Ingestion",
group="Lifecycle Stages", ladder_rank=2, ladder_tier="foundations",
description="""Lifecycle starts at creation: the moment a record enters the managed estate, whether born in an application, ingested from a feed, or declared from a file share. Good creation captures what the rest of the lifecycle needs: the content, the creation timestamp, the creator or source, the record class (which lifecycle rules apply), the classification (which protections apply), and the initial retention clock. Ingestion is creation's gate: validation checks the record is complete and well-formed, classification assigns protections, deduplication avoids double-births, and registration mints the record's identity in the registry. Records created without this discipline - the spreadsheet emailed around, the database row with no timestamp - enter the lifecycle already broken: no one knows their age, their class, or their rules. The registry's rule is simple: every record is born registered, classified, and clocked, or it is not born at all.""",
how_it_works="""Creation paths - application writes, feed ingestion, file declaration - all pass through the registration gate: validate completeness and form, classify sensitivity, assign record class, mint identity, start the retention clock. Ingestion pipelines enforce the gate mechanically; application integrations call the registration API. Unregistered records found in the estate (discovered by scans) enter a birth-registration workflow: classified, clocked from best-available dates, with the late registration noted. Creation metadata is immutable - the birth record never changes - while lifecycle metadata evolves. Registration failures quarantine the record, never silently admit it.""",
key_points=[
 "Creation captures content, timestamp, creator, class, classification, retention clock.",
 "Ingestion gates: validation, classification, deduplication, registration.",
 "Unregistered records enter broken: unknown age, class, and rules.",
 "Discovered strays get birth-registration with late notation.",
 "Birth metadata is immutable; lifecycle metadata evolves."],
requirements=[
 "Registration gates on all creation paths.",
 "Immutable birth metadata per record.",
 "Birth-registration workflows for discovered strays.",
 "Quarantine on registration failure."],
standards=[
 "ISO 15489 for records management.",
 "ISO/IEC 11179 for metadata."],
citations=[
 "ISO 15489-1. Information and documentation - Records management. ISO, 2016.",
 "DAMA International. DAMA-DMBOK, 2nd ed. Technics Publications, 2017."],
sig_lens="""The Signature reading: creation is every record's birth, registered and witnessed - class named, protections assigned, clock started. The Signature registry admits no foundlings without papers and no birth without a record.""",
demo_data={"records":[
 {"id":"R-010","created":"2026-01-10","retention_years":3,"hold":False},
 {"id":"R-011","created":"2021-03-03","retention_years":3,"hold":False}],
 "asof":"2026-10-17",
 "expect":{"R-010":"active","R-011":"expired"}},
),
dict(
name="Active Use",
group="Lifecycle Stages", ladder_rank=3, ladder_tier="foundations",
description="""Active use is the record's working life: read by applications, updated by users, shared with partners, analyzed by models. Lifecycle governance during active use focuses on three things. Access control: only the cleared read or change the record, enforced at every access path with audit logging. Integrity: updates version the record rather than overwriting, so the working life is itself a history. Value monitoring: usage metrics show which records earn their keep - the hot records accessed daily, the cold ones untouched for years. Cold active records are the quiet scandal of data estates: petabytes nobody reads but everybody pays to keep fast. Lifecycle policies use usage data to trigger early archival: the record untouched for two years moves to cheaper storage while still active, cutting cost without losing access. Active use ends by schedule (retention expiry), by supersession (a newer version replaces it), or by hold (frozen in place).""",
how_it_works="""Access controls enforce clearance on every read and write with audit logging. Updates create new versions, preserving the working history. Usage meters record access patterns per record; analytics classify hot, warm, and cold. Tiering policies move cold-but-active records to cheaper storage transparently. Supersession links new versions to old, ending the old version's active life while keeping it reachable. Expiry evaluation runs on schedule against retention clocks. All active-life events - accesses, updates, tiers, supersessions - feed the lifecycle history.""",
key_points=[
 "Active use governed by access control, versioned integrity, and usage monitoring.",
 "Cold active records moved to cheaper storage cut cost without losing access.",
 "Updates version; the working life is itself a history.",
 "Active life ends by schedule, supersession, or hold.",
 "Usage data drives tiering and early-archival decisions."],
requirements=[
 "Access controls with audit logging on all paths.",
 "Versioned updates preserving working history.",
 "Usage metering with hot/warm/cold classification.",
 "Transparent tiering for cold active records."],
standards=[
 "ISO 15489 for records management.",
 "ISO/IEC 27001 access controls."],
citations=[
 "ISO 15489-1. Information and documentation - Records management. ISO, 2016.",
 "ISO/IEC 27001. Information security management. ISO."],
sig_lens="""The Signature reading: active use is the record's working years - guarded in access, honest in versioning, watched for idleness. The Signature registry lets no worker's papers be read by strangers and moves the idle to cheaper lodgings.""",
demo_data={"records":[
 {"id":"R-020","created":"2026-09-01","retention_years":5,"hold":False}],
 "asof":"2026-10-17",
 "expect":{"R-020":"active"}},
),
dict(
name="Revision and Versioning",
group="Lifecycle Stages", ladder_rank=4, ladder_tier="foundations",
description="""Revision is how records change without lying about their past: every update creates a new version, linked to its predecessor, with the changer, the timestamp, the reason, and the diff. Versioning discipline distinguishes the kinds of change: corrections fix errors (the typo in the address), updates reflect new reality (the customer moved), and amendments change the record's meaning (the contract terms revised) - each with different approval needs. Version chains support the queries that matter: what did this record say on March 3rd (as-of), what changed between versions (diff), who changed it and why (accountability). Retention applies to versions too: the current version lives under the record's schedule, while superseded versions may have shorter retention - unless the law requires full history. The registry never allows silent overwrites: an update without a version is data corruption with a friendly name.""",
how_it_works="""Update APIs create new versions with predecessor links, changer identity, timestamps, reasons, and diffs. Change kinds (correction, update, amendment) route through different approvals. As-of queries select the version effective on a date; diff views show version-to-version changes. Version retention policies handle superseded versions per legal requirements. Consumers subscribe to version streams for the records they depend on. Integrity checks verify version chains - no gaps, no forks except declared branches, hashes chaining for tamper evidence.""",
key_points=[
 "Every update versions: predecessor link, changer, timestamp, reason, diff.",
 "Change kinds (correction, update, amendment) carry different approvals.",
 "As-of and diff queries make history usable.",
 "Superseded versions have their own retention, sometimes shorter.",
 "Silent overwrites are forbidden - updates without versions are corruption."],
requirements=[
 "Versioned update APIs with full change metadata.",
 "Change-kind classification with approval routing.",
 "As-of and diff query support.",
 "Version-chain integrity checks."],
standards=[
 "ISO 15489 for records management."],
citations=[
 "ISO 15489-1. Information and documentation - Records management. ISO, 2016.",
 "DAMA International. DAMA-DMBOK, 2nd ed. Technics Publications, 2017."],
sig_lens="""The Signature reading: revision is the record's honest aging - every change a new page, never an erased one, each signed and dated. The Signature registry forbids the silent overwrite as it forbids forgery.""",
demo_data={"records":[
 {"id":"R-030","created":"2025-05-05","retention_years":2,"hold":False}],
 "asof":"2026-10-17",
 "expect":{"R-030":"active"}},
),
dict(
name="Lifecycle Supersession",
group="Lifecycle Stages", ladder_rank=5, ladder_tier="foundations",
description="""Supersession is orderly replacement: the new price list supersedes the old, the revised policy supersedes the previous, the corrected report supersedes the erroneous one. The superseded record is not deleted - it is retired with honor: marked superseded, linked to its successor, kept readable for history, and excluded from active use. The discipline matters because silent replacement destroys trust: consumers who built on the old version need to know it is no longer current, why it was replaced, and where to go now. Supersession events notify subscribers, update catalogs to point at the successor, and start the superseded version's own retention clock (often shorter, but never zero without legal clearance). Chains of supersession form the record's genealogy - version 5 supersedes 4 supersedes 3 - letting anyone walk the full history of an idea.""",
how_it_works="""Supersession is declared explicitly: the successor record links to its predecessor with the reason and effective date. The predecessor's status flips to superseded; catalogs and search update to surface the successor; subscribers get supersession notices. The superseded record's retention clock restarts under the superseded-version policy. Genealogy queries walk the chain in both directions. Accidental supersession (the wrong record marked) is reversible with an un-supersede event that restores status and notifies - the registry treats it as a first-class correction, not a quiet fix.""",
key_points=[
 "Supersession retires records with honor: marked, linked, readable, excluded from active use.",
 "Subscribers are notified; catalogs point to the successor.",
 "Superseded versions get their own (shorter) retention clocks.",
 "Chains form genealogies walkable in both directions.",
 "Wrong supersessions reverse explicitly with notifications."],
requirements=[
 "Explicit supersession declarations with reasons and dates.",
 "Status management with catalog and subscriber updates.",
 "Superseded-version retention policies.",
 "Reversible supersession with correction events."],
standards=[
 "ISO 15489 for records management."],
citations=[
 "ISO 15489-1. Information and documentation - Records management. ISO, 2016.",
 "DAMA International. DAMA-DMBOK, 2nd ed. Technics Publications, 2017."],
sig_lens="""The Signature reading: supersession is honorable succession - the old record yielding to the new with ceremony, its service recorded, its heir named. The Signature registry never deposes silently and never erases the retired.""",
demo_data={"records":[
 {"id":"R-040","created":"2019-01-01","retention_years":5,"hold":False}],
 "asof":"2026-10-17",
 "expect":{"R-040":"expired"}},
),
dict(
name="Lifecycle Expiration",
group="Lifecycle Stages", ladder_rank=6, ladder_tier="foundations",
description="""Expiration is the end of a record's active life, computed from its retention schedule: created January 2020 plus 7-year retention expires January 2027. Expiration is not deletion - it is the transition point where the record leaves active systems for archival or disposition review. The expiration engine evaluates retention clocks on schedule, handling the subtleties: event-based retention (7 years after the contract ends, not after creation), holds that pause the clock, and extensions granted by stewards with reasons. Expired records queue for their next step: auto-archive for the routine, disposition review for the sensitive, legal review for the litigable. Notifications go out before expiry - the owning team gets 90, 30, and 7-day warnings - because surprise expiration destroys trust in the lifecycle system. Expiration is the lifecycle's most mechanical transition, and its reliability is what lets the organization promise regulators that retention schedules are actually followed.""",
how_it_works="""Retention clocks compute expiry from creation or trigger events per the schedule; holds pause clocks with the pause recorded. The expiration engine evaluates on schedule, queuing records for archive, review, or extended hold. Warning notifications fire at 90/30/7 days to owners. Event-based retention watches for trigger events (contract end, employee departure) to start clocks. Extensions require steward approval with reasons and new dates. Expiry decisions log with the schedule version applied; disputes about expiry consult the log.""",
key_points=[
 "Expiration ends active life per the retention schedule; it is not deletion.",
 "Clocks run from creation or trigger events; holds pause them.",
 "Expired records queue for archive, disposition review, or legal review.",
 "Warnings at 90/30/7 days; surprise expiration destroys trust.",
 "Reliable expiration is what makes retention promises credible to regulators."],
requirements=[
 "Retention clocks with event-based triggers and hold pauses.",
 "Scheduled expiration evaluation with queuing.",
 "Advance warnings to owners.",
 "Expiry logging with schedule versions."],
standards=[
 "ISO 15489 for records management."],
citations=[
 "ISO 15489-1. Information and documentation - Records management. ISO, 2016.",
 "DAMA International. DAMA-DMBOK, 2nd ed. Technics Publications, 2017."],
sig_lens="""The Signature reading: expiration is the record's appointed retirement - computed fairly, warned in advance, executed reliably. The Signature registry retires no record by surprise and keeps every retirement credible.""",
demo_data={"records":[
 {"id":"R-050","created":"2018-06-01","retention_years":7,"hold":False},
 {"id":"R-051","created":"2018-06-01","retention_years":7,"hold":True}],
 "asof":"2026-10-17",
 "expect":{"R-050":"expired","R-051":"held"}},
),
dict(
name="Retention Schedules",
group="Retention and Expiration", ladder_rank=7, ladder_tier="foundations",
description="""Retention schedules are the law of how long each record class lives: financial transactions 7 years, employee records 6 years after departure, marketing consents 3 years, security logs 1 year. Each schedule entry names the record class, the retention period, the trigger (creation, event, or fiscal year), the legal basis (which regulation or business need requires it), the disposition (archive then destroy, or destroy directly), and the owner. Schedules are built from legal research - every period traceable to a statute, regulation, or business requirement - because arbitrary periods fail audits and either keep too much (risk) or too little (non-compliance). Schedules version like everything else: when the law changes, the schedule updates with effective dates, and the update applies prospectively unless the law says otherwise. The schedule is published where record creators can see it, because the best retention enforcement is a creator who classifies correctly at birth.""",
how_it_works="""Legal and business analysis produces the schedule table: class, period, trigger, basis, disposition, owner. The registry versions schedules with effective dates and change logs; updates apply prospectively by default. Record classes link to schedule entries at creation, starting the right clock automatically. Schedule publication includes plain-language guidance for creators. Compliance audits sample records against the schedule - is everything kept as long as required and no longer? Legal updates trigger schedule reviews; the review workflow assesses impact on existing records' clocks.""",
key_points=[
 "Schedules name class, period, trigger, legal basis, disposition, owner.",
 "Every period traceable to statute, regulation, or business need.",
 "Versioned with effective dates; legal changes apply prospectively by default.",
 "Published plainly so creators classify correctly at birth.",
 "Audits sample records against the schedule for compliance."],
requirements=[
 "Legally researched schedule tables with cited bases.",
 "Versioning with effective dates and change logs.",
 "Automatic clock-starting from class linkage.",
 "Compliance sampling audits."],
standards=[
 "ISO 15489 for records management.",
 "ISO 30300 series for management systems for records."],
citations=[
 "ISO 15489-1. Information and documentation - Records management. ISO, 2016.",
 "ISO 30301. Management systems for records. ISO."],
sig_lens="""The Signature reading: retention schedules are the law of lifespans - every record class granted its years by researched statute, the laws versioned and published. The Signature registry keeps no record past its lawful span nor destroys one before.""",
demo_data={"records":[
 {"id":"R-060","created":"2020-03-15","retention_years":7,"hold":False}],
 "asof":"2026-10-17",
 "expect":{"R-060":"active"}},
),
dict(
name="Retention by Regulation: GDPR, SOX, HIPAA",
group="Retention and Expiration", ladder_rank=8, ladder_tier="foundations",
description="""Regulations set retention floors and ceilings that schedules must honor. GDPR's storage limitation principle: keep personal data no longer than necessary for its purpose - a ceiling that forces deletion, not just a floor. Financial regulations (SOX in the US) demand 7-year retention of audit-relevant records - a floor that forbids early deletion. HIPAA requires 6 years for administrative records while medical records follow state laws that vary widely. Tax codes worldwide demand 5-10 years of financial records. The pattern is always: identify which regulations apply to each record class, take the longest floor as the minimum, honor the strictest ceiling as the maximum, and document the reasoning. Multi-jurisdiction records take the union of requirements - the strictest rule among applicable regimes wins. The registry's schedule entries cite the specific provisions, so when the law changes, the affected entries are found by citation, not by memory.""",
how_it_works="""Regulatory analysis maps record classes to applicable regulations with specific provisions and their floors/ceilings. Schedules take the max floor and min ceiling per class with the reasoning documented. Citation-indexed schedule entries enable impact analysis when laws change: find all entries citing GDPR Article 5(1)(e). Multi-jurisdiction logic applies the strictest applicable rule automatically. Regulatory change monitoring feeds schedule reviews; legal signs off on the updated periods. Compliance reporting shows per-regulation adherence with the cited provisions.""",
key_points=[
 "GDPR storage limitation is a ceiling (delete when unnecessary); SOX is a floor (keep 7 years).",
 "Per class: longest floor as minimum, strictest ceiling as maximum, reasoning documented.",
 "Multi-jurisdiction takes the strictest applicable rule.",
 "Schedule entries cite specific provisions for change impact analysis.",
 "Regulatory monitoring feeds schedule reviews with legal sign-off."],
requirements=[
 "Regulation-to-class mapping with cited provisions.",
 "Floor/ceiling computation with documented reasoning.",
 "Citation-indexed schedules for change impact.",
 "Regulatory change monitoring with legal review."],
standards=[
 "ISO 15489; ISO 30301.",
 "GDPR, SOX, HIPAA regulatory texts."],
citations=[
 "Regulation (EU) 2016/679 (GDPR), Article 5(1)(e).",
 "Sarbanes-Oxley Act, Section 802."],
sig_lens="""The Signature reading: regulatory retention is the registry obeying many masters' laws at once - taking each master's strictest command as its own. The Signature registry cites every law it obeys and finds them all again when any law changes.""",
demo_data={"records":[
 {"id":"R-070","created":"2019-11-20","retention_years":6,"hold":False}],
 "asof":"2026-10-17",
 "expect":{"R-070":"expired"}},
),
dict(
name="Legal Holds",
group="Retention and Expiration", ladder_rank=9, ladder_tier="foundations",
description="""A legal hold freezes records in place: when litigation is reasonably anticipated, the organization must preserve everything relevant, suspending normal retention and deletion - destroying held records is spoliation, with severe legal consequences. Holds name the matter, the custodian scope (whose records), the subject scope (what topics), the date range, and the issuing authority. The hold engine finds matching records across the estate - by custodian, keyword, date, and classification - and flags them held, pausing their retention clocks and blocking deletion. Hold notices go to custodians with acknowledgment tracking; custodians must preserve and must not delete, with the duty explained plainly. Holds release when the matter ends, through formal release with the authority recorded - and the clocks resume. The hardest part is scope: too narrow risks spoliation, too broad freezes the business. The registry's search and scoping tools, plus counsel's judgment, draw the line.""",
how_it_works="""Hold orders capture matter, scope (custodians, subjects, dates), and authority. The hold engine searches the estate and flags matches, pausing clocks and blocking deletion mechanically - deletion jobs check hold flags before destroying anything. Custodian notices go out with acknowledgment tracking and plain-language duty explanations. Scope reviews happen on schedule: is the hold still needed this broad? Releases are formal, recorded, and resume clocks. Hold effectiveness audits sample held records for accidental deletion; any deletion of held records triggers immediate incident response. The hold registry itself is retained per the matter's requirements.""",
key_points=[
 "Legal holds freeze relevant records when litigation is anticipated; destroying them is spoliation.",
 "Holds name matter, custodian scope, subject scope, dates, authority.",
 "The engine finds matches estate-wide, pauses clocks, blocks deletion mechanically.",
 "Custodian notices with acknowledgment; scope reviewed on schedule.",
 "Release is formal and recorded; clocks resume."],
requirements=[
 "Hold order workflow with matter, scope, authority.",
 "Estate-wide hold matching with mechanical deletion blocking.",
 "Custodian notification with acknowledgment tracking.",
 "Scheduled scope reviews and formal releases."],
standards=[
 "ISO 15489; ISO 30301.",
 "Sedona Conference guidance on legal holds."],
citations=[
 "The Sedona Conference. Commentary on Legal Holds, 2nd ed.",
 "ISO 15489-1. Information and documentation - Records management. ISO, 2016."],
sig_lens="""The Signature reading: legal holds are the registry's royal injunctions - freezing records mid-journey at law's command, enforced mechanically, released formally. The Signature registry obeys the injunction absolutely, for to destroy the held is the gravest offense.""",
demo_data={"records":[
 {"id":"R-080","created":"2015-01-01","retention_years":7,"hold":True},
 {"id":"R-081","created":"2015-01-01","retention_years":7,"hold":False}],
 "asof":"2026-10-17",
 "expect":{"R-080":"held","R-081":"expired"}},
),
dict(
name="Hold Placement and Release",
group="Retention and Expiration", ladder_rank=10, ladder_tier="foundations",
description="""Placing a hold is a controlled operation: counsel issues the order, the registry scopes it, matching records freeze, custodians are notified, and the placement is logged with the authority. The placement workflow validates scope before executing - a typo in the date range could freeze a million wrong records - and runs in phases for large estates: identify, verify sample, then freeze. Release reverses with equal care: counsel confirms the matter ended, the registry identifies held records whose only hold was this matter (records under multiple holds stay frozen), custodians are notified of release, clocks resume, and the release is logged. Partial release handles matters that narrow: the date range shrinks, and records outside the new scope release while the rest stay held. Every placement and release is an auditable event with the authority named, because holds are the lifecycle's most legally sensitive operation.""",
how_it_works="""Placement workflows validate scope (sample verification before full freeze), execute phased freezing, notify custodians, and log with authority. Multi-hold tracking keeps per-record hold lists; release checks whether other holds remain before unfreezing. Partial releases adjust scope and release the difference. Notifications go to custodians on both placement and release with duty explanations. Placement/release events are immutable and retained per matter requirements. Effectiveness monitoring verifies frozen records are actually immutable - any mutation of held records pages immediately.""",
key_points=[
 "Placement: counsel order, scope validation, phased freeze, custodian notice, logged authority.",
 "Release: matter-end confirmation, multi-hold check, custodian notice, clock resume.",
 "Partial release narrows scope and frees the difference.",
 "Multi-hold records stay frozen until all holds release.",
 "Every placement and release is an immutable auditable event."],
requirements=[
 "Placement workflows with scope validation and phased execution.",
 "Multi-hold tracking per record.",
 "Partial release with scope adjustment.",
 "Immutability verification on held records."],
standards=[
 "ISO 15489.",
 "Sedona Conference guidance."],
citations=[
 "The Sedona Conference. Commentary on Legal Holds, 2nd ed.",
 "ISO 15489-1. Information and documentation - Records management. ISO, 2016."],
sig_lens="""The Signature reading: placement and release are the injunction's setting and lifting - done carefully, in phases, with every frozen record accounted and every release verified. The Signature registry handles law's commands with law's own care.""",
demo_data={"records":[
 {"id":"R-090","created":"2016-04-04","retention_years":7,"hold":True}],
 "asof":"2026-10-17",
 "expect":{"R-090":"held"}},
),
dict(
name="Lifecycle Archival",
group="Archival and Deletion", ladder_rank=11, ladder_tier="foundations",
description="""Archival moves records from active systems to long-term preservation: cheaper storage, slower access, but complete context - the record plus its metadata, versions, and lifecycle history, packaged so it remains understandable decades later. Good archival preserves more than bits: format documentation (how to read this file in 2045), context (what system created it, what it meant), and integrity proofs (checksums, fixity checks on schedule). The archival package follows standards like OAIS - Submission Information Packages becoming Archival Information Packages with preservation metadata. Archival is not backup: backups restore systems, archives preserve evidence. Retention clocks keep running in the archive - archived records still expire and still honor holds. The archive's catalog makes holdings discoverable; an archive nobody can search is a write-only memory.""",
how_it_works="""Archival jobs package records with metadata, version histories, format documentation, and checksums into preservation packages per OAIS. Fixity checks run on schedule, detecting bit rot with repair from redundant copies. The archive catalog indexes holdings for discovery with access controls. Retention and holds continue to apply; disposition review queues surface archived records reaching end-of-life. Format migration plans handle obsolete formats: when a format nears unreadability, holdings migrate with the migration recorded. Archive audits verify package completeness and fixity on samples.""",
key_points=[
 "Archival preserves records plus context: metadata, versions, format docs, integrity proofs.",
 "Follows OAIS packaging: submission to archival information packages.",
 "Archives preserve evidence; backups restore systems - different purposes.",
 "Retention and holds continue to apply in the archive.",
 "Fixity checks and format migration keep archives readable for decades."],
requirements=[
 "OAIS-style archival packaging with preservation metadata.",
 "Fixity checking with repair from redundant copies.",
 "Searchable archive catalog with access controls.",
 "Format migration planning for obsolete formats."],
standards=[
 "ISO 14721 (OAIS reference model).",
 "ISO 15489 for records management."],
citations=[
 "ISO 14721. Open archival information system (OAIS). ISO, 2012.",
 "ISO 15489-1. Information and documentation - Records management. ISO, 2016."],
sig_lens="""The Signature reading: archival is the registry's hall of memory - records laid to rest with their full stories, guarded against rot, findable forever. The Signature hall keeps its charges readable for generations.""",
demo_data={"records":[
 {"id":"R-100","created":"2017-08-08","retention_years":10,"hold":False}],
 "asof":"2026-10-17",
 "expect":{"R-100":"active"}},
),
dict(
name="Cold vs Hot Storage",
group="Archival and Deletion", ladder_rank=12, ladder_tier="foundations",
description="""Storage tiers match cost to access needs: hot storage is fast and expensive for active records, warm is cheaper for infrequent access, cold is cheapest for archival with retrieval in hours, and deep-freeze is cheapest of all with retrieval in days. Tiering policies move records by age, access pattern, and lifecycle stage: active records stay hot, untouched-for-a-year records go warm, archived records go cold, end-of-life records awaiting disposition review go deep. The economics are stark - cold storage can cost a tenth of hot - so tiering is among the highest-ROI lifecycle operations. The disciplines: tiering must be transparent (applications read through tiers without knowing), reversible (a cold record needed urgently promotes back), and safe (integrity verified before and after moves, with the move logged). Retrieval SLAs per tier are contractual: cold retrieval in 4 hours is a promise, not a hope.""",
how_it_works="""Tiering policies define the rules: age thresholds, access-pattern triggers, lifecycle-stage mappings. The tiering engine moves records on schedule, verifying integrity (checksums) before deleting from the source tier. Access layers abstract tiers - reads route automatically with retrieval-time expectations surfaced. Promotion workflows expedite cold records when needed urgently. Tiering is logged per record with the policy applied. Cost dashboards show spend per tier and savings from tiering; policy reviews adjust thresholds from access analytics.""",
key_points=[
 "Tiers: hot (fast, costly), warm, cold (hours retrieval), deep-freeze (days).",
 "Policies move by age, access pattern, lifecycle stage.",
 "Tiering must be transparent, reversible, and integrity-verified.",
 "Retrieval SLAs per tier are contractual promises.",
 "Cold can cost a tenth of hot - tiering is high-ROI."],
requirements=[
 "Tiering policies with age, access, and stage rules.",
 "Integrity-verified moves with logging.",
 "Transparent access abstraction across tiers.",
 "Cost dashboards with policy reviews."],
standards=[
 "ISO 14721 (OAIS)."],
citations=[
 "ISO 14721. Open archival information system (OAIS). ISO, 2012.",
 "DAMA International. DAMA-DMBOK, 2nd ed. Technics Publications, 2017."],
sig_lens="""The Signature reading: storage tiers are the registry's lodgings - the busy housed well, the resting housed cheaply, all retrievable on sworn schedules. The Signature steward moves lodgers transparently and verifies every move.""",
demo_data={"records":[
 {"id":"R-110","created":"2026-02-02","retention_years":7,"hold":False}],
 "asof":"2026-10-17",
 "expect":{"R-110":"active"}},
),
]
