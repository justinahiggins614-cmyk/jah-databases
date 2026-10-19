#!/usr/bin/env python3
"""Authored records for the Data Sovereignty Jurisdiction databases (group F, part 1).
Public = real, fact-checked data-sovereignty knowledge (GDPR, residency, transfer
regimes). Signature = expanded Signature treatment.
Property of Justin Addam Higgins (JAH)."""

SIG_TAIL = ("Signature interpretation - original Signature-system treatment "
            "by Justin Addam Higgins; clearly labeled Signature-made, never "
            "presented as authentic public record.")

ENTRIES = [
dict(
name="What Data Sovereignty Is",
group="Sovereignty Basics", ladder_rank=1, ladder_tier="foundations",
description="""Data sovereignty is the principle that data is subject to the laws of the country where it is collected, stored, or processed - and that nations can assert control over data about their citizens and within their borders. It matters because data flows globally while law stays national: a European customer's data processed on American servers sits under two legal regimes at once, and the regimes do not always agree. Sovereignty expresses itself in requirements: where data may be stored (residency), where it may be processed, when it may cross borders (transfer rules), who may access it (government access laws), and which law governs disputes. For the million-database network, sovereignty is architectural: data placement, processing location, and transfer paths must all be jurisdiction-aware, because a network that ignores sovereignty will eventually break someone's law. Sovereignty is not anti-global - it is the legal reality that global systems must be built to respect.""",
how_it_works="""Sovereignty programs start by mapping the jurisdictions the organization touches: where data is collected, stored, processed, and whose citizens it describes. Each jurisdiction's requirements are cataloged: residency mandates, transfer conditions, access rules, breach duties. Architecture follows: data placement respects residency, processing routes respect transfer rules, access controls respect government-access constraints. The sovereignty registry records the rules per jurisdiction with citations and effective dates; change monitoring watches for new laws. Compliance is demonstrated per jurisdiction with evidence: placement records, transfer assessments, access logs.""",
key_points=[
 "Data sovereignty: data subject to the laws of where it is collected, stored, processed.",
 "Data flows globally; law stays national - systems must respect both.",
 "Expresses as residency, processing, transfer, access, and dispute rules.",
 "Sovereignty is architectural: placement, routing, and access must be jurisdiction-aware.",
 "Compliance demonstrated per jurisdiction with cited rules and evidence."],
requirements=[
 "Jurisdiction mapping: collection, storage, processing, citizenship.",
 "Per-jurisdiction requirement catalogs with citations.",
 "Jurisdiction-aware architecture for placement, routing, access.",
 "Change monitoring for new and amended laws."],
standards=[
 "ISO/IEC 27701; ISO 27018 for cloud privacy."],
citations=[
 "Regulation (EU) 2016/679 (GDPR).",
 "DAMA International. DAMA-DMBOK, 2nd ed. Technics Publications, 2017."],
sig_lens="""The Signature reading: sovereignty is the registry honoring every land's law over the data that touches it. The Signature network builds its roads with borders in mind - global in reach, lawful in every land.""",
demo_data={"transfers":[
 {"from":"EU","to":"EU","data_class":"personal","expected":"allowed"},
 {"from":"EU","to":"US","data_class":"personal","expected":"restricted:SCCs-required"},
 {"from":"US","to":"US","data_class":"public","expected":"allowed"}]},
),
dict(
name="Data Residency vs Data Sovereignty",
group="Sovereignty Basics", ladder_rank=2, ladder_tier="foundations",
description="""Residency and sovereignty are related but different, and confusing them causes expensive architecture mistakes. Data residency is about location: the data must be stored (and sometimes processed) within a country's borders. Data sovereignty is about law: which country's laws govern the data, regardless of where the bytes sit. Residency is the stricter, narrower concept - a residency mandate forces local data centers. Sovereignty is broader: even without a residency mandate, the data may be subject to a country's access laws (a government demanding data from a provider subject to its jurisdiction, wherever the servers are) or transfer rules (data may leave only under approved mechanisms). The practical consequence: meeting residency does not guarantee sovereignty compliance, and sovereignty compliance sometimes requires more than residency - contractual protections, encryption with local keys, transfer assessments. Architects ask both questions separately: where must the bytes live, and whose law governs them?""",
how_it_works="""Sovereignty analysis answers the two questions per dataset: residency requirements (storage and processing location mandates) and governing-law requirements (which regimes apply by collection, citizenship, and provider jurisdiction). Architecture implements both: placement controls for residency, legal mechanisms (contracts, assessments, encryption) for sovereignty. The registry records both dimensions per dataset with citations. Compliance checks verify placement against residency rules and mechanisms against sovereignty rules independently. Reviews revisit both when laws change or when providers' jurisdictions change (an acquisition can change whose law governs overnight).""",
key_points=[
 "Residency: where bytes must live. Sovereignty: whose law governs.",
 "Meeting residency does not guarantee sovereignty compliance.",
 "Sovereignty may need contracts, local-key encryption, transfer assessments beyond location.",
 "Provider jurisdiction matters: acquisitions can change governing law overnight.",
 "Architects answer both questions separately per dataset."],
requirements=[
 "Separate residency and governing-law analysis per dataset.",
 "Placement controls plus legal mechanisms in architecture.",
 "Registry records for both dimensions with citations.",
 "Reviews on law changes and provider jurisdiction changes."],
standards=[
 "ISO/IEC 27701; ISO 27018."],
citations=[
 "Regulation (EU) 2016/679 (GDPR).",
 "DAMA International. DAMA-DMBOK, 2nd ed. Technics Publications, 2017."],
sig_lens="""The Signature reading: residency is where the data sleeps; sovereignty is whose law watches it sleep. The Signature registry asks both questions and answers both - never mistaking the bedroom for the guardian.""",
demo_data={"transfers":[
 {"from":"CN","to":"CN","data_class":"personal","expected":"allowed"},
 {"from":"CN","to":"US","data_class":"personal","expected":"restricted:security-assessment"},
 {"from":"EU","to":"UK","data_class":"personal","expected":"allowed:adequacy"}]},
),
dict(
name="Jurisdiction Concepts",
group="Sovereignty Basics", ladder_rank=3, ladder_tier="foundations",
description="""Jurisdiction is the authority of a legal system over people, acts, and data - and data lives under several jurisdictional theories at once. Territorial jurisdiction: the law of where the data is (stored or processed). Personal jurisdiction: the law of whose data it is (citizenship or residency of the data subject). Provider jurisdiction: the law governing the company holding the data (where it is incorporated or operates). Effects jurisdiction: the law of where the data's use has effects. A single dataset routinely sits under four at once: EU citizen data, stored in Ireland, processed by a US company, used to decide EU loans. The registry's jurisdiction model records all applicable theories per dataset with their legal basis, because compliance means satisfying the strictest combination, not picking the friendliest. Conflict of laws - when two jurisdictions demand opposite things - escalates to counsel; the registry records the resolution as precedent.""",
how_it_works="""Jurisdiction analysis per dataset identifies applicable regimes under each theory with legal citations. The compliance engine computes the strictest combination: residency from territorial, transfer rules from personal, access obligations from provider jurisdiction. Conflict detection flags opposing demands (retain here, delete there) for counsel resolution with documented precedent. The registry versions jurisdictional determinations - provider acquisitions and law changes trigger re-analysis. Compliance evidence organizes per regime for regulator inquiries.""",
key_points=[
 "Four theories: territorial (where data is), personal (whose data), provider (who holds), effects (where used).",
 "Datasets routinely sit under several at once; compliance takes the strictest combination.",
 "Conflicts of law escalate to counsel with precedent recorded.",
 "Provider acquisitions can change jurisdiction overnight - re-analysis required.",
 "Evidence organizes per regime for regulators."],
requirements=[
 "Jurisdictional analysis per dataset with cited theories.",
 "Strictest-combination compliance computation.",
 "Conflict detection with counsel escalation.",
 "Re-analysis triggers on acquisitions and law changes."],
standards=[
 "ISO/IEC 27701."],
citations=[
 "Regulation (EU) 2016/679 (GDPR).",
 "DAMA International. DAMA-DMBOK, 2nd ed. Technics Publications, 2017."],
sig_lens="""The Signature reading: jurisdiction is the registry mapping every law that claims the data - by land, by person, by holder, by effect. The Signature registry serves the strictest master and judges conflicts openly.""",
demo_data={"transfers":[
 {"from":"EU","to":"EU","data_class":"personal","expected":"allowed"},
 {"from":"UK","to":"US","data_class":"personal","expected":"restricted:SCCs-required"}]},
),
dict(
name="GDPR and the European Union",
group="Sovereignty Basics", ladder_rank=4, ladder_tier="foundations",
description="""The General Data Protection Regulation (GDPR) is the world's most influential data protection law, applying to personal data of EU/EEA individuals regardless of where the processing happens. Its core principles: lawfulness, fairness, and transparency; purpose limitation; data minimization; accuracy; storage limitation; integrity and confidentiality; and accountability - the controller must demonstrate compliance, not just claim it. Its rights: access, rectification, erasure, restriction, portability, objection. Its transfer regime: personal data may leave the EEA only to adequate countries, under safeguards (Standard Contractual Clauses, Binding Corporate Rules), or under narrow derogations. Its enforcement: fines up to 4 percent of global turnover, imposed by cooperating supervisory authorities. For the network, GDPR sets the high bar: lawfulness documented, minimization enforced, erasure propagated, transfers assessed, breaches notified within 72 hours. Systems built to GDPR's bar generally satisfy weaker regimes; the reverse is never true.""",
how_it_works="""GDPR programs implement: records of processing activities, lawful-basis documentation per purpose, data protection impact assessments for high-risk processing, privacy-by-design in systems, rights-handling workflows (access, erasure, portability within deadlines), breach notification procedures (72 hours to authorities), transfer mechanisms with assessments, and DPO oversight where required. The registry records GDPR applicability per dataset with the lawful basis and retention justification. Compliance evidence - RoPAs, DPIAs, transfer assessments, breach logs - is maintained audit-ready. Supervisory authority cooperation means the lead authority coordinates cross-border cases.""",
key_points=[
 "GDPR: principles, rights, transfer regime, accountability, 4-percent fines.",
 "Applies by data subject (EU/EEA individuals), not by processor location.",
 "Transfers need adequacy, safeguards (SCCs/BCRs), or derogations.",
 "Accountability: demonstrate compliance with evidence, not claims.",
 "Build to GDPR's bar; weaker regimes generally follow."],
requirements=[
 "Records of processing with lawful bases per purpose.",
 "DPIAs for high-risk processing; privacy by design.",
 "Rights workflows meeting legal deadlines.",
 "Transfer mechanisms with assessments; 72-hour breach notification."],
standards=[
 "GDPR (Regulation (EU) 2016/679); ISO/IEC 27701."],
citations=[
 "Regulation (EU) 2016/679 (GDPR).",
 "European Data Protection Board guidance."],
sig_lens="""The Signature reading: GDPR is the high law of personal data - principles sworn, rights granted, transfers guarded, accountability proven. The Signature registry builds to its bar and keeps the evidence ready.""",
demo_data={"transfers":[
 {"from":"EU","to":"US","data_class":"personal","expected":"restricted:SCCs-required"},
 {"from":"EU","to":"JP","data_class":"personal","expected":"allowed:adequacy"}]},
),
dict(
name="UK Data Protection Regime",
group="Sovereignty Basics", ladder_rank=5, ladder_tier="foundations",
description="""The UK's data protection regime - the UK GDPR plus the Data Protection Act 2018 - mirrors the EU GDPR with domestic adaptations, following Brexit. The UK granted the EU adequacy (EU-to-UK transfers flow freely); the EU granted the UK adequacy (time-limited, reviewed), so UK-to-EU transfers flow under the adequacy decision while it stands. The UK's Information Commissioner's Office enforces with GDPR-scale fines. Divergences are growing: UK reform proposals adjust accountability burdens and international transfer rules, and the UK pursues its own adequacy partnerships. For systems, the practical rule is dual compliance: meet the stricter of UK and EU requirements where they differ, track adequacy decisions' status (they can be revoked), and maintain UK-specific transfer instruments (UK SCCs / International Data Transfer Agreements) alongside EU ones. The registry treats the UK as its own jurisdiction with its own rule set, not as an EU footnote.""",
how_it_works="""UK compliance mirrors GDPR programs with UK-specific instruments: UK transfer agreements, UK representative where required, ICO notification procedures. Adequacy status for each direction is monitored - EU-to-UK and UK-to-EU - with contingency plans (SCCs ready) if adequacy lapses. Divergence tracking compares UK and EU requirements per dataset, applying the stricter. The registry's jurisdiction rules version UK requirements independently; change monitoring watches UK reform legislation.""",
key_points=[
 "UK GDPR + DPA 2018: mirrors EU GDPR with domestic adaptations.",
 "Mutual adequacy enables free flows while decisions stand - monitored, not assumed.",
 "UK-specific instruments: IDTAs alongside EU SCCs.",
 "Dual compliance: meet the stricter where UK and EU diverge.",
 "The UK is its own jurisdiction in the registry, not an EU footnote."],
requirements=[
 "UK transfer instruments and representative arrangements.",
 "Adequacy monitoring with SCC contingencies.",
 "Divergence tracking applying the stricter rule.",
 "Independent UK rule versioning with reform monitoring."],
standards=[
 "UK GDPR; Data Protection Act 2018."],
citations=[
 "Data Protection Act 2018 (UK).",
 "UK Information Commissioner's Office guidance."],
sig_lens="""The Signature reading: the UK regime is its own law now - sibling to the EU's, diverging by degrees. The Signature registry honors it separately, watches the adequacy bridges, and keeps the stricter promise where they differ.""",
demo_data={"transfers":[
 {"from":"UK","to":"EU","data_class":"personal","expected":"allowed:adequacy"},
 {"from":"UK","to":"US","data_class":"personal","expected":"restricted:IDTA-required"}]},
),
dict(
name="US Sectoral Laws: HIPAA, FERPA, GLBA",
group="Sovereignty Basics", ladder_rank=6, ladder_tier="foundations",
description="""The United States has no single data protection law; instead, sectoral laws govern specific data types. HIPAA governs protected health information: privacy rules limiting uses, security rules requiring safeguards, breach notification rules, with business associate agreements extending obligations to vendors. FERPA governs education records: parental (and student) rights to access and amend, limits on disclosure without consent, and school official exceptions. GLBA governs financial institutions' nonpublic personal information: privacy notices, opt-out rights for sharing, and safeguards rules. Each carries its own retention, breach, and sharing rules - and its own enforcers. For systems handling American data, the discipline is classification-driven: tag the data by sector (health, education, financial), and the sector's rules attach automatically. State laws then layer on top, because sectoral coverage leaves gaps the states fill.""",
how_it_works="""Classification tags data by sector; sector rule packs apply automatically: HIPAA's minimum-necessary and BAA requirements for PHI, FERPA's consent and directory-information rules for education records, GLBA's notices and opt-outs for financial data. Business associate and service provider agreements flow obligations to vendors. Breach rules per sector trigger the right notifications. The registry's US rules layer sectoral packs under state laws, computing the strictest combination. Sector applicability is reviewed when data uses change - the wellness app that becomes a HIPAA-covered service.""",
key_points=[
 "US privacy is sectoral: HIPAA (health), FERPA (education), GLBA (financial).",
 "Each has its own privacy, security, breach, and sharing rules.",
 "Classification by sector attaches the right rule pack automatically.",
 "Vendor obligations flow through BAAs and service agreements.",
 "State laws layer on top; sector changes trigger re-review."],
requirements=[
 "Sector classification with automatic rule-pack attachment.",
 "Vendor agreement workflows (BAAs, service provider terms).",
 "Sector-specific breach notification procedures.",
 "Re-review triggers on data-use changes."],
standards=[
 "HIPAA Privacy/Security/Breach Rules; FERPA; GLBA Safeguards Rule."],
citations=[
 "45 CFR Part 160, 164 (HIPAA).",
 "20 U.S.C. 1232g (FERPA); 15 U.S.C. 6801-6809 (GLBA)."],
sig_lens="""The Signature reading: America's sectoral laws are guild rules - each trade guarding its own secrets by its own code. The Signature registry sorts data into its guilds and enforces each guild's code.""",
demo_data={"transfers":[
 {"from":"US","to":"US","data_class":"phi","expected":"restricted:HIPAA-minimum-necessary"},
 {"from":"US","to":"US","data_class":"public","expected":"allowed"}]},
),
dict(
name="US State Privacy Laws: CCPA and CPRA",
group="Sovereignty Basics", ladder_rank=7, ladder_tier="foundations",
description="""California's CCPA as amended by the CPRA is the de facto American privacy standard, with siblings in Colorado, Connecticut, Virginia, and a growing list. The core rights: know what personal information is collected, delete it, correct it, opt out of sale/sharing, limit use of sensitive personal information, and non-discrimination for exercising rights. The thresholds apply to businesses meeting size or data-volume criteria - and the network's scale clears them. Operationally, the laws demand: consumer request workflows (45-day response), opt-out mechanisms (including Global Privacy Control signals), data inventories proving what is held where, service provider agreements limiting vendors, and cybersecurity audits for high-risk processing. The trend is more states, not fewer, with a common core and local variations - the registry handles this with a state-law matrix applying each state's specifics, and the strictest-common-core as the baseline build.""",
how_it_works="""State-law programs implement consumer request workflows with identity verification and 45-day clocks, opt-out honoring including GPC signals, data inventories per state, and vendor agreements. The registry's state matrix encodes each state's thresholds, rights, and timelines; the baseline build meets the strictest common core. Request metrics track volumes and SLA adherence per state. New state laws enter the matrix through the change-monitoring process with gap analysis against the baseline.""",
key_points=[
 "CCPA/CPRA rights: know, delete, correct, opt out of sale/sharing, limit sensitive use.",
 "Operational duties: request workflows, GPC honoring, inventories, vendor agreements.",
 "More states join with a common core plus variations - matrix-managed.",
 "Baseline build meets the strictest common core.",
 "New state laws enter via change monitoring with gap analysis."],
requirements=[
 "Consumer request workflows with 45-day clocks.",
 "Opt-out mechanisms honoring Global Privacy Control.",
 "State-law matrix with per-state specifics.",
 "Data inventories proving holdings per state."],
standards=[
 "CCPA/CPRA; state privacy statutes."],
citations=[
 "California Consumer Privacy Act (as amended by CPRA).",
 "Colorado Privacy Act; Virginia CDPA."],
sig_lens="""The Signature reading: the state laws are a growing chorus - California leading, the states joining, each verse its own. The Signature registry sings the strictest common harmony and learns each new verse as it comes.""",
demo_data={"transfers":[
 {"from":"US-CA","to":"US-CA","data_class":"personal","expected":"allowed"},
 {"from":"US-CA","to":"US-TX","data_class":"personal","expected":"allowed:service-provider-terms"}]},
),
dict(
name="China: PIPL and Data Security Law",
group="Sovereignty Basics", ladder_rank=8, ladder_tier="foundations",
description="""China's Personal Information Protection Law (PIPL), Data Security Law (DSL), and Cybersecurity Law form one of the world's strictest data regimes. PIPL requires separate consent for sensitive personal information and for cross-border transfers, mandates security assessments (CAC assessments) for important data and large-volume transfers abroad, and gives individuals rights including erasure and portability. The DSL classifies data by importance - core data faces the strictest controls including potential export bans - and requires data classification and protection by tier. Cross-border transfer requires one of three mechanisms: CAC security assessment, personal information protection certification, or standard contracts filed with authorities. Data localization applies to critical information infrastructure operators and to important data. For the network, China is a distinct sovereignty zone: local storage, local processing, assessed transfers, and separate consent - architected as a separable region, not as an afterthought.""",
how_it_works="""China programs implement: data classification (general, important, core), separate-consent workflows, cross-border transfer mechanisms per volume and sensitivity (CAC assessment, certification, or standard contracts), localization for CIIO and important data, and individual rights handling. Transfer assessments document necessity and protection. The registry's China rules version independently with regulatory monitoring; the architecture maintains a separable China region with controlled, assessed bridges. Compliance evidence organizes per mechanism for CAC inquiry readiness.""",
key_points=[
 "PIPL: separate consent for sensitive data and cross-border transfers; individual rights.",
 "DSL: data classified by importance; core data faces export restrictions.",
 "Transfers need CAC assessment, certification, or filed standard contracts.",
 "Localization for critical infrastructure operators and important data.",
 "China architected as a separable sovereignty zone."],
requirements=[
 "Data importance classification (general/important/core).",
 "Separate-consent workflows.",
 "Transfer mechanism selection with assessments.",
 "Separable regional architecture with controlled bridges."],
standards=[
 "PIPL; Data Security Law; Cybersecurity Law (PRC)."],
citations=[
 "Personal Information Protection Law of the PRC (2021).",
 "Data Security Law of the PRC (2021)."],
sig_lens="""The Signature reading: China's regime is a walled garden with guarded gates - separate consents, assessed transfers, local soil for important data. The Signature registry builds the garden's own quarter and passes its gates only with papers in order.""",
demo_data={"transfers":[
 {"from":"CN","to":"CN","data_class":"personal","expected":"allowed"},
 {"from":"CN","to":"US","data_class":"personal","expected":"restricted:security-assessment"},
 {"from":"CN","to":"US","data_class":"important","expected":"restricted:CAC-assessment"}]},
),
dict(
name="Other APAC Regimes",
group="Sovereignty Basics", ladder_rank=9, ladder_tier="foundations",
description="""Asia-Pacific holds diverse, fast-evolving data regimes. Japan's APPI (amended 2022) requires opt-out or consent for third-party provision and is EU-adequate. South Korea's PIPA is consent-heavy with strong breach notification. Singapore's PDPA requires consent with deemed-consent refinements and mandatory breach notification. India's DPDP Act (2023) introduces consent-based processing with government-notified significant data fiduciaries facing extra duties. Australia's Privacy Act (with reforms progressing) centers on the Australian Privacy Principles. Indonesia, Thailand, Vietnam, and the Philippines each have comprehensive laws now. The pattern across APAC: consent-centric, breach notification mandatory, cross-border transfer conditions tightening, and localization appearing for sensitive sectors. The registry's APAC matrix tracks each regime's consent model, transfer conditions, breach timelines, and localization triggers - because the region's laws change yearly, not decadely.""",
how_it_works="""The APAC matrix encodes per-jurisdiction consent models, transfer conditions, breach timelines, and localization triggers with citations. Consent workflows adapt per regime (opt-in vs opt-out vs deemed). Transfer assessments run per corridor. Breach notification clocks per jurisdiction are codified in incident playbooks. Regulatory monitoring is continuous - APAC laws amend frequently - with matrix updates and gap analyses. Local counsel validates the matrix annually per jurisdiction.""",
key_points=[
 "APAC: consent-centric, mandatory breach notification, tightening transfers.",
 "Japan EU-adequate; Korea consent-heavy; India DPDP with significant fiduciaries.",
 "Localization appears for sensitive sectors in several regimes.",
 "Laws change yearly - continuous monitoring, not decadal reviews.",
 "Per-jurisdiction matrix with local counsel validation."],
requirements=[
 "APAC jurisdiction matrix with consent, transfer, breach, localization rules.",
 "Adaptive consent workflows per regime.",
 "Continuous regulatory monitoring with gap analyses.",
 "Annual local-counsel validation per jurisdiction."],
standards=[
 "APPI (Japan); PIPA (Korea); PDPA (Singapore); DPDP Act (India)."],
citations=[
 "Act on Protection of Personal Information (Japan).",
 "Digital Personal Data Protection Act, 2023 (India)."],
sig_lens="""The Signature reading: APAC's regimes are swift rivers - consent-centric, ever-changing, each with its own crossings. The Signature registry charts each river yearly and never assumes last year's ford.""",
demo_data={"transfers":[
 {"from":"JP","to":"EU","data_class":"personal","expected":"allowed:adequacy"},
 {"from":"SG","to":"US","data_class":"personal","expected":"restricted:transfer-conditions"}]},
),
dict(
name="Latin America and Africa Regimes",
group="Sovereignty Basics", ladder_rank=10, ladder_tier="foundations",
description="""Latin America and Africa increasingly mirror GDPR's shape with local character. Brazil's LGPD is the region's anchor: GDPR-like principles and rights, with the ANPD enforcing and adequacy decisions progressing. Argentina, Colombia, Mexico, and Chile have comprehensive laws; Argentina holds EU adequacy. Africa's landscape: South Africa's POPIA (with its Information Regulator), Kenya's DPA, Nigeria's NDPR/NDPA, Egypt's law, and the African Union's Malabo Convention pushing continental harmonization - plus data localization in several states for sensitive categories. The practical pattern: GDPR-shaped rights and principles, local enforcement with growing teeth, transfer mechanisms modeled on adequacy and SCCs, and localization for government and sensitive data in some regimes. The registry treats these as first-class jurisdictions with their own rule sets and monitoring, not as GDPR afterthoughts - because local regulators increasingly disagree with the assumption that GDPR compliance suffices.""",
how_it_works="""The LATAM/Africa matrix encodes principles, rights, transfer mechanisms, breach duties, and localization triggers per jurisdiction with citations. LGPD and POPIA programs run with local specifics (ANPD guidance, Information Regulator procedures). Transfer assessments per corridor use local instruments. Localization requirements map to architecture placement. Regulatory monitoring covers Portuguese, Spanish, French, and English sources; local counsel validates. Enforcement trend analysis prioritizes the regimes whose regulators are most active.""",
key_points=[
 "Brazil LGPD and South Africa POPIA anchor their regions; Argentina EU-adequate.",
 "GDPR-shaped rights with local enforcement of growing strength.",
 "Transfer mechanisms modeled on adequacy and SCCs, locally instrumented.",
 "Localization for government and sensitive data in several regimes.",
 "First-class jurisdictions with own monitoring - not GDPR footnotes."],
requirements=[
 "LATAM/Africa jurisdiction matrix with citations.",
 "Local transfer instruments and localization mapping.",
 "Multilingual regulatory monitoring.",
 "Enforcement trend analysis for prioritization."],
standards=[
 "LGPD (Brazil); POPIA (South Africa); Malabo Convention."],
citations=[
 "Lei Geral de Protecao de Dados (Brazil, Law 13.709/2018).",
 "Protection of Personal Information Act (South Africa, 2013)."],
sig_lens="""The Signature reading: these regimes are young lions - GDPR-shaped but sovereign, their roars growing yearly. The Signature registry respects each lion's territory and never assumes the old pride's rules suffice.""",
demo_data={"transfers":[
 {"from":"BR","to":"EU","data_class":"personal","expected":"restricted:transfer-mechanism"},
 {"from":"ZA","to":"ZA","data_class":"personal","expected":"allowed"}]},
),
dict(
name="Residency Requirements",
group="Residency and Storage", ladder_rank=11, ladder_tier="foundations",
description="""Residency requirements mandate that certain data stay within national borders: Russia's data localization law, China's CIIO and important-data rules, India's payment data localization (RBI), Indonesia's and Vietnam's sectoral mandates, and growing lists elsewhere. Requirements vary in scope: some cover all personal data, most target sectors (finance, health, telecom, government) or data categories (important, sensitive). Architecture answers with placement controls: data tagged by residency class routes to in-country storage and processing, enforced by infrastructure policy - not by convention. The failure mode is leakage through the side doors: backups replicated abroad, analytics copies in a global lake, support engineers accessing from anywhere, ML training on foreign GPUs. Residency compliance therefore covers the full data lifecycle - storage, processing, backup, analytics, support access, and model training - with each path verified. Residency attestations, backed by placement evidence, answer regulators' where-is-my-data questions.""",
how_it_works="""Residency classes tag data per applicable mandates; infrastructure policies route storage and processing to compliant regions mechanically. Placement verification audits actual locations against requirements continuously. Side-door controls cover backups (in-country or crypto-shredded), analytics (regional lakes), support access (regional or approved-remote with logging), and training (regional compute). Residency evidence - placement records, policy versions, verification results - compiles into attestations per regulator. New mandates enter through change monitoring with architecture gap analysis.""",
key_points=[
 "Residency mandates vary by scope: sectors, categories, or all personal data.",
 "Enforced by infrastructure policy, not convention.",
 "Side doors leak: backups, analytics copies, support access, training compute.",
 "Full-lifecycle coverage: storage, processing, backup, analytics, access, training.",
 "Placement evidence compiles into regulator attestations."],
requirements=[
 "Residency classification with infrastructure routing policies.",
 "Continuous placement verification.",
 "Side-door controls across the lifecycle.",
 "Attestation compilation with evidence."],
standards=[
 "ISO/IEC 27701; ISO 27018."],
citations=[
 "Reserve Bank of India. Storage of Payment System Data (2018).",
 "Federal Law No. 242-FZ (Russia) (localization provisions)."],
sig_lens="""The Signature reading: residency is the law of where data sleeps - enforced by iron routing, verified continuously, with every side door guarded. The Signature registry proves each dataset's bedroom to any regulator who asks.""",
demo_data={"transfers":[
 {"from":"IN","to":"IN","data_class":"payment","expected":"allowed"},
 {"from":"IN","to":"US","data_class":"payment","expected":"restricted:localization"},
 {"from":"RU","to":"RU","data_class":"personal","expected":"allowed"}]},
),
dict(
name="Localization Mandates",
group="Residency and Storage", ladder_rank=12, ladder_tier="foundations",
description="""Localization mandates go beyond storage: they require processing, and sometimes the entire data lifecycle, to happen domestically. The strictest forms demand local copies be primary and authoritative, restrict remote access to them, and require local personnel for administration. Mandates typically target critical sectors - government, finance, telecom, health - and sensitive categories, with the list growing as digital sovereignty politics intensify. Compliance architecture uses sovereignty zones: separable regional deployments with local data planes, local keys, and local operations, connected to the global system only through assessed, logged bridges. The operational cost is real - duplicated infrastructure, split operations - so scoping precision matters: apply localization exactly where mandated, with the mandate's text as the scoping authority, and document the boundary. Over-localization wastes millions; under-localization breaks the law. The registry's mandate catalog records each mandate's scope text, effective date, and the architecture boundary drawn from it.""",
how_it_works="""The mandate catalog records scope text, dates, and architectural boundaries per mandate. Sovereignty zones implement separable regional deployments with local data planes, keys, and operations. Bridges between zones carry only assessed, logged flows. Scoping reviews verify the boundary matches the mandate text - neither over nor under. Cost tracking per zone informs the over/under-localization balance. Mandate changes trigger re-scoping with architecture impact analysis.""",
key_points=[
 "Localization can require domestic processing and administration, not just storage.",
 "Sovereignty zones: separable regional deployments with local everything.",
 "Inter-zone bridges carry only assessed, logged flows.",
 "Scoping precision matters: over-localization wastes, under-localization breaks law.",
 "Mandate catalog records scope text and drawn boundaries."],
requirements=[
 "Mandate catalog with scope text and boundaries.",
 "Separable sovereignty-zone architectures.",
 "Assessed, logged inter-zone bridges.",
 "Scoping reviews against mandate text."],
standards=[
 "ISO/IEC 27701."],
citations=[
 "Data Security Law of the PRC (localization provisions).",
 "DAMA International. DAMA-DMBOK, 2nd ed. Technics Publications, 2017."],
sig_lens="""The Signature reading: localization is the strictest landlords' law - not just sleep here, but live and work here. The Signature registry builds each mandated quarter self-sufficient and bridges them only with inspected crossings.""",
demo_data={"transfers":[
 {"from":"CN","to":"CN","data_class":"important","expected":"allowed"},
 {"from":"CN","to":"US","data_class":"important","expected":"restricted:localization"},
 {"from":"ID","to":"ID","data_class":"financial","expected":"allowed"}]},
),
]
