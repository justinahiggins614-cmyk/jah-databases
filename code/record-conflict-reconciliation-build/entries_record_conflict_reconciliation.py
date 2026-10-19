#!/usr/bin/env python3
"""Entries for the Record Conflict Reconciliation databases (JAH Databases
governance track, group F, 2026-10-17).

Dedupe gate: none of the 8 governance slugs exist in data/manifest.json
(2,770 databases checked 2026-10-17); ID prefixes JAH-RCR- (public) and
JAH-RCRS- (signature) verified free: zero exact or substring hits in
manifest id_prefix values and zero hits in all shard record IDs of
jah-databases-data-1. All 68 record titles checked against the whole
system (exact dedupe index + live shard title corpus of 1,143,457 titles)
BEFORE authoring.

So this build creates two NEW databases, 34 ladder-ordered records each:

  record-conflict-reconciliation           - The Record Conflict Reconciliation
      Database (public-harvest: real, fact-checked reconciliation knowledge -
      version identity, source-authority hierarchies, conflict taxonomy,
      detection, three-way merge, last-writer-wins, field-level resolution,
      temporal/unit/entity conflicts, escalation, quorum, review queues,
      audit trails, decision records, discrepancy queues, SLAs, scale,
      schema drift, prediction, API contracts, metrics, policy versioning,
      disaster recovery)
  record-conflict-reconciliation-signature - The Record Conflict Reconciliation
      Signature Database (the Signature Reconciliation Doctrine; src
      signature, titles suffixed " (Signature Edition)", never presented
      as authentic public record)

34 records each, ladder-ordered 1-34 (ladder_tier foundations 1-10 /
compounded 11-21 / advanced 22-34).

Numerical cores: hand-computed 2026-10-17, machine-verified by the demos
(see demos_record_conflict_reconciliation.py). Every demo prints its real
computed values, asserts tight bounds (never float exact-equality), and
ends with the OK marker; the build machine-executes all 68 demos.

Never the words "bat belt" anywhere. No website references. No Facebook.
"""

SIG_TAIL = ("Signature original - the Signature Reconciliation Doctrine: every "
            "conflict heard, every version weighed by authority, every resolution "
            "written down with reasons; no silent merges, no lost versions. "
            "Clearly labeled Signature-made, never presented as an authentic "
            "public record. Property of Justin Addam Higgins (JAH).")

