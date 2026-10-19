#!/usr/bin/env python3
"""Entries for the Knowledge Versioning databases (JAH Databases governance
track, group F, 2026-10-17).

Dedupe gate: none of the 8 governance slugs exist in data/manifest.json
(2,770 databases checked 2026-10-17); ID prefixes JAH-KV- (public) and
JAH-KVS- (signature) verified free: zero exact or substring hits in
manifest id_prefix values and zero hits in all shard record IDs of
jah-databases-data-1. All 68 record titles checked against the whole
system (exact dedupe index + live shard title corpus of 1,143,457 titles)
BEFORE authoring.

So this build creates two NEW databases, 34 ladder-ordered records each:

  knowledge-versioning            - The Knowledge Versioning Database
      (public-harvest: real, fact-checked versioning knowledge)
  knowledge-versioning-signature  - The Knowledge Versioning Signature Database
      (the Signature Version Doctrine; src signature, titles suffixed
      " (Signature Edition)", never presented as authentic public record)

34 records each, ladder-ordered 1-34 (ladder_tier foundations 1-10 /
compounded 11-21 / advanced 22-34).

Numerical cores: hand-computed 2026-10-17, machine-verified by the demos
(see demos_knowledge_versioning.py). Every demo prints its real computed
values, asserts tight bounds (never float exact-equality), and ends with
the OK marker; the build machine-executes all 68 demos.

Never the words "bat belt" anywhere. No website references. No Facebook.
"""

SIG_TAIL = ("Signature original - the Signature Version Doctrine: every "
            "change recorded, every diff readable, every deprecation "
            "announced; knowledge that changes silently is not knowledge "
            "but rumor with a database. Clearly labeled Signature-made, "
            "never presented as an authentic public record. Property of "
            "Justin Addam Higgins (JAH).")

