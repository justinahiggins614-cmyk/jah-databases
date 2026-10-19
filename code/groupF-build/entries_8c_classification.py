#!/usr/bin/env python3
"""Sensitive Data Classification entries 25-34 (advanced)."""

APPEND = [
dict(
name="Declassification",
group="Advanced Classification", ladder_rank=25, ladder_tier="advanced",
description="""Declassification lowers labels when sensitivity fades: the merger closes and the plan becomes history, the product launches and the design becomes public, the retention period ends and the records lose their business value. The declassification workflow verifies the fade is real: the triggering event occurred (launch happened, period elapsed), no residual sensitivity remains (the launched product's design still contains next-generation secrets - partial declassification), and no legal duty persists (the litigation hold still covers these records). Partial declassification handles the mixed case: downgrade the bulk, keep the sensitive excerpts restricted. Declassification is approved, never automatic - the reviewer confirms the fade with evidence - because premature declassification is irreversible disclosure. The declassified data's history retains its original labels in the audit trail; the downgrade itself is a labeled event. Scheduled declassification reviews (the 5-year embargo list, the launch calendar) keep the process proactive rather than archaeological.""",
how_it_works="""Declassification triggers (events, elapsed periods, scheduled reviews) queue candidates with fade evidence. Reviewers verify: event occurred, no residual sensitivity, no legal duties persist. Partial declassification splits mixed content, downgrading the bulk and retaining excerpts. Approvals record with evidence; downgrades execute with protection updates. Audit trails preserve original labels historically. Scheduled reviews process embargo lists and launch calendars proactively.""",
key_points=[
 "Declassification lowers labels when sensitivity genuinely fades.",
 "Verified: triggering event, no residual sensitivity, no legal duties.",
 "Partial declassification splits mixed content.",
 "Approved, never automatic - premature declassification is irreversible.",
 "Scheduled reviews keep the process proactive."],
requirements=[
 "Declassification workflows with fade verification.",
 "Partial declassification with content splitting.",
 "Approval with evidence records.",
 "Scheduled embargo and launch-calendar reviews."],
standards=[
 "ISO/IEC 27001."],
citations=[
 "ISO/IEC 27001. Information security management. ISO.",
 "NIST SP 800-60 Vol. 2."],
sig_lens="""The Signature reading: declassification is the registry's honorable discharge - granted when service ends, verified genuine, never rushed. The Signature discharge keeps the service record and never frees a secret still at war.""",
demo_data={"fields":[
 {"name":"declass_old_plan","patterns":["secret"],"expected":"restricted"},
 {"name":"declass_launched","patterns":[],"expected":"public"}]},
),
dict(
name="Classification Disputes",
group="Advanced Classification", ladder_rank=26, ladder_tier="advanced",
description="""Classification disputes arise when classifiers disagree: the automated model says confidential, the data owner says internal; security says restricted, the business says the protections block the work. The dispute process gives both sides a hearing: the challenger states the case with evidence (the data's actual content and harm analysis), the classifier defends (criteria citation, pattern evidence), and the classification board rules with published reasoning. Disputes are triaged by risk: challenges seeking downgrade get full review (the risk is under-protection), challenges seeking upgrade get fast-tracked (the risk was already conservative). The board's rulings become case law, cited in future classifications. Dispute metrics reveal systemic issues: many disputes on one criteria section means the criteria need rewriting; many overturns of one classifier means the classifier needs retraining. The process protects dissent: challenging a label is always allowed, never punished - the organization that punishes challenges gets silent misclassification instead.""",
how_it_works="""Dispute intake captures the challenged label, the proposed label, evidence, and harm analysis. Triage routes by direction: downgrade challenges to full review, upgrade challenges fast-tracked. Board hearings (async or convened) rule with published reasoning entering case law. Metrics track dispute volumes, overturn rates, and systemic patterns feeding criteria and classifier improvements. Challenge rights are communicated; retaliation for challenges is a conduct violation.""",
key_points=[
 "Disputes get hearings: challenger evidence vs classifier defense, board ruling.",
 "Downgrade challenges fully reviewed; upgrade challenges fast-tracked.",
 "Rulings publish as case law for future classifications.",
 "Dispute metrics reveal criteria and classifier problems.",
 "Challenging labels is protected; punished dissent breeds silent misclassification."],
requirements=[
 "Dispute intake with evidence and harm analysis.",
 "Risk-triaged review routing.",
 "Board rulings published as case law.",
 "Dispute metrics feeding criteria improvements."],
standards=[
 "ISO/IEC 27001."],
citations=[
 "ISO/IEC 27001. Information security management. ISO.",
 "DAMA International. DAMA-DMBOK, 2nd ed. Technics Publications, 2017."],
sig_lens="""The Signature reading: disputes are the registry's court of grading - both sides heard, rulings reasoned and published. The Signature court protects the challenger, for the silenced challenger hides the misgraded.""",
demo_data={"fields":[
 {"name":"dispute_secret","patterns":["secret"],"expected":"restricted"},
 {"name":"dispute_open","patterns":[],"expected":"public"}]},
),
dict(
name="Classification for a Million-Database Network",
group="Advanced Classification", ladder_rank=27, ladder_tier="advanced",
description="""A million databases need classification that scales by federation: a global label taxonomy with consistent meanings (restricted means restricted everywhere), local classification execution per database, and a network spine aggregating the sensitive-data picture. The global taxonomy defines the levels, criteria, and handling baselines; databases may add sub-levels for local needs but cannot redefine the globals. Each database classifies its holdings and publishes label summaries (counts per label per data kind, not the data) to the spine. Cross-database flows check labels at both ends: restricted data leaving a database needs the receiving database's protections verified. The spine's sensitive-data map shows where the network's secrets live in aggregate - guiding audit focus, incident response, and investment. Standard classifier profiles per data kind keep judgments consistent: every customer database runs the same PII discovery. Local judgment stays local: the database's stewards rule on its borderline cases under the global criteria.""",
how_it_works="""The global taxonomy publishes with criteria and handling baselines; databases extend with sub-levels. Local classification runs per database with standard profiles per data kind; summaries publish to the spine. Cross-database transfers verify label compatibility mechanically. The spine aggregates the sensitive-data map with drill-down; audits sample per database. Borderline rulings stay local under global criteria with case law shared network-wide.""",
key_points=[
 "Global taxonomy with consistent meanings; local sub-levels allowed, redefinition forbidden.",
 "Local execution per database; label summaries (not data) to the spine.",
 "Cross-database flows verify label compatibility at both ends.",
 "Spine's sensitive-data map guides audit, response, investment.",
 "Standard classifier profiles per data kind; local stewards rule borderlines."],
requirements=[
 "Global taxonomy with criteria and handling baselines.",
 "Local classification with summary publication.",
 "Label-compatibility checks on cross-database flows.",
 "Network sensitive-data map with drill-down."],
standards=[
 "ISO/IEC 27001."],
citations=[
 "ISO/IEC 27001. Information security management. ISO.",
 "NIST SP 800-60 Vol. 2."],
sig_lens="""The Signature reading: network classification is a million archives under one heraldry - the ranks meaning the same everywhere, each archive grading its own, the spine mapping where the secrets sleep. The Signature heraldry is universal; its application, local.""",
demo_data={"fields":[
 {"name":"net_secret","patterns":["secret"],"expected":"restricted"},
 {"name":"net_guide","patterns":[],"expected":"public"}]},
),
dict(
name="Classification Metrics",
group="Advanced Classification", ladder_rank=28, ladder_tier="advanced",
description="""Classification metrics prove the program works: coverage (share of estate labeled, by tier), accuracy (sampled labels correct per audits), automation rate (share labeled by machines vs humans), dispute rates (challenges per thousand labels), re-classification velocity (criteria updates applied estate-wide within SLA), and protection alignment (sensitive labels with matching controls deployed). Metrics report per database and aggregated network-wide, with targets from policy (100 percent coverage of tier-1 data) and trends triggering action (coverage sliding as new data outpaces classification). The metrics that move executives are risk-oriented: unlabeled sensitive data found by audits (the exposure), over-classified data blocking work (the friction), and incident response time by label (the payoff). Every metric has an owner; the classification council reviews quarterly and funds the gaps.""",
how_it_works="""Metric jobs aggregate from inventories, audits, dispute logs, and control deployments into coverage, accuracy, automation, dispute, velocity, and alignment measures. Dashboards per database and network-wide with targets and trends. Owners respond per playbooks; the council reviews quarterly with funding decisions. Risk-oriented executive views show exposure, friction, and payoff. Metric definitions version with the taxonomy.""",
key_points=[
 "Metrics: coverage, accuracy, automation rate, dispute rates, re-classification velocity, protection alignment.",
 "Per-database and network-wide with targets and trends.",
 "Risk-oriented executive views: exposure, friction, payoff.",
 "Targets from policy; trends trigger action before failure.",
 "Council reviews quarterly with funding authority."],
requirements=[
 "Metric definitions across classification dimensions.",
 "Per-database and network dashboards.",
 "Owner assignment with response playbooks.",
 "Quarterly council reviews with funding."],
standards=[
 "ISO/IEC 27001."],
citations=[
 "ISO/IEC 27001. Information security management. ISO.",
 "DAMA International. DAMA-DMBOK, 2nd ed. Technics Publications, 2017."],
sig_lens="""The Signature reading: classification metrics are the registry's inspection of its own grading - coverage counted, accuracy sampled, disputes heard. The Signature inspector reports to the council, and the council funds the gaps.""",
demo_data={"fields":[
 {"name":"metric_secret","patterns":["secret"],"expected":"restricted"},
 {"name":"metric_open","patterns":[],"expected":"public"}]},
),
dict(
name="Classification and Lineage",
group="Advanced Classification", ladder_rank=29, ladder_tier="advanced",
description="""Classification joined with lineage answers where sensitive data flows: the restricted column's downstream journey through pipelines into marts, dashboards, and partner feeds - every hop labeled, every derived dataset inheriting the mark. The join powers the critical workflows: impact analysis respects sensitivity (this pipeline change touches restricted columns - security reviews), breach scoping uses lineage (the compromised table's restricted columns flowed to these three downstream tables - scope the notification), and compliance proves handling (show the restricted data's full journey with protections at each hop). Labels propagate through the lineage graph with high-water-mark rules; derived nodes inherit the maximum input label unless explicitly reviewed and downgraded. The combined graph is access-controlled by label: analysts see lineage for data they are cleared for, with sensitive paths summarized or redacted. Without the join, classification is a point-in-time label and lineage is a sensitivity-blind map - together they are a living protection system.""",
how_it_works="""The classification registry shares the lineage graph: labels on nodes and edges with propagation rules. Breach scoping traverses downstream from compromised nodes collecting sensitive labels. Impact workflows consult sensitivity for security-review routing. Compliance exports render labeled journeys with per-hop protections. Access control filters lineage views by clearance with redaction. Propagation conflicts (derived node with lower label than inputs) queue for review.""",
key_points=[
 "Labels on lineage nodes and edges; high-water-mark propagation.",
 "Breach scoping: downstream traversal collects exposed sensitive labels.",
 "Impact analysis routes sensitive changes to security review.",
 "Compliance exports show labeled journeys with per-hop protections.",
 "Lineage views filtered by clearance with redaction."],
requirements=[
 "Shared classification-lineage graph with propagation.",
 "Breach scoping via downstream label collection.",
 "Sensitivity-aware impact routing.",
 "Clearance-filtered lineage views."],
standards=[
 "ISO/IEC 27001."],
citations=[
 "ISO/IEC 27001. Information security management. ISO.",
 "OpenLineage. OpenLineage Specification. Linux Foundation."],
sig_lens="""The Signature reading: classification and lineage are the registry's two ledgers joined - the grades and the journeys, each illuminating the other. Together they trace every secret's travels and guard every road it walks.""",
demo_data={"fields":[
 {"name":"lineage_secret","patterns":["secret"],"expected":"restricted"},
 {"name":"lineage_kpi","patterns":[],"expected":"internal"}]},
),
dict(
name="Classification of Derived Data",
group="Advanced Classification", ladder_rank=30, ladder_tier="advanced",
description="""Derived data inherits sensitivity with judgment: the aggregate of restricted transactions is usually restricted (the underlying secrets shaped it), but the count of transactions may be internal (the number alone reveals nothing). The classification rules for derivatives: high-water mark by default (take the highest input label), downgrade allowed with review and evidence (the aggregate provably reveals nothing sensitive - differential privacy bounds, k-anonymity analysis), and re-derivation triggers re-classification (new inputs, new assessment). The dangerous cases are inference and reconstruction: the model trained on restricted data may memorize secrets (model weights inherit restricted), the aggregate with small cell sizes reveals individuals (cell suppression required). Reviews of derived classifications examine what the output actually reveals, not just its inputs - the output's own information content decides. ML models get special handling: training data labels propagate to model artifacts with memorization testing.""",
how_it_works="""Derivation workflows compute default labels by high-water mark; downgrade requests submit evidence (privacy analyses, cell sizes, memorization tests) for review. Small-cell suppression and differential privacy provide the evidence for safe downgrades. Model artifacts inherit training labels with memorization testing before any downgrade. Re-derivation re-triggers classification automatically. Reviews examine output information content, not just input labels.""",
key_points=[
 "Default: high-water mark from inputs; downgrade needs review with evidence.",
 "Danger cases: memorization, small cells, reconstruction from aggregates.",
 "Evidence for downgrade: differential privacy, k-anonymity, suppression.",
 "ML models inherit training labels; memorization tested before downgrade.",
 "Re-derivation re-triggers classification automatically."],
requirements=[
 "High-water-mark defaults with evidence-based downgrade review.",
 "Privacy analyses for downgrade evidence.",
 "Model memorization testing.",
 "Automatic re-classification on re-derivation."],
standards=[
 "ISO/IEC 27001; NIST SP 800-188 (de-identification)."],
citations=[
 "NIST SP 800-188. De-identifying Government Datasets. NIST.",
 "ISO/IEC 27001. Information security management. ISO."],
sig_lens="""The Signature reading: derived classification is the registry judging children by what they reveal, not just their parentage - the safe aggregate freed, the memorizing model bound. The Signature judge examines the child's own testimony.""",
demo_data={"fields":[
 {"name":"derived_secret","patterns":["secret"],"expected":"restricted"},
 {"name":"derived_count","patterns":[],"expected":"internal"}]},
),
dict(
name="Provenance of Classifications",
group="Advanced Classification", ladder_rank=31, ladder_tier="advanced",
description="""Every label should answer: who classified this, by what criteria version, with what confidence, on what evidence, when? Classification provenance records the chain: the classifier identity (human steward, pattern version, model version), the criteria version applied, the evidence (matched patterns, model features, human rationale), confidence, and timestamp. Provenance serves challenges (the label is wrong - show me why it was applied), audits (prove classifications followed criteria), tuning (which classifier version made these errors?), and re-classification (labels under old criteria versions need review). When labels propagate through pipelines, provenance chains extend: derived-from links back to source classifications. Provenance is immutable and retained with the label; re-classification appends new provenance rather than rewriting. A label without provenance is an assertion; with provenance, it is a defensible decision.""",
how_it_works="""Labeling tools emit PROV-O provenance with every classification: classifier, criteria version, evidence, confidence, timestamp. Propagation extends chains with derived-from links. Challenge workflows start from provenance; audits sample it; tuning analyzes errors by classifier version. Re-classification appends new provenance entries. Provenance stores immutably with labels, retained per data retention.""",
key_points=[
 "Provenance: classifier, criteria version, evidence, confidence, timestamp.",
 "Serves challenges, audits, tuning, re-classification.",
 "Propagation extends chains with derived-from links.",
 "Immutable, retained with labels; re-classification appends.",
 "Labels without provenance are assertions; with it, defensible decisions."],
requirements=[
 "PROV-O provenance emission on all classifications.",
 "Provenance chains through propagation.",
 "Challenge and audit workflows starting from provenance.",
 "Immutable provenance retained with labels."],
standards=[
 "W3C PROV-O; ISO/IEC 27001."],
citations=[
 "W3C. PROV-O: The PROV Ontology. W3C Recommendation, 2013.",
 "ISO/IEC 27001. Information security management. ISO."],
sig_lens="""The Signature reading: classification provenance is each grade's sworn testimony - grader named, law cited, evidence shown. The Signature registry's every grade can defend itself.""",
demo_data={"fields":[
 {"name":"prov_secret","patterns":["secret"],"expected":"restricted"},
 {"name":"prov_notice","patterns":[],"expected":"public"}]},
),
dict(
name="Classification Audits",
group="Advanced Classification", ladder_rank=32, ladder_tier="advanced",
description="""Classification audits verify the program's honesty: sampling labeled data and checking the labels are right, hunting unlabeled sensitive data, verifying protections match labels, and testing the classifiers. Audit types: label accuracy audits (sample per label, expert re-grade, measure precision/recall), coverage audits (scan for sensitive patterns in unlabeled data), control alignment audits (restricted labels with restricted controls deployed?), and classifier audits (model performance on fresh samples, pattern test suites). Findings route by severity: mislabeled restricted data as internal is an incident (under-protected now), over-labeled public as confidential is efficiency work. Audit independence matters: the team grading the graders cannot be the classifiers themselves. Audit results feed the metrics, the tuning, and the board - and the audit of audits checks that findings actually remediate, because findings without remediation are theater.""",
how_it_works="""Audit programs schedule the four audit types per database with independent auditors. Sampling is stratified by label and risk. Findings classify by severity with remediation workflows and deadlines; under-protection findings trigger incidents. Classifier audits run pattern test suites and model evaluations. Remediation verification closes findings with evidence; the audit-of-audits tracks closure rates. Results feed metrics dashboards and board reports.""",
key_points=[
 "Four audits: label accuracy, coverage, control alignment, classifier performance.",
 "Under-protection findings are incidents; over-labeling is efficiency work.",
 "Auditors independent from classifiers.",
 "Findings remediate with evidence; closure tracked.",
 "Audit-of-audits verifies remediation actually happens."],
requirements=[
 "Scheduled audit programs with independent auditors.",
 "Stratified sampling by label and risk.",
 "Severity-routed findings with remediation deadlines.",
 "Remediation verification with closure tracking."],
standards=[
 "ISO/IEC 27001 (internal audit); NIST SP 800-53 (CA family)."],
citations=[
 "ISO/IEC 27001. Information security management. ISO.",
 "NIST SP 800-53 Rev. 5 (CA family)."],
sig_lens="""The Signature reading: classification audits are the registry's inspection of its own graders - independent, sampled, severe on under-protection. The Signature inspection closes every finding with evidence.""",
demo_data={"fields":[
 {"name":"audit_secret","patterns":["secret"],"expected":"restricted"},
 {"name":"audit_faq","patterns":[],"expected":"public"}]},
),
dict(
name="Incident Handling for Misclassified Data",
group="Advanced Classification", ladder_rank=33, ladder_tier="advanced",
description="""Misclassified data causes incidents in two directions: under-classified (restricted data labeled internal - exposed without protections) and over-classified (public data labeled restricted - work blocked, or worse, the label ignored because everything is restricted). Under-classification incidents run the breach playbook: contain the exposure, assess what was exposed to whom, notify per the true label's duties, fix the classification, and hunt for siblings (the same classifier's other errors). Over-classification incidents run the friction playbook: assess what work was blocked, downgrade with review, and tune the classifier. Both feed root-cause analysis: was it criteria ambiguity, classifier error, human mistake, or context change? The incident record links to the re-classification, so the fix is verifiable. Misclassification trends - rising under-classification from one classifier - trigger classifier suspension pending retraining. The program's credibility rests on handling these incidents visibly and well.""",
how_it_works="""Incident intake classifies direction: under (breach playbook) or over (friction playbook). Under-classification: contain, assess exposure, notify per true label, fix labels, hunt siblings. Over-classification: assess blocked work, downgrade with review, tune classifier. Root-cause analysis per incident with classifier suspension triggers on trends. Records link to re-classifications for verifiable fixes. Trend dashboards watch misclassification rates per classifier.""",
key_points=[
 "Under-classified: breach playbook - contain, assess, notify, fix, hunt siblings.",
 "Over-classified: friction playbook - assess blocked work, downgrade, tune.",
 "Root-cause per incident; trends suspend faulty classifiers.",
 "Records link to re-classifications for verifiable fixes.",
 "Credibility rests on visible, competent handling."],
requirements=[
 "Direction-triaged incident playbooks.",
 "Sibling-hunting for classifier errors.",
 "Classifier suspension triggers on trends.",
 "Verifiable fix linkage in records."],
standards=[
 "ISO/IEC 27001; NIST SP 800-61."],
citations=[
 "NIST SP 800-61 Rev. 2. Computer Security Incident Handling Guide.",
 "ISO/IEC 27001. Information security management. ISO."],
sig_lens="""The Signature reading: misclassification incidents are the registry's reckoning with its own errors - the exposed contained, the blocked freed, the faulty grader retrained or retired. The Signature reckoning is public within the house, for credibility is earned in the open.""",
demo_data={"fields":[
 {"name":"incident_secret","patterns":["secret"],"expected":"restricted"},
 {"name":"incident_help","patterns":[],"expected":"public"}]},
),
dict(
name="Sensitive Data Classification Mastery Review",
group="Advanced Classification", ladder_rank=34, ladder_tier="advanced",
description="""The mastery review binds the ladder. Foundations: classification grades data by harm and law; its worth proven in risk, compliance, and cost; public data cleared with integrity; internal data bounded; confidential data sealed with need-to-know; restricted and regulated data in the inner sanctum with maximum controls; personal data as the charge of souls; special categories sacred; proprietary data as competitive lifeblood; trade secrets armored by three prongs; health data tenderly guarded; financial data in the industry's strictest vault. Compounded: criteria as grading laws; labeling as heraldry; automated scribes with human judgment; pattern scouts and learned judges; handling codes per rank; graded gates of access; graded armor of encryption; veils of masking; labels riding pipelines; metadata as credentials; honest re-grading. Advanced: honorable discharges; courts of dispute; the million-archive heraldry; inspection metrics; joined ledgers of classification and lineage; judgment of derived children; sworn testimonies of provenance; independent audits; reckonings with error. The creed: every secret graded, every grade protected, every protection proven.""",
how_it_works="""The review serves as capstone assessment and deployment checklist: can the team define the taxonomy, classify the estate, enforce handling, and prove it? New classification programs verify each rung: criteria written, classifiers running, labels propagating, audits scheduled. Gaps become the quarter's program of work. The review repeats as data and law evolve.""",
key_points=[
 "Foundations: taxonomy, worth, public through restricted, PII, special categories, proprietary, trade secrets, PHI, PCI.",
 "Compounded: criteria, labeling, automation, patterns, ML, handling, access, encryption, masking, pipelines, metadata, re-classification.",
 "Advanced: declassification, disputes, network scale, metrics, lineage join, derived data, provenance, audits, incidents.",
 "The creed: every secret graded, every grade protected, every protection proven.",
 "Mastery reassessed as data and law evolve."],
requirements=[
 "Demonstrated competence at every rung before program launch.",
 "Checklist rerun on taxonomy and estate changes.",
 "Gaps converted to funded program work."],
standards=[
 "ISO/IEC 27001."],
citations=[
 "ISO/IEC 27001. Information security management. ISO.",
 "NIST SP 800-60 Vol. 2."],
sig_lens="""The Signature reading: the mastery review is graduation as keeper of secrets. The Signature graduate grades every secret justly, guards each by its rank, and swears the creed: every secret graded, every grade protected, every protection proven.""",
demo_data={"fields":[
 {"name":"mastery_secret","patterns":["secret"],"expected":"restricted"},
 {"name":"mastery_open","patterns":[],"expected":"public"}]},
),
]