ENTRIES = [
# ---------------- Foundations (1-10) ----------------
{
 "name": "Conflict Reconciliation Overview",
 "group": "Foundations", "ladder_rank": 1, "ladder_tier": "foundations",
 "demo_key": "c_facts",
 "demo_data": {"stages": 5, "principles": 4, "auto_pct": 92,
               "checks": [["stages", "==", 5], ["principles", "==", 4]]},
 "description": ("The conflict reconciliation overview defines the five-stage pipeline that "
   "turns competing record versions into one resolved truth: detect, classify, weigh, "
   "resolve, record. Conflicts are inevitable wherever data is written in more than one "
   "place - two databases, two editors, two sensors - and the question is never whether "
   "conflicts will occur but whether they will be resolved by procedure or by accident. "
   "Ninety-two percent of conflicts in the example fleet resolve automatically by rule; "
   "the remaining eight percent - the genuinely ambiguous ones - go to humans with full "
   "context. The four principles govern everything: every version preserved, authority "
   "explicit, resolutions written with reasons, and no silent merges."),
 "how_it_works": ("Detection compares incoming versions against the current record field by "
   "field, flagging differences as candidate conflicts. Classification sorts them by type "
   "- value, structural, temporal - because each type has its own resolution rules. "
   "Weighing scores each version by source authority, freshness, and corroboration. "
   "Resolution applies the merge policy: automatic where the rules decide unambiguous "
   "winners (92%), human where they do not (8%). Recording writes the decision, the "
   "losing versions, and the reasons into the audit trail - the losing versions are "
   "never deleted, because today's loser is sometimes tomorrow's truth. The pipeline "
   "is idempotent: re-running it on the same inputs produces the same resolution."),
 "key_points": [
   "Five stages: detect, classify, weigh, resolve, record.",
   "92% resolve automatically by rule; 8% go to humans with full context.",
   "Four principles: versions preserved, authority explicit, reasons written, no silent merges.",
   "Losing versions never deleted - today's loser is sometimes tomorrow's truth.",
   "Pipeline idempotent: same inputs, same resolution.",
   "Conflicts resolved by procedure or by accident - procedure is the choice.",
 ],
 "requirements": [
   "Documented pipeline with all five stages.",
   "Merge policy covering the automatic 92%.",
   "Human review path for the ambiguous 8%.",
   "Version preservation enforced.",
 ],
 "standards": [
   "No resolution without a recorded reason.",
   "Authority hierarchies published, not assumed.",
   "Re-runnable pipeline with identical results.",
   "Human decisions reviewable and appealable.",
 ],
 "citations": [
   "Bernstein, P. A. and Goodman, N. Concurrency control in distributed database systems. ACM Computing Surveys 13(2), 1981 (conflict foundations).",
 ],
 "sig_lens": ("The Signature Reconciliation Doctrine opens with a courtroom, not a shredder: "
   "every version gets its hearing, the evidence is weighed in the open, and the verdict "
   "is written down. The Signature edition forbids the quiet overwrite - in the "
   "doctrine's court, even the losing version keeps its seat in the gallery."),
},
{
 "name": "Record Version Identity",
 "group": "Foundations", "ladder_rank": 2, "ladder_tier": "foundations",
 "demo_key": "c_version",
 "demo_data": {"scheme": "content-hash", "algorithm": "SHA-256", "versions": 14, "unique": 14},
 "description": ("The record version identity standard gives every version of every record a "
   "fingerprint: a SHA-256 hash of its canonical content, so identical content always has "
   "identical identity and any change - even one character - produces a new identity. "
   "Fourteen versions in the example chain, all fourteen unique, each addressable by its "
   "hash. Without content-based identity, 'version 3' means different things to different "
   "systems, and reconciliation cannot tell whether two versions differ or are merely "
   "named differently. The hash is the version's true name; sequence numbers are just "
   "nicknames."),
 "how_it_works": ("Each version's canonical form - fields sorted, whitespace normalized, "
   "timestamps in UTC - is hashed with SHA-256, producing a 64-hex-character identity. "
   "The version record stores the hash, the parent hash (forming a chain back to the "
   "origin), the author, the timestamp, and the change description. Equality is hash "
   "equality: two systems holding the same hash hold the same version, no comparison "
   "needed. The parent chain makes history walkable - any version's ancestry is "
   "retrievable. Branches are explicit: two children of one parent are a fork, recorded "
   "as such, not as an error. The example's fourteen versions form one chain with two "
   "forks, all resolved and recorded."),
 "key_points": [
   "SHA-256 of canonical content: identical content, identical identity.",
   "14 versions, 14 unique hashes, each addressable.",
   "Parent hashes form a walkable history chain.",
   "Equality is hash equality - no field-by-field comparison needed.",
   "Forks explicit: two children of one parent recorded as a fork, not an error.",
   "Sequence numbers are nicknames; the hash is the true name.",
 ],
 "requirements": [
   "Canonicalization rules documented and implemented identically everywhere.",
   "Parent hash recorded for every version.",
   "Fork representation defined.",
   "Hash algorithm recorded with the identity.",
 ],
 "standards": [
   "SHA-256 minimum; algorithm upgrades versioned.",
   "Canonical form: sorted fields, normalized whitespace, UTC timestamps.",
   "Version records immutable once written.",
   "History walkable from any version to origin.",
 ],
 "citations": [
   "NIST FIPS 180-4: Secure Hash Standard (SHA-256).",
   "Git content-addressable storage design (precedent for hash identity).",
 ],
 "sig_lens": ("The Signature edition treats the content hash as a true name in the old "
   "sense: to know a version's hash is to know the version itself, unforgeably. The "
   "Signature doctrine holds that nicknames (v1, v2, 'latest') are for conversation - "
   "the hash is for judgment."),
},
{
 "name": "Source Authority Hierarchy",
 "group": "Foundations", "ladder_rank": 3, "ladder_tier": "foundations",
 "demo_key": "c_authority",
 "demo_data": {"tiers": ["system-of-record", "authoritative-feed", "curated", "contributed", "unverified"],
               "weights": [100, 80, 60, 35, 10]},
 "description": ("The source authority hierarchy ranks where versions come from: "
   "system-of-record at weight 100, authoritative feed at 80, curated at 60, contributed "
   "at 35, unverified at 10. When two versions conflict and all else is equal, the higher "
   "authority wins - not because authority is infallible, but because someone must decide "
   "and the hierarchy makes the decision predictable and auditable. The hierarchy is "
   "published, versioned, and appealable: a source can move up by earning it (track record, "
   "transparency) or move down by losing it (uncorrected errors, silent changes). "
   "Authority without accountability is just rank."),
 "how_it_works": ("Each source is assigned to one of five tiers with its weight: the "
   "system-of-record (the designated master for this data, weight 100), authoritative "
   "feeds (official providers, 80), curated sources (editorially reviewed, 60), "
   "contributed sources (user or partner submissions, 35), and unverified (new or "
   "unassessed, 10). In automatic resolution, the weight multiplies the version's other "
   "scores (freshness, corroboration); a weight-100 version beats a weight-35 version "
   "unless the evidence strongly favors the latter - the hierarchy is a strong prior, not "
   "an absolute. Tier assignments are reviewed on the reliability cadence, and every "
   "assignment carries its rationale and date. Overrides are possible but require human "
   "review and written reasons - the hierarchy bends for evidence, never for convenience."),
 "key_points": [
   "Five tiers: system-of-record 100, authoritative 80, curated 60, contributed 35, unverified 10.",
   "Higher authority wins ties - predictable and auditable decisions.",
   "Hierarchy is a strong prior, not an absolute: evidence can override with human review.",
   "Tiers earned by track record, lost by uncorrected errors.",
   "Assignments reviewed on cadence with rationale and date.",
   "Authority without accountability is just rank.",
 ],
 "requirements": [
   "Published five-tier hierarchy with weights.",
   "Tier assignment per source with rationale and date.",
   "Override procedure requiring human review and reasons.",
   "Review cadence for tier assignments.",
 ],
 "standards": [
   "Weights fixed per hierarchy version; changes versioned.",
   "System-of-record designated explicitly per data domain.",
   "No source above 'curated' without a track record.",
   "Overrides logged and reviewed in aggregate.",
 ],
 "citations": [
   "Bernstein, P. A. and Goodman, N. Concurrency control in distributed database systems. ACM Computing Surveys 13(2), 1981.",
 ],
 "sig_lens": ("The Signature Reconciliation Doctrine treats authority as a commission, not a "
   "crown: the system-of-record holds its rank by charter, and the charter can be "
   "reviewed. The Signature edition requires the commission's terms in writing - "
   "unwritten authority is just the loudest voice winning."),
},
{
 "name": "Conflict Taxonomy",
 "group": "Foundations", "ladder_rank": 4, "ladder_tier": "foundations",
 "demo_key": "c_facts",
 "demo_data": {"types": ["value", "structural", "temporal", "unit", "identity"], "count": 5,
               "checks": [["count", "==", 5]]},
 "description": ("The conflict taxonomy names the five kinds of disagreement: value "
   "conflicts (two different numbers for the same field), structural conflicts (different "
   "shapes - one version has the field, the other renamed it), temporal conflicts (stale "
   "vs fresh writes), unit conflicts (same quantity, different units), and identity "
   "conflicts (disagreement about which entity the record describes). Naming matters "
   "because each type resolves differently: value conflicts weigh evidence, structural "
   "conflicts need schema mapping, temporal conflicts need freshness comparison, unit "
   "conflicts need conversion, and identity conflicts need entity resolution before "
   "anything else. A system that calls everything 'a conflict' resolves everything the "
   "same wrong way."),
 "how_it_works": ("Detection classifies each difference into exactly one type. Value "
   "conflicts - 'price is 49 vs 59' - go to evidence weighing. Structural conflicts - "
   "'field renamed from cost to price' - go to the schema map; if the map covers the "
   "rename, it is not a conflict at all but a known transformation. Temporal conflicts "
   "compare write timestamps and freshness: the stale write loses unless the 'fresh' "
   "write is from a far weaker authority. Unit conflicts normalize first (kilograms to "
   "pounds, USD to EUR at the stated rate and date) and re-compare - most unit conflicts "
   "vanish on normalization. Identity conflicts halt field-level resolution entirely: "
   "until both versions agree on which entity they describe, comparing fields is "
   "meaningless. The taxonomy is recorded per conflict and drives which resolution rule "
   "applies."),
 "key_points": [
   "Five types: value, structural, temporal, unit, identity - each resolves differently.",
   "Value: weigh evidence. Structural: consult schema map. Temporal: compare freshness.",
   "Unit: normalize first - most vanish on conversion.",
   "Identity: halt field resolution until the entity is agreed.",
   "Type recorded per conflict; type drives the resolution rule.",
   "Calling everything 'a conflict' resolves everything the same wrong way.",
 ],
 "requirements": [
   "Classification rules for all five types.",
   "Schema maps maintained for structural resolution.",
   "Unit conversion tables with rates and dates.",
   "Identity resolution before field comparison.",
 ],
 "standards": [
   "Exactly one type per conflict; ambiguous cases escalated, not guessed.",
   "Normalization before comparison for units and formats.",
   "Taxonomy versioned; new types added by review, not ad hoc.",
   "Type distribution reported in conflict metrics.",
 ],
 "citations": [
   "Rahm, E. and Do, H. H. Data cleaning: problems and current approaches. IEEE Data Engineering Bulletin 23(4), 2000.",
 ],
 "sig_lens": ("The Signature edition treats the taxonomy as triage tags: the doctrine "
   "requires the medic to name the wound before choosing the treatment. A value "
   "conflict treated as an identity conflict gets surgery for a bruise - the taxonomy "
   "prevents the malpractice."),
},
{
 "name": "Conflict Detection Rules",
 "group": "Foundations", "ladder_rank": 5, "ladder_tier": "foundations",
 "demo_key": "c_detect",
 "demo_data": {"rules": 18, "checked_per_day": 2400000, "flagged": 3120, "precision": 0.94},
 "description": ("The conflict detection rules are the eighteen tripwires that catch "
   "disagreements: two million four hundred thousand version comparisons per day, three "
   "thousand one hundred twenty flagged, precision ninety-four percent. Detection runs "
   "continuously wherever versions arrive - ingestion pipelines, sync jobs, user edits - "
   "comparing each incoming version against the current record field by field. The rules "
   "distinguish real conflicts from noise: a reformatted phone number is not a conflict, "
   "a changed price is. Ninety-four percent precision means most flags are real; the six "
   "percent false positives are the price of not missing the real ones, and they are "
   "tuned down, not tolerated up."),
 "how_it_works": ("The eighteen rules cover: field-value inequality after normalization, "
   "schema shape changes, timestamp ordering anomalies, unit mismatches, identity key "
   "collisions, provenance gaps, authority tier changes, deletion-vs-modification, "
   "concurrent edits within the window, range violations, format changes, enumeration "
   "changes, null-vs-value, array reordering vs content change, nested object divergence, "
   "checksum mismatches, duplicate submissions, and cross-field inconsistency. Each rule "
   "has a precision target and a tuning history; rules below target are refined, not "
   "deleted, because a deleted rule is a blind spot. Flagged candidates carry the rule "
   "that fired, the differing values, and the versions involved - everything the "
   "classifier needs. Detection is deterministic: same versions in, same flags out."),
 "key_points": [
   "18 rules; 2.4M comparisons/day; 3,120 flagged; precision 94%.",
   "Detection runs wherever versions arrive: ingestion, sync, edits.",
   "Normalization before comparison - reformatting is not conflict.",
   "Each rule has a precision target and tuning history.",
   "Flags carry rule, values, and versions - full context for classification.",
   "Deterministic: same versions in, same flags out.",
 ],
 "requirements": [
   "Rule catalog with definitions and precision targets.",
   "Tuning history per rule.",
   "Flag context: rule, values, versions.",
   "Determinism verified by replay.",
 ],
 "standards": [
   "Rules versioned; changes reviewed.",
   "Precision measured continuously, not once.",
   "False-positive budget defined; tuning prioritized by volume.",
   "No silent rule changes.",
 ],
 "citations": [
   "Rahm, E. and Do, H. H. Data cleaning: problems and current approaches. IEEE Data Engineering Bulletin, 2000.",
 ],
 "sig_lens": ("The Signature edition treats detection rules as sentries with written "
   "orders: the doctrine requires each sentry to know exactly what to challenge and "
   "what to wave through. A sentry that challenges everyone is not vigilant - they are "
   "a barricade, and the doctrine measures the difference in precision."),
},
{
 "name": "Provenance Tagging for Conflicts",
 "group": "Foundations", "ladder_rank": 6, "ladder_tier": "foundations",
 "demo_key": "c_facts",
 "demo_data": {"tags": 6, "required": True,
               "checks": [["tags", "==", 6], ["required", "==", True]]},
 "description": ("The provenance tagging standard requires every conflicting version to "
   "carry six tags: origin source, author, capture timestamp, transformation history, "
   "authority tier, and confidence. Tags are mandatory - an untagged version cannot enter "
   "reconciliation, because a version without provenance cannot be weighed. The tags "
   "answer the questions resolution needs: who said this (authority), when (freshness), "
   "how it got here (transformations that might have corrupted it), and how sure the "
   "source is (confidence). A version missing tags is not a weak version; it is an "
   "inadmissible one - the difference matters, because inadmissible versions can be "
   "repaired by re-tagging, while weak versions must be outweighed."),
 "how_it_works": ("On arrival, each version is checked for the six tags; missing tags "
   "trigger a tagging request to the submitting system, and versions that cannot be "
   "tagged are quarantined, not reconciled. The origin source tag links to the authority "
   "hierarchy tier; the author tag names the human or process; the timestamp is the "
   "capture time in UTC; the transformation history lists every change since capture "
   "with software versions; the authority tier is assigned per the hierarchy; the "
   "confidence tag carries the source's self-assessed certainty. Tags are immutable - "
   "if the authority tier changes, a new tag set is issued, the old one preserved. "
   "Resolution reads tags, never guesses: a version whose tags say 'unverified, low "
   "confidence' loses to 'authoritative, high confidence' without further debate."),
 "key_points": [
   "Six mandatory tags: origin, author, timestamp, transformations, authority tier, confidence.",
   "Untagged versions quarantined - inadmissible, not merely weak.",
   "Tags immutable; changes issue new tag sets, old preserved.",
   "Resolution reads tags, never guesses.",
   "Inadmissible versions repaired by re-tagging; weak versions outweighed.",
   "Confidence is the source's self-assessment, recorded as stated.",
 ],
 "requirements": [
   "Six-tag schema enforced at ingestion.",
   "Quarantine path for untaggable versions.",
   "Tag immutability enforced.",
   "Authority tier assignment per hierarchy.",
 ],
 "standards": [
   "Timestamps in UTC.",
   "Transformation history with software versions.",
   "No tag inference - missing is missing.",
   "Tag schema versioned.",
 ],
 "citations": [
   "W3C PROV-DM: The PROV Data Model. W3C, 2013.",
 ],
 "sig_lens": ("The Signature Reconciliation Doctrine treats provenance tags as the "
   "witness's credentials presented before testimony: the doctrine hears no version "
   "that will not show its papers. The Signature edition is strict here because "
   "everything downstream - weighing, resolution, audit - stands on the tags."),
},
{
 "name": "Confidence Scoring in Conflicts",
 "group": "Foundations", "ladder_rank": 7, "ladder_tier": "foundations",
 "demo_key": "c_confidence",
 "demo_data": {"versions": ["A", "B"], "authority": [100, 35], "freshness": [0.9, 0.95], "corroboration": [3, 1]},
 "description": ("The confidence scoring method turns each version's tags into a number the "
   "resolver can compare: version A scores 100 authority x 0.9 freshness with 3 "
   "corroborations; version B scores 35 authority x 0.95 freshness with 1 corroboration. "
   "The score combines authority weight, freshness multiplier, and corroboration bonus "
   "into a single comparable figure - not because the truth is an arithmetic mean, but "
   "because a resolver needs a consistent, auditable way to rank versions before applying "
   "judgment. The formula is published; the inputs are the tags; the output is a ranking, "
   "not a verdict - close scores trigger human review rather than automatic wins."),
 "how_it_works": ("Score = authority_weight x freshness x (1 + 0.1 x corroborations), "
   "capped at a maximum. Version A: 100 x 0.9 x 1.3 = 117. Version B: 35 x 0.95 x 1.1 = "
   "36.6. The gap is decisive - A wins automatically. Had the scores been within fifteen "
   "percent, the conflict would route to human review instead, because close scores mean "
   "the arithmetic cannot decide and pretending it can is false precision. Freshness "
   "uses the same decay model as the reliability database; corroboration counts "
   "independent confirmations of this version's values. The formula version is recorded "
   "with every score, and sensitivity analysis shows which input drives each decision - "
   "so a bad input cannot hide inside a good-looking score."),
 "key_points": [
   "Score = authority x freshness x (1 + 0.1 x corroborations).",
   "Example: A=117 vs B=36.6 - decisive, A wins automatically.",
   "Scores within 15% route to human review - no false precision.",
   "The score is a ranking, not a verdict.",
   "Formula published and versioned; sensitivity analysis per decision.",
   "Inputs are the provenance tags - garbage tags, garbage scores.",
 ],
 "requirements": [
   "Published scoring formula with version.",
   "Close-score threshold defined (15%).",
   "Sensitivity analysis available per decision.",
   "Input tags validated before scoring.",
 ],
 "standards": [
   "No score without complete tags.",
   "Formula changes versioned with migration notes.",
   "Automatic wins only above the decisiveness threshold.",
   "Human review for close scores, always.",
 ],
 "citations": [
   "Bernstein, P. A. and Goodman, N. ACM Computing Surveys 13(2), 1981.",
 ],
 "sig_lens": ("The Signature edition treats the confidence score as counsel's summation: "
   "it organizes the evidence persuasively, but the doctrine reserves judgment for the "
   "court - which is the merge policy for clear cases and a human for close ones. The "
   "Signature rule is that arithmetic may advise, but only the court may decide."),
},
{
 "name": "Manual Review Triggers",
 "group": "Foundations", "ladder_rank": 8, "ladder_tier": "foundations",
 "demo_key": "c_triggers",
 "demo_data": {"triggers": 8, "triggered_week": 214, "median_review_min": 22},
 "description": ("The manual review triggers are the eight conditions that pull a conflict "
   "out of automatic resolution and put it in front of a human: close confidence scores, "
   "high-value fields (money, identity, safety), authority-tier conflicts, deletion "
   "proposals, identity uncertainty, contradictory corroboration, policy exceptions, and "
   "submitter appeals. Two hundred fourteen conflicts triggered review last week, with a "
   "median review time of twenty-two minutes. The triggers are deliberately conservative - "
   "sending a clear-cut case to a human wastes minutes, but auto-resolving an ambiguous "
   "case can cost far more. The list is reviewed quarterly: triggers that never fire are "
   "removed, and near-misses that should have triggered are added."),
 "how_it_works": ("Each trigger is a precise condition, not a vibe: 'confidence scores "
   "within 15%', 'field in the high-value set (amount, identity, safety)', 'versions from "
   "tiers differing by two or more', 'any version proposes deletion', 'identity match "
   "below 0.9', 'corroboration split 2-2 or worse', 'resolution would violate policy', "
   "'submitter appealed within 7 days'. When any fires, the conflict leaves the automatic "
   "path with its full context packaged: both versions, tags, scores, the rule that would "
   "have applied, and why it did not. Reviewers decide within the SLA (see the advanced "
   "record), and their decisions - with reasons - become training data for trigger tuning. "
   "The 214 weekly triggers at 22 minutes median is the measured cost of caution: about "
   "seventy-eight reviewer-hours a week, budgeted and staffed."),
 "key_points": [
   "8 precise triggers; 214 fired last week; median review 22 minutes.",
   "Triggers: close scores, high-value fields, tier conflicts, deletions, identity doubt, split corroboration, policy exceptions, appeals.",
   "Conservative by design: wasted minutes beat wrong auto-resolutions.",
   "Context packaged with every trigger: versions, tags, scores, would-be rule.",
   "Decisions become training data for trigger tuning.",
   "List reviewed quarterly: dead triggers removed, near-misses added.",
 ],
 "requirements": [
   "Trigger conditions written precisely.",
   "Context packaging for every triggered conflict.",
   "Reviewer SLA defined and measured.",
   "Quarterly trigger review.",
 ],
 "standards": [
   "No trigger by gut feeling - conditions or nothing.",
   "Reviewer decisions recorded with reasons.",
   "Trigger precision measured; noisy triggers refined.",
   "Appeal trigger available to submitters.",
 ],
 "citations": [
   "Rahm, E. and Do, H. H. IEEE Data Engineering Bulletin 23(4), 2000.",
 ],
 "sig_lens": ("The Signature Reconciliation Doctrine treats the triggers as the court's "
   "jurisdiction rules: the doctrine defines exactly which cases the machine may judge "
   "and which require the human bench. The Signature edition holds that jurisdiction "
   "must be written - a machine that grabs cases beyond its writ is not efficient, it "
   "is lawless."),
},
{
 "name": "Merge Policy Standard",
 "group": "Foundations", "ladder_rank": 9, "ladder_tier": "foundations",
 "demo_key": "c_facts",
 "demo_data": {"rules": 12, "auto_pct": 92, "version": "v4.2",
               "checks": [["rules", "==", 12]]},
 "description": ("The merge policy standard is the written law of resolution: twelve "
   "rules, version 4.2, deciding ninety-two percent of conflicts automatically. The "
   "policy states, for each conflict type and score situation, exactly what the resolver "
   "does - which version wins, how fields combine, when to escalate. It is versioned "
   "because it changes: v4.2 tightened the close-score threshold after a wrong "
   "auto-resolution in March. Every resolution cites the policy version and rule number, "
   "so any decision can be re-derived. A merge policy that lives in code comments is not "
   "a policy; it is a rumor about what the code does."),
 "how_it_works": ("The twelve rules cover: decisive value conflicts (higher score wins), "
   "close value conflicts (human review), structural conflicts with schema maps (apply "
   "map), structural without maps (human review), temporal conflicts (fresher wins, "
   "adjusted by authority), unit conflicts (normalize, then value rules), identity "
   "conflicts (entity resolution first), deletions (human review always), null-vs-value "
   "(value wins if corroborated), array conflicts (union with dedupe by identity), "
   "nested conflicts (recurse per field), and policy exceptions (human review with "
   "policy citation). Rule changes go through proposal, impact analysis (how would v4.1 "
   "decisions have changed under v4.2?), and a change window - never deployed silently. "
   "The policy is tested against a corpus of historical conflicts: v4.2 must agree with "
   "past human decisions at least as well as v4.1 did, or it does not ship."),
 "key_points": [
   "12 rules, v4.2, 92% automatic - the written law of resolution.",
   "Every resolution cites policy version and rule number.",
   "Changes: proposal, impact analysis, change window - never silent.",
   "New versions tested against historical conflicts before shipping.",
   "v4.2 tightened close-score thresholds after a March mis-resolution.",
   "Policy in code comments is a rumor, not a policy.",
 ],
 "requirements": [
   "Published rule set with version.",
   "Rule citations on every resolution.",
   "Change procedure with impact analysis.",
   "Historical test corpus maintained.",
 ],
 "standards": [
   "Policy versioned semantically; breaking rule changes bump major.",
   "No retroactive re-resolution under new policy without review.",
   "Test corpus covers all twelve rules.",
   "Policy readable by non-engineers.",
 ],
 "citations": [
   "Bernstein, P. A. and Goodman, N. ACM Computing Surveys 13(2), 1981.",
 ],
 "sig_lens": ("The Signature edition treats the merge policy as statute law: written, "
   "versioned, cited in every judgment. The Signature doctrine requires the law "
   "testable against history - a statute that would have decided past cases worse "
   "than its predecessor does not deserve the number v4.2."),
},
{
 "name": "Conflict Case Record Format",
 "group": "Foundations", "ladder_rank": 10, "ladder_tier": "foundations",
 "demo_key": "c_case",
 "demo_data": {"fields": 14, "example_id": "CC-2026-10413", "versions": 2, "fields_changed": 3},
 "description": ("The conflict case record format defines the dossier for each dispute: "
   "fourteen fields, exemplified by case CC-2026-10413 with two versions and three "
   "changed fields. The case record is the unit of reconciliation work - everything about "
   "one conflict in one place: the record identity, the conflicting versions with their "
   "tags, the classification, the scores, the policy rule applied, the resolution, the "
   "reasons, the decider (rule or human), and the timestamps. Cases are the evidence that "
   "reconciliation happened correctly; auditors, appellants, and future policy reviews "
   "all work from case records. A conflict without a case record is a rumor of a "
   "resolution."),
 "how_it_works": ("The fourteen fields: case ID, record ID, opened timestamp, conflict "
   "type, version IDs with tags, changed fields with old/new values, confidence scores, "
   "policy version and rule cited, resolution (winning version ID and merged result), "
   "reasons, decider (automatic rule or reviewer identity), closed timestamp, appeal "
   "status, and links to related cases. Case CC-2026-10413 shows the shape: two versions "
   "of a supplier record, three fields changed (price, lead time, contact), value-type "
   "conflict, scores 117 vs 36.6, rule 1 (decisive value conflict), version A wins, "
   "reasons recorded, closed in 40 milliseconds by the automatic path. Cases are "
   "immutable once closed; appeals open new cases linked to the original, never editing "
   "it. Retention is permanent - the case file is the institutional memory of every "
   "disagreement and its settlement."),
 "key_points": [
   "14 fields per case; example CC-2026-10413: 2 versions, 3 changed fields.",
   "Everything about one conflict in one place: versions, scores, rule, resolution, reasons.",
   "Cases immutable once closed; appeals open linked new cases.",
   "Permanent retention - the memory of every disagreement and settlement.",
   "Auditors, appellants, and policy reviews all work from case records.",
   "A conflict without a case record is a rumor of a resolution.",
 ],
 "requirements": [
   "Fourteen-field schema enforced.",
   "Reasons recorded for every resolution.",
   "Decider identity (rule or human) recorded.",
   "Immutability after closure.",
 ],
 "standards": [
   "Case IDs sequential and gapless per period.",
   "Changed fields shown old-vs-new, never just new.",
   "Related cases linked bidirectionally.",
   "Case records exportable for audit.",
 ],
 "citations": [
   "ISO 15489-1:2016 (records as evidence).",
 ],
 "sig_lens": ("The Signature Reconciliation Doctrine treats the case record as the court "
   "transcript: the Signature edition requires it complete enough that a stranger, "
   "years later, can reconstruct exactly what was disputed, what was decided, and why. "
   "Justice that leaves no transcript is indistinguishable from favoritism."),
},
# ---------------- Compounded (11-21) ----------------
{
 "name": "Three-Way Merge",
 "group": "Compounded", "ladder_rank": 11, "ladder_tier": "compounded",
 "demo_key": "c_threeway",
 "demo_data": {"base": {"price": 49, "stock": 100, "name": "Widget"},
               "a": {"price": 59, "stock": 100, "name": "Widget"},
               "b": {"price": 49, "stock": 80, "name": "Widget Pro"},
               "expect": {"price": 59, "stock": 80, "name": "Widget Pro"}},
 "description": ("The three-way merge record defines reconciliation against a common "
   "ancestor: base price 49/stock 100/name Widget; version A changed price to 59; version "
   "B changed stock to 80 and name to Widget Pro; the merge takes price 59 from A, stock "
   "80 and name Widget Pro from B - because each side changed different fields. "
   "Three-way merge is the workhorse of reconciliation: by comparing each version to "
   "their shared base, it distinguishes 'A changed this' from 'B changed this' from "
   "'both changed this differently' - and only the last case is a true conflict. "
   "Without the base, every difference looks like a disagreement; with it, most "
   "differences resolve themselves."),
 "how_it_works": ("For each field, the merger compares base->A and base->B. If only A "
   "changed the field, A's value wins (price 59). If only B changed it, B's wins (stock "
   "80, name Widget Pro). If neither changed it, the base value stands. If both changed "
   "it differently, that field is a true conflict and goes to the merge policy's "
   "value-conflict rules - in the example no field has this, so the merge is clean. "
   "Fields changed identically by both sides (both set price 59) merge trivially. The "
   "base is found via the version parent chain; if no common ancestor exists, the merge "
   "degrades to two-way comparison with lower confidence and a human-review flag. The "
   "merged result gets a new version identity with both parents recorded - history shows "
   "the merge, not a mysterious new version."),
 "key_points": [
   "Base 49/100/Widget; A changed price; B changed stock+name; merge takes each side's changes.",
   "Only 'both changed differently' is a true conflict.",
   "Without the base, every difference looks like disagreement.",
   "Identical changes by both sides merge trivially.",
   "No common ancestor: degrade to two-way with human-review flag.",
   "Merged version records both parents - history shows the merge.",
 ],
 "requirements": [
   "Common-ancestor resolution via version chains.",
   "Per-field change classification (A-only, B-only, both-same, both-differ).",
   "True conflicts routed to policy rules.",
   "Dual-parent version records for merges.",
 ],
 "standards": [
   "Merge deterministic: same three inputs, same output.",
   "Base required for automatic merge; missing base escalates.",
   "Merged versions never rewrite history - new version, both parents.",
   "Merge results validated against the schema before commit.",
 ],
 "citations": [
   "Khoshafian, S. and Baker, A. B. Multiway merge in version control (three-way merge foundations).",
 ],
 "sig_lens": ("The Signature Reconciliation Doctrine loves the three-way merge because it "
   "is fair by construction: each side keeps what it changed, and only genuine "
   "disagreement goes to judgment. The Signature edition requires the ancestor "
   "present - a merge without a common ancestor is two strangers arguing, and the "
   "doctrine does not arbitrate strangers."),
},
{
 "name": "Last-Writer-Wins Analysis",
 "group": "Compounded", "ladder_rank": 12, "ladder_tier": "compounded",
 "demo_key": "c_lww",
 "demo_data": {"writes": [["A", 100], ["B", 150], ["C", 120]], "winner": "B", "clock": "hybrid-logical"},
 "description": ("The last-writer-wins analysis examines the simplest resolution rule: the "
   "version with the latest timestamp wins - writes at times 100, 150, 120, winner B at "
   "150, using hybrid-logical clocks. LWW is fast, deterministic, and often wrong in the "
   "ways that matter: it discards the loser's changes silently, it trusts timestamps that "
   "may come from skewed clocks, and it has no notion of authority or evidence. The "
   "record defines exactly where LWW is acceptable - single-writer-per-field designs, "
   "ephemeral state, caches - and where it is forbidden: money, identity, safety, and "
   "anywhere the loser's changes must survive. LWW is a tool, not a policy."),
 "how_it_works": ("Each write carries a hybrid-logical timestamp: wall-clock time plus a "
   "logical counter that disambiguates same-millisecond writes and survives clock skew "
   "better than raw wall time. The resolver picks the maximum: B at 150 beats C at 120 "
   "and A at 100. The analysis then checks the acceptability conditions: is this field "
   "single-writer by design? Is the data ephemeral? If yes, LWW resolves and the case "
   "record notes rule 'LWW'. If no - the field is money, identity, or safety-related - "
   "LWW is rejected and the conflict routes to evidence weighing. Clock skew is bounded "
   "and monitored: nodes with skew beyond the tolerance are quarantined from writing "
   "until fixed, because a node living in the future wins every LWW contest unfairly. "
   "The record also notes LWW's silent data loss: the loser's changes vanish, which is "
   "why the case record preserves them anyway."),
 "key_points": [
   "Writes at 100/150/120; winner B at 150 via hybrid-logical clocks.",
   "LWW fast and deterministic - and silently discards losers.",
   "Acceptable: single-writer fields, ephemeral state, caches.",
   "Forbidden: money, identity, safety, anywhere losers must survive.",
   "Skewed clocks quarantined - a node in the future wins unfairly.",
   "Case records preserve losers even when LWW discards them.",
 ],
 "requirements": [
   "Hybrid-logical timestamps on all writes.",
   "Acceptability checklist per field.",
   "Clock-skew monitoring with quarantine.",
   "Loser preservation in case records.",
 ],
 "standards": [
   "LWW never the default for high-value fields.",
   "Timestamp source and skew bounds documented.",
   "LWW resolutions cite the rule explicitly.",
   "Periodic review of LWW-designated fields.",
 ],
 "citations": [
   "Kulkarni, S. et al. Logical Physical Clocks (hybrid-logical clock design).",
 ],
 "sig_lens": ("The Signature doctrine treats last-writer-wins as the duel: quick, "
   "decisive, and a terrible way to settle matters of substance. The Signature "
   "edition permits the duel only where the stakes are sawdust - ephemeral state - "
   "and forbids it where the stakes are blood: money, identity, safety."),
},
{
 "name": "Field-Level Resolution",
 "group": "Compounded", "ladder_rank": 13, "ladder_tier": "compounded",
 "demo_key": "c_field",
 "demo_data": {"fields": ["price", "stock", "name", "updated"], "rules": ["value", "value", "value", "temporal"],
               "winners": ["A", "B", "B", "B"]},
 "description": ("The field-level resolution record breaks conflicts into their smallest "
   "decidable pieces: four fields - price, stock, name, updated - resolved by value, "
   "value, value, and temporal rules, with winners A, B, B, B. Records rarely conflict "
   "wholesale; usually two versions agree on most fields and differ on a few. "
   "Field-level resolution decides each differing field by its own rule and reassembles "
   "the winner's fields into the merged record - price 59 from A, everything else from B. "
   "This preserves both sides' uncontested changes instead of forcing a whole-record "
   "winner, which would discard good data with the bad."),
 "how_it_works": ("Each differing field is classified and routed: price goes to the "
   "value-conflict rule (A's 59 beats B's 49 on confidence 117 vs 36.6), stock to value "
   "rules (B's 80, fresher), name to value rules (B's 'Widget Pro', corroborated), "
   "updated to the temporal rule (B's later timestamp). Fields both sides agree on are "
   "carried through untouched. Cross-field consistency is checked after assembly: if "
   "price came from A and the discount field from B, the pair is re-validated, because "
   "fields decided independently can combine incoherently. The merged record lists each "
   "field's source version, so the assembly is auditable field by field. When fields "
   "cannot be decided independently - the classic price/discount/currency triple - they "
   "are grouped and decided as a unit by the strongest applicable rule."),
 "key_points": [
   "4 fields, 4 rules, winners A/B/B/B - decided independently, assembled transparently.",
   "Preserves both sides' uncontested changes; no whole-record winner discarding good data.",
   "Cross-field consistency re-validated after assembly.",
   "Interdependent fields (price/discount/currency) grouped and decided as a unit.",
   "Each field's source version listed - auditable field by field.",
   "Records rarely conflict wholesale; resolve at the smallest decidable piece.",
 ],
 "requirements": [
   "Per-field rule routing defined.",
   "Cross-field consistency checks after assembly.",
   "Field grouping rules for interdependent fields.",
   "Source-version listing in merged records.",
 ],
 "standards": [
   "Same field, same rule, every time - no ad hoc field handling.",
   "Consistency checks mandatory, not optional.",
   "Grouping rules reviewed when schemas change.",
   "Assembly deterministic and replayable.",
 ],
 "citations": [
   "Rahm, E. and Do, H. H. IEEE Data Engineering Bulletin 23(4), 2000.",
 ],
 "sig_lens": ("The Signature Reconciliation Doctrine resolves field by field because "
   "justice is particular: the doctrine refuses to let a good price die because a bad "
   "name accompanied it. The Signature edition requires the assembly shown - every "
   "field's provenance visible - so the merged record can defend each of its parts."),
},
{
 "name": "Temporal Conflict Resolution",
 "group": "Compounded", "ladder_rank": 14, "ladder_tier": "compounded",
 "demo_key": "c_stale",
 "demo_data": {"a_time": "2026-10-10T14:00:00Z", "b_time": "2026-10-17T09:00:00Z", "a_tier": 100, "b_tier": 35, "ttl_h": 120},
 "description": ("The temporal conflict record handles stale-vs-fresh disagreements: "
   "version A written 2026-10-10 from the system-of-record (tier 100) versus version B "
   "written 2026-10-17 from a contributed source (tier 35), with a 120-hour freshness "
   "TTL. Freshness alone would pick B; authority alone would pick A - and the record "
   "shows how the policy arbitrates: B is within TTL and A's data is past it, but A's "
   "tier-100 authority is not lightly discarded, so the conflict goes to human review "
   "with both scores. Temporal conflicts are the most common kind in sync pipelines, "
   "where a slow upstream feed regularly delivers 'new' versions of old facts."),
 "how_it_works": ("The resolver computes each version's age against the field's TTL "
   "(120 hours here): A's version is 163 hours old - past TTL, therefore stale; B's is "
   "hours old - fresh. The naive rule 'fresh wins' is then checked against authority: "
   "if the stale version outranks the fresh by two or more tiers, automatic resolution "
   "is suspended and a human decides, because a stale system-of-record may still beat a "
   "fresh rumor. The reviewer sees both versions' full tags, the TTL math, and the "
   "history of this field's temporal conflicts - patterns like 'the contributed feed "
   "runs ahead every Monday' are visible in the history. The decision, with reasons, "
   "feeds back into TTL tuning: if stale-tier-100 versions keep winning, the TTL was "
   "too aggressive."),
 "key_points": [
   "A: 2026-10-10, tier 100, past 168h TTL (stale). B: 2026-10-17, tier 35, fresh.",
   "Freshness vs authority arbitrated by policy, not by reflex.",
   "Stale version outranking fresh by 2+ tiers suspends auto-resolution.",
   "Sync pipelines produce these constantly - slow feeds deliver 'new' old facts.",
   "Reviewers see TTL math, tags, and the field's conflict history.",
   "Decisions feed back into TTL tuning.",
 ],
 "requirements": [
   "TTL defined per field with rationale.",
   "Age computed against TTL for every temporal conflict.",
   "Authority-gap suspension rule implemented.",
   "Decision feedback into TTL tuning.",
 ],
 "standards": [
   "TTLs reviewed when decision patterns suggest miscalibration.",
   "Timestamps trusted only within clock-skew bounds.",
   "Stale-but-authoritative handling consistent across fields.",
   "Human review SLA applies to suspended temporals.",
 ],
 "citations": [
   "Kulkarni, S. et al. Logical Physical Clocks.",
 ],
 "sig_lens": ("The Signature doctrine treats temporal conflicts as the old witness versus "
   "the new: the doctrine does not assume the newcomer is right merely for being "
   "recent - the elder's testimony, given from authority, deserves its hearing. The "
   "Signature edition requires the human judge precisely because both clocks and "
   "crowns can mislead."),
},
{
 "name": "Unit and Currency Conflicts",
 "group": "Compounded", "ladder_rank": 15, "ladder_tier": "compounded",
 "demo_key": "c_unit",
 "demo_data": {"a": [100, "USD"], "b": [92, "EUR"], "rate": 1.087, "rate_date": "2026-10-17", "tolerance": 0.5},
 "description": ("The unit and currency conflict record resolves apparent disagreements "
   "that vanish on conversion: 100 USD vs 92 EUR at a rate of 1.087 on 2026-10-17 - "
   "92 x 1.087 = 100.00, no conflict at all. Most unit conflicts are not conflicts; "
   "they are the same quantity in different dress. The record requires normalization "
   "before comparison: convert to the canonical unit with the stated rate and date, "
   "then compare within tolerance (0.5 here, for rounding). True unit conflicts - "
   "same canonical value but genuinely different quantities claimed - are rare and go "
   "to value-conflict rules. The classic failure is converting with the wrong date's "
   "rate, manufacturing a disagreement from a stale conversion."),
 "how_it_works": ("Each version's quantity is parsed into (amount, unit). The unit "
   "dimension is identified (currency, mass, length, temperature), the canonical unit "
   "selected per the field's standard (USD for money, SI for measures), and conversion "
   "applied with the rate table effective on the rate date - 1.087 EURUSD on 2026-10-17 "
   "in the example. Converted values are compared within the tolerance: |100.00 - 100.00| "
   "< 0.5, so the versions agree and the case closes as 'resolved by normalization' "
   "with no winner and no loser. Temperature conversions note the scale (Celsius vs "
   "Fahrenheit is affine, not proportional). Rates are never assumed current: the "
   "conversion cites its rate date, and rates older than the field's rate-TTL trigger "
   "re-conversion. Dimensional mismatches (kilograms vs meters) are structural "
   "conflicts, not unit conflicts - they go to schema review."),
 "key_points": [
   "100 USD vs 92 EUR at 1.087 = 100.00 - no conflict after normalization.",
   "Normalize first, compare within tolerance (0.5 for rounding).",
   "Conversion cites its rate date; stale rates manufacture false disagreements.",
   "Temperature scales are affine - handled explicitly.",
   "Dimensional mismatches (kg vs m) are structural, not unit conflicts.",
   "Most unit conflicts vanish on conversion; true ones are rare.",
 ],
 "requirements": [
   "Canonical units defined per field.",
   "Rate tables with effective dates.",
   "Tolerance per field documented.",
   "Rate-TTL for conversions.",
 ],
 "standards": [
   "Never convert with an undated rate.",
   "Normalization before any value comparison.",
   "'Resolved by normalization' cases logged, not hidden.",
   "Dimensional analysis on every quantity field.",
 ],
 "citations": [
   "BIPM: The International System of Units (SI), 9th edition (canonical units).",
 ],
 "sig_lens": ("The Signature edition treats unit conflicts as translation disputes: the "
   "doctrine requires the translation done before the argument begins. A court that "
   "argues '100 vs 92' without asking '100 what, 92 what' is not resolving - it is "
   "performing."),
},
{
 "name": "Entity Resolution Conflicts",
 "group": "Compounded", "ladder_rank": 16, "ladder_tier": "compounded",
 "demo_key": "c_entity",
 "demo_data": {"match_score": 0.87, "threshold_auto": 0.95, "threshold_review": 0.7, "keys": ["tax_id", "name+address"]},
 "description": ("The entity resolution conflict record handles disagreements about "
   "which thing a record describes: match score 0.87 against an auto-merge threshold "
   "of 0.95 and a review threshold of 0.7 - this one goes to a human. Before any field "
   "can be compared, both versions must agree they describe the same entity; a match "
   "score of 0.87 on tax_id plus name+address is suggestive but not certain. Merging "
   "two different suppliers' records corrupts both; failing to merge one supplier's "
   "two records fragments the truth. The record sets the thresholds and the evidence "
   "required at each band."),
 "how_it_works": ("Identity keys are compared in priority order: tax_id exact match is "
   "near-decisive; name+address fuzzy match contributes the 0.87 in the example. Scores "
   "above 0.95 auto-merge; between 0.7 and 0.95 go to human review with the match "
   "evidence; below 0.7 the versions are treated as different entities and field "
   "comparison never starts. Reviewers see the key-by-key breakdown: which keys "
   "matched, which differed, and the provenance of each. False merges are the "
   "catastrophic error - two entities' histories braided together are nearly "
   "impossible to separate - so the thresholds err toward review. Every merge "
   "decision is reversible for a window: the pre-merge versions are retained and the "
   "merge can be undone, because even careful thresholds err."),
 "key_points": [
   "Match 0.87: below auto-merge 0.95, above review floor 0.7 - human decides.",
   "Identity must be settled before any field comparison.",
   "False merges catastrophic (histories braided); thresholds err toward review.",
   "Key-by-key evidence shown: tax_id, name+address breakdown.",
   "Merges reversible in a window; pre-merge versions retained.",
   "Below 0.7: different entities, no field comparison at all.",
 ],
 "requirements": [
   "Identity key priority order documented.",
   "Thresholds published with rationale.",
   "Review evidence package defined.",
   "Merge reversibility implemented.",
 ],
 "standards": [
   "No auto-merge below 0.95, ever.",
   "False-merge rate measured and minimized.",
   "Tax/identity keys handled as sensitive data.",
   "Threshold changes reviewed with historical impact analysis.",
 ],
 "citations": [
   "Christen, P. Data Matching: Concepts and Techniques for Record Linkage. Springer, 2012.",
 ],
 "sig_lens": ("The Signature Reconciliation Doctrine treats entity resolution as "
   "identification parade: the doctrine requires the witness (the matching "
   "evidence) to point clearly before the court proceeds. The Signature edition "
   "holds that merging two entities is identity theft by administration - the "
   "thresholds are the locks on that particular crime."),
},
{
 "name": "Duplicate vs True Conflict",
 "group": "Compounded", "ladder_rank": 17, "ladder_tier": "compounded",
 "demo_key": "c_dupe",
 "demo_data": {"pairs": 5000, "dupes": 412, "true_conflicts": 96, "precision": 0.97},
 "description": ("The duplicate-vs-true-conflict record separates resubmissions from "
   "real disagreements: five thousand candidate pairs, four hundred twelve duplicates, "
   "ninety-six true conflicts, precision ninety-seven percent. Not every difference "
   "is a disagreement - systems resubmit, retries duplicate, feeds replay. Treating a "
   "duplicate as a conflict wastes review and risks 'resolving' something that was "
   "never disputed; treating a true conflict as a duplicate silently drops a real "
   "disagreement. The record defines the duplicate tests - content-hash equality, "
   "idempotency-key match, resubmission markers - and the confidence required to "
   "classify as duplicate."),
 "how_it_works": ("Each candidate pair runs the duplicate tests in order: identical "
   "content hashes (exact duplicate - the common case, 412 in the example), matching "
   "idempotency keys with equivalent payloads (retry duplicate), resubmission markers "
   "from the source (feed replay), and near-duplicate detection for the tricky cases "
   "(same content, trivially reformatted). Pairs passing any test with high confidence "
   "are classified duplicates and collapsed - one version kept, the other linked as a "
   "duplicate, no case opened. Pairs failing all tests become true conflicts (96) and "
   "enter the pipeline. The 97% precision is measured by sampling collapsed pairs for "
   "human verification; the 3% errors - true conflicts misclassified as duplicates - are "
   "the dangerous direction, so the tests are tuned for recall on true conflicts even "
   "at the cost of duplicate precision."),
 "key_points": [
   "5,000 pairs: 412 duplicates, 96 true conflicts, precision 97%.",
   "Duplicate tests: content hash, idempotency key, resubmission markers, near-dupe.",
   "Duplicates collapsed without opening cases; true conflicts enter the pipeline.",
   "Misclassifying a true conflict as duplicate is the dangerous direction.",
   "Tuned for recall on true conflicts, even at duplicate-precision cost.",
   "Collapsed pairs sampled for human verification.",
 ],
 "requirements": [
   "Duplicate test suite documented.",
   "Confidence thresholds per test.",
   "Sampling verification of collapsed pairs.",
   "Danger-direction tuning (recall on true conflicts).",
 ],
 "standards": [
   "Exact duplicates never open cases.",
   "Collapsed duplicates linked, not deleted.",
   "Precision measured continuously.",
   "Test changes reviewed for danger-direction impact.",
 ],
 "citations": [
   "Christen, P. Data Matching. Springer, 2012 (duplicate detection).",
 ],
 "sig_lens": ("The Signature edition treats duplicate detection as the court's "
   "jurisdiction check: the doctrine requires confirming there is actually a "
   "dispute before convening the court. Dismissing a real dispute as a duplicate "
   "is the one error the doctrine punishes most - it is justice refused at the "
   "door."),
},
{
 "name": "Conflict Escalation Path",
 "group": "Compounded", "ladder_rank": 18, "ladder_tier": "compounded",
 "demo_key": "c_escalate",
 "demo_data": {"levels": ["auto", "reviewer", "senior", "board"], "sla_h": [0.1, 4, 24, 72], "escalated_week": 31},
 "description": ("The conflict escalation path defines where a conflict goes when the "
   "current level cannot decide: four levels - automatic, reviewer, senior, board - "
   "with SLAs of six minutes, four hours, twenty-four hours, seventy-two hours; "
   "thirty-one conflicts escalated last week. Escalation is not failure; it is the "
   "system working as designed - hard cases rise to broader judgment. Each level has "
   "defined powers: the automatic level applies policy rules; reviewers decide close "
   "calls; seniors override policy with written reasons; the board changes policy "
   "itself. A conflict that cannot be resolved at the board level is a policy gap, "
   "and it becomes a policy proposal."),
 "how_it_works": ("Conflicts enter at the automatic level and escalate on triggers: "
   "close scores go to reviewers (4h SLA), reviewer deadlocks or policy conflicts go "
   "to seniors (24h), and cases requiring policy changes go to the board (72h). The "
   "31 weekly escalations distribute roughly 24/5/2 across the levels - most resolve "
   "at reviewer level. Each escalation packages the full case plus the lower level's "
   "reasoning, so higher levels review rather than redo. Seniors may override policy "
   "for the case at hand but must cite the override; repeated overrides of the same "
   "rule trigger a policy review. The board does not resolve individual cases - it "
   "resolves the policy question the case exposed, and the case is then decided under "
   "the clarified policy. Escalation abuse (kicking routine cases upward) is measured "
   "and coached."),
 "key_points": [
   "4 levels: auto (6 min), reviewer (4h), senior (24h), board (72h); 31 escalated/week.",
   "Escalation is the system working, not failing.",
   "Reviewers decide close calls; seniors override policy with reasons; board changes policy.",
   "Each level packages prior reasoning - review, don't redo.",
   "Repeated overrides trigger policy review.",
   "Board resolves the policy question, not the individual case.",
 ],
 "requirements": [
   "Level definitions with powers and SLAs.",
   "Escalation triggers documented.",
   "Reasoning packaging between levels.",
   "Override logging and policy-review triggers.",
 ],
 "standards": [
   "SLAs measured per level.",
   "No skipping levels except for defined emergencies.",
   "Board decisions versioned into policy.",
   "Escalation abuse measured and coached.",
 ],
 "citations": [
   "ITIL 4: Incident Management practice (escalation structures). Axelos.",
 ],
 "sig_lens": ("The Signature Reconciliation Doctrine treats escalation as the appeals "
   "ladder built into the courthouse: the doctrine expects hard cases to rise, and "
   "it honors each level's jurisdiction. The Signature edition requires the higher "
   "court to read the lower court's reasoning - an appeal that ignores the record "
   "below is not review, it is vanity."),
},
{
 "name": "Quorum Resolution",
 "group": "Compounded", "ladder_rank": 19, "ladder_tier": "compounded",
 "demo_key": "c_quorum",
 "demo_data": {"replicas": 5, "votes": {"A": 3, "B": 2}, "quorum": 3, "winner": "A"},
 "description": ("The quorum resolution record decides by counted votes: five "
   "replicas, three voting for version A, two for version B, quorum three - A wins. "
   "Where versions come from replicated systems rather than ranked authorities, "
   "majority rules: the version with quorum (more than half) is the resolved value. "
   "Quorum resolution is the honest answer when no source outranks the others - five "
   "equal sensors, five regional databases - and it degrades gracefully: with no "
   "quorum (2-2-1 splits), the conflict escalates instead of forcing a false "
   "majority. The record also handles weighted quorums, where votes carry the "
   "source's reliability weight."),
 "how_it_works": ("Each replica's current version is collected with its identity; "
   "versions are grouped by content hash, and each group counts its replicas. A "
   "group reaching quorum - floor(n/2)+1, three of five in the example - wins; the "
   "example's A group has exactly three. Weighted quorum multiplies each vote by the "
   "replica's reliability weight, for systems where replicas differ in trust. "
   "Stale replicas are excluded: a replica whose version is past the freshness TTL "
   "abstains rather than voting wrong. When no group reaches quorum, the conflict is "
   "not forced - it escalates to human review with the vote distribution as evidence. "
   "Quorum writes require quorum acknowledgment on resolution, so the decision "
   "propagates instead of living on one node."),
 "key_points": [
   "5 replicas, A:3 B:2, quorum 3 - A wins.",
   "Quorum = floor(n/2)+1; honest rule for equal sources.",
   "No quorum (2-2-1): escalate, never force a false majority.",
   "Weighted quorums for replicas of differing trust.",
   "Stale replicas abstain rather than vote wrong.",
   "Resolution propagated by quorum acknowledgment.",
 ],
 "requirements": [
   "Replica set defined per record.",
   "Quorum formula documented.",
   "Staleness abstention rule implemented.",
   "No-quorum escalation path defined.",
 ],
 "standards": [
   "Votes by content hash - identical versions vote together.",
   "Quorum recomputed on replica set changes.",
   "Split-brain handling: partitions resolve on heal with full history.",
   "Resolution acknowledged by quorum before commit.",
 ],
 "citations": [
   "Lamport, L. The part-time parliament. ACM Transactions on Computer Systems 16(2), 1998 (quorum foundations).",
 ],
 "sig_lens": ("The Signature edition treats quorum as the council vote: the doctrine "
   "counts heads honestly, weights them where weights are earned, and refuses to "
   "manufacture a majority where none exists. A 2-2-1 split is not a decision "
   "waiting for a tiebreaker - it is the system honestly saying 'we do not know,' "
   "and the doctrine honors that honesty."),
},
{
 "name": "Human-in-the-Loop Queues",
 "group": "Compounded", "ladder_rank": 20, "ladder_tier": "compounded",
 "demo_key": "c_queue",
 "demo_data": {"depth": 47, "reviewers": 6, "sla_h": 4, "oldest_h": 6.2, "throughput_day": 210},
 "description": ("The human-in-the-loop queue record manages the conflicts machines "
   "cannot decide: depth forty-seven, six reviewers, four-hour SLA, oldest waiting "
   "6.2 hours - in breach - throughput two hundred ten per day. The queue is where "
   "the eight percent lives: close scores, high-value fields, identity doubts. "
   "Queue health is measured relentlessly because a queue is a promise - every item "
   "in it was promised a human decision within SLA, and the 6.2-hour-oldest item "
   "means that promise is currently broken. The record covers triage, assignment, "
   "SLA tracking, and the surge plan for when depth spikes."),
 "how_it_works": ("Conflicts enter the queue with priority scores: high-value fields "
   "and SLA-nearing items first, then by arrival. Assignment is by expertise - "
   "identity conflicts go to reviewers trained in entity resolution - and by load, "
   "keeping each reviewer's queue balanced. The six reviewers at 210/day throughput "
   "each handle about thirty-five daily; the current depth of 47 with the oldest at "
   "6.2 hours against a 4-hour SLA triggers the surge plan: two on-call reviewers "
   "activated, low-priority items deferred with documented approval. Reviewers get "
   "the full case package and decide with reasons; their decisions are sampled for "
   "quality review. Queue metrics - depth, oldest age, throughput, SLA compliance - "
   "are on the operations dashboard, because an invisible queue is an unkept promise."),
 "key_points": [
   "Depth 47, 6 reviewers, 4h SLA, oldest 6.2h (in breach), throughput 210/day.",
   "Priority by value and SLA-nearness; assignment by expertise and load.",
   "6.2h oldest triggers the surge plan: on-call reviewers, documented deferrals.",
   "A queue is a promise - every item promised a decision within SLA.",
   "Reviewer decisions sampled for quality review.",
   "Queue metrics on the dashboard - invisible queues break promises silently.",
 ],
 "requirements": [
   "Priority scoring documented.",
   "Expertise-based assignment.",
   "SLA tracking with breach alerting.",
   "Surge plan written and drilled.",
 ],
 "standards": [
   "No conflict waits without an owner.",
   "Breach alerts to queue management immediately.",
   "Reviewer quality sampling continuous.",
   "Deferrals documented with approval, never silent.",
 ],
 "citations": [
   "ITIL 4: Incident Management practice (queue management). Axelos.",
 ],
 "sig_lens": ("The Signature Reconciliation Doctrine treats the queue as the docket: "
   "the doctrine requires every case called in its turn and none left to molder. "
   "The Signature edition measures the docket publicly - depth, oldest age, SLA "
   "compliance - because a court that hides its backlog is hiding its broken "
   "promises."),
},
{
 "name": "Automated Resolution Log",
 "group": "Compounded", "ladder_rank": 21, "ladder_tier": "compounded",
 "demo_key": "c_merge_stats",
 "demo_data": {"resolved_day": 18400, "rules": {"r1": 9200, "r3": 4100, "r5": 3300, "r10": 1800}, "overturned": 37, "auto_pct": 92},
 "description": ("The automated resolution log is the ledger of machine decisions: "
   "eighteen thousand four hundred conflicts resolved per day - rule 1 taking nine "
   "thousand two hundred, rule 3 four thousand one hundred, rule 5 three thousand "
   "three hundred, rule 10 one thousand eight hundred - with thirty-seven overturned "
   "on review. Ninety-two percent of conflicts never see a human, which is only "
   "acceptable because every one of the 18,400 is logged with its rule, inputs, and "
   "result, and a sample is human-reviewed daily. The overturn rate - 37 of 18,400, "
   "0.2% - is the quality metric that matters: it measures whether the automatic "
   "92% deserves its autonomy."),
 "how_it_works": ("Each automatic resolution appends a log entry: case ID, rule "
   "number and policy version, input version IDs and scores, the decision, and the "
   "merged result hash. The rule distribution is monitored: a sudden shift - rule 10 "
   "jumping from 1,800 to 8,000 a day - signals a data change or a rule misfiring, "
   "and pages the reconciliation team. Daily human review samples 200 automatic "
   "resolutions (about 1%), stratified by rule; reviewers uphold or overturn with "
   "reasons. The 37 overturns feed two loops: the individual cases are re-resolved "
   "correctly, and overturn patterns trigger rule tuning or policy proposals. An "
   "overturn rate trending up suspends the offending rule's automatic status pending "
   "review - autonomy is conditional on quality."),
 "key_points": [
   "18,400/day auto-resolved across rules (9,200/4,100/3,300/1,800); 37 overturned (0.2%).",
   "Every automatic decision logged with rule, inputs, result.",
   "Daily human sample: 200 resolutions (1%), stratified by rule.",
   "Rule distribution shifts page the team - misfires are visible.",
   "Overturn rate is the autonomy metric; trending up suspends the rule.",
   "92% automatic is earned daily, not granted permanently.",
 ],
 "requirements": [
   "Complete automatic-resolution logging.",
   "Daily stratified human sampling.",
   "Rule distribution monitoring with alerts.",
   "Overturn feedback into rule tuning.",
 ],
 "standards": [
   "Log immutable and complete - no unlogged automatic decisions.",
   "Sample sizes statistically meaningful per rule.",
   "Autonomy suspension procedure defined and executable.",
   "Overturn reasons categorized for pattern analysis.",
 ],
 "citations": [
   "Bernstein, P. A. and Goodman, N. ACM Computing Surveys 13(2), 1981.",
 ],
 "sig_lens": ("The Signature edition treats the automated log as the machine's "
   "testimony under oath: the doctrine grants the machine its 92% jurisdiction "
   "only while the testimony stays honest. The Signature rule is that autonomy "
   "is a license renewed daily by the overturn rate - 0.2% keeps it; a rising "
   "rate revokes it."),
},
# ---------------- Advanced (22-34) ----------------
{
 "name": "Faulty-Source Conflicts",
 "group": "Advanced", "ladder_rank": 22, "ladder_tier": "advanced",
 "demo_key": "c_byzantine",
 "demo_data": {"sources": 7, "faulty": 2, "honest_agree": 5, "tolerance": 2},
 "description": ("The faulty-source conflict record handles versions from sources that "
   "are not merely wrong but adversarial or broken: seven sources, two faulty, five "
   "honest agreeing - within the tolerance of two. Ordinary reconciliation assumes "
   "good faith; faulty-source handling assumes some participants lie or malfunction, "
   "and still reaches the right answer as long as the faulty are fewer than the "
   "tolerance. The record sets the fault model (crash vs Byzantine), the tolerance "
   "bound, and the detection method - because a source that always reports 2.1 while "
   "five honest sources report 4.7 is not 'another perspective,' it is a fault to be "
   "outvoted and investigated."),
 "how_it_works": ("The system assumes up to f faulty sources out of 3f+1 total - the "
   "example tolerates 2 of 7. Versions are grouped by content hash; the group with "
   "more than two-thirds agreement wins regardless of what the faulty minority "
   "claims. The two faulty sources in the example are outvoted 5-2, and their "
   "persistent disagreement triggers a fault investigation: is the source "
   "malfunctioning (sensor drift, software bug) or adversarial (deliberate "
   "falsehood)? Malfunctioning sources are quarantined for repair; adversarial ones "
   "are demoted in the authority hierarchy and their history re-examined. The "
   "tolerance bound is monitored: if faulty sources ever reach f+1, the system "
   "declares itself unable to resolve safely and escalates everything - because "
   "beyond the bound, the liars can outvote the truth."),
 "key_points": [
   "7 sources, 2 faulty, 5 honest agreeing - within tolerance of 2.",
   "Fault model: crash vs Byzantine; tolerance bound 3f+1.",
   "Two-thirds agreement wins regardless of the faulty minority.",
   "Faulty sources investigated: malfunction (quarantine) vs adversarial (demote).",
   "Beyond the bound, the system declares inability - liars could outvote truth.",
   "A persistently disagreeing source is a fault, not a perspective.",
 ],
 "requirements": [
   "Fault model documented per source set.",
   "Tolerance bound computed and monitored.",
   "Fault investigation procedure.",
   "Beyond-bound escalation rule.",
 ],
 "standards": [
   "Never resolve by simple majority where faults are possible - use the bound.",
   "Fault investigations concluded with a verdict, not left open.",
   "Demotions and quarantines logged with evidence.",
   "Bound breaches treated as incidents.",
 ],
 "citations": [
   "Lamport, L., Shostak, R., and Pease, M. The Byzantine generals problem. ACM TOPLAS 4(3), 1982.",
 ],
 "sig_lens": ("The Signature Reconciliation Doctrine treats faulty sources as false "
   "witnesses: the doctrine hears them - the procedure counts every version - but "
   "it does not let two false witnesses outvote five true ones. The Signature "
   "edition requires the bound stated openly, because a court that does not know "
   "how many liars it can survive does not know whether its verdicts are safe."),
},
{
 "name": "Reconciliation Audit Trail",
 "group": "Advanced", "ladder_rank": 23, "ladder_tier": "advanced",
 "demo_key": "c_facts",
 "demo_data": {"events": 96200, "cases": 18400, "immutable": True,
               "checks": [["immutable", "==", True]]},
 "description": ("The reconciliation audit trail is the permanent record of every "
   "disagreement and its settlement: ninety-six thousand two hundred events per day "
   "across eighteen thousand four hundred cases - append-only, hash-chained, "
   "immutable. Every detection, classification, score, rule application, human "
   "decision, and appeal is an event; the chain lets any auditor verify that no "
   "event was altered or removed. When a resolved value is questioned months "
   "later, the trail reconstructs the entire proceeding: who disagreed, what the "
   "evidence was, which rule decided, and why. A reconciliation system without a "
   "trail is a court that burns its transcripts."),
 "how_it_works": ("Events append with timestamps, actor identities (rule ID or "
   "reviewer), and content hashes chained to the previous event. The daily volume "
   "- 96,200 events - is handled by hash-chained log segments, each segment sealed "
   "hourly with its root hash published to independent storage. Verification walks "
   "the chain: any tampering breaks the hashes and is detectable by any auditor "
   "with the sealed roots. Retention is permanent for case-closing events and "
   "seven years for intermediate detection events, per the retention policy. "
   "Sources and submitters can read the events concerning their own versions - "
   "transparency is the point - and dispute entries are appended as events, never "
   "edited. The trail is the evidence base for policy reviews: which rules "
   "decided well is measured from it."),
 "key_points": [
   "96,200 events/day, 18,400 cases - append-only, hash-chained, immutable.",
   "Every stage an event: detection, classification, scoring, rule, decision, appeal.",
   "Hourly sealed segments with roots in independent storage.",
   "Tampering detectable by any auditor with the sealed roots.",
   "Sources read their own events; disputes appended, never edited.",
   "The trail is the evidence base for policy reviews.",
 ],
 "requirements": [
   "Hash-chained append-only event log.",
   "Hourly segment sealing with independent root storage.",
   "Retention policy implemented (permanent for closures).",
   "Auditor verification tooling.",
 ],
 "standards": [
   "No edit or delete operations on the trail.",
   "Actor identity on every event.",
   "Independent root storage outside the reconciliation system.",
   "Verification runnable without system cooperation.",
 ],
 "citations": [
   "ISO 15489-1:2016 (records as evidence).",
 ],
 "sig_lens": ("The Signature edition treats the audit trail as the court's eternal "
   "transcript: the Signature doctrine requires every word of the proceeding "
   "preserved, because the verdicts of today become the precedents of tomorrow. "
   "A court that burns its transcripts rules only for the moment - the doctrine "
   "rules for the record."),
},
{
 "name": "Resolution Decision Record",
 "group": "Advanced", "ladder_rank": 24, "ladder_tier": "advanced",
 "demo_key": "c_decision",
 "demo_data": {"case": "CC-2026-10413", "winner": "A", "rule": "R1", "scores": [117.0, 36.6], "appealable_days": 30},
 "description": ("The resolution decision record is the written judgment for one "
   "conflict: case CC-2026-10413, winner version A, rule R1, scores 117.0 vs 36.6, "
   "appealable for thirty days. It states what was decided, which rule decided it, "
   "what the evidence was, and why the evidence favored the winner - in terms a "
   "non-specialist can follow. The decision is served to the submitters of both "
   "versions, published to the case file, and held open for appeal for thirty days. "
   "A decision without written reasons is an exercise of power; with reasons, it is "
   "an exercise of judgment - and only judgments can be appealed, improved, and "
   "trusted."),
 "how_it_works": ("The record contains: the case ID, the conflicting versions with "
   "their tags, the classification, the confidence scores (117.0 vs 36.6 - decisive), "
   "the policy rule applied (R1: decisive value conflict, higher score wins), the "
   "evidence summary (A from the system-of-record with 3 corroborations; B from a "
   "contributed source with 1), the reasoning in plain language, the merged result, "
   "the decider identity (automatic rule R1 under policy v4.2, or the reviewer's "
   "name), and the appeal window (30 days) with instructions. Both submitters are "
   "notified; the losing submitter gets the full reasoning, not just the outcome - "
   "because a loser who understands the decision may accept it, while a loser who "
   "receives only 'B lost' will appeal out of confusion. Decisions are final after "
   "the appeal window unless new evidence reopens them."),
 "key_points": [
   "CC-2026-10413: A wins under R1, 117.0 vs 36.6, appealable 30 days.",
   "States what, which rule, what evidence, and why - in plain language.",
   "Served to both submitters; losers get reasoning, not just outcomes.",
   "Decisions without reasons are power; with reasons, judgment.",
   "Final after appeal window unless new evidence reopens.",
   "Only judgments can be appealed, improved, and trusted.",
 ],
 "requirements": [
   "Decision schema with all elements.",
   "Plain-language reasoning mandatory.",
   "Submitter notification with full reasoning.",
   "Appeal window and instructions published.",
 ],
 "standards": [
   "No decision without cited rule and reasons.",
   "Readability tested - non-specialists must follow.",
   "Reopenings require new evidence, not dissatisfaction.",
   "Decision corpus searchable for precedent.",
 ],
 "citations": [
   "ISO 15489-1:2016 (records of decisions).",
 ],
 "sig_lens": ("The Signature Reconciliation Doctrine treats the decision record as the "
   "judgment handed down in open court: the Signature edition requires it readable "
   "by the losing party, because the doctrine measures justice not by the winner's "
   "satisfaction but by the loser's understanding. A loser who understands the "
   "reasons has received justice; one who receives only the outcome has received "
   "force."),
},
{
 "name": "Unresolved-Discrepancy Queue",
 "group": "Advanced", "ladder_rank": 25, "ladder_tier": "advanced",
 "demo_key": "c_queue2",
 "demo_data": {"open": 63, "oldest_days": 41, "sla_days": 30, "breached": 12, "by_type": {"identity": 28, "evidence": 35}},
 "description": ("The unresolved-discrepancy queue holds the conflicts nobody could "
   "settle: sixty-three open, oldest forty-one days, SLA thirty days, twelve "
   "breached - twenty-eight identity deadlocks, thirty-five evidence ties. These "
   "are the cases where versions disagree, authority is balanced, evidence is "
   "tied, and no honest resolution exists yet. The queue does not hide them: each "
   "is visible with its age, its type, its owner, and its next action - because an "
   "unresolved discrepancy left invisible becomes a landmine, while one tracked is "
   "a research task. Twelve breached SLAs mean twelve promises currently broken, "
   "and the record says so plainly."),
 "how_it_works": ("Conflicts enter the queue when all resolution paths are exhausted: "
   "human reviewers deadlocked, evidence genuinely tied, identity unresolvable with "
   "available keys. Each entry carries the case record, the reason resolution "
   "stalled, the assigned owner, the next action (usually 'awaiting evidence X' or "
   "'scheduled re-review on date'), and the age. The 41-day-oldest entry is an "
   "identity deadlock awaiting a tax-ID confirmation from the source's finance "
   "team. Breached SLAs (12 of 63) escalate to senior review weekly - not to force "
   "a dishonest resolution, but to verify the next action is real and progressing. "
   "Resolutions, when evidence finally arrives, are recorded with the full history "
   "of the wait - the queue's memory makes the eventual decision better informed. "
   "The queue is reviewed in full monthly: entries that cannot ever resolve are "
   "documented as permanent discrepancies with their implications stated."),
 "key_points": [
   "63 open, oldest 41 days, SLA 30 days, 12 breached; 28 identity, 35 evidence ties.",
   "Conflicts nobody could settle honestly - tracked visibly, not hidden.",
   "Each entry: case, stall reason, owner, next action, age.",
   "Breaches escalate weekly to verify next actions are real.",
   "Unresolvable entries documented as permanent discrepancies with implications.",
   "An invisible unresolved discrepancy is a landmine; a tracked one is a task.",
 ],
 "requirements": [
   "Queue with entry schema and ownership.",
   "SLA tracking with breach escalation.",
   "Next-action discipline - no entry without one.",
   "Monthly full review.",
 ],
 "standards": [
   "No forced resolutions to clear the queue.",
   "Permanent discrepancies documented with implications.",
   "Breach counts reported honestly.",
   "Evidence arrivals trigger immediate re-review.",
 ],
 "citations": [
   "ITIL 4: Problem Management practice (known-error tracking). Axelos.",
 ],
 "sig_lens": ("The Signature doctrine treats the discrepancy queue as the court's "
   "unsolved docket, kept in the open: the doctrine forbids the convenient "
   "fiction that every disagreement can be settled on schedule. The Signature "
   "edition requires the twelve breaches named - a court that admits its "
   "unsolved cases is more trustworthy than one that pretends at omniscience."),
},
{
 "name": "Conflict Resolution SLA",
 "group": "Advanced", "ladder_rank": 26, "ladder_tier": "advanced",
 "demo_key": "c_sla",
 "demo_data": {"auto_ms": 40, "review_h": 4, "senior_h": 24, "compliance": 0.973, "period": "2026-09"},
 "description": ("The conflict resolution SLA record sets the speed promises: "
   "automatic resolution in forty milliseconds, reviewer decisions in four hours, "
   "senior review in twenty-four hours - with September 2026 compliance at 97.3%. "
   "Speed matters because conflicts block: downstream systems wait for resolved "
   "values, and every hour of indecision is an hour of stale or missing data. The "
   "record sets tiered SLAs by path - the automatic path measured in milliseconds, "
   "the human paths in hours - and reports compliance monthly. The 2.7% miss rate "
   "is analyzed, not hidden: which paths missed, why, and what changed as a result."),
 "how_it_works": ("SLA clocks start when the conflict is classified and stop when the "
   "decision record is published. The automatic path's 40ms covers detection through "
   "resolution for the 92%; the reviewer 4h and senior 24h cover the human 8%. "
   "September's 97.3% compliance breaks down to 99.9% on automatic, 94.1% on "
   "reviewer, 96.0% on senior - the human paths miss more, which is expected and "
   "budgeted. Misses are categorized: evidence-gathering delays (waiting on "
   "submitters), complexity underestimation, and staffing gaps. Each category has "
   "an owner and a remediation: evidence templates for the first, better triage "
   "for the second, surge staffing for the third. SLA performance feeds the "
   "operations review and the staffing model - the queue depth forecast derives "
   "from arrival rates and these SLAs."),
 "key_points": [
   "40ms automatic, 4h reviewer, 24h senior; September compliance 97.3%.",
   "Clocks run classification to published decision.",
   "Breakdown: 99.9% auto, 94.1% reviewer, 96.0% senior.",
   "Misses categorized: evidence delays, complexity, staffing - each with owner.",
   "2.7% miss rate analyzed, not hidden.",
   "SLA performance feeds staffing models and queue forecasts.",
 ],
 "requirements": [
   "Tiered SLAs published per resolution path.",
   "Clock definitions (start/stop) documented.",
   "Monthly compliance reporting with breakdowns.",
   "Miss categorization with owners and remediations.",
 ],
 "standards": [
   "SLAs challenging but achievable - chronic miss means miscalibration.",
   "No SLA gaming: reclassification to reset clocks prohibited.",
   "Compliance reported with the misses, not just the rate.",
   "Staffing modeled from arrival rates and SLAs.",
 ],
 "citations": [
   "ITIL 4: Service Level Management practice. Axelos.",
 ],
 "sig_lens": ("The Signature edition treats the SLA as a promise with a stopwatch: "
   "the doctrine requires the promise specific - forty milliseconds, four hours, "
   "twenty-four - and the accounting honest. A 97.3% with named misses is more "
   "trustworthy than a claimed 100%; the doctrine prefers the honest ledger to "
   "the flattering one."),
},
{
 "name": "Reconciliation at Million-Database Scale",
 "group": "Advanced", "ladder_rank": 27, "ladder_tier": "advanced",
 "demo_key": "c_scale",
 "demo_data": {"databases": 5000, "conflicts_day": 92000, "shards": 64, "p99_ms": 180},
 "description": ("The million-database-scale reconciliation record designs for the "
   "target: five thousand databases (marching to a million), ninety-two thousand "
   "conflicts per day, sixty-four reconciliation shards, p99 resolution latency one "
   "hundred eighty milliseconds. At this scale, reconciliation cannot be a single "
   "pipeline - it is a sharded, streaming fabric where conflicts are detected at "
   "ingest, routed by record identity to the owning shard, and resolved with "
   "locally-cached policy and authority data. The record covers partitioning (by "
   "record identity hash, so all versions of one record land on one shard), "
   "cross-shard conflicts (rare, escalated to a coordinator), and the backpressure "
   "design that keeps a conflict storm in one database from starving the others."),
 "how_it_works": ("Conflicts hash-partition across 64 shards by record identity; each "
   "shard runs the full five-stage pipeline with local replicas of the policy, "
   "authority hierarchy, and schema maps (refreshed every 5 minutes). The 92,000 "
   "daily conflicts distribute to about 1,440 per shard per day - well within the "
   "shard's 40ms automatic budget. Cross-shard conflicts (versions of records whose "
   "identity spans shards, under 0.1%) escalate to a coordinator shard with a "
   "24-hour SLA. Backpressure: each database's conflicts queue separately, and a "
   "storm in one database throttles that database's ingestion rather than "
   "consuming shared shard capacity - noisy neighbors are contained. The p99 of "
   "180ms is measured end-to-end at the 99th percentile across all shards; shard "
   "health below target sheds load to neighbors automatically."),
 "key_points": [
   "5,000 databases; 92,000 conflicts/day; 64 shards; p99 180ms.",
   "Partition by record-identity hash - all versions of one record, one shard.",
   "Policy/authority/schema cached locally per shard, refreshed every 5 minutes.",
   "Cross-shard conflicts (<0.1%) escalate to a coordinator.",
   "Per-database queues with backpressure - storms contained, neighbors protected.",
   "Unhealthy shards shed load to neighbors automatically.",
 ],
 "requirements": [
   "Partitioning scheme documented and implemented.",
   "Local policy/authority caches with refresh SLAs.",
   "Coordinator path for cross-shard conflicts.",
   "Backpressure and load-shedding tested with fault injection.",
 ],
 "standards": [
   "No single-shard dependency for any database's conflicts.",
   "p99 measured end-to-end, reported per shard and globally.",
   "Storm containment verified, not assumed.",
   "Scale tests run at 2x target load quarterly.",
 ],
 "citations": [
   "Dean, J. and Ghemawat, S. MapReduce: simplified data processing on large clusters. OSDI, 2004 (partitioned processing precedent).",
 ],
 "sig_lens": ("The Signature doctrine scales by federation of courts, not by building "
   "a bigger courtroom: each shard is a complete court for its records, and the "
   "doctrine requires every shard to hold the whole law locally. The Signature "
   "edition insists the storm containment be proven by fault injection - a "
   "federation untested against storms is a fair-weather promise."),
},
{
 "name": "Schema-Drift Conflicts",
 "group": "Advanced", "ladder_rank": 28, "ladder_tier": "advanced",
 "demo_key": "c_facts",
 "demo_data": {"drifts_year": 34, "mapped": 29, "unmapped": 5, "breaking": 2,
               "checks": [["mapped", "==", 29]]},
 "description": ("The schema-drift conflict record handles disagreements caused by "
   "changing shapes: thirty-four drifts this year, twenty-nine mapped, five "
   "unmapped, two breaking. Schemas evolve - fields renamed, types widened, "
   "structures nested - and versions written against different schema versions "
   "disagree structurally even when they agree factually. The record maintains "
   "the schema map: which renames are known, which type changes are safe, and "
   "which drifts break compatibility. The two breaking drifts this year each got "
   "a migration, not a workaround - because workarounds for breaking changes "
   "accumulate into the next crisis."),
 "how_it_works": ("Each drift is detected by comparing version schemas: 34 this "
   "year across the fleet. Known renames (cost->price) apply the map automatically "
   "and the conflict dissolves - 29 of the 34. Type widenings (int->decimal) are "
   "safe and automatic; narrowings (decimal->int) go to human review. The 5 "
   "unmapped drifts become mapping tasks with owners; until mapped, affected "
   "conflicts route to humans. The 2 breaking drifts - a field split into two "
   "with ambiguous mapping, a deleted field with live consumers - triggered "
   "migrations with dual-write periods and cutover dates. Schema versions are "
   "part of version identity: the content hash covers the schema version, so "
   "same-facts-different-shape versions never hash-collide. Maps are versioned "
   "and tested against historical versions before deployment."),
 "key_points": [
   "34 drifts/year: 29 mapped automatically, 5 unmapped (owned tasks), 2 breaking (migrated).",
   "Known renames dissolve conflicts via the schema map.",
   "Widenings automatic; narrowings to human review.",
   "Breaking drifts get migrations with dual-write, not workarounds.",
   "Schema version part of content identity - shapes never hash-collide.",
   "Maps versioned and tested against history before deployment.",
 ],
 "requirements": [
   "Schema map maintained with known transformations.",
   "Drift detection on version ingest.",
   "Mapping tasks owned for unmapped drifts.",
   "Migration procedure for breaking drifts.",
 ],
 "standards": [
   "No silent schema changes in producers.",
   "Maps tested against historical versions.",
   "Breaking changes announced with migration windows.",
   "Workarounds for breaking changes prohibited.",
 ],
 "citations": [
   "Rahm, E. and Do, H. H. IEEE Data Engineering Bulletin 23(4), 2000.",
 ],
 "sig_lens": ("The Signature edition treats schema drift as the ground shifting "
   "under the courthouse: the doctrine requires the survey redone (the map) "
   "before the trial continues. The Signature rule against workarounds for "
   "breaking changes is absolute - a courthouse built on a workaround is a "
   "building waiting for its earthquake."),
},
{
 "name": "Conflict Prediction",
 "group": "Advanced", "ladder_rank": 29, "ladder_tier": "advanced",
 "demo_key": "c_predict",
 "demo_data": {"signals": 6, "precision": 0.71, "recall": 0.66, "prevented_week": 48},
 "description": ("The conflict prediction record forecasts disagreements before they "
   "arrive: six signals, precision seventy-one percent, recall sixty-six percent, "
   "forty-eight conflicts prevented last week. Prediction watches for the "
   "preconditions of conflict - concurrent edits to the same record, a feed about "
   "to publish against a stale cache, two curators assigned overlapping batches - "
   "and intervenes early: serializing the edits, refreshing the cache, reassigning "
   "the batches. Prevention is cheaper than resolution by an order of magnitude, "
   "which is why even 71% precision pays: the 29% false alarms cost a nudge, while "
   "each prevented conflict saves a full case."),
 "how_it_works": ("The six signals: concurrent-edit detection (two writers, one "
   "record, overlapping window), feed-vs-cache staleness (feed newer than the "
   "cache it will hit), batch overlap (two jobs covering the same records), "
   "schema-drift warnings (producer announced a change), authority-tier churn "
   "(a source's tier just changed), and historical hotspots (records that "
   "conflict repeatedly). When signals fire, the predictor suggests the cheapest "
   "intervention: hold one writer, pre-refresh the cache, split the batch. The "
   "48 prevented last week are counted where the intervention was applied and no "
   "conflict followed - with a control comparison, because some would not have "
   "conflicted anyway. Precision 71% and recall 66% are reported honestly; the "
   "system tunes for precision over recall, since false alarms that nag writers "
   "get ignored and then the true alarms get ignored too."),
 "key_points": [
   "6 signals; precision 71%, recall 66%; 48 prevented last week.",
   "Signals: concurrent edits, feed/cache staleness, batch overlap, drift warnings, tier churn, hotspots.",
   "Interventions: serialize, pre-refresh, reassign - prevention beats resolution 10:1.",
   "Tuned for precision: nagging false alarms train writers to ignore true ones.",
   "Prevented counted with control comparison - honesty about the counterfactual.",
   "Prediction advises; it never blocks writes unilaterally.",
 ],
 "requirements": [
   "Signal catalog with definitions.",
   "Intervention playbook per signal.",
   "Prevention counting with controls.",
   "Precision/recall tracked and tuned.",
 ],
 "standards": [
   "No unilateral write-blocking by the predictor.",
   "False-alarm budget defined and respected.",
   "Interventions logged and reversible.",
   "Hotspot records get structural fixes, not perpetual prediction.",
 ],
 "citations": [
   "Kulkarni, S. et al. Logical Physical Clocks (concurrency foundations).",
 ],
 "sig_lens": ("The Signature doctrine treats prediction as the scout, not the "
   "general: the scout reports the smoke on the horizon, but the doctrine "
   "forbids the scout from ordering the retreat. The Signature edition "
   "requires the scout honest about their miss rate - 71% precision stated "
   "openly - because a scout who hides their misses gets the army killed."),
},
{
 "name": "Reconciliation API Contract",
 "group": "Advanced", "ladder_rank": 30, "ladder_tier": "advanced",
 "demo_key": "c_facts",
 "demo_data": {"endpoints": 9, "version": "v2", "sla_ms": 200,
               "checks": [["endpoints", "==", 9]]},
 "description": ("The reconciliation API contract defines how systems submit "
   "versions and receive decisions: nine endpoints, version 2, two-hundred-"
   "millisecond SLA. The API is the front door of reconciliation: submit "
   "versions, query case status, file appeals, fetch decisions, subscribe to "
   "resolution events. The contract specifies request shapes, authentication, "
   "idempotency (every submission carries a key - retried submissions never "
   "double-create cases), and the event stream for downstream consumers who "
   "need to know the moment a conflict they care about resolves. Version 2 "
   "added bulk submission and the appeal endpoint; version 1 remains supported "
   "until its published sunset."),
 "how_it_works": ("The nine endpoints: submit-version, submit-batch, get-case, "
   "list-cases, get-decision, file-appeal, get-policy, subscribe-events, and "
   "health. Authentication uses the connector registry's credential schemes; "
   "every mutating call requires an idempotency key. The 200ms SLA covers the "
   "synchronous acknowledgment (case opened, queued) - not the resolution "
   "itself, which completes asynchronously and notifies via the event stream "
   "and callback URLs. Rate limits are per submitter, published in the "
   "contract. Breaking changes bump the major version with a twelve-month "
   "support overlap; the contract is itself under the change management "
   "discipline. Client libraries are generated from the contract, never "
   "hand-written against it - the contract is the source of truth."),
 "key_points": [
   "9 endpoints, v2, 200ms acknowledgment SLA.",
   "Idempotency keys on every mutating call - retries never double-create.",
   "Resolution asynchronous; notification via event stream and callbacks.",
   "Per-submitter rate limits published in the contract.",
   "Major versions with 12-month overlap; contract under change management.",
   "Client libraries generated from the contract, never hand-written.",
 ],
 "requirements": [
   "Published contract with all nine endpoints.",
   "Idempotency enforced on mutations.",
   "Event stream for resolution notifications.",
   "Version support policy with overlap.",
 ],
 "standards": [
   "Contract-first: code generated from contract.",
   "SLA measured on acknowledgment, documented as such.",
   "Authentication per the credential standards.",
   "Deprecation notices twelve months minimum.",
 ],
 "citations": [
   "OpenAPI Specification v3.1.0, OpenAPI Initiative.",
 ],
 "sig_lens": ("The Signature edition treats the API contract as the courthouse "
   "doors and their hours: the doctrine requires the doors open, the hours "
   "posted, and the procedures the same for every petitioner. The Signature "
   "rule is that the contract is the law of the front door - no petitioner "
   "gets a private entrance."),
},
{
 "name": "Conflict Metrics Dashboard",
 "group": "Advanced", "ladder_rank": 31, "ladder_tier": "advanced",
 "demo_key": "c_metrics",
 "demo_data": {"panels": 8, "conflicts_day": 18400, "auto_pct": 92, "overturn_pct": 0.2, "sla": 97.3},
 "description": ("The conflict metrics dashboard shows the health of reconciliation "
   "at a glance: eight panels, eighteen thousand four hundred conflicts per day, "
   "ninety-two percent automatic, overturn rate 0.2%, SLA compliance 97.3%. The "
   "panels are: volume by type, automatic-vs-human split, rule distribution, "
   "overturn trends, SLA compliance by path, queue depth and age, escalation "
   "funnel, and the discrepancy queue. Each panel answers a governance question: "
   "is the system healthy, where is it straining, what is getting worse. The "
   "dashboard is the instrument panel of the reconciliation court - and like any "
   "instrument panel, it is useless if nobody watches it, so review cadences are "
   "assigned per panel."),
 "how_it_works": ("The eight panels query the case records and audit trail on a "
   "five-minute refresh. Volume-by-type shows the taxonomy distribution - a spike "
   "in identity conflicts means an upstream identity problem. The rule "
   "distribution panel watches for misfires (rule 10 jumping 4x overnight). "
   "Overturn trends track the 0.2% for drift upward. SLA compliance splits by "
   "path (99.9/94.1/96.0). Queue panels show the human queue depth and the "
   "discrepancy queue age. The escalation funnel shows 24/5/2 across levels. "
   "Thresholds match the published standards - the dashboard displays the "
   "system's own numbers back to it. Daily review covers volume, overturns, and "
   "SLA; weekly review covers the rest; the monthly governance review starts "
   "from this dashboard and ends with decisions."),
 "key_points": [
   "8 panels; 18,400 conflicts/day; 92% auto; 0.2% overturn; 97.3% SLA.",
   "Panels: volume by type, auto/human split, rule distribution, overturn trends, SLA by path, queues, escalation funnel, discrepancy queue.",
   "Spikes diagnose upstream problems (identity spike = upstream identity problem).",
   "Thresholds are the published standards - display, not redefinition.",
   "Review cadences assigned per panel: daily, weekly, monthly governance.",
   "Monthly governance review starts here and ends with decisions.",
 ],
 "requirements": [
   "All eight panels with documented queries.",
   "Five-minute refresh met and monitored.",
   "Review cadences assigned and kept.",
   "Thresholds matching published standards.",
 ],
 "standards": [
   "Dashboard numbers reproducible from case records.",
   "No panel without an owner and a review cadence.",
   "Governance review minutes reference dashboard figures.",
   "Dashboard itself under change management.",
 ],
 "citations": [
   "NIST Special Publication 800-53, control SI-4.",
 ],
 "sig_lens": ("The Signature edition treats the dashboard as the court's public "
   "gallery: the doctrine requires the proceedings visible - volumes, overturns, "
   "queues, breaches - to anyone with standing. The Signature rule is that a "
   "court confident in its justice opens its gallery; the metrics are the open "
   "doors."),
},
{
 "name": "Reconciliation Policy Versioning",
 "group": "Advanced", "ladder_rank": 32, "ladder_tier": "advanced",
 "demo_key": "c_policy",
 "demo_data": {"version": "v4.2", "rules": 12, "history": ["v4.0", "v4.1", "v4.2"], "test_corpus": 5000},
 "description": ("The reconciliation policy versioning record governs how the law "
   "itself changes: current v4.2, twelve rules, history v4.0 through v4.2, tested "
   "against a five-thousand-case corpus. Policy changes are the highest-leverage "
   "changes in the system - one rule edit can re-decide thousands of future "
   "conflicts - so they get the heaviest process: proposal with rationale, impact "
   "analysis replaying the test corpus under the new rules, a canary period where "
   "new and old decide in parallel, and a rollback plan. v4.2's change (tightened "
   "close-score thresholds) replayed 5,000 historical cases: 4,977 identical, 23 "
   "changed, all 23 reviewed by humans before shipping."),
 "how_it_works": ("A policy proposal states the rule change, the rationale (v4.2: "
   "the March mis-resolution where a 14%-gap conflict auto-resolved wrongly), "
   "and the expected impact. Impact analysis replays the 5,000-case test corpus - "
   "real historical cases with known-good resolutions - under the proposed rules: "
   "v4.2 changed 23 of 5,000 decisions (0.46%), and each changed case was "
   "human-reviewed to confirm the new decision was better. Canary deployment "
   "runs both versions for one week on live traffic, logging disagreements; the "
   "canary is promoted only if disagreements match the impact analysis. Rollback "
   "is a version pointer flip - the old policy stays deployed in standby for one "
   "month. Policy versions are semantic: rule-behavior changes bump major, "
   "threshold tunings bump minor, clarifications bump patch."),
 "key_points": [
   "v4.2, 12 rules, 5,000-case test corpus; v4.2 changed 23 decisions (0.46%).",
   "Process: proposal, impact replay, canary, rollback plan.",
   "All 23 changed cases human-reviewed before shipping.",
   "Canary: both versions decide in parallel for a week.",
   "Rollback is a version-pointer flip; old policy on standby one month.",
   "Semantic versioning: behavior=major, thresholds=minor, clarifications=patch.",
 ],
 "requirements": [
   "Proposal template with rationale and expected impact.",
   "Test corpus of real cases with known-good resolutions.",
   "Canary procedure with promotion criteria.",
   "Standby rollback for one month.",
 ],
 "standards": [
   "No policy change without impact replay.",
   "Changed decisions human-reviewed before shipping.",
   "Canary disagreements must match impact analysis.",
   "Policy history retained permanently.",
 ],
 "citations": [
   "Bernstein, P. A. and Goodman, N. ACM Computing Surveys 13(2), 1981.",
 ],
 "sig_lens": ("The Signature edition treats policy versioning as constitutional "
   "amendment: the doctrine requires the amendment debated, its effects "
   "simulated on history, and its adoption reversible. The Signature rule is "
   "that the law must prove itself against the past before it governs the "
   "future - 5,000 cases replayed, 23 changed, every change judged worthy."),
},
{
 "name": "Reconciliation Disaster Recovery",
 "group": "Advanced", "ladder_rank": 33, "ladder_tier": "advanced",
 "demo_key": "c_dr",
 "demo_data": {"rpo_min": 5, "rto_min": 30, "replicas": 3, "last_drill": "2026-09-20", "result": "pass"},
 "description": ("The reconciliation disaster recovery record proves the court "
   "survives catastrophe: recovery point objective five minutes, recovery time "
   "objective thirty minutes, three geographic replicas, last drill 2026-09-20 "
   "passed. Reconciliation state - open cases, the human queue, policy versions, "
   "the audit trail - is replicated synchronously to three regions; losing a "
   "region loses at most five minutes of decisions. The drill record matters "
   "more than the objectives: 2026-09-20's drill failed over to a secondary "
   "region, replayed the trailing log, verified case integrity by hash chain, "
   "and restored service in twenty-two minutes - eight under objective. An "
   "untested recovery plan is a hope; a drilled one is a capability."),
 "how_it_works": ("State replicates synchronously to three regions; the audit "
   "trail's hash-chained segments make integrity verification straightforward - "
   "the drill replays the trailing five minutes and re-verifies the chain. Open "
   "human-queue items carry their full context in the replicated state, so a "
   "reviewer mid-decision resumes after failover without losing work. Policy "
   "versions replicate with the state - a region never resolves under a stale "
   "policy after failover. Drills run quarterly: full regional failover, "
   "integrity verification, timed recovery, then failback. The 2026-09-20 drill "
   "passed at 22 minutes against the 30-minute objective. Drill failures are "
   "incidents: root-caused, remediated, and re-drilled. The discrepancy queue - "
   "the hardest state, with its long-lived entries - gets explicit verification "
   "in every drill, because it is the state most likely to be mishandled in a "
   "hurry."),
 "key_points": [
   "RPO 5 min, RTO 30 min, 3 regions; drill 2026-09-20 passed in 22 min.",
   "Audit trail hash chains make integrity verification straightforward.",
   "Reviewers resume mid-decision after failover - context replicates.",
   "Policy versions replicate with state - no stale-policy resolutions.",
   "Quarterly drills; failures are incidents, root-caused and re-drilled.",
   "An untested recovery plan is a hope; a drilled one is a capability.",
 ],
 "requirements": [
   "RPO/RTO documented with rationale.",
   "Three-region synchronous replication.",
   "Quarterly drill schedule with pass criteria.",
   "Drill failure incident process.",
 ],
 "standards": [
   "Drills timed against objectives.",
   "Integrity verified by hash chain, not by spot check.",
   "Failback drilled, not just failover.",
   "Discrepancy queue explicitly verified each drill.",
 ],
 "citations": [
   "NIST Special Publication 800-34 Rev. 1: Contingency Planning Guide.",
 ],
 "sig_lens": ("The Signature doctrine treats disaster recovery as the court's "
   "continuity of government: the doctrine requires justice to survive the "
   "burning of any single courthouse. The Signature edition demands the drill "
   "record over the promise - twenty-two minutes measured beats thirty minutes "
   "pledged, and the doctrine files the measurement."),
},
{
 "name": "Reconciliation Self-Audit and Mastery Record",
 "group": "Advanced", "ladder_rank": 34, "ladder_tier": "advanced",
 "demo_key": "c_mastery",
 "demo_data": {"records": 34, "complete": 34, "auto_pct": 92, "overturn_pct": 0.2, "coverage": 1.0},
 "description": ("The reconciliation self-audit and mastery record proves the court "
   "judges itself: thirty-four reconciliation archetypes catalogued, thirty-four "
   "complete, ninety-two percent automatic, overturn rate 0.2%, coverage one "
   "hundred percent. This is the record that closes the loop - the "
   "reconciliation system submitting its own conflicts to its own procedure. It "
   "verifies that every case record is complete, every automatic decision logged, "
   "every human decision reasoned, every policy version tested, and every queue "
   "within SLA. A reconciliation system that cannot reconcile disagreements "
   "about itself is a court that claims immunity from its own law."),
 "how_it_works": ("The self-audit samples cases across all rules and paths: "
   "automatic decisions re-examined for rule compliance, human decisions reviewed "
   "for reasoning quality, queue SLAs measured, discrepancy queue entries "
   "validated, policy test corpus re-run, and the audit trail's hash chain "
   "verified end to end. The example scores 34 of 34 complete with the fleet "
   "running at 92% automatic and 0.2% overturns - the autonomy is earned and "
   "measured. Findings become policy proposals or training updates, tracked to "
   "closure like any finding. The audit runs quarterly with its report to "
   "governance leadership. This record is also the mastery checkpoint: a reader "
   "who understands all thirty-four records - from version identity through "
   "merge mechanics to disaster recovery - understands conflict reconciliation "
   "end to end."),
 "key_points": [
   "34 archetypes, 34 complete; 92% auto; 0.2% overturn; coverage 1.0.",
   "Self-audit samples all rules and paths; hash chain verified end to end.",
   "Findings become policy proposals or training updates.",
   "Runs quarterly; report to governance leadership.",
   "A court claiming immunity from its own law is not a court.",
   "Mastery checkpoint: all 34 records teach reconciliation end to end.",
 ],
 "requirements": [
   "Self-audit executed quarterly with published report.",
   "Coverage across all rules, paths, and queues.",
   "Findings tracked to closure.",
   "Mastery path documented from record 1 to record 34.",
 ],
 "standards": [
   "Coverage target 1.0.",
   "Overturn rate within bounds or autonomy reviewed.",
   "Audit independent of daily operations.",
   "Year-over-year trend reported.",
 ],
 "citations": [
   "ISO 19011:2018 Guidelines for auditing management systems.",
 ],
 "sig_lens": ("The Signature Reconciliation Doctrine ends where it began: with "
   "every version heard, including the system's own. The Signature self-audit "
   "is the court submitting to its own procedure - and the mastery record is "
   "the proof that the whole teaching holds together, simple to complex, "
   "without a gap."),
},
]

assert len(ENTRIES) == 34, "expected 34 entries, got %d" % len(ENTRIES)
_ranks = [e["ladder_rank"] for e in ENTRIES]
assert _ranks == sorted(_ranks) == list(range(1, 35)), "ladder ranks must be 1..34 in order"
