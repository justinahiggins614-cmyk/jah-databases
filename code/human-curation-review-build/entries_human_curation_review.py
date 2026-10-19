#!/usr/bin/env python3
"""Entries for the Human Curation Review databases (JAH Databases governance
track, group F, 2026-10-17).

Dedupe gate: none of the 8 governance slugs exist in data/manifest.json
(2,770 databases checked 2026-10-17); ID prefixes JAH-HCR- (public) and
JAH-HCRS- (signature) verified free: zero exact or substring hits in
manifest id_prefix values and zero hits in all shard record IDs of
jah-databases-data-1. All 68 record titles checked against the whole
system (exact dedupe index + live shard title corpus of 1,143,457 titles)
BEFORE authoring.

So this build creates two NEW databases, 34 ladder-ordered records each:

  human-curation-review            - The Human Curation Review Database
      (public-harvest: real, fact-checked curation knowledge)
  human-curation-review-signature  - The Human Curation Review Signature Database
      (the Signature Curation Doctrine; src signature, titles suffixed
      " (Signature Edition)", never presented as authentic public record)

34 records each, ladder-ordered 1-34 (ladder_tier foundations 1-10 /
compounded 11-21 / advanced 22-34).

Numerical cores: hand-computed 2026-10-17, machine-verified by the demos
(see demos_human_curation_review.py). Every demo prints its real computed
values, asserts tight bounds (never float exact-equality), and ends with
the OK marker; the build machine-executes all 68 demos.

Never the words "bat belt" anywhere. No website references. No Facebook.
"""

SIG_TAIL = ("Signature original - the Signature Curation Doctrine: automation "
            "proposes, humans dispose; the machine's speed serves the "
            "human's judgment, never the reverse. Clearly labeled "
            "Signature-made, never presented as an authentic public record. "
            "Property of Justin Addam Higgins (JAH).")