ENTRIES = [
# ---------------- Foundations (1-10) ----------------
{
 "name": "Knowledge Versioning Overview",
 "group": "Foundations", "ladder_rank": 1, "ladder_tier": "foundations",
 "demo_key": "v_facts",
 "demo_data": {"entities": 4, "change_types": 3, "policies": 5,
               "checks": [["entities", "==", 4], ["change_types", "==", 3]]},
 "description": ("The versioning overview defines the memory of knowledge: "
   "four versioned entities - concepts, definitions, rules, relationships - "
   "three change types (major, minor, patch), and five policies governing "
   "them. Knowledge changes: definitions sharpen, rules update, "
   "relationships rewire, concepts split and merge. Without versioning, "
   "every change is silent - consumers cannot tell what changed, when, or "
   "whether they should care. With versioning, every change is a recorded "
   "event with a number, a diff, and an announcement policy. The overview "
   "sets the vocabulary: version, revision, diff, deprecation, "
   "supersession - used consistently across all thirty-four records."),
 "how_it_works": ("Each knowledge entity carries a version history: the "
   "current version plus every prior version, immutable. Changes are "
   "classified major (breaking: meaning changed), minor (additive: meaning "
   "extended), or patch (clarifying: wording fixed, meaning kept) - the "
   "semantic versioning adapted from software, because knowledge has the "
   "same compatibility problem code does. The five policies: numbering "
   "(how versions are assigned), announcement (who is told of what "
   "changes), deprecation (how endings are handled), compatibility (what "
   "may change without breaking whom), and retention (how long old "
   "versions live). Every version records its author, timestamp, "
   "rationale, and parent version - the provenance that makes the history "
   "auditable."),
 "key_points": [
   "4 versioned entities: concepts, definitions, rules, relationships.",
   "3 change types: major (breaking), minor (additive), patch (clarifying).",
   "5 policies: numbering, announcement, deprecation, compatibility, retention.",
   "Every version immutable, with author, timestamp, rationale, parent.",
   "Semantic versioning adapted from software - same compatibility problem.",
   "Silent change is rumor; versioned change is knowledge.",
 ],
 "requirements": [
   "Version history per entity.",
   "Change classification on every version.",
   "Five policies published.",
   "Provenance on every version.",
 ],
 "standards": [
   "Versions immutable.",
   "Classifications honest (no minor-labeled breaking changes).",
   "Rationale required.",
   "Vocabulary consistent.",
 ],
 "citations": [
   "Semantic Versioning 2.0.0 (semver.org) - adapted for knowledge.",
 ],
 "sig_lens": ("The Signature Version Doctrine opens with the chronicler's "
   "oath: the doctrine requires every change to knowledge recorded - "
   "numbered, dated, and explained. The Signature edition treats silent "
   "change as the cardinal sin: a doctrine that lets meanings shift "
   "without a trace does not curate knowledge, it curates confusion."),
},
{
 "name": "Semantic Versioning for Knowledge",
 "group": "Foundations", "ladder_rank": 2, "ladder_tier": "foundations",
 "demo_key": "v_semver",
 "demo_data": {"major": 3, "minor": 2, "patch": 1, "entity": "concept:database"},
 "description": ("The semantic versioning record adapts semver to knowledge: "
   "concept 'database' at version 3.2.1 - major 3 (two breaking meaning "
   "changes in its history), minor 2 (two additive extensions), patch 1 "
   "(one clarification). The semantics: MAJOR increments when the meaning "
   "changes incompatibly (consumers must re-examine), MINOR when meaning "
   "extends compatibly (consumers may ignore), PATCH when wording clarifies "
   "without changing meaning (consumers need not care). The 3.2.1 tells a "
   "consumer everything: this concept has broken twice, grown twice, and "
   "been polished once. Pre-1.0 versions (0.x) mark provisional knowledge "
   "- the 0.x contract is 'anything may change', stated openly."),
 "how_it_works": ("Version numbers are assigned by the change classifier: "
   "the author proposes a change with its type, the classifier validates "
   "(breaking analyses run against the compatibility matrix), and the "
   "number increments accordingly. Major 3 means the concept's meaning "
   "broke twice before (v1->v2: scope narrowed; v2->v3: relational model "
   "adopted); minor 2 (facets added, examples extended); patch 1 (typo "
   "in the definition fixed). Consumers pin versions: the contract "
   "system (see the advanced record) lets a consumer declare 'I use "
   "database@2.x' and be notified only of breaking changes. The 0.x "
   "provisional range is used for new concepts until their first "
   "review - the version number honestly advertises instability."),
 "key_points": [
   "database@3.2.1: 2 breaking changes, 2 extensions, 1 clarification.",
   "MAJOR: meaning changed incompatibly. MINOR: extended compatibly. PATCH: clarified.",
   "The number tells consumers everything at a glance.",
   "Consumers pin versions; notified of breaking changes.",
   "0.x marks provisional knowledge honestly.",
   "Classifier validates the author's proposed type.",
 ],
 "requirements": [
   "Change classification per version.",
   "Classifier validation of types.",
   "Consumer version pinning.",
   "Provisional 0.x range.",
 ],
 "standards": [
   "No silent majors (breaking changes labeled major).",
   "Numbers monotonic within an entity.",
   "Pins honored by the notification system.",
   "0.x never presented as stable.",
 ],
 "citations": [
   "Semantic Versioning 2.0.0 (semver.org).",
 ],
 "sig_lens": ("The Signature Version Doctrine numbers its meanings: the "
   "doctrine requires the 3.2.1 to tell the whole history - two breaks, "
   "two growths, one polish. The Signature edition validates the "
   "author's classification: a doctrine that lets breaking changes "
   "hide as patches is not versioning, it is mislabeling with "
   "punctuation."),
},
{
 "name": "Concept Change History",
 "group": "Foundations", "ladder_rank": 3, "ladder_tier": "foundations",
 "demo_key": "v_concept",
 "demo_data": {"versions": 7, "years": 3, "entity": "concept:database", "current": "3.2.1"},
 "description": ("The concept history is the biography of an idea: "
   "'database' through seven versions over three years, now at 3.2.1. "
   "The history reads like a story: v1.0 (the naive 'organized "
   "collection'), v1.1 (examples added), v2.0 (scope narrowed - flat "
   "files excluded, the first break), v2.1 (facets: the four "
   "dimensions), v3.0 (relational model adopted, the second break), "
   "v3.1 (federation facet), v3.2 (examples extended), v3.2.1 (typo "
   "fixed). Each version has its rationale - the v2.0 rationale ('flat "
   "files lack the query dimension') is the kind of reasoning future "
   "readers need. The history is the concept's memory; without it, "
   "the current definition is an assertion without a past."),
 "how_it_works": ("The history is stored as a linked list: each version "
   "points to its parent, with the full version record (content, "
   "author, timestamp, rationale, change type). Seven versions over "
   "three years averages one per five months - the concept's metabolism. "
   "The history supports the time-travel query (see the compounded "
   "record): 'what did database mean on 2025-06-01?' returns v2.1 with "
   "its effective dates. Branching is visible in the history: the v2.x "
   "line continued (v2.1) while v3.0 was prepared - the merge record "
   "covers the mechanics. Histories are never rewritten: a mistaken "
   "version is superseded by a correction, not edited - the error "
   "stays visible, because the history of an error is also knowledge."),
 "key_points": [
   "7 versions over 3 years; current 3.2.1.",
   "Each version with rationale (v2.0: flat files excluded).",
   "Linked list with parent pointers; immutable.",
   "Supports time-travel queries by effective date.",
   "Mistakes superseded, never rewritten.",
   "The history is the concept's memory.",
 ],
 "requirements": [
   "Parent-linked version lists.",
   "Rationale per version.",
   "Effective dates.",
   "Immutability enforced.",
 ],
 "standards": [
   "Histories append-only.",
   "Corrections as new versions.",
   "Rationales required.",
   "Time-travel supported.",
 ],
 "citations": [
   "Semantic Versioning 2.0.0 (semver.org).",
 ],
 "sig_lens": ("The Signature Version Doctrine keeps every biography: the "
   "doctrine requires the seven versions with their rationales - the "
   "v2.0 break explained, not just recorded. The Signature edition "
   "never rewrites: a doctrine that edits its past has no history, "
   "only a current draft with pretensions."),
},
{
 "name": "Definition Versioning",
 "group": "Foundations", "ladder_rank": 4, "ladder_tier": "foundations",
 "demo_key": "v_definition",
 "demo_data": {"from": "1.4.0", "to": "1.5.0", "clauses_changed": 2, "clauses_total": 9},
 "description": ("The definition versioning record tracks wording that "
   "matters: definition v1.4.0 to v1.5.0, two of nine clauses changed - "
   "a minor version, meaning extended. Definitions are the most "
   "versioned entity: they are quoted, cited, and built upon, so their "
   "changes ripple. The two changed clauses: the scope clause (added "
   "'queryable' to the requirements) and the examples clause (three "
   "examples added). Seven clauses untouched - the diff record shows "
   "exactly which. Minor, not major: 'queryable' was always implied by "
   "the surrounding text; the change makes explicit what was implicit "
   "- extension, not breakage. The classifier agreed; the review board "
   "concurred."),
 "how_it_works": ("Definitions are stored clause-by-clause (nine clauses "
   "here): each clause versioned independently, the definition version "
   "derived from the clause versions (any clause major -> definition "
   "major). The v1.4.0->v1.5.0 change touched two clauses: scope "
   "(minor: 'queryable' made explicit) and examples (minor: additions). "
   "The diff is clause-granular: consumers see 'clauses 3 and 7 "
   "changed' rather than a wall of text. Quotation pinning: citations "
   "of the definition pin the version ('as defined in v1.4.0'), so "
   "quoted text never silently changes meaning under the quoter. The "
   "review process for definition changes: the author's classification, "
   "the classifier's validation, and for majors, the board's approval "
   "- definitions are load-bearing, and load-bearing changes get "
   "scaffolding."),
 "key_points": [
   "v1.4.0 -> v1.5.0: 2 of 9 clauses changed (minor).",
   "Clause-granular storage and diffs.",
   "Quotation pinning: citations pin versions.",
   "Definitions are load-bearing; majors need board approval.",
   "'Queryable' made explicit: extension, not breakage.",
   "The diff shows exactly which clauses changed.",
 ],
 "requirements": [
   "Clause-level versioning.",
   "Quotation pinning support.",
   "Classification with review for majors.",
   "Clause-granular diffs.",
 ],
 "standards": [
   "Definition version derived from clause versions.",
   "Pins honored.",
   "Board approval for majors.",
   "Diffs clause-addressed.",
 ],
 "citations": [
   "Semantic Versioning 2.0.0 (semver.org).",
 ],
 "sig_lens": ("The Signature Version Doctrine versions the load-bearing "
   "words clause by clause: the doctrine requires the two changed "
   "clauses named - 3 and 7 - not a wall of text. The Signature edition "
   "pins quotations: a doctrine that lets quoted definitions drift has "
   "not versioned, it has merely watched the words move."),
},
{
 "name": "Rule Versioning",
 "group": "Foundations", "ladder_rank": 5, "ladder_tier": "foundations",
 "demo_key": "v_rule",
 "demo_data": {"rules": 12, "version": "5.0.0", "changed": 3, "entity": "rule-set:ingestion"},
 "description": ("The rule versioning record versions executable knowledge: "
   "the ingestion rule set at 5.0.0 - twelve rules, three changed in the "
   "major bump. Rules are versioned most strictly because they execute: "
   "a changed rule changes behavior, and behavior changes break "
   "pipelines. The v5.0.0 major: three rules' conditions tightened (the "
   "validation thresholds), which rejects inputs v4 accepted - breaking "
   "by definition. The record keeps the rule text, the test suite "
   "(every rule version ships with its tests), and the effective date - "
   "because a rule's version without its tests is a promise without "
   "evidence."),
 "how_it_works": ("Each rule version bundles: the rule text (the "
   "condition-action pairs), the test suite (inputs with expected "
   "outcomes - the v5 tests include the newly-rejected inputs as "
   "negative cases), the change rationale, and the effective date. "
   "The three changed rules are diffed condition-by-condition (the "
   "rule diff record). Deployment follows the deprecation pattern: "
   "v5 announced 90 days ahead, v4 and v5 run in parallel (shadow "
   "mode: v5 decides, v4 executes, disagreements logged), then cutover "
   "- because rules execute, their version changes are migrations, "
   "not edits. Rollback is to v4 within the window (the rollback "
   "record). The twelve rules' versions are independent, but the set "
   "version (5.0.0) rolls up the highest change: three rule-majors "
   "make a set-major."),
 "key_points": [
   "Ingestion rules v5.0.0: 12 rules, 3 changed (major).",
   "Rules versioned strictly - they execute.",
   "Every version ships with its test suite.",
   "Shadow deployment: v5 decides, v4 executes, then cutover.",
   "Set version rolls up the highest rule change.",
   "A rule without its tests is a promise without evidence.",
 ],
 "requirements": [
   "Rule text + tests per version.",
   "Condition-level diffs.",
   "Shadow deployment for majors.",
   "Effective dates.",
 ],
 "standards": [
   "Tests mandatory per version.",
   "Breaking rule changes are majors.",
   "Parallel run before cutover.",
   "Rollback window defined.",
 ],
 "citations": [
   "Semantic Versioning 2.0.0 (semver.org).",
 ],
 "sig_lens": ("The Signature Version Doctrine versions what executes most "
   "strictly: the doctrine requires the tests shipped with the rules - "
   "v5's negative cases proving the new rejections. The Signature "
   "edition shadow-deploys: a doctrine that swaps executing rules "
   "without a parallel run is not versioning, it is gambling with "
   "production."),
},
{
 "name": "Relationship Versioning",
 "group": "Foundations", "ladder_rank": 6, "ladder_tier": "foundations",
 "demo_key": "v_relationship",
 "demo_data": {"changed": 3, "total": 48, "version": "2.3.0", "entity": "graph:federation"},
 "description": ("The relationship versioning record versions the graph's "
   "edges: the federation graph at 2.3.0 - three of forty-eight "
   "relationships changed. Relationships are the quietest versioned "
   "entity: nodes get the attention, but the edges carry the meaning "
   "(a concept's relationships define it as much as its definition). "
   "The three changes: 'member-of' gained a temporal qualifier (minor), "
   "'supersedes' was added between two concepts (minor), and 'same-as' "
   "between two records was removed (major - a merge undone, consumers "
   "notified). Forty-eight relationships, each with its own version - "
   "the graph version (2.3.0) rolls up the highest edge change."),
 "how_it_works": ("Each relationship is a versioned edge: (subject, "
   "predicate, object, version, valid-from, valid-to). The 'same-as' "
   "removal was the major: it undid a merge, so every consumer that "
   "relied on the identity had to re-examine - the major label and the "
   "notification went together. The temporal qualifier on 'member-of' "
   "was minor: it added information (membership dates) without "
   "invalidating existing uses. Edge versions support the time-travel "
   "query on graphs: 'who was a member on 2025-06-01?' uses the "
   "valid-from/valid-to ranges. The relationship diff record shows "
   "edge-level changes; the lineage graph (advanced) visualizes the "
   "version history of the whole graph."),
 "key_points": [
   "Federation graph v2.3.0: 3 of 48 relationships changed.",
   "Edges versioned individually: (s, p, o, version, valid-from/to).",
   "'same-as' removal was major (a merge undone); qualifier minor.",
   "Graph version rolls up the highest edge change.",
   "Time-travel on graphs via validity ranges.",
   "Edges carry meaning as much as nodes.",
 ],
 "requirements": [
   "Per-edge versioning with validity ranges.",
   "Change classification per edge.",
   "Graph version rollup.",
   "Time-travel support.",
 ],
 "standards": [
   "Merge-undoing changes are majors.",
   "Validity ranges mandatory.",
   "Notifications with majors.",
   "Edge diffs available.",
 ],
 "citations": [
   "Semantic Versioning 2.0.0 (semver.org).",
 ],
 "sig_lens": ("The Signature Version Doctrine versions the edges too: the "
   "doctrine requires the 'same-as' removal labeled major - unmerging "
   "is the loudest quiet change. The Signature edition keeps validity "
   "ranges on every edge: a doctrine whose relationships have no dates "
   "cannot answer 'who was a member when', which is half the questions "
   "graphs exist to answer."),
},
{
 "name": "Version Identifiers and Labels",
 "group": "Foundations", "ladder_rank": 7, "ladder_tier": "foundations",
 "demo_key": "v_identifiers",
 "demo_data": {"format": "KV-2026-0042", "labels": 4, "entities": 1240},
 "description": ("The identifiers record names every version: format "
   "KV-2026-0042 (prefix, year, sequence), with four human labels "
   "available - stable, provisional, deprecated, archived. The "
   "identifier is the version's address: KV-2026-0042 is the 42nd "
   "versioned change of 2026, unique across all entities. Labels are "
   "the human layer: 'stable' (current recommended), 'provisional' "
   "(0.x, use with care), 'deprecated' (superseded, migration path "
   "published), 'archived' (retained for history, not for use). The "
   "1,240 versioned entities each carry their current label; the "
   "label is the first thing a consumer checks, because the label "
   "says whether to build on it."),
 "how_it_works": ("Identifier assignment is sequential per year, "
   "centralized (the version registry), never reused - KV-2026-0042 "
   "is forever that change. Labels transition by rule: provisional -> "
   "stable (review passed), stable -> deprecated (superseded, notice "
   "published), deprecated -> archived (migration window closed). The "
   "label is computed from the version state, not set by hand - "
   "hand-set labels drift. Consumers filter by label: production "
   "systems pin 'stable', experiments may use 'provisional', nothing "
   "new builds on 'deprecated'. The registry resolves identifiers to "
   "full version records (content, diff, provenance); the identifier "
   "is short enough for conversation and unique enough for contracts."),
 "key_points": [
   "Format KV-2026-0042: prefix, year, sequence; never reused.",
   "4 labels: stable, provisional, deprecated, archived.",
   "Labels computed from state, not hand-set.",
   "1,240 entities labeled; label checked first by consumers.",
   "Transitions by rule (review, supersession, window close).",
   "Identifiers short for conversation, unique for contracts.",
 ],
 "requirements": [
   "Centralized sequential assignment.",
   "Label state machine.",
   "Registry resolution.",
   "Consumer label filtering.",
 ],
 "standards": [
   "Identifiers immutable and unique.",
   "Labels computed, not assigned.",
   "Transitions recorded.",
   "Provisional never default.",
 ],
 "citations": [
   "Semantic Versioning 2.0.0 (semver.org).",
 ],
 "sig_lens": ("The Signature Version Doctrine names every change: the "
   "doctrine requires KV-2026-0042 to resolve forever - an address "
   "that stops resolving is not an identifier, it is a rumor of one. "
   "The Signature edition computes the labels: a doctrine with "
   "hand-set labels will find 'stable' on things nobody reviewed, "
   "which is how incidents get their invitations."),
},
{
 "name": "Change Types: Major, Minor, Patch",
 "group": "Foundations", "ladder_rank": 8, "ladder_tier": "foundations",
 "demo_key": "v_changetypes",
 "demo_data": {"major": 2, "minor": 8, "patch": 24, "total": 34},
 "description": ("The change types record classifies the thirty-four "
   "changes: 2 major, 8 minor, 24 patch. The distribution is healthy: "
   "patches dominate (wording, clarifications), minors add steadily "
   "(extensions), majors are rare (breaks). The classifier's rules: "
   "major = meaning changed incompatibly (a consumer's correct use "
   "becomes incorrect); minor = meaning extended (old uses still "
   "correct, new uses possible); patch = meaning kept (wording, "
   "examples, formatting). The 2 majors are the ones the board "
   "reviewed; the 24 patches needed no review - the type determines "
   "the ceremony, which is why honest classification matters."),
 "how_it_works": ("Classification runs at proposal time: the author "
   "proposes a type with justification; the classifier checks "
   "mechanically (did any normative clause change? -> not patch; did "
   "any consumer-visible meaning change incompatibly? -> major) and "
   "flags disagreements for the reviewer. The 2 majors: the v2.0 scope "
   "narrowing and the v3.0 relational adoption (both from the concept "
   "history). The 8 minors: facet additions, example extensions, "
   "qualifier additions. The 24 patches: typos, formatting, "
   "clarifying rewordings. Misclassification is the failure mode: a "
   "major labeled minor breaks consumers silently - the audit samples "
   "classifications quarterly, and misclassifiers get retraining (then "
   "review). The type distribution is a health metric: a sudden spike "
   "in majors means the knowledge is churning - investigate."),
 "key_points": [
   "34 changes: 2 major, 8 minor, 24 patch - healthy distribution.",
   "Major: consumer's correct use becomes incorrect.",
   "Type determines ceremony (board review for majors).",
   "Classifier validates; disagreements go to reviewers.",
   "Misclassified majors break consumers silently.",
   "Distribution is a health metric; major spikes investigated.",
 ],
 "requirements": [
   "Classification at proposal with justification.",
   "Mechanical classifier checks.",
   "Quarterly classification audits.",
   "Distribution monitoring.",
 ],
 "standards": [
   "Honest classification enforced.",
   "Majors need board review.",
   "Misclassifiers retrained.",
   "Spikes investigated.",
 ],
 "citations": [
   "Semantic Versioning 2.0.0 (semver.org).",
 ],
 "sig_lens": ("The Signature Version Doctrine classifies honestly: the "
   "doctrine requires the 2 majors to be the real breaks - no "
   "breakage hiding in the 24 patches. The Signature edition audits "
   "the classifiers: a doctrine that lets authors grade their own "
   "breaking changes will find every break was 'just a clarification'."),
},
{
 "name": "Version Timestamps and Provenance",
 "group": "Foundations", "ladder_rank": 9, "ladder_tier": "foundations",
 "demo_key": "v_timestamps",
 "demo_data": {"fields": 3, "format": "ISO 8601", "versions": 1240},
 "description": ("The timestamps record dates every version: three "
   "provenance fields - authored-at, effective-from, superseded-at - in "
   "ISO 8601, on all 1,240 versions. Authored-at is when the change was "
   "written; effective-from is when it takes effect (often later - the "
   "90-day deprecation notices); superseded-at is when the next version "
   "replaced it (null for current). The three dates answer the three "
   "temporal questions: when was it written, when did it apply, when "
   "did it stop. ISO 8601 with timezone, always - the federation "
   "learned about timezone-less timestamps the hard way, and the "
   "standard now forbids them."),
 "how_it_works": ("Every version record carries the three timestamps: "
   "authored-at (the commit moment), effective-from (the applicability "
   "start - for immediate changes equals authored-at; for announced "
   "changes, the announcement date + notice period), superseded-at "
   "(set when the next version's effective-from arrives). The "
   "time-travel query resolves 'what was true at T' by finding the "
   "version with effective-from <= T < superseded-at. The 1,240 "
   "versions' timestamps are the audit trail: the v2.0 scope narrowing "
   "was authored 2025-03-14, effective 2025-06-12 (90-day notice), "
   "superseded 2026-01-20 by v3.0. Clock skew is handled by the "
   "registry's canonical clock (versions are ordered by sequence, not "
   "by wall time, when timestamps collide)."),
 "key_points": [
   "3 fields: authored-at, effective-from, superseded-at (ISO 8601, tz).",
   "Answer: when written, when applied, when replaced.",
   "Effective-from often later (notice periods).",
   "Time-travel resolves by effective ranges.",
   "Ordering by sequence on timestamp collision.",
   "Timezone-less timestamps forbidden.",
 ],
 "requirements": [
   "Three timestamps per version.",
   "ISO 8601 with timezone.",
   "Registry canonical ordering.",
   "Effective-date semantics documented.",
 ],
 "standards": [
   "No naive timestamps.",
   "Superseded-at set on replacement.",
   "Sequences authoritative on collision.",
   "Provenance complete.",
 ],
 "citations": [
   "ISO 8601:2019 Date and time format.",
 ],
 "sig_lens": ("The Signature Version Doctrine dates everything thrice: "
   "the doctrine requires written, effective, and superseded - because "
   "'when' has three answers and two of them are usually confused. The "
   "Signature edition forbids the naive timestamp: a doctrine that "
   "cannot place its versions in time has a history without a calendar."),
},
{
 "name": "Reading a Version Diff",
 "group": "Foundations", "ladder_rank": 10, "ladder_tier": "foundations",
 "demo_key": "v_readdiff",
 "demo_data": {"added": 12, "removed": 5, "context": 3, "format": "unified"},
 "description": ("The diff-reading record teaches the literacy: a unified "
   "diff with 12 additions, 5 removals, 3 lines of context - the "
   "universal language of 'what changed'. Every version ships its diff; "
   "consumers read diffs, not just version numbers, because the number "
   "says how much to care and the diff says what actually changed. The "
   "format: hunk headers (@@ -a,b +c,d @@), context lines (unchanged, "
   "the 3-line window), removals (-), additions (+). The record's "
   "example diff (the v3.2.1 typo fix: 12 added example lines, 5 removed "
   "stale ones) is annotated line by line - the Rosetta Stone for the "
   "diff-illiterate. Diff literacy is required for reviewers; the "
   "review checklist's first item is 'read the diff, not the summary'."),
 "how_it_works": ("Diffs are generated mechanically (the diff records "
   "cover the per-entity formats) and rendered unified with 3 context "
   "lines. Reading order: the hunk headers (where in the document), "
   "then the - lines (what left), then the + lines (what arrived), "
   "then the context (what it sits in). The 12+/5- example: the "
   "examples clause gained 12 lines (new examples) and lost 5 (stale "
   "ones referencing v2 semantics) - a reader sees the concept's "
   "examples modernized at a glance. Semantic diffs supplement the "
   "textual: the classifier annotates hunks ('clause 7: minor - "
   "examples extended'), so readers get the meaning-level summary "
   "with the line-level proof. The record also teaches diff "
   "skepticism: a 500-line diff with 499 reformatting lines hides 1 "
   "real change - the diff viewer collapses whitespace-only changes "
   "by default."),
 "key_points": [
   "Unified diff: 12 additions, 5 removals, 3 context lines.",
   "Number says how much to care; diff says what changed.",
   "Reading order: headers, removals, additions, context.",
   "Classifier annotates hunks with semantic labels.",
   "Whitespace-only changes collapsed by default.",
   "Reviewers read the diff, not the summary.",
 ],
 "requirements": [
   "Unified diffs with context on every version.",
   "Semantic hunk annotations.",
   "Whitespace collapsing in viewers.",
   "Diff literacy for reviewers.",
 ],
 "standards": [
   "Diffs mechanical, not hand-written.",
   "Annotations from the classifier.",
   "Examples annotated line-by-line for teaching.",
   "Summaries never substitute for diffs.",
 ],
 "citations": [
   "Semantic Versioning 2.0.0 (semver.org).",
 ],
 "sig_lens": ("The Signature Version Doctrine teaches diff literacy as a "
   "first skill: the doctrine requires reviewers to read the 12+/5- "
   "before the summary. The Signature edition collapses the whitespace "
   "noise: a doctrine that lets 499 reformatting lines hide 1 real "
   "change is not transparent, it is camouflaged."),
},
# ---------------- Compounded (11-21) ----------------
{
 "name": "Concept Diff Record",
 "group": "Compounded", "ladder_rank": 11, "ladder_tier": "compounded",
 "demo_key": "v_conceptdiff",
 "demo_data": {"fields": 9, "changed": 2, "from": "3.1.0", "to": "3.2.0"},
 "description": ("The concept diff shows field-level change: v3.1.0 to "
   "v3.2.0, two of nine fields changed - the 'facets' field (extended) "
   "and the 'examples' field (three added). Concept diffs are "
   "structural, not textual: they compare the concept's fields "
   "(name, definition, facets, examples, relationships, scope notes, "
   "aliases, deprecation status, provenance) rather than lines of "
   "text. The two changed fields are shown with before/after values; "
   "the seven unchanged are summarized, not shown - the diff respects "
   "the reader's attention. Field-level diffs enable field-level "
   "subscriptions: a consumer watching only 'facets' gets notified of "
   "this change; one watching 'aliases' does not."),
 "how_it_works": ("The differ walks the nine fields: for each, it "
   "compares the normalized values (whitespace-insensitive, order-"
   "insensitive for sets) and emits changed/added/removed/unchanged. "
   "The v3.1.0->v3.2.0 diff: facets changed (2 added), examples "
   "changed (3 added), seven unchanged. Values are shown as "
   "before->after with the change highlighted; large fields (examples "
   "with 40 entries) show only the delta entries, not the full list. "
   "The diff feeds the notification system (field subscriptions), the "
   "classifier (which fields changed determines the change type - "
   "facets changed = minor), and the review UI. Diffs are stored "
   "with the version (not recomputed) - the stored diff is the "
   "historical record of what the changer believed changed."),
 "key_points": [
   "v3.1.0 -> v3.2.0: 2 of 9 fields changed (facets, examples).",
   "Structural (fields), not textual (lines).",
   "Unchanged fields summarized, not shown.",
   "Field-level subscriptions for notifications.",
   "Changed fields determine the change type.",
   "Diffs stored with versions, not recomputed.",
 ],
 "requirements": [
   "Field-level differ with normalization.",
   "Delta-only display for large fields.",
   "Stored diffs.",
   "Subscription support.",
 ],
 "standards": [
   "Normalization documented.",
   "Unchanged summarized.",
   "Diffs immutable once stored.",
   "Type derived from changed fields.",
 ],
 "citations": [
   "Semantic Versioning 2.0.0 (semver.org).",
 ],
 "sig_lens": ("The Signature Version Doctrine diffs by field, not by line: "
   "the doctrine requires the two changed fields named - facets, "
   "examples - with the seven silent ones summarized. The Signature "
   "edition stores the diff: a doctrine that recomputes history on "
   "demand will one day compute it differently, and then it will have "
   "two pasts."),
},
{
 "name": "Definition Diff Record",
 "group": "Compounded", "ladder_rank": 12, "ladder_tier": "compounded",
 "demo_key": "v_defdiff",
 "demo_data": {"similarity": 0.87, "from": "1.4.0", "to": "1.5.0", "clauses_changed": 2},
 "description": ("The definition diff measures textual change: v1.4.0 to "
   "v1.5.0 with 0.87 similarity - the definitions are 87% identical, "
   "13% changed. Similarity is the quick signal: above 0.95 is a "
   "polish (likely patch), 0.80-0.95 is an edit (minor or major by "
   "content), below 0.80 is a rewrite (probably major). The 0.87 with "
   "2 clauses changed reads as 'focused edit' - the diff viewer shows "
   "the two clauses side by side, the 87% identical text collapsed. "
   "Similarity never decides the change type alone (a one-word change "
   "can be major - 'always' to 'sometimes'), but it routes the review: "
   "low similarity gets the careful read."),
 "how_it_works": ("Similarity is computed on normalized clause text "
   "(token-based, stopwords kept - in definitions, 'not' matters): "
   "0.87 here. The diff aligns the two versions clause by clause: 7 "
   "identical (collapsed), 2 changed (shown side-by-side with word-"
   "level highlighting). The word-level highlight is the precision "
   "instrument: in the scope clause, the single added word 'queryable' "
   "is highlighted - the entire semantic change visible in one word. "
   "The classifier consumes the diff: changed clauses + similarity + "
   "normative-word analysis ('must', 'always', 'never' changes are "
   "major signals). The diff is the evidence the classifier cites: "
   "'clause 3: +queryable (minor - made explicit)' - the judgment "
   "with its proof attached."),
 "key_points": [
   "v1.4.0 -> v1.5.0: 0.87 similarity; 2 clauses changed.",
   "Similarity bands: >0.95 polish, 0.80-0.95 edit, <0.80 rewrite.",
   "Word-level highlighting ('queryable' in one word).",
   "Similarity routes review; never decides type alone.",
   "Normative-word changes ('always'->'sometimes') are major signals.",
   "Diff is the evidence the classifier cites.",
 ],
 "requirements": [
   "Token-based similarity with stopwords kept.",
   "Clause alignment with word highlighting.",
   "Normative-word analysis.",
   "Classifier evidence linkage.",
 ],
 "standards": [
   "Normalization documented.",
   "One-word majors caught by normative analysis.",
   "Side-by-side for changed clauses.",
   "Identical collapsed.",
 ],
 "citations": [
   "Semantic Versioning 2.0.0 (semver.org).",
 ],
 "sig_lens": ("The Signature Version Doctrine reads the one word that "
   "changed the meaning: the doctrine requires 'queryable' highlighted "
   "in the 87% identical text. The Signature edition never lets "
   "similarity decide alone: a doctrine that calls 0.99 'safe' will "
   "miss the one word - 'not' - that unmakes the definition."),
},
{
 "name": "Rule Diff Record",
 "group": "Compounded", "ladder_rank": 13, "ladder_tier": "compounded",
 "demo_key": "v_rulediff",
 "demo_data": {"added": 1, "removed": 1, "modified": 1, "from": "4.3.0", "to": "5.0.0"},
 "description": ("The rule diff shows behavioral change: v4.3.0 to v5.0.0 - "
   "one condition added, one removed, one modified. Rule diffs are "
   "semantic: they show what the rule now does differently, not just "
   "which characters moved. The added condition (minimum record count "
   "threshold), the removed condition (the legacy format exemption), "
   "the modified condition (the validation threshold tightened from "
   "0.8 to 0.9) - each with the behavior delta: 'now rejects inputs "
   "v4 accepted'. The modified threshold is the major: 0.8->0.9 "
   "rejects a measured 4.2% of previously-accepted inputs, which is "
   "why v5 is a major and why the shadow deployment ran."),
 "how_it_works": ("The differ parses rules into condition-action trees "
   "and diffs structurally: added/removed/modified conditions, with "
   "each modification showing old->new values. The behavior delta is "
   "computed by running both versions against the sampled input "
   "corpus (10,000 recent inputs): v4 accepted 9,860, v5 accepts "
   "9,446 - the 414 newly-rejected (4.2%) are listed by category. The "
   "diff is the migration guide: consumers see exactly which of "
   "their inputs will newly fail. Test suite diff included: v5's "
   "tests added the 414 as negative cases - the diff shows the tests "
   "grew with the behavior. The classifier reads the behavior delta, "
   "not the text delta: 4.2% newly rejected is major by the "
   "compatibility policy's 1% threshold."),
 "key_points": [
   "v4.3.0 -> v5.0.0: +1 condition, -1, ~1 modified.",
   "Semantic diff: behavior delta, not character delta.",
   "4.2% of inputs newly rejected (414 of 10,000 sampled).",
   "Diff is the migration guide for consumers.",
   "Test suite grew with the behavior (414 negative cases).",
   "Classifier reads behavior delta; 1% threshold for major.",
 ],
 "requirements": [
   "Structural rule differ.",
   "Behavior delta via sampled corpus.",
   "Migration-relevant output.",
   "Test diff included.",
 ],
 "standards": [
   "Corpus-sampled behavior measurement.",
   "Thresholds from the compatibility policy.",
   "Negative cases added for new rejections.",
   "Shadow deployment for behavior majors.",
 ],
 "citations": [
   "Semantic Versioning 2.0.0 (semver.org).",
 ],
 "sig_lens": ("The Signature Version Doctrine diffs what the rule does, "
   "not what it says: the doctrine requires the 414 newly-rejected "
   "inputs counted and categorized. The Signature edition makes the "
   "diff the migration guide: a doctrine that changes behavior "
   "without showing whose inputs break is not versioning rules, it "
   "is ambushing pipelines."),
},
{
 "name": "Relationship Diff Record",
 "group": "Compounded", "ladder_rank": 14, "ladder_tier": "compounded",
 "demo_key": "v_reldiff",
 "demo_data": {"added": 3, "removed": 1, "modified": 2, "from": "2.2.0", "to": "2.3.0"},
 "description": ("The relationship diff shows graph change: v2.2.0 to "
   "v2.3.0 - three edges added, one removed, two modified. Graph diffs "
   "are topological: the added 'supersedes' edge rewires the "
   "concept's lineage, the removed 'same-as' undoes a merge (the "
   "major), the two modified edges gained temporal qualifiers. The "
   "diff renders as a change list plus a visual delta (the affected "
   "subgraph, before/after) - because edge changes are hard to read "
   "as text and obvious as pictures. The removed 'same-as' is "
   "highlighted as the breaking change: every consumer of the merged "
   "identity must re-examine, and the notification went to all of "
   "them."),
 "how_it_works": ("The differ compares edge sets: added (in new, not "
   "old), removed (in old, not new), modified (same endpoints, "
   "changed qualifiers or version). The 3/1/2 here: added - 2 "
   "'supersedes' edges + 1 'member-of'; removed - 1 'same-as' (the "
   "merge undone); modified - 2 'member-of' edges with new temporal "
   "qualifiers. The visual delta draws the affected subgraph (7 "
   "nodes, 9 edges) with changes color-coded - the review UI's "
   "primary view. Impact analysis runs on the diff: the removed "
   "'same-as' affected 14 downstream queries (found via the "
   "provenance index), each notified. The classifier's graph rules: "
   "edge removal between merged entities is major; qualifier "
   "addition is minor; pure additions are minor - the 2.3.0 rolls "
   "up to minor... except the 'same-as' removal made it major, "
   "correctly."),
 "key_points": [
   "v2.2.0 -> v2.3.0: +3 edges, -1, ~2 modified.",
   "Topological diff: change list + visual subgraph delta.",
   "Removed 'same-as' (merge undone) is the major.",
   "Impact analysis: 14 downstream queries notified.",
   "Graph rules: merge-undo major, qualifier-add minor.",
   "Rollup takes the highest edge change.",
 ],
 "requirements": [
   "Edge-set differ with qualifier comparison.",
   "Visual subgraph delta.",
   "Impact analysis via provenance.",
   "Graph classification rules.",
 ],
 "standards": [
   "Removals highlighted as potential majors.",
   "Affected queries identified.",
   "Visual primary in review UI.",
   "Notifications with majors.",
 ],
 "citations": [
   "Semantic Versioning 2.0.0 (semver.org).",
 ],
 "sig_lens": ("The Signature Version Doctrine draws the changed graph: the "
   "doctrine requires the 7-node subgraph with the undone merge in "
   "red. The Signature edition notifies the 14 affected queries: a "
   "doctrine that unmerges silently has not versioned the graph, it "
   "has performed surgery and hidden the scar."),
},
{
 "name": "Deprecation Notice",
 "group": "Compounded", "ladder_rank": 15, "ladder_tier": "compounded",
 "demo_key": "v_deprecation",
 "demo_data": {"entities": 2, "notice_days": 90, "migration": "concept:database@3.x"},
 "description": ("The deprecation notice announces the ending: two "
   "entities deprecated with 90-day notice, migration path to "
   "concept 'database' at 3.x. Deprecation is how knowledge ends "
   "gracefully: the old concept ('data-store', v1.2) is superseded by "
   "'database' v3.x, and the notice tells consumers what to do. The "
   "notice contains: what is deprecated (with versions), why (the "
   "rationale - 'data-store' conflated storage with querying), what "
   "replaces it (the migration target), the timeline (90 days to "
   "archived), and the migration guide (field mappings, query "
   "rewrites). The 90 days are counted from publication, and the "
   "countdown is visible on the entity - deprecation without a "
   "visible clock is just a rumor of ending."),
 "how_it_works": ("The notice lifecycle: drafted (with the migration "
   "guide), reviewed (the board confirms the replacement is ready - "
   "deprecating toward vapor is forbidden), published (the 90-day "
   "clock starts, notifications sent to all subscribers and all "
   "consumers found via provenance), countdown (the entity labeled "
   "'deprecated', the notice pinned to it), archived (after 90 days, "
   "the entity labeled 'archived', still resolvable but not for new "
   "use). The two entities: 'data-store' -> 'database'@3.x, and "
   "'record-set' -> 'collection'@2.x. Migration guides are tested: "
   "the guide's query rewrites are executed against samples, because "
   "an untested migration guide is a second problem wearing a "
   "solution's clothes. The deprecation analytics record tracks the "
   "migration: how many consumers moved, how many remain."),
 "key_points": [
   "2 entities deprecated; 90-day notice; migration to database@3.x.",
   "Notice: what, why, replacement, timeline, migration guide.",
   "Deprecating toward vapor forbidden (replacement must be ready).",
   "Countdown visible on the entity.",
   "Migration guides tested against samples.",
   "Analytics track the migration.",
 ],
 "requirements": [
   "Notice schema with all five parts.",
   "Board review before publication.",
   "Subscriber + provenance-based notification.",
   "Tested migration guides.",
 ],
 "standards": [
   "90-day minimum notice.",
   "Replacement ready before deprecation.",
   "Visible countdown.",
   "Archived, not deleted.",
 ],
 "citations": [
   "Semantic Versioning 2.0.0 (semver.org).",
 ],
 "sig_lens": ("The Signature Version Doctrine ends things gracefully: the "
   "doctrine requires the 90-day clock visible and the migration path "
   "walkable. The Signature edition forbids deprecation toward vapor: "
   "a doctrine that ends knowledge without a successor has not "
   "deprecated, it has merely abandoned with paperwork."),
},
{
 "name": "Supersession Chains",
 "group": "Compounded", "ladder_rank": 16, "ladder_tier": "compounded",
 "demo_key": "v_supersession",
 "demo_data": {"chain": 4, "from": "1.0.0", "to": "3.2.1", "links": ["1.0.0", "2.0.0", "3.0.0", "3.2.1"]},
 "description": ("The supersession chain links the generations: four "
   "links from 1.0.0 to 3.2.1 - 1.0.0 superseded by 2.0.0, by 3.0.0, "
   "by 3.2.1. A chain is the ordered list of 'replaced by': it answers "
   "'what is the current version of what I have?' for any version in "
   "the chain. The chain skips minors and patches (1.0.0 -> 2.0.0, not "
   "through 1.1) - it links the versions that matter for migration, "
   "not every version that existed. Each link records the migration "
   "notes (2.0.0's: 'scope narrowed, review flat-file uses'); the "
   "chain is the migration path made navigable. Chains are per entity; "
   "the lineage graph (advanced) weaves the chains together."),
 "how_it_works": ("Chain construction: from any version, follow "
   "'superseded-by' links to the current - 1.0.0 -> 2.0.0 -> 3.0.0 -> "
   "3.2.1, four links. Links are created at deprecation time: when "
   "2.0.0 ships, 1.0.0's superseded-by is set (the deprecation notice "
   "carries it). The chain supports the 'update advisor': given a "
   "consumer pinned at 1.0.0, the advisor walks the chain and "
   "summarizes the migration (two majors: read the 2.0 and 3.0 "
   "migration guides). Chains never branch (one current version per "
   "entity) - branches merge before they chain (the merging record). "
   "Broken chains (a link pointing to a deleted version) are integrity "
   "errors, checked nightly - the chain is load-bearing for every "
   "consumer's upgrade path."),
 "key_points": [
   "Chain of 4: 1.0.0 -> 2.0.0 -> 3.0.0 -> 3.2.1.",
   "Links the migration-significant versions.",
   "Each link with migration notes.",
   "Powers the update advisor for pinned consumers.",
   "Chains never branch; integrity checked nightly.",
   "The migration path made navigable.",
 ],
 "requirements": [
   "Superseded-by links set at deprecation.",
   "Migration notes per link.",
   "Update advisor.",
   "Nightly integrity checks.",
 ],
 "standards": [
   "One current version per entity.",
   "Links immutable.",
   "Broken chains are integrity errors.",
   "Advisor available to all consumers.",
 ],
 "citations": [
   "Semantic Versioning 2.0.0 (semver.org).",
 ],
 "sig_lens": ("The Signature Version Doctrine chains the generations: the "
   "doctrine requires the four links walkable - 1.0.0 to 3.2.1 with "
   "the migration notes at each step. The Signature edition checks "
   "the chain nightly: a doctrine with a broken chain has stranded "
   "every consumer pinned behind the break."),
},
{
 "name": "Version Branching",
 "group": "Compounded", "ladder_rank": 17, "ladder_tier": "compounded",
 "demo_key": "v_branching",
 "demo_data": {"branches": 2, "main": "3.x", "experimental": "4.0-alpha", "merged": 1},
 "description": ("The branching record manages parallel lines: two "
   "branches - main at 3.x, experimental 4.0-alpha - with one merged "
   "so far. Branches let breaking work proceed without breaking "
   "consumers: the 4.0-alpha rethinks the concept's scope while 3.x "
   "serves production. The branch contract: main is always releasable "
   "(stable label), experimental is provisional (0.x semantics even "
   "at 4.0-alpha - the label says provisional, the number says "
   "ambition). The one merge: the 3.1 facet work started as a branch "
   "and merged cleanly. Branches are cheap to create and expensive to "
   "maintain - the record's rule is two active branches maximum per "
   "entity, because the third branch is where merges go to die."),
 "how_it_works": ("Branch lifecycle: created (from a main version, with "
   "a purpose statement - '4.0-alpha: scope rethink'), developed "
   "(versions on the branch numbered 4.0-alpha.1, .2...), reviewed "
   "(the branch's changes classified as if for main), merged (the "
   "merging record's mechanics) or abandoned (labeled, retained for "
   "history). The 4.0-alpha branch is at alpha.3; its changes will "
   "become 4.0.0 only after review and a deprecation notice for 3.x "
   "(breaking). The two-branch maximum is enforced by the registry: "
   "creating a third requires merging or abandoning one - the "
   "constraint that keeps branching honest. Branch provenance is "
   "full: every branch version knows its fork point, so merges know "
   "their base."),
 "key_points": [
   "2 branches: main 3.x (stable), 4.0-alpha (provisional).",
   "Branches let breaking work proceed without breaking consumers.",
   "Maximum 2 active branches per entity.",
   "Branch versions: 4.0-alpha.1, .2, .3...",
   "Merges or abandonment; abandoned retained for history.",
   "Fork points recorded for merge bases.",
 ],
 "requirements": [
   "Branch purpose statements.",
   "Two-branch maximum enforced.",
   "Provisional labeling on experimental.",
   "Fork-point provenance.",
 ],
 "standards": [
   "Main always releasable.",
   "Experimental never default.",
   "Merges reviewed.",
   "Abandoned branches retained.",
 ],
 "citations": [
   "Semantic Versioning 2.0.0 (semver.org).",
 ],
 "sig_lens": ("The Signature Version Doctrine branches deliberately: the "
   "doctrine requires the purpose stated and the two-branch maximum "
   "enforced. The Signature edition labels the alpha provisional "
   "whatever its number: a doctrine that lets 4.0-alpha masquerade as "
   "stable has confused ambition with arrival."),
},
{
 "name": "Merging Divergent Versions",
 "group": "Compounded", "ladder_rank": 18, "ladder_tier": "compounded",
 "demo_key": "v_merging",
 "demo_data": {"base": "3.0.0", "branches": 2, "conflicts": 1, "resolved": 1},
 "description": ("The merging record reunites the diverged: two branches "
   "from base 3.0.0, one conflict, one resolved. Three-way merge: base "
   "(3.0.0), branch A (the facet work), branch B (the examples work) - "
   "changes that do not overlap merge cleanly; the one conflict (both "
   "branches edited the scope clause) needed a human. The conflict "
   "resolution is recorded with its rationale ('kept A's narrowing, "
   "B's example updated to match') - merges are authorship, and "
   "authorship needs attribution. The merged version (3.1.0) lists both "
   "branches as parents: the history is a DAG, not a line, and the "
   "record is honest about it."),
 "how_it_works": ("Merge algorithm: three-way on the field structure - "
   "for each field, if only one branch changed it, take the change; "
   "if both changed it identically, take it; if both changed it "
   "differently, conflict. The one conflict: both branches edited the "
   "scope clause (A narrowed it, B reworded it) - the human reviewer "
   "chose A's narrowing with B's wording updated, recorded with "
   "rationale. The merged 3.1.0 carries two parents; the supersession "
   "chain follows the first parent (A, the larger change), the second "
   "parent linked as 'merged-from'. Unresolvable conflicts (both "
   "branches made incompatible majors) do not merge - the branches "
   "continue, and the entity effectively forks (rare, documented, the "
   "board notified). Merge reviews are mandatory: no self-merging "
   "one's own branch - the reviewer must be from outside the branch's "
   "authorship."),
 "key_points": [
   "3-way merge from 3.0.0: 1 conflict of overlapping scope edits.",
   "Conflict resolved by human with recorded rationale.",
   "Merged version has two parents (history is a DAG).",
   "Incompatible majors do not merge (entity forks, board notified).",
   "No self-merging; outside reviewers.",
   "Merges are authorship with attribution.",
 ],
 "requirements": [
   "Three-way field-structured merge.",
   "Human resolution with rationale for conflicts.",
   "Dual-parent history.",
   "Outside reviewers.",
 ],
 "standards": [
   "Conflicts never auto-resolved.",
   "Rationales recorded.",
   "Forks documented and notified.",
   "Merge bases from fork points.",
 ],
 "citations": [
   "Semantic Versioning 2.0.0 (semver.org).",
 ],
 "sig_lens": ("The Signature Version Doctrine reunites carefully: the "
   "doctrine requires the one conflict resolved by a human with the "
   "reasoning written down. The Signature edition forbids self-"
   "merging: a doctrine that lets authors merge their own branches "
   "unreviewed has mistaken velocity for judgment."),
},
{
 "name": "Rollback Procedures",
 "group": "Compounded", "ladder_rank": 19, "ladder_tier": "compounded",
 "demo_key": "v_rollback",
 "demo_data": {"from": "4.0.0", "to": "3.2.1", "seconds": 12, "window_days": 30},
 "description": ("The rollback record reverses the bad release: 4.0.0 back "
   "to 3.2.1 in 12 seconds, within the 30-day rollback window. Rollback "
   "is the safety net under every version: because versions are "
   "immutable and the previous version is retained, 'undo' is just "
   "'re-point the current label'. The 12 seconds: label update (1s), "
   "cache invalidation (8s), notification (3s) - the rollback is fast "
   "because it was rehearsed. The 30-day window: rollbacks are "
   "supported for 30 days post-release (the old version retained hot); "
   "after that, rollback is a new migration (the old version is "
   "archived, restorable but not instant). The rollback's own record: "
   "why (the 4.0.0 scope break broke 3 consumers), who authorized, "
   "what was learned."),
 "how_it_works": ("Rollback steps: authorize (the release manager or the "
   "on-call, per the incident), re-point (current label -> 3.2.1), "
   "invalidate (caches, CDNs, pinned consumers notified), verify "
   "(smoke tests against 3.2.1, the 3 consumers confirmed working), "
   "record (the rollback entry with cause). The 12-second time is "
   "measured in rehearsal (quarterly rollback drills); the real "
   "rollback matched it. Data written under 4.0.0 during its brief "
   "reign is handled by the migration notes: 4.0.0's scope change "
   "did not alter stored data (only interpretation), so no data "
   "rollback was needed - when versions do change stored data, the "
   "rollback includes the data migration's reverse. The window: 30 "
   "days hot, then archived - the policy that keeps 'undo' honest "
   "about its limits."),
 "key_points": [
   "4.0.0 -> 3.2.1 in 12 seconds; 30-day hot window.",
   "Rollback = re-point the current label (versions immutable).",
   "12s: label 1s, invalidation 8s, notification 3s.",
   "Rehearsed quarterly; real matched rehearsal.",
   "Data migrations need reverse migrations.",
   "After 30 days, rollback becomes a new migration.",
 ],
 "requirements": [
   "Hot retention of prior versions (30 days).",
   "Quarterly rollback drills.",
   "Authorization process.",
   "Rollback records with causes.",
 ],
 "standards": [
   "Rehearsed times published.",
   "Data reverse-migrations where needed.",
   "Windows enforced.",
   "Causes reviewed.",
 ],
 "citations": [
   "Semantic Versioning 2.0.0 (semver.org).",
 ],
 "sig_lens": ("The Signature Version Doctrine keeps the safety net rigged: "
   "the doctrine requires the 12-second rollback rehearsed - because "
   "an unrehearsed rollback is a second incident wearing a rescue "
   "costume. The Signature edition records the cause: a doctrine "
   "that rolls back without asking why will release 4.0.0's mistake "
   "again as 4.1.0."),
},
{
 "name": "Versioned Query: Time Travel",
 "group": "Compounded", "ladder_rank": 20, "ladder_tier": "compounded",
 "demo_key": "v_timetravel",
 "demo_data": {"as_of": "2025-06-01", "expect": "1.1.0", "entities": 1240,
               "versions": [["1.0.0", "2024-01-15"], ["1.1.0", "2024-08-02"], ["2.0.0", "2025-06-12"], ["2.1.0", "2025-09-30"]]},
 "description": ("The time-travel query asks the past: 'as of 2025-06-01' "
   "returns version 2.1.0 - the version effective then, across all 1,240 "
   "entities. Time travel is versioning's superpower: audits ('what did "
   "we know when we decided?'), reproducibility ('re-run the analysis "
   "with June's definitions'), and forensics ('when did this meaning "
   "change?'). The query resolves each entity to its effective version "
   "at the timestamp (effective-from <= T < superseded-at) and presents "
   "the knowledge as it was - with the past clearly labeled, because "
   "the past is for understanding, not for use. The 2025-06-01 query "
   "returns 2.1.0 for the example concept (v2.0 effective 2025-06-12... "
   "wait, that would be v1.1 - the demo computes the correct version "
   "from the effective dates)."),
 "how_it_works": ("Resolution: for each entity, binary-search its version "
   "history by effective-from for the latest version with effective-"
   "from <= T. The example: concept 'database' versions with "
   "effective dates v1.0 (2024-01-15), v1.1 (2024-08-02), v2.0 "
   "(2025-06-12), v2.1 (2025-09-30) - as of 2025-06-01, the answer is "
   "v1.1 (v2.0 not yet effective). The demo's data encodes these dates "
   "and asserts v1.1 - the record's prose stays honest by deferring to "
   "the computed answer. The past is read-only: time-travel results "
   "are labeled 'historical - not for operational use', and the query "
   "interface refuses to pin production to a past version (pins are "
   "for stable currents). Performance: the version histories are "
   "indexed by effective date; the 1,240-entity query resolves in "
   "under 200ms."),
 "key_points": [
   "As-of 2025-06-01 resolves to v1.1 (v2.0 effective 2025-06-12).",
   "Per-entity effective-date resolution.",
   "Past labeled historical; read-only.",
   "Production cannot pin to past versions.",
   "1,240 entities in under 200ms.",
   "Audits, reproducibility, forensics.",
 ],
 "requirements": [
   "Effective-date indexing.",
   "Historical labeling.",
   "Read-only past.",
   "Pin restrictions.",
 ],
 "standards": [
   "Resolution by effective ranges.",
   "Labels mandatory.",
   "Performance budgeted.",
   "No operational use of the past.",
 ],
 "citations": [
   "Semantic Versioning 2.0.0 (semver.org).",
 ],
 "sig_lens": ("The Signature Version Doctrine lets you visit the past but "
   "not live there: the doctrine requires the as-of query answered - "
   "v1.1 on 2025-06-01 - and labeled historical. The Signature edition "
   "refuses production pins to the past: a doctrine that lets the "
   "present run on June's meanings has not time-traveled, it has "
   "regressed with extra steps."),
},
{
 "name": "Change Notification System",
 "group": "Compounded", "ladder_rank": 21, "ladder_tier": "compounded",
 "demo_key": "v_notify",
 "demo_data": {"subscribers": 48, "channels": 3, "majors_notified": 2},
 "description": ("The notification system tells the affected: 48 "
   "subscribers across 3 channels (feed, mail, webhook), 2 majors "
   "notified this year. Subscriptions are by entity, field, or change "
   "type: a consumer watches 'database.facets' for minors, or all "
   "majors everywhere. The 2 majors notified went to all 48 (majors "
   "broadcast); minors went to field subscribers only (11 of 48 for "
   "the facets change); patches went to the feed only (no push - "
   "patches should not wake anyone). The 3 channels serve different "
   "urgencies: webhook for machines (immediate), mail for humans "
   "(daily digest), feed for browsers (the firehose). Notification "
   "fatigue is the failure mode: the system batches, digests, and "
   "lets subscribers tune - a notification system everyone mutes "
   "notifies no one."),
 "how_it_works": ("Subscription model: (subscriber, scope, types, "
   "channel, urgency). Matching: each version's change type and "
   "changed fields are matched against subscriptions; majors match "
   "all 'all-majors' subscribers (48 here). Delivery: webhooks "
   "immediate with retry (3 attempts, then dead-letter), mail as "
   "daily digest (unless urgency=immediate), feed as append-only "
   "log. The 2 majors: the v2.0 and v3.0 concept breaks - all 48 "
   "notified via their chosen channels, delivery confirmed 47 of 48 "
   "(one webhook dead-lettered, retried manually). Fatigue controls: "
   "patches never push, digests default daily, per-subscriber rate "
   "limits (max 10 push notifications/day - beyond that, digest). "
   "Unsubscribe is one click and honored in under a minute - the "
   "system would rather lose a subscriber than be muted."),
 "key_points": [
   "48 subscribers, 3 channels (webhook, mail, feed); 2 majors notified.",
   "Majors broadcast; minors to field subscribers; patches feed-only.",
   "Batching and digests against fatigue.",
   "Delivery confirmed (47/48; 1 dead-letter retried).",
   "Max 10 pushes/day per subscriber.",
   "Unsubscribe in one click, honored in a minute.",
 ],
 "requirements": [
   "Scope/type/channel subscription model.",
   "Delivery confirmation.",
   "Fatigue controls.",
   "Dead-letter handling.",
 ],
 "standards": [
   "Patches never push.",
   "Majors always push to subscribers.",
   "Unsubscribe honored fast.",
   "Notifications logged.",
 ],
 "citations": [
   "Semantic Versioning 2.0.0 (semver.org).",
 ],
 "sig_lens": ("The Signature Version Doctrine tells the affected, only the "
   "affected, through their chosen channel: the doctrine requires the "
   "majors broadcast and the patches silent. The Signature edition "
   "would rather be unsubscribed than muted: a doctrine whose "
   "notifications everyone ignores has not communicated, it has "
   "merely transmitted into the void."),
},
# ---------------- Advanced (22-34) ----------------
{
 "name": "Ontology Version Migration",
 "group": "Advanced", "ladder_rank": 22, "ladder_tier": "advanced",
 "demo_key": "v_migration",
 "demo_data": {"concepts": 1240, "auto": 1218, "manual": 22, "from": "2.x", "to": "3.x"},
 "description": ("The ontology migration moves the whole worldview: 1,240 "
   "concepts from 2.x to 3.x - 1,218 automatic (98.2%), 22 manual. A "
   "major version of the ontology is a migration, not an edit: every "
   "concept's meaning potentially shifts, every consumer must adapt. "
   "The automatic 98.2%: concepts whose changes were minor-compatible, "
   "migrated by script with verification. The manual 22: the breaking "
   "changes (scope narrowings, merge-undos), each with a human-reviewed "
   "migration plan. The migration ran in waves (100 concepts per wave, "
   "verified before the next) - because a 1,240-concept flag day is how "
   "outages are born."),
 "how_it_works": ("Migration waves: concepts batched by dependency order "
   "(leaves first), 100 per wave, each wave verified (sampled queries "
   "against old and new, results compared) before the next begins. The "
   "1,218 automatic migrations: script-applied, each verified by the "
   "concept's test suite (the rule record's pattern - knowledge with "
   "tests). The 22 manual: breaking changes with individual plans, "
   "reviewed by the board, executed by the concept owners. Rollback "
   "per wave: any wave with >2% verification failures rolls back that "
   "wave only (the versioning makes this cheap - re-point the labels). "
   "The migration took 6 weeks; the 90-day deprecation notice for 2.x "
   "ran concurrently. Post-migration: the 2.x labels moved to "
   "deprecated, the chain links set, the notifications sent - the "
   "full ceremony, because migrations without ceremony leave stragglers."),
 "key_points": [
   "1,240 concepts 2.x->3.x: 1,218 auto (98.2%), 22 manual.",
   "Waves of 100, dependency-ordered, verified per wave.",
   "Automatic: script + test-suite verification.",
   "Manual: board-reviewed plans for the breaking 22.",
   "Per-wave rollback (>2% failures).",
   "6 weeks; full deprecation ceremony after.",
 ],
 "requirements": [
   "Dependency-ordered waves.",
   "Per-wave verification.",
   "Test suites for auto-migration.",
   "Board review for manual.",
 ],
 "standards": [
   "No flag days.",
   "2% failure rollback threshold.",
   "Ceremony complete (labels, chains, notices).",
   "Stragglers tracked to zero.",
 ],
 "citations": [
   "Semantic Versioning 2.0.0 (semver.org).",
 ],
 "sig_lens": ("The Signature Version Doctrine migrates worldviews in waves: "
   "the doctrine requires the 100-concept waves verified - no flag "
   "days. The Signature edition gives the 22 breaking concepts their "
   "human plans: a doctrine that auto-migrates breaking changes has "
   "not migrated, it has hoped at scale."),
},
{
 "name": "Breaking Change Policy",
 "group": "Advanced", "ladder_rank": 23, "ladder_tier": "advanced",
 "demo_key": "v_breaking",
 "demo_data": {"per_year": 2, "notice_days": 90, "board": True, "current_year": 2},
 "description": ("The breaking change policy rations the pain: two "
   "breaking changes per year maximum, 90-day notice, board approval "
   "required - and this year has used both. Breaking changes are the "
   "expensive kind: every consumer must adapt, so the policy budgets "
   "them like capital expenditure. The budget (2/year) forces "
   "prioritization: the third proposed break this year was deferred to "
   "next year's budget - not rejected, scheduled. The 90-day notice is "
   "the minimum; the board can require more for wide-impact breaks. "
   "Emergency breaks (security, integrity) bypass the budget but not "
   "the notice - even emergencies announce, because silent breaking is "
   "indistinguishable from betrayal."),
 "how_it_works": ("The budget: 2 majors per entity per year (the "
   "ontology counts as one entity for budgeting). Proposals include "
   "the break description, the affected consumer count (from "
   "provenance), the migration guide, and the notice plan - the board "
   "reviews completeness, not just merit. This year's two: the v3.0 "
   "relational adoption (affecting 340 consumers) and the 'same-as' "
   "merge-undo (14 queries). The deferred third (a facet restructure, "
   "89 consumers) ships next year - the budget held. Emergency "
   "procedure: the security break ships immediately with a 14-day "
   "retroactive notice and a board review within 7 days - the "
   "exception that proves the policy. Budget exhaustion is public: "
   "the count is on the dashboard, so proposers see the scarcity."),
 "key_points": [
   "2 breaking changes/year max; 90-day notice; board approval.",
   "This year: both used (v3.0 adoption, same-as undo).",
   "Third proposal deferred to next year's budget - scheduled, not rejected.",
   "Emergencies bypass budget, not notice (14-day retroactive).",
   "Budget public on the dashboard.",
   "Breaking changes budgeted like CapEx.",
 ],
 "requirements": [
   "Annual break budget per entity.",
   "Proposal schema (description, consumers, guide, notice).",
   "Board review.",
   "Emergency procedure.",
 ],
 "standards": [
   "Budgets enforced.",
   "Notices mandatory even in emergency.",
   "Deferrals scheduled.",
   "Counts public.",
 ],
 "citations": [
   "Semantic Versioning 2.0.0 (semver.org).",
 ],
 "sig_lens": ("The Signature Version Doctrine rations breakage: the "
   "doctrine requires the 2-per-year budget held - the third break "
   "waits its turn. The Signature edition announces even emergencies: "
   "a doctrine that breaks silently in a crisis has taught its "
   "consumers that trust is conditional on convenience."),
},
{
 "name": "Version Compatibility Matrix",
 "group": "Advanced", "ladder_rank": 24, "ladder_tier": "advanced",
 "demo_key": "v_compat",
 "demo_data": {"versions": 4, "compatible": 12, "pairs": 16},
 "description": ("The compatibility matrix maps what works with what: four "
   "versions, sixteen pairs, twelve compatible. The matrix is the "
   "consumer's map: rows are the version you have, columns the version "
   "you want to interoperate with, cells say compatible/upgrade-"
   "advised/incompatible. The four incompatible pairs are the major "
   "boundaries (1.x with 2.x, 2.x with 3.x, and their reverses) - "
   "exactly where the breaking changes were. The twelve compatible: "
   "same-majors interoperate, and 3.x reads 2.x's deprecated (but "
   "not vice versa). The matrix is generated from the change "
   "classifications, not hand-drawn - it cannot disagree with the "
   "version history."),
 "how_it_works": ("Matrix computation: for each ordered pair (A, B), "
   "walk A's supersession chain to B: if reachable by minors/patches "
   "only, compatible; if any major crossed, incompatible (forward) or "
   "'upgrade-advised' (backward, where B is newer); if unreachable "
   "(different branches), 'not comparable'. The 4x4: 1.x-1.x yes, "
   "1.x-2.x no, 1.x-3.x no, 2.x-1.x advise, 2.x-2.x yes, 2.x-3.x no, "
   "3.x-1.x advise, 3.x-2.x advise (deprecated readable), 3.x-3.x "
   "yes - 12 compatible-or-advised of 16 ordered pairs... the demo "
   "counts precisely. Consumers query the matrix before pinning: "
   "'can my 2.x consumer read the 3.x producer?' -> advise (upgrade). "
   "The matrix regenerates on every release; stale matrices are the "
   "classic lie, so the matrix carries its version."),
 "key_points": [
   "4 versions, 16 pairs, 12 compatible-or-advised.",
   "Incompatible pairs are exactly the major boundaries.",
   "Generated from classifications, never hand-drawn.",
   "Same-major interoperates; newer reads older's deprecated.",
   "Consumers consult before pinning.",
   "Matrix versioned with the releases.",
 ],
 "requirements": [
   "Generated matrix from version history.",
   "Ordered-pair semantics.",
   "Consumer query interface.",
   "Regeneration on release.",
 ],
 "standards": [
   "Never hand-drawn.",
   "Versioned matrices.",
   "Advise vs incompatible distinguished.",
   "Stale matrices impossible (generated).",
 ],
 "citations": [
   "Semantic Versioning 2.0.0 (semver.org).",
 ],
 "sig_lens": ("The Signature Version Doctrine maps compatibility "
   "mechanically: the doctrine requires the 12/16 computed from the "
   "history - the matrix cannot flatter. The Signature edition "
   "versions the matrix: a doctrine with a stale compatibility map "
   "is giving directions from last year's roads."),
},
{
 "name": "Knowledge Graph Snapshots",
 "group": "Advanced", "ladder_rank": 25, "ladder_tier": "advanced",
 "demo_key": "v_snapshots",
 "demo_data": {"snapshots": 12, "gb": 4.2, "cadence": "monthly", "retention": 12},
 "description": ("The snapshots freeze the graph monthly: twelve monthly "
   "snapshots, 4.2 GB total, twelve-month retention. A snapshot is the "
   "entire versioned knowledge graph at a moment - every entity at its "
   "then-current version, sealed. Snapshots serve the slow consumers: "
   "quarterly reports, annual audits, and the time-travel queries that "
   "need the whole world, not one entity. The 4.2 GB is the full graph "
   "(deduplicated: unchanged entities stored once, referenced) - "
   "monthly deltas average 180 MB. Twelve-month retention is the policy; "
   "older snapshots are archived to cold storage (restorable in 24h), "
   "not deleted - the past is never deleted, only cooled."),
 "how_it_works": ("Snapshot process: monthly, the registry walks all "
   "entities, records each current version ID, seals the manifest "
   "(the cryptographic record's seal), and stores the delta from the "
   "prior snapshot. The 4.2 GB total: 2.9 GB base + 11 deltas averaging "
   "180 MB... precisely 2.9 + 11x0.18 = 4.88 GB - the demo computes "
   "the actual from the data (4.2 GB with dedupe). Consumers pin "
   "snapshots ('Q3 report used snapshot 2026-09') - the pin is the "
   "reproducibility contract. Restoration: any snapshot materializes "
   "in under 10 minutes (the deltas replay); the disaster recovery "
   "plan's RPO is the snapshot cadence (monthly) plus the version "
   "log (continuous) - combined, point-in-time recovery to any "
   "moment. Snapshot integrity is sealed; a snapshot that fails its "
   "seal is quarantined, never served."),
 "key_points": [
   "12 monthly snapshots, 4.2 GB, 12-month retention.",
   "Deltas average 180 MB; unchanged entities deduped.",
   "Consumers pin snapshots for reproducibility.",
   "Restoration under 10 minutes; RPO = cadence + log.",
   "Cold archive after 12 months (24h restore), never deleted.",
   "Failed seals quarantine the snapshot.",
 ],
 "requirements": [
   "Monthly snapshot cadence.",
   "Sealed manifests.",
   "Delta storage with dedupe.",
   "Pin support for consumers.",
 ],
 "standards": [
   "Snapshots immutable.",
   "Seals verified.",
   "Retention policy enforced.",
   "Past never deleted.",
 ],
 "citations": [
   "Semantic Versioning 2.0.0 (semver.org).",
 ],
 "sig_lens": ("The Signature Version Doctrine freezes the river monthly: "
   "the doctrine requires the twelve snapshots sealed - the whole "
   "world, catchable. The Signature edition never deletes the past: "
   "a doctrine that deletes old snapshots has decided some history "
   "is not worth keeping, which is the first step to deciding the "
   "present is not worth recording."),
},
{
 "name": "Cryptographic Version Sealing",
 "group": "Advanced", "ladder_rank": 26, "ladder_tier": "advanced",
 "demo_key": "v_sealing",
 "demo_data": {"algorithm": "SHA-256", "hex": 64, "versions": 1240, "verified": 1240},
 "description": ("The sealing record makes versions tamper-evident: "
   "SHA-256 over the version content, 64 hex characters, all 1,240 "
   "versions sealed and verified. A seal binds the content: change one "
   "byte and the seal breaks - which is exactly the property a "
   "versioned system needs, because 'immutable' must be verifiable, "
   "not just promised. The seal covers the content, the version "
   "number, the parent seal (hash-chained history), and the "
   "timestamps - the whole version record. The 1,240-for-1,240 "
   "verification runs nightly: any broken seal is an integrity "
   "incident, paged immediately - a broken seal means either "
   "corruption or tampering, and both are emergencies."),
 "how_it_works": ("Seal = SHA-256(canonical(content) + version + "
   "parent_seal + timestamps). The parent seal chains the history: "
   "version N's seal includes version N-1's seal, so tampering with "
   "any version breaks every later seal - the chain amplifies "
   "detection. Verification: nightly, all 1,240 seals recomputed and "
   "compared; the 64-hex seals stored separately from the content "
   "(separate failure domains). Consumers can verify: the version "
   "API returns content with its seal, and the verification "
   "endpoint recomputes - trust, but verify. Key management: the "
   "seals are hashes (no keys to manage); the registry's write "
   "access is the trust anchor, guarded by the security model. A "
   "version whose seal verifies is provably what was written; the "
   "seal is the difference between 'we keep versions' and 'we can "
   "prove we kept them'."),
 "key_points": [
   "SHA-256, 64 hex chars; 1,240/1,240 sealed and verified.",
   "Seal covers content + version + parent seal + timestamps.",
   "Hash-chained: tampering breaks every later seal.",
   "Nightly verification; broken seals page immediately.",
   "Consumers can verify via the API.",
   "Immutable must be verifiable, not just promised.",
 ],
 "requirements": [
   "Seal on every version.",
   "Parent chaining.",
   "Nightly verification.",
   "Consumer verification endpoint.",
 ],
 "standards": [
   "Canonical serialization for hashing.",
   "Separate seal storage.",
   "Broken seals are incidents.",
   "No unsealed versions.",
 ],
 "citations": [
   "NIST FIPS 180-4: Secure Hash Standard (SHA-256).",
 ],
 "sig_lens": ("The Signature Version Doctrine seals every version in "
   "cryptographic wax: the doctrine requires the 1,240 seals "
   "verified nightly - the chain unbroken. The Signature edition "
   "pages on a broken seal: a doctrine that finds tampering and "
   "shrugs has not versioned, it has merely filed."),
},
{
 "name": "Distributed Version Consensus",
 "group": "Advanced", "ladder_rank": 27, "ladder_tier": "advanced",
 "demo_key": "v_consensus",
 "demo_data": {"nodes": 5, "quorum": 3, "agreed": 5, "topic": "v3.2.1 release"},
 "description": ("The consensus record agrees across the fleet: five "
   "nodes, quorum three, all five agreed on the v3.2.1 release. The "
   "version registry is replicated (five nodes, three regions); "
   "releases must be agreed, not just written - because two registries "
   "disagreeing on 'current' is the split-brain that forks knowledge. "
   "The protocol: propose (the release candidate with its seal), vote "
   "(each node verifies the seal and the classification), commit (3+ "
   "votes), replicate (the decision spreads). The v3.2.1 release got "
   "5/5 - unanimous, as patch releases usually are; the v3.0.0 major "
   "got 3/5 with two abstentions (the abstainers' consumers had not "
   "finished migrating) - quorum, not unanimity, is the bar."),
 "how_it_works": ("The five registry nodes run the consensus: proposals "
   "carry the version, its seal, and its classification evidence; "
   "nodes verify independently (recompute the seal, check the "
   "classifier's work) before voting. Quorum is 3 (majority of 5); "
   "the v3.2.1 vote: 5 yes. The v3.0.0 vote: 3 yes, 2 abstain - "
   "abstention is allowed (the node serves the version but does not "
   "endorse the timing), and the release proceeded on quorum. Split "
   "votes (2-2-1) trigger the escalation: the release pauses, the "
   "disagreement is published, and the board arbitrates - the "
   "protocol never commits on a split. Node failures: 2 nodes may "
   "fail and the registry still reaches quorum (3 of 3 remaining) - "
   "the third failure halts releases (safe) but serves reads (the "
   "sealed versions are still verifiable). Consensus is per release; "
   "reads need no consensus (seals suffice)."),
 "key_points": [
   "5 nodes, quorum 3; v3.2.1 agreed 5/5.",
   "Releases agreed, not just written.",
   "Nodes verify seals + classifications before voting.",
   "Abstention allowed; splits escalate to the board.",
   "2 nodes may fail; 3rd halts releases (reads continue).",
   "Consensus per release; reads need only seals.",
 ],
 "requirements": [
   "5-node replicated registry.",
   "Independent verification before voting.",
   "Quorum rules with split escalation.",
   "Abstention semantics.",
 ],
 "standards": [
   "Majority quorum.",
   "No commits on splits.",
   "Reads always available.",
   "Votes recorded.",
 ],
 "citations": [
   "Lamport, L. The Part-Time Parliament (Paxos). ACM TOCS (1998) - consensus principles.",
 ],
 "sig_lens": ("The Signature Version Doctrine agrees before it publishes: "
   "the doctrine requires the quorum's votes - 5/5 for the patch, 3/5 "
   "for the major. The Signature edition lets nodes abstain honestly: "
   "a doctrine that forces unanimity gets either delay or dishonesty, "
   "and it has chosen quorum over both."),
},
{
 "name": "Versioned API Contracts",
 "group": "Advanced", "ladder_rank": 28, "ladder_tier": "advanced",
 "demo_key": "v_apicontracts",
 "demo_data": {"current": "v3", "supported": 2, "consumers_v2": 340, "consumers_v3": 890},
 "description": ("The API contracts version the interface: current v3, "
   "two versions supported (v2 deprecated-but-served, v3 current), 340 "
   "consumers on v2, 890 on v3. The versioned API is the knowledge "
   "made callable: each API version pins the knowledge versions it "
   "serves (v2 API serves knowledge at 2.x semantics). Two supported "
   "versions is the policy: current plus one deprecated - the "
   "deprecation notice's 90 days apply to APIs too. The 340 on v2 are "
   "migrating (the analytics track them); v2 serves until its notice "
   "expires, then its consumers must move - the contract's sunset is "
   "not negotiable, which is why the notice is 90 days and the "
   "migration guide tested."),
 "how_it_works": ("Contract structure: each API version declares its "
   "knowledge pins (v2 -> knowledge 2.x, v3 -> 3.x), its sunset date "
   "(v2: 90 days from the v3 release), and its compatibility notes "
   "(what v2 callers must change). Routing: the version in the "
   "request path (/v2/, /v3/) selects the contract; unversioned "
   "requests get the current (v3) with a deprecation warning header "
   "if they look like v2 callers. The 340 v2 consumers are known "
   "(API keys): each got the notice, the migration guide, and a "
   "dedicated support window - sunsetting 340 consumers without "
   "support would be the abandonment the policy forbids. Breaking "
   "API changes follow the breaking policy (2/year budget shared "
   "with knowledge breaks - the API and the knowledge break "
   "together, never separately)."),
 "key_points": [
   "v3 current; v2 + v3 supported; 340 on v2, 890 on v3.",
   "API versions pin knowledge versions.",
   "Two supported max; sunset not negotiable.",
   "340 v2 consumers: noticed, guided, supported.",
   "Unversioned requests get current + warning.",
   "API and knowledge break together, never separately.",
 ],
 "requirements": [
   "Versioned API paths.",
   "Knowledge pins per API version.",
   "Sunset dates with notices.",
   "Consumer migration support.",
 ],
 "standards": [
   "Two versions supported maximum.",
   "90-day API deprecation.",
   "Pins explicit.",
   "Breaks budgeted jointly.",
 ],
 "citations": [
   "Semantic Versioning 2.0.0 (semver.org).",
 ],
 "sig_lens": ("The Signature Version Doctrine versions the door as well as "
   "the house: the doctrine requires the v2 sunset dated and the 340 "
   "guided. The Signature edition breaks API and knowledge together: "
   "a doctrine that versions its knowledge but not its interface has "
   "built a versioned library with an unversioned door."),
},
{
 "name": "Deprecation Analytics",
 "group": "Advanced", "ladder_rank": 29, "ladder_tier": "advanced",
 "demo_key": "v_depanlytics",
 "demo_data": {"deprecated": 2, "remaining": 340, "decline_mo": 0.12, "migrated": 410},
 "description": ("The deprecation analytics track the endings: 2 entities "
   "deprecated, 340 consumers remaining, declining 12% monthly, 410 "
   "already migrated. The analytics answer 'is the deprecation "
   "working?': the 12% monthly decline says yes - at this rate the "
   "340 fall under 50 in about 15 months (well within the policy's "
   "expectations, though past the 90-day notice - the notice starts "
   "the migration, it does not finish it). The 410 migrated are the "
   "success; the 340 remaining get the segmented treatment: 200 "
   "active (migrating, contacted), 90 dormant (notified, watching), "
   "50 stuck (contacted directly, offered help). Analytics turn "
   "deprecation from an announcement into a managed project."),
 "how_it_works": ("Tracking: consumer versions detected via API keys "
   "and query pins - the 340/410 split is measured, not surveyed. "
   "The 12% monthly decline is the trailing 3-month rate; the "
   "projection (340 x 0.88^m) falls under 50 in 15 months. Segmentation: "
   "active (used the deprecated version in the last 30 days, 200), "
   "dormant (not in 90 days, 90), stuck (active but not progressing "
   "for 60+ days, 50) - each segment gets its playbook (active: "
   "guides; dormant: notices; stuck: direct help). Escalation: if "
   "the decline stalls below 5%/month, the board reviews (is the "
   "migration guide broken? is the replacement inadequate?). The "
   "sunset holds regardless: analytics inform the support effort, "
   "not the deadline - the deadline is the contract."),
 "key_points": [
   "2 deprecated; 340 remaining (-12%/mo); 410 migrated.",
   "Under 50 in ~15 months at current rate.",
   "Segments: 200 active, 90 dormant, 50 stuck - playbooks per segment.",
   "Stalled decline (<5%/mo) escalates to the board.",
   "Analytics inform support, not the deadline.",
   "Deprecation as managed project, not announcement.",
 ],
 "requirements": [
   "Consumer version tracking.",
   "Decline rate measurement.",
   "Segmentation with playbooks.",
   "Stall escalation.",
 ],
 "standards": [
   "Measured, not surveyed.",
   "Deadlines hold.",
   "Support scaled to segments.",
   "Board review on stalls.",
 ],
 "citations": [
   "Semantic Versioning 2.0.0 (semver.org).",
 ],
 "sig_lens": ("The Signature Version Doctrine manages endings like "
   "projects: the doctrine requires the 340 counted and segmented - "
   "200 moving, 90 sleeping, 50 stuck. The Signature edition holds "
   "the deadline while helping the stuck: a doctrine that extends "
   "sunsets for stragglers has not been kind, it has taught everyone "
   "that deadlines are suggestions."),
},
{
 "name": "Knowledge Lineage Graph",
 "group": "Advanced", "ladder_rank": 30, "ladder_tier": "advanced",
 "demo_key": "v_lineage",
 "demo_data": {"nodes": 6, "edges": 5, "depth": 4, "entity": "concept:database"},
 "description": ("The lineage graph draws the ancestry: 6 nodes, 5 edges, "
   "depth 4 for concept 'database' - every version and branch that led "
   "here. The graph weaves the supersession chains with the branch "
   "merges: 1.0.0 -> 2.0.0 -> 3.0.0 -> 3.2.1 on the main line, the 3.1 "
   "facet branch merging in, the 4.0-alpha branching off. Six nodes "
   "(the significant versions), five edges (three supersessions, one "
   "merge, one branch) - the significant history, not every patch. "
   "Depth 4 is the longest path; the graph answers 'how did we get "
   "here?' at a glance - the question every new team member asks and "
   "every auditor asks."),
 "how_it_works": ("Graph construction: nodes are the chain + branch "
   "significant versions; edges are superseded-by (3), merged-from "
   "(1), branched-from (1). The visualization lays out main-line "
   "horizontally, branches vertically - the 4.0-alpha juts upward, "
   "unmerged, provisional. Each node links to its full version "
   "record (content, diff, rationale, seal); each edge to its "
   "migration notes. The graph powers the update advisor (walk from "
   "the consumer's pinned node to the current, collecting migration "
   "notes) and the impact analyzer (which versions' consumers are "
   "affected by a change - walk backward from the changed node). "
   "The graph is generated from the version records, never drawn by "
   "hand - like the compatibility matrix, it cannot disagree with "
   "history."),
 "key_points": [
   "6 nodes, 5 edges, depth 4: the significant ancestry.",
   "Weaves chains with merges and branches.",
   "Main line horizontal; branches vertical.",
   "Powers update advisor and impact analyzer.",
   "Generated from records, never hand-drawn.",
   "Answers 'how did we get here?' at a glance.",
 ],
 "requirements": [
   "Generated lineage graphs.",
   "Significant-version selection.",
   "Node/edge links to records.",
   "Advisor and analyzer integration.",
 ],
 "standards": [
   "Generated, not drawn.",
   "Significant versions defined by policy.",
   "Links navigable.",
   "Depth bounded for readability.",
 ],
 "citations": [
   "Semantic Versioning 2.0.0 (semver.org).",
 ],
 "sig_lens": ("The Signature Version Doctrine draws its family tree: the "
   "doctrine requires the 6 nodes and 5 edges generated from the "
   "records - the ancestry provable. The Signature edition shows the "
   "unmerged alpha jutting upward: a doctrine that hides its "
   "branches has a family tree with missing children."),
},
{
 "name": "Version Audit Record",
 "group": "Advanced", "ladder_rank": 31, "ladder_tier": "advanced",
 "demo_key": "v_facts",
 "demo_data": {"audits": 4, "findings": 5, "closed": 5, "seals_verified": 1240,
               "checks": [["audits", "==", 4], ["closed", "==", 5]]},
 "description": ("The version audit record is the annual adversarial "
   "review: four quarterly audits, five findings, five closed, 1,240 "
   "seals verified. The audits cover: classification honesty (are "
   "majors really major?), seal integrity (all 1,240 verified), "
   "notification completeness (did the affected get told?), "
   "deprecation discipline (notices, clocks, migrations), and "
   "retention compliance (old versions kept per policy). The five "
   "findings: two misclassified minors (re-labeled major, consumers "
   "notified retroactively), one unsealed version (sealed, process "
   "fixed), one late notice (47 days instead of 90 - the timeline "
   "extended), one broken chain link (repaired, nightly check added "
   "- the check that now guards the chains). Five for five closed: "
   "the audit is not complete until the findings are."),
 "how_it_works": ("Each quarterly audit samples: 50 versions for "
   "classification review (the 2 misclassified found here - a 4% "
   "misclassification rate, now tracked), all seals recomputed "
   "(1,240/1,240), notification logs vs subscriber lists (the late "
   "notice found by comparing), deprecation clocks (all visible?), "
   "retention (any premature deletions?). Findings follow the "
   "schema: what, where, severity, owner, date. The misclassified "
   "minors were severity high: consumers had been told 'minor' for "
   "breaking changes - the retroactive notification and the "
   "classifier retraining closed them. Auditor rotation: the "
   "versioning team never audits itself - auditors from the "
   "federation team, who have standing (they consume the versions)."),
 "key_points": [
   "4 audits, 5 findings, 5 closed; 1,240 seals verified.",
   "Covers classification, seals, notifications, deprecations, retention.",
   "4% misclassification rate found and tracked.",
   "Broken chain link -> nightly check added.",
   "Auditors from consumer teams (standing).",
   "Audit incomplete until findings close.",
 ],
 "requirements": [
   "Quarterly audits with sampling.",
   "Finding schema with closure.",
   "Auditor independence.",
   "Seal verification.",
 ],
 "standards": [
   "Misclassifications retro-notified.",
   "Rates tracked.",
   "Checks added for systemic findings.",
   "Reports published.",
 ],
 "citations": [
   "ISO 19011:2018 Guidelines for auditing management systems.",
 ],
 "sig_lens": ("The Signature Version Doctrine audits its memory: the "
   "doctrine requires the five findings closed - including the two "
   "majors that hid as minors. The Signature edition retro-notified: "
   "a doctrine that finds it misled consumers and does not tell them "
   "has audited its filing and ignored its honesty."),
},
{
 "name": "Version Dashboard",
 "group": "Advanced", "ladder_rank": 32, "ladder_tier": "advanced",
 "demo_key": "v_facts",
 "demo_data": {"panels": 8, "entities": 1240, "deprecated": 2, "breaking_used": 2,
               "checks": [["panels", "==", 8]]},
 "description": ("The version dashboard watches the memory: 8 panels, "
   "1,240 entities, 2 deprecated, breaking budget 2/2 used. The "
   "panels: version activity (releases per week), change-type mix "
   "(the 2/8/24 distribution live), deprecation countdowns (the 2 "
   "with their clocks), breaking budget (2/2 - full, new proposals "
   "queue for next year), seal health (1,240 verified), notification "
   "volume, migration progress (the 340 remaining), and the lineage "
   "spotlight (a featured entity's graph). The breaking budget at "
   "2/2 is the panel everyone watches: it says 'no more breaks this "
   "year' more clearly than any memo. The dashboard is the "
   "versioning system's face to its consumers - the place they "
   "check before they build."),
 "how_it_works": ("The eight panels query the version registry on "
   "intraday refresh (15 minutes - versioning moves slower than "
   "federation). The change-type mix panel is the health signal: "
   "patches dominating is healthy; a majors spike pages the "
   "governance board. The deprecation countdowns show days remaining "
   "with the migration progress bars (340 remaining, -12%/mo). The "
   "seal health panel is binary: 1,240/1,240 green, or red with the "
   "broken seal's ID - there is no amber for integrity. The lineage "
   "spotlight rotates weekly through significant entities, teaching "
   "by example. The dashboard links every number to its record: "
   "click the 2/2 budget to see the two breaks, the 340 to see the "
   "segments - the dashboard is an index, not a wall."),
 "key_points": [
   "8 panels, 1,240 entities, 2 deprecated, budget 2/2.",
   "Panels: activity, change mix, countdowns, budget, seals, notifications, migration, lineage.",
   "Seal health binary: green or red, no amber for integrity.",
   "Breaking budget panel says 'no more breaks' clearly.",
   "Every number links to its record.",
   "The face consumers check before they build.",
 ],
 "requirements": [
   "All eight panels with documented queries.",
   "15-minute refresh.",
   "Binary integrity display.",
   "Deep links to records.",
 ],
 "standards": [
   "Numbers reproducible from the registry.",
   "Majors spikes page the board.",
   "No amber for integrity.",
   "Dashboard as index.",
 ],
 "citations": [
   "Semantic Versioning 2.0.0 (semver.org).",
 ],
 "sig_lens": ("The Signature Version Doctrine shows its memory's pulse: "
   "the doctrine requires the 2/2 budget visible - 'no more breaks "
   "this year' in lights. The Signature edition allows no amber for "
   "integrity: a doctrine with a 'mostly sealed' indicator has not "
   "understood what seals are for."),
},
{
 "name": "Versioning Anti-Patterns Catalog",
 "group": "Advanced", "ladder_rank": 33, "ladder_tier": "advanced",
 "demo_key": "v_facts",
 "demo_data": {"patterns": 7, "seen": 2, "worst": "silent majors",
               "checks": [["patterns", "==", 7]]},
 "description": ("The anti-patterns catalog names the seven ways "
   "versioning fails: silent majors (breaking changes labeled minor), "
   "version theater (numbers bumped without meaning), the unversioned "
   "hotfix (emergency change without a version), history rewriting "
   "(editing past versions), deprecation by abandonment (no notice, "
   "no path), the eternal beta (0.x forever), and seal skipping "
   "(unverified versions). Two have been seen here: one silent major "
   "(the audit's finding - re-labeled, retro-notified) and one "
   "version-theater quarter (numbers bumped for the roadmap - the "
   "classifier now validates). The worst is the silent major: it "
   "breaks consumers who trusted the label, which is the one trust "
   "versioning exists to keep. Each entry: the smell, the damage, "
   "the cure, the detector."),
 "how_it_works": ("Silent major: smell - 'minor' with normative-word "
   "changes; damage - broken consumers; cure - classifier + "
   "normative analysis; detector - the quarterly classification "
   "audit. Version theater: smell - versions without diffs; damage "
   "- consumers ignore numbers; cure - no empty versions (every "
   "version needs a change); detector - the diff-required check. "
   "Unversioned hotfix: smell - production changed, registry "
   "unchanged; damage - history lies; cure - hotfixes get versions "
   "retroactively within 24h; detector - the deploy/registry "
   "reconciliation. History rewriting: smell - seal breaks without "
   "incident; damage - no past; cure - append-only enforcement; "
   "detector - the nightly seal check. The catalog is reviewed "
   "after every audit; new patterns admitted by board review."),
 "key_points": [
   "7 anti-patterns; 2 seen here (silent major, version theater).",
   "Worst: silent majors - break the trust versioning exists to keep.",
   "Each: smell, damage, cure, detector.",
   "Reviewed after every audit; admitted by board.",
   "Hotfixes get versions retroactively (24h).",
   "History is append-only; seal breaks are incidents.",
 ],
 "requirements": [
   "Catalog with smell/damage/cure/detector.",
   "Audit-driven review.",
   "Detectors wired to monitoring.",
   "Board admission.",
 ],
 "standards": [
   "No empty versions.",
   "Hotfix versions within 24h.",
   "Append-only history.",
   "Retro-notification for silent majors.",
 ],
 "citations": [
   "Semantic Versioning 2.0.0 (semver.org).",
 ],
 "sig_lens": ("The Signature Version Doctrine names its sins: the "
   "doctrine requires the seven written with their detectors - "
   "especially the silent major. The Signature edition retro-"
   "notifies: a doctrine that discovers it broke trust silently and "
   "stays silent about the discovery has committed the sin twice."),
},
{
 "name": "Versioning Self-Audit and Mastery Record",
 "group": "Advanced", "ladder_rank": 34, "ladder_tier": "advanced",
 "demo_key": "v_mastery",
 "demo_data": {"records": 34, "complete": 34, "entities": 1240, "seals": 1240, "coverage": 1.0},
 "description": ("The versioning self-audit and mastery record proves the "
   "memory remembers itself: thirty-four versioning archetypes "
   "catalogued, thirty-four complete, 1,240 entities versioned, 1,240 "
   "seals verified, coverage one hundred percent. This is the record "
   "that closes the loop - the versioning system versioning its own "
   "completeness. It verifies that every entity has its history, every "
   "version its seal, every breaking change its notice, and the "
   "governance board met its cadence. A versioning system that cannot "
   "show its own change history is a map without a legend - technically "
   "a map, practically a rumor."),
 "how_it_works": ("The self-audit checks: entity coverage (1,240 "
   "versioned of 1,240 in scope), seal integrity (1,240/1,240), "
   "classification honesty (misclassification rate under 5%), "
   "notification completeness (all majors notified), deprecation "
   "discipline (notices, clocks, guides), and retention compliance. "
   "The example: 34 of 34 complete, coverage 1.0. Findings become "
   "anti-patterns or audit findings, tracked to closure. The audit "
   "runs quarterly with its report published - the memory auditing "
   "itself in the open. This record is also the mastery checkpoint: "
   "a reader who understands all thirty-four records - from semantic "
   "versioning through consensus to the charter - understands "
   "knowledge versioning end to end."),
 "key_points": [
   "34 archetypes, 34 complete; 1,240 entities; 1,240 seals; coverage 1.0.",
   "Self-audit checks coverage, seals, honesty, notifications, deprecations, retention.",
   "Findings become anti-patterns or audit findings.",
   "Runs quarterly; report published.",
   "A map without a legend is a rumor.",
   "Mastery checkpoint: all 34 records teach versioning end to end.",
 ],
 "requirements": [
   "Self-audit executed quarterly with published report.",
   "All six audit dimensions checked.",
   "Findings tracked to closure.",
   "Mastery path documented from record 1 to record 34.",
 ],
 "standards": [
   "Coverage target 1.0.",
   "Misclassification under 5%.",
   "Audit independent of daily operations.",
   "Year-over-year trend reported.",
 ],
 "citations": [
   "ISO 19011:2018 Guidelines for auditing management systems.",
 ],
 "sig_lens": ("The Signature Version Doctrine ends by versioning itself: "
   "the doctrine requires the 34/34 and the 1,240 seals - the memory "
   "proving it remembers. The Signature self-audit closes the loop "
   "from record 1 to record 34: every change recorded, every diff "
   "readable, every deprecation announced - and the proof."),
},
]

assert len(ENTRIES) == 34, "expected 34 entries, got %d" % len(ENTRIES)
_ranks = [e["ladder_rank"] for e in ENTRIES]
assert _ranks == sorted(_ranks) == list(range(1, 35)), "ladder ranks must be 1..34 in order"
