#!/usr/bin/env python3
"""Data Lifecycle Retention entries 25-34 (advanced)."""

APPEND = [
dict(
name="Retention Across Jurisdictions",
group="Advanced Lifecycle Topics", ladder_rank=25, ladder_tier="advanced",
description="""Records living in multiple jurisdictions obey multiple retention laws, and the registry must satisfy them all at once. The governing principle is strictest-wins per direction: the longest retention floor among applicable regimes sets the minimum keep, the shortest ceiling sets the maximum keep - and when floor exceeds ceiling (keep 10 years here, delete after 5 there), the conflict escalates to counsel for a documented resolution, never to silent non-compliance. Jurisdiction tagging on records (where collected, where stored, whose citizen) determines which regimes apply. Data residency interacts: a record that must stay in-country may need jurisdiction-specific retention clocks. The registry computes per-record effective retention from the jurisdiction set automatically, cites the regimes applied, and flags conflicts for legal review. Regulatory change monitoring watches all applicable regimes; a law change in any one recomputes the affected records' clocks.""",
how_it_works="""Records carry jurisdiction tags; the policy engine maps tags to applicable regimes and computes effective retention as max floors and min ceilings with cited provisions. Conflicts (floor above ceiling) queue for counsel resolution with documented outcomes that become precedent. Residency rules layer with retention: in-country records get in-country clocks. Law-change monitoring triggers recomputation for affected records with notifications. Compliance reports show per-jurisdiction adherence; auditors see the regime citations per record.""",
key_points=[
 "Strictest-wins: longest floor as minimum, shortest ceiling as maximum.",
 "Floor-above-ceiling conflicts escalate to counsel with documented precedent.",
 "Jurisdiction tags determine applicable regimes per record.",
 "Residency layers with retention for in-country records.",
 "Law-change monitoring recomputes affected clocks automatically."],
requirements=[
 "Jurisdiction tagging on records.",
 "Multi-regime retention computation with citations.",
 "Conflict escalation with precedent documentation.",
 "Regulatory monitoring with recomputation."],
standards=[
 "ISO 15489; ISO/IEC 27701."],
citations=[
 "Regulation (EU) 2016/679 (GDPR).",
 "ISO 15489-1. Information and documentation - Records management. ISO, 2016."],
sig_lens="""The Signature reading: multi-jurisdiction retention is the registry obeying every land's law for the records that touch it - strictest in each direction, conflicts judged by counsel and recorded as precedent. The Signature registry breaks no law silently.""",
demo_data={"records":[
 {"id":"R-240","created":"2020-05-05","retention_years":10,"hold":False}],
 "asof":"2026-10-17",
 "expect":{"R-240":"active"}},
),
dict(
name="Lifecycle for a Million-Database Network",
group="Advanced Lifecycle Topics", ladder_rank=26, ladder_tier="advanced",
description="""A million databases need lifecycle governance that scales by subsidiarity: global lifecycle policies for the universal rules (holds always win, erasure propagates, certificates required), database-local policies for the specifics (this archive's retention schedules, that community's review boards). Each database runs its own lifecycle engine against its records; the network's lifecycle spine aggregates compliance - disposition rates, hold effectiveness, erasure SLA adherence - and coordinates cross-database obligations: erasure in one database propagates to derived data in others via lineage, holds on shared records freeze them everywhere. Standard lifecycle profiles per data kind keep the network consistent: every customer record honors erasure the same way. The spine never becomes a bottleneck because it coordinates and audits rather than executing - the million engines do the work, the spine verifies.""",
how_it_works="""Global policies define universal rules; local policies extend them per database. Each database's engine executes locally and publishes compliance summaries to the spine. Cross-database propagation uses lineage: erasure and hold events flow to derived records in other databases with acknowledgment. Standard profiles per data kind ensure consistent handling. The spine audits via sampling and coordinates cross-database incidents. Non-compliant databases get remediation plans; persistent non-compliance escalates to network governance.""",
key_points=[
 "Subsidiarity: global universal rules, local specific policies.",
 "Each database runs its engine; the spine aggregates and coordinates.",
 "Cross-database erasure and hold propagation via lineage with acknowledgment.",
 "Standard profiles per data kind keep handling consistent.",
 "The spine audits by sampling; it coordinates, not executes."],
requirements=[
 "Global lifecycle policies with local extensions.",
 "Per-database engines with compliance summary publication.",
 "Cross-database propagation with acknowledgment.",
 "Standard profiles per data kind."],
standards=[
 "ISO 15489."],
citations=[
 "ISO 15489-1. Information and documentation - Records management. ISO, 2016.",
 "DAMA International. DAMA-DMBOK, 2nd ed. Technics Publications, 2017."],
sig_lens="""The Signature reading: network lifecycle is a million estates under one law of seasons - each keeping its own calendar, all honoring the universal injunctions. The Signature law binds the network without burdening it.""",
demo_data={"records":[
 {"id":"R-250","created":"2019-12-12","retention_years":6,"hold":False}],
 "asof":"2026-10-17",
 "expect":{"R-250":"expired"}},
),
dict(
name="Lifecycle Metrics",
group="Advanced Lifecycle Topics", ladder_rank=27, ladder_tier="advanced",
description="""Lifecycle metrics prove the system works: disposition compliance (what share of expired records were actually disposed on time?), hold effectiveness (any held records accidentally deleted? must be zero), erasure SLA adherence (requests completed within legal deadlines), archival integrity (fixity check pass rates), storage efficiency (spend per tier trending), and review timeliness (disposition reviews completed before expiry). Metrics report in tiers: engine health for operators, compliance posture for legal, cost and risk for executives. Targets are contractual where regulations demand (erasure deadlines) and committed where they do not (disposition within 30 days of expiry). Trends matter more than snapshots: disposition compliance sliding from 99 to 94 percent is the early warning. Every metric has an owner and a response playbook; the metrics review is part of the governance cadence.""",
how_it_works="""Metric jobs aggregate lifecycle events into compliance, effectiveness, SLA, integrity, efficiency, and timeliness measures per database and network-wide. Dashboards tier the views; breaches alert owners with playbooks. Targets derive from regulations and commitments; trends trigger reviews before breaches. Benchmarking compares databases; laggards get improvement plans. Metric definitions version with the policies they measure.""",
key_points=[
 "Metrics: disposition compliance, hold effectiveness, erasure SLAs, archival integrity, storage efficiency.",
 "Tiered reporting: operators, legal, executives.",
 "Trends over snapshots: sliding compliance is the early warning.",
 "Every metric owned with a response playbook.",
 "Benchmarking across databases drives improvement."],
requirements=[
 "Metric definitions across lifecycle dimensions.",
 "Tiered dashboards with breach playbooks.",
 "Trend analysis with pre-breach reviews.",
 "Cross-database benchmarking."],
standards=[
 "ISO 15489; ISO 8000-8."],
citations=[
 "ISO 15489-1. Information and documentation - Records management. ISO, 2016.",
 "DAMA International. DAMA-DMBOK, 2nd ed. Technics Publications, 2017."],
sig_lens="""The Signature reading: lifecycle metrics are the registry's account of its stewardship - dispositions done, holds honored, erasures timely, archives sound. The Signature steward renders accounts honestly and answers for every shortfall.""",
demo_data={"records":[
 {"id":"R-260","created":"2024-03-03","retention_years":6,"hold":False}],
 "asof":"2026-10-17",
 "expect":{"R-260":"active"}},
),
dict(
name="Lifecycle and Lineage",
group="Advanced Lifecycle Topics", ladder_rank=28, ladder_tier="advanced",
description="""Lifecycle transitions propagate through lineage: when a source record expires, its derived copies must be evaluated; when a hold lands, downstream derivatives freeze; when erasure executes, personal data leaves every downstream table. The registry joins the two systems: lifecycle engines query lineage for downstream impact before acting, and lineage captures lifecycle events as nodes in the graph (this aggregate was recomputed after its source's erasure). The combination answers the hard compliance questions: prove this erasure reached every copy (lineage shows all downstream, lifecycle shows each deleted), prove this hold froze everything relevant (lineage found the derivatives, lifecycle froze them). Without the join, lifecycle is blind to copies and lineage is blind to obligations - together they are complete. The integration is bidirectional: lifecycle events enrich lineage (why was this recomputed?), and lineage scopes lifecycle actions (what must this erasure touch?).""",
how_it_works="""Lifecycle engines call lineage services for downstream enumeration before expiries, holds, and erasures; actions execute across the enumerated set with per-node verification. Lifecycle events publish to the lineage graph as annotations. Compliance queries join both: erasure completeness verified against lineage downstream, hold coverage verified the same way. Gaps - lifecycle actions without lineage coverage - are flagged as blind spots for lineage instrumentation. The join is tested in drills: simulated erasures verify complete propagation.""",
key_points=[
 "Lifecycle transitions propagate downstream via lineage: expiry, holds, erasure.",
 "Lineage captures lifecycle events as graph annotations.",
 "The join proves erasure completeness and hold coverage.",
 "Lifecycle without lineage is blind to copies; lineage without lifecycle is blind to obligations.",
 "Drills verify propagation; gaps become lineage instrumentation work."],
requirements=[
 "Lifecycle-lineage integration with downstream enumeration.",
 "Propagation verification per action.",
 "Compliance queries joining both systems.",
 "Propagation drills with gap remediation."],
standards=[
 "ISO 15489; OpenLineage."],
citations=[
 "ISO 15489-1. Information and documentation - Records management. ISO, 2016.",
 "OpenLineage. OpenLineage Specification. Linux Foundation."],
sig_lens="""The Signature reading: lifecycle and lineage are the registry's two hands - one executing the seasons, the other mapping the family. Together they leave no descendant unaccounted when fate arrives.""",
demo_data={"records":[
 {"id":"R-270","created":"2021-01-15","retention_years":5,"hold":False}],
 "asof":"2026-10-17",
 "expect":{"R-270":"expired"}},
),
dict(
name="Automated Classification for Retention",
group="Advanced Lifecycle Topics", ladder_rank=29, ladder_tier="advanced",
description="""Records arrive unclassified, and manual classification does not scale: automated classification assigns record classes at creation using content analysis, metadata patterns, and source context. Classifiers combine rules (emails from the finance system about invoices are financial records) with ML models trained on labeled examples, each prediction carrying confidence. High-confidence predictions apply automatically with audit; low-confidence ones queue for human review - and the reviews train the models. The classification determines the retention schedule, so errors have legal consequences: misclassifying a 7-year financial record as a 1-year log risks unlawful destruction. The safeguards match the stakes: confidence thresholds per class, human review for high-stakes classes regardless of confidence, and periodic accuracy audits with labeled samples. Classification models version with their training data, and reclassification sweeps apply improved models to historical records where the law permits.""",
how_it_works="""Classification pipelines apply rules then ML models at creation, emitting class plus confidence. Auto-apply above per-class thresholds; human review below and for high-stakes classes always. Reviews label examples feeding model retraining. Accuracy audits on labeled samples measure per-class precision/recall; underperforming classes get rule or model fixes. Model versions track with training data; reclassification sweeps update historical records with the changes logged. Misclassification incidents trigger root-cause analysis like any data incident.""",
key_points=[
 "Automated classification assigns retention classes at creation with confidence.",
 "Rules plus ML; high-confidence auto-applies, low-confidence goes to review.",
 "Misclassification has legal consequences - safeguards match the stakes.",
 "High-stakes classes always get human review regardless of confidence.",
 "Accuracy audits and reclassification sweeps keep classification honest."],
requirements=[
 "Classification pipelines with rules and ML models.",
 "Per-class confidence thresholds with human review queues.",
 "Accuracy audits on labeled samples.",
 "Model versioning with reclassification sweeps."],
standards=[
 "ISO 15489."],
citations=[
 "ISO 15489-1. Information and documentation - Records management. ISO, 2016.",
 "DAMA International. DAMA-DMBOK, 2nd ed. Technics Publications, 2017."],
sig_lens="""The Signature reading: automated classification is the registry's swift sorter - reading each newborn record and naming its class, humble about uncertainty, always deferring the weighty judgments to humans. The Signature sorter is audited like any judge.""",
demo_data={"records":[
 {"id":"R-280","created":"2026-08-08","retention_years":7,"hold":False}],
 "asof":"2026-10-17",
 "expect":{"R-280":"active"}},
),
dict(
name="Disposition Reviews",
group="Advanced Lifecycle Topics", ladder_rank=30, ladder_tier="advanced",
description="""Disposition review is the human judgment before destruction: a steward examines records queued for deletion and confirms they may go - checking for holds, ongoing matters, historical value, and classification errors. Reviews are tiered: routine records auto-approve when eligibility is clean, sensitive records get individual review, and historically valuable records get archival appraisal (should the museum keep this?). The review board works from disposition packets: the records, their metadata, eligibility evidence, and the recommendation. Decisions - destroy, extend, archive, escalate - are recorded with reasons and authority. Review backlogs are managed like any queue: aging items escalate, and chronic backlog triggers either more reviewers or broader auto-approval criteria (with the risk accepted explicitly). What disposition review forbids is the alternative: automatic deletion of anything with a pulse of doubt.""",
how_it_works="""Disposition queues present packets with records, metadata, eligibility evidence, and recommendations. Tiered review routes routine to auto-approval, sensitive to stewards, historical to appraisers. Decisions record with reasons and authority; destroys execute through deletion workflows. Backlog dashboards track aging with escalation; criteria reviews adjust auto-approval scope with explicit risk acceptance. Appraisal decisions for historical value follow archival policy with institutional sign-off.""",
key_points=[
 "Human judgment before destruction: holds, matters, value, errors checked.",
 "Tiered: routine auto-approves when clean, sensitive reviewed, historical appraised.",
 "Disposition packets carry records, evidence, and recommendations.",
 "Decisions recorded with reasons and authority.",
 "Backlogs managed; auto-approval scope changes accept risk explicitly."],
requirements=[
 "Disposition queues with evidence packets.",
 "Tiered review routing with auto-approval criteria.",
 "Recorded decisions with reasons and authority.",
 "Backlog management with escalation."],
standards=[
 "ISO 15489."],
citations=[
 "ISO 15489-1. Information and documentation - Records management. ISO, 2016.",
 "DAMA International. DAMA-DMBOK, 2nd ed. Technics Publications, 2017."],
sig_lens="""The Signature reading: disposition review is the registry's court of last resort - every condemned record heard, the doubtful spared or archived, the verdict recorded. The Signature court never executes on doubt.""",
demo_data={"records":[
 {"id":"R-290","created":"2016-06-06","retention_years":7,"hold":False}],
 "asof":"2026-10-17",
 "expect":{"R-290":"expired"}},
),
dict(
name="Provenance of Lifecycle Events",
group="Advanced Lifecycle Topics", ladder_rank=31, ladder_tier="advanced",
description="""Every lifecycle transition should answer: who ordered it, under what authority, by which policy version, with what evidence? Lifecycle provenance records the chain: the retention schedule version that set the clock, the hold order with its authority, the steward who approved disposition, the engine version that executed deletion, the certificate that verified it. Provenance makes lifecycle auditable: the regulator asking why this record was deleted gets the full chain from schedule to certificate. It makes lifecycle debuggable: the wrongly deleted record's provenance shows which rule misfired. And it makes lifecycle trustworthy across the network: a database receiving a propagated erasure can verify the authority behind it. Provenance records are immutable and retained beyond the records they describe - the proof outlives the data.""",
how_it_works="""Lifecycle services emit PROV-O provenance with every transition: policy versions, authorities, approvers, evidence, executors. Provenance stores immutably alongside event logs, retained beyond record lifetimes. Audit queries traverse from any record (or its tombstone) through its full lifecycle provenance. Cross-database propagation carries provenance with the action for verification. Provenance completeness is monitored; transitions without provenance are blocked.""",
key_points=[
 "Provenance chains: schedule versions, hold authorities, approvers, executors, certificates.",
 "Makes lifecycle auditable, debuggable, and trustworthy across the network.",
 "Proof outlives data: provenance retained beyond record lifetimes.",
 "Propagated actions carry provenance for verification.",
 "Transitions without provenance are blocked."],
requirements=[
 "PROV-O provenance emission on all transitions.",
 "Immutable provenance retained beyond records.",
 "Audit traversal from records through full provenance.",
 "Completeness monitoring with blocking."],
standards=[
 "W3C PROV-O; ISO 15489."],
citations=[
 "W3C. PROV-O: The PROV Ontology. W3C Recommendation, 2013.",
 "ISO 15489-1. Information and documentation - Records management. ISO, 2016."],
sig_lens="""The Signature reading: lifecycle provenance is every passage's warrant - the law cited, the authority named, the execution certified. The Signature registry's proof outlives its data, so the dead can still testify.""",
demo_data={"records":[
 {"id":"R-300","created":"2025-12-01","retention_years":8,"hold":False}],
 "asof":"2026-10-17",
 "expect":{"R-300":"active"}},
),
dict(
name="Lifecycle in Streaming Systems",
group="Advanced Lifecycle Topics", ladder_rank=32, ladder_tier="advanced",
description="""Streams never end, so lifecycle in streaming is about windows and state, not files: how long are events retained in the stream, how long does processor state live, when do late events stop being accepted? Retention in streaming has two clocks: the log retention (how far back the stream's history reaches - 7 days, 30 days, governed like any retention) and the state retention (how long aggregations remember - windows plus allowed lateness plus grace). Tombstones handle deletion in streams: erasure publishes a tombstone that compacts the key away, with the compaction lag documented as the deletion's effective delay. Holds in streaming freeze compaction for held keys. The physics differ from batch - you cannot delete from an append-only log except by compaction or expiry - so streaming lifecycle policies are written in the stream's own terms: retention.ms, state TTLs, tombstone propagation, compaction monitoring. Consumers of streams inherit the lifecycle: the materialized view's retention derives from its source stream's.""",
how_it_works="""Stream policies configure log retention, state TTLs, and tombstone handling per stream. Erasure publishes tombstones per key with propagation monitoring until compaction completes. Holds suspend compaction for held keys. State stores enforce TTLs with expiry metrics. Materialized views derive retention from source streams automatically. Lifecycle dashboards show stream retention posture: log ages, state sizes, tombstone backlogs, compaction health.""",
key_points=[
 "Streaming lifecycle governs windows and state: log retention, state TTLs, lateness.",
 "Tombstones implement deletion via compaction, with documented delay.",
 "Holds suspend compaction for held keys.",
 "Policies written in stream terms: retention.ms, TTLs, tombstone propagation.",
 "Materialized views inherit retention from source streams."],
requirements=[
 "Per-stream retention and state TTL policies.",
 "Tombstone-based erasure with propagation monitoring.",
 "Hold-aware compaction suspension.",
 "Retention inheritance for materialized views."],
standards=[
 "ISO 15489 (adapted)."],
citations=[
 "Akidau T et al. Streaming Systems. O'Reilly, 2018.",
 "Kleppmann M. Designing Data-Intensive Applications. O'Reilly, 2017."],
sig_lens="""The Signature reading: streaming lifecycle is the registry's law for rivers - how long the waters remember, how the unmaking travels downstream as tombstones. The Signature law respects the river's physics and writes policy in its own current.""",
demo_data={"records":[
 {"id":"R-310","created":"2023-02-02","retention_years":4,"hold":False}],
 "asof":"2026-10-17",
 "expect":{"R-310":"active"}},
),
dict(
name="Edge Cases: Merged and Split Records",
group="Advanced Lifecycle Topics", ladder_rank=33, ladder_tier="advanced",
description="""Merges and splits tangle lifecycles: two records merge - whose retention clock governs the survivor? A record splits - do both children inherit the parent's holds? The registry's rules are principled. Merges: the survivor takes the longest applicable retention among merged records (never shorten by merging), inherits all holds (a hold on either parent freezes the survivor), and the retired ID's lifecycle history joins the survivor's. Splits: both children inherit the parent's holds and the longest applicable retention, with the split reason recorded - splitting must never be an escape from obligations. Erasure interacts carefully: erasing one merged identity requires evaluating all constituent records' exemptions. Disposition review of merged records examines the full constituent history. The rules are enforced mechanically in the merge/split workflows - not left to steward memory - because lifecycle obligations are legal obligations, and legal obligations do not dissolve in reorganization.""",
how_it_works="""Merge workflows compute survivor retention as the max of constituents, union holds, and join histories; the rules execute in the merge transaction. Split workflows copy holds and max retention to both children with the split reason. Erasure on merged entities evaluates exemptions per constituent record. Disposition packets for merged records include full constituent histories. Compliance checks verify the rules held after every merge/split; violations page immediately.""",
key_points=[
 "Merges: survivor takes longest retention, inherits all holds, joins histories.",
 "Splits: both children inherit holds and longest retention - never an escape.",
 "Erasure on merged entities evaluates exemptions per constituent.",
 "Rules enforced mechanically in merge/split workflows.",
 "Lifecycle obligations are legal obligations; reorganization does not dissolve them."],
requirements=[
 "Merge/split lifecycle rules in workflow transactions.",
 "Max-retention and hold-union computation.",
 "Constituent-level exemption evaluation for erasure.",
 "Post-merge/split compliance verification."],
standards=[
 "ISO 15489."],
citations=[
 "ISO 15489-1. Information and documentation - Records management. ISO, 2016.",
 "DAMA International. DAMA-DMBOK, 2nd ed. Technics Publications, 2017."],
sig_lens="""The Signature reading: merged and split lifecycles are the registry's inheritance law - the survivor bearing the longest span and every injunction, the children sharing the parent's obligations. The Signature law permits no escape through reorganization.""",
demo_data={"records":[
 {"id":"R-320","created":"2018-08-08","retention_years":7,"hold":True},
 {"id":"R-321","created":"2018-08-08","retention_years":7,"hold":False}],
 "asof":"2026-10-17",
 "expect":{"R-320":"held","R-321":"expired"}},
),
dict(
name="Data Lifecycle Retention Mastery Review",
group="Advanced Lifecycle Topics", ladder_rank=34, ladder_tier="advanced",
description="""The mastery review binds the ladder. Foundations: every record lives a managed life - creation registered and clocked, active use governed and metered, revision versioned honestly, supersession honorable, expiration computed and warned, retention schedules researched and cited, regulatory floors and ceilings honored, legal holds freezing with mechanical force, placement and release executed with care, archival preserving context for decades, cold and hot storage tiered by need. Compounded: deletion workflows verifying and certifying, crypto-shredding unmaking thoroughly, erasure rights honored completely, tombstones marking merciful pauses, minimization holding only what purpose warrants, policies as executable code, engines enforcing conservatively, events chronicled immutably, metadata traveling with records, backups lifecycle-governed, derived data inheriting fate, notifications heralding every passage. Advanced: multi-jurisdiction strictness, the million-database subsidiarity, metrics proving stewardship, lineage joined to lifecycle, automated classification with humble confidence, disposition courts of last resort, provenance outliving data, streaming rivers under law, and inheritance law for merged and split records. The creed: every record its seasons, every season its law, no destruction without warrant, no hold without release.""",
how_it_works="""The review serves as capstone assessment and deployment checklist: can the team define lifecycles, enforce retention, honor holds and erasures, and prove it all? New lifecycle programs verify each rung: policies coded, engines running, holds mechanical, archives sound. Gaps become the quarter's program of work. The review repeats as regulations and the estate evolve.""",
key_points=[
 "Foundations: lifecycle stages, schedules, regulations, holds, archival, tiering.",
 "Compounded: deletion, crypto-shredding, erasure, minimization, policy-as-code, engines, events.",
 "Advanced: jurisdictions, network scale, metrics, lineage join, classification, disposition, provenance.",
 "The creed: every record its seasons, every season its law, no destruction without warrant.",
 "Mastery is proven stewardship, reassessed as law and estate evolve."],
requirements=[
 "Demonstrated competence at every rung before program launch.",
 "Checklist rerun on regulatory and estate changes.",
 "Gaps converted to funded program work."],
standards=[
 "ISO 15489; ISO 30301."],
citations=[
 "ISO 15489-1. Information and documentation - Records management. ISO, 2016.",
 "DAMA International. DAMA-DMBOK, 2nd ed. Technics Publications, 2017."],
sig_lens="""The Signature reading: the mastery review is graduation as keeper of seasons. The Signature graduate grants every record its lawful span, freezes at law's command, unmakes only with warrant, and swears the creed: every record its seasons, every season its law.""",
demo_data={"records":[
 {"id":"R-330","created":"2026-10-01","retention_years":7,"hold":False}],
 "asof":"2026-10-17",
 "expect":{"R-330":"active"}},
),
]
