#!/usr/bin/env python3
"""Data Sovereignty Jurisdiction entries 13-24 (compounded)."""

APPEND = [
dict(
name="Cross-Border Transfer Rules",
group="Transfer Regimes", ladder_rank=13, ladder_tier="compounded",
description="""Cross-border transfer rules govern when data may leave its jurisdiction: the legal gates every international flow must pass. The common patterns: adequacy (the destination country's protections are deemed sufficient - data flows freely), safeguards (the exporter adds protections - contracts, binding rules - to make the transfer safe), and derogations (narrow exceptions: explicit consent, contract necessity, vital interests). Each transfer needs its gate identified before it flows - the registry's transfer register records every cross-border flow with its mechanism, and flows without mechanisms are blocked. The rules apply per data category: personal data faces the strict gates; anonymized data (truly anonymous, not merely pseudonymized) generally flows freely; important/core data faces the strictest gates of all. Transfer compliance is continuous, not one-time: adequacy decisions can be revoked, safeguards need reassessment, and the register is audited against actual flows.""",
how_it_works="""The transfer register catalogs every cross-border flow: data categories, source and destination jurisdictions, mechanism (adequacy citation, safeguard instrument, derogation basis), assessment reference, and owner. Flow discovery (network monitoring, lineage analysis) finds undeclared transfers for registration or shutdown. Mechanism monitoring tracks adequacy status and safeguard validity; revocations trigger re-mechanism workflows. Assessments attach to register entries with review dates. Audits compare registered flows against observed flows; gaps are incidents.""",
key_points=[
 "Transfer gates: adequacy, safeguards (SCCs/BCRs), derogations - identified before flowing.",
 "The transfer register records every cross-border flow with its mechanism.",
 "Rules apply per category: personal strict, truly anonymous freer, important strictest.",
 "Adequacy can be revoked; safeguards need reassessment - compliance is continuous.",
 "Observed-vs-registered audits catch undeclared transfers."],
requirements=[
 "Transfer registers with mechanisms and assessments per flow.",
 "Flow discovery for undeclared transfers.",
 "Adequacy and safeguard monitoring with re-mechanism workflows.",
 "Observed-vs-registered audits."],
standards=[
 "GDPR Chapter V; ISO/IEC 27701."],
citations=[
 "Regulation (EU) 2016/679 (GDPR), Chapter V.",
 "European Data Protection Board transfer guidance."],
sig_lens="""The Signature reading: transfer rules are the border crossings' law - every flow with its papers, every gate named, no smuggling. The Signature registry mans every crossing and audits the traffic against the manifests.""",
demo_data={"transfers":[
 {"from":"EU","to":"US","data_class":"personal","expected":"restricted:SCCs-required"},
 {"from":"EU","to":"CH","data_class":"personal","expected":"allowed:adequacy"},
 {"from":"EU","to":"US","data_class":"anonymous","expected":"allowed"}]},
),
dict(
name="Adequacy Decisions",
group="Transfer Regimes", ladder_rank=14, ladder_tier="compounded",
description="""Adequacy decisions are a government's finding that another country's data protections are essentially equivalent to its own - the gold standard for transfers, because data flows to adequate countries as freely as domestically. The EU has granted adequacy to a short list: the UK (time-limited), Japan, Switzerland, Israel, New Zealand, and others - each decision scoped and reviewable. Adequacy is political as well as legal: the Schrems II judgment struck down the EU-US Privacy Shield, ending years of transfers overnight and forcing the industry onto SCCs until the Data Privacy Framework. The operational discipline: track adequacy per corridor (A-to-B is not B-to-A), monitor for reviews and revocations, maintain fallback mechanisms (SCCs ready) for corridors whose adequacy is fragile, and never build architecture that assumes adequacy is permanent. Adequacy decisions cite in transfer registers with their scope and review dates.""",
how_it_works="""The adequacy tracker monitors each relevant decision: scope, review dates, political risk signals. Transfer registers cite adequacy decisions per corridor with fallback mechanisms documented. Revocation playbooks activate on adverse judgments: switch corridors to SCCs, assess the new risk, notify affected owners. Architecture avoids adequacy-only dependencies for critical flows - dual mechanisms where the corridor matters. Monitoring covers official journals, court dockets, and regulatory announcements for early warning.""",
key_points=[
 "Adequacy lets data flow as freely as domestically - the gold standard.",
 "Decisions are scoped, reviewable, and political - Schrems II ended Privacy Shield overnight.",
 "Track per corridor; A-to-B adequacy is not B-to-A.",
 "Maintain fallback mechanisms for fragile corridors.",
 "Never architect critical flows on adequacy alone."],
requirements=[
 "Adequacy tracking with scope, reviews, risk signals.",
 "Fallback mechanisms documented per corridor.",
 "Revocation playbooks with corridor-switching procedures.",
 "Early-warning monitoring of courts and regulators."],
standards=[
 "GDPR Article 45."],
citations=[
 "CJEU. Schrems II (C-311/18). 2020.",
 "European Commission adequacy decisions."],
sig_lens="""The Signature reading: adequacy is the treaty of free passage between realms - precious, political, revocable. The Signature registry honors the treaties, watches the politics, and keeps the old roads ready.""",
demo_data={"transfers":[
 {"from":"EU","to":"JP","data_class":"personal","expected":"allowed:adequacy"},
 {"from":"EU","to":"US","data_class":"personal","expected":"restricted:DPF-or-SCCs"}]},
),
dict(
name="Standard Contractual Clauses",
group="Transfer Regimes", ladder_rank=15, ladder_tier="compounded",
description="""Standard Contractual Clauses (SCCs) are the workhorse transfer safeguard: pre-approved contract terms that exporters and importers sign, binding the importer to protect the data as the source jurisdiction requires. The EU's modernized SCCs (2021) come in modules - controller-to-controller, controller-to-processor, processor-to-processor, processor-to-controller - with obligations on purpose limitation, security, sub-processors, data subject rights, and government access transparency. SCCs are not sign-and-forget: Schrems II requires assessing whether the destination country's laws undermine the clauses' protections (the transfer impact assessment), and adding supplementary measures where needed (encryption the importer cannot break, access controls, transparency commitments). The registry tracks SCC execution per transfer: which module, signed when, by whom, with which supplementary measures - because an unsigned or unassessed SCC is paperwork, not protection.""",
how_it_works="""Transfer workflows select the SCC module per relationship, execute with authorized signatories, and attach transfer impact assessments with supplementary measures. The SCC register tracks execution status, signatories, dates, and measures per transfer. Reassessment runs on schedule and on trigger (destination law changes, Schrems-like judgments). Supplementary measures implement technically: encryption with exporter-held keys, strict access controls, government-request transparency procedures. Audits verify executed, assessed, and measured transfers; gaps become incidents.""",
key_points=[
 "SCCs: pre-approved clauses binding importers to source-jurisdiction protections.",
 "Modules per relationship: controller/processor combinations.",
 "Schrems II requires transfer impact assessments plus supplementary measures where needed.",
 "Track execution, signatories, measures per transfer - unassessed SCCs are paperwork.",
 "Reassess on destination law changes."],
requirements=[
 "SCC module selection and execution workflows.",
 "Transfer impact assessments with supplementary measures.",
 "SCC register with execution tracking.",
 "Scheduled reassessment and audit."],
standards=[
 "EU SCCs (2021/914); UK IDTA."],
citations=[
 "Commission Implementing Decision (EU) 2021/914 (SCCs).",
 "CJEU. Schrems II (C-311/18). 2020."],
sig_lens="""The Signature reading: SCCs are sworn oaths between sender and receiver - standardized, signed, and tested against the destination's laws. The Signature registry keeps every oath executed, assessed, and re-examined.""",
demo_data={"transfers":[
 {"from":"EU","to":"US","data_class":"personal","expected":"restricted:SCCs-required"},
 {"from":"EU","to":"IN","data_class":"personal","expected":"restricted:SCCs-required"}]},
),
dict(
name="Binding Corporate Rules",
group="Transfer Regimes", ladder_rank=16, ladder_tier="compounded",
description="""Binding Corporate Rules (BCRs) let multinational groups transfer personal data internally under one approved framework: the group's global privacy rules, approved by regulators, binding every member company. BCRs suit organizations with heavy intra-group flows - shared services, global HR, centralized analytics - where signing SCCs for every flow would be impractical. Approval is rigorous: the rules must demonstrate enforceable rights for data subjects, clear responsibilities, training, audit, and complaint handling - and approval takes a year or more through the consistency mechanism. Once approved, intra-group transfers flow under the BCRs with the approval as the mechanism, though transfer impact assessments still apply per Schrems II. BCRs demand ongoing compliance: training records, audit programs, complaint handling, and updates approved when the business changes. For groups that qualify, BCRs are the most elegant transfer solution; for others, the approval burden makes SCCs the pragmatic choice.""",
how_it_works="""BCR programs draft group-wide rules covering principles, rights, responsibilities, training, audit, and complaints; submit through the lead authority's consistency process; and implement upon approval with training and intra-group agreements. The BCR register tracks approved scope, member entities, and covered flows. Transfer impact assessments still run per destination. Ongoing compliance maintains training, audits, complaint handling, and change-approved updates. Annual BCR compliance reports go to the lead authority; material business changes trigger re-approval workflows.""",
key_points=[
 "BCRs: regulator-approved group rules enabling internal transfers.",
 "Best for heavy intra-group flows; approval takes a year or more.",
 "Must show enforceable rights, responsibilities, training, audit, complaints.",
 "Transfer impact assessments still apply per destination.",
 "Ongoing compliance: training, audits, complaints, approved updates."],
requirements=[
 "BCR drafting with full governance apparatus.",
 "Consistency-mechanism approval process management.",
 "Intra-group implementation with training.",
 "Ongoing compliance program with authority reporting."],
standards=[
 "GDPR Article 47; EDPB BCR guidance."],
citations=[
 "Regulation (EU) 2016/679 (GDPR), Article 47.",
 "European Data Protection Board BCR guidance."],
sig_lens="""The Signature reading: BCRs are a house's own sworn law, approved by the realm's judges - one covenant covering all the family's internal roads. The Signature house earns the approval through rigor and keeps it through eternal vigilance.""",
demo_data={"transfers":[
 {"from":"EU","to":"US","data_class":"personal","expected":"restricted:BCRs-or-SCCs"},
 {"from":"DE","to":"FR","data_class":"personal","expected":"allowed"}]},
),
dict(
name="Transfer Impact Assessments",
group="Transfer Regimes", ladder_rank=17, ladder_tier="compounded",
description="""Transfer Impact Assessments (TIAs) answer the Schrems II question: do the destination country's laws undermine the transfer safeguards? The assessment examines the destination's surveillance and government-access laws, the data's sensitivity, the transfer's purpose and volume, and the safeguards in place - then judges whether the transfer can proceed, proceed with supplementary measures, or must not proceed. TIAs are documented per transfer or per corridor, with legal analysis of the destination regime, technical analysis of the measures (can the importer actually prevent access?), and the conclusion with its reasoning. They are living documents: destination laws change, judgments land, and assessments need review - the registry schedules TIA reviews and triggers them on legal developments. A TIA that concludes proceed-with-measures must verify the measures work; a TIA that concludes must-not-proceed must be obeyed, however inconvenient.""",
how_it_works="""TIA workflows per transfer/corridor gather: destination law analysis (surveillance, access, redress), data sensitivity and volume, safeguard description, and supplementary measures with effectiveness analysis. Legal and technical reviewers sign the conclusion: proceed, proceed-with-measures, or stop. Measures implement and verify (encryption tested, access controls audited). Review schedules plus legal-development triggers keep TIAs current. Stop conclusions escalate - the transfer redesigns (localize, anonymize) or the business case changes. TIA records persist as transfer evidence.""",
key_points=[
 "TIAs judge whether destination laws undermine transfer safeguards.",
 "Documented per transfer/corridor with legal and technical analysis.",
 "Conclusions: proceed, proceed-with-measures, or stop - stop must be obeyed.",
 "Living documents: reviewed on schedule and on legal developments.",
 "Measures must be verified effective, not just declared."],
requirements=[
 "TIA workflows with legal and technical review.",
 "Destination law analysis with surveillance and redress assessment.",
 "Measure effectiveness verification.",
 "Review schedules with legal-development triggers."],
standards=[
 "EDPB transfer guidance post-Schrems II."],
citations=[
 "CJEU. Schrems II (C-311/18). 2020.",
 "European Data Protection Board. Recommendations on supplementary measures."],
sig_lens="""The Signature reading: TIAs are the registry's honest reckoning with foreign powers - do their laws respect our oaths? The Signature reckoning is documented, reviewed, and obeyed even when the answer is no.""",
demo_data={"transfers":[
 {"from":"EU","to":"US","data_class":"personal","expected":"restricted:TIA+SCCs"},
 {"from":"EU","to":"CA","data_class":"personal","expected":"allowed:adequacy"}]},
),
dict(
name="Data Processing Agreements",
group="Transfer Regimes", ladder_rank=18, ladder_tier="compounded",
description="""Data Processing Agreements (DPAs) bind processors to controllers' instructions: the processor handles personal data only as directed, with required security, sub-processor controls, breach notification, audit rights, and end-of-contract data return or deletion. Every vendor touching personal data needs one - cloud providers, analytics tools, support platforms - and the registry tracks execution like any contract. DPAs carry the transfer dimension too: processors in other jurisdictions need the transfer mechanism (SCCs module 2/3) integrated or attached. The operational discipline is coverage: vendor onboarding cannot complete without an executed DPA, vendor reviews verify the DPA's terms are actually followed (audit rights exercised, sub-processor lists current), and vendor offboarding executes the return-or-delete clause with confirmation. A DPA nobody enforces is a hope; the registry's vendor compliance program makes it a control.""",
how_it_works="""Vendor onboarding requires executed DPAs with transfer mechanisms where needed before data flows. The DPA register tracks execution, terms, sub-processor lists, and review dates per vendor. Vendor reviews exercise audit rights and verify sub-processor currency; findings become remediation with deadlines. Offboarding executes return-or-delete with vendor confirmation. Sub-processor change notifications flow to controllers for objection. Coverage dashboards show vendors with and without executed DPAs; gaps block data flows.""",
key_points=[
 "DPAs bind processors: instructions-only, security, sub-processors, breach notice, audit, return/delete.",
 "Every vendor touching personal data needs an executed DPA before data flows.",
 "Transfer mechanisms integrate for cross-border processors.",
 "Vendor reviews exercise audit rights; offboarding executes return-or-delete.",
 "Coverage dashboards block flows to vendors without DPAs."],
requirements=[
 "DPA execution as vendor-onboarding gate.",
 "DPA register with terms, sub-processors, reviews.",
 "Vendor compliance reviews with remediation.",
 "Offboarding with confirmed return-or-delete."],
standards=[
 "GDPR Article 28."],
citations=[
 "Regulation (EU) 2016/679 (GDPR), Article 28.",
 "ISO/IEC 27701. Privacy information management. ISO."],
sig_lens="""The Signature reading: DPAs are the registry's bonds on hired hands - sworn to follow instructions, guarded in security, audited in deed, dismissed cleanly. The Signature registry lets no vendor touch personal data unbonded.""",
demo_data={"transfers":[
 {"from":"EU","to":"US","data_class":"personal","expected":"restricted:DPA+SCCs"},
 {"from":"US","to":"US","data_class":"personal","expected":"allowed:DPA"}]},
),
dict(
name="Sub-Processor Registers",
group="Transfer Regimes", ladder_rank=19, ladder_tier="compounded",
description="""Sub-processor registers list every vendor's vendors: the cloud provider's subprocessors, the analytics tool's infrastructure, the support platform's AI features - the full chain of hands touching the data. Controllers need the list to assess risk (each sub-processor is a new jurisdiction, a new breach surface), to object to risky additions, and to prove due diligence. The register per vendor records sub-processor identity, function, location, and the due-diligence evidence; change notifications flow to controllers with objection windows before new sub-processors go live. The discipline extends down the chain: contracts require vendors to impose equivalent terms on their sub-processors, and the registry verifies the flow-down on review. Undeclared sub-processors discovered by audits are incidents - the vendor hid a pair of hands. In the network's scale, sub-processor registers are themselves federated: each database publishes its chain, and the spine can trace any data's full handling chain on demand.""",
how_it_works="""Vendor contracts require sub-processor disclosure with change notification and objection rights. Registers per vendor track identity, function, location, diligence evidence, and flow-down terms. Change workflows notify controllers with objection windows; objections resolve by alternative or termination. Audits verify declared-vs-actual sub-processors via traffic and contract analysis. Flow-down verification checks equivalent terms at each tier. Federation publishes chains per database; the spine traces full handling chains on demand.""",
key_points=[
 "Registers list every vendor's vendors with function, location, diligence.",
 "Controllers assess risk, object to additions, prove due diligence.",
 "Contracts require equivalent terms flowed down each tier.",
 "Undeclared sub-processors are incidents.",
 "Federated registers let the spine trace any data's full chain."],
requirements=[
 "Sub-processor disclosure with change notification and objection.",
 "Per-vendor registers with diligence evidence.",
 "Flow-down verification on review.",
 "Declared-vs-actual audits."],
standards=[
 "GDPR Article 28(2)-(4)."],
citations=[
 "Regulation (EU) 2016/679 (GDPR), Article 28.",
 "ISO/IEC 27701. Privacy information management. ISO."],
sig_lens="""The Signature reading: sub-processor registers are the registry's chain of custody - every hand that touches the data named, vetted, and bound. The Signature chain tolerates no hidden hands.""",
demo_data={"transfers":[
 {"from":"EU","to":"US","data_class":"personal","expected":"restricted:sub-processor-listed"},
 {"from":"EU","to":"US","data_class":"public","expected":"allowed"}]},
),
dict(
name="Sovereign Clouds",
group="Transfer Regimes", ladder_rank=20, ladder_tier="compounded",
description="""Sovereign clouds are cloud environments engineered for jurisdictional compliance: data resident in-country, operated by local personnel, with government-access protections and audit rights that satisfy regulators. The models vary: the hyperscaler's in-country regions (data resident, but the provider remains foreign-jurisdiction), the operated-by-local-partner model (local company operates the cloud), and the fully disconnected national clouds. Each model answers different sovereignty demands - and none answers all: in-country regions do not fully solve provider-jurisdiction concerns, while disconnected clouds sacrifice global integration. The selection discipline matches mandate to model: residency-only needs met by regions, access-law concerns needing operational separation, the strictest mandates needing disconnection. The registry records the sovereignty properties of each cloud deployment - residency, operator jurisdiction, key custody, access logging - so workload placement decisions are evidence-based. Workload classification routes each workload to the cloud model its mandates require.""",
how_it_works="""Sovereignty requirements per workload map to cloud models: regions, partnered operation, or disconnected. Deployments record residency, operator jurisdiction, key custody, and access properties in the registry. Workload placement policies route by classification; violations block deployment. Access logging and audit rights verify the sovereignty properties continuously. Model reviews reassess as mandates evolve and providers' structures change. Cost tracking per model informs the mandate-to-model matching - the strictest model only where mandated.""",
key_points=[
 "Sovereign cloud models: in-country regions, local-partner operation, disconnected national clouds.",
 "Each answers different demands; none answers all.",
 "Match mandate to model: residency vs access-law vs strictest needs.",
 "Registry records each deployment's sovereignty properties.",
 "Workload classification routes to the required model; violations block."],
requirements=[
 "Sovereignty requirement analysis per workload.",
 "Deployment property records: residency, operator, keys, access.",
 "Placement policies with violation blocking.",
 "Continuous verification of sovereignty properties."],
standards=[
 "ISO/IEC 27018; ISO/IEC 27701."],
citations=[
 "ISO/IEC 27018. Protection of PII in public clouds. ISO.",
 "DAMA International. DAMA-DMBOK, 2nd ed. Technics Publications, 2017."],
sig_lens="""The Signature reading: sovereign clouds are fortresses built to each realm's siege laws - some with local walls, some with local garrisons, some fully separate. The Signature quartermaster places each workload in the fortress its mandate requires.""",
demo_data={"transfers":[
 {"from":"EU","to":"EU","data_class":"personal","expected":"allowed"},
 {"from":"EU","to":"US","data_class":"personal","expected":"restricted:sovereign-cloud-only"}]},
),
dict(
name="Government Access Laws: The CLOUD Act",
group="Transfer Regimes", ladder_rank=21, ladder_tier="compounded",
description="""Government access laws let states compel data from providers subject to their jurisdiction - wherever the data sits. The US CLOUD Act clarifies that US providers must produce data in their control regardless of storage location, while creating executive agreements (like the US-UK agreement) for reciprocal access with protections. The EU debates its own e-evidence framework; China's laws assert broad access. For sovereignty, the consequence is stark: data held by a provider subject to a foreign access law is reachable by that foreign government, and no residency mandate fully prevents it - residency controls where bytes sleep, not whose courts can wake them. Mitigations are layered: provider selection considering jurisdiction, encryption with customer-held keys (the provider cannot produce what it cannot read), transparency reporting on government requests, and legal challenge procedures. Transfer impact assessments must consider access laws honestly - the supplementary measures exist precisely because access laws are real. The registry records access-law exposure per provider relationship.""",
how_it_works="""Provider jurisdiction analysis maps access-law exposure per provider: which governments can compel, under what procedures, with what transparency. Mitigations deploy per exposure: customer-held-key encryption where the threat model warrants, provider diversification, transparency report monitoring. TIAs incorporate access-law analysis with supplementary measures. Government request procedures define the response: validate, narrow, challenge where lawful, notify the customer where permitted. Exposure records version with provider changes; acquisitions re-trigger analysis.""",
key_points=[
 "Access laws compel providers regardless of data location - residency does not fully prevent.",
 "CLOUD Act: US providers produce data in their control, wherever stored.",
 "Mitigations: provider selection, customer-held keys, transparency, legal challenge.",
 "TIAs must consider access laws honestly with supplementary measures.",
 "Exposure recorded per provider relationship, re-analyzed on change."],
requirements=[
 "Provider jurisdiction and access-law analysis.",
 "Mitigation deployment per exposure: keys, diversification, transparency.",
 "Government request response procedures.",
 "Exposure records with re-analysis triggers."],
standards=[
 "ISO/IEC 27018; ISO/IEC 27701."],
citations=[
 "Clarifying Lawful Overseas Use of Data Act (CLOUD Act), 2018.",
 "CJEU. Schrems II (C-311/18). 2020."],
sig_lens="""The Signature reading: access laws are the powers that can wake sleeping data across borders - acknowledged honestly, mitigated layeredly. The Signature registry maps every such power and arms each dataset accordingly.""",
demo_data={"transfers":[
 {"from":"EU","to":"US","data_class":"personal","expected":"restricted:access-law-assessed"},
 {"from":"EU","to":"EU","data_class":"personal","expected":"allowed"}]},
),
dict(
name="Data Embassy Concepts",
group="Transfer Regimes", ladder_rank=22, ladder_tier="compounded",
description="""Data embassies extend diplomatic immunity to data: Estonia's pioneering model places government data centers in allied countries under treaty protections - the host country agrees the data remains under Estonian jurisdiction, like an embassy's soil. The concept addresses the ultimate sovereignty fear: that domestic catastrophe (or occupation) destroys the state's data. For the network, the embassy pattern generalizes: critical datasets replicated to allied jurisdictions under formal agreements that fix governing law regardless of location. The agreements cover jurisdiction (whose law applies), access (who may compel), and continuity (operation during crises). Embassy arrangements are exceptional - negotiated state-to-state or enterprise-to-enterprise for the most critical data - but the pattern informs ordinary design: jurisdiction follows agreement, not just geography, and the strongest sovereignty guarantees are contractual and treaty-backed, not merely architectural.""",
how_it_works="""Embassy arrangements are established by formal agreement fixing jurisdiction, access rules, and continuity provisions for replicated critical data. Technical implementation ensures the data remains operable under the agreement's terms - separate key custody, independent operation capability. The registry records embassy datasets with their governing agreements and jurisdictional determinations. Reviews test the arrangement against scenarios: host-country legal change, diplomatic rupture, technical isolation. Ordinary systems borrow the pattern: inter-zone agreements fixing governing law for critical replications.""",
key_points=[
 "Data embassies: treaty-protected data centers abroad under home jurisdiction.",
 "Addresses ultimate sovereignty fear: domestic catastrophe destroying data.",
 "Agreements fix jurisdiction, access, and continuity regardless of location.",
 "Exceptional arrangements for the most critical data.",
 "Pattern generalizes: jurisdiction follows agreement, not just geography."],
requirements=[
 "Formal agreements with jurisdiction and access provisions.",
 "Independent operability: separate keys, autonomous operation.",
 "Scenario testing against legal and diplomatic changes.",
 "Registry records with governing agreements."],
standards=[
 "Estonian data embassy model (precedent)."],
citations=[
 "Estonian Government. Data embassy concept documentation.",
 "DAMA International. DAMA-DMBOK, 2nd ed. Technics Publications, 2017."],
sig_lens="""The Signature reading: data embassies are sovereign soil abroad - the homeland's law traveling with its most precious records under treaty seal. The Signature registry honors such treaties as the highest sovereignty art.""",
demo_data={"transfers":[
 {"from":"EE","to":"LU","data_class":"government","expected":"allowed:embassy-treaty"},
 {"from":"EE","to":"US","data_class":"government","expected":"restricted"}]},
),
dict(
name="Jurisdiction-Aware Routing",
group="Transfer Regimes", ladder_rank=23, ladder_tier="compounded",
description="""Jurisdiction-aware routing ensures data flows only along lawful paths: packets, queries, and replications steered by jurisdiction policy, not just by latency. The routing layer consults the sovereignty registry per flow: this dataset's residency class permits these regions, its transfer register allows these corridors with these mechanisms, its holds forbid these movements entirely. Enforcement is mechanical - the orchestrator refuses to schedule processing in a forbidden region, the replicator refuses the unassessed corridor, the query planner keeps EU personal data in EU execution. The subtle paths need coverage too: support engineers' remote access routes through approved jumps, ML training jobs pin to compliant compute, backup replication respects residency. Routing decisions log with the policy version applied, so any flow's lawfulness is auditable. When policies change, in-flight work is evaluated: grandfathered, rerouted, or stopped per the change's terms.""",
how_it_works="""Routing policies compile from residency classes, transfer registers, and holds into per-dataset routing rules. Orchestrators, replicators, and query planners consult the rules before placing work; violations block with the violated rule cited. Support access, training compute, and backup paths are routed equally. Decision logs record policy versions per flow. Policy changes evaluate in-flight work per grandfathering terms. Routing health dashboards show blocked attempts - attempted violations are security signals.""",
key_points=[
 "Routing steered by jurisdiction policy: residency, transfer mechanisms, holds.",
 "Enforcement mechanical: orchestrators and planners refuse unlawful placement.",
 "Covers subtle paths: support access, training compute, backups.",
 "Decisions logged with policy versions for auditability.",
 "Policy changes evaluate in-flight work per grandfathering terms."],
requirements=[
 "Compiled per-dataset routing rules from sovereignty policies.",
 "Mechanical enforcement in orchestration and planning.",
 "Full-path coverage including support and training.",
 "Decision logging with policy versions."],
standards=[
 "ISO/IEC 27701."],
citations=[
 "DAMA International. DAMA-DMBOK, 2nd ed. Technics Publications, 2017.",
 "Regulation (EU) 2016/679 (GDPR), Chapter V."],
sig_lens="""The Signature reading: jurisdiction-aware routing is the realm's road wardens - every flow checked against the law before it travels, the unlawful turned back at the gate. The Signature wardens log every passage and guard even the footpaths.""",
demo_data={"transfers":[
 {"from":"EU","to":"EU","data_class":"personal","expected":"allowed"},
 {"from":"EU","to":"US","data_class":"personal","expected":"restricted:SCCs-required"},
 {"from":"CN","to":"EU","data_class":"personal","expected":"restricted:security-assessment"}]},
),
dict(
name="Transfer Records and Logs",
group="Transfer Regimes", ladder_rank=24, ladder_tier="compounded",
description="""Transfer records prove each cross-border movement was lawful: what data, from where to where, under which mechanism, assessed when, by whom. The logging captures transfers at the infrastructure layer (replication events, API calls crossing borders) and reconciles them against the transfer register - every observed flow must have a registered mechanism, and every registered flow should show observed activity (a registered-but-never-flowing transfer is reviewed, not assumed fine). Logs retain per the strictest applicable requirement and are themselves sovereignty-aware: transfer logs containing personal data get the same protections as the data. Discrepancy handling treats unregistered observed flows as incidents and registered-but-absent flows as reviews. Regulators asking prove your transfers are lawful get the register plus the reconciled logs - the complete evidentiary chain from permission to movement.""",
how_it_works="""Transfer logging instruments replication, API gateways, and data movement tools with border-crossing events. Reconciliation jobs match observed flows to register entries continuously. Discrepancies queue as incidents (unregistered) or reviews (absent). Logs retain per requirements with sovereignty-appropriate protections. Evidence packages compile register plus reconciled logs per corridor for regulators. Log integrity is protected; tampering with transfer logs is treated as a security incident.""",
key_points=[
 "Transfer records: what, from where to where, under which mechanism, assessed when.",
 "Observed flows reconciled against the register continuously.",
 "Unregistered observed flows are incidents; registered-but-absent are reviews.",
 "Logs sovereignty-protected like the data they describe.",
 "Register plus reconciled logs form the complete evidentiary chain."],
requirements=[
 "Border-crossing event instrumentation on movement paths.",
 "Continuous observed-vs-registered reconciliation.",
 "Discrepancy workflows: incidents and reviews.",
 "Evidence package compilation per corridor."],
standards=[
 "GDPR accountability principle."],
citations=[
 "Regulation (EU) 2016/679 (GDPR), Article 5(2).",
 "European Data Protection Board transfer guidance."],
sig_lens="""The Signature reading: transfer logs are the border's own journals - every crossing recorded, every manifest checked. The Signature journals reconcile nightly, and the unmanifested crossing is pursued as smuggling.""",
demo_data={"transfers":[
 {"from":"EU","to":"UK","data_class":"personal","expected":"allowed:adequacy"},
 {"from":"EU","to":"BR","data_class":"personal","expected":"restricted:transfer-mechanism"}]},
),
]
