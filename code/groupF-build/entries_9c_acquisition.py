#!/usr/bin/env python3
"""Dataset Acquisition Licensing entries 25-34 (advanced)."""

APPEND = [
dict(
name="License Audits",
group="Advanced Acquisition", ladder_rank=25, ladder_tier="advanced",
description="""License audits verify the program's honesty from both sides: internal audits check that the organization's uses match its licenses (are we redistributing the non-redistributable? training on the no-training data?), and vendor audits check the organization's compliance from the licensor's side. Internal audit types: use-case audits (each product's data sources vs their permitted uses), redistribution audits (outbound flows vs redistribution rights), attribution audits (credits rendered where required), and renewal audits (no lapsed licenses in production). Findings route by severity: willful-looking violations get legal involvement immediately; accidental overruns get remediation with the vendor. Vendor audits arrive with notice per the contract's audit clause: the program cooperates with evidence - the registry's records are the defense. Audit readiness is continuous: the registry's license records, use registrations, and flow verifications mean an audit is a report, not a fire drill. The audit of audits verifies findings remediate.""",
how_it_works="""Internal audit programs schedule the four audit types with independent auditors. Findings classify by severity with remediation workflows and legal involvement where needed. Vendor audit responses compile evidence from the registry: license records, use registrations, flow verifications. Readiness maintained continuously through the registry's records. Remediation verification closes findings; audit-of-audits tracks closure.""",
key_points=[
 "Internal audits: use-case, redistribution, attribution, renewal compliance.",
 "Vendor audits answered with registry evidence - readiness is continuous.",
 "Willful-looking violations get immediate legal involvement.",
 "Findings remediate with verification; closure tracked.",
 "An audit should be a report, not a fire drill."],
requirements=[
 "Scheduled internal audit programs with independence.",
 "Severity-routed findings with remediation.",
 "Vendor audit response with registry evidence.",
 "Remediation verification with closure tracking."],
standards=[
 "DAMA-DMBOK data governance guidance."],
citations=[
 "DAMA International. DAMA-DMBOK, 2nd ed. Technics Publications, 2017.",
 "Open Data Institute. Guidance on data licensing."],
sig_lens="""The Signature reading: license audits are the registry's inspection of its own charters - uses matched to permissions, vendors answered with evidence. The Signature inspection keeps the house audit-ready always.""",
demo_data={"licenses":[
 {"name":"audit-clean","commercial":True,"redistribute":True,"expires":"2030-01-01","expected":"ok"},
 {"name":"audit-lapsed","commercial":True,"redistribute":True,"expires":"2020-01-01","expected":"expired"}]},
),
dict(
name="Acquisition for a Million-Database Network",
group="Advanced Acquisition", ladder_rank=26, ladder_tier="advanced",
description="""A million databases acquiring data need acquisition at network scale: shared source evaluations (one database's vendor assessment benefits all), collective licensing (network-wide agreements with better terms than any database alone), and a shared source catalog (every database sees what sources exist, under what licenses, with what quality). The network's acquisition spine maintains: the source catalog with license records, collective agreements negotiated centrally, and compliance verification across databases. Databases acquire locally but register globally: each acquisition enters the shared catalog, preventing duplicate vendor contracts and surfacing license conflicts early. License compliance federates: each database verifies its uses against the shared license records; the spine audits by sampling. The economics compound: collective bargaining cuts costs, shared evaluations cut diligence, and the catalog prevents the same source being bought ten times over.""",
how_it_works="""The spine's source catalog aggregates acquisitions network-wide with license records. Collective agreements negotiated centrally with volume terms; databases opt in. Local acquisitions register globally on completion. Compliance verifies locally against shared records; the spine audits by sampling. Duplicate detection prevents redundant contracts. Bargaining leverage tracked: collective vs individual pricing.""",
key_points=[
 "Shared evaluations, collective licensing, shared catalog - network-scale acquisition.",
 "Acquire locally, register globally: no duplicate contracts, early conflict detection.",
 "Collective bargaining cuts costs; shared diligence cuts effort.",
 "Compliance federates: local verification, spine sampling audits.",
 "Economics compound across the network."],
requirements=[
 "Network source catalog with license records.",
 "Collective agreement negotiation with opt-in.",
 "Global registration of local acquisitions.",
 "Federated compliance with sampling audits."],
standards=[
 "DAMA-DMBOK data governance guidance."],
citations=[
 "DAMA International. DAMA-DMBOK, 2nd ed. Technics Publications, 2017.",
 "Open Data Institute. Guidance on data procurement."],
sig_lens="""The Signature reading: network acquisition is a million houses buying as one guild - shared scouting, bargained charters, one catalog of provisions. The Signature guild buys wisely once instead of dearly a thousand times.""",
demo_data={"licenses":[
 {"name":"guild-source","commercial":True,"redistribute":True,"expires":"2030-01-01","expected":"ok"},
 {"name":"guild-nc","commercial":False,"redistribute":True,"expires":"2030-01-01","expected":"no-commercial"}]},
),
dict(
name="Provenance of Licenses",
group="Advanced Acquisition", ladder_rank=27, ladder_tier="advanced",
description="""Every license record should answer: where did this license come from, who agreed it, when, under what authority, and what has changed since? License provenance records the source of the terms (the signed agreement, the published license text, the portal's terms page captured on that date), the negotiating parties and signatories, the effective dates, amendments with their own provenance, and the evidence for interpreted terms (legal opinions on ambiguous clauses). Provenance serves disputes (the vendor claims the terms differ - here is the signed copy), audits (prove this use was licensed on that date), and re-licensing (the portal changed its terms - here is what changed). Web-captured terms get archived snapshots - the terms page as it read on the capture date - because live pages change and memories differ. Provenance is immutable and retained with the license; amendments append new provenance.""",
how_it_works="""License records capture provenance: term sources, signatories, dates, amendments, legal opinions. Web terms archived as snapshots on capture dates. Disputes consult the provenance record; audits verify against it. Re-licensing diffs new terms against archived snapshots. Provenance retained immutably with licenses; amendments append.""",
key_points=[
 "Provenance: term sources, signatories, dates, amendments, legal opinions.",
 "Web terms archived as snapshots - live pages change.",
 "Serves disputes, audits, re-licensing.",
 "Amendments append new provenance; history preserved.",
 "Provenance retained immutably with licenses."],
requirements=[
 "Provenance capture on all license records.",
 "Web snapshot archiving for terms pages.",
 "Dispute and audit workflows from provenance.",
 "Immutable provenance with amendment appending."],
standards=[
 "W3C PROV-O."],
citations=[
 "W3C. PROV-O: The PROV Ontology. W3C Recommendation, 2013.",
 "DAMA International. DAMA-DMBOK, 2nd ed. Technics Publications, 2017."],
sig_lens="""The Signature reading: license provenance is each charter's pedigree - signed copies kept, web pages snapshotted, amendments chained. The Signature archive settles disputes with documents, not memories.""",
demo_data={"licenses":[
 {"name":"prov-license","commercial":True,"redistribute":True,"expires":"2030-01-01","expected":"ok"},
 {"name":"prov-old","commercial":True,"redistribute":True,"expires":"2019-01-01","expected":"expired"}]},
),
dict(
name="License Change Tracking",
group="Advanced Acquisition", ladder_rank=28, ladder_tier="advanced",
description="""Licenses change: vendors amend terms, portals update licenses, open projects re-license, and each change can invalidate existing uses. Change tracking monitors license sources for amendments: vendor notices, portal terms pages, project announcements. Each detected change triages: does it affect our rights (the redistribution clause narrowed?), our obligations (new attribution form?), our costs (price changes?)? Affected uses enter impact analysis with legal review; the license record versions with the new terms and effective date; communications go to affected product owners with action items (migrate, renegotiate, or accept). The dangerous changes are the silent narrowings - the terms update that removes a permitted use without fanfare - caught by diffing, not by reading announcements. Change tracking's lead time is its value: weeks of warning beat days of scrambling.""",
how_it_works="""Monitoring watches license sources with diffing on terms pages and notice tracking. Triage assesses rights, obligations, and cost impacts per change. Impact workflows engage legal with affected-use inventories. License records version with new terms; owners get action communications. Silent narrowings caught by automated diffing. Lead-time metrics track detection speed.""",
key_points=[
 "Licenses change: amendments, portal updates, re-licensing - each can invalidate uses.",
 "Triage per change: rights, obligations, costs affected?",
 "Silent narrowings caught by diffing, not announcements.",
 "License records version; owners get action items.",
 "Lead time is the value: weeks of warning beat days of scrambling."],
requirements=[
 "License source monitoring with terms diffing.",
 "Change triage with legal impact analysis.",
 "Versioned license records with owner communications.",
 "Lead-time metrics."],
standards=[
 "DAMA-DMBOK data governance guidance."],
citations=[
 "DAMA International. DAMA-DMBOK, 2nd ed. Technics Publications, 2017.",
 "Open Data Institute. Guidance on data licensing."],
sig_lens="""The Signature reading: change tracking is the registry's watch on the charter-makers - every amendment noticed, every narrowing caught by diffing. The Signature watch buys weeks of warning with diligent eyes.""",
demo_data={"licenses":[
 {"name":"change-tracked","commercial":True,"redistribute":True,"expires":"2030-01-01","expected":"ok"},
 {"name":"change-narrowed","commercial":False,"redistribute":True,"expires":"2030-01-01","expected":"no-commercial"}]},
),
dict(
name="Termination Clauses",
group="Advanced Acquisition", ladder_rank=29, ladder_tier="advanced",
description="""Termination clauses define how data relationships end: what triggers termination (breach, convenience with notice, insolvency), what notice is required, what happens to the data (return? delete? keep historical?), what survives (confidentiality, accrued payments, audit rights), and the transition assistance owed. The clauses that matter most are negotiated upfront when leverage is highest: post-termination data rights (may we keep using already-ingested data? for how long?), deletion verification (the vendor certifies destruction of our data), and transition periods (the feed continues during migration). Termination execution follows the clause mechanically: notice given, data disposition verified, surviving obligations tracked. The registry's termination workflows ensure no relationship ends messily: every ended source gets its disposition confirmed, its surviving obligations calendared, and its lessons recorded for the next negotiation.""",
how_it_works="""Termination terms extracted per license with triggers, notice, disposition, survival, transition. Workflows execute mechanically: notice, disposition verification, obligation calendaring. Post-termination rights honored per the clause (use windows for ingested data). Lessons recorded per termination feeding negotiation playbooks. Surviving obligations tracked to completion.""",
key_points=[
 "Clauses cover triggers, notice, data disposition, survival, transition.",
 "Negotiate post-termination data rights upfront at highest leverage.",
 "Execution mechanical: notice, verified disposition, calendared obligations.",
 "Lessons per termination feed future negotiations.",
 "No relationship ends messily - every ending verified."],
requirements=[
 "Termination term extraction per license.",
 "Mechanical termination workflows.",
 "Post-termination rights tracking.",
 "Lessons-learned recording."],
standards=[
 "DAMA-DMBOK data governance guidance."],
citations=[
 "DAMA International. DAMA-DMBOK, 2nd ed. Technics Publications, 2017.",
 "Open Data Institute. Guidance on data procurement."],
sig_lens="""The Signature reading: termination clauses are the charters' rules of parting - notice given, goods returned or released, surviving duties calendared. The Signature parting is clean, verified, and instructive.""",
demo_data={"licenses":[
 {"name":"term-clean","commercial":True,"redistribute":True,"expires":"2030-01-01","expected":"ok"},
 {"name":"term-ended","commercial":True,"redistribute":True,"expires":"2020-06-01","expected":"expired"}]},
),
dict(
name="Acquisition Indemnification",
group="Advanced Acquisition", ladder_rank=30, ladder_tier="advanced",
description="""Indemnification allocates the risk of third-party claims: if the licensed data infringes someone's rights, who defends and pays? The standard pattern: the licensor indemnifies against IP claims arising from the data as delivered (it was theirs to license), the licensee indemnifies for claims arising from its uses (what it built), each with caps and procedures (prompt notice, control of defense, settlement consent). The negotiation points: scope (IP only? or broader?), caps (unlimited? capped at fees paid? multiples?), and carve-outs (indemnification surviving liability caps). Open licenses typically disclaim everything - use at your own risk, no indemnification - which is the price of free. The registry records indemnification terms per license; risk assessment weighs the uncapped exposures. Indemnification claims follow the procedure mechanically: notice, tender of defense, cooperation - because botched procedure can void the protection.""",
how_it_works="""Indemnification terms extracted per license: scope, caps, procedures, carve-outs. Risk assessments weigh exposures, especially uncapped. Claims follow procedures mechanically with legal engagement. Open-license disclaimers noted as accepted risk. Term records version with licenses.""",
key_points=[
 "Indemnification: who defends and pays third-party claims - licensor for the data, licensee for its uses.",
 "Negotiation: scope, caps, carve-outs, procedures.",
 "Open licenses disclaim everything - the price of free.",
 "Procedures matter: botched notice can void protection.",
 "Terms recorded per license; exposures risk-assessed."],
requirements=[
 "Indemnification term extraction per license.",
 "Risk assessment of exposures.",
 "Claims procedures with legal engagement.",
 "Open-license disclaimer acknowledgment."],
standards=[
 "DAMA-DMBOK data governance guidance."],
citations=[
 "DAMA International. DAMA-DMBOK, 2nd ed. Technics Publications, 2017.",
 "Creative Commons. License suite documentation."],
sig_lens="""The Signature reading: indemnification is the charters' bond of defense - who stands surety for the goods' title, and to what limit. The Signature surety's terms are recorded and its procedures followed exactly.""",
demo_data={"licenses":[
 {"name":"indem-standard","commercial":True,"redistribute":True,"expires":"2030-01-01","expected":"ok"},
 {"name":"indem-open","commercial":True,"redistribute":True,"expires":"2030-01-01","expected":"ok"}]},
),
dict(
name="Data Quality Warranties",
group="Advanced Acquisition", ladder_rank=31, ladder_tier="advanced",
description="""Quality warranties are the licensor's promises about the data: accuracy levels, completeness, freshness, fitness for purpose - or the explicit disclaimer that none are warranted. Commercial vendors often warrant to service levels (99.5 percent deliverability, daily freshness) with remedies (credits, termination rights); open licenses warrant nothing. The acquisition program treats warranties as contractual terms to verify, not marketing to believe: acceptance testing measures the warranted qualities on delivery, ongoing monitoring tracks them, and warranty claims follow the contract's procedure with evidence. The warranty's exclusions matter as much as its promises: as-is clauses, fitness disclaimers, and the fine print limiting remedies. When warranties are absent (open data), the program substitutes its own verification: profile everything, trust nothing unwarranted. Warranty records version with the license; warranty performance feeds renewal negotiations.""",
how_it_works="""Warranty terms extracted per license with remedies. Acceptance testing verifies warranted qualities on onboarding. Ongoing monitoring tracks warranty metrics; breaches trigger claims with evidence. Open-data gaps covered by program verification (profile everything). Warranty performance feeds renewal negotiations and vendor scorecards.""",
key_points=[
 "Warranties promise accuracy, completeness, freshness - or disclaim them.",
 "Verified by acceptance testing and ongoing monitoring, not believed.",
 "Exclusions and remedy limits matter as much as promises.",
 "Open data: substitute program verification for absent warranties.",
 "Warranty performance feeds renewals and scorecards."],
requirements=[
 "Warranty term extraction per license.",
 "Acceptance testing on onboarding.",
 "Ongoing warranty monitoring with claims procedures.",
 "Program verification for unwarranted sources."],
standards=[
 "DAMA-DMBOK data governance guidance."],
citations=[
 "DAMA International. DAMA-DMBOK, 2nd ed. Technics Publications, 2017.",
 "Open Data Institute. Guidance on data procurement."],
sig_lens="""The Signature reading: warranties are the provisioners' sworn measures - promised, tested on delivery, watched thereafter. The Signature buyer trusts the unwarranted only after proving it himself.""",
demo_data={"licenses":[
 {"name":"warranty-sla","commercial":True,"redistribute":False,"expires":"2028-01-01","expected":"ok"},
 {"name":"warranty-asis","commercial":True,"redistribute":True,"expires":"2030-01-01","expected":"ok"}]},
),
dict(
name="Acquisition Pipelines",
group="Advanced Acquisition", ladder_rank=32, ladder_tier="advanced",
description="""Acquisition pipelines automate the intake: scheduled fetching, validation against source contracts, quality profiling, license verification (is this source still licensed for this use?), and loading into the estate with provenance. The pipeline stages mirror the acquisition workflow: collect (per the collection method's terms), validate (schema, completeness, license currency), profile (quality signals feeding trust), and publish (with provenance: source, retrieval time, license version). License gates are the distinctive stage: the pipeline checks the source's license currency and use-rights before each run - the lapsed license blocks ingestion automatically, preventing unlicensed accumulation. Pipeline health is monitored like any data pipeline with acquisition-specific alerts: source unreachable, license expiring, quality collapse. The pipelines are themselves licensed-aware infrastructure: every run records the license version it operated under.""",
how_it_works="""Acquisition pipelines implement collect-validate-profile-publish with license gates checking currency and rights per run. Provenance records source, retrieval, license version per load. Health monitoring covers source reachability, license expiry, quality. Lapsed licenses block ingestion mechanically. Pipeline definitions version with the source's terms.""",
key_points=[
 "Pipelines automate: collect, validate, profile, publish - with license gates.",
 "License gates check currency and rights before each run; lapses block ingestion.",
 "Provenance per load: source, retrieval time, license version.",
 "Acquisition-specific alerts: unreachable, expiring, quality collapse.",
 "Pipeline definitions version with source terms."],
requirements=[
 "Acquisition pipeline framework with license gates.",
 "Per-run license verification.",
 "Provenance recording per load.",
 "Acquisition health monitoring."],
standards=[
 "DAMA-DMBOK data integration guidance."],
citations=[
 "DAMA International. DAMA-DMBOK, 2nd ed. Technics Publications, 2017.",
 "Open Data Institute. Guidance on data licensing."],
sig_lens="""The Signature reading: acquisition pipelines are the registry's automated provision trains - running on schedule, checked at the license gate, every load manifested. The Signature trains halt at expired charters.""",
demo_data={"licenses":[
 {"name":"pipe-source","commercial":True,"redistribute":True,"expires":"2029-05-01","expected":"ok"},
 {"name":"pipe-lapsed","commercial":True,"redistribute":True,"expires":"2021-05-01","expected":"expired"}]},
),
dict(
name="Source Reliability Scoring",
group="Advanced Acquisition", ladder_rank=33, ladder_tier="advanced",
description="""Source reliability scores quantify trust in each source: delivery reliability (on-time rate), quality stability (defect rates trending), license stability (terms changed how often?), support responsiveness, and business viability. Scores combine into a single reliability rating per source, updated continuously from operational data - not from vendor promises. The scores drive decisions: renewals weigh reliability against cost, pipeline designs add redundancy for unreliable sources, and the portfolio prunes the chronically unreliable. Score components are transparent: the vendor sees the same delivery metrics the score uses, making reviews factual rather than political. Reliability incidents (the source that went dark for a week) record with impact, feeding both the score and the contingency planning. New sources start with provisional scores from their evaluation until operational history accumulates.""",
how_it_works="""Scoring jobs compute delivery, quality, license-stability, support, viability metrics per source into reliability ratings. Dashboards show scores with component drill-downs shared with vendors. Renewal and architecture decisions consume scores. Incidents record with impact feeding scores and contingency plans. Provisional scores for new sources graduate on operational history.""",
key_points=[
 "Reliability scored from operational data: delivery, quality, license stability, support, viability.",
 "Scores drive renewals, redundancy design, and pruning.",
 "Transparent components make vendor reviews factual.",
 "Incidents feed scores and contingency planning.",
 "New sources carry provisional scores until history accumulates."],
requirements=[
 "Reliability scoring from operational metrics.",
 "Transparent scorecards shared with vendors.",
 "Decision integration: renewals, architecture, pruning.",
 "Incident recording with impact."],
standards=[
 "DAMA-DMBOK data governance guidance."],
citations=[
 "DAMA International. DAMA-DMBOK, 2nd ed. Technics Publications, 2017.",
 "Open Data Institute. Guidance on data procurement."],
sig_lens="""The Signature reading: reliability scores are the registry's ledgers on its provisioners - delivery counted, quality weighed, promises kept or broken. The Signature ledger is open to the provisioners and decides renewals.""",
demo_data={"licenses":[
 {"name":"reliable-vendor","commercial":True,"redistribute":False,"expires":"2028-11-01","expected":"ok"},
 {"name":"flaky-source","commercial":True,"redistribute":True,"expires":"2030-01-01","expected":"ok"}]},
),
dict(
name="Dataset Acquisition Licensing Mastery Review",
group="Advanced Acquisition", ladder_rank=34, ladder_tier="advanced",
description="""The mastery review binds the ladder. Foundations: acquisition as disciplined supply chain; source identification by needs, landscape, and gaps; four collection roads with the highway preferred; scraping only with leave; API charters read and obeyed; public granaries verified and mirrored; vendors tasted before buying; partnerships as sworn exchanges; license families from commons to vaults; CC and ODC charters; bespoke proprietary terms; government gifts recorded exactly. Compounded: license anatomy dissected; attribution debts paid and carried; share-alike chains unbroken; redistribution cargos checked; derivative workshops chartered; commercial stalls separated; renewal clocks watched; access road rules obeyed; quotas rationed; ledgers balanced; charter chemistry tested; disputes diplomatically resolved. Advanced: audits inspecting; the guild buying as one; charter pedigrees kept; charter-makers watched; partings clean; sureties recorded; provisioners' measures tested; provision trains manifested; provisioners ledgered. The creed: no unlicensed data, no lapsed renewal, every use permitted, every source recorded.""",
how_it_works="""The review serves as capstone assessment and deployment checklist: can the team find sources, clear licenses, manage renewals, and prove compliance? New acquisition programs verify each rung: registry complete, licenses recorded, renewals watched, pipelines gated. Gaps become the quarter's program of work. The review repeats as sources and laws evolve.""",
key_points=[
 "Foundations: supply chain, identification, collection, scraping rules, APIs, portals, vendors, partnerships, license families.",
 "Compounded: anatomy, attribution, share-alike, redistribution, derivatives, commercial, renewals, access, quotas, cost, compatibility, conflicts.",
 "Advanced: audits, network scale, provenance, change tracking, termination, indemnification, warranties, pipelines, reliability.",
 "The creed: no unlicensed data, no lapsed renewal, every use permitted, every source recorded.",
 "Mastery reassessed as sources and laws evolve."],
requirements=[
 "Demonstrated competence at every rung before program launch.",
 "Checklist rerun on source and legal changes.",
 "Gaps converted to funded program work."],
standards=[
 "DAMA-DMBOK data governance guidance."],
citations=[
 "DAMA International. DAMA-DMBOK, 2nd ed. Technics Publications, 2017.",
 "Open Data Institute. Guidance on data licensing."],
sig_lens="""The Signature reading: the mastery review is graduation as keeper of provisions. The Signature graduate vets every source, charters every use, watches every clock, and swears the creed: no unlicensed data, no lapsed renewal, every use permitted, every source recorded.""",
demo_data={"licenses":[
 {"name":"mastery-src","commercial":True,"redistribute":True,"expires":"2030-01-01","expected":"ok"},
 {"name":"mastery-old","commercial":True,"redistribute":True,"expires":"2019-01-01","expected":"expired"}]},
),
]
