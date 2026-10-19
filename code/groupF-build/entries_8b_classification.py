#!/usr/bin/env python3
"""Sensitive Data Classification entries 13-24 (compounded)."""

APPEND = [
dict(
name="Classification Criteria",
group="Classification Operations", ladder_rank=13, ladder_tier="compounded",
description="""Classification criteria are the decision rules that assign labels: the written tests a classifier - human or machine - applies to data. Good criteria are specific, testable, and harm-anchored: restricted if disclosure would cause severe financial loss (over $1M), legal violation, or physical harm; confidential if it would cause material harm or trigger breach notification; internal if for employees only; public if cleared for release. Criteria cover content (what the data is), context (who it is about, what project), and combination (individually internal fields that together identify someone become confidential). The criteria document includes examples per level and borderline cases with rulings - the case law of classification that keeps decisions consistent. Criteria are reviewed when harm landscapes change: a new breach law can move data from internal to confidential overnight. The registry versions criteria; every classification cites the criteria version applied.""",
how_it_works="""Criteria documents define per-level tests with harm thresholds, content/context/combination rules, examples, and borderline rulings. Classifiers (human and automated) apply the current version; classifications cite it. Borderline cases escalate to the classification board, whose rulings publish as new case law. Harm-landscape reviews (new laws, new breach costs) trigger criteria updates with re-classification sweeps where needed. Consistency audits sample classifications against criteria; drift triggers retraining.""",
key_points=[
 "Criteria: specific, testable, harm-anchored decision rules per label.",
 "Cover content, context, and combination effects.",
 "Borderline rulings publish as case law for consistency.",
 "Reviewed when harm landscapes change; versions cited by classifications.",
 "Consistency audits sample decisions against criteria."],
requirements=[
 "Criteria documents with harm thresholds and examples.",
 "Borderline case law with board rulings.",
 "Versioned criteria cited by every classification.",
 "Consistency audits with retraining on drift."],
standards=[
 "ISO/IEC 27001 Annex A.8.",
 "NIST SP 800-60."],
citations=[
 "ISO/IEC 27001. Information security management. ISO.",
 "NIST SP 800-60 Vol. 2."],
sig_lens="""The Signature reading: criteria are the registry's laws of grading - written, harm-anchored, with case law for the hard cases. The Signature laws version with the world and judge every classification by the edition in force.""",
demo_data={"fields":[
 {"name":"merger_plan","patterns":["secret"],"expected":"restricted"},
 {"name":"team_lunch","patterns":[],"expected":"internal"}]},
),
dict(
name="Labeling Schemes",
group="Classification Operations", ladder_rank=14, ladder_tier="compounded",
description="""Labeling schemes make classification visible and machine-enforceable: every file, email, database column, and dashboard carries its label where systems and humans can see it. The scheme defines label formats per medium: email subject prefixes ([CONFIDENTIAL]), document headers and footers, file metadata tags, database column tags, and API response headers. Labels must be persistent (surviving copies and conversions), visible (humans see them without hunting), and structured (machines parse them reliably). The scheme also handles composites: a document combining internal and confidential sources takes the highest label - the high-water mark rule. Labeling is enforced at creation (templates pre-labeled, classifiers suggesting) and verified by audits (unlabeled sensitive data is a finding). The scheme versions like criteria; label migrations (renaming levels) are managed projects, not silent edits.""",
how_it_works="""The scheme specifies label formats per medium with persistence, visibility, and structure requirements. Creation tools apply labels: templates pre-labeled, classifiers auto-suggesting, humans confirming. High-water-mark rules compute composite labels automatically. DLP and access systems read structured labels for enforcement. Audits sample for unlabeled or mislabeled data; findings route to owners with relabeling. Scheme changes version with migration plans for existing labels.""",
key_points=[
 "Labels visible on every medium: emails, documents, files, columns, APIs.",
 "Persistent, visible, structured - surviving copies, seen by humans, parsed by machines.",
 "High-water mark: composites take the highest constituent label.",
 "Enforced at creation; verified by audit.",
 "Scheme versions; label migrations are managed projects."],
requirements=[
 "Label format specifications per medium.",
 "Creation-time labeling with classifier assistance.",
 "High-water-mark computation for composites.",
 "Audit sampling with relabeling workflows."],
standards=[
 "ISO/IEC 27001 Annex A.8."],
citations=[
 "ISO/IEC 27001. Information security management. ISO.",
 "NIST SP 800-53 (media protection)."],
sig_lens="""The Signature reading: labeling is the registry's heraldry - every document bearing its rank openly, composites flying the highest color. The Signature heraldry is enforced at creation and inspected in audit.""",
demo_data={"fields":[
 {"name":"secret_memo","patterns":["secret"],"expected":"restricted"},
 {"name":"newsletter","patterns":[],"expected":"public"}]},
),
dict(
name="Automated Classification",
group="Classification Operations", ladder_rank=15, ladder_tier="compounded",
description="""Automated classification labels data at machine scale: pattern matchers find SSNs and card numbers, ML models judge sensitivity from content and context, and metadata rules apply labels from source and type. The pipeline runs at creation and on schedule across the estate, each label carrying the classifier, confidence, and criteria version. Automation's strength is coverage - millions of files labeled where humans could never reach; its weakness is judgment - the model cannot know the merger plan's sensitivity from its words alone. The operating model is therefore human-in-the-loop by confidence: high-confidence labels apply automatically, medium-confidence suggest for human confirmation, low-confidence queue for review. Feedback from human decisions retrains the models; accuracy is measured per class on labeled samples, with minimum bars before auto-apply is allowed. Automated labels are marked as such - provenance matters when a label is challenged.""",
how_it_works="""Classifiers run at creation (inline) and on schedule (estate sweeps): patterns, ML models, metadata rules. Labels record classifier, confidence, criteria version. Confidence routing: auto-apply, suggest, or queue per thresholds. Human decisions feed retraining; accuracy measured per class on samples with auto-apply bars. Model versions track with training data; estate re-scans apply improved models. Provenance marks automated labels for challenge workflows.""",
key_points=[
 "Patterns, ML models, and metadata rules classify at machine scale.",
 "Labels carry classifier, confidence, criteria version.",
 "Human-in-the-loop by confidence: auto-apply, suggest, or queue.",
 "Accuracy measured per class; auto-apply needs minimum bars.",
 "Human decisions retrain models; provenance marks automated labels."],
requirements=[
 "Classifier pipeline with patterns, ML, and rules.",
 "Confidence routing with per-class thresholds.",
 "Accuracy measurement on labeled samples.",
 "Retraining from human decisions with versioning."],
standards=[
 "ISO/IEC 27001."],
citations=[
 "ISO/IEC 27001. Information security management. ISO.",
 "NIST SP 800-60 Vol. 2."],
sig_lens="""The Signature reading: automated classification is the registry's tireless scribe - labeling millions where humans cannot reach, humble about uncertainty, learning from every correction. The Signature scribe marks its own work and submits to audit.""",
demo_data={"fields":[
 {"name":"auto_ssn","patterns":["ssn"],"expected":"restricted"},
 {"name":"auto_note","patterns":[],"expected":"internal"}]},
),
dict(
name="Regex and Pattern Matching",
group="Classification Operations", ladder_rank=16, ladder_tier="compounded",
description="""Pattern matching finds structured sensitive data with regular expressions: SSNs (ddd-dd-dddd with area-number validation), card numbers (13-19 digits passing Luhn), emails, phones, IBANs (country-specific check digits), passport formats. Patterns run fast over massive estates and need no training - the first line of classification defense. But patterns have known weaknesses: false positives (the 16-digit order number that passes Luhn), false negatives (the SSN with spaces instead of dashes), and context blindness (the test card number in documentation). The discipline is pattern engineering: validate check digits, require context keywords nearby, maintain allow-lists for test data, and tune per data source. Patterns are versioned with their test suites - each pattern ships with true/false positive examples that CI verifies. Pattern libraries are shared across the estate so every scanner uses the same definitions.""",
how_it_works="""The pattern library holds versioned regexes with check-digit validation, context requirements, and allow-lists. Scanners run patterns over estate data on schedule; matches get confidence from pattern strength plus context. Test suites per pattern verify against true/false examples in CI. Tuning per source adjusts for local formats; false-positive feedback refines patterns. Libraries publish to all scanners ensuring consistent definitions estate-wide.""",
key_points=[
 "Patterns find SSNs, PANs (Luhn), IBANs, phones, emails - fast, no training needed.",
 "Weaknesses: false positives, false negatives, context blindness.",
 "Pattern engineering: check digits, context keywords, allow-lists, per-source tuning.",
 "Patterns versioned with test suites verified in CI.",
 "Shared libraries keep definitions consistent estate-wide."],
requirements=[
 "Versioned pattern library with validation logic.",
 "Per-pattern test suites in CI.",
 "Context requirements and allow-lists.",
 "Shared publication to all scanners."],
standards=[
 "NIST SP 800-122 (PII patterns)."],
citations=[
 "NIST SP 800-122. Guide to Protecting PII.",
 "PCI SSC guidance on PAN discovery."],
sig_lens="""The Signature reading: pattern matching is the registry's sharp-eyed scout - swift, tireless, finding the structured secrets by their shapes. The Signature scout's eyes are tested regularly and its judgments tuned per terrain.""",
demo_data={"fields":[
 {"name":"regex_pan","patterns":["card"],"expected":"restricted"},
 {"name":"regex_free","patterns":[],"expected":"public"}]},
),
dict(
name="ML Classifiers for Sensitivity",
group="Classification Operations", ladder_rank=17, ladder_tier="compounded",
description="""ML classifiers judge sensitivity where patterns cannot: the merger memo with no card numbers but unmistakable sensitivity, the free-text complaint containing health details, the code file with embedded credentials. Models learn from labeled examples - documents labeled by humans across the taxonomy - using text and metadata features. The engineering challenges are real: labeled data is scarce and expensive, classes are imbalanced (restricted is rare), language and domain shift degrade models, and false negatives (missing a secret) cost more than false positives. The operating discipline: train per domain where feasible, calibrate confidence honestly, set decision thresholds by the cost of errors per class, and keep humans on the high-stakes classes. Model cards document training data, performance per class, limitations, and intended use - because a classifier deployed beyond its training is a liability. Drift monitoring watches for the world changing under the model.""",
how_it_works="""Training pipelines use human-labeled examples with active learning prioritizing the most informative unlabeled items. Models version with training data and per-class metrics; model cards document scope and limits. Thresholds set per class by error costs; high-stakes classes keep human review. Deployment monitors drift and performance decay; retraining triggers on labeled feedback and schedule. Inference labels carry model version and confidence for provenance.""",
key_points=[
 "ML judges sensitivity from content and context where patterns cannot.",
 "Challenges: scarce labels, imbalanced classes, domain shift, costly false negatives.",
 "Thresholds set by per-class error costs; humans stay on high-stakes classes.",
 "Model cards document training, performance, limits, intended use.",
 "Drift monitoring with retraining from labeled feedback."],
requirements=[
 "Labeled training data with active learning.",
 "Per-class thresholds by error cost.",
 "Model cards with versioned training data.",
 "Drift monitoring with retraining triggers."],
standards=[
 "NIST AI risk management framework (adapted)."],
citations=[
 "NIST AI 100-1. AI Risk Management Framework.",
 "ISO/IEC 27001. Information security management. ISO."],
sig_lens="""The Signature reading: ML classifiers are the registry's learned judges - reading meaning, not just shapes, honest about their limits. The Signature judges carry their credentials (model cards) and defer the gravest cases to humans.""",
demo_data={"fields":[
 {"name":"ml_memo","patterns":["secret"],"expected":"restricted"},
 {"name":"ml_public","patterns":[],"expected":"public"}]},
),
dict(
name="Handling Rules by Level",
group="Handling Rules", ladder_rank=18, ladder_tier="compounded",
description="""Handling rules translate labels into behavior: what may be done with data at each level. Public: share freely, integrity-protected. Internal: authenticated access, no external sharing without approval. Confidential: need-to-know, encrypted, no external transmission unprotected, DLP monitored. Restricted: multi-party approval, hardware-backed protection, segmented networks, continuous monitoring. The rules cover the full handling lifecycle: creation (label it), storage (encrypt per level), use (access per level), sharing (approve per level), transmission (protect per level), and disposal (destroy per level). Rules are written plainly for the humans who must follow them - the one-page handling guide per level beats the fifty-page policy nobody reads. Enforcement is layered: technical controls where possible (DLP blocking restricted email attachments), training and culture where not, and audit verifying both. Handling violations feed the incident process with severity by label.""",
how_it_works="""Handling matrices define allowed actions per label across creation, storage, use, sharing, transmission, disposal. Technical enforcement implements where possible: DLP, encryption enforcement, sharing approvals. Plain-language guides per level distribute to staff; training covers the rules with examples. Audits sample handling compliance; violations route to incidents by label severity. Rule changes version with communication to all handlers.""",
key_points=[
 "Rules per level across creation, storage, use, sharing, transmission, disposal.",
 "Plain-language one-page guides beat unread fifty-page policies.",
 "Technical enforcement where possible; training and audit elsewhere.",
 "Violations feed incidents with severity by label.",
 "Rules versioned with communication on change."],
requirements=[
 "Handling matrices per label covering the full lifecycle.",
 "Technical enforcement (DLP, encryption, approvals).",
 "Plain-language guides and training.",
 "Handling audits with incident routing."],
standards=[
 "ISO/IEC 27001 Annex A.8.",
 "NIST SP 800-53."],
citations=[
 "ISO/IEC 27001. Information security management. ISO.",
 "NIST SP 800-53 Rev. 5."],
sig_lens="""The Signature reading: handling rules are the registry's code of conduct per rank - plain, complete, enforced. The Signature code is written for humans to follow and machines to enforce.""",
demo_data={"fields":[
 {"name":"handle_secret","patterns":["secret"],"expected":"restricted"},
 {"name":"handle_news","patterns":[],"expected":"public"}]},
),
dict(
name="Access Controls by Classification",
group="Handling Rules", ladder_rank=19, ladder_tier="compounded",
description="""Access controls scale with labels: public needs none beyond integrity, internal needs authentication, confidential needs need-to-know authorization, restricted needs multi-party approval with time limits. The models combine: RBAC for role-based grants at scale, ABAC for attribute-driven decisions (this analyst may see EU customer data but not US), and just-in-time elevation for the rare restricted access (approved, time-boxed, fully logged). The critical disciplines are least privilege (no standing access beyond need), regular recertification (managers confirm their teams' access quarterly), and prompt deprovisioning (departures revoke within hours, not weeks). Access decisions log with the label and justification - the audit trail proving who saw what sensitive data when. Break-glass procedures cover emergencies: predefined emergency access with automatic full logging and mandatory post-use review. Access analytics hunt anomalies: the account reading ten times its normal confidential volume gets investigated.""",
how_it_works="""Access policies per label define the model: public open, internal authenticated, confidential RBAC/ABAC need-to-know, restricted JIT with multi-party approval. Provisioning workflows grant per policy; recertification campaigns confirm quarterly; deprovisioning triggers on HR events. Break-glass accounts exist with sealed credentials and automatic review. Access logs record label, justification, and decision; analytics flag anomalies. Policy violations block with the violated rule cited.""",
key_points=[
 "Controls scale: public open, internal authenticated, confidential need-to-know, restricted JIT.",
 "RBAC for scale, ABAC for attribute precision, JIT for rare sensitive access.",
 "Least privilege, quarterly recertification, prompt deprovisioning.",
 "Break-glass with automatic logging and mandatory review.",
 "Access analytics hunt anomalous sensitive-data reading."],
requirements=[
 "Per-label access policies with models defined.",
 "Recertification and deprovisioning workflows.",
 "Break-glass procedures with review.",
 "Access logging with anomaly analytics."],
standards=[
 "NIST SP 800-53 (AC family); ISO/IEC 27001."],
citations=[
 "NIST SP 800-53 Rev. 5. Security and Privacy Controls.",
 "ISO/IEC 27001. Information security management. ISO."],
sig_lens="""The Signature reading: access by classification is the registry's graded gates - each rank's door with its proper lock, the innermost needing many keys and an hourglass. The Signature gates log every entry and hunt the anomalous visitor.""",
demo_data={"fields":[
 {"name":"gate_secret","patterns":["secret"],"expected":"restricted"},
 {"name":"gate_internal_doc","patterns":[],"expected":"internal"}]},
),
dict(
name="Encryption Requirements",
group="Handling Rules", ladder_rank=20, ladder_tier="compounded",
description="""Encryption requirements scale with labels: confidential data encrypted at rest (AES-256) and in transit (TLS 1.2+), restricted data with hardware-backed keys and field-level encryption for the most sensitive fields, internal data encrypted in transit with at-rest encryption standard. The requirements cover key management per label: confidential keys in managed KMS with rotation, restricted keys in HSMs with dual control and jurisdictional custody. Field-level encryption protects the sensitive columns within mixed datasets - the table is internal, but the SSN column is encrypted restricted. Requirements also cover the edges: backups encrypted per the data's label, key destruction as the deletion method for crypto-shredding, and cryptographic agility to migrate algorithms before they weaken. Compliance verifies encryption actually deployed - the requirement on paper means nothing if the bucket is unencrypted.""",
how_it_works="""Encryption policies per label define algorithms, key storage, rotation, and scope (full-disk, database, field-level). KMS/HSM infrastructure implements per policy with jurisdictional custody. Field-level encryption integrates with applications for mixed-sensitivity datasets. Deployment verification scans for unencrypted holdings per label; gaps remediate on timelines by label severity. Algorithm agility plans schedule migrations; key destruction executes crypto-shredding deletions.""",
key_points=[
 "Requirements scale: confidential AES-256/TLS, restricted HSM-backed with field-level.",
 "Key management per label: KMS rotation to HSM dual control.",
 "Field-level encryption for sensitive columns in mixed datasets.",
 "Backups and key destruction covered; agility plans migrate algorithms.",
 "Deployment verified - paper requirements mean nothing unencrypted."],
requirements=[
 "Per-label encryption policies with algorithms and key rules.",
 "KMS/HSM infrastructure with jurisdictional custody.",
 "Field-level encryption for mixed datasets.",
 "Deployment verification scanning."],
standards=[
 "NIST SP 800-57; ISO/IEC 27040."],
citations=[
 "NIST SP 800-57. Recommendation for Key Management. NIST.",
 "NIST SP 800-53 Rev. 5 (SC family)."],
sig_lens="""The Signature reading: encryption by label is the registry's graded armor - each rank's secrets sealed to its worth, the keys kept as carefully as the data. The Signature armory verifies its seals and plans their renewal.""",
demo_data={"fields":[
 {"name":"enc_secret","patterns":["secret"],"expected":"restricted"},
 {"name":"enc_note","patterns":[],"expected":"internal"}]},
),
dict(
name="Masking and Tokenization",
group="Handling Rules", ladder_rank=21, ladder_tier="compounded",
description="""Masking and tokenization let systems use sensitive data's shape without its substance: the support agent sees the last four digits, the analyst works with tokens that preserve joins but reveal nothing, the test environment runs on masked copies. Masking transforms values irreversibly (or reversibly with privileged unmasking): full masking (XXX-XX-1234), partial masking, format-preserving masking (a valid-looking but fake card number), and redaction (removal). Tokenization replaces values with random tokens mapped in a secure vault - the token keeps referential integrity across systems while the vault holds the secret. The choice depends on need: analytics needing joins uses tokenization; display needing plausibility uses format-preserving masking; irreversible needs use redaction. Masking policies per label define what each role sees: support sees partial, analytics sees tokens, nobody outside production sees real. Unmasking is privileged, logged, and approved - the exception, never the norm.""",
how_it_works="""Masking policies per label and role define the transformation: full, partial, format-preserving, redaction, or tokenization. Token vaults secure the mappings with restricted access. Data pipelines apply masking at the boundary between production and lower environments; test data is masked by default. Unmasking workflows require approval with logged justification. Policy verification samples masked outputs for reversibility leaks. Token vaults get the restricted label with HSM backing.""",
key_points=[
 "Masking: irreversible (or privileged-reversible) transformation preserving shape.",
 "Tokenization: random tokens with vault mappings preserving joins.",
 "Choice by need: tokens for analytics joins, format-preserving for display, redaction for removal.",
 "Policies per label and role: who sees what form.",
 "Unmasking privileged, logged, approved - the exception."],
requirements=[
 "Masking policies per label and role.",
 "Token vaults with restricted HSM-backed protection.",
 "Boundary masking between production and lower environments.",
 "Unmasking workflows with approval and logging."],
standards=[
 "NIST SP 800-53; PCI SSC tokenization guidance."],
citations=[
 "PCI Security Standards Council. Tokenization Product Security Guidelines.",
 "NIST SP 800-53 Rev. 5."],
sig_lens="""The Signature reading: masking is the registry's veil - each rank shown only what its eyes may see, the substance hidden but the shape kept. The Signature veil's lifting is privileged, logged, and rare.""",
demo_data={"fields":[
 {"name":"mask_ssn","patterns":["ssn"],"expected":"restricted"},
 {"name":"mask_city","patterns":[],"expected":"internal"}]},
),
dict(
name="Classification in Pipelines",
group="Handling Rules", ladder_rank=22, ladder_tier="compounded",
description="""Classification must flow through pipelines, not stop at the source: the restricted column entering the ETL must emerge labeled in the warehouse, the masked field must stay masked through transformations, the derived table must inherit the highest input label. Pipeline classification propagates labels through transformations with rules: high-water mark (output takes the max input label), masking preservation (masked inputs stay masked unless explicitly unmasked by privilege), and derivation review (new combinations assessed for emergent sensitivity). Pipeline frameworks integrate classification natively: column tags propagate through SQL, Spark, and dbt transformations automatically. Unlabeled pipeline outputs are blocked from production - the pipeline that drops labels fails its contract. Lineage carries labels: the classification registry and lineage registry share the graph, so impact analysis respects sensitivity (this change touches restricted columns - route to security review).""",
how_it_works="""Pipeline frameworks propagate column tags through transformations with high-water-mark rules. Masking operators preserve masking through pipelines; unmasking requires privilege at defined points. Derivation reviews assess new combinations for emergent sensitivity before production. Contract checks block unlabeled outputs. The classification-lineage integration shares the graph with labels on nodes and edges; change workflows consult sensitivity for routing.""",
key_points=[
 "Labels propagate through pipelines: high-water mark on outputs.",
 "Masking preserved through transformations; unmasking privileged.",
 "New combinations reviewed for emergent sensitivity.",
 "Unlabeled pipeline outputs blocked from production.",
 "Classification-lineage integration routes sensitive changes to security review."],
requirements=[
 "Label propagation in pipeline frameworks.",
 "Masking preservation with privileged unmasking points.",
 "Derivation sensitivity reviews.",
 "Contract blocking on unlabeled outputs."],
standards=[
 "ISO/IEC 27001."],
citations=[
 "ISO/IEC 27001. Information security management. ISO.",
 "DAMA International. DAMA-DMBOK, 2nd ed. Technics Publications, 2017."],
sig_lens="""The Signature reading: pipeline classification is the registry's labels traveling with the data through every transformation - never dropped, never diluted, the highest mark prevailing. The Signature labels ride every pipeline like seals on cargo.""",
demo_data={"fields":[
 {"name":"pipe_secret","patterns":["secret"],"expected":"restricted"},
 {"name":"pipe_metric","patterns":[],"expected":"internal"}]},
),
dict(
name="Classification Metadata",
group="Handling Rules", ladder_rank=23, ladder_tier="compounded",
description="""Classification metadata records every labeling decision: the label, the classifier (human, pattern, model with version), confidence, criteria version, timestamp, and the evidence (which pattern matched, which features mattered). Metadata travels with the data - in file tags, column tags, API headers - so protections apply wherever the data goes. The metadata model distinguishes asserted labels (human-declared, highest trust) from derived labels (propagated, high-water-marked) from inferred labels (model-guessed, confidence-marked) - because the label's own trustworthiness matters when labels conflict. Metadata quality is monitored: unlabeled sensitive data found by audits, conflicting labels on the same data, stale labels under old criteria versions. The metadata store is queryable: show me all restricted data in this system, show me labels applied by model v3 needing review under v4 criteria.""",
how_it_works="""Labeling tools write full metadata with every label; propagation preserves and extends it (derived-from chains). Metadata travels in file tags, column properties, and headers. Quality monitors find unlabeled-sensitive, conflicts, and stale-criteria labels. Query APIs serve inventories by label, classifier, and criteria version. Re-labeling sweeps update stale labels under new criteria with the changes logged. Metadata retention follows the data's retention.""",
key_points=[
 "Metadata: label, classifier, confidence, criteria version, timestamp, evidence.",
 "Distinguishes asserted, derived, and inferred labels by trustworthiness.",
 "Travels with data across files, columns, APIs.",
 "Quality monitored: unlabeled-sensitive, conflicts, stale criteria.",
 "Queryable inventories by label, classifier, version."],
requirements=[
 "Full metadata capture on every labeling.",
 "Propagation preserving metadata chains.",
 "Quality monitoring with remediation workflows.",
 "Queryable metadata store with re-labeling sweeps."],
standards=[
 "ISO/IEC 27001."],
citations=[
 "ISO/IEC 27001. Information security management. ISO.",
 "NIST SP 800-60 Vol. 2."],
sig_lens="""The Signature reading: classification metadata is each label's credentials - who graded, how surely, by which law, on what evidence. The Signature credentials travel with the grade and are inspected for forgery.""",
demo_data={"fields":[
 {"name":"meta_secret","patterns":["secret"],"expected":"restricted"},
 {"name":"meta_public_doc","patterns":[],"expected":"public"}]},
),
dict(
name="Re-classification Workflows",
group="Handling Rules", ladder_rank=24, ladder_tier="compounded",
description="""Re-classification changes labels when the world changes: criteria update, data sensitivity shifts, errors are found, or contexts change (the internal project goes public, the public dataset gains personal data). The workflow handles both directions with appropriate care: upgrades (internal to confidential) apply protections immediately - the data was under-protected, fix it now; downgrades (confidential to internal) require review and approval - the data may still need protection, and premature downgrades leak. Re-classification sweeps apply criteria updates across the estate: the new criteria version re-evaluates labels, changes queue for the right workflow (auto-upgrade, reviewed downgrade), and the sweep reports its blast radius. Individual challenges let data owners dispute labels with evidence; the classification board adjudicates. Every re-classification logs with the reason, the criteria versions, and the authority - because label changes rewrite protections, and protection changes need audit trails.""",
how_it_works="""Triggers (criteria updates, error findings, context changes, challenges) queue items for re-classification. Upgrades auto-apply with immediate protection enforcement; downgrades route to review with risk assessment. Sweeps re-evaluate estate-wide under new criteria with blast-radius reports. Challenge workflows let owners dispute with evidence; boards adjudicate with published rulings. All changes log with reasons, versions, authority. Protection systems consume label changes in near real-time.""",
key_points=[
 "Upgrades apply immediately (was under-protected); downgrades need review (may still need it).",
 "Criteria-update sweeps re-evaluate estate-wide with blast-radius reports.",
 "Challenges let owners dispute labels; boards adjudicate with published rulings.",
 "Every change logged with reason, versions, authority.",
 "Protection systems consume label changes in near real-time."],
requirements=[
 "Re-classification triggers with upgrade/downgrade routing.",
 "Estate sweeps on criteria updates.",
 "Challenge workflows with board adjudication.",
 "Real-time protection updates on label change."],
standards=[
 "ISO/IEC 27001."],
citations=[
 "ISO/IEC 27001. Information security management. ISO.",
 "DAMA International. DAMA-DMBOK, 2nd ed. Technics Publications, 2017."],
sig_lens="""The Signature reading: re-classification is the registry's honest re-grading - promotions swift, demotions careful, challenges heard, every change warranted. The Signature re-grader never strips protection on a whim.""",
demo_data={"fields":[
 {"name":"reclass_secret","patterns":["secret"],"expected":"restricted"},
 {"name":"reclass_blog","patterns":[],"expected":"public"}]},
),
]