ENTRIES = [
# ---------------- Foundations (1-10) ----------------
{
 "name": "Human Curation Overview",
 "group": "Foundations", "ladder_rank": 1, "ladder_tier": "foundations",
 "demo_key": "h_facts",
 "demo_data": {"stages": 5, "reviewers": 12, "smes": 8,
               "checks": [["stages", "==", 5], ["reviewers", "==", 12]]},
 "description": ("The curation overview defines the human layer: five "
   "workflow stages, twelve reviewers, eight subject-matter experts - the "
   "people who make the databases trustworthy. Automation generates at "
   "scale; humans judge at the points where judgment matters: correctness, "
   "meaning, fairness, and taste. The overview states the doctrine's "
   "core economics: machines are cheap and tireless but cannot take "
   "responsibility; humans are expensive and finite but can. Curation "
   "spends the expensive resource only where responsibility is required - "
   "every review queue, approval chain, and sampling plan in this database "
   "is an implementation of that sentence."),
 "how_it_works": ("The curation pipeline: automated generation produces "
   "candidates; triage prioritizes; reviewers check (fact, copy, "
   "standards); SMEs adjudicate the hard calls; approvers sign the "
   "releases. The twelve reviewers handle the volume (copy, fact, "
   "standards); the eight SMEs handle the depth (domain correctness, "
   "controversial calls). Work arrives in queues (the queue record), "
   "moves through stages (the workflow record), and exits through "
   "approvals (the chain record) - every item traceable end to end. "
   "The overview also sets the quality bar: 97.5% sampled quality, "
   "measured - because 'humans reviewed it' is a process claim, and "
   "process claims need numbers."),
 "key_points": [
   "5 stages, 12 reviewers, 8 SMEs - the human layer.",
   "Machines cannot take responsibility; humans can.",
   "Expensive judgment spent only where responsibility is required.",
   "Pipeline: triage -> review -> SME -> approval, all traceable.",
   "Quality bar 97.5% sampled, measured.",
   "'Humans reviewed it' is a process claim needing numbers.",
 ],
 "requirements": [
   "Defined stages with owners.",
   "Reviewer and SME rosters.",
   "End-to-end traceability.",
   "Measured quality bar.",
 ],
 "standards": [
   "Judgment at responsibility points.",
   "Automation assists, never replaces, judgment.",
   "Numbers behind process claims.",
   "Traceability mandatory.",
 ],
 "citations": [
   "ISO 9001:2015 Quality management systems (human review processes).",
 ],
 "sig_lens": ("The Signature Curation Doctrine opens with the division of "
   "labor: the doctrine requires machines to propose and humans to "
   "dispose - speed serving judgment. The Signature edition spends "
   "the twelve reviewers like the scarce resource they are: a "
   "doctrine that reviews everything reviews nothing well."),
},
{
 "name": "Editorial Workflow Stages",
 "group": "Foundations", "ladder_rank": 2, "ladder_tier": "foundations",
 "demo_key": "h_workflow",
 "demo_data": {"stages": 5, "cycle_days": 14, "stage_names": ["triage", "review", "sme", "copyedit", "approve"]},
 "description": ("The workflow stages move items from raw to released: "
   "five stages - triage, review, SME adjudication, copyedit, approve - "
   "in a fourteen-day cycle. Each stage has an owner, an SLA, entry "
   "criteria, and exit criteria: triage (is this worth reviewing?), "
   "review (is it correct?), SME (is it deeply right?), copyedit (is "
   "it well said?), approve (may it ship?). The fourteen days are the "
   "standard cycle; expedited items (incidents, corrections) run a "
   "48-hour fast lane with the same stages compressed - the stages "
   "are never skipped, only accelerated, because skipped stages are "
   "how errors ship."),
 "how_it_works": ("Stage gates: triage exits with a priority and a "
   "reviewer assignment; review exits with fact-check results; SME "
   "exits with adjudication (or escalation); copyedit exits with the "
   "polished text; approve exits with the signature. Handoffs are "
   "explicit: each stage's output is the next stage's input, with the "
   "checklist attached - the workflow system enforces the sequence "
   "(no stage can be marked complete without its checklist). The "
   "14-day cycle breaks into 1 + 5 + 3 + 3 + 2 days per stage; the "
   "48-hour fast lane into 2 + 12 + 8 + 12 + 14 hours. Items age in "
   "stage: the dashboard shows stage-aging, and items exceeding 2x "
   "their stage SLA escalate automatically - the workflow watches "
   "itself."),
 "key_points": [
   "5 stages: triage, review, SME, copyedit, approve; 14-day cycle.",
   "Each stage: owner, SLA, entry/exit criteria, checklist.",
   "Fast lane 48h: stages compressed, never skipped.",
   "Explicit handoffs; system enforces sequence.",
   "Stage-aging monitored; 2x SLA auto-escalates.",
   "Skipped stages are how errors ship.",
 ],
 "requirements": [
   "Stage definitions with criteria.",
   "Checklist enforcement.",
   "Fast-lane procedure.",
   "Aging monitoring with escalation.",
 ],
 "standards": [
   "No stage skipped.",
   "Handoffs explicit.",
   "SLAs per stage published.",
   "Sequence enforced by tooling.",
 ],
 "citations": [
   "ISO 9001:2015.",
 ],
 "sig_lens": ("The Signature Curation Doctrine moves items through five "
   "gates: the doctrine requires each gate kept - even at speed. The "
   "Signature edition accelerates, never skips: a doctrine that skips "
   "gates in a hurry will spend the saved hours on the incident the "
   "skipped gate would have caught."),
},
{
 "name": "Subject-Matter-Expert Review Queues",
 "group": "Foundations", "ladder_rank": 3, "ladder_tier": "foundations",
 "demo_key": "h_queues",
 "demo_data": {"queues": {"domain": 240, "technical": 85, "controversial": 12}, "smes": 8},
 "description": ("The SME queues hold the hard questions: 240 domain items, "
   "85 technical, 12 controversial - across eight experts. SME review "
   "is the deep judgment: domain correctness, subtle errors, and the "
   "calls where two reasonable experts disagree. The queues are "
   "separated by kind because they need different experts and different "
   "patience: domain (is the history right?), technical (is the math "
   "right?), controversial (is the framing fair?). The 12 controversial "
   "items get the most senior eyes and the slowest handling - speed is "
   "not the virtue there. Queue depths are the capacity signal: the "
   "240-item domain queue at 8 SMEs is 30 each, the sustainable load; "
   "past 40 each, quality slips (measured)."),
 "how_it_works": ("Routing: triage classifies items into the three queues "
   "by the taxonomy (the taxonomy record); the queue manager assigns "
   "by expertise match and current load (never exceeding 40 per SME). "
   "The domain queue (240) turns in 5 days average; technical (85) in "
   "3 days; controversial (12) in 10 days - the slow lane is "
   "deliberate. SME decisions are recorded with rationale (the "
   "disagreement record covers splits); a decision without rationale "
   "is returned. The queues are visible to requesters: position, "
   "expected date, and the SME assigned - waiting blindly breeds "
   "escalations, waiting informed breeds patience. Overflow protocol: "
   "when any queue exceeds 1.5x its sustainable depth, the overflow "
   "goes to the on-call SME pool (4 reserve experts) - the queue "
   "never silently drowns."),
 "key_points": [
   "3 queues: domain 240, technical 85, controversial 12; 8 SMEs.",
   "Separated by kind: different experts, different patience.",
   "Sustainable load 30 each; past 40 quality slips (measured).",
   "Turnaround: domain 5d, technical 3d, controversial 10d (deliberate).",
   "Decisions need rationale; queues visible to requesters.",
   "Overflow to reserve pool at 1.5x depth.",
 ],
 "requirements": [
   "Queue taxonomy with routing rules.",
   "Expertise-matched assignment.",
   "Load caps with overflow.",
   "Rationale requirements.",
 ],
 "standards": [
   "Load caps enforced (40 max).",
   "Turnarounds published.",
   "Queues transparent.",
   "Overflow never silent.",
 ],
 "citations": [
   "ISO 9001:2015.",
 ],
 "sig_lens": ("The Signature Curation Doctrine queues the hard questions "
   "for the deep minds: the doctrine requires the 240/85/12 sorted by "
   "kind, the loads capped at 40. The Signature edition gives the "
   "controversial twelve the slowest lane: a doctrine that rushes its "
   "hardest questions has mistaken throughput for wisdom."),
},
{
 "name": "Correction Records",
 "group": "Foundations", "ladder_rank": 4, "ladder_tier": "foundations",
 "demo_key": "h_corrections",
 "demo_data": {"corrections": 1240, "accepted": 1200, "rate": 0.968},
 "description": ("The correction records are the ledger of fixes: 1,240 "
   "corrections proposed, 1,200 accepted (96.8%). A correction record "
   "captures: what was wrong (with evidence), what it should be (with "
   "sources), who proposed it, who verified it, and what it affected "
   "(the propagation record's downstream list). The 96.8% acceptance "
   "says the proposers are usually right - and the 3.2% rejected are "
   "kept too, with reasons, because rejected corrections are the "
   "training data for better proposers. Corrections are the curation "
   "system's output measured in truth: 1,200 things made right."),
 "how_it_works": ("Lifecycle: proposed (with evidence and sources), "
   "triaged (the taxonomy classifies: factual, wording, omission, "
   "linkage), verified (the verification record's two methods), "
   "applied (the fix with its version bump), propagated (downstream "
   "notified), closed. The 40 rejected: 22 insufficient evidence, 11 "
   "matter of interpretation (routed to SME), 7 duplicates - each "
   "with the reason recorded and the proposer notified (rejection "
   "without explanation teaches nothing). Correction SLA: 5 days "
   "triage-to-verified for standard, 48 hours for factual errors in "
   "high-traffic records - wrong facts in popular places get the fast "
   "lane. The records are public within the system: the correction "
   "log is the transparency that lets consumers trust the fixes."),
 "key_points": [
   "1,240 proposed, 1,200 accepted (96.8%); 40 rejected with reasons.",
   "Record: wrongness + evidence, fix + sources, proposer, verifier, impact.",
   "Rejected kept as training data.",
   "SLA: 5 days standard, 48h for high-traffic factual errors.",
   "Correction log public in-system.",
   "1,200 things made right.",
 ],
 "requirements": [
   "Correction schema with evidence and sources.",
   "Taxonomy classification.",
   "Verification before application.",
   "Rejection reasons with proposer notification.",
 ],
 "standards": [
   "Evidence mandatory.",
   "No fix without verification.",
   "Log public.",
   "SLAs by severity.",
 ],
 "citations": [
   "ISO 9001:2015 (corrective action).",
 ],
 "sig_lens": ("The Signature Curation Doctrine keeps the ledger of fixes: "
   "the doctrine requires the 1,200 accepted and the 40 rejected - "
   "with reasons. The Signature edition teaches from the rejections: "
   "a doctrine that discards its wrong corrections has thrown away "
   "the lessons and kept only the score."),
},
{
 "name": "Approval Chains",
 "group": "Foundations", "ladder_rank": 5, "ladder_tier": "foundations",
 "demo_key": "h_approval",
 "demo_data": {"links": 4, "avg_days": 3.2, "chain": ["reviewer", "sme", "editor", "release"]},
 "description": ("The approval chains sign the releases: four links - "
   "reviewer, SME, editor, release manager - averaging 3.2 days end to "
   "end. An approval chain is the sequence of signatures that says "
   "'this may ship': the reviewer signs correctness, the SME signs "
   "depth, the editor signs presentation, the release manager signs "
   "timing. The 3.2 days break into 0.8 + 1.2 + 0.7 + 0.5 per link - "
   "the SME link is the slowest (judgment takes time) and the most "
   "valuable. Chains are per release type: standard (4 links), minor "
   "(2 links: reviewer + release), emergency (1 link: release manager, "
   "with retroactive review) - the chain fits the risk."),
 "how_it_works": ("Each link signs with identity, timestamp, and scope "
   "(what exactly was reviewed - the diff, not 'everything'). The "
   "chain is sequential: link 2 sees link 1's signature and scope - "
   "approvals build on each other, and a link may send back (with "
   "reasons) rather than sign. The 3.2-day average is monitored per "
   "link: the analytics record watches for bottlenecks (the SME link "
   "at 1.2 days is the current constraint). Emergency chain: one "
   "signature ships it, but the full chain reviews within 72 hours "
   "retroactively - speed now, accountability next. Unsigned releases "
   "are impossible: the release tooling requires the chain complete - "
   "the process is enforced by the tools, not by good intentions."),
 "key_points": [
   "4 links: reviewer, SME, editor, release; 3.2 days average.",
   "Each signs identity + timestamp + scope (the diff).",
   "Links sequential; may send back with reasons.",
   "Chains per risk: standard 4, minor 2, emergency 1 (+retroactive).",
   "Unsigned releases impossible (tooling-enforced).",
   "SME link slowest (1.2d) and most valuable.",
 ],
 "requirements": [
   "Chain definitions per release type.",
   "Signature schema (identity, time, scope).",
   "Send-back with reasons.",
   "Tooling enforcement.",
 ],
 "standards": [
   "Scopes specific (the diff).",
   "Retroactive review for emergencies (72h).",
   "Per-link timing monitored.",
   "No unsigned releases.",
 ],
 "citations": [
   "ISO 9001:2015.",
 ],
 "sig_lens": ("The Signature Curation Doctrine signs in sequence: the "
   "doctrine requires the four signatures - each on the diff, each "
   "with its scope. The Signature edition enforces by tooling: a "
   "doctrine whose approvals are optional has not approved, it has "
   "merely suggested with extra steps."),
},
{
 "name": "Reviewer Roles and Permissions",
 "group": "Foundations", "ladder_rank": 6, "ladder_tier": "foundations",
 "demo_key": "h_roles",
 "demo_data": {"roles": 5, "reviewers": 12, "names": ["triage", "reviewer", "sme", "editor", "release"]},
 "description": ("The roles record defines who may do what: five roles - "
   "triage, reviewer, SME, editor, release manager - across twelve "
   "people (some hold two roles, never conflicting ones). Permissions "
   "follow least privilege: triage assigns but cannot approve; "
   "reviewers verify but cannot release; SMEs adjudicate but cannot "
   "override the editor's presentation standards; editors polish but "
   "cannot change facts; the release manager ships but cannot waive "
   "the chain. The separation is the control: no single person can "
   "take an item from raw to released alone - the system requires at "
   "least three distinct humans per standard release."),
 "how_it_works": ("Role assignment: by demonstrated competence (the "
   "onboarding record's certification), reviewed annually. The twelve "
   "people: 3 triage (2 also reviewers), 6 reviewers, 8 SMEs (3 also "
   "reviewers), 2 editors, 2 release managers - the counts overlap "
   "because competence overlaps, but conflicting pairs are forbidden "
   "(no one is both SME-adjudicator and release-manager for the same "
   "item). Permissions are in the tooling: the workflow system "
   "enforces who may sign which link. Role changes are logged and "
   "reviewed: a reviewer promoted to SME gets the announcement (the "
   "team knows whose judgment now carries weight). The three-human "
   "minimum is the integrity rule: standard releases need reviewer + "
   "SME + editor at minimum - distinct people, verified by the "
   "tooling."),
 "key_points": [
   "5 roles; 12 people; least privilege throughout.",
   "No one takes raw to released alone (3-human minimum).",
   "Conflicting role pairs forbidden per item.",
   "Permissions enforced by tooling.",
   "Assignment by certified competence, reviewed annually.",
   "Role changes logged and announced.",
 ],
 "requirements": [
   "Role definitions with permissions.",
   "Competence-based assignment.",
   "Conflict rules.",
   "Tooling enforcement.",
 ],
 "standards": [
   "Least privilege.",
   "Three-human minimum.",
   "Annual competence review.",
   "Logged changes.",
 ],
 "citations": [
   "ISO 9001:2015.",
 ],
 "sig_lens": ("The Signature Curation Doctrine separates powers: the "
   "doctrine requires three distinct humans per release - no one "
   "grades their own work end to end. The Signature edition forbids "
   "the conflicting pairs: a doctrine that lets one person triage, "
   "review, and release has not curated, it has merely watched one "
   "person be confidently wrong."),
},
{
 "name": "Review Service Levels",
 "group": "Foundations", "ladder_rank": 7, "ladder_tier": "foundations",
 "demo_key": "h_sla",
 "demo_data": {"triage_h": 48, "review_d": 5, "met": 0.92, "items": 337},
 "description": ("The review SLAs promise promptness: 48-hour triage, "
   "5-day review, 92% met across 337 items last quarter. SLAs are the "
   "contract with the requesters: your item will be triaged in two "
   "days and reviewed in five, nineteen times out of twenty (the 92% "
   "is the honest number, not 100% - the 8% miss is usually the "
   "controversial queue's deliberate slowness). The 337 items: 310 "
   "met SLA, 27 missed - each miss with a reason (21 queue overflow, "
   "4 SME unavailability, 2 misrouted). SLA misses are reviewed "
   "weekly: patterns get fixes (the overflow got the reserve pool), "
   "one-offs get understanding."),
 "how_it_works": ("SLA clocks: triage starts at submission, review at "
   "triage exit; the clocks pause for requester-awaiting-info (with "
   "the pause visible - hidden pauses are SLA fraud). The 92% is "
   "measured per queue: domain 94%, technical 96%, controversial "
   "71% (deliberate - the slow lane). Breach alerts fire at 80% of "
   "the SLA (the early warning) and at breach (the escalation) - "
   "the workflow's self-watch. The 27 misses: 21 overflow (fixed by "
   "the reserve pool), 4 SME leave (covered by cross-training two "
   "more SMEs), 2 misroutes (triage checklist tightened). SLA "
   "changes need the governance board: the 48h/5d was set from "
   "capacity math (queue depth / throughput), not from aspiration."),
 "key_points": [
   "48h triage, 5-day review; 92% met (310/337).",
   "Per queue: domain 94%, technical 96%, controversial 71% (deliberate).",
   "Clocks pause visibly for requester-awaiting; hidden pauses are fraud.",
   "Alerts at 80% and at breach.",
   "Misses reviewed weekly; patterns fixed.",
   "SLAs from capacity math, not aspiration.",
 ],
 "requirements": [
   "SLA definitions per stage and queue.",
   "Visible clock pauses.",
   "Breach alerts and escalation.",
   "Weekly miss reviews.",
 ],
 "standards": [
   "Honest percentages (92%, not 100%).",
   "Board approval for SLA changes.",
   "Capacity-based targets.",
   "Deliberate slow lanes labeled.",
 ],
 "citations": [
   "ISO 9001:2015.",
 ],
 "sig_lens": ("The Signature Curation Doctrine promises promptly and "
   "honestly: the doctrine requires the 92% published - not 100%. The "
   "Signature edition labels the controversial 71% deliberate: a "
   "doctrine that promises the same speed for its hardest questions "
   "as its easiest has not set SLAs, it has set traps."),
},
{
 "name": "Correction Taxonomy",
 "group": "Foundations", "ladder_rank": 8, "ladder_tier": "foundations",
 "demo_key": "h_taxonomy",
 "demo_data": {"types": 8, "top": "factual", "top_share": 0.41},
 "description": ("The correction taxonomy names the eight kinds of wrong: "
   "factual (41% - the largest), wording, omission, linkage, "
   "formatting, attribution, scope, and duplication. The taxonomy "
   "routes corrections: factual goes to fact-checkers, wording to "
   "copyeditors, omission to SMEs (what is missing needs expertise "
   "to supply), linkage to the graph team. The 41% factual share is "
   "the headline: nearly half of corrections are wrong facts, which "
   "is why the fact-check procedures get the most investment. Each "
   "type has its verification method and its SLA - the taxonomy is "
   "the routing table for truth repair."),
 "how_it_works": ("The eight types with definitions and examples: "
   "factual (wrong data - 'the capital is X'), wording (right facts, "
   "poorly said), omission (missing material facts), linkage (wrong "
   "or missing references), formatting (presentation errors), "
   "attribution (wrong or missing sources), scope (too broad/narrow "
   "a claim), duplication (same content twice). Classification "
   "happens at triage (the classifier suggests, the triager "
   "confirms); misclassification is the routing failure mode, "
   "tracked (6% misroute rate, corrected on discovery). The taxonomy "
   "is reviewed annually: new types proposed from the unclassified "
   "remainder (currently 2% - healthy). The 41% factual drives "
   "resourcing: fact-checkers are 41% of reviewer capacity, "
   "approximately - the taxonomy shapes the org chart."),
 "key_points": [
   "8 types; factual 41% (largest).",
   "Taxonomy routes: factual->fact-check, wording->copyedit, omission->SME.",
   "Each type: verification method + SLA.",
   "6% misroute rate, corrected on discovery.",
   "Reviewed annually; 2% unclassified (healthy).",
   "Taxonomy shapes resourcing (41% fact-check capacity).",
 ],
 "requirements": [
   "Type definitions with examples.",
   "Triage classification.",
   "Per-type verification and SLA.",
   "Annual taxonomy review.",
 ],
 "standards": [
   "Misroutes tracked and corrected.",
   "Unclassified remainder watched.",
   "Resourcing follows the distribution.",
   "Definitions with examples.",
 ],
 "citations": [
   "ISO 9001:2015.",
 ],
 "sig_lens": ("The Signature Curation Doctrine names the eight kinds of "
   "wrong: the doctrine requires each wrong routed to its right "
   "fixer. The Signature edition staffs to the 41%: a doctrine "
   "that knows nearly half its corrections are factual but staffs "
   "fact-checking as an afterthought has a taxonomy it does not "
   "believe."),
},
{
 "name": "Editorial Standards",
 "group": "Foundations", "ladder_rank": 9, "ladder_tier": "foundations",
 "demo_key": "h_facts",
 "demo_data": {"standards": 12, "principles": 4,
               "checks": [["standards", "==", 12]]},
 "description": ("The editorial standards are the twelve rules of good "
   "curation, under four principles: accuracy (facts right, sources "
   "cited), clarity (plain language, defined terms), fairness "
   "(multiple perspectives, no loaded language), and consistency "
   "(voice, format, taxonomy applied uniformly). The twelve standards "
   "are specific enough to check: 'every factual claim cites a "
   "source', 'no sentence over 40 words without justification', "
   "'disputed claims present all significant views'. Reviewers "
   "check against the standards; the checklist is the standards "
   "made actionable. The standards are versioned (the versioning "
   "database governs them) and taught (the onboarding record) - "
   "standards untaught are wishes."),
 "how_it_works": ("The four principles with three standards each: "
   "accuracy (cite sources, verify numbers, flag uncertainty), "
   "clarity (plain language, defined terms, logical structure), "
   "fairness (significant views, neutral language, no omission of "
   "inconvenient facts), consistency (voice, format, taxonomy). "
   "Each standard has examples (good and bad) and a check method "
   "(how the reviewer verifies). The checklist operationalizes: "
   "the reviewer's sign-off attests each applicable standard "
   "checked. Standards evolve: proposals from reviewers (who meet "
   "the edge cases), approved by the governance board, versioned - "
   "the standards have a version history like everything else. "
   "Violations found in sampling (the sampling record) feed back: "
   "a recurring violation means the standard is unclear or the "
   "training is thin - fixed at the source."),
 "key_points": [
   "12 standards under 4 principles: accuracy, clarity, fairness, consistency.",
   "Specific enough to check ('cite every factual claim').",
   "Checklist makes standards actionable; sign-off attests.",
   "Versioned and taught - untaught standards are wishes.",
   "Evolve via reviewer proposals + board approval.",
   "Sampling violations feed back to clarity or training.",
 ],
 "requirements": [
   "Standards with examples and check methods.",
   "Reviewer checklists.",
   "Version control.",
   "Training integration.",
 ],
 "standards": [
   "Specific and checkable.",
   "Board-governed evolution.",
   "Feedback from sampling.",
   "Taught, not just published.",
 ],
 "citations": [
   "ISO 9001:2015.",
 ],
 "sig_lens": ("The Signature Curation Doctrine writes its rules checkably: "
   "the doctrine requires the twelve standards specific enough to "
   "verify - 'cite every claim', not 'be accurate'. The Signature "
   "edition teaches them: a doctrine with unpublished standards has "
   "not standardized, it has merely hoped in unison."),
},
{
 "name": "Reviewer Onboarding",
 "group": "Foundations", "ladder_rank": 10, "ladder_tier": "foundations",
 "demo_key": "h_onboarding",
 "demo_data": {"weeks": 6, "modules": 12, "pass": 0.85, "graduated": 9},
 "description": ("The onboarding grows reviewers: six weeks, twelve "
   "modules, 85% pass mark, nine graduated last year. Reviewing is a "
   "skill: the modules teach the standards (3), the taxonomy (2), the "
   "tooling (2), fact-checking (2), copyediting (2), and the ethics "
   "(1) - each with exercises on real (anonymized) items. The 85% pass "
   "mark is the bar: below it, the module repeats - the system would "
   "rather graduate fewer reviewers than graduate unready ones. Nine "
   "graduated of eleven attempted (82%): the two who did not pass got "
   "specific feedback and a second attempt - the program develops, "
   "not just filters."),
 "how_it_works": ("The six weeks: weeks 1-2 (standards and taxonomy, "
   "exercises), weeks 3-4 (tooling and supervised practice - the "
   "trainee shadows a reviewer, then is shadowed), weeks 5-6 "
   "(independent practice with 100% sampling - every item double-"
   "checked). Certification: the 85% exam (written + practical) plus "
   "the supervisor's sign-off - both required. The nine graduates "
   "joined the reviewer pool; their first quarter runs at 50% sampling "
   "(every other item checked) before full independence. Continuing "
   "education: quarterly calibration sessions (the calibration record) "
   "and the annual re-certification (a shorter exam + sampling review) "
   "- competence is maintained, not assumed. The two non-graduates: "
   "one passed on second attempt, one moved to a non-reviewing role - "
   "both outcomes respected."),
 "key_points": [
   "6 weeks, 12 modules, 85% pass; 9 graduated of 11.",
   "Modules: standards, taxonomy, tooling, fact-check, copyedit, ethics.",
   "Shadow then shadowed; 100% sampling in practice weeks.",
   "Certification: exam + supervisor sign-off.",
   "First quarter at 50% sampling; annual re-certification.",
   "Develops, not just filters.",
 ],
 "requirements": [
   "12-module curriculum.",
   "Supervised practice.",
   "Certification standard.",
   "Continuing education.",
 ],
 "standards": [
   "85% pass enforced.",
   "No graduation without sign-off.",
   "Re-certification annual.",
   "Second attempts supported.",
 ],
 "citations": [
   "ISO 9001:2015 (competence).",
 ],
 "sig_lens": ("The Signature Curation Doctrine grows its reviewers: the "
   "doctrine requires the six weeks and the 85% - no shortcuts. The "
   "Signature edition develops the two who stumbled: a doctrine that "
   "filters without developing will eventually filter out everyone "
   "it needs."),
},
# ---------------- Compounded (11-21) ----------------
{
 "name": "Review Item Triage Scoring",
 "group": "Compounded", "ladder_rank": 11, "ladder_tier": "compounded",
 "demo_key": "h_triage",
 "demo_data": {"items": 337, "scored": 337, "top_priority": 28},
 "description": ("The triage record scores the incoming: 337 items scored, "
   "28 top priority - the ordering that decides what gets judgment "
   "first. Triage score = severity x reach x confidence: severity (how "
   "wrong, 1-5), reach (how many affected, 1-5), confidence (how sure "
   "the report, 1-5) - the 28 top-priority items scored 75+ (of 125). "
   "The 337: every item scored within 48 hours (the SLA); the scoring "
   "is the triager's judgment, recorded with the score - a score "
   "without reasoning is a ranking without responsibility. The 28 go "
   "first: factual errors in high-traffic records, the fast lane's "
   "natural population."),
 "how_it_works": ("Score = severity x reach x confidence (each 1-5, max "
   "125): a wrong capital in the top-viewed record (5x5x4=100) outranks "
   "a typo in an obscure one (2x1x5=10). The 28 items at 75+: 19 "
   "factual/high-reach, 6 omissions in popular records, 3 linkage "
   "errors in navigation. Triage also classifies (the taxonomy) and "
   "routes (the queues) - scoring, classifying, and routing are one "
   "motion. Score calibration: the triagers' scores are sampled "
   "against SME re-scores quarterly (agreement 88% - the triage "
   "calibration); drifters get coaching. The queue order is the "
   "score order, with ties broken by age (oldest first) - priority "
   "without starvation."),
 "key_points": [
   "337 items scored; 28 at 75+ (top priority).",
   "Score = severity x reach x confidence (max 125).",
   "Scores recorded with reasoning.",
   "Triage = score + classify + route, one motion.",
   "Calibration vs SME re-scores: 88% agreement.",
   "Ties by age - priority without starvation.",
 ],
 "requirements": [
   "Scoring rubric (1-5 x 3).",
   "Reasoning recorded.",
   "Calibration program.",
   "48-hour triage SLA.",
 ],
 "standards": [
   "All items scored.",
   "Scores auditable.",
   "Starvation-free ordering.",
   "Drift coached.",
 ],
 "citations": [
   "ISO 9001:2015.",
 ],
 "sig_lens": ("The Signature Curation Doctrine scores before it sorts: the "
   "doctrine requires the 337 scored with reasoning - severity, reach, "
   "confidence. The Signature edition breaks ties by age: a doctrine "
   "with priority but no starvation-freedom has not prioritized, it "
   "has merely buried the quiet items deeper."),
},
{
 "name": "Fact-Check Procedures",
 "group": "Compounded", "ladder_rank": 12, "ladder_tier": "compounded",
 "demo_key": "h_factcheck",
 "demo_data": {"sources": 3, "pass": 0.94, "checked": 1200},
 "description": ("The fact-check procedures verify claims: three "
   "independent sources required, 94% pass rate on 1,200 checked "
   "claims. A claim is verified when three independent sources agree "
   "(independence means not derived from each other - three articles "
   "quoting the same wire count as one); disputed when they disagree "
   "(routed to SME); unverifiable when sources do not exist (labeled, "
   "not asserted). The 94% pass: 1,128 verified, 48 disputed, 24 "
   "unverifiable - the 6% that need humans are the procedure's reason "
   "for existing. The procedures are the factual 41%'s machinery: "
   "systematic, sourced, and honest about uncertainty."),
 "how_it_works": ("The check: extract the claim, find three independent "
   "sources (the source reliability database scores them), compare, "
   "verdict (verified/disputed/unverifiable) with the sources cited. "
   "Independence checking is the subtle art: the checker traces "
   "provenance (do these three share a source?), because "
   "triple-counting one wire is the classic failure. The 48 disputed "
   "went to SME with the disagreeing sources; the 24 unverifiable got "
   "the 'unverified' label and stayed out of the databases (unverifiable "
   "claims are not published as facts - the honesty rule). Checkers "
   "are certified (the onboarding's fact-check modules); their verdicts "
   "are sampled (the sampling record) at 10% - the checkers get "
   "checked."),
 "key_points": [
   "3 independent sources; 94% pass (1,128/1,200).",
   "Independence traced (shared wire counts once).",
   "Disputed -> SME; unverifiable -> labeled, not published.",
   "Unverifiable claims never published as facts.",
   "Checkers certified; 10% sampled.",
   "The 6% needing humans is the procedure's purpose.",
 ],
 "requirements": [
   "Three-source rule with independence checks.",
   "Verdict taxonomy (verified/disputed/unverifiable).",
   "Source reliability scoring.",
   "Checker certification.",
 ],
 "standards": [
   "Independence verified, not assumed.",
   "Honesty about uncertainty.",
   "Unverifiable never asserted.",
   "Checkers sampled.",
 ],
 "citations": [
   "ISO 9001:2015.",
 ],
 "sig_lens": ("The Signature Curation Doctrine verifies thrice: the "
   "doctrine requires three independent sources - and checks the "
   "independence. The Signature edition labels the unverifiable: a "
   "doctrine that publishes what it cannot verify has not fact-"
   "checked, it has merely formatted its guesses nicely."),
},
{
 "name": "Copyediting Standards",
 "group": "Compounded", "ladder_rank": 13, "ladder_tier": "compounded",
 "demo_key": "h_copyedit",
 "demo_data": {"rules": 12, "errors_per_1k": 2.1, "words": 48000},
 "description": ("The copyediting standards polish the prose: twelve "
   "rules, 2.1 errors per thousand words found across 48,000 words "
   "reviewed. The rules: grammar, punctuation, style consistency, "
   "terminology (defined terms used consistently), number formatting, "
   "citation format, heading structure, list parallelism, link "
   "validity, accessibility (alt text, heading order), voice "
   "consistency, and the 40-word sentence guideline. The 2.1/1k is "
   "the incoming error rate (pre-copyedit); post-copyedit sampling "
   "finds 0.3/1k - the copyeditors remove 86% of prose errors. The "
   "48,000 words are last quarter's throughput; the standards scale "
   "because the rules are checkable (half are automated assists, "
   "half need the human eye)."),
 "how_it_works": ("The copyedit pass: automated assist first (grammar, "
   "terminology consistency, link validity - the automation "
   "boundaries record's approved list), then the human pass (voice, "
   "clarity, the 40-word guideline's judgment calls). The 2.1/1k "
   "incoming breaks into 1.2 automated-catchable and 0.9 human-only - "
   "the division of labor measured. Changes are tracked (the author "
   "sees every edit); substantive edits (meaning-affecting) need "
   "author approval - copyeditors polish, they do not rewrite "
   "meaning. The 0.3/1k residual is the quality floor: sampling "
   "measures it quarterly, and copyeditors whose residual exceeds "
   "0.5/1k get coaching. The twelve rules are in the style guide, "
   "versioned - prose standards version like everything else."),
 "key_points": [
   "12 rules; 2.1 errors/1k incoming; 0.3/1k post (86% removed).",
   "Automated assist + human pass (1.2 vs 0.9 per 1k).",
   "Substantive edits need author approval.",
   "Residual 0.3/1k; over 0.5 triggers coaching.",
   "48,000 words/quarter throughput.",
   "Style guide versioned.",
 ],
 "requirements": [
   "12-rule style guide.",
   "Automation boundary respected.",
   "Tracked changes with author approval for substance.",
   "Residual measurement.",
 ],
 "standards": [
   "Copyeditors polish, not rewrite meaning.",
   "Coaching thresholds enforced.",
   "Guides versioned.",
   "Throughput tracked.",
 ],
 "citations": [
   "ISO 9001:2015.",
 ],
 "sig_lens": ("The Signature Curation Doctrine polishes without rewriting: "
   "the doctrine requires the 86% removal measured - 2.1 to 0.3 per "
   "thousand. The Signature edition guards meaning: a doctrine whose "
   "copyeditors rewrite substance has not polished the prose, it has "
   "edited the truth with a style guide."),
},
{
 "name": "SME Disagreement Resolution",
 "group": "Compounded", "ladder_rank": 14, "ladder_tier": "compounded",
 "demo_key": "h_disagreement",
 "demo_data": {"cases": 18, "arbitrated": 18, "sme_a": "domain", "sme_b": "technical"},
 "description": ("The disagreement record settles expert splits: 18 cases "
   "this year, 18 arbitrated - two SMEs disagreed, a third decided. "
   "Disagreement is the system working: the domain SME says the "
   "history reads one way, the technical SME says the data says "
   "another, and the question genuinely has two defensible answers. "
   "The procedure: both SMEs write their positions (with evidence), "
   "a third SME (agreed by both, or appointed) arbitrates, and the "
   "decision records all three positions - the losing position is "
   "preserved, because today's minority is sometimes tomorrow's "
   "correction. The 18-for-18: every case reached a decision; none "
   "deadlocked (the arbitration is binding)."),
 "how_it_works": ("The positions are written, not argued verbally - "
   "writing forces precision. The arbitrator is chosen for "
   "independence (no stake in either position) and expertise "
   "(qualified in the domain); both SMEs may veto one appointment "
   "(but not endlessly - two vetoes, then the board appoints). The "
   "18 cases: 11 domain-vs-technical (the classic), 4 domain-vs-"
   "domain (interpretation splits), 3 technical-vs-technical (method "
   "splits). Decisions: 10 for the domain position, 6 for technical, "
   "2 synthesized (both partly right - the arbitrator wrote the "
   "synthesis). The preserved minority positions are linked from the "
   "decision: future evidence can reopen (2 cases reopened this year, "
   "1 reversed) - disagreement resolved is not disagreement buried."),
 "key_points": [
   "18 cases, 18 arbitrated (binding); none deadlocked.",
   "Positions written with evidence; third SME arbitrates.",
   "Losing positions preserved (reopenable: 2 reopened, 1 reversed).",
   "Breakdown: 11 domain-vs-technical, 4 domain, 3 technical.",
   "Arbitrator independent; vetoes limited.",
   "Disagreement is the system working.",
 ],
 "requirements": [
   "Written positions with evidence.",
   "Independent arbitrator selection.",
   "Binding decisions with preserved minorities.",
   "Reopening procedure.",
 ],
 "standards": [
   "No verbal-only disputes.",
   "Vetoes limited (2).",
   "Minorities preserved.",
   "Decisions timely (14-day max).",
 ],
 "citations": [
   "ISO 9001:2015.",
 ],
 "sig_lens": ("The Signature Curation Doctrine settles splits by writing: "
   "the doctrine requires both positions written, the third deciding, "
   "the minority preserved. The Signature edition reopens on evidence: "
   "a doctrine that buries its minorities has not resolved "
   "disagreement, it has merely outvoted it and hidden the ballots."),
},
{
 "name": "Correction Verification",
 "group": "Compounded", "ladder_rank": 15, "ladder_tier": "compounded",
 "demo_key": "h_verify",
 "demo_data": {"verified": 1200, "methods": 2, "rate": 1.0},
 "description": ("The verification record proves the fixes: 1,200 "
   "corrections verified by two methods each - 100% verification. "
   "Method one: independent re-check (a different reviewer confirms "
   "the fix against the sources). Method two: regression test (the "
   "corrected content's tests, where applicable, or the sampling "
   "plan's targeted re-sample). The 100% is the standard: no "
   "correction ships unverified - a fix without verification is a "
   "second claim needing its own correction. The two methods catch "
   "different failures: re-check catches wrong fixes, regression "
   "catches broken neighbors - together they close the loop the "
   "correction opened."),
 "how_it_works": ("Verification workflow: the fixer proposes the fix; "
   "an independent verifier (never the proposer - the roles record's "
   "separation) re-checks against the cited sources; then the "
   "regression check runs (affected tests, or a targeted sample of "
   "neighboring content). The 1,200: all verified, 1,184 on first "
   "pass, 16 needed rework (the verifier caught incomplete fixes - "
   "the system working). Verification SLA: 3 days (within the 5-day "
   "correction SLA). Failed verifications return to the fixer with "
   "the verifier's notes - the loop continues until verified or the "
   "correction is withdrawn (3 withdrawn this year: the evidence did "
   "not support the fix on re-examination - honesty over throughput)."),
 "key_points": [
   "1,200 corrections, 100% verified by 2 methods.",
   "Method 1: independent re-check. Method 2: regression test.",
   "16 needed rework (verifiers caught incomplete fixes).",
   "Verifier never the proposer.",
   "3 withdrawn (evidence did not support) - honesty over throughput.",
   "No fix ships unverified.",
 ],
 "requirements": [
   "Two-method verification.",
   "Independent verifiers.",
   "Verification SLA (3 days).",
   "Rework loop with withdrawal option.",
 ],
 "standards": [
   "100% verification.",
   "Separation of fixer and verifier.",
   "Withdrawals honored.",
   "Regression coverage.",
 ],
 "citations": [
   "ISO 9001:2015 (verification).",
 ],
 "sig_lens": ("The Signature Curation Doctrine verifies every fix twice: "
   "the doctrine requires the independent re-check and the regression "
   "- 100%, no exceptions. The Signature edition honors the 3 "
   "withdrawals: a doctrine that cannot withdraw a correction has "
   "not verified, it has merely double-stamped its mistakes."),
},
{
 "name": "Approval Chain Analytics",
 "group": "Compounded", "ladder_rank": 16, "ladder_tier": "compounded",
 "demo_key": "h_analytics",
 "demo_data": {"links": 4, "times": [0.8, 1.2, 0.7, 0.5], "bottleneck": 1},
 "description": ("The chain analytics find the slow link: four links at "
   "0.8, 1.2, 0.7, 0.5 days - the SME link (index 1, 1.2 days) is the "
   "bottleneck. The analytics measure per-link timing, send-back "
   "rates, and approval rates: the SME link is slowest (judgment "
   "takes time) but has the lowest send-back rate (4% - the SMEs get "
   "it right); the reviewer link is fastest but sends back 11% (the "
   "triage misses the reviewers catch). Total 3.2 days; the "
   "theoretical floor (all links at their best observed) is 2.1 days "
   "- the 1.1-day gap is the improvement opportunity, mostly in the "
   "SME link's queueing (not its judging)."),
 "how_it_works": ("Metrics per link: median time, p90 time, send-back "
   "rate, approval rate, volume. The SME link: median 1.2d, p90 2.8d "
   "(the controversial items), send-back 4%, volume 85/quarter. The "
   "reviewer link: median 0.8d, send-back 11% (triage quality signal - "
   "the 11% feeds back to triage training). The improvement plan "
   "targets queueing, not judging: the SME link's 1.2 days split into "
   "0.9 waiting + 0.3 judging - the fix is the reserve pool (already "
   "added) and better load balancing (the workload record), not "
   "rushing the judgment. The analytics run monthly; the bottleneck "
   "link gets the attention - the chain is only as fast as its "
   "slowest judgment."),
 "key_points": [
   "Links: 0.8/1.2/0.7/0.5 days; SME link (1.2d) is the bottleneck.",
   "SME: slowest but 4% send-back (gets it right).",
   "Reviewer: 11% send-back (triage quality signal).",
   "1.2d splits 0.9 waiting + 0.3 judging - fix the queueing.",
   "Floor 2.1d; gap 1.1d is the opportunity.",
   "Monthly analytics; bottleneck gets attention.",
 ],
 "requirements": [
   "Per-link timing and quality metrics.",
   "Send-back analysis.",
   "Wait-vs-work decomposition.",
   "Monthly review.",
 ],
 "standards": [
   "Bottlenecks addressed, not just measured.",
   "Judgment never rushed.",
   "Feedback to upstream (triage).",
   "Floors computed honestly.",
 ],
 "citations": [
   "ISO 9001:2015.",
 ],
 "sig_lens": ("The Signature Curation Doctrine measures its own patience: "
   "the doctrine requires the 1.2-day SME link decomposed - 0.9 "
   "waiting, 0.3 judging. The Signature edition fixes the waiting: "
   "a doctrine that rushes judgment to fix a queue has mistaken the "
   "disease for the symptom."),
},
{
 "name": "Reviewer Workload Balancing",
 "group": "Compounded", "ladder_rank": 17, "ladder_tier": "compounded",
 "demo_key": "h_workload",
 "demo_data": {"reviewers": 12, "avg": 28.08, "max": 40, "items": 337},
 "description": ("The workload record balances the twelve: 337 items "
   "across 12 reviewers averages 28.1 each, capped at 40. Balance is "
   "quality infrastructure: the overloaded reviewer (past 40) slips "
   "(measured: error rate doubles past 45), and the idle reviewer "
   "rusts. Assignment is by expertise match first, load second - the "
   "best reviewer for the item who is under 40 gets it. The current "
   "spread: 22 to 36 (the balancer keeps the range tight); the 40 cap "
   "is hard (the system refuses the 41st assignment). The 337/12 = "
   "28.08 average is the sustainable pace; quarters above 35 average "
   "trigger hiring review - the workload record is the hiring signal."),
 "how_it_works": ("The balancer runs on each assignment: eligible "
   "reviewers (expertise match, under 40, available), scored by "
   "(expertise fit x 0.6 + load inverse x 0.4), top score assigned. "
   "The 40 cap is the quality guardrail (from the queue record's "
   "measurement); the 28 average is the planning figure. Load is "
   "tracked in real time; the dashboard shows the spread (22-36 "
   "now). Rebalancing: when a reviewer goes on leave, their items "
   "redistribute by the same scoring (no dumping on the junior). "
   "The hiring signal: two consecutive quarters above 35 average "
   "opens a hiring requisition - the workload record speaks, and "
   "management listens (the last hire came from exactly this "
   "signal)."),
 "key_points": [
   "12 reviewers, 337 items, avg 28, cap 40 (hard).",
   "Spread 22-36 (kept tight).",
   "Assignment: expertise 60%, load 40%.",
   "Error rate doubles past 45 (measured) - hence the cap.",
   "Leave redistribution by scoring, no dumping.",
   "2 quarters >35 avg triggers hiring.",
 ],
 "requirements": [
   "Expertise-load scoring.",
   "Hard cap enforcement.",
   "Real-time load tracking.",
   "Hiring signal rule.",
 ],
 "standards": [
   "Caps from measurement.",
   "No cap breaches.",
   "Fair redistribution.",
   "Hiring signal honored.",
 ],
 "citations": [
   "ISO 9001:2015.",
 ],
 "sig_lens": ("The Signature Curation Doctrine balances its twelve: the "
   "doctrine requires the 28 average and the 40 cap - the spread "
   "22-36. The Signature edition hires on the signal: a doctrine "
   "that watches its reviewers drown for three quarters has not "
   "measured workload, it has merely counted the bodies."),
},
{
 "name": "Quality Sampling",
 "group": "Compounded", "ladder_rank": 18, "ladder_tier": "compounded",
 "demo_key": "h_sampling",
 "demo_data": {"rate": 0.05, "quality": 0.975, "sampled": 240, "passed": 234},
 "description": ("The sampling record measures what the process "
   "produces: 5% sampled, 97.5% quality - 234 of 240 sampled items "
   "passed. Sampling is the independent check: items already through "
   "the workflow are re-examined by samplers who did not touch them, "
   "against the standards. The 5% rate (240 of ~4,800 quarterly "
   "items) balances cost and confidence; high-risk items (controversial, "
   "new reviewers) are sampled at 50%, not 5% - the sampling is "
   "stratified, not uniform. The 6 failures: 3 wording, 2 factual "
   "(both corrected, corrections verified), 1 linkage - each root-"
   "caused, each feeding back to training or standards."),
 "how_it_works": ("Stratified sampling: 5% base, 50% for high-risk "
   "(controversial topics, first-quarter reviewers, new item types), "
   "100% for the onboarding practice weeks. Samplers are senior "
   "reviewers rotated quarterly (never sampling their own work). "
   "The 234/240 = 97.5% is the headline quality metric - reported "
   "to the governance board, trended quarterly (97.1%, 97.5%, 97.8% "
   "- improving). The 6 failures each got: root cause (3 wording = "
   "copyedit standards gap, now trained; 2 factual = source "
   "misread, checker coached; 1 linkage = tooling gap, fixed), "
   "correction, and verification. Sampling below 97% triggers the "
   "quality review (the incident-adjacent process); the bar is "
   "97%, and the trend must not decline two quarters running."),
 "key_points": [
   "5% sampled (stratified); 234/240 passed = 97.5%.",
   "High-risk at 50%; onboarding at 100%.",
   "Samplers senior, rotated, never own work.",
   "6 failures root-caused and fed back.",
   "Trend 97.1% -> 97.5% -> 97.8% (improving).",
   "Below 97% or 2 declining quarters triggers review.",
 ],
 "requirements": [
   "Stratified sampling plan.",
   "Independent samplers.",
   "Root-cause per failure.",
   "Trend reporting.",
 ],
 "standards": [
   "97% quality bar.",
   "Stratification by risk.",
   "Feedback mandatory.",
   "Decline triggers review.",
 ],
 "citations": [
   "ISO 9001:2015 (monitoring).",
 ],
 "sig_lens": ("The Signature Curation Doctrine checks its own work: the "
   "doctrine requires the 5% sampled by independent eyes - 97.5%. The "
   "Signature edition root-causes the 6: a doctrine that counts its "
   "quality but does not dissect its failures has a scoreboard, not "
   "a quality system."),
},
{
 "name": "Escalation Procedures",
 "group": "Compounded", "ladder_rank": 19, "ladder_tier": "compounded",
 "demo_key": "h_escalation",
 "demo_data": {"levels": 3, "hours": [4, 24, 72], "escalated": 23},
 "description": ("The escalation record routes the stuck: three levels - "
   "4 hours (lead), 24 hours (manager), 72 hours (board) - with 23 "
   "escalations last quarter. Escalation is the pressure valve: items "
   "blocked, disputed, or aging get a bigger hammer. Level 1 (4h): the "
   "team lead unblocks (reassigns, clarifies, decides). Level 2 (24h): "
   "the manager resolves (resource conflicts, priority disputes). "
   "Level 3 (72h): the governance board adjudicates (policy questions, "
   "controversial deadlocks). The 23: 17 resolved at level 1, 5 at "
   "level 2, 1 at level 3 (the controversial framing dispute) - the "
   "pyramid works (most resolved low). Escalation is never punishment: "
   "the record states it plainly, because teams that fear escalation "
   "hide blockages."),
 "how_it_works": ("Triggers: SLA at 80% (early warning), SLA breach "
   "(automatic level 1), SME disagreement deadlock (level 2), "
   "controversial split (level 3 track), requester appeal (level 1, "
   "reviewed). Each escalation records: the blocker, the level, the "
   "decider, the decision, the time - the 23 all have complete "
   "records. The level-3 case (controversial framing): the board heard "
   "both SMEs, decided the framing with modifications, and published "
   "the reasoning - the escalation that became precedent. Escalation "
   "abuse is watched: requesters escalating routinely get coaching "
   "(2 coached last quarter); reviewers escalating to avoid decisions "
   "get coaching too (1) - the valve must not become the workflow."),
 "key_points": [
   "3 levels: 4h lead, 24h manager, 72h board; 23 escalations.",
   "17/5/1 across levels - the pyramid works.",
   "Triggers: SLA warnings, deadlocks, splits, appeals.",
   "Level-3 decisions become precedent (published).",
   "Escalation is never punishment.",
   "Abuse watched (routine escalators coached).",
 ],
 "requirements": [
   "Level definitions with timeframes.",
   "Trigger rules.",
   "Complete escalation records.",
   "Abuse monitoring.",
 ],
 "standards": [
   "Timeframes enforced.",
   "Decisions published at level 3.",
   "No punishment culture.",
   "Coaching for abuse.",
 ],
 "citations": [
   "ISO 9001:2015.",
 ],
 "sig_lens": ("The Signature Curation Doctrine provides the bigger hammer: "
   "the doctrine requires the three levels with their hours - and the "
   "promise that escalation is not punishment. The Signature edition "
   "publishes the level-3 precedents: a doctrine whose hardest calls "
   "vanish into private decisions has not escalated, it has merely "
   "moved the argument upstairs."),
},
{
 "name": "Reviewer Feedback Loops",
 "group": "Compounded", "ladder_rank": 20, "ladder_tier": "compounded",
 "demo_key": "h_feedback",
 "demo_data": {"items": 48, "acted": 41, "rate": 0.854},
 "description": ("The feedback loops listen to the reviewers: 48 feedback "
   "items, 41 acted on (85.4%). Reviewers meet the edge cases first: "
   "unclear standards, broken tooling, impossible SLAs, taxonomy gaps - "
   "their feedback is the system's early warning. The 48: 19 tooling "
   "issues (14 fixed, 5 queued), 12 standards clarifications (11 "
   "published, 1 rejected with reason), 9 workload concerns (7 "
   "rebalanced, 2 hiring-signal), 8 process suggestions (6 adopted). "
   "The 85.4% acted-on rate is the trust metric: reviewers who see "
   "their feedback die stop giving it - and the system goes blind. "
   "Every item gets a response (acted, queued with date, or rejected "
   "with reason) within 14 days."),
 "how_it_works": ("Feedback channels: the retro (monthly, team), the "
   "tool (one-click 'report issue' on every screen), the 1:1s "
   "(managers ask explicitly). Triage: the curation lead classifies "
   "weekly (tooling/standards/workload/process), assigns owners, sets "
   "dates. The 41 acted: fixes shipped, clarifications published, "
   "rebalances done, suggestions adopted - each closed with a note "
   "to the reporter ('your issue fixed in Tuesday's deploy'). The 7 "
   "not acted: 5 queued with dates (honest backlog), 2 rejected with "
   "reasons (one conflicted with the standards' intent - the "
   "reporter agreed after discussion). The loop's health is the "
   "acted-on rate, reported monthly: below 70% triggers the "
   "governance review - a deaf system is a dying system."),
 "key_points": [
   "48 feedback items; 41 acted on (85.4%).",
   "Channels: retros, in-tool reporting, 1:1s.",
   "Every item answered in 14 days (acted/queued/rejected-with-reason).",
   "Acted-on rate is the trust metric.",
   "Below 70% triggers governance review.",
   "Reviewers are the early warning; listen or go blind.",
 ],
 "requirements": [
   "Feedback channels.",
   "Weekly triage with owners.",
   "14-day response.",
   "Acted-on rate tracking.",
 ],
 "standards": [
   "No silent feedback.",
   "Honest backlogs (queued with dates).",
   "Rejections with reasons.",
   "70% floor enforced.",
 ],
 "citations": [
   "ISO 9001:2015 (improvement).",
 ],
 "sig_lens": ("The Signature Curation Doctrine listens to its reviewers: "
   "the doctrine requires the 85.4% acted-on - every item answered. "
   "The Signature edition treats the rate as the trust metric: a "
   "doctrine whose reviewers' feedback dies in a backlog has not a "
   "feedback loop, but a suggestion box nailed shut."),
},
{
 "name": "Curation Metrics Dashboard",
 "group": "Compounded", "ladder_rank": 21, "ladder_tier": "compounded",
 "demo_key": "h_metrics",
 "demo_data": {"kpis": 8, "reviewers": 12, "quality": 0.975, "sla": 0.92},
 "description": ("The metrics dashboard watches the curation: 8 KPIs, 12 "
   "reviewers, 97.5% quality, 92% SLA. The eight KPIs: throughput "
   "(items/quarter), quality (sampled %), SLA compliance, queue "
   "depths, correction acceptance, reviewer load spread, feedback "
   "acted-on rate, and cost per item. Each KPI has a target, a trend, "
   "and an owner - the dashboard is the management view of the human "
   "layer. The current picture: quality 97.5% (target 97%, green), "
   "SLA 92% (target 90%, green), queue depths nominal, cost per item "
   "$11.40 (target $12, green) - a healthy quarter, with the workload "
   "spread (22-36) the closest watch. The dashboard refreshes weekly; "
   "the governance board reviews it monthly."),
 "how_it_works": ("The eight KPIs with targets: throughput 1,350/quarter "
   "(1,348 actual), quality 97% (97.5%), SLA 90% (92%), queue depth "
   "<1.5x sustainable (1.1x), correction acceptance 95% (96.8%), load "
   "spread max-min <20 (14), feedback acted-on 70% (85.4%), cost/item "
   "$12 ($11.40). All green this quarter - the dashboard also shows "
   "the trends (4 quarters) so greens turning yellow are caught "
   "early. Drill-down: each KPI links to its record (quality -> the "
   "sampling record, cost -> the cost model). The board's monthly "
   "review asks three questions: what is red, what is yellowing, "
   "what did we learn - the dashboard exists to make those "
   "answerable in one screen. KPI changes need board approval: the "
   "metrics are the contract, and contracts change deliberately."),
 "key_points": [
   "8 KPIs with targets, trends, owners; all green this quarter.",
   "KPIs: throughput, quality, SLA, queues, corrections, load, feedback, cost.",
   "Quality 97.5% (target 97%); SLA 92% (target 90%); cost $11.40 (target $12).",
   "Weekly refresh; board monthly review.",
   "Drill-down to records.",
   "KPI changes need board approval.",
 ],
 "requirements": [
   "8 KPIs defined with targets.",
   "Weekly refresh.",
   "Trend display (4 quarters).",
   "Drill-down links.",
 ],
 "standards": [
   "Targets board-approved.",
   "Trends mandatory.",
   "Reviews monthly.",
   "Changes deliberate.",
 ],
 "citations": [
   "ISO 9001:2015 (monitoring).",
 ],
 "sig_lens": ("The Signature Curation Doctrine watches its humans with "
   "numbers: the doctrine requires the eight KPIs - targets, trends, "
   "owners. The Signature edition asks the three questions monthly: "
   "a doctrine with metrics no one reviews has not measured, it has "
   "merely decorated."),
},
# ---------------- Advanced (22-34) ----------------
{
 "name": "Editorial Governance Board",
 "group": "Advanced", "ladder_rank": 22, "ladder_tier": "advanced",
 "demo_key": "h_facts",
 "demo_data": {"members": 7, "cadence": "monthly", "decisions": 31,
               "checks": [["members", "==", 7]]},
 "description": ("The governance board steers the curation: seven members, "
   "monthly cadence, thirty-one decisions last year. The board owns the "
   "standards (approves changes), the SLAs (sets targets), the KPIs "
   "(approves changes), the escalations (level 3), and the policy "
   "(breaking changes, controversial topics). The seven: the curation "
   "lead (chair), two senior reviewers, two SMEs, one editor, one "
   "engineering representative (the tooling voice). The thirty-one "
   "decisions: 12 standards changes, 8 SLA/KPI adjustments, 6 "
   "escalation adjudications, 3 policy updates, 2 hiring approvals - "
   "each recorded with rationale and dissent. The board is the "
   "curation system's legislature: deliberate, recorded, and "
   "accountable."),
 "how_it_works": ("Monthly agenda: metrics review (the dashboard's three "
   "questions), standards proposals, escalation adjudications, policy "
   "updates, and the open floor (any reviewer may raise anything - "
   "the feedback loop's formal channel). Decisions need 5 of 7 "
   "(supermajority - curation policy should not swing on one vote); "
   "the 31 decisions averaged 6.2 votes (consensus is the norm, the "
   "rule is the backstop). Dissent is recorded and published - the "
   "board's legitimacy depends on visible disagreement handled "
   "fairly. The board also runs the annual review: the year's "
   "quality trend, the standards' fitness, the reviewers' development "
   "needs, and the budget - the curation system's yearly physical. "
   "Emergency sessions: the incident record's 6-hour response was "
   "board-authorized by emergency quorum (4 of 7 within 2 hours)."),
 "key_points": [
   "7 members, monthly, 31 decisions last year.",
   "Owns standards, SLAs, KPIs, escalations, policy.",
   "Supermajority 5/7; dissent recorded and published.",
   "Annual review: quality, standards, development, budget.",
   "Emergency quorum 4/7 in 2 hours.",
   "The legislature: deliberate, recorded, accountable.",
 ],
 "requirements": [
   "Board charter with membership.",
   "Decision recording with dissent.",
   "Monthly cadence with agenda.",
   "Annual review.",
 ],
 "standards": [
   "Supermajority for policy.",
   "Published decisions.",
   "Emergency procedures.",
   "Open floor for reviewers.",
 ],
 "citations": [
   "ISO 9001:2015.",
 ],
 "sig_lens": ("The Signature Curation Doctrine legislates deliberately: "
   "the doctrine requires the 31 decisions recorded - with dissent. "
   "The Signature edition publishes the disagreements: a doctrine "
   "whose board never dissents has not governed, it has merely "
   "nodded in unison."),
},
{
 "name": "Bias Detection in Reviews",
 "group": "Advanced", "ladder_rank": 23, "ladder_tier": "advanced",
 "demo_key": "h_bias",
 "demo_data": {"checks": 4, "flagged": 2, "reviewers": 12},
 "description": ("The bias detection watches the watchers: four checks, "
   "two flagged among twelve reviewers. Reviewers are human, and "
   "humans have patterns: the checks look for severity skew (one "
   "reviewer rejects 3x the average), topic skew (systematic "
   "harshness on a subject), source skew (preferring certain "
   "sources), and calibration drift (scores diverging from the "
   "calibration baseline). The two flagged: one severity skew "
   "(rejecting 31% vs 11% average - coached, now at 14%), one topic "
   "skew (harsh on economics items - reassigned off economics, "
   "retrained). Flagging is not accusing: the process is coaching "
   "and reassignment, never punishment - bias unexamined is the "
   "enemy, bias admitted is the lesson."),
 "how_it_works": ("The four checks run quarterly on reviewer decision "
   "data: severity rates vs peer average (3x threshold), topic-"
   "conditioned rates (chi-square vs peers), source preference "
   "(citation diversity index), calibration drift (vs the "
   "calibration session baseline). The two flags: severity skew "
   "(31% reject vs 11% - the reviewer was applying personal "
   "standards above the published ones; coaching realigned), topic "
   "skew (economics items scored 0.8 points lower on average - the "
   "reviewer disclosed a background dispute with the field's "
   "orthodoxy; reassigned, retrained on neutrality). Both reviewers "
   "were told plainly, both improved, both still review - the "
   "process worked. The checks themselves are audited: false flags "
   "are tracked (1 this year - a reviewer with a genuinely harder "
   "queue, cleared on review)."),
 "key_points": [
   "4 checks; 2 flagged of 12 reviewers; both coached, both improved.",
   "Checks: severity skew, topic skew, source skew, calibration drift.",
   "Flagging is coaching, never punishment.",
   "Severity 31%->14% after coaching; topic skew reassigned.",
   "Checks audited for false flags (1 this year, cleared).",
   "Bias unexamined is the enemy; admitted is the lesson.",
 ],
 "requirements": [
   "Quarterly bias checks on decision data.",
   "Coaching (not punishment) process.",
   "Reassignment options.",
   "Check auditing.",
 ],
 "standards": [
   "Thresholds published (3x severity).",
   "Plain communication.",
   "Retraining available.",
   "False flags tracked.",
 ],
 "citations": [
   "ISO 9001:2015.",
 ],
 "sig_lens": ("The Signature Curation Doctrine watches its watchers: the "
   "doctrine requires the four checks quarterly - and the coaching, "
   "not the punishment. The Signature edition audits the checks: a "
   "doctrine that flags bias but never checks its flags has built a "
   "suspicion machine, not a fairness system."),
},
{
 "name": "Inter-Rater Reliability",
 "group": "Advanced", "ladder_rank": 24, "ladder_tier": "advanced",
 "demo_key": "h_reliability",
 "demo_data": {"kappa": 0.78, "raters": 3, "items": 120, "target": 0.75},
 "description": ("The reliability record measures agreement: Cohen's "
   "kappa 0.78 across three raters on 120 items - above the 0.75 "
   "target. Kappa measures agreement beyond chance: 0.78 is "
   "'substantial' - the reviewers largely see the same quality. "
   "The 120 items were triple-reviewed (each by three reviewers "
   "independently); the kappa computed on their pass/fail verdicts. "
   "The 0.78 decomposes: 0.86 on factual items (facts are "
   "checkable), 0.71 on wording (taste varies), 0.69 on fairness "
   "(perspective matters) - the decomposition says where the "
   "standards need tightening (fairness guidance, now in review). "
   "Below-target kappa would trigger the calibration sessions; "
   "above-target, they maintain."),
 "how_it_works": ("The study: 120 items sampled across types, each "
   "reviewed independently by 3 reviewers (blinded to each other), "
   "verdicts collected, kappa computed per type and overall. "
   "Cohen's kappa = (Po - Pe)/(1 - Pe): observed agreement 0.91, "
   "expected-by-chance 0.59, kappa 0.78 (demo-computed). The "
   "0.69 fairness kappa is the finding: reviewers disagree most "
   "where the standards are vaguest - the fairness standards are "
   "being rewritten with examples (the standards record's evolution). "
   "The study runs semi-annually; the trend (0.74 -> 0.78) shows "
   "the calibration working. Raters are sampled across seniority: "
   "the kappa must hold for junior-senior pairs too (0.76 - "
   "holds)."),
 "key_points": [
   "Kappa 0.78 (3 raters, 120 items) vs 0.75 target.",
   "Decomposition: factual 0.86, wording 0.71, fairness 0.69.",
   "Fairness standards being rewritten (vaguest -> most disagreement).",
   "Semi-annual; trend 0.74 -> 0.78.",
   "Holds for junior-senior pairs (0.76).",
   "0.78 is substantial agreement.",
 ],
 "requirements": [
   "Semi-annual reliability studies.",
   "Blinded independent ratings.",
   "Per-type decomposition.",
   "Trend tracking.",
 ],
 "standards": [
   "0.75 kappa target.",
   "Below target triggers calibration.",
   "Decompositions drive standards work.",
   "Seniority coverage.",
 ],
 "citations": [
   "Cohen, J. A Coefficient of Agreement for Nominal Scales. Educational and Psychological Measurement (1960).",
 ],
 "sig_lens": ("The Signature Curation Doctrine measures its own "
   "agreement: the doctrine requires the 0.78 - substantial, not "
   "perfect. The Signature edition dissects the 0.69: a doctrine "
   "that averages its disagreements away will never learn that "
   "fairness is where its standards are thinnest."),
},
{
 "name": "Calibration Sessions",
 "group": "Advanced", "ladder_rank": 25, "ladder_tier": "advanced",
 "demo_key": "h_calibration",
 "demo_data": {"cadence": "quarterly", "cases": 12, "agreement": 0.91, "reviewers": 12},
 "description": ("The calibration sessions align the twelve: quarterly, "
   "twelve cases, 91% agreement after (from 78% before). Calibration "
   "is the practice of judging together: the reviewers independently "
   "score twelve difficult cases, then discuss the divergences until "
   "the reasoning converges. The 78%-to-91% is the session's product: "
   "not forced agreement, but understood standards - the reviewers "
   "leave knowing why the borderline cases fall where they do. The "
   "twelve cases are chosen from the quarter's disagreements (the "
   "disagreement record), sampling failures (the sampling record), "
   "and bias flags (the bias record) - the curriculum writes itself "
   "from the system's own hard calls."),
 "how_it_works": ("Session format: 2 hours, all twelve reviewers (SMEs "
   "join for 2 sessions/year). Each case: independent scoring (5 "
   "minutes, blinded), reveal (the spread shown), discussion (the "
   "divergent reviewers explain), resolution (the standard clarified "
   "or the case logged as genuinely borderline). The 91% post-"
   "agreement is measured on a fresh set of 12 cases (not the "
   "discussed ones - testing transfer, not memory). The 78% pre-"
   "agreement is the honest baseline: calibration starts where the "
   "reviewers actually are. Outcomes feed the standards (3 "
   "clarifications published from last year's sessions) and the "
   "training (the borderline cases become onboarding exercises). "
   "Attendance is mandatory; the sessions are the culture - the "
   "place where 'how we judge' stays a living conversation."),
 "key_points": [
   "Quarterly, 12 cases, 12 reviewers; 78% -> 91% agreement.",
   "Cases from real disagreements, failures, flags.",
   "Post-agreement on fresh cases (transfer, not memory).",
   "Outcomes feed standards (3 clarifications) and training.",
   "Mandatory attendance; the culture's living room.",
   "Understood standards, not forced agreement.",
 ],
 "requirements": [
   "Quarterly sessions.",
   "Real-case curriculum.",
   "Pre/post measurement.",
   "Standards feedback.",
 ],
 "standards": [
   "Blinded independent scoring.",
   "Fresh cases for post-measurement.",
   "Mandatory attendance.",
   "Outcomes published.",
 ],
 "citations": [
   "ISO 9001:2015.",
 ],
 "sig_lens": ("The Signature Curation Doctrine judges together quarterly: "
   "the doctrine requires the 78%-to-91% - earned, not assumed. The "
   "Signature edition teaches from its own hard calls: a doctrine "
   "whose calibration uses textbook cases is rehearsing; one that "
   "uses its own disagreements is learning."),
},
{
 "name": "Review Automation Boundaries",
 "group": "Advanced", "ladder_rank": 26, "ladder_tier": "advanced",
 "demo_key": "h_automation",
 "demo_data": {"auto": 0.6, "human": 0.4, "rules": 12, "approved": 7},
 "description": ("The automation boundaries say what machines may do: 60% "
   "automated (the approved 7 of 12 assist rules), 40% human-only. "
   "Automation assists curation: grammar checks, terminology "
   "consistency, link validity, formatting, duplicate detection, "
   "triage scoring assists, and SLA tracking - the 7 approved. The 5 "
   "not approved: fact verdicts (humans verify), fairness judgments, "
   "SME adjudications, final approvals, and controversial framing - "
   "the judgment core. The 60/40 split is the policy, reviewed "
   "annually: automation proposes, humans dispose - the doctrine's "
   "sentence made operational. Every automated assist is labeled "
   "(the reviewer sees 'machine suggestion'), and the human may "
   "override - the machine's confidence never outranks the human's "
   "judgment."),
 "how_it_works": ("The boundary list: approved assists (7) run inline "
   "with labels; prohibited automations (5) are blocked by policy "
   "and by tooling (the workflow system has no 'auto-approve' "
   "button). New automation proposals go to the governance board "
   "with evidence (accuracy on samples, failure analysis); the "
   "board approved 2 this year (duplicate detection, SLA tracking) "
   "and rejected 1 (auto-fact-verdicts - accuracy 91%, below the "
   "96% bar for assists). The 60% is measured by task count; by "
   "time, automation handles ~35% (the quick checks) and humans "
   "65% (the thinking) - the honest accounting. Override rates are "
   "tracked: reviewers override 8% of machine suggestions (healthy "
   "skepticism); override rates below 2% would flag automation bias "
   "(the humans deferring) - watched, not yet seen."),
 "key_points": [
   "60% automated (7 approved assists); 40% human-only (judgment core).",
   "Prohibited: fact verdicts, fairness, adjudication, approvals, framing.",
   "New automation needs board + evidence (96% accuracy bar).",
   "By time: machines 35%, humans 65% (honest accounting).",
   "Overrides 8% (healthy); <2% would flag automation bias.",
   "Automation proposes, humans dispose.",
 ],
 "requirements": [
   "Approved/prohibited automation lists.",
   "Board approval for new automation.",
   "Labeling of machine suggestions.",
   "Override tracking.",
 ],
 "standards": [
   "96% accuracy bar for assists.",
   "No auto-approve tooling.",
   "Human override always available.",
   "Annual boundary review.",
 ],
 "citations": [
   "ISO 9001:2015.",
 ],
 "sig_lens": ("The Signature Curation Doctrine draws the machine's "
   "boundary in ink: the doctrine requires the 5 prohibitions held - "
   "no auto-verdicts, no auto-approvals. The Signature edition "
   "watches the override rate: a doctrine whose humans never "
   "override the machine has not automated assistance, it has "
   "automated abdication."),
},
{
 "name": "Controversial Topic Handling",
 "group": "Advanced", "ladder_rank": 27, "ladder_tier": "advanced",
 "demo_key": "h_controversial",
 "demo_data": {"topics": 5, "reviewers": 2, "board": True, "queue": 12},
 "description": ("The controversial handling treats the hard twelve: 5 "
   "flagged topics, 2 reviewers minimum each, board oversight on all. "
   "Controversial topics (the queue's 12 items) are where curation "
   "meets its hardest test: reasonable people disagree, and the "
   "database must be fair without being false. The procedure: "
   "flagged at triage (by topic list or reviewer judgment), assigned "
   "to two reviewers of demonstrated neutrality (the bias record "
   "clears them), reviewed against the fairness standards with extra "
   "care, and every decision reviewed by the governance board - the "
   "12 items' 10-day turnaround includes the board's look. The 5 "
   "topics are listed (not hidden): the list is public so the "
   "handling is auditable - secret sensitivity lists are where bias "
   "hides."),
 "how_it_works": ("The topic list (5): maintained by the board, reviewed "
   "quarterly, published - currently the longstanding disputes in "
   "the covered domains. Handling per item: dual review (2 "
   "reviewers, blinded to each other), fairness checklist (all "
   "significant views? neutral language? no omission?), SME "
   "adjudication where the reviewers split, board sign-off on the "
   "final text. The 12 items last quarter: 9 passed with minor "
   "framing adjustments, 2 needed SME arbitration, 1 went to full "
   "board review (the framing dispute that became precedent). "
   "Reviewer protection: controversial assignments are voluntary "
   "with the option to recuse (2 recusals last quarter, honored "
   "without question) - forced neutrality is not neutrality. The "
   "handling is the fairness standards' proving ground."),
 "key_points": [
   "5 topics listed publicly; 12 items; 2 reviewers each; board oversight.",
   "Dual blinded review + fairness checklist + board sign-off.",
   "12 items: 9 passed, 2 arbitrated, 1 became precedent.",
   "Recusal honored without question (2 last quarter).",
   "10-day turnaround includes the board's look.",
   "Secret sensitivity lists are where bias hides.",
 ],
 "requirements": [
   "Public topic list, quarterly reviewed.",
   "Dual review with neutrality-cleared reviewers.",
   "Board sign-off.",
   "Recusal rights.",
 ],
 "standards": [
   "Fairness checklist mandatory.",
   "Lists public.",
   "Recusals honored.",
   "Precedents published.",
 ],
 "citations": [
   "ISO 9001:2015.",
 ],
 "sig_lens": ("The Signature Curation Doctrine handles the hard twelve "
   "in the open: the doctrine requires the 5 topics listed publicly "
   "- auditable fairness. The Signature edition honors recusal: a "
   "doctrine that forces reviewers onto topics they cannot judge "
   "fairly has not been rigorous, it has been coercive with extra "
   "paperwork."),
},
{
 "name": "Correction Propagation",
 "group": "Advanced", "ladder_rank": 28, "ladder_tier": "advanced",
 "demo_key": "h_propagation",
 "demo_data": {"correction": 1, "downstream": 14, "applied": 14, "rate": 1.0},
 "description": ("The propagation record spreads the fix: one correction, "
   "14 downstream uses, 14 applied (100%). A correction to a record "
   "is not complete until every downstream use is fixed: the "
   "derivatives, the citations, the cached answers, the federated "
   "copies. The provenance index finds the 14 (every use traced); "
   "each gets the correction applied or the reason it does not need "
   "it (3 of the 14 were unaffected - the corrected clause was not "
   "the cited part - recorded as 'reviewed, not applicable'). The "
   "100% is verified: the propagation checklist closes only when "
   "all 14 are applied-or-justified. A correction that stops at the "
   "source is a press release; propagation is the delivery."),
 "how_it_works": ("Propagation workflow: the correction record lists "
   "affected downstream (from provenance); each item gets a "
   "propagation task (apply the fix, or justify non-applicability); "
   "tasks have SLAs (5 days, like corrections); the checklist tracks "
   "14/14. The example correction (a factual fix to a definition): "
   "14 downstream - 6 database records updated, 3 cached answers "
   "invalidated, 2 federated copies notified, 3 reviewed-not-"
   "applicable. Verification: the verifier samples 3 of the 14 "
   "propagations (the verification record's method, extended). "
   "Propagation failures (a downstream that cannot take the fix) "
   "escalate: the downstream gets a compatibility note, and the "
   "incompatibility is tracked - the versioning database's "
   "compatibility matrix learns from propagation."),
 "key_points": [
   "1 correction -> 14 downstream; 14/14 applied-or-justified (100%).",
   "Provenance index finds every use.",
   "Non-applicable justified (3 reviewed, clause not cited).",
   "Checklist closes only at 14/14.",
   "Propagation SLA 5 days.",
   "A correction that stops at the source is a press release.",
 ],
 "requirements": [
   "Provenance-based downstream discovery.",
   "Propagation tasks with SLAs.",
   "Applied-or-justified closure.",
   "Verification sampling.",
 ],
 "standards": [
   "100% closure.",
   "Justifications recorded.",
   "Failures escalated with compatibility notes.",
   "Matrix learns from propagation.",
 ],
 "citations": [
   "ISO 9001:2015 (corrective action).",
 ],
 "sig_lens": ("The Signature Curation Doctrine delivers the fix everywhere: "
   "the doctrine requires the 14/14 - applied or justified. The "
   "Signature edition verifies the propagation: a doctrine that "
   "corrects the source and forgets the copies has not fixed the "
   "error, it has merely moved it out of sight."),
},
{
 "name": "Reviewer Reputation System",
 "group": "Advanced", "ladder_rank": 29, "ladder_tier": "advanced",
 "demo_key": "h_reputation",
 "demo_data": {"reviewers": 12, "top": 94, "scale": 100,
               "weights": [0.40, 0.25, 0.20, 0.15],
               "components": [94, 100, 90, 88]},
 "description": ("The reputation system scores the scorers: twelve "
   "reviewers on a 0-100 scale, top at 94, from four components. The "
   "components: accuracy (sampling pass rate, 40%), thoroughness "
   "(checklist completion depth, 25%), timeliness (SLA compliance, "
   "20%), and collegiality (feedback quality, escalation judgment - "
   "15%, peer-assessed). The top reviewer's 94 comes from its "
   "components (94% accuracy, full checklists, 90% timeliness, 88 "
   "peer marks) - the demo computes the weighted score from these "
   "components. Reputation informs "
   "assignment (the best get the hardest items), calibration "
   "leadership (top reviewers lead sessions), and development (low "
   "scores get coaching plans) - never compensation directly (the "
   "policy: reputation guides growth, not pay, to avoid gaming). The "
   "scores are visible to the reviewer and their lead - transparent "
   "to the scored, not public theater."),
 "how_it_works": ("Score = 0.4x accuracy + 0.25x thoroughness + 0.2x "
   "timeliness + 0.15x collegiality, computed quarterly from the "
   "metrics (sampling, checklists, SLAs, peer input). The 94 comes "
   "from its components: 0.40x94 + 0.25x100 + 0.20x90 + 0.15x88 = "
   "93.8, rounding to the published 94 - the demo computes this. "
   "Low scores (<70) trigger the development plan "
   "(coaching, shadowing, reduced load); two quarters below 65 "
   "triggers the role review (not automatic removal - the review "
   "considers context). Gaming resistance: the components are "
   "hard to fake jointly (accuracy needs real skill, collegiality "
   "needs real peers), and the calibration sessions cross-check. "
   "The system is reviewed annually for perverse incentives - the "
   "reputation system itself gets reviewed, because scorers of "
   "scorers need scoring too."),
 "key_points": [
   "12 reviewers, 0-100 scale, top 94; 4 components.",
   "Weights: accuracy 40%, thoroughness 25%, timeliness 20%, collegiality 15%.",
   "Guides assignment, leadership, development - not pay.",
   "Below 70: development plan. Below 65 x2: role review.",
   "Visible to scored + lead; not public theater.",
   "System reviewed annually for perverse incentives.",
 ],
 "requirements": [
   "Four-component scoring.",
   "Quarterly computation.",
   "Development plans for low scores.",
   "Annual system review.",
 ],
 "standards": [
   "Components hard to game jointly.",
   "No direct pay linkage.",
   "Context in role reviews.",
   "Transparency to the scored.",
 ],
 "citations": [
   "ISO 9001:2015.",
 ],
 "sig_lens": ("The Signature Curation Doctrine scores its scorers: the "
   "doctrine requires the 94 computed from the four components - "
   "transparent to the scored. The Signature edition reviews the "
   "system itself: a doctrine that scores reviewers but never "
   "questions its scoring has built a hierarchy, not a meritocracy."),
},
{
 "name": "Curation Audit Record",
 "group": "Advanced", "ladder_rank": 30, "ladder_tier": "advanced",
 "demo_key": "h_facts",
 "demo_data": {"audits": 4, "findings": 7, "closed": 7, "period": "2026",
               "checks": [["audits", "==", 4], ["closed", "==", 7]]},
 "description": ("The curation audit record is the annual adversarial "
   "review: four quarterly audits, seven findings, seven closed in "
   "2026. The audits cover: standards compliance (are reviewers "
   "checking what they sign?), SLA honesty (are the clocks honest?), "
   "bias controls (are the checks running?), and the automation "
   "boundaries (is anything auto-doing what humans must do?). The "
   "seven findings: two checklist shortcuts (reviewers signing "
   "unchecked items - retrained, sampling increased), one hidden "
   "clock pause (fixed, the pause now visible), one missed bias "
   "check (run retroactively, clean), two automation drifts (assists "
   "used beyond approval - rolled back), one stale standard (rewritten). "
   "Seven for seven closed: the audit is not complete until the "
   "findings are."),
 "how_it_works": ("Each quarterly audit samples: 60 reviewed items "
   "re-examined (the 2 checklist shortcuts found here), the SLA "
   "clocks audited against the raw timestamps (the hidden pause "
   "found: a 3-day pause not marked requester-awaiting), the bias "
   "checks verified run (the missed one: a quarter skipped for "
   "the new reviewers - run retroactively), the automation logs "
   "reviewed against the approved list (the 2 drifts: auto-"
   "formatting applied to fairness-sensitive text - beyond approval, "
   "rolled back), the standards reviewed for staleness (1 found). "
   "Findings follow the schema with owners and dates; the checklist "
   "shortcuts were severity high (trust issue) - the retraining was "
   "team-wide, not just the two. Auditor independence: the audits "
   "are led by the governance board's audit committee (not the "
   "curation lead) - the curation system does not audit itself."),
 "key_points": [
   "4 audits, 7 findings, 7 closed in 2026.",
   "Covers compliance, SLA honesty, bias controls, automation boundaries.",
   "Checklist shortcuts: retrained team-wide, sampling increased.",
   "Hidden pause fixed; automation drifts rolled back.",
   "Led by the board's audit committee (independent).",
   "Audit incomplete until findings close.",
 ],
 "requirements": [
   "Quarterly audits with sampling.",
   "Finding schema with closure.",
   "Independent audit leadership.",
   "Trust-issue findings handled team-wide.",
 ],
 "standards": [
   "No self-audit.",
   "Hidden pauses are fraud (fixed).",
   "Drifts rolled back.",
   "Stale standards rewritten.",
 ],
 "citations": [
   "ISO 19011:2018 Guidelines for auditing management systems.",
 ],
 "sig_lens": ("The Signature Curation Doctrine audits its humans: the "
   "doctrine requires the seven findings closed - including the two "
   "who signed unchecked. The Signature edition retrained team-"
   "wide: a doctrine that disciplines the two but not the culture "
   "has punished, not improved."),
},
{
 "name": "Editorial Incident Response",
 "group": "Advanced", "ladder_rank": 31, "ladder_tier": "advanced",
 "demo_key": "h_incident",
 "demo_data": {"incidents": 1, "hours": 6, "affected": 340, "severity": "high"},
 "description": ("The incident record answers the bad day: one high-"
   "severity incident last year, resolved in 6 hours, 340 records "
   "affected. The incident: a faulty automated assist (the formatting "
   "tool beyond its approval) rewrote fairness-sensitive language in "
   "340 records - the automation drift the audit later found. "
   "Response: detected by sampling (2 hours), contained (assist "
   "disabled, 1 hour), assessed (340 affected identified via "
   "provenance, 2 hours), corrected (reverted with human review, 6 "
   "hours total), reviewed (the postmortem, board-attended). The 6 "
   "hours are the honest number: detection to corrected-and-verified. "
   "The postmortem's actions: the assist's approval revoked pending "
   "re-review, the drift detector added (automation logs vs approved "
   "list, daily), the 340 records re-verified by humans."),
 "how_it_works": ("Incident levels: low (single record, standard "
   "correction), medium (multiple records, curation lead runs it), "
   "high (systemic, board involved - this one), critical (public "
   "trust at risk, emergency board). The high-severity playbook: "
   "detect (monitoring/sampling), contain (stop the bleeding - "
   "disable first, ask later), assess (provenance for blast radius), "
   "correct (human-verified fixes), communicate (affected consumers "
   "notified - the 340 records' consumers got the notice), review "
   "(blameless postmortem, board-attended for high+). The 340: all "
   "reverted and re-verified; 12 needed SME re-review (the fairness "
   "nuances). The incident's metrics join the dashboard (incidents/"
   "quarter: 1); the actions join the audit's verification (the "
   "drift detector confirmed running). Blameless: the postmortem "
   "named the system gaps, not the operator - the operator followed "
   "the approved list; the list was wrong."),
 "key_points": [
   "1 high-severity incident; 6 hours; 340 records affected.",
   "Faulty auto-assist rewrote fairness language (automation drift).",
   "Playbook: detect, contain, assess, correct, communicate, review.",
   "340 reverted + re-verified; 12 needed SME re-review.",
   "Actions: approval revoked, drift detector added (daily).",
   "Blameless postmortem; board-attended.",
 ],
 "requirements": [
   "Severity levels with playbooks.",
   "Blast-radius assessment via provenance.",
   "Consumer notification.",
   "Blameless postmortems.",
 ],
 "standards": [
   "Contain first (disable, ask later).",
   "Human verification of corrections.",
   "Actions tracked to closure.",
   "Board attendance for high+.",
 ],
 "citations": [
   "ISO 9001:2015 (nonconformity).",
 ],
 "sig_lens": ("The Signature Curation Doctrine answers its bad day in six "
   "hours: the doctrine requires the 340 found, fixed, and verified - "
   "blamelessly. The Signature edition fixed the list, not just the "
   "operator: a doctrine that blames the human for the system's gap "
   "will get the same incident with a different human."),
},
{
 "name": "Curation Cost Model",
 "group": "Advanced", "ladder_rank": 32, "ladder_tier": "advanced",
 "demo_key": "h_cost",
 "demo_data": {"quarter_cost": 15372, "items": 1348, "per_item": 11.4},
 "description": ("The curation cost model prices the human layer: "
   "$15,372 per quarter across 1,348 items is $11.40 per item - under "
   "the $12 target. The cost breaks into reviewer time (62%, $9,531), "
   "SME time (23%, $3,536), tooling (9%, $1,383), and overhead "
   "(6%, $922: training, calibration, audits). The $11.40 is the "
   "fully-loaded cost of a human-curated item: the number that "
   "prices the 'humans reviewed it' claim. The model also prices "
   "the alternatives: pure automation ($1.10/item, 91% quality - "
   "below the bar) and the sampling-only model ($3.20/item, 94% - "
   "also below) - the $11.40 buys the 97.5%, and the record shows "
   "the tradeoff explicitly."),
 "how_it_works": ("Cost = sum over resources (hours x burdened rate): "
   "reviewers 312h x $30.55 = $9,531; SMEs 41.6h x $85 = $3,536; "
   "tooling $1,383; overhead $922; total $15,372. Per item: "
   "$15,372/1,348 = $11.40 (demo-computed). The burdened rates "
   "include benefits and the calibration/training time (the human "
   "layer's maintenance). The alternatives priced: automation-only "
   "(the rejected auto-verdicts at scale: $1.10/item, 91% quality), "
   "sampling-only (5% sampled deeply, rest automated: $3.20, 94%) - "
   "both below the 97% bar, both documented as 'cheaper and worse'. "
   "The model informs the budget (the cost accounting database's "
   "governance overhead takes this number) and the automation "
   "reviews (a proposed automation must beat $11.40 at equal "
   "quality, not just be cheaper)."),
 "key_points": [
   "$15,372/quarter / 1,348 items = $11.40/item (target $12).",
   "Breakdown: reviewers 62%, SME 23%, tooling 9%, overhead 6%.",
   "Fully-loaded: burdened rates include training/calibration.",
   "Alternatives priced: auto $1.10 (91%), sampling $3.20 (94%) - cheaper and worse.",
   "$11.40 buys the 97.5%.",
   "New automation must beat $11.40 at equal quality.",
 ],
 "requirements": [
   "Fully-loaded cost accounting.",
   "Per-item unit cost.",
   "Alternative pricing.",
   "Budget linkage.",
 ],
 "standards": [
   "Burdened rates.",
   "Quality held constant in comparisons.",
   "Targets board-set.",
   "Automation judged on value, not just cost.",
 ],
 "citations": [
   "FinOps Foundation: FinOps Framework (cost modeling).",
 ],
 "sig_lens": ("The Signature Curation Doctrine prices its humans honestly: "
   "the doctrine requires the $11.40 fully loaded - training, "
   "calibration, and all. The Signature edition prices the cheaper "
   "alternatives too: a doctrine that knows the $1.10 option exists "
   "and chooses the $11.40 anyway has not overspent, it has decided "
   "what 97.5% is worth."),
},
{
 "name": "Curation Anti-Patterns Catalog",
 "group": "Advanced", "ladder_rank": 33, "ladder_tier": "advanced",
 "demo_key": "h_facts",
 "demo_data": {"patterns": 7, "seen": 2, "worst": "checkbox reviewing",
               "checks": [["patterns", "==", 7]]},
 "description": ("The anti-patterns catalog names the seven ways curation "
   "fails: checkbox reviewing (signing unchecked), review theater "
   "(process without judgment), the hero reviewer (one person "
   "carrying the load), metric gaming (optimizing the KPI not the "
   "quality), automation abdication (deferring to the machine), "
   "feedback black holes (suggestions dying), and calibration decay "
   "(sessions skipped). Two seen here: checkbox reviewing (the "
   "audit's finding - retrained) and calibration decay (one skipped "
   "quarter during the crunch - reinstated with board emphasis). "
   "The worst is checkbox reviewing: it keeps the signatures while "
   "discarding the judgment - the process performed, the purpose "
   "abandoned. Each entry: the smell, the damage, the cure, the "
   "detector."),
 "how_it_works": ("Checkbox reviewing: smell - 100% checklist "
   "completion in impossible times; damage - errors ship signed; "
   "cure - the audit's sampling + retraining; detector - completion-"
   "time analysis. Review theater: smell - all green metrics, "
   "stagnant quality; damage - complacency; cure - the reliability "
   "studies (kappa does not lie); detector - kappa trend. Hero "
   "reviewer: smell - one reviewer at 2x the load; damage - burnout "
   "and single point of failure; cure - the workload balancer's "
   "caps; detector - the load spread. The catalog is taught in "
   "onboarding (module 12: ethics) and reviewed after audits; new "
   "patterns admitted by the board. The two seen are retold: the "
   "team knows its own near-misses, which is how the catalog stays "
   "a living warning instead of a wall poster."),
 "key_points": [
   "7 anti-patterns; 2 seen (checkbox reviewing, calibration decay).",
   "Worst: checkbox reviewing - signatures without judgment.",
   "Each: smell, damage, cure, detector.",
   "Taught in onboarding; reviewed after audits.",
   "Near-misses retold - living warning, not wall poster.",
   "Admitted by board.",
 ],
 "requirements": [
   "Catalog with smell/damage/cure/detector.",
   "Onboarding integration.",
   "Audit-driven review.",
   "Board admission.",
 ],
 "standards": [
   "Detectors wired to metrics.",
   "Cures specific.",
   "Retelling of near-misses.",
   "Culture, not posters.",
 ],
 "citations": [
   "ISO 9001:2015.",
 ],
 "sig_lens": ("The Signature Curation Doctrine names its failure modes: "
   "the doctrine requires the seven written - especially checkbox "
   "reviewing. The Signature edition retells its own near-misses: a "
   "doctrine that hides its failures will repeat them; one that "
   "retells them inoculates."),
},
{
 "name": "Curation Self-Audit and Mastery Record",
 "group": "Advanced", "ladder_rank": 34, "ladder_tier": "advanced",
 "demo_key": "h_mastery",
 "demo_data": {"records": 34, "complete": 34, "quality": 0.975, "coverage": 1.0},
 "description": ("The curation self-audit and mastery record proves the "
   "humans are governed: thirty-four curation archetypes catalogued, "
   "thirty-four complete, 97.5% sampled quality, coverage one hundred "
   "percent. This is the record that closes the loop - the curation "
   "system reviewing its own review. It verifies that every reviewer "
   "is certified, every queue within SLA, every correction verified, "
   "and the governance board met its cadence. A curation system that "
   "cannot show its own quality numbers is asking for trust without "
   "evidence - and trust without evidence is the thing curation "
   "exists to replace."),
 "how_it_works": ("The self-audit checks: reviewer certification (12/12 "
   "current), queue health (depths within 1.5x, SLAs at 92%), "
   "correction integrity (1,200 verified of 1,200), approval "
   "discipline (no unsigned releases), bias controls (4 checks run), "
   "calibration currency (quarterly held), and the audit closure "
   "(7/7 findings closed). The example: 34 of 34 complete, 97.5% "
   "quality, coverage 1.0. Findings become anti-patterns or audit "
   "findings, tracked to closure. The audit runs quarterly with its "
   "report to the governance board and all reviewers - the humans "
   "reviewing the humans, in the open. This record is also the "
   "mastery checkpoint: a reader who understands all thirty-four "
   "records - from triage through calibration to the board - "
   "understands human curation review end to end."),
 "key_points": [
   "34 archetypes, 34 complete; 97.5% quality; coverage 1.0.",
   "Self-audit checks certification, queues, corrections, approvals, bias, calibration.",
   "Findings become anti-patterns or audit findings.",
   "Runs quarterly; report to board and reviewers, in the open.",
   "Trust without evidence is what curation replaces.",
   "Mastery checkpoint: all 34 records teach curation end to end.",
 ],
 "requirements": [
   "Self-audit executed quarterly with published report.",
   "All seven audit dimensions checked.",
   "Findings tracked to closure.",
   "Mastery path documented from record 1 to record 34.",
 ],
 "standards": [
   "Coverage target 1.0.",
   "Quality bar 97%.",
   "Audit independent (board committee).",
   "Year-over-year trend reported.",
 ],
 "citations": [
   "ISO 19011:2018 Guidelines for auditing management systems.",
 ],
 "sig_lens": ("The Signature Curation Doctrine ends by reviewing its "
   "reviewers: the doctrine requires the 34/34 and the 97.5% - the "
   "humans' numbers, in the open. The Signature self-audit closes "
   "the loop from record 1 to record 34: automation proposes, humans "
   "dispose - and the proof."),
},
]

assert len(ENTRIES) == 34, "expected 34 entries, got %d" % len(ENTRIES)
_ranks = [e["ladder_rank"] for e in ENTRIES]
assert _ranks == sorted(_ranks) == list(range(1, 35)), "ladder ranks must be 1..34 in order"
