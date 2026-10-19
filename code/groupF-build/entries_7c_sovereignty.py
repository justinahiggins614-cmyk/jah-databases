#!/usr/bin/env python3
"""Data Sovereignty Jurisdiction entries 25-34 (advanced)."""

APPEND = [
dict(
name="Multi-Jurisdiction Architectures",
group="Advanced Sovereignty", ladder_rank=25, ladder_tier="advanced",
description="""Multi-jurisdiction architectures serve global users under local laws simultaneously: the application runs everywhere, but data placement, processing, and features adapt per jurisdiction. The patterns: regional deployments (separate stacks per region with data staying local), sharded-by-jurisdiction (one logical system, data partitioned by governing law), and policy-driven (one stack, jurisdiction rules enforced in code and routing). The choice balances cost against risk: regional deployments cost most but isolate best; policy-driven costs least but demands flawless enforcement. The architecture handles the hard intersections: a German user traveling in Brazil (which law? - usually the account's home jurisdiction plus local constraints), shared datasets across regions (aggregates computed per region, combined under transfer rules), and feature variance (the feature lawful in one region disabled in another). The registry's architecture records map every data flow to its jurisdictional treatment, and compliance testing verifies the mapping continuously.""",
how_it_works="""Architects select the pattern per system from the cost-risk analysis, documenting the jurisdictional treatment per data flow. Implementation enforces through placement policies, routing rules, and feature flags per jurisdiction. Traveler scenarios resolve by home-jurisdiction-plus-local-constraint rules. Cross-region aggregates compute under transfer mechanisms. Compliance testing probes the architecture: attempt unlawful placements and verify blocking. Architecture reviews reassess on law changes and expansion into new jurisdictions.""",
key_points=[
 "Patterns: regional deployments, sharded-by-jurisdiction, policy-driven enforcement.",
 "Cost-risk tradeoff: isolation costs, enforcement demands flawlessness.",
 "Traveler scenarios resolve by home jurisdiction plus local constraints.",
 "Feature variance: lawful features per region, others disabled.",
 "Compliance testing verifies the jurisdictional mapping continuously."],
requirements=[
 "Pattern selection with documented cost-risk analysis.",
 "Per-flow jurisdictional treatment mapping.",
 "Traveler and cross-region rules.",
 "Continuous compliance testing of the mapping."],
standards=[
 "ISO/IEC 27701."],
citations=[
 "DAMA International. DAMA-DMBOK, 2nd ed. Technics Publications, 2017.",
 "Regulation (EU) 2016/679 (GDPR)."],
sig_lens="""The Signature reading: multi-jurisdiction architecture is the realm's federal design - one crown, many laws, each land's customs honored in its borders. The Signature federation tests its own borders continuously.""",
demo_data={"transfers":[
 {"from":"EU","to":"EU","data_class":"personal","expected":"allowed"},
 {"from":"BR","to":"BR","data_class":"personal","expected":"allowed"}]},
),
dict(
name="Sovereignty for a Million-Database Network",
group="Advanced Sovereignty", ladder_rank=26, ladder_tier="advanced",
description="""A million databases under hundreds of jurisdictions need sovereignty by subsidiarity: each database declares its jurisdictional posture - applicable regimes, residency classes, transfer mechanisms - and the network's sovereignty spine aggregates, verifies, and coordinates. Cross-database flows check both ends' rules: the transfer is lawful only if exporter and importer mechanisms align. The spine maintains the global rule corpus (every jurisdiction's requirements, versioned), the corridor matrix (which transfers are lawful under what mechanisms), and the compliance picture (which databases are current, which lag). Databases that cannot meet a corridor's requirements do not get the data - the spine blocks mechanically, not hopefully. New jurisdictions enter through the rule corpus with gap analyses for affected databases. The design scales because sovereignty decisions are local (each database knows its data) while the rules and verification are shared.""",
how_it_works="""Databases publish jurisdictional postures to the spine: regimes, residency, mechanisms, assessments. The spine's corridor matrix computes lawful transfers per data class; cross-database flows check both ends mechanically. Compliance aggregation shows posture currency per database; laggards get remediation. New jurisdictions enter the corpus with affected-database gap analyses. The spine coordinates multi-database incidents (a revocation affecting many corridors) with synchronized re-mechanism. Verification sampling audits postures against reality.""",
key_points=[
 "Subsidiarity: local posture declarations, shared rules and verification.",
 "Cross-database flows lawful only if both ends' mechanisms align.",
 "Global rule corpus versioned; corridor matrix computed per data class.",
 "Non-compliant databases are blocked mechanically from corridors.",
 "Decisions local, rules shared - the design scales."],
requirements=[
 "Jurisdictional posture publication per database.",
 "Corridor matrix with per-class lawful-transfer computation.",
 "Mechanical blocking of non-compliant flows.",
 "Compliance aggregation with remediation workflows."],
standards=[
 "ISO/IEC 27701."],
citations=[
 "Regulation (EU) 2016/679 (GDPR), Chapter V.",
 "DAMA International. DAMA-DMBOK, 2nd ed. Technics Publications, 2017."],
sig_lens="""The Signature reading: network sovereignty is a million realms under shared border law - each declaring its customs, the spine holding the treaties, the unlawful turned back everywhere alike. The Signature treaties scale because each realm minds its own gates.""",
demo_data={"transfers":[
 {"from":"EU","to":"JP","data_class":"personal","expected":"allowed:adequacy"},
 {"from":"CN","to":"EU","data_class":"personal","expected":"restricted:security-assessment"}]},
),
dict(
name="Conflict of Laws",
group="Advanced Sovereignty", ladder_rank=27, ladder_tier="advanced",
description="""Conflict of laws is when two jurisdictions demand opposite things of the same data: retain for 10 years here, delete after 5 there; produce for investigators here, protect from disclosure there. The registry's conflict doctrine: identify the conflict precisely (which provisions, which data), assess the penalties of each non-compliance, seek counsel's resolution - and counsel's options are real: comply with the stricter where possible, seek licenses or exceptions, restructure to avoid the conflict (separate the data by jurisdiction), or in rare cases accept one non-compliance with eyes open and reserves booked. What the doctrine forbids is silent non-compliance - the conflict must be identified, escalated, decided, and recorded, because undiscovered conflicts become surprise enforcement. Conflict precedents accumulate into guidance: the twentieth retain-vs-delete conflict resolves faster with nineteen precedents. The registry versions conflict resolutions; law changes reopen them.""",
how_it_works="""Conflict detection compares applicable regimes' demands per dataset, flagging opposing requirements. Counsel workflows analyze penalties, options (stricter compliance, exceptions, restructuring, accepted non-compliance), and decide with documented reasoning. Restructuring (jurisdictional data separation) is the preferred resolution where feasible. Precedents record in the conflict library; new conflicts search it first. Resolutions version with the laws; legal developments reopen affected conflicts. Compliance reports disclose accepted non-compliances with their reasoning to leadership.""",
key_points=[
 "Conflicts: opposite demands on the same data from different jurisdictions.",
 "Options: stricter compliance, exceptions, restructuring, eyes-open non-compliance.",
 "Silent non-compliance forbidden: identify, escalate, decide, record.",
 "Precedents accelerate repeat conflicts.",
 "Resolutions version with laws; developments reopen them."],
requirements=[
 "Conflict detection across applicable regimes.",
 "Counsel workflows with penalty analysis and documented decisions.",
 "Precedent library with search.",
 "Versioned resolutions with reopening triggers."],
standards=[
 "ISO/IEC 27701."],
citations=[
 "Regulation (EU) 2016/679 (GDPR).",
 "DAMA International. DAMA-DMBOK, 2nd ed. Technics Publications, 2017."],
sig_lens="""The Signature reading: conflict of laws is the registry's hardest judgment - two sovereigns commanding opposite, the registry choosing openly with counsel's wisdom. The Signature judgment is never silent and always recorded.""",
demo_data={"transfers":[
 {"from":"EU","to":"US","data_class":"personal","expected":"restricted:conflict-review"},
 {"from":"EU","to":"EU","data_class":"personal","expected":"allowed"}]},
),
dict(
name="Sovereignty Metrics",
group="Advanced Sovereignty", ladder_rank=28, ladder_tier="advanced",
description="""Sovereignty metrics prove the program works: transfer register completeness (observed vs registered flows), mechanism currency (assessments current, adequacy monitored), residency compliance (placement verification pass rates), rights SLA adherence (erasure and access within deadlines), breach notification timeliness, and vendor DPA coverage. Metrics report per jurisdiction to local leadership and aggregated to global governance. Targets are set by law where the law sets them (72-hour breach notification) and by commitment elsewhere. Trends reveal decay: register completeness sliding means shadow flows are growing. Every metric has an owner and a playbook; the sovereignty review cadence matches the regulatory tempo - quarterly for stable regimes, continuous for volatile ones. Metrics also feed the network spine's compliance aggregation, letting the million-database network prove its sovereignty posture as a whole.""",
how_it_works="""Metric jobs aggregate from transfer registers, placement verifiers, rights workflows, breach logs, and vendor registers into per-jurisdiction and global dashboards. Targets derive from law and commitment; trends trigger reviews before breaches. Owners respond per playbooks; the sovereignty council reviews quarterly. Network aggregation feeds the spine's compliance picture with drill-down to databases. Metric definitions version with the rules they measure.""",
key_points=[
 "Metrics: register completeness, mechanism currency, residency compliance, rights SLAs, breach timeliness, DPA coverage.",
 "Per-jurisdiction reporting plus global aggregation.",
 "Targets from law and commitment; trends trigger pre-breach reviews.",
 "Review cadence matches regulatory tempo.",
 "Feeds network spine compliance aggregation."],
requirements=[
 "Metric definitions across sovereignty dimensions.",
 "Per-jurisdiction and global dashboards.",
 "Owner assignment with response playbooks.",
 "Network aggregation with drill-down."],
standards=[
 "ISO/IEC 27701."],
citations=[
 "Regulation (EU) 2016/679 (GDPR).",
 "DAMA International. DAMA-DMBOK, 2nd ed. Technics Publications, 2017."],
sig_lens="""The Signature reading: sovereignty metrics are the registry's account to every sovereign - transfers manifested, placements verified, rights honored on time. The Signature steward renders accounts per realm and for the whole.""",
demo_data={"transfers":[
 {"from":"UK","to":"UK","data_class":"personal","expected":"allowed"},
 {"from":"UK","to":"US","data_class":"personal","expected":"restricted:IDTA-required"}]},
),
dict(
name="Sovereignty and Encryption",
group="Advanced Sovereignty", ladder_rank=29, ladder_tier="advanced",
description="""Encryption is sovereignty's technical backstop: properly encrypted data is protected even where it sits, because the holder of the ciphertext without the key holds nothing readable. The sovereignty uses of encryption: customer-held keys (the provider cannot produce plaintext to any government - the strongest access-law mitigation), per-jurisdiction keys (EU data encrypted with EU-held keys, so foreign compulsion of the provider yields nothing), and encryption as a transfer safeguard (Schrems II supplementary measure - the importer demonstrably cannot read what it must not disclose). The disciplines are key custody (who holds keys determines who can be compelled), key jurisdiction (keys resident where the law requires), and cryptographic agility (algorithms and key lengths that survive the decade). Encryption is not magic: it does not fix unlawful collection, it does not excuse missing transfer mechanisms, and compelled key disclosure laws exist. But as a layer in the sovereignty architecture, it is the layer attackers and overreach must defeat first.""",
how_it_works="""Encryption architectures assign key custody per sovereignty requirement: customer-held, jurisdiction-held, or provider-held with contractual limits. Key management systems enforce jurisdictional key residency with dual control and audit. Transfer assessments credit encryption only where the importer verifiably lacks key access. Algorithm and key-length policies version with cryptographic developments. Key disclosure procedures define the response to compulsion with legal challenge paths. Effectiveness audits verify the encryption actually protects (penetration tests, key-access reviews).""",
key_points=[
 "Encryption backstops sovereignty: ciphertext without keys is unreadable anywhere.",
 "Customer-held keys: strongest access-law mitigation.",
 "Per-jurisdiction keys with jurisdictional custody.",
 "Supplementary measure for transfers where importer verifiably lacks access.",
 "Not magic: does not fix unlawful collection or excuse missing mechanisms."],
requirements=[
 "Key custody architectures per sovereignty requirement.",
 "Jurisdictional key residency with dual control.",
 "Transfer assessment crediting rules for encryption.",
 "Compulsion response procedures with challenge paths."],
standards=[
 "NIST SP 800-57 (key management); ISO/IEC 27701."],
citations=[
 "NIST SP 800-57. Recommendation for Key Management. NIST.",
 "European Data Protection Board. Recommendations on supplementary measures."],
sig_lens="""The Signature reading: encryption is sovereignty's sealed vault - the keys held where the law commands, by hands the law trusts. The Signature vault's seals are assessed honestly and never claimed as magic.""",
demo_data={"transfers":[
 {"from":"EU","to":"US","data_class":"personal","expected":"restricted:encryption+keys-EU"},
 {"from":"EU","to":"EU","data_class":"personal","expected":"allowed"}]},
),
dict(
name="Key Management by Jurisdiction",
group="Advanced Sovereignty", ladder_rank=30, ladder_tier="advanced",
description="""Keys must live under the right law: encryption keys for EU personal data held in the EU, for Chinese important data in China, with custody arrangements that match each regime's compulsion rules. Jurisdictional key management separates key estates by regime: EU keys in EU key managers under EU legal process, each estate with its own administrators, audit, and disclosure procedures. The operational rules: keys never leave their jurisdiction except under assessed mechanisms, key administrators are vetted per local requirements, disclosure follows local legal process with challenge rights, and key destruction (for crypto-shredding) is verifiable per estate. Multi-jurisdiction keys - one key protecting data under two regimes - are avoided; per-jurisdiction keys keep the legal analysis clean. Key ceremonies (generation, rotation, destruction) follow jurisdictional procedures with witnesses where required. The key inventory maps every key to its jurisdiction, custodian, and the data it protects - the map auditors ask for first.""",
how_it_works="""Key estates per jurisdiction run in compliant key managers with local administrators and audit. Keys are generated, rotated, and destroyed per jurisdictional procedures with ceremony records. Per-jurisdiction keys avoid multi-regime entanglement. Disclosure workflows follow local process with challenge paths; destructions verify and log. The key inventory maps keys to jurisdictions, custodians, and protected data with versioning. Estate reviews verify custody matches policy; anomalies (a key outside its jurisdiction) page immediately.""",
key_points=[
 "Keys resident under the law governing the data they protect.",
 "Separate key estates per jurisdiction with local administration.",
 "Per-jurisdiction keys avoid multi-regime legal entanglement.",
 "Ceremonies for generation, rotation, destruction with records.",
 "Key inventory maps keys to jurisdictions, custodians, data."],
requirements=[
 "Jurisdictional key estates with compliant managers.",
 "Local administrators with vetting and audit.",
 "Ceremony procedures with records.",
 "Key inventory with anomaly paging."],
standards=[
 "NIST SP 800-57; ISO/IEC 27701."],
citations=[
 "NIST SP 800-57. Recommendation for Key Management. NIST.",
 "ISO/IEC 27701. Privacy information management. ISO."],
sig_lens="""The Signature reading: jurisdictional keys are the vault's keys kept in the vault's own land - each estate sovereign, each ceremony witnessed. The Signature keymaster's inventory is the first exhibit in any audit.""",
demo_data={"transfers":[
 {"from":"CN","to":"CN","data_class":"important","expected":"allowed"},
 {"from":"CN","to":"US","data_class":"important","expected":"restricted:keys-CN-only"}]},
),
dict(
name="Provenance of Jurisdiction Rules",
group="Advanced Sovereignty", ladder_rank=31, ladder_tier="advanced",
description="""Every sovereignty rule should cite its authority: this residency requirement comes from that statute's article, this transfer mechanism from that adequacy decision, this retention floor from that regulation's section. Rule provenance records the legal source with citation, the effective date, the interpreting guidance, the counsel opinion where judgment was involved, and the review history. Provenance serves change management (the cited article amends - find all rules citing it), audit (prove this rule's legal basis), and consistency (two rules citing the same article should agree). When counsel's judgment fills a gap the law leaves, the opinion is recorded as the rule's basis - transparent that this is interpretation, not text. The rule corpus versions with its provenance; a rule without provenance is folklore, and folklore does not survive regulatory inquiry.""",
how_it_works="""The rule corpus stores each rule with legal citations, effective dates, guidance links, and counsel opinions. Citation indexing enables impact analysis on legal changes: amend Article X, find all citing rules. Consistency checks flag rules citing the same provision with different implementations. Counsel opinions version with the rules they support. Corpus reviews verify citations still current; stale citations queue for legal review. Audit exports show rule-to-authority chains.""",
key_points=[
 "Every rule cites its legal authority with article-level precision.",
 "Provenance enables change impact analysis on legal amendments.",
 "Counsel opinions recorded transparently as interpretation.",
 "Consistency checks across rules citing the same provisions.",
 "Rules without provenance are folklore."],
requirements=[
 "Citation-indexed rule corpus with effective dates.",
 "Counsel opinion records linked to rules.",
 "Change impact analysis on legal amendments.",
 "Consistency checking across same-provision rules."],
standards=[
 "ISO/IEC 27701."],
citations=[
 "Regulation (EU) 2016/679 (GDPR).",
 "DAMA International. DAMA-DMBOK, 2nd ed. Technics Publications, 2017."],
sig_lens="""The Signature reading: rule provenance is each law's pedigree - article cited, counsel's judgment recorded, history kept. The Signature registry's every rule can show its warrant on demand.""",
demo_data={"transfers":[
 {"from":"EU","to":"EU","data_class":"personal","expected":"allowed"},
 {"from":"SG","to":"SG","data_class":"personal","expected":"allowed"}]},
),
dict(
name="Regulatory Change Tracking",
group="Advanced Sovereignty", ladder_rank=32, ladder_tier="advanced",
description="""Laws change constantly - new statutes, amended articles, fresh guidance, landmark judgments - and the sovereignty program must track them all. Change tracking monitors official journals, regulator announcements, court dockets, and reputable legal publishers across every covered jurisdiction, in their languages. Each detected change triages: does it affect our rules, our transfers, our products? Affected items enter impact analysis with the legal team; the rule corpus updates with new citations and effective dates; transfer registers re-verify mechanisms; and communications go to affected owners. The tempo varies: the EU issues guidance monthly, APAC amends yearly, courts surprise everyone. The tracking system's value is measured in lead time: how many days between a law's publication and the program's response. Automation assists - alerts, machine translation, change diffing - but legal judgment remains human: the machine finds the change, the lawyer decides what it means.""",
how_it_works="""Monitoring feeds cover official sources per jurisdiction with alerting on publications. Triage classifies changes by affected rules, transfers, and products. Impact workflows engage legal with the change text and affected inventory. The corpus updates with new citations; registers re-verify; owners get communications with action items. Lead-time metrics track publication-to-response; retrospectives improve slow paths. Machine assistance (translation, diffing, alerting) scales the monitoring; lawyers make the judgments.""",
key_points=[
 "Track official journals, regulators, courts, publishers across jurisdictions and languages.",
 "Triage: affected rules, transfers, products - then legal impact analysis.",
 "Corpus updates, register re-verification, owner communications follow.",
 "Lead time (publication to response) is the key metric.",
 "Machines find changes; lawyers decide meanings."],
requirements=[
 "Multi-source, multilingual monitoring feeds.",
 "Triage with affected-inventory mapping.",
 "Impact workflows with legal engagement.",
 "Lead-time metrics with retrospectives."],
standards=[
 "ISO/IEC 27701."],
citations=[
 "Regulation (EU) 2016/679 (GDPR).",
 "DAMA International. DAMA-DMBOK, 2nd ed. Technics Publications, 2017."],
sig_lens="""The Signature reading: change tracking is the registry's watch on the lawgivers - every statute, judgment, and guidance noticed in its own tongue. The Signature watch measures its swiftness and leaves judgment to the learned.""",
demo_data={"transfers":[
 {"from":"BR","to":"BR","data_class":"personal","expected":"allowed"},
 {"from":"EU","to":"US","data_class":"personal","expected":"restricted:SCCs-required"}]},
),
dict(
name="Incident Response Across Borders",
group="Advanced Sovereignty", ladder_rank=33, ladder_tier="advanced",
description="""A breach spanning jurisdictions triggers every regime's duties at once: notify the EU authority within 72 hours, notify California consumers without unreasonable delay, notify China's CAC under its timelines - each with different content, thresholds, and recipients. Cross-border incident response runs on playbooks per jurisdiction, coordinated by a global incident commander who sequences notifications by deadline. The playbooks cover: jurisdictional scope assessment (whose data, where, which regimes), evidence preservation across borders (with transfer mechanisms for the forensic data itself), notification drafting per regime, regulator liaison per authority, and consumer communication per language. Tabletop exercises rehearse the multi-jurisdiction breach yearly - the team that has never practiced the 72-hour clock will miss it. Post-incident, each regime's lessons feed the program, and the response timeline itself becomes evidence of diligence.""",
how_it_works="""Incident playbooks per jurisdiction codify scope assessment, notification content and deadlines, evidence handling, and liaison procedures. The global commander sequences per-deadline execution with a unified timeline. Forensic data transfers use assessed mechanisms. Tabletop exercises rehearse multi-jurisdiction scenarios yearly with measured notification times. Post-incident reviews per regime feed program improvements; the timeline archives as diligence evidence. Playbook versions track regulatory changes.""",
key_points=[
 "Multi-jurisdiction breaches trigger every regime's duties simultaneously.",
 "Playbooks per jurisdiction, sequenced by deadline under global command.",
 "Forensic data itself needs transfer mechanisms across borders.",
 "Yearly tabletops rehearse the 72-hour clock and other deadlines.",
 "Response timelines archive as diligence evidence."],
requirements=[
 "Per-jurisdiction incident playbooks with deadlines.",
 "Global coordination with sequenced execution.",
 "Forensic transfer mechanisms.",
 "Yearly multi-jurisdiction tabletop exercises."],
standards=[
 "ISO/IEC 27701; NIST SP 800-61 (incident handling)."],
citations=[
 "Regulation (EU) 2016/679 (GDPR), Articles 33-34.",
 "NIST SP 800-61 Rev. 2. Computer Security Incident Handling Guide."],
sig_lens="""The Signature reading: cross-border response is the registry's fire brigade for many realms at once - every alarm answered on its own clock, the commander sequencing the brigade. The Signature brigade drills yearly and archives every response.""",
demo_data={"transfers":[
 {"from":"EU","to":"US","data_class":"personal","expected":"restricted:breach-notify-both"},
 {"from":"JP","to":"JP","data_class":"personal","expected":"allowed"}]},
),
dict(
name="Data Sovereignty Jurisdiction Mastery Review",
group="Advanced Sovereignty", ladder_rank=34, ladder_tier="advanced",
description="""The mastery review binds the ladder. Foundations: sovereignty is law following data across borders; residency is where bytes sleep, sovereignty whose law watches; jurisdiction runs by territory, person, provider, and effect; GDPR sets the high bar with principles, rights, transfers, and accountability; the UK stands as its own regime; US sectoral laws (HIPAA, FERPA, GLBA) guard their guilds; state laws chorus with California leading; China's PIPL/DSL wall their garden; APAC's rivers run swift; Latin America and Africa's young lions roar; residency requirements enforced by iron routing; localization mandates building sovereign quarters. Compounded: transfer gates of adequacy, SCCs, BCRs; TIAs reckoning honestly; DPAs bonding vendors; sub-processor chains of custody; sovereign clouds as fortresses; CLOUD Act access honestly mapped; data embassies as treaty soil; jurisdiction-aware road wardens; transfer journals reconciled nightly. Advanced: federal architectures; the million-realm treaty spine; conflict judgments; sovereignty accounts rendered; encryption vaults; jurisdictional key estates; rule pedigrees; lawgiver watches; cross-border fire brigades. The creed: every land's law honored, every crossing manifested, no data above the law.""",
how_it_works="""The review serves as capstone assessment and deployment checklist: can the team map jurisdictions, implement residency, mechanism transfers, and respond across borders? New sovereignty programs verify each rung: rules cited, registers complete, mechanisms assessed, playbooks drilled. Gaps become the quarter's program of work. The review repeats as laws evolve - sovereignty mastery is perpetual vigilance.""",
key_points=[
 "Foundations: sovereignty concepts, GDPR, UK, US sectoral and state, China, APAC, LATAM/Africa, residency, localization.",
 "Compounded: transfer regimes, TIAs, DPAs, sub-processors, sovereign clouds, access laws, routing, logs.",
 "Advanced: federal architectures, network spine, conflicts, metrics, encryption, keys, provenance, change tracking, incidents.",
 "The creed: every land's law honored, every crossing manifested, no data above the law.",
 "Mastery is perpetual vigilance as laws evolve."],
requirements=[
 "Demonstrated competence at every rung before program launch.",
 "Checklist rerun on legal and architectural changes.",
 "Gaps converted to funded program work."],
standards=[
 "ISO/IEC 27701."],
citations=[
 "Regulation (EU) 2016/679 (GDPR).",
 "DAMA International. DAMA-DMBOK, 2nd ed. Technics Publications, 2017."],
sig_lens="""The Signature reading: the mastery review is graduation as keeper of borders. The Signature graduate honors every land's law, manifests every crossing, and swears the creed: every land's law honored, every crossing manifested, no data above the law.""",
demo_data={"transfers":[
 {"from":"EU","to":"EU","data_class":"personal","expected":"allowed"},
 {"from":"US","to":"US","data_class":"public","expected":"allowed"}]},
),
]
