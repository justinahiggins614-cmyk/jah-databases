#!/usr/bin/env python3
"""Authored records for the Sensitive Data Classification databases (group F, part 1).
Public = real, fact-checked classification knowledge (PII, PHI, PCI, handling
rules). Signature = expanded Signature treatment.
Property of Justin Addam Higgins (JAH)."""

SIG_TAIL = ("Signature interpretation - original Signature-system treatment "
            "by Justin Addam Higgins; clearly labeled Signature-made, never "
            "presented as authentic public record.")

ENTRIES = [
dict(
name="What Data Classification Is",
group="Classification Basics", ladder_rank=1, ladder_tier="foundations",
description="""Data classification is the assignment of sensitivity labels to data - public, internal, confidential, restricted - based on what harm disclosure would cause and what laws apply. Classification drives everything downstream: who may access the data, how it must be encrypted, whether it can leave the country, how long it is kept, and what happens when it leaks. Without classification, protections are guesswork: the same controls guard the lunch menu and the customer database, which means the customer database is under-protected and the lunch menu is over-protected. Classification is risk-proportionate: the label reflects the impact of compromise, and the controls scale with the label. The classification registry is the system of record: the label taxonomy, the criteria per label, the classified inventory, the handling rules, and the re-classification workflows - so every dataset's protections trace to a labeled, justified decision.""",
how_it_works="""The organization defines its label taxonomy with criteria per level and examples. Data is classified at creation (by creators, assisted by automated classifiers) and recorded in the inventory with the label, classifier, confidence, and date. Handling rules attach per label: access controls, encryption, transfer restrictions, retention. Controls enforce mechanically - the restricted dataset cannot be emailed externally, the public dataset needs no approval to publish. Classification is reviewed on schedule and on trigger (data changes, incidents, new regulations). Misclassified data found by audits enters re-classification workflows.""",
key_points=[
 "Classification labels data by sensitivity: harm of disclosure plus legal duties.",
 "Labels drive access, encryption, transfer, retention, and incident response.",
 "Without classification, protections are guesswork - over and under at once.",
 "Controls scale with labels and enforce mechanically.",
 "Every dataset's protections trace to a labeled, justified decision."],
requirements=[
 "A label taxonomy with criteria and examples per level.",
 "Classification at creation with inventory recording.",
 "Per-label handling rules enforced mechanically.",
 "Scheduled and triggered re-classification."],
standards=[
 "ISO/IEC 27001 Annex A.8 (information classification).",
 "NIST SP 800-60 (information type classification)."],
citations=[
 "ISO/IEC 27001. Information security management. ISO.",
 "NIST SP 800-60 Vol. 2. Guide for Mapping Types of Information to Security Categories."],
sig_lens="""The Signature reading: classification is the registry grading every secret by its worth - the labels sworn, the protections fitted, the decisions recorded. The Signature registry guards the crown jewels and leaves the lunch menu unguarded, each by deliberate judgment.""",
demo_data={"fields":[
 {"name":"email","patterns":["@"],"expected":"confidential"},
 {"name":"press_release","patterns":[],"expected":"public"},
 {"name":"salary","patterns":["salary"],"expected":"restricted"}]},
),
dict(
name="Why Classify: Risk, Compliance, Cost",
group="Classification Basics", ladder_rank=2, ladder_tier="foundations",
description="""Classification pays for itself three ways. Risk: labeled data gets proportionate protection - the breach that exposes properly classified restricted data triggers the full incident response, while the public data leak is a non-event; without labels, every leak is a maximum-alarm fire drill. Compliance: regulations demand classification - GDPR's special categories, HIPAA's PHI, PCI's cardholder data each require knowing where the regulated data lives; you cannot protect what you cannot find. Cost: classification focuses spending - encryption, DLP, and audit effort go to the data that needs them instead of being spread thin or piled on everything. The business case writes itself: one prevented misdirected-email incident on properly labeled data pays for the classification program. Organizations that resist classification discover its absence at the worst moment: the breach where nobody can say what was exposed, to whom, or what law applies.""",
how_it_works="""The program builds its case on the three returns: risk scenarios quantified (breach cost by label), compliance mappings (which labels satisfy which regulations), and cost models (protection spend per label vs flat). Classification coverage becomes a KPI: what share of the estate is labeled, by tier. Incident post-mortems credit or blame classification - did labels speed the response? Compliance audits sample labels against regulatory mappings. The program reports its value in prevented incidents and focused spend, reviewed annually with leadership.""",
key_points=[
 "Risk: labels make incident response proportionate - no more maximum-alarm for lunch menus.",
 "Compliance: regulations require knowing where regulated data lives.",
 "Cost: protection spending focuses on data that needs it.",
 "Coverage is a KPI: share of estate labeled, by tier.",
 "Value proven in prevented incidents and focused spend."],
requirements=[
 "Risk, compliance, and cost models justifying the program.",
 "Classification coverage KPIs by tier.",
 "Incident credit/blame analysis for classification.",
 "Annual value reporting to leadership."],
standards=[
 "ISO/IEC 27001.",
 "NIST SP 800-60."],
citations=[
 "ISO/IEC 27001. Information security management. ISO.",
 "NIST SP 800-60 Vol. 2. Guide for Mapping Types of Information to Security Categories."],
sig_lens="""The Signature reading: classification's worth is proven threefold - in disasters averted, laws satisfied, and coin well spent. The Signature registry counts its value honestly and reports it yearly.""",
demo_data={"fields":[
 {"name":"lunch_menu","patterns":[],"expected":"public"},
 {"name":"customer_db","patterns":["@"],"expected":"confidential"}]},
),
dict(
name="Public Data",
group="Data Categories", ladder_rank=3, ladder_tier="foundations",
description="""Public data is information cleared for anyone: press releases, published prices, marketing materials, open datasets. The public label means no confidentiality protection needed - but public data still needs integrity protection (nobody may alter the published price list) and availability protection (the website must stay up). The classification discipline for public data is the clearance decision: who may mark data public, and what review does it need? Premature publication - the unreleased earnings, the draft announcement - is the classic public-data incident, prevented by publication workflows with approvals. Public data also carries licensing: public does not mean public domain - the press release may be copyrighted, the open dataset may require attribution. The registry marks public data with its license terms, so reusers know their rights. And public data can become sensitive in aggregate: individually public facts combined can reveal confidential patterns - the aggregation risk that classification reviews watch for.""",
how_it_works="""Publication workflows route public-bound data through clearance: content review, approval by authorized publishers, license assignment. Published data gets integrity protections (signed, versioned, tamper-evident) and availability SLAs. Licenses attach as metadata: copyright, open licenses with terms, attribution requirements. Aggregation reviews assess whether combined public datasets reveal sensitive patterns; risky combinations get restricted. Publication logs record what went public when, by whose authority - the evidence for premature-publication investigations.""",
key_points=[
 "Public: no confidentiality needed, but integrity and availability still required.",
 "Clearance workflows with authorized publishers prevent premature publication.",
 "Public is not public domain: licenses and attribution attach.",
 "Aggregation risk: public facts combined can reveal confidential patterns.",
 "Publication logs record what, when, by whose authority."],
requirements=[
 "Publication clearance workflows with authorized publishers.",
 "Integrity protections on published data.",
 "License metadata on public datasets.",
 "Aggregation risk reviews."],
standards=[
 "ISO/IEC 27001."],
citations=[
 "ISO/IEC 27001. Information security management. ISO.",
 "NIST SP 800-60 Vol. 2."],
sig_lens="""The Signature reading: public data is the registry's open square - free to all, guarded in integrity, its proclamations authorized. The Signature square watches for the mosaic: innocent stones that together draw a secret picture.""",
demo_data={"fields":[
 {"name":"homepage_text","patterns":[],"expected":"public"},
 {"name":"price_list","patterns":[],"expected":"public"}]},
),
dict(
name="Internal Data",
group="Data Categories", ladder_rank=4, ladder_tier="foundations",
description="""Internal data is the organization's working information: not secret, but not for outsiders - memos, internal wikis, project plans, employee directories. The internal label means: share freely inside, protect from outside. The controls are boundary controls: authentication for access, no public links, no external sharing without approval. The common failures are boundary leaks: the internal wiki indexed by search engines, the all-hands recording shared externally, the employee directory scraped. Internal is the default label for unclassified business data in many organizations - a sensible default that errs toward protection while classification catches up. But internal is not a dumping ground: data that is actually confidential must not hide in internal, and internal data with regulatory duties (employee personal data) needs its specific protections layered on. Reviews promote data out of internal in both directions as its true sensitivity becomes clear.""",
how_it_works="""Boundary controls enforce the internal label: authenticated access, no anonymous links, external sharing workflows with approval. Discovery scans find internal data exposed publicly (search-indexed wikis, open buckets) for remediation. Default-labeling policies assign internal to unclassified business data at creation. Reviews reclassify: confidential data promoted out, truly public data cleared for publication. Employee personal data within internal gets its regulatory protections layered per the privacy program.""",
key_points=[
 "Internal: share freely inside, protect from outside - boundary controls.",
 "Common failures: search-indexed wikis, open buckets, external shares.",
 "Sensible default for unclassified business data - errs toward protection.",
 "Not a dumping ground: confidential data must not hide here.",
 "Reviews promote data out as true sensitivity clarifies."],
requirements=[
 "Boundary controls: authentication, no public links, approved external sharing.",
 "Exposure scanning for internal data gone public.",
 "Default-labeling policies for unclassified data.",
 "Review workflows promoting misclassified data."],
standards=[
 "ISO/IEC 27001."],
citations=[
 "ISO/IEC 27001. Information security management. ISO.",
 "NIST SP 800-60 Vol. 2."],
sig_lens="""The Signature reading: internal data is the registry's household - open to the family, closed to strangers, the doors checked nightly. The Signature household sweeps for open windows and sorts its members' true stations in review.""",
demo_data={"fields":[
 {"name":"team_wiki","patterns":[],"expected":"internal"},
 {"name":"project_plan","patterns":[],"expected":"internal"}]},
),
dict(
name="Confidential Data",
group="Data Categories", ladder_rank=5, ladder_tier="foundations",
description="""Confidential data would cause real harm if disclosed: customer personal data, employee records, unreleased products, financials, contracts, security architectures. The confidential label triggers the full protection suite: need-to-know access (not just authenticated, but authorized per role), encryption at rest and in transit, no external transmission without approval and protection, watermarking or DLP on exfiltration paths, and breach notification duties if exposed. The classification criteria center on harm: would disclosure cause financial loss, legal liability, competitive damage, or personal harm? Confidential is typically the largest sensitive category - most of what the privacy and security programs protect lives here. The discipline that matters most is need-to-know enforcement: confidential data accessible to everyone with a login is confidential in name only. Access reviews prune the accumulated permissions quarterly, because access only grows.""",
how_it_works="""Need-to-know access control lists per dataset with role-based grants; encryption enforced at rest and in transit; DLP monitors exfiltration paths; external sharing requires approval with protection verification. Breach playbooks for confidential exposure run notification and containment. Access reviews quarterly prune stale grants. Data inventories map confidential holdings per system for audit. Handling training teaches staff the confidential rules; violations feed the incident process.""",
key_points=[
 "Confidential: disclosure causes financial, legal, competitive, or personal harm.",
 "Full suite: need-to-know access, encryption, DLP, approved external sharing.",
 "Need-to-know is the critical discipline - login-wide access is nominal only.",
 "Access reviews prune accumulated permissions quarterly.",
 "Breach playbooks with notification duties attach to the label."],
requirements=[
 "Need-to-know ACLs with role-based grants.",
 "Encryption at rest and in transit enforced.",
 "DLP on exfiltration paths.",
 "Quarterly access reviews."],
standards=[
 "ISO/IEC 27001 Annex A.8.",
 "NIST SP 800-53 (access control family)."],
citations=[
 "ISO/IEC 27001. Information security management. ISO.",
 "NIST SP 800-53 Rev. 5. Security and Privacy Controls."],
sig_lens="""The Signature reading: confidential data is the registry's sealed archive - opened only to the needful, encrypted in rest and travel, its thieves pursued by playbook. The Signature archive prunes its key-holders quarterly.""",
demo_data={"fields":[
 {"name":"customer_email","patterns":["@"],"expected":"confidential"},
 {"name":"contract_pdf","patterns":["contract"],"expected":"confidential"}]},
),
dict(
name="Restricted and Regulated Data",
group="Data Categories", ladder_rank=6, ladder_tier="foundations",
description="""Restricted is the highest sensitivity tier: data whose disclosure would cause severe harm or violate the law - authentication credentials, encryption keys, special-category personal data at scale, trade secrets, classified government data. Regulated data overlaps: categories the law singles out for mandatory protections - PHI under HIPAA, cardholder data under PCI DSS, special-category data under GDPR. The restricted label triggers maximum controls: strict need-to-know with multi-party approval for access, hardware-backed key storage, network segmentation, continuous monitoring, and pre-approved handling procedures for every use. Regulated labels add their regime's specific duties: PCI's network and logging requirements, HIPAA's minimum-necessary and audit controls, GDPR's special-category conditions. The registry distinguishes the tiers mechanically: restricted data cannot flow through channels cleared only for confidential, and regulated data carries its regime tags so the right duties attach automatically.""",
how_it_works="""Maximum controls per dataset: multi-party access approval, hardware key storage, segmentation, continuous monitoring. Regime tags attach regulatory duty packs automatically: PCI DSS controls for cardholder data, HIPAA safeguards for PHI, GDPR conditions for special categories. Channel clearance enforcement blocks restricted data on confidential-cleared paths. Handling procedures are pre-approved per use; deviations need security review. Compliance audits verify the controls per regime; findings remediate on regulatory timelines.""",
key_points=[
 "Restricted: severe harm or legal violation on disclosure - maximum controls.",
 "Regulated: law-mandated protections (PHI, cardholder data, special categories).",
 "Multi-party approval, hardware keys, segmentation, continuous monitoring.",
 "Regime tags attach duty packs automatically.",
 "Channel clearance enforced mechanically by label tier."],
requirements=[
 "Maximum-control baselines for restricted data.",
 "Regime tagging with automatic duty-pack attachment.",
 "Channel clearance enforcement by tier.",
 "Pre-approved handling procedures per use."],
standards=[
 "ISO/IEC 27001; PCI DSS; HIPAA Security Rule."],
citations=[
 "PCI Security Standards Council. PCI DSS v4.0.",
 "45 CFR Part 164 (HIPAA Security Rule)."],
sig_lens="""The Signature reading: restricted data is the registry's inner sanctum - entered by few, with many keys, watched always. The Signature sanctum's laws are the strictest, its duties automatic, its channels guarded by tier.""",
demo_data={"fields":[
 {"name":"ssn","patterns":["ssn"],"expected":"restricted"},
 {"name":"card_number","patterns":["card"],"expected":"restricted"}]},
),
dict(
name="Personal Data (PII)",
group="Data Categories", ladder_rank=7, ladder_tier="foundations",
description="""Personal data is information relating to an identified or identifiable individual: names, emails, phone numbers, addresses, device IDs, IP addresses, and - in combination - the quasi-identifiers that single someone out. The identifiability test is practical: can this data, alone or combined with reasonably available other data, pick out a person? If yes, it is personal. Personal data triggers the privacy program's full machinery: lawful basis, purpose limitation, minimization, rights handling (access, erasure, portability), breach notification, and transfer rules. The classification challenge is the long tail: personal data hides in logs, free-text fields, file names, and backups - the PII discovery program hunts it continuously. Pseudonymized data (identifiers replaced with tokens) remains personal data under GDPR - only truly anonymous data, irreversibly de-identified, escapes. The registry tags personal data with its categories and lawful bases, so every protection and right attaches correctly.""",
how_it_works="""PII discovery scans structured fields, free text (pattern matching plus ML), logs, and file stores continuously. Findings classify into personal data with categories (contact, identifier, behavioral) and lawful bases. Privacy machinery attaches: rights workflows, breach duties, transfer rules, minimization reviews. Pseudonymization is applied where analytics needs patterns without identities - with the mapping secured as personal data itself. Anonymization, where truly irreversible, reclassifies out of personal data with the method documented and re-identification risk assessed. Inventories map personal data per system for RoPA and audits.""",
key_points=[
 "Personal data: relates to an identifiable individual, alone or in combination.",
 "Triggers privacy machinery: lawful basis, rights, breach duties, transfer rules.",
 "Hides in logs, free text, file names - discovery hunts continuously.",
 "Pseudonymized stays personal; only truly anonymous escapes.",
 "Tagged with categories and lawful bases for correct protections."],
requirements=[
 "Continuous PII discovery across structured, text, logs, files.",
 "Category and lawful-basis tagging.",
 "Rights workflows and breach duties attached.",
 "Anonymization with documented irreversibility assessment."],
standards=[
 "GDPR; ISO/IEC 27701; NIST SP 800-122 (PII)."],
citations=[
 "Regulation (EU) 2016/679 (GDPR), Article 4(1).",
 "NIST SP 800-122. Guide to Protecting PII."],
sig_lens="""The Signature reading: personal data is the registry's charge of souls - each individual's traces known, guarded, and answerable to their rights. The Signature registry hunts the hidden traces and honors every soul's commands.""",
demo_data={"fields":[
 {"name":"phone","patterns":["phone"],"expected":"confidential"},
 {"name":"ip_address","patterns":["ip"],"expected":"confidential"}]},
),
dict(
name="Special-Category Personal Data",
group="Data Categories", ladder_rank=8, ladder_tier="foundations",
description="""Special-category data is personal data the law treats as extra sensitive: racial or ethnic origin, political opinions, religious beliefs, trade union membership, health data, sex life or orientation, genetic and biometric data (GDPR Article 9). Processing is generally prohibited except under narrow conditions: explicit consent, employment law obligations, vital interests, or substantial public interest with safeguards. The classification bar is higher and the handling stricter: separate consent records, enhanced access controls, prohibition on repurposing, and data protection impact assessments before processing. Health, genetic, and biometric data get their own regimes too (HIPAA, genetic privacy laws, biometric laws like Illinois BIPA). The discovery challenge is acute: special-category data hides in plain sight - the prayer-time app logs reveal religion, the pharmacy purchases reveal health. Classification programs treat any plausible special-category inference as special-category until proven otherwise.""",
how_it_works="""Discovery flags potential special-category data with conservative inference rules. Processing requires a documented Article 9 condition plus DPIA; separate explicit consent records where consent is the basis. Enhanced controls: strict need-to-know, purpose binding with no repurposing, audit of every access. Biometric and genetic data get regime-specific handling (BIPA consent, HIPAA safeguards). Inference risks assessed: does this dataset allow special-category inferences? If yes, it is treated as special-category. Reviews verify conditions remain met; expired consents trigger deletion or re-consent.""",
key_points=[
 "Special categories: race, politics, religion, union, health, sex life, genetic, biometric.",
 "Processing generally prohibited except narrow conditions (explicit consent etc.).",
 "Separate consent records, DPIAs, no repurposing, enhanced access controls.",
 "Inference risk: datasets allowing special-category inferences are treated as such.",
 "Regime-specific handling for biometric, genetic, health data."],
requirements=[
 "Conservative discovery with inference-risk assessment.",
 "Documented Article 9 conditions with DPIAs.",
 "Separate explicit consent records.",
 "Enhanced controls with access auditing."],
standards=[
 "GDPR Article 9; Illinois BIPA; HIPAA."],
citations=[
 "Regulation (EU) 2016/679 (GDPR), Article 9.",
 "Illinois Biometric Information Privacy Act (740 ILCS 14)."],
sig_lens="""The Signature reading: special-category data is the registry's most sacred charge - the intimate truths, guarded by the highest law. The Signature registry demands explicit leave, forbids repurposing, and treats inference as possession.""",
demo_data={"fields":[
 {"name":"health_diagnosis","patterns":["diagnosis"],"expected":"restricted"},
 {"name":"biometric_template","patterns":["biometric"],"expected":"restricted"}]},
),
dict(
name="Proprietary Data",
group="Data Categories", ladder_rank=9, ladder_tier="foundations",
description="""Proprietary data is the organization's competitive lifeblood: product designs, source code, algorithms, pricing strategies, customer lists, merger plans, manufacturing processes. Its value is exclusivity - disclosure destroys the advantage - so protection centers on need-to-know, compartmentalization (project code names, clean teams for M&A), and exit controls (what departing employees may not take). Unlike regulated data, the duties are set by the business, not the law - but the law helps: trade secret statutes protect properly guarded secrets, and employment agreements bind the humans. Classification criteria ask: would a competitor pay for this? Would disclosure erase margin or advantage? Proprietary data at the highest sensitivity gets the restricted label with trade-secret handling: documented reasonable measures (access controls, markings, agreements) that the law requires for protection. The registry tracks proprietary holdings with their business value assessments, because protection spending should follow value.""",
how_it_works="""Business value assessments classify proprietary data by competitive impact. Compartmentalization isolates the most sensitive (code names, clean teams, need-to-know enclaves). Reasonable measures document for trade-secret protection: markings, access controls, agreements. Exit procedures cover departing employees: access revocation, return of materials, reminder of obligations. Value-based protection spending aligns controls with assessed worth. Misappropriation response playbooks cover investigation, legal action, and containment.""",
key_points=[
 "Proprietary data's value is exclusivity - disclosure destroys advantage.",
 "Protection: need-to-know, compartmentalization, exit controls.",
 "Trade secret law protects properly guarded secrets - document reasonable measures.",
 "Classification by competitive impact: would a competitor pay for this?",
 "Protection spending follows assessed business value."],
requirements=[
 "Business value assessments per proprietary holding.",
 "Compartmentalization for the most sensitive.",
 "Documented reasonable measures for trade-secret protection.",
 "Exit procedures with obligation reminders."],
standards=[
 "Defend Trade Secrets Act (US); EU Trade Secrets Directive."],
citations=[
 "Defend Trade Secrets Act of 2016 (US).",
 "Directive (EU) 2016/943 on trade secrets."],
sig_lens="""The Signature reading: proprietary data is the registry's armory of advantage - compartmented, marked, its guardians bound by oath. The Signature armory documents its locks, for the law protects only the guarded secret.""",
demo_data={"fields":[
 {"name":"pricing_strategy","patterns":["pricing"],"expected":"confidential"},
 {"name":"source_code","patterns":["source"],"expected":"confidential"}]},
),
dict(
name="Trade Secrets",
group="Data Categories", ladder_rank=10, ladder_tier="foundations",
description="""Trade secrets are proprietary information with legal armor: formulas, processes, and compilations that derive value from secrecy and are subject to reasonable secrecy measures. The legal test (US DTSA, EU Directive) has three prongs: the information is secret (not generally known), derives independent economic value from secrecy, and is subject to reasonable measures to keep it secret. Fail any prong and the armor falls - the famous recipe published in an interview is no longer a secret no matter how valuable. The classification program's role is maintaining the prongs: secrecy through access controls and need-to-know, value through business assessment, reasonable measures through documented controls, markings, and agreements. Trade secret registers record each secret with its prong evidence - the documentation that wins misappropriation cases. Disclosure incidents get immediate legal involvement: the clock on remedies starts fast, and public disclosure can kill the secret permanently.""",
how_it_works="""Trade secret registers record each secret with secrecy, value, and measures evidence. Reasonable measures implement: markings (confidential/trade secret), access controls, need-to-know, employee and vendor agreements, exit procedures. Prong reviews verify all three hold on schedule; weakened prongs trigger remediation. Disclosure incidents engage legal immediately with containment and remedy assessment. Litigation readiness maintains the evidence package: the register, the measures documentation, the value assessment.""",
key_points=[
 "Trade secret test: secret, valuable-from-secrecy, reasonable measures - all three.",
 "Fail any prong and the legal armor falls.",
 "Registers record prong evidence per secret.",
 "Reasonable measures: markings, controls, agreements, exits - documented.",
 "Disclosure incidents need immediate legal involvement."],
requirements=[
 "Trade secret registers with prong evidence.",
 "Documented reasonable measures.",
 "Scheduled prong reviews with remediation.",
 "Disclosure incident playbooks with legal engagement."],
standards=[
 "Defend Trade Secrets Act; EU Directive 2016/943."],
citations=[
 "Defend Trade Secrets Act of 2016 (US).",
 "Directive (EU) 2016/943 on trade secrets."],
sig_lens="""The Signature reading: trade secrets are the registry's crown formulas - secret, precious, and guarded by documented rite. The Signature registry maintains all three prongs, for armor with a chink is no armor.""",
demo_data={"fields":[
 {"name":"secret_formula","patterns":["secret"],"expected":"restricted"},
 {"name":"process_patent_pending","patterns":["secret"],"expected":"restricted"}]},
),
dict(
name="Health Data (PHI)",
group="Data Categories", ladder_rank=11, ladder_tier="foundations",
description="""Protected health information (PHI) is individually identifiable health data held by covered entities and business associates: diagnoses, treatments, test results, prescriptions, plus the identifiers that link them to people. HIPAA's Privacy Rule limits uses and disclosures to the minimum necessary; the Security Rule requires administrative, physical, and technical safeguards; the Breach Notification Rule mandates notifications. De-identification under HIPAA follows two paths: expert determination (statistical certification of very small re-identification risk) or safe harbor (removal of 18 identifier types with no residual knowledge). The classification challenge: health data hides outside healthcare - the wellness app, the sick-day records, the pharmacy loyalty data - and where HIPAA does not apply, other laws (state health privacy, GDPR health provisions) often do. PHI gets the restricted label with the HIPAA duty pack: minimum necessary, audit controls, encryption, BAAs for every vendor touch.""",
how_it_works="""PHI discovery covers clinical systems plus the hiding places: wellness apps, HR sick records, loyalty data. HIPAA duty packs attach: minimum-necessary access, audit controls, encryption, breach procedures. BAAs execute with every vendor touching PHI. De-identification follows expert determination or safe harbor with documentation; re-identification risk assessed for the safe harbor's residual knowledge. Minimum-necessary reviews prune access regularly. Breach risk assessments run per incident with the four-factor test.""",
key_points=[
 "PHI: identifiable health data with HIPAA's privacy, security, breach duties.",
 "Minimum necessary: access limited to what each role needs.",
 "De-identification via expert determination or safe harbor (18 identifiers).",
 "Health data hides outside healthcare - discover the wellness apps and sick records.",
 "BAAs for every vendor touch; breach notification per the four-factor test."],
requirements=[
 "PHI discovery including non-clinical hiding places.",
 "HIPAA duty packs: minimum necessary, audit, encryption.",
 "BAAs with all vendors.",
 "De-identification with documented method and risk assessment."],
standards=[
 "HIPAA Privacy, Security, Breach Notification Rules."],
citations=[
 "45 CFR Part 160, 164 (HIPAA).",
 "HHS guidance on de-identification."],
sig_lens="""The Signature reading: health data is the registry's most tender charge - the body's secrets, guarded by law's strictest care. The Signature registry grants only the minimum necessary and hunts the hidden stashes.""",
demo_data={"fields":[
 {"name":"diagnosis_code","patterns":["diagnosis"],"expected":"restricted"},
 {"name":"prescription","patterns":["prescription"],"expected":"restricted"}]},
),
dict(
name="Financial Data (PCI)",
group="Data Categories", ladder_rank=12, ladder_tier="foundations",
description="""Cardholder data under PCI DSS is the payment industry's regulated crown jewels: primary account numbers (PANs), cardholder names, expiration dates, service codes - with sensitive authentication data (full track data, CAV2/CVC, PINs) forbidden from storage entirely. PCI DSS v4.0 requires: network security controls, secure configurations, strong access control, encryption of PANs at rest and in transit, logging and monitoring, vulnerability management, and regular testing. The classification imperative is scope reduction: the fewer systems touching cardholder data, the smaller the compliance burden - tokenization and point-to-point encryption shrink scope dramatically. Discovery hunts PANs in the wrong places: logs, emails, recordings, spreadsheets - each a scope-expanding incident. PANs get the restricted label with the PCI duty pack; sensitive authentication data gets the never-store rule enforced by DLP and code review. PCI compliance is assessed yearly (by QSA or self-assessment by merchant level) with continuous control operation between.""",
how_it_works="""PAN discovery scans structured data, logs, recordings, and files continuously; findings trigger scope review and remediation. Tokenization replaces PANs with tokens wherever the PAN is not needed; P2PE encrypts at capture. The PCI duty pack enforces: encryption, access control, logging, vulnerability management, testing. Scope is minimized architecturally: cardholder data environments segmented from the rest. Assessments run yearly with continuous control monitoring; non-compliance findings remediate on PCI timelines. Sensitive authentication data is blocked from storage by DLP and pre-commit hooks.""",
key_points=[
 "Cardholder data: PANs, names, expirations - with SAD (track data, CVC, PINs) never stored.",
 "PCI DSS v4.0: network, config, access, encryption, logging, vuln management, testing.",
 "Scope reduction via tokenization and P2PE shrinks the compliance burden.",
 "Discovery hunts PANs in logs, emails, recordings - each a scope incident.",
 "Yearly assessment with continuous control operation."],
requirements=[
 "Continuous PAN discovery with scope review.",
 "Tokenization and P2PE for scope reduction.",
 "PCI duty packs with continuous monitoring.",
 "SAD storage blocking via DLP and code review."],
standards=[
 "PCI DSS v4.0."],
citations=[
 "PCI Security Standards Council. PCI DSS v4.0.",
 "PCI SSC guidance on tokenization."],
sig_lens="""The Signature reading: cardholder data is the registry's minted coin - guarded by the industry's strictest vault rules, its scope shrunk by tokenization. The Signature vault never stores what the law forbids and hunts stray coins relentlessly.""",
demo_data={"fields":[
 {"name":"pan","patterns":["card"],"expected":"restricted"},
 {"name":"cvc","patterns":["card"],"expected":"restricted"}]},
),
]
