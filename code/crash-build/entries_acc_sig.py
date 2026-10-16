#!/usr/bin/env python3
"""PHASE M — accidents-insurance-proven-signature (Signature Edition) seed entries.

Original Signature creations: his own accident-verification frameworks and
documentation standards. src="signature".
Tuple: (key, group, title, desc, points, req, standards, citations, demo_kind, verification)
"""

ENTRIES = [
# ---------------- verification frameworks (15) ----------------
("sig-three-tier-scale", "verification-frameworks",
 "The Signature Three-Tier Verification Scale",
 "The Signature Three-Tier Verification Scale is the original Signature method "
 "for grading accident documentation: Tier 1, official-investigation, for "
 "records resting on a formal investigation report by an official body; Tier 2, "
 "insurance-documented, for records resting on claims, compensation, or "
 "litigation files; Tier 3, publicly-reported, for records resting on reputable "
 "public reporting and public records. Every record in the system carries its "
 "tier as a visible field, and no record may claim a higher tier than its "
 "weakest supporting document. The scale makes documentation strength "
 "explicit instead of implied.",
 ("Tier 1: official-investigation — formal report by an official body",
  "Tier 2: insurance-documented — claims, compensation, or litigation files",
  "Tier 3: publicly-reported — reputable public reporting and public records",
  "Tier carried as a visible field on every record",
  "No record claims a higher tier than its weakest document",
  "Makes documentation strength explicit, not implied"),
 "A complete framework record requires: tier definitions; tier-assignment rules; "
 "weakest-document rule; field specification; worked tiering description.",
 ("Signature verification canon — original Signature method",
  "Compatibility: maps to evidence-hierarchy practice"),
 "Original Signature creation — Signature system (Signature Edition).",
 "verify", None),

("sig-evidence-custody", "verification-frameworks",
 "Signature Evidence Chain-of-Custody Protocol",
 "The Signature Evidence Chain-of-Custody Protocol is an original Signature "
 "procedure that makes every accident document traceable: each item is logged "
 "at acquisition with source, date, custodian, and integrity check; every "
 "transfer is countersigned; and any gap in the chain downgrades the item's "
 "verification tier automatically. The protocol treats an undocumented "
 "document as unverified by definition — provenance is part of the evidence, "
 "not paperwork around it. It applies equally to official reports, claims "
 "files, and press archives.",
 ("Every item logged: source, date, custodian, integrity check",
  "Every transfer countersigned",
  "Chain gaps downgrade the verification tier automatically",
  "Undocumented documents are unverified by definition",
  "Provenance is part of the evidence",
  "Applies to reports, claims files, and press archives alike"),
 "A complete framework record requires: log schema; transfer procedure; "
 "integrity-check methods; downgrade rules; application notes per document type.",
 ("Signature verification canon — original Signature method",
  "Compatibility: consistent with evidence-handling standards"),
 "Original Signature creation — Signature system (Signature Edition).",
 "verify", None),

("sig-official-intake", "verification-frameworks",
 "The Signature Official-Investigation Intake Standard",
 "The Signature Official-Investigation Intake Standard is an original Signature "
 "checklist for admitting Tier 1 records: the report must be issued by a "
 "recognized investigation body, must be the final (not interim) version "
 "unless marked as such, must contain findings distinct from factual narrative, "
 "and must be retrievable from a public source. Reports that fail any check "
 "are admitted at Tier 3 with a note, never silently promoted. The standard "
 "prevents press summaries of investigations from masquerading as the "
 "investigations themselves.",
 ("Admit only: recognized body, final version, findings distinct from narrative",
  "Must be retrievable from a public source",
  "Failures admitted at Tier 3 with a note — never silently promoted",
  "Press summaries never masquerade as investigations",
  "Interim reports marked as interim",
  "Output: a tiered intake decision per document"),
 "A complete framework record requires: the four intake checks; version-marking rules; "
 "downgrade procedure; press-summary detection guidance.",
 ("Signature verification canon — original Signature method",
  "Compatibility: consistent with archival appraisal practice"),
 "Original Signature creation — Signature system (Signature Edition).",
 "verify", None),

("sig-insurance-verification", "verification-frameworks",
 "Signature Insurance-Document Verification Checklist",
 "The Signature Insurance-Document Verification Checklist is an original "
 "Signature tool for Tier 2 records: it verifies that a claims file shows the "
 "claimant, the covered event, the causation link, and the adjudication — all "
 "four, or the record is incomplete. It checks that aggregate statistics come "
 "from the administering body rather than secondary reporting, and that "
 "settlement amounts are distinguished from admitted liability. The checklist "
 "keeps insurance documentation honest about what it proves: payment is not "
 "proof of the underlying facts, and the record says so explicitly.",
 ("Four required elements: claimant, covered event, causation link, adjudication",
  "Aggregates must come from the administering body",
  "Settlements distinguished from admitted liability",
  "Payment is not proof of underlying facts — stated explicitly",
  "Incomplete files flagged, not padded",
  "Output: a completeness verdict per claims record"),
 "A complete framework record requires: the four-element schema; source-of-aggregate rule; "
 "settlement-vs-liability distinction; incompleteness handling.",
 ("Signature verification canon — original Signature method",
  "Compatibility: consistent with claims-audit practice"),
 "Original Signature creation — Signature system (Signature Edition).",
 "verify", None),

("sig-public-corroboration", "verification-frameworks",
 "The Signature Public-Report Corroboration Rule",
 "The Signature Public-Report Corroboration Rule is an original Signature "
 "standard for Tier 3 records: no fact enters the archive from a single press "
 "account — every material fact requires two independent reputable sources or "
 "one official source, and single-source facts are marked as such. The rule "
 "defines independence strictly: two outlets repeating one wire report count "
 "as one source. Corroboration status is stored per fact, so the record shows "
 "exactly which claims are well-supported and which rest on thin sourcing.",
 ("Two independent reputable sources per material fact, or one official source",
  "Single-source facts marked as single-source",
  "Independence defined strictly — shared wire copy counts once",
  "Corroboration status stored per fact",
  "Shows which claims are solid and which are thin",
  "Output: a corroboration-graded fact set"),
 "A complete framework record requires: source-independence definition; corroboration grades; "
 "marking rules; per-fact status storage; worked grading description.",
 ("Signature verification canon — original Signature method",
  "Compatibility: consistent with journalistic verification practice"),
 "Original Signature creation — Signature system (Signature Edition).",
 "verify", None),

("sig-fraud-signal", "verification-frameworks",
 "Signature Fraud-Signal Detection Framework",
 "The Signature Fraud-Signal Detection Framework is an original Signature "
 "method for protecting the accident archive from fabricated claims: it "
 "scores each record on anomaly signals — impossible timelines, stock "
 "imagery, duplicated text across supposedly independent sources, claimant "
 "patterns, and statistical outliers — and routes high-scoring records to "
 "manual review. The framework is tuned to catch fraud without punishing "
 "genuine edge cases: signals trigger review, never automatic rejection. It "
 "keeps the insurance-documented tier trustworthy at scale.",
 ("Anomaly signals: timelines, imagery, duplicated text, patterns, outliers",
  "High scores route to manual review",
  "Signals trigger review, never automatic rejection",
  "Tuned to avoid punishing genuine edge cases",
  "Keeps the insurance tier trustworthy at scale",
  "Output: a fraud-risk score with review routing"),
 "A complete framework record requires: signal taxonomy; scoring method; review-routing rules; "
 "false-positive safeguards; reviewer guidance.",
 ("Signature verification canon — original Signature method",
  "Compatibility: consistent with fraud-analytics practice"),
 "Original Signature creation — Signature system (Signature Edition).",
 "stats", None),

("sig-causation-link", "verification-frameworks",
 "Signature Causation-Link Standard",
 "The Signature Causation-Link Standard is an original Signature rule for "
 "what counts as a verified cause in an accident record: a cause is verified "
 "only when the record shows mechanism (how), sequence (when), and exclusion "
 "(why not the alternatives) — all three. Records with mechanism and sequence "
 "but no exclusion are marked 'probable'; records with only correlation are "
 "marked 'associated.' The standard stops the archive from presenting "
 "correlations as causes and makes the strength of every causal claim visible.",
 ("Verified cause requires: mechanism, sequence, and exclusion",
  "Mechanism plus sequence without exclusion: 'probable'",
  "Correlation alone: 'associated' — never 'cause'",
  "Stops correlations from being presented as causes",
  "Causal strength visible on every claim",
  "Output: a graded causal claim"),
 "A complete framework record requires: the three-element rule; grading definitions; "
 "exclusion-documentation method; marking rules; worked grading description.",
 ("Signature verification canon — original Signature method",
  "Compatibility: consistent with epidemiological causation criteria"),
 "Original Signature creation — Signature system (Signature Edition).",
 "causetree", None),

("sig-witness-weighting", "verification-frameworks",
 "Signature Witness-Statement Weighting Method",
 "The Signature Witness-Statement Weighting Method is an original Signature "
 "procedure for using eyewitness accounts in accident records: each statement "
 "is scored on vantage (could the witness see it), immediacy (how soon "
 "recorded), consistency (stable across retellings), and corroboration "
 "(matched by other evidence). High-weight statements can carry facts; "
 "low-weight statements are preserved as color, never as findings. The method "
 "respects witnesses while protecting the record from the well-documented "
 "fallibility of memory under stress.",
 ("Four scores: vantage, immediacy, consistency, corroboration",
  "High-weight statements can carry facts",
  "Low-weight statements preserved as color, never findings",
  "Accounts for memory fallibility under stress",
  "Respects witnesses while protecting the record",
  "Output: a weighted statement set"),
 "A complete framework record requires: the four scoring dimensions; weighting formula; "
 "use rules per weight band; preservation policy for low-weight accounts.",
 ("Signature verification canon — original Signature method",
  "Compatibility: consistent with investigative interviewing research"),
 "Original Signature creation — Signature system (Signature Edition).",
 "investigation", None),

("sig-statistical-claim", "verification-frameworks",
 "Signature Statistical-Claim Verification Rule",
 "The Signature Statistical-Claim Verification Rule is an original Signature "
 "standard for numbers in accident records: every statistic must carry its "
 "source, its coverage (who and when), and its uncertainty — and comparisons "
 "must use like-for-like denominators. A 'percent reduction' without a "
 "baseline, a fatality count without a coverage definition, or a trend "
 "without a time window is rejected at intake. The rule keeps the archive's "
 "numbers honest in a domain where dramatic figures travel faster than "
 "careful ones.",
 ("Every statistic: source, coverage, uncertainty",
  "Comparisons require like-for-like denominators",
  "No baseless percentages, coverless counts, or windowless trends",
  "Rejected at intake if the metadata is missing",
  "Keeps numbers honest where dramatic figures travel fast",
  "Output: a metadata-complete statistical claim"),
 "A complete framework record requires: metadata schema; denominator-matching rules; "
 "rejection criteria; uncertainty-expression guidance.",
 ("Signature verification canon — original Signature method",
  "Compatibility: consistent with statistical reporting standards"),
 "Original Signature creation — Signature system (Signature Edition).",
 "stats", None),

("sig-translation-fidelity", "verification-frameworks",
 "Signature Translation-Fidelity Protocol",
 "The Signature Translation-Fidelity Protocol is an original Signature "
 "procedure for accident records sourced across languages: key findings must "
 "be verified against the original-language document or a certified "
 "translation, machine-translated claims are marked as such, and technical "
 "terms are checked against domain glossaries rather than general "
 "dictionaries. The protocol exists because investigation findings have been "
 "misreported through translation errors — including causal terms with no "
 "exact English equivalent. Fidelity is graded, and low-fidelity translations "
 "cap the record's tier.",
 ("Key findings verified against original or certified translation",
  "Machine-translated claims marked as such",
  "Technical terms checked against domain glossaries",
  "Fidelity graded; low fidelity caps the tier",
  "Addresses real misreporting through translation error",
  "Output: a fidelity-graded multilingual record"),
 "A complete framework record requires: fidelity grades; verification procedure; "
 "glossary requirements; tier-capping rules.",
 ("Signature verification canon — original Signature method",
  "Compatibility: consistent with legal-translation practice"),
 "Original Signature creation — Signature system (Signature Edition).",
 "verify", None),

("sig-update-discipline", "verification-frameworks",
 "Signature Record-Update Discipline",
 "The Signature Record-Update Discipline is an original Signature procedure "
 "for keeping accident records current without rewriting history: new "
 "information is appended as dated updates, superseded facts are marked "
 "superseded rather than deleted, and the tier is re-evaluated on every "
 "material update. The discipline preserves the audit trail — a reader can "
 "see what the record claimed in 2020 and why it changed in 2024. It treats "
 "the archive as a living document with a memory, not a page that gets "
 "quietly edited.",
 ("New information appended as dated updates",
  "Superseded facts marked, never silently deleted",
  "Tier re-evaluated on every material update",
  "Full audit trail preserved",
  "The archive has a memory",
  "Output: a versioned, auditable record"),
 "A complete framework record requires: update schema; supersession marking rules; "
 "tier re-evaluation triggers; audit-trail format; reader guidance.",
 ("Signature verification canon — original Signature method",
  "Compatibility: consistent with archival versioning practice"),
 "Original Signature creation — Signature system (Signature Edition).",
 "timeline", None),

("sig-conflict-resolution", "verification-frameworks",
 "Signature Source-Conflict Resolution Method",
 "The Signature Source-Conflict Resolution Method is an original Signature "
 "procedure for when reputable sources disagree about an accident: the "
 "conflict is documented explicitly with each source's claim and tier, "
 "adjudicated by preferring higher-tier sources and primary evidence, and "
 "left openly unresolved when the evidence does not decide — with the "
 "disagreement itself recorded as a fact about the state of knowledge. The "
 "method forbids silent averaging of conflicting numbers and forbids picking "
 "the most dramatic figure. Uncertainty, documented, beats false precision.",
 ("Conflicts documented with each source's claim and tier",
  "Adjudication prefers higher tiers and primary evidence",
  "Genuinely undecided conflicts left open — recorded as such",
  "No silent averaging; no dramatic-figure picking",
  "Documented uncertainty beats false precision",
  "Output: an adjudicated or openly-unresolved conflict record"),
 "A complete framework record requires: conflict-documentation format; adjudication hierarchy; "
 "open-unresolved marking; forbidden practices; worked conflict description.",
 ("Signature verification canon — original Signature method",
  "Compatibility: consistent with historical method"),
 "Original Signature creation — Signature system (Signature Edition).",
 "investigation", None),

("sig-image-verification", "verification-frameworks",
 "Signature Image-and-Video Verification Standard",
 "The Signature Image-and-Video Verification Standard is an original Signature "
 "procedure for visual evidence in accident records: every image is checked "
 "for provenance (who captured it, when), manipulation (edit detection), and "
 "context (is this the claimed event, place, and time). Reverse-image search, "
 "metadata analysis, and shadow/weather consistency checks are the standard "
 "toolkit. Unverifiable visuals are excluded from the evidentiary record — "
 "they may illustrate, but they may not prove. The standard keeps the "
 "archive's visual layer as rigorous as its textual one.",
 ("Three checks: provenance, manipulation, context",
  "Toolkit: reverse search, metadata, shadow/weather consistency",
  "Unverifiable visuals excluded from evidence — illustrate only",
  "Visual layer as rigorous as the textual layer",
  "Deepfake and misattribution awareness built in",
  "Output: a verified visual-evidence set"),
 "A complete framework record requires: the three-check procedure; toolkit guidance; "
 "illustrate-vs-prove distinction; exclusion rules.",
 ("Signature verification canon — original Signature method",
  "Compatibility: consistent with digital-forensics practice"),
 "Original Signature creation — Signature system (Signature Edition).",
 "verify", None),

("sig-tier-migration", "verification-frameworks",
 "Signature Tier-Migration Protocol",
 "The Signature Tier-Migration Protocol is an original Signature procedure "
 "for records that improve over time: when a publicly-reported record gains "
 "an official investigation report, or an insurance file gains court "
 "validation, the record migrates upward through the tiers with a dated "
 "migration entry recording what changed and why. Migration is never "
 "automatic — a reviewer confirms the new document meets the intake standard "
 "for the higher tier. The protocol lets the archive get more verified over "
 "time while keeping every promotion auditable.",
 ("Upward migration when documentation improves",
  "Dated migration entry: what changed and why",
  "Reviewer confirms intake standard for the higher tier",
  "Never automatic",
  "The archive gets more verified over time",
  "Output: an auditable tier history"),
 "A complete framework record requires: migration triggers; reviewer confirmation; "
 "migration-entry format; tier-history display.",
 ("Signature verification canon — original Signature method",
  "Compatibility: consistent with records-management practice"),
 "Original Signature creation — Signature system (Signature Edition).",
 "reclog", None),

("sig-redaction-balance", "verification-frameworks",
 "Signature Redaction-Balance Doctrine",
 "The Signature Redaction-Balance Doctrine is an original Signature policy "
 "for the tension between documentation and dignity: accident records are "
 "maximally complete on causes, systems, and lessons, and minimally detailed "
 "on victims — aggregate figures, no names beyond the public record, no "
 "graphic description. Redaction decisions are logged with reasons, so the "
 "archive is transparent about what it withholds and why. The doctrine holds "
 "that thoroughness about the accident and restraint about the victims are "
 "not in conflict — they are the same professionalism.",
 ("Maximal on causes, systems, lessons; minimal on victims",
  "Aggregate figures; no names beyond the public record; no graphic detail",
  "Redaction decisions logged with reasons",
  "Transparent about what is withheld and why",
  "Thoroughness and restraint as one professionalism",
  "Output: a documented redaction policy per record"),
 "A complete framework record requires: completeness criteria; restraint rules; "
 "redaction-log format; review procedure.",
 ("Signature verification canon — original Signature method",
  "Compatibility: consistent with journalism ethics standards"),
 "Original Signature creation — Signature system (Signature Edition).",
 "investigation", None),

# ---------------- documentation standards (15) ----------------
("sig-complete-file-standard", "documentation-standards",
 "The Signature Complete-File Standard",
 "The Signature Complete-File Standard is an original Signature specification "
 "for what a finished accident record contains: occurrence data, evidence "
 "inventory, analysis, findings, causal grading, safety outcomes, verification "
 "tier with supporting documents, update history, and citations — nine "
 "sections, each with completeness criteria. A record missing a section is "
 "marked incomplete, never silently short. The standard is the acceptance test "
 "for every record entering the archive: complete files only, with gaps "
 "labeled rather than hidden.",
 ("Nine required sections per finished record",
  "Each section has completeness criteria",
  "Missing sections marked incomplete — never silently short",
  "Gaps labeled, not hidden",
  "The acceptance test for archive entry",
  "Output: a completeness-scored record"),
 "A complete standard record requires: the nine section definitions; completeness criteria; "
 "incomplete-marking rules; acceptance procedure.",
 ("Signature documentation canon — original Signature standard",
  "Compatibility: consistent with archival description standards"),
 "Original Signature creation — Signature system (Signature Edition).",
 "verify", None),

("sig-citation-grammar", "documentation-standards",
 "Signature Citation Grammar",
 "Signature Citation Grammar is an original Signature specification for how "
 "accident records cite sources: every citation names the issuing body, the "
 "document title, the publication status (final, interim, press release), and "
 "the retrieval path or archive location. Citations are machine-checkable — "
 "a validator can confirm each field is present — and human-readable. The "
 "grammar eliminates the vague 'according to reports' sourcing that weakens "
 "public accident documentation, replacing it with citations a reader can "
 "actually follow.",
 ("Every citation: body, title, status, retrieval path",
  "Machine-checkable and human-readable",
  "Eliminates 'according to reports' vagueness",
  "Status marked: final, interim, press release",
  "Citations a reader can actually follow",
  "Output: a validated citation set"),
 "A complete standard record requires: citation field specification; status vocabulary; "
 "validator rules; reader-guidance notes.",
 ("Signature documentation canon — original Signature standard",
  "Compatibility: consistent with scholarly citation practice"),
 "Original Signature creation — Signature system (Signature Edition).",
 "investigation", None),

("sig-naming-convention", "documentation-standards",
 "Signature Record-Naming Convention",
 "The Signature Record-Naming Convention is an original Signature standard "
 "for accident record titles: event name, followed by year, followed by "
 "location or flight identifier where needed for disambiguation — never "
 "sensational epithets, never victim names in titles. The convention makes "
 "records findable, sortable, and dignified. Aliases and common names are "
 "stored as search metadata, not as titles, so 'the Hudson ditching' finds "
 "the record without becoming its name.",
 ("Title pattern: event name, year, disambiguator as needed",
  "No sensational epithets; no victim names in titles",
  "Findable, sortable, dignified",
  "Aliases stored as search metadata, not titles",
  "Common names find records without renaming them",
  "Output: a conformant, searchable title"),
 "A complete standard record requires: title pattern; disambiguation rules; "
 "prohibited elements; alias-metadata schema.",
 ("Signature documentation canon — original Signature standard",
  "Compatibility: consistent with archival naming practice"),
 "Original Signature creation — Signature system (Signature Edition).",
 "verify", None),

("sig-crossreference-map", "documentation-standards",
 "Signature Cross-Reference Map Standard",
 "The Signature Cross-Reference Map Standard is an original Signature "
 "specification for linking related accident records: causal links (this "
 "accident's recommendation addressed that accident's cause), pattern links "
 "(same failure pattern), documentation links (shared sources), and "
 "contrast links (similar events, different outcomes). Each link is typed "
 "and directional, so the archive becomes a navigable graph rather than a "
 "pile of files. The map turns individual records into a body of knowledge "
 "about how accidents repeat and how they are stopped.",
 ("Four link types: causal, pattern, documentation, contrast",
  "Links typed and directional",
  "The archive as a navigable graph",
  "Shows how accidents repeat and how they stop",
  "Links reviewed for accuracy on a schedule",
  "Output: a typed link set per record"),
 "A complete standard record requires: link-type definitions; directionality rules; "
 "review schedule; graph-navigation guidance.",
 ("Signature documentation canon — original Signature standard",
  "Compatibility: consistent with knowledge-graph practice"),
 "Original Signature creation — Signature system (Signature Edition).",
 "causetree", None),

("sig-lesson-extraction", "documentation-standards",
 "Signature Lesson-Extraction Format",
 "The Signature Lesson-Extraction Format is an original Signature "
 "specification for the 'what was learned' section of every record: each "
 "lesson states the finding, the evidence behind it, the action taken (or "
 "not taken), and the measured or expected effect — in that order, every "
 "time. Lessons without evidence are marked as hypotheses; lessons without "
 "actions are marked as open. The format prevents the archive from "
 "collecting platitudes: every lesson is a checkable claim about the world.",
 ("Each lesson: finding, evidence, action, effect — in order",
  "Evidenceless lessons marked as hypotheses",
  "Actionless lessons marked as open",
  "No platitudes: every lesson a checkable claim",
  "Lessons reviewed when new evidence arrives",
  "Output: a checkable lesson set per record"),
 "A complete standard record requires: lesson schema; hypothesis and open marking; "
 "checkability criteria; review triggers.",
 ("Signature documentation canon — original Signature standard",
  "Compatibility: consistent with lessons-learned practice"),
 "Original Signature creation — Signature system (Signature Edition).",
 "reclog", None),

("sig-multilingual-record", "documentation-standards",
 "Signature Multilingual Record Standard",
 "The Signature Multilingual Record Standard is an original Signature "
 "specification for accidents documented in multiple languages: the record "
 "names its primary language, stores key findings in each available language "
 "with fidelity grades, and marks which language version is authoritative for "
 "each section. Discrepancies between language versions are documented as "
 "translation notes, not silently resolved. The standard recognizes that the "
 "authoritative record of many accidents exists first in the investigating "
 "country's language — and treats that as an asset, not an obstacle.",
 ("Primary language named per record",
  "Key findings stored per language with fidelity grades",
  "Authoritative version marked per section",
  "Discrepancies documented as translation notes",
  "Investigating country's language treated as an asset",
  "Output: a multilingual, fidelity-graded record"),
 "A complete standard record requires: language-role schema; fidelity grading; "
 "authority marking; discrepancy-note format.",
 ("Signature documentation canon — original Signature standard",
  "Compatibility: consistent with multilingual archival practice"),
 "Original Signature creation — Signature system (Signature Edition).",
 "verify", None),

("sig-accessibility-standard", "documentation-standards",
 "Signature Record-Accessibility Standard",
 "The Signature Record-Accessibility Standard is an original Signature "
 "specification ensuring accident records serve all readers: plain-language "
 "summaries alongside technical findings, structured data for machine "
 "readers, alt-text for diagrams, and reading-level-graded sections. The "
 "standard holds that a safety lesson locked in jargon is a lesson not yet "
 "taught — the families, journalists, and students who read these records "
 "deserve the same clarity as the engineers. Accessibility is tested, not "
 "assumed, with reader feedback rounds.",
 ("Plain-language summaries beside technical findings",
  "Structured data for machine readers",
  "Alt-text for diagrams; graded reading levels",
  "Safety lessons must be teachable, not just filed",
  "Accessibility tested with reader feedback",
  "Output: a multi-level accessible record"),
 "A complete standard record requires: summary specifications; structured-data schema; "
 "alt-text rules; feedback-test procedure.",
 ("Signature documentation canon — original Signature standard",
  "Compatibility: consistent with accessibility standards"),
 "Original Signature creation — Signature system (Signature Edition).",
 "investigation", None),

("sig-retention-schedule", "documentation-standards",
 "Signature Records-Retention Schedule",
 "The Signature Records-Retention Schedule is an original Signature policy "
 "for how long accident documentation is kept and why: investigation records "
 "are permanent; supporting evidence is kept while the record is active plus a "
 "defined margin; working drafts are kept until superseded and then archived "
 "with their successors. Destruction requires dual authorization and a "
 "destruction log — the archive never quietly loses the ability to check its "
 "own past claims. The schedule treats retention as a promise to future "
 "investigators.",
 ("Investigation records: permanent",
  "Supporting evidence: active life plus margin",
  "Drafts archived with successors, never silently deleted",
  "Destruction needs dual authorization and a log",
  "Retention as a promise to future investigators",
  "Output: a retention-ruled archive"),
 "A complete standard record requires: retention classes; duration rules; "
 "destruction authorization; destruction-log format.",
 ("Signature documentation canon — original Signature standard",
  "Compatibility: consistent with records-management standards"),
 "Original Signature creation — Signature system (Signature Edition).",
 "reclog", None),

("sig-quality-sampling", "documentation-standards",
 "Signature Archive Quality-Sampling Protocol",
 "The Signature Archive Quality-Sampling Protocol is an original Signature "
 "method for keeping a large accident archive honest: on a schedule, a random "
 "sample of records is re-verified end to end — tier checks, citation checks, "
 "fact checks — by reviewers who did not write them. Findings are published "
 "as a quality report with error rates by category, and systematic errors "
 "trigger archive-wide sweeps. The protocol assumes errors exist and finds "
 "them on purpose, which is why the archive's claims can be trusted.",
 ("Scheduled random-sample re-verification",
  "Independent reviewers — never the original authors",
  "Published quality reports with error rates",
  "Systematic errors trigger archive-wide sweeps",
  "Assumes errors exist; finds them on purpose",
  "Output: a measured, published quality level"),
 "A complete standard record requires: sampling method; reviewer-independence rules; "
 "report format; sweep triggers; publication policy.",
 ("Signature documentation canon — original Signature standard",
  "Compatibility: consistent with quality-audit practice"),
 "Original Signature creation — Signature system (Signature Edition).",
 "stats", None),

("sig-api-record-contract", "documentation-standards",
 "Signature Machine-Readable Record Contract",
 "The Signature Machine-Readable Record Contract is an original Signature "
 "specification for accident data as structured data: every record exposes "
 "its fields — identifiers, dates, locations, casualty figures, causal "
 "grading, verification tier, citations — in a stable schema with versioned "
 "field definitions. The contract guarantees backward compatibility: new "
 "fields may be added, existing fields never change meaning. It lets "
 "researchers, journalists, and safety systems build on the archive "
 "programmatically, with the same rigor as the human-readable pages.",
 ("Stable schema with versioned field definitions",
  "New fields may be added; existing fields never change meaning",
  "Backward compatibility guaranteed",
  "Serves researchers, journalists, and safety systems",
  "Same rigor as the human-readable record",
  "Output: a versioned machine-readable record"),
 "A complete standard record requires: schema definition; versioning rules; "
 "compatibility guarantees; consumer guidance.",
 ("Signature documentation canon — original Signature standard",
  "Compatibility: consistent with open-data standards"),
 "Original Signature creation — Signature system (Signature Edition).",
 "investigation", None),

("sig-contributor-code", "documentation-standards",
 "Signature Contributor Code for Accident Records",
 "The Signature Contributor Code is an original Signature policy governing "
 "who may add to the accident archive and how: contributors are identified, "
 "their contributions are attributed and tier-checked, and domain experts "
 "review technical claims before publication. The code welcomes public "
 "contributions — corrections, translations, additional sources — while "
 "holding them to the same verification tiers as staff work. Vandalism and "
 "sensationalism are removed with logged reasons; good-faith errors are "
 "corrected with thanks. The archive grows through trust with verification.",
 ("Contributors identified; contributions attributed",
  "Expert review of technical claims before publication",
  "Public contributions welcome — corrections, translations, sources",
  "Same tiers for contributed and staff work",
  "Vandalism removed with logged reasons; errors corrected with thanks",
  "Output: a governed, growing contributor base"),
 "A complete standard record requires: contributor roles; review workflow; "
 "attribution rules; moderation policy; recognition practice.",
 ("Signature documentation canon — original Signature standard",
  "Compatibility: consistent with open-knowledge governance"),
 "Original Signature creation — Signature system (Signature Edition).",
 "verify", None),

("sig-glossary-standard", "documentation-standards",
 "Signature Accident-Glossary Standard",
 "The Signature Accident-Glossary Standard is an original Signature "
 "specification for the controlled vocabulary of the archive: every technical "
 "term used in records — from 'probable cause' to 'hull loss' — has one "
 "defined meaning, with synonyms mapped and deprecated terms flagged. The "
 "glossary prevents the quiet drift where the same word means different "
 "things in different records, which is how archives become unreliable. Terms "
 "are versioned, and records cite the glossary version they were written "
 "against.",
 ("One defined meaning per technical term",
  "Synonyms mapped; deprecated terms flagged",
  "Prevents semantic drift across records",
  "Terms versioned; records cite glossary version",
  "From 'probable cause' to 'hull loss' — all defined",
  "Output: a versioned controlled vocabulary"),
 "A complete standard record requires: term-entry format; synonym mapping; "
 "deprecation procedure; version-citation rules.",
 ("Signature documentation canon — original Signature standard",
  "Compatibility: consistent with terminology standards"),
 "Original Signature creation — Signature system (Signature Edition).",
 "timeline", None),

("sig-digitization-standard", "documentation-standards",
 "Signature Historical-Document Digitization Standard",
 "The Signature Historical-Document Digitization Standard is an original "
 "Signature specification for bringing paper accident records into the "
 "archive: scanning resolution minimums, OCR with human verification of key "
 "fields, preservation of original pagination, and metadata recording the "
 "physical source's location and condition. Digitized documents carry a "
 "fidelity statement — what was verified against the original and what was "
 "not. The standard ensures the digital archive is a faithful witness to the "
 "paper one, not a degraded copy.",
 ("Scan resolution minimums; OCR with human verification",
  "Original pagination preserved",
  "Physical source location and condition recorded",
  "Fidelity statement per digitized document",
  "The digital archive as faithful witness",
  "Output: a fidelity-stated digital surrogate"),
 "A complete standard record requires: technical specifications; verification workflow; "
 "metadata schema; fidelity-statement format.",
 ("Signature documentation canon — original Signature standard",
  "Compatibility: consistent with digitization best practice"),
 "Original Signature creation — Signature system (Signature Edition).",
 "stats", None),

("sig-ethics-charter", "documentation-standards",
 "Signature Accident-Archive Ethics Charter",
 "The Signature Accident-Archive Ethics Charter is the original Signature "
 "statement of principles governing the whole accident documentation system: "
 "accuracy before speed, dignity before detail, transparency about "
 "uncertainty, independence from interested parties, and service to "
 "prevention. The charter binds every contributor and every automated "
 "process; violations are investigated like any other failure — with "
 "findings and corrective actions published. It is the reason the archive "
 "can be trusted with the worst days of strangers' lives.",
 ("Accuracy before speed; dignity before detail",
  "Transparency about uncertainty",
  "Independence from interested parties",
  "Service to prevention as the purpose",
  "Violations investigated with published findings",
  "Output: a governed, trustworthy archive"),
 "A complete charter record requires: principle statements; binding scope; "
 "violation-investigation procedure; publication requirements.",
 ("Signature documentation canon — original Signature charter",
  "Compatibility: consistent with archival ethics codes"),
 "Original Signature creation — Signature system (Signature Edition).",
 "investigation", None),

("sig-interop-standard", "documentation-standards",
 "Signature Cross-Archive Interoperability Standard",
 "The Signature Cross-Archive Interoperability Standard is an original "
 "Signature specification for exchanging accident records with other "
 "archives: shared identifiers for occurrences, mapped verification tiers, "
 "and conflict flags where archives disagree. The standard lets the "
 "Signature archive federate with official investigation libraries, press "
 "archives, and claims databases without merging their different evidentiary "
 "standards into mush. Each federated record keeps its home archive's tier — "
 "interoperability without false equivalence.",
 ("Shared occurrence identifiers across archives",
  "Mapped verification tiers between systems",
  "Conflict flags where archives disagree",
  "Federation without false equivalence",
  "Each record keeps its home tier",
  "Output: a federated, tier-honest network"),
 "A complete standard record requires: identifier-mapping rules; tier-mapping tables; "
 "conflict-flag format; federation governance.",
 ("Signature documentation canon — original Signature standard",
  "Compatibility: consistent with data-exchange standards"),
 "Original Signature creation — Signature system (Signature Edition).",
 "causetree", None),
]
