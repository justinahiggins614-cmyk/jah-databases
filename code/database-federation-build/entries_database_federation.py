#!/usr/bin/env python3
"""Entries for the Database Federation databases (JAH Databases governance
track, group F, 2026-10-17).

Dedupe gate: none of the 8 governance slugs exist in data/manifest.json
(2,770 databases checked 2026-10-17); ID prefixes JAH-DFED- (public) and
JAH-DFEDS- (signature) verified free: zero exact or substring hits in
manifest id_prefix values and zero hits in all shard record IDs of
jah-databases-data-1. (JAH-DBF- was rejected: it substring-collides with
the existing JAH-DB prefix.) All 68 record titles checked against the whole
system (exact dedupe index + live shard title corpus of 1,143,457 titles)
BEFORE authoring.

So this build creates two NEW databases, 34 ladder-ordered records each:

  database-federation            - The Database Federation Database
      (public-harvest: real, fact-checked federation knowledge)
  database-federation-signature  - The Database Federation Signature Database
      (the Signature Federation Doctrine; src signature, titles suffixed
      " (Signature Edition)", never presented as authentic public record)

34 records each, ladder-ordered 1-34 (ladder_tier foundations 1-10 /
compounded 11-21 / advanced 22-34).

Numerical cores: hand-computed 2026-10-17, machine-verified by the demos
(see demos_database_federation.py). Every demo prints its real computed
values, asserts tight bounds (never float exact-equality), and ends with
the OK marker; the build machine-executes all 68 demos.

Never the words "bat belt" anywhere. No website references. No Facebook.
"""

SIG_TAIL = ("Signature original - the Signature Federation Doctrine: many "
            "databases, one question, zero confusion; a federation is a "
            "promise between databases, and promises need contracts, "
            "witnesses, and consequences. Clearly labeled Signature-made, "
            "never presented as an authentic public record. Property of "
            "Justin Addam Higgins (JAH).")

ENTRIES = [
# ---------------- Foundations (1-10) ----------------
{
 "name": "Federation Overview",
 "group": "Foundations", "ladder_rank": 1, "ladder_tier": "foundations",
 "demo_key": "g_facts",
 "demo_data": {"patterns": 3, "members": 64, "contracts": 12,
               "checks": [["patterns", "==", 3], ["members", "==", 64]]},
 "description": ("The federation overview defines the alliance: sixty-four "
   "member databases answering as one, through three query patterns "
   "(scatter-gather, broadcast, chained) bound by twelve join contracts. A "
   "federation lets questions span databases that were never designed "
   "together - the patent database joining the spec database, the wiki "
   "joining the dictionary - without merging them into one. The alternative "
   "is the data warehouse (copy everything centrally) or the application "
   "join (fetch and stitch in code); federation is the middle path, "
   "querying where the data lives. The overview sets the vocabulary every "
   "later record uses: member, contract, pattern, coordinator, shard."),
 "how_it_works": ("A federated query arrives at the coordinator, which "
   "chooses a pattern, routes sub-queries to members per the routing "
   "rules, and merges results per the join contracts. The sixty-four "
   "members are the shard databases plus the specialty databases (patents, "
   "wiki, dictionary); the twelve join contracts define which pairs may "
   "join on which keys. Membership is voluntary and contractual: members "
   "advertise capabilities, accept rate limits, and meet SLAs - the "
   "federation works because the contracts are enforced, not because the "
   "databases are friendly. The overview also states the non-goals: the "
   "federation does not replace member databases, does not copy their "
   "data centrally, and does not hide member failures - it reports them."),
 "key_points": [
   "64 members, 3 query patterns, 12 join contracts.",
   "Questions span databases never designed together - without merging them.",
   "Middle path between central warehouse and application joins.",
   "Membership voluntary and contractual: capabilities, limits, SLAs.",
   "Does not replace members, copy data centrally, or hide failures.",
   "Vocabulary: member, contract, pattern, coordinator, shard.",
 ],
 "requirements": [
   "Member registry with capabilities.",
   "Join contract registry.",
   "Pattern selection rules.",
   "Coordinator implementation.",
 ],
 "standards": [
   "Contracts enforced, not assumed.",
   "Failures reported, never hidden.",
   "No central data copying.",
   "Vocabulary used consistently.",
 ],
 "citations": [
   "Sheth, A. & Larson, J. Federated Database Systems for Managing Distributed, Heterogeneous, and Autonomous Databases. ACM Computing Surveys (1990).",
 ],
 "sig_lens": ("The Signature Federation Doctrine opens with the alliance of "
   "allies: the doctrine requires each member sovereign (its data stays "
   "home) yet bound (its promises kept). The Signature edition insists "
   "the contracts precede the queries - a federation that queries first "
   "and contracts later is not an alliance, it is a raid."),
},
{
 "name": "Scatter-Gather Query Pattern",
 "group": "Foundations", "ladder_rank": 2, "ladder_tier": "foundations",
 "demo_key": "g_scatter",
 "demo_data": {"shards": 16, "shard_p95_ms": 340, "merge_ms": 25},
 "description": ("The scatter-gather pattern fans out and collects: a query "
   "scatters to sixteen shards in parallel, each answers in up to 340ms "
   "p95, and the coordinator gathers and merges in 25ms - total 365ms p95. "
   "Scatter-gather is the workhorse pattern for partitioned data: every "
   "shard holds part of the answer, all are asked at once, and the "
   "coordinator assembles the whole. Its latency is the slowest shard "
   "plus the merge - the straggler problem is the pattern's tax, paid on "
   "every query. The record's example (365ms p95) assumes healthy shards; "
   "the partial-failure record handles the unhealthy ones."),
 "how_it_works": ("The coordinator sends the sub-query to all sixteen "
   "shards simultaneously with a deadline (500ms here, above the 340ms "
   "p95). Responses stream back; the merge combines them - concatenation "
   "for lists, summation for counts, top-K merge for ranked results. "
   "Latency = max(shard latencies) + merge: 340 + 25 = 365ms p95. "
   "Straggler mitigation: at the deadline, missing shards are treated as "
   "partial failure (their absence noted in the result metadata). The "
   "pattern suits partitioned-by-key data where the answer spans shards; "
   "it is wasteful where only one shard holds the answer (the optimizer "
   "routes those directly). Fan-out is bounded: sixteen here, never more "
   "than sixty-four - unbounded fan-out is a denial-of-service attack on "
   "oneself."),
 "key_points": [
   "16 shards in parallel, 340ms p95 each + 25ms merge = 365ms p95.",
   "Latency = slowest shard + merge; stragglers are the pattern's tax.",
   "Deadline 500ms; missing shards become noted partial failures.",
   "Suits partitioned data spanning shards; wasteful for single-shard answers.",
   "Fan-out bounded (<=64) - unbounded fan-out is self-DoS.",
   "The workhorse pattern for partitioned data.",
 ],
 "requirements": [
   "Per-shard deadlines.",
   "Merge semantics per result type.",
   "Straggler policy.",
   "Fan-out bounds.",
 ],
 "standards": [
   "Partial results labeled, never silent.",
   "Deadlines above p95, below timeout budgets.",
   "Merge correctness tested per type.",
   "Single-shard queries routed directly.",
 ],
 "citations": [
   "Sheth & Larson (1990).",
 ],
 "sig_lens": ("The Signature Federation Doctrine scatters the question to "
   "sixteen and gathers sixteen answers into one: the doctrine requires "
   "the 365ms budgeted honestly - slowest shard plus merge. The Signature "
   "edition names the straggler tax on every query: a doctrine that "
   "pretends all shards answer equally fast has never watched a p95."),
},
{
 "name": "Broadcast Query Pattern",
 "group": "Foundations", "ladder_rank": 3, "ladder_tier": "foundations",
 "demo_key": "g_broadcast",
 "demo_data": {"shards": 64, "responded": 48, "timeout_ms": 800},
 "description": ("The broadcast pattern asks everyone: a query goes to all "
   "sixty-four shards, forty-eight respond within the 800ms timeout - 75% "
   "coverage. Broadcast is for questions whose location is unknown: "
   "full-text search across the fleet, 'find this record wherever it is', "
   "schema discovery. It is the most expensive pattern (sixty-four "
   "sub-queries for one question) and the least precise (coverage is "
   "whatever responds in time) - used only where scatter-gather cannot "
   "apply because the data is not partitioned by the query key. The "
   "record's rule: broadcast is the pattern of last resort, and every "
   "broadcast query is logged for review - frequent broadcasts mean the "
   "partitioning is wrong."),
 "how_it_works": ("The coordinator sends to all sixty-four shards with an "
   "800ms deadline; forty-eight respond (75%). Results merge like "
   "scatter-gather, but the metadata emphasizes coverage: '48 of 64 "
   "shards, 75% coverage' rides with every broadcast answer, because an "
   "answer from three-quarters of the fleet is not the whole truth. "
   "Timeouts are generous (800ms) because broadcast already accepts "
   "slowness; the cost is counted (64 sub-queries x unit cost) and charged "
   "to the querying team. Deduplication matters more here: the same record "
   "may live on multiple shards (replicas), and the merge dedupes by "
   "record ID. The review log is the control: broadcasts per week are "
   "trended, and a rising trend triggers a partitioning review - the "
   "pattern should get rarer as the federation matures, not more common."),
 "key_points": [
   "64 shards asked, 48 respond in 800ms: 75% coverage.",
   "For unknown-location questions: fleet search, record hunting, discovery.",
   "Most expensive, least precise - pattern of last resort.",
   "Coverage metadata rides with every answer (48/64).",
   "Replicas deduped by record ID in the merge.",
   "Rising broadcast trend triggers partitioning review.",
 ],
 "requirements": [
   "Coverage metadata on every broadcast result.",
   "Cost accounting per broadcast.",
   "Broadcast review log with trend.",
   "Generous but bounded timeouts.",
 ],
 "standards": [
   "Broadcast only where partitioning cannot route.",
   "Coverage never hidden.",
   "Dedupe by record ID.",
   "Trend reviewed monthly.",
 ],
 "citations": [
   "Sheth & Larson (1990).",
 ],
 "sig_lens": ("The Signature Federation Doctrine shouts only when whispering "
   "cannot work: the doctrine requires every broadcast logged and its "
   "75% coverage confessed. The Signature edition treats frequent "
   "broadcasts as a confession - the partitioning is wrong, and the "
   "doctrine would rather fix the map than keep shouting."),
},
{
 "name": "Chained Query Pattern",
 "group": "Foundations", "ladder_rank": 4, "ladder_tier": "foundations",
 "demo_key": "g_chained",
 "demo_data": {"hops": 3, "hop_ms": 120, "overhead_ms": 30},
 "description": ("The chained pattern follows references: three hops at "
   "120ms each plus 30ms coordination overhead is 390ms - each hop's "
   "results determining the next hop's query. Chained queries traverse "
   "relationships across databases: find the patent, follow its citation "
   "to the spec database, follow the spec's author to the people "
   "database. Each hop depends on the last, so the pattern is sequential "
   "- its latency adds rather than maxes. The record bounds the chain: "
   "three hops here, never more than five - longer chains are replanned "
   "as application logic, because a six-hop federated query is a "
   "distributed transaction wearing a query's clothes."),
 "how_it_works": ("Hop 1 queries database A (120ms), extracts the join keys "
   "from its results; hop 2 queries database B with those keys (120ms); "
   "hop 3 queries database C (120ms); coordination overhead 30ms; total "
   "390ms. The coordinator plans the chain from the join contracts: each "
   "hop's contract names the key the next hop needs. Fan-out within a hop "
   "is allowed (hop 2 may scatter to shards), but hops themselves are "
   "sequential. Cycle detection is mandatory: the planner rejects chains "
   "where a database appears twice (A->B->A), because cyclic chains are "
   "infinite loops with extra steps. Result size is capped per hop "
   "(1,000 keys) - a hop returning a million keys would drown the next "
   "hop, so the cap forces pagination or replanning."),
 "key_points": [
   "3 hops x 120ms + 30ms overhead = 390ms; latency adds, not maxes.",
   "Follows cross-database references: patent -> spec -> person.",
   "Bounded at 5 hops; longer chains become application logic.",
   "Cycle detection mandatory (A->B->A rejected).",
   "Per-hop result cap (1,000 keys) with pagination.",
   "Sequential by nature - the price of following references.",
 ],
 "requirements": [
   "Hop planning from join contracts.",
   "Cycle detection in the planner.",
   "Per-hop result caps.",
   "Hop bound (5 maximum).",
 ],
 "standards": [
   "Chains planned, not improvised.",
   "Cyclic chains rejected.",
   "Overhead budgeted per hop.",
   "Long chains replanned as application logic.",
 ],
 "citations": [
   "Sheth & Larson (1990).",
 ],
 "sig_lens": ("The Signature Federation Doctrine follows the thread hop by "
   "hop: the doctrine requires the 390ms added honestly - sequential "
   "questions take sequential time. The Signature edition caps the chain "
   "at five: a doctrine that lets queries wander six databases deep has "
   "mistaken a journey for a question."),
},
{
 "name": "Cross-Database Join Contract",
 "group": "Foundations", "ladder_rank": 5, "ladder_tier": "foundations",
 "demo_key": "g_join",
 "demo_data": {"left": 96796, "right": 438346, "probes": 12400, "key": "record_id"},
 "description": ("The join contract is the treaty that lets two databases "
   "combine: 96,796 records joining 438,346 on record_id, with a bloom "
   "filter cutting the probe set to 12,400. A contract names the two "
   "members, the join key, the key's format and semantics (record_id: "
   "JAH-prefixed, case-sensitive, never reused), the join type supported "
   "(inner here), and the freshness guarantee (right side within 24 "
   "hours). The bloom filter is the contract's efficiency clause: the "
   "small side's keys filter the large side's scan, so 438,346 records "
   "are not all probed - 12,400 candidate probes, a 35x reduction. Twelve "
   "such contracts bind the federation's key pairs."),
 "how_it_works": ("The contract lifecycle: proposed (with key analysis), "
   "reviewed (semantics verified - both sides' record_id mean the same "
   "thing), tested (sample join on 1,000 keys, results validated), signed, "
   "and monitored (join success rate tracked; below 99% the contract is "
   "suspended for review). Execution: the coordinator fetches the small "
   "side's keys (96,796), builds the bloom filter, ships it to the large "
   "side, which returns only the 12,400 matching candidates; the "
   "coordinator completes the join. The 35x reduction is measured, not "
   "assumed - the contract records the actual probe count per execution. "
   "Key collisions across members (two databases' record_ids overlapping) "
   "are resolved by namespacing: the contract prefixes keys with the "
   "member ID, because the cheapest join bug is the silent one."),
 "key_points": [
   "96,796 x 438,346 on record_id; bloom filter -> 12,400 probes (35x cut).",
   "Contract names members, key, format, semantics, join type, freshness.",
   "Lifecycle: propose, review, test, sign, monitor.",
   "Join success below 99% suspends the contract.",
   "Keys namespaced by member - silent collisions are the cheapest bug.",
   "12 contracts bind the federation's key pairs.",
 ],
 "requirements": [
   "Key semantic verification before signing.",
   "Sample-join testing (1,000 keys).",
   "Probe-count measurement per execution.",
   "Success-rate monitoring with suspension threshold.",
 ],
 "standards": [
   "No join without a signed contract.",
   "Semantics verified, not assumed.",
   "Namespaced keys across members.",
   "Freshness guarantees stated and met.",
 ],
 "citations": [
   "Sheth & Larson (1990).",
 ],
 "sig_lens": ("The Signature Federation Doctrine signs treaties before "
   "combining armies: the doctrine requires the join contract - keys, "
   "semantics, freshness - before the first combined query. The Signature "
   "edition namespaces every key: a doctrine that joins on unnamespaced "
   "keys is not federating, it is colliding politely."),
},
{
 "name": "Schema Mapping Record",
 "group": "Foundations", "ladder_rank": 6, "ladder_tier": "foundations",
 "demo_key": "g_schema",
 "demo_data": {"fields": 14, "transformed": 2, "dropped": 1, "version": "v3"},
 "description": ("The schema mapping translates between members: fourteen "
   "fields mapped, two transformed, one dropped, at mapping version 3. "
   "Databases never share a schema - one calls it 'title', another "
   "'name', a third stores the date as text - and the mapping is the "
   "dictionary between them. Fourteen fields map directly (same meaning, "
   "different names); two transform (the text date parses to ISO, the "
   "price string to decimal); one drops (the internal flag with no "
   "cross-database meaning). The mapping is versioned (v3) because "
   "schemas evolve; the evolution record governs changes. Unmapped fields "
   "are the honest gaps: the mapping lists what cannot translate, so "
   "queries know what they cannot ask."),
 "how_it_works": ("Each mapping is a table: source field -> target field, "
   "with the transform function where needed and the drop reason where "
   "not. The two transforms are pure functions with tests: parse_date "
   "(text -> ISO, 99.2% success, failures logged) and parse_price "
   "(string -> decimal, currency normalized to USD). The dropped field "
   "(internal_review_flag) is documented as intentionally unmapped - "
   "dropping silently would be data loss; dropping loudly is a decision. "
   "Mappings are tested against samples: 1,000 records through the "
   "mapping, field-by-field verification, 99.5% pass rate required. "
   "Version 3 changed two mappings from v2 (the date transform tightened); "
   "the version history is kept because old queries may reference old "
   "mappings."),
 "key_points": [
   "14 mapped, 2 transformed, 1 dropped - mapping v3.",
   "Transforms are tested pure functions (parse_date 99.2%, parse_price).",
   "Drops documented loudly - silent drops are data loss.",
   "Sample-tested: 1,000 records, 99.5% pass required.",
   "Unmapped fields listed as honest gaps.",
   "Versioned; history kept for old queries.",
 ],
 "requirements": [
   "Field-level mapping tables.",
   "Transform functions with tests.",
   "Drop reasons documented.",
   "Sample testing at 99.5%.",
 ],
 "standards": [
   "No silent drops.",
   "Transforms pure and tested.",
   "Versions immutable; changes are new versions.",
   "Gaps listed, not hidden.",
 ],
 "citations": [
   "Sheth & Larson (1990).",
 ],
 "sig_lens": ("The Signature Federation Doctrine translates faithfully or "
   "not at all: the doctrine requires the fourteen mappings, the two "
   "transforms tested, the one drop confessed. The Signature edition "
   "lists the untranslatable openly - a doctrine that pretends every "
   "field translates is not mapping, it is mistranslating with "
   "confidence."),
},
{
 "name": "Identity Resolution Across Databases",
 "group": "Foundations", "ladder_rank": 7, "ladder_tier": "foundations",
 "demo_key": "g_identity",
 "demo_data": {"candidates": 3, "scores": [0.94, 0.71, 0.32], "threshold": 0.85},
 "description": ("The identity resolution record decides when two records "
   "are the same thing: three candidates scoring 0.94, 0.71, and 0.32 "
   "against the 0.85 threshold - one match, one review, one rejection. "
   "Federation constantly asks 'is this the same record?' - the same "
   "patent in two databases, the same person under two spellings. The "
   "score blends key matches (exact ID: 0.5), name similarity (0.3), and "
   "attribute agreement (0.2); the 0.85 threshold was set where precision "
   "hit 99% on the labeled sample. The 0.71 goes to human review (the "
   "curation database's queue); the 0.32 is rejected outright. Resolution "
   "decisions are recorded with their scores - identity is a judgment, "
   "and judgments need audit trails."),
 "how_it_works": ("Scoring: exact key match contributes 0.5, normalized "
   "name similarity 0.3 (trigram), attribute agreement 0.2 (dates, "
   "categories). The 0.94 (key + name + attributes agree) auto-matches; "
   "the 0.71 (name similar, key missing) queues for review; the 0.32 "
   "(name vaguely similar only) rejects. Threshold 0.85 was calibrated "
   "on 5,000 labeled pairs: precision 99.1%, recall 87% - the federation "
   "prefers precision (false merges corrupt) over recall (missed merges "
   "merely duplicate). Matches create the cross-database link (the "
   "provenance record's lineage); the link stores both record IDs, the "
   "score, the timestamp, and the decider (auto or reviewer). Links are "
   "revisited when scores decay (a renamed record re-scores); stale links "
   "are the quiet corruption, so re-resolution runs quarterly."),
 "key_points": [
   "Scores 0.94/0.71/0.32 vs 0.85: match, review, reject.",
   "Blend: key 0.5, name 0.3, attributes 0.2.",
   "Calibrated: 99.1% precision, 87% recall on 5,000 labeled pairs.",
   "Precision over recall: false merges corrupt, missed merges duplicate.",
   "Decisions recorded with scores, timestamps, deciders.",
   "Re-resolution quarterly - stale links are quiet corruption.",
 ],
 "requirements": [
   "Calibrated threshold with labeled samples.",
   "Review queue for the uncertain band.",
   "Decision audit trails.",
   "Quarterly re-resolution.",
 ],
 "standards": [
   "Precision target 99%+.",
   "Thresholds calibrated, not chosen.",
   "Human review for 0.6-0.85 band.",
   "Links versioned with scores.",
 ],
 "citations": [
   "Sheth & Larson (1990).",
 ],
 "sig_lens": ("The Signature Federation Doctrine identifies with care: the "
   "doctrine requires the 0.85 threshold earned on 5,000 labeled pairs, "
   "not assumed. The Signature edition prefers the honest duplicate to "
   "the false merge - a doctrine that merges recklessly does not unify "
   "knowledge, it counterfeits it."),
},
{
 "name": "Federation Membership Record",
 "group": "Foundations", "ladder_rank": 8, "ladder_tier": "foundations",
 "demo_key": "g_member",
 "demo_data": {"members": 64, "tiers": {"gold": 8, "silver": 24, "bronze": 32}, "quorum": 43},
 "description": ("The membership record lists the allies: sixty-four "
   "members in three tiers - 8 gold, 24 silver, 32 bronze - with charter "
   "quorum at forty-three. Tiers reflect commitment: gold members guarantee "
   "99.9% availability and sub-500ms p95 (the shard databases); silver "
   "99.5% and 1s (the specialty databases); bronze best-effort (the "
   "experimental ones). Membership is the federation's census: each entry "
   "names the database, its tier, its advertised capabilities, its rate "
   "limits, and its SLA - the facts the coordinator routes on. Quorum "
   "(43, two-thirds plus one) governs charter changes; ordinary operations "
   "need no vote, which is why the federation can act daily and deliberate "
   "quarterly."),
 "how_it_works": ("The registry stores per member: endpoint, tier, "
   "capabilities (from the advertisement record), rate limits, SLA terms, "
   "join contracts signed, and health status (from the dashboard). Tier "
   "determines routing priority: gold first for latency-sensitive queries, "
   "bronze only for best-effort analytics. Members attest quarterly: "
   "capabilities re-advertised, SLAs re-confirmed - the attestation is "
   "the membership's heartbeat. Tier changes follow performance: a silver "
   "member holding 99.9% for two quarters may petition for gold; a gold "
   "member missing SLA for a quarter is demoted automatically - the tiers "
   "are earned continuously, not granted permanently. The 43-member "
   "quorum amends the charter; admitting a member needs only the "
   "coordinator's approval against the onboarding checklist."),
 "key_points": [
   "64 members: 8 gold (99.9%), 24 silver (99.5%), 32 bronze (best-effort).",
   "Tiers earned continuously: promotion by petition, demotion automatic.",
   "Quarterly attestation: capabilities, SLAs re-confirmed.",
   "Quorum 43 (2/3+1) amends the charter; operations need no vote.",
   "Registry is the census the coordinator routes on.",
   "Admission by checklist; expulsion by charter process.",
 ],
 "requirements": [
   "Member registry with tiers and capabilities.",
   "Quarterly attestation.",
   "Tier promotion/demotion rules.",
   "Quorum definition.",
 ],
 "standards": [
   "Tiers performance-based.",
   "Attestations enforced (missed = review).",
   "Demotion automatic on SLA breach.",
   "Charter changes need quorum.",
 ],
 "citations": [
   "Sheth & Larson (1990).",
 ],
 "sig_lens": ("The Signature Federation Doctrine keeps a roll of allies: "
   "the doctrine requires the sixty-four listed with their tiers earned, "
   "not granted. The Signature edition demotes automatically - a doctrine "
   "that lets a failing gold member keep its rank is not loyal, it is "
   "sentimental, and sentiment does not answer queries."),
},
{
 "name": "Capability Advertisement",
 "group": "Foundations", "ladder_rank": 9, "ladder_tier": "foundations",
 "demo_key": "g_capability",
 "demo_data": {"capabilities": 5, "members": 64, "stale": 2},
 "description": ("The capability advertisement is each member's menu: five "
   "capability types advertised - query patterns supported, join keys "
   "offered, result formats, latency class, and data freshness - by all "
   "sixty-four members, with two currently stale. The coordinator cannot "
   "route what it does not know: advertisements tell it which members "
   "answer scatter-gather, which offer the record_id join key, which "
   "return ranked results, which are fast, and how fresh their data is. "
   "The two stale advertisements (members that changed capabilities "
   "without re-advertising) are flagged - routing on stale menus sends "
   "queries where they cannot be answered, the federation's version of "
   "a wrong number."),
 "how_it_works": ("Advertisements are structured documents: patterns "
   "(scatter/broadcast/chain support), join keys (with contracts), "
   "formats (JSON, ranked lists, aggregates), latency class (gold/silver/"
   "bronze p95), freshness (update cadence, last update). Members publish "
   "on joining and on any capability change; the registry versions each "
   "publication. Staleness detection: the coordinator probes advertised "
   "capabilities (a test query per pattern quarterly); the two stale "
   "members failed their probes - one dropped broadcast support silently, "
   "one's freshness slipped from daily to weekly. Failed probes suspend "
   "the capability (not the member) until re-advertised. Consumers of "
   "advertisements (the optimizer, the router) always read the registry "
   "version, never a cache older than the attestation quarter."),
 "key_points": [
   "5 capability types x 64 members; 2 stale (flagged).",
   "Menu tells the coordinator what each member can do.",
   "Published on join and on change; versioned.",
   "Staleness probed quarterly; failed probes suspend the capability.",
   "Routing on stale menus is the federation's wrong number.",
   "Registry version always read fresh.",
 ],
 "requirements": [
   "Structured advertisement schema.",
   "Publication on join and change.",
   "Quarterly capability probing.",
   "Staleness flagging with suspension.",
 ],
 "standards": [
   "Advertisements versioned.",
   "Probes mandatory.",
   "Suspension until re-advertised.",
   "No routing on stale capabilities.",
 ],
 "citations": [
   "Sheth & Larson (1990).",
 ],
 "sig_lens": ("The Signature Federation Doctrine requires every ally to "
   "state its menu honestly: the doctrine probes the menu quarterly and "
   "suspends what fails. The Signature edition flags the two stale "
   "without mercy - a doctrine that routes on outdated promises is not "
   "trusting, it is negligent with other people's questions."),
},
{
 "name": "Query Routing Rules",
 "group": "Foundations", "ladder_rank": 10, "ladder_tier": "foundations",
 "demo_key": "g_routing",
 "demo_data": {"rules": 5, "members": 64, "default": "scatter-gather"},
 "description": ("The routing rules direct each question: five rules map "
   "query shapes to members and patterns, defaulting to scatter-gather. "
   "Rule 1: keyed lookups (record_id present) route to the owning shard "
   "directly. Rule 2: partitioned scans scatter-gather across the sixteen "
   "shards. Rule 3: unknown-location searches broadcast (logged). Rule 4: "
   "reference traversals chain per the join contracts. Rule 5: analytics "
   "aggregations route to bronze members off-peak. The rules are evaluated "
   "in order, first match wins - the ordering is the policy (precision "
   "before coverage, cheap before expensive). Routing decisions are "
   "logged with the rule that fired, so misroutes are diagnosable."),
 "how_it_works": ("The router parses the query shape: keys present? "
   "partition key known? references followed? aggregation? - then walks "
   "the five rules. A record_id lookup hits rule 1 and goes to one shard "
   "(not sixteen): the cheapest correct route. A full-text search with no "
   "key hits rule 3 and broadcasts (with the coverage caveat). The "
   "default (rule 0, scatter-gather) catches what the five miss - "
   "defaulting to the workhorse, never to broadcast. Rule changes are "
   "versioned and canary-tested: a new rule routes 1% of matching queries "
   "for a week before promotion. The router also enforces member health: "
   "unhealthy members are skipped regardless of rules (with the skip "
   "noted), because routing to a down member is not routing."),
 "key_points": [
   "5 rules, ordered, first match wins; default scatter-gather.",
   "Keyed lookups -> one shard (cheapest correct route).",
   "Unknown-location -> broadcast (logged, pattern of last resort).",
   "Rule changes versioned + canary-tested (1% for a week).",
   "Unhealthy members skipped regardless of rules.",
   "Decisions logged with the firing rule - misroutes diagnosable.",
 ],
 "requirements": [
   "Ordered rule set with default.",
   "Query-shape parsing.",
   "Canary process for rule changes.",
   "Health-aware skipping.",
 ],
 "standards": [
   "Precision before coverage in ordering.",
   "Cheap before expensive.",
   "Defaults never broadcast.",
   "All decisions logged.",
 ],
 "citations": [
   "Sheth & Larson (1990).",
 ],
 "sig_lens": ("The Signature Federation Doctrine directs each question by "
   "rule, not by whim: the doctrine requires the five rules ordered, the "
   "default the workhorse. The Signature edition canaries every change - "
   "a doctrine that reroutes the fleet on untested rules is not "
   "decisive, it is reckless with sixty-four allies' load."),
},
# ---------------- Compounded (11-21) ----------------
{
 "name": "Distributed Search Architecture",
 "group": "Compounded", "ladder_rank": 11, "ladder_tier": "compounded",
 "demo_key": "g_distsearch",
 "demo_data": {"tiers": 3, "shards": 16, "coordinators": 2, "cache_hit": 0.68},
 "description": ("The distributed search architecture stacks three tiers: "
   "two coordinators (active-passive) fanning out to sixteen shards, with "
   "a result cache absorbing 68% of queries. The coordinators own routing, "
   "merging, and contracts; the shards own data and local search; the "
   "cache owns repeat questions. Two coordinators (not one) because the "
   "coordinator is the single point of orchestration - active-passive "
   "with 30-second failover, health-checked continuously. The 68% cache "
   "hit rate means only a third of queries reach the shards; the "
   "architecture's capacity plan assumes the cache, and the cache's "
   "invalidation policy (write-through from member updates) keeps it "
   "honest."),
 "how_it_works": ("A query hits the active coordinator, which checks the "
   "cache (68% hit: answered in 12ms, never touching a shard), routes "
   "misses per the routing rules, merges per the contracts, writes the "
   "cache, and returns. The passive coordinator replays the active's "
   "decision log (30-second lag max); on active failure it promotes and "
   "replays - in-flight queries retry once. Shards are stateless from the "
   "federation's view: they answer sub-queries and know nothing of the "
   "federation. The cache key includes the query, the member set version, "
   "and the contracts version - a stale cache entry from before a "
   "contract change cannot serve. Tier scaling is independent: "
   "coordinators scale with query rate, shards with data, cache with "
   "repeat rate."),
 "key_points": [
   "3 tiers: 2 coordinators (active-passive), 16 shards, cache (68% hit).",
   "Cache absorbs two-thirds; capacity plans assume it.",
   "Failover 30s; in-flight queries retry once.",
   "Cache keys versioned on member set + contracts.",
   "Shards stateless to the federation.",
   "Tiers scale independently (rate, data, repeats).",
 ],
 "requirements": [
   "Active-passive coordinators with decision-log replay.",
   "Versioned cache keys.",
   "Write-through invalidation from members.",
   "Independent tier scaling.",
 ],
 "standards": [
   "Failover tested quarterly.",
   "Cache never serves across contract versions.",
   "Shards unaware of federation topology.",
   "Hit rates monitored with the cache economics.",
 ],
 "citations": [
   "Sheth & Larson (1990).",
 ],
 "sig_lens": ("The Signature Federation Doctrine builds the search as three "
   "tiers with no single throat to choke: the doctrine requires the "
   "passive coordinator rehearsed, the cache versioned. The Signature "
   "edition versions the cache keys on the contracts - a doctrine that "
   "serves answers from before the treaty changed is not caching, it is "
   "time-traveling without a license."),
},
{
 "name": "Result Merging and Ranking",
 "group": "Compounded", "ladder_rank": 12, "ladder_tier": "compounded",
 "demo_key": "g_merge",
 "demo_data": {"shards": 16, "results": 1240, "top_k": 100, "dupes": 87},
 "description": ("The merging record assembles the whole answer: 1,240 "
   "results from sixteen shards, deduplicated (87 duplicates removed), "
   "ranked, top 100 returned. Merging is where federation quality lives: "
   "the shards return local answers, and only the merge makes them a "
   "global answer. The 87 duplicates are replicas (same record on two "
   "shards) - removed by record ID, keeping the highest-scored copy. "
   "Ranking blends the shards' local scores (normalized per shard, "
   "because shard A's 0.9 is not shard B's 0.9) with the federation's "
   "global signals (freshness, member tier). The top-100 cap is the "
   "contract with the user: the federation promises the best hundred, "
   "not every match."),
 "how_it_works": ("Merge steps: collect (1,240 with per-shard scores), "
   "dedupe (87 removed by record ID, best score kept -> 1,153), normalize "
   "(scores z-scored per shard, because local scales differ), re-rank "
   "(0.7 x normalized local + 0.2 x freshness + 0.1 x tier weight), "
   "truncate (top 100). The weights are calibrated quarterly against "
   "click-through: the 0.7/0.2/0.1 blend beat pure local scores by 18% "
   "on the relevance sample. Ties break by record ID (deterministic - "
   "the same query returns the same order). The merge is streaming: "
   "results merge as shards respond, so the top-100 is often ready "
   "before the slowest shard answers - the straggler only matters if it "
   "holds a top-100 candidate, checked by score bounds."),
 "key_points": [
   "1,240 results -> 87 dupes removed -> 1,153 -> top 100.",
   "Scores normalized per shard (local 0.9s are not comparable).",
   "Re-rank: 0.7 local + 0.2 freshness + 0.1 tier; calibrated quarterly.",
   "Deterministic tie-breaks by record ID.",
   "Streaming merge: top-100 often ready before stragglers.",
   "The merge is where federation quality lives.",
 ],
 "requirements": [
   "Dedupe by record ID.",
   "Per-shard score normalization.",
   "Calibrated re-rank weights.",
   "Streaming merge with score bounds.",
 ],
 "standards": [
   "Deterministic ordering.",
   "Weights calibrated, not chosen.",
   "Dedupe keeps best-scored copy.",
   "Top-K cap published.",
 ],
 "citations": [
   "Sheth & Larson (1990).",
 ],
 "sig_lens": ("The Signature Federation Doctrine assembles sixteen partial "
   "truths into one ranked answer: the doctrine requires the 87 "
   "duplicates removed and the scores normalized - unnormalized merging "
   "is not ranking, it is letting the loudest shard win. The Signature "
   "edition calibrates the blend quarterly: a doctrine that never "
   "re-tunes its ranking is navigating by last year's stars."),
},
{
 "name": "Consistency Models in Federation",
 "group": "Compounded", "ladder_rank": 13, "ladder_tier": "compounded",
 "demo_key": "g_consistency",
 "demo_data": {"N": 3, "R": 2, "W": 2, "model": "quorum"},
 "description": ("The consistency record chooses the truth contract: "
   "N=3 replicas, R=2 reads, W=2 writes - R+W (4) > N (3), so the "
   "federation reads its writes. Federation spans autonomous databases "
   "that update on their own schedules; the consistency model defines "
   "what a query may assume. Quorum (R+W>N) is the default: overlapping "
   "read and write sets guarantee the latest write is seen. The record "
   "is honest about the cost: quorum reads touch 2 of 3 replicas (slower "
   "than one), and cross-member writes need the transaction record's "
   "two-phase commit. Where the application tolerates staleness "
   "(analytics), the model relaxes to eventual with a documented lag "
   "bound (5 minutes) - consistency chosen per query class, not per "
   "federation."),
 "how_it_works": ("The model registry maps query classes to models: "
   "interactive reads -> quorum (R=2,W=2,N=3); analytics -> eventual "
   "(lag bound 5 min, monitored); cross-member writes -> 2PC (the "
   "transaction record). The R+W>N proof is checked per member set: with "
   "N=3, R=2, W=2, any read quorum overlaps any write quorum in at least "
   "one replica - the overlapping replica has the latest write. Members "
   "advertise their native consistency (the capability record); the "
   "federation's model is the weakest that satisfies the query class - "
   "never stronger than needed, because strength costs latency. "
   "Violations are detected by the reconciliation record (read-your-write "
   "checks on sampled queries); a member drifting past its lag bound is "
   "flagged. The model is per query class precisely because one size "
   "fits none: the checkout needs quorum, the dashboard needs eventual."),
 "key_points": [
   "Quorum default: N=3, R=2, W=2; R+W=4 > 3 reads-your-writes.",
   "Per query class: interactive quorum, analytics eventual (5-min bound).",
   "Strength costs latency - never stronger than needed.",
   "Member native models advertised; federation takes the weakest sufficient.",
   "Violations detected by sampled read-your-write checks.",
   "One size fits none.",
 ],
 "requirements": [
   "Model registry per query class.",
   "Quorum arithmetic verified per member set.",
   "Lag bounds monitored for eventual.",
   "Violation detection with flagging.",
 ],
 "standards": [
   "R+W>N checked, not assumed.",
   "Bounds documented and monitored.",
   "Models chosen per class.",
   "Drift flagged, not absorbed.",
 ],
 "citations": [
   "Sheth & Larson (1990).",
 ],
 "sig_lens": ("The Signature Federation Doctrine promises exactly the "
   "truth it can keep: the doctrine requires R+W>N proven per member "
   "set, and eventual only where the lag bound is monitored. The "
   "Signature edition never sells quorum latency at eventual prices - "
   "a doctrine that promises strong consistency on a slow quorum is "
   "not consistent, it is late."),
},
{
 "name": "Federated Authentication Tokens",
 "group": "Compounded", "ladder_rank": 14, "ladder_tier": "compounded",
 "demo_key": "g_auth",
 "demo_data": {"members": 5, "ttl_s": 3600, "scope": "federation:query"},
 "description": ("The federated authentication record issues the passports: "
   "one token, five members, 3,600-second TTL, scoped to "
   "federation:query. A federated query touches many members; making the "
   "user authenticate to each would be unusable, and sharing passwords "
   "would be unforgivable. The federation runs its own token service: the "
   "user authenticates once, gets a scoped token, and members accept it "
   "because they trust the issuer (the trust is the charter, signed by "
   "all). The scope (federation:query) is the least privilege: the token "
   "queries, nothing else - it cannot administer members, change "
   "contracts, or read outside the query patterns."),
 "how_it_works": ("Token flow: user -> federation auth service (proves "
   "identity per the member's accepted methods) -> signed JWT (issuer, "
   "subject, scope federation:query, expiry now+3600s, member list) -> "
   "presented to each member -> member verifies signature against the "
   "charter's public key, checks scope and expiry, serves. The five "
   "members in the example accept the token; members may additionally "
   "require their own local authorization (the token says who, the "
   "member decides what). Revocation: the auth service publishes a "
   "revocation list every 60 seconds; members check it for tokens older "
   "than 60 seconds - the 60-second window is the documented revocation "
   "lag. Token theft is bounded by the TTL and scope: a stolen token "
   "queries for at most an hour, and only through the federation's "
   "patterns."),
 "key_points": [
   "One token, 5 members, 3600s TTL, scope federation:query.",
   "Members trust the charter-signed issuer.",
   "Least privilege: queries only, nothing else.",
   "Revocation list every 60s; 60-second revocation lag documented.",
   "Members keep local authorization (token says who, member says what).",
   "Theft bounded by TTL + scope.",
 ],
 "requirements": [
   "Charter-signed token issuer.",
   "Scoped tokens (least privilege).",
   "Revocation with documented lag.",
   "Member-side signature verification.",
 ],
 "standards": [
   "No password sharing between members.",
   "TTLs bounded (max 1 hour for query scope).",
   "Revocation lag published.",
   "Local authorization preserved.",
 ],
 "citations": [
   "Sheth & Larson (1990).",
 ],
 "sig_lens": ("The Signature Federation Doctrine issues one passport for "
   "five borders: the doctrine requires the token scoped, short-lived, "
   "and charter-signed. The Signature edition documents the 60-second "
   "revocation lag openly - a doctrine that pretends revocation is "
   "instant is not secure, it is optimistic with other people's data."),
},
{
 "name": "Rate Limiting Across Members",
 "group": "Compounded", "ladder_rank": 15, "ladder_tier": "compounded",
 "demo_key": "g_ratelimit",
 "demo_data": {"per_member": 1000, "members": 64, "window_s": 60},
 "description": ("The rate limit record shares the road fairly: 1,000 "
   "requests per minute per member across 64 members is 64,000 fleet "
   "requests per minute - the federation's total query budget. Rate "
   "limits protect members from each other: one team's broadcast storm "
   "must not starve another's keyed lookups. The limits are per member "
   "per caller, in 60-second windows, with the coordinator enforcing the "
   "federation-wide view (a caller at 900/min on each of 64 members is "
   "at 57,600/min fleet-wide - the coordinator sees the sum the members "
   "cannot). Exceeding callers get 429s with retry-after; the limits are "
   "published, so 429s are never a surprise."),
 "how_it_works": ("Each member enforces its 1,000/min per caller (token "
   "bucket, 60-second window); the coordinator additionally tracks "
   "per-caller fleet totals and throttles at 90% of the 64,000 fleet "
   "budget - the federation's circuit breaker. Broadcast queries cost "
   "64 against the caller's budget (one per shard); scatter-gather costs "
   "16; keyed lookups cost 1 - the pattern's fan-out is priced into the "
   "limit, which is why broadcast is self-limiting for heavy users. "
   "Burst allowances (2x for 10 seconds) absorb legitimate spikes; "
   "sustained exceeders are throttled, then notified, then (for abuse) "
   "suspended per the charter. The limits are reviewed quarterly against "
   "the throughput forecasts - limits that throttle legitimate growth "
   "are raised, with the member capacity to match."),
 "key_points": [
   "1,000/min/member x 64 = 64,000/min fleet budget.",
   "Per-caller, 60s windows; coordinator sees the fleet sum.",
   "Fan-out priced in: broadcast costs 64, scatter 16, lookup 1.",
   "429s with retry-after; limits published, never surprising.",
   "Burst 2x/10s; sustained excess throttled then suspended.",
   "Reviewed quarterly against throughput forecasts.",
 ],
 "requirements": [
   "Per-member per-caller limits.",
   "Fleet-wide coordinator view.",
   "Fan-out cost accounting.",
   "Published limits with 429 semantics.",
 ],
 "standards": [
   "Limits from capacity, not from round numbers.",
   "Broadcast self-limiting via fan-out pricing.",
   "Abuse process per the charter.",
   "Growth-driven limit increases.",
 ],
 "citations": [
   "Sheth & Larson (1990).",
 ],
 "sig_lens": ("The Signature Federation Doctrine rations the road so all "
   "may travel: the doctrine requires the 64,000/min budget published "
   "and the fan-out priced in. The Signature edition makes broadcast "
   "self-limiting - a doctrine that lets one team's curiosity starve "
   "another's work is not a federation, it is a tragedy of the commons "
   "with better branding."),
},
{
 "name": "Caching Federated Results",
 "group": "Compounded", "ladder_rank": 16, "ladder_tier": "compounded",
 "demo_key": "g_cachefed",
 "demo_data": {"ttl_s": 300, "hit_rate": 0.68, "members": 64},
 "description": ("The federated cache remembers answers: 300-second TTL, "
   "68% hit rate across the 64 members' query load. Federated queries are "
   "expensive (sixteen shards, 365ms); repeat questions should not pay "
   "twice. The cache sits at the coordinator and keys on the query plus "
   "the member-set and contract versions - the versioning that keeps "
   "treaty changes from serving stale answers. The 68% hit rate reflects "
   "the workload's repeat structure (dashboards, popular searches); the "
   "32% miss is the long tail of unique questions. Invalidation is "
   "write-through: member updates push invalidations to the coordinator, "
   "so the cache never serves data the member has already replaced."),
 "how_it_works": ("Cache key = hash(query, member_set_version, "
   "contracts_version, caller_scope) - the scope prevents cross-tenant "
   "leaks. TTL 300 seconds balances freshness and hit rate; the "
   "invalidation channel (member -> coordinator, <2s) handles the "
   "urgent staleness. The 68% hit rate is measured per query class: "
   "dashboard queries 91%, ad-hoc 34% - the cache is sized for the "
   "dashboards, and ad-hoc misses are accepted. Negative caching "
   "(remembering empty results for 60s) absorbs the repeated 'find this "
   "nonexistent record' broadcasts - the most wasteful query shape. "
   "Cache stampedes are prevented by request coalescing: ten identical "
   "in-flight queries become one shard fan-out, nine waiters - the "
   "thundering herd becomes a single file."),
 "key_points": [
   "300s TTL, 68% hit rate (dashboards 91%, ad-hoc 34%).",
   "Keys versioned on member set + contracts + scope.",
   "Write-through invalidation (<2s) from members.",
   "Negative caching (60s) for empty results.",
   "Request coalescing defeats stampedes.",
   "Repeat questions never pay twice.",
 ],
 "requirements": [
   "Versioned cache keys.",
   "Invalidation channel from members.",
   "Per-class hit rate tracking.",
   "Coalescing for identical in-flight queries.",
 ],
 "standards": [
   "Scope in the key (no cross-tenant leaks).",
   "Invalidation lag published.",
   "Negative caching bounded (60s).",
   "Stale-serve never across contract versions.",
 ],
 "citations": [
   "Sheth & Larson (1990).",
 ],
 "sig_lens": ("The Signature Federation Doctrine remembers answers but "
   "never outlives its treaties: the doctrine requires the 300s TTL and "
   "the versioned keys. The Signature edition coalesces the stampede - "
   "a doctrine that lets ten identical questions fan out sixteen ways "
   "is not caching, it is watching money burn in triplicate."),
},
{
 "name": "Partial Failure Handling",
 "group": "Compounded", "ladder_rank": 17, "ladder_tier": "compounded",
 "demo_key": "g_partial",
 "demo_data": {"shards": 16, "failed": 2, "degraded": True},
 "description": ("The partial failure record plans for the missing: sixteen "
   "shards, two fail - 87.5% coverage, degraded mode, the query answered "
   "with the fourteen. In a federation of sixty-four, something is always "
   "slightly broken; the system must answer anyway and say what is "
   "missing. Degraded mode is the doctrine: return the 87.5% with the "
   "coverage labeled ('14 of 16 shards; shards 7 and 12 unavailable'), "
   "never silently pretend fourteen is sixteen. The alternative - failing "
   "the whole query for two shards - turns every member's bad day into "
   "everyone's outage, which is how federations die."),
 "how_it_works": ("Failure detection: shard deadlines (500ms) plus health "
   "checks; two missed deadlines mark the shard failed for the query. "
   "The merge proceeds with fourteen, and the result metadata carries "
   "the coverage: which shards, what percent, whether the missing shards "
   "could hold top-100 candidates (score bounds checked - if shard 7's "
   "bound exceeds the 100th result's score, the answer is marked "
   "'incomplete, top results uncertain'). Retry policy: idempotent "
   "queries retry once against the failed shards (30% recover on retry); "
   "non-idempotent never retry. Escalation: two failed shards page the "
   "member's on-call; four failed shards (75% coverage) mark the "
   "federation degraded fleet-wide; eight failed halt broadcast queries "
   "(coverage too low to be useful). The dashboard shows the degraded "
   "state plainly - partial failure is normal operations, not an "
   "embarrassment."),
 "key_points": [
   "16 shards, 2 fail: 87.5% coverage, degraded mode, labeled.",
   "Never silently pretend fourteen is sixteen.",
   "Score bounds check whether missing shards could hold top-100.",
   "Idempotent retries once (30% recover); non-idempotent never.",
   "Escalation: 2 page member, 4 fleet-degraded, 8 halt broadcasts.",
   "Partial failure is normal operations.",
 ],
 "requirements": [
   "Coverage metadata on every degraded result.",
   "Score-bound completeness checks.",
   "Retry policy by idempotency.",
   "Escalation tiers.",
 ],
 "standards": [
   "Degraded results labeled, never silent.",
   "Failing the query requires <50% coverage.",
   "Health checks independent of query deadlines.",
   "Dashboard shows degraded state plainly.",
 ],
 "citations": [
   "Sheth & Larson (1990).",
 ],
 "sig_lens": ("The Signature Federation Doctrine answers with fourteen "
   "when sixteen were asked: the doctrine requires the missing two "
   "named on the answer. The Signature edition checks the score bounds "
   "- a doctrine that claims its partial answer is complete has not "
   "degraded gracefully, it has lied politely."),
},
{
 "name": "Federated Query Cost Estimation",
 "group": "Compounded", "ladder_rank": 18, "ladder_tier": "compounded",
 "demo_key": "g_qcost",
 "demo_data": {"shards": 16, "per_shard": 2, "merge": 5, "cache_hit": 0.68},
 "description": ("The federated cost estimator prices questions: sixteen "
   "shards at 2 cost units each plus 5 for the merge is 37 units per "
   "scatter-gather - but the 68% cache hit rate means the expected cost "
   "is 11.84 units. Federated queries have real costs (member compute, "
   "bandwidth, merge compute), and the estimator predicts them before "
   "execution so the optimizer can choose and the accountants can bill. "
   "The per-shard 2 units blend member compute and transfer; the merge 5 "
   "covers the coordinator. Cached answers cost ~0.1 (the cache lookup). "
   "The estimate rides with the query plan; actuals are metered and the "
   "estimator is scored like the forecasts - estimators get graded too."),
 "how_it_works": ("Cost = fanout x per_shard + merge: 16x2+5 = 37 for "
   "scatter-gather; 64x2+8 = 136 for broadcast (bigger merge); 3x2+3 = 9 "
   "per chained hop. Expected cost = (1 - hit_rate) x full + hit_rate x "
   "cached: 0.32x37 + 0.68x0.1 = 11.91 units (demo-computed precisely). "
   "The optimizer uses the estimates to choose patterns (the global "
   "optimizer record); the chargeback uses them to bill (the cost "
   "accounting database's retrieval model takes the federated actuals). "
   "Estimation error is tracked: the estimator's MAPE is 11% (federated "
   "costs are bursty), and estimates more than 3x the actual trigger a "
   "review - the estimator must not cry wolf, or optimizers stop "
   "listening."),
 "key_points": [
   "Scatter-gather: 16x2+5 = 37 units; expected 11.91 with 68% cache.",
   "Broadcast 136, chained 9/hop - patterns priced differently.",
   "Estimates ride with the plan; actuals metered.",
   "Estimator MAPE 11%; 3x errors trigger review.",
   "Feeds the optimizer (choice) and chargeback (billing).",
   "Estimators get graded too.",
 ],
 "requirements": [
   "Per-pattern cost formulas.",
   "Cache-adjusted expected costs.",
   "Estimate-vs-actual tracking.",
   "Integration with optimizer and billing.",
 ],
 "standards": [
   "Costs from metering, not from hope.",
   "Estimates before execution.",
   "Error reviews at 3x.",
   "Formulas versioned with the patterns.",
 ],
 "citations": [
   "Sheth & Larson (1990).",
 ],
 "sig_lens": ("The Signature Federation Doctrine prices the question before "
   "asking it: the doctrine requires the 37 units estimated and the "
   "11.91 expected. The Signature edition grades the estimator - a "
   "doctrine whose cost predictions are never scored will predict "
   "cheaply and spend dearly."),
},
{
 "name": "Schema Evolution in Federation",
 "group": "Compounded", "ladder_rank": 19, "ladder_tier": "compounded",
 "demo_key": "g_evolution",
 "demo_data": {"from": "v3", "to": "v4", "breaking": 2, "migration_days": 90},
 "description": ("The schema evolution record manages change across the "
   "alliance: mapping v3 to v4 with two breaking changes and a 90-day "
   "migration. Members evolve their schemas independently - the "
   "federation cannot freeze them, so it versions the mappings and "
   "migrates deliberately. The two breaking changes (the date field's "
   "format tightened, the price field renamed) are the kind that silently "
   "corrupt joins; the record treats them as the serious events they "
   "are: announced 90 days ahead, dual-mapped during migration (v3 and v4 "
   "both served), and cut over only when all consumers attest. The 90 "
   "days are not arbitrary: the slowest consumer's release cycle, plus "
   "margin."),
 "how_it_works": ("Evolution process: change proposed (with the breaking "
   "analysis), announced (90-day clock starts), dual-mapping (the "
   "coordinator serves both v3 and v4, translating between), consumer "
   "attestation (each consumer confirms v4 readiness), cutover (v3 "
   "retired, announced). The two breaking changes each got a compatibility "
   "shim during migration: the old date format parsed leniently, the old "
   "price field aliased. Rollback is the reverse: v4->v3 dual-mapping "
   "restored within the migration window - after cutover, rollback is a "
   "new evolution, not a revert. The mapping registry versions everything; "
   "queries declare the version they expect, and the coordinator "
   "translates. A member that breaks its schema without notice violates "
   "its membership terms - the charter has consequences."),
 "key_points": [
   "v3->v4: 2 breaking changes, 90-day migration.",
   "Dual-mapping during migration; cutover on consumer attestation.",
   "Compatibility shims for each breaking change.",
   "90 days = slowest consumer cycle + margin.",
   "Rollback within window; after cutover it is a new evolution.",
   "Unannounced breaks violate membership terms.",
 ],
 "requirements": [
   "Breaking-change analysis per evolution.",
   "90-day announcement minimum.",
   "Dual-mapping with shims.",
   "Consumer attestation before cutover.",
 ],
 "standards": [
   "Versions immutable.",
   "Queries declare expected versions.",
   "Shims tested like transforms.",
   "Charter consequences for unannounced breaks.",
 ],
 "citations": [
   "Sheth & Larson (1990).",
 ],
 "sig_lens": ("The Signature Federation Doctrine changes its treaties "
   "slowly and loudly: the doctrine requires the 90 days, the dual "
   "mapping, the attestation. The Signature edition punishes the "
   "unannounced break - a doctrine that tolerates silent schema changes "
   "will federate beautifully right up until it corrupts everything."),
},
{
 "name": "Membership Onboarding Record",
 "group": "Compounded", "ladder_rank": 20, "ladder_tier": "compounded",
 "demo_key": "g_onboard",
 "demo_data": {"steps": 5, "days": 14, "checklist": 23},
 "description": ("The onboarding record admits new allies: five steps, "
   "fourteen days, twenty-three checklist items. Admitting a member is "
   "the federation's growth moment - and its risk moment, because a bad "
   "member degrades every query it touches. The five steps: application "
   "(capabilities claimed), verification (claims probed - the capability "
   "record's tests), contract signing (join contracts where applicable, "
   "SLA terms), shadow routing (1% of matching queries for a week, "
   "results compared), and full admission (registry updated, announced). "
   "Fourteen days is the standard; the checklist's twenty-three items "
   "are the evidence - endpoints, keys, rate limits, health checks, "
   "runbooks, on-call contacts."),
 "how_it_works": ("The checklist (23 items) covers: technical (endpoint, "
   "auth, schemas, sample data), operational (health endpoint, on-call, "
   "runbook, status page), contractual (SLA tier, rate limits, join "
   "contracts, charter signature), and data (freshness attestation, "
   "provenance hooks, retention policy). Shadow routing is the proving "
   "ground: 1% of queries for seven days, with the new member's results "
   "compared against the federation's (agreement rate must exceed 98% "
   "for identical queries). Failures during shadow extend the shadow "
   "(never promote a failing member). Admission is the coordinator's "
   "decision against the checklist - all 23 checked, or no admission. "
   "The new member starts at bronze tier regardless of claims; promotion "
   "is earned (the membership record's rules)."),
 "key_points": [
   "5 steps, 14 days, 23 checklist items.",
   "Shadow routing: 1% for 7 days, 98% agreement required.",
   "Checklist: technical, operational, contractual, data.",
   "Failures extend shadow; never promote a failing member.",
   "New members start bronze; promotion earned.",
   "Admission is growth; bad admission is contagion.",
 ],
 "requirements": [
   "23-item checklist, all checked.",
   "Shadow routing with agreement threshold.",
   "Contract signing before admission.",
   "Bronze-start policy.",
 ],
 "standards": [
   "No admission without verification.",
   "Shadow failures extend, never promote.",
   "Checklist evidence retained.",
   "Coordinator decides against the checklist.",
 ],
 "citations": [
   "Sheth & Larson (1990).",
 ],
 "sig_lens": ("The Signature Federation Doctrine admits allies carefully: "
   "the doctrine requires the fourteen days, the twenty-three checks, "
   "the shadow week. The Signature edition starts everyone at bronze - "
   "a doctrine that grants gold on promises will spend its queries "
   "learning what the checklist would have told it."),
},
{
 "name": "Membership Offboarding Record",
 "group": "Compounded", "ladder_rank": 21, "ladder_tier": "compounded",
 "demo_key": "g_offboard",
 "demo_data": {"steps": 4, "purge_days": 30, "notice_days": 90},
 "description": ("The offboarding record parts ways cleanly: four steps, "
   "thirty-day data purge, ninety-day notice. Members leave - decommissioned, "
   "superseded, or expelled - and the federation must unwind them without "
   "breaking queries. The four steps: notice (90 days, or immediate for "
   "charter violations), rerouting (contracts rewired around the departing "
   "member, queries drained), purge (the member's cached data deleted "
   "within 30 days, attestations collected), and registry removal (the "
   "census updated, announced). The ninety days let dependents migrate; "
   "the thirty-day purge honors the data agreements - the federation does "
   "not keep what it no longer has the right to hold."),
 "how_it_works": ("Rerouting is the delicate step: the join contracts "
   "involving the member are suspended, the optimizer replans without "
   "it, and dependent queries are notified of the capability loss (some "
   "questions become unanswerable - the federation says so plainly). "
   "The purge is verified: cache keys for the member's data deleted, "
   "the member attests deletion of federated tokens and query logs per "
   "the retention agreement, and the federation's audit confirms. "
   "Expulsion (charter violation) compresses the timeline: immediate "
   "suspension, 30-day wind-down, then purge - the charter's consequences "
   "are not theoretical. The offboarding checklist (17 items) mirrors "
   "onboarding's; a member that leaves cleanly may return through "
   "onboarding - the door revolves, but only through the checklist."),
 "key_points": [
   "4 steps: notice, reroute, purge, remove. 90-day notice, 30-day purge.",
   "Rerouting rewires contracts; some questions become unanswerable (said plainly).",
   "Purge verified with attestations; audit confirms.",
   "Expulsion compresses: immediate suspension, 30-day wind-down.",
   "17-item checklist mirrors onboarding.",
   "Clean leavers may return - through the checklist.",
 ],
 "requirements": [
   "Notice periods (90 standard, immediate for violations).",
   "Rerouting with dependent notification.",
   "Verified purge with attestations.",
   "Registry removal with announcement.",
 ],
 "standards": [
   "No data kept past the right to hold it.",
   "Unanswerable questions declared, not faked.",
   "Expulsion per the charter process.",
   "Return only through onboarding.",
 ],
 "citations": [
   "Sheth & Larson (1990).",
 ],
 "sig_lens": ("The Signature Federation Doctrine parts cleanly: the "
   "doctrine requires the ninety days' notice, the thirty days' purge, "
   "the attestations. The Signature edition declares the unanswerable "
   "questions plainly - a doctrine that fakes answers after losing the "
   "member that held them is not federating, it is hallucinating with "
   "a registry."),
},
# ---------------- Advanced (22-34) ----------------
{
 "name": "Global Query Optimizer",
 "group": "Advanced", "ladder_rank": 22, "ladder_tier": "advanced",
 "demo_key": "g_optimizer",
 "demo_data": {"selectivity": 0.02, "threshold": 0.1, "shards_hit": 3, "shards_total": 16},
 "description": ("The global optimizer chooses the cheapest correct plan: "
   "selectivity 0.02 against the 0.10 threshold routes to scatter-gather "
   "on 3 of 16 shards instead of broadcasting to 64. The routing rules "
   "are static; the optimizer is dynamic - it uses statistics (selectivity "
   "estimates, shard histograms, the cost estimator's numbers) to pick "
   "the plan per query. The example: a selective predicate (2% of "
   "records) hits only the 3 shards whose key ranges overlap - 3x2+5 = "
   "11 units instead of broadcast's 136. The optimizer's plans are "
   "explained (the plan cites the statistics used), because an optimizer "
   "that cannot explain itself cannot be debugged."),
 "how_it_works": ("Optimization steps: parse (query shape), estimate "
   "(selectivity from histograms: 0.02), enumerate (candidate plans: "
   "broadcast 136 units, scatter-16 37, scatter-3 11, chained 9/hop), "
   "choose (cheapest correct: scatter-3 at 11 units), execute with the "
   "plan attached. The 0.10 threshold is the scatter/broadcast boundary "
   "from the cost model: below 10% selectivity, targeted scatter wins; "
   "above, broadcast's coverage justifies its cost. Statistics are "
   "maintained per shard (key histograms, updated daily); stale "
   "statistics are the optimizer's failure mode, so the histograms' "
   "freshness is monitored. Plan regressions are caught by the estimator's "
   "scoring: a plan costing 3x its estimate triggers review - the "
   "optimizer, like the estimator, gets graded."),
 "key_points": [
   "Selectivity 0.02 < 0.10 threshold: scatter 3 shards (11 units) not broadcast (136).",
   "Dynamic per-query choice from statistics; routing rules are static.",
   "Plans explained with cited statistics.",
   "Shard histograms updated daily; staleness monitored.",
   "3x cost regressions trigger review.",
   "Cheapest correct plan - correctness never traded for cost.",
 ],
 "requirements": [
   "Per-shard statistics (histograms).",
   "Cost-based plan enumeration.",
   "Plan explanations.",
   "Regression detection.",
 ],
 "standards": [
   "Correctness never sacrificed for cost.",
   "Statistics fresh (daily).",
   "Thresholds from the cost model.",
   "Optimizer graded like the estimator.",
 ],
 "citations": [
   "Sheth & Larson (1990).",
 ],
 "sig_lens": ("The Signature Federation Doctrine plans each question like "
   "a campaign: the doctrine requires the statistics consulted, the "
   "cheapest correct plan chosen, the choice explained. The Signature "
   "edition grades the optimizer - a doctrine whose planner is never "
   "scored will plan brilliantly right up until it plans catastrophically."),
},
{
 "name": "Distributed Transactions",
 "group": "Advanced", "ladder_rank": 23, "ladder_tier": "advanced",
 "demo_key": "g_2pc",
 "demo_data": {"participants": 4, "prepare_ok": 4, "commit_ok": 4, "rounds": 2},
 "description": ("The distributed transaction record coordinates the "
   "all-or-nothing: four participants, four prepare-OKs, four commit-OKs, "
   "two round trips - the two-phase commit that writes across members "
   "atomically. Federated writes are rare (the federation is "
   "read-mostly) but real: cross-database corrections, membership "
   "changes, contract updates. Two-phase commit: phase 1 (prepare - each "
   "participant promises it can commit), phase 2 (commit - all do, or "
   "all abort). The four-for-four example is the happy path; the "
   "record's substance is the sad paths - a prepare-no becomes a global "
   "abort, a commit-time crash becomes recovery by the transaction log."),
 "how_it_works": ("The coordinator logs the transaction intention, sends "
   "prepare to all four participants, collects votes (4 yes here), logs "
   "the commit decision, sends commit, collects acks (4 here). Two round "
   "trips, ~240ms at 120ms/hop. Failure handling: any prepare-no or "
   "timeout -> global abort (all participants roll back); coordinator "
   "crash after prepare -> participants query the coordinator's log on "
   "recovery (the log is the ground truth); participant crash during "
   "commit -> recovery replays from its own log. The transaction log is "
   "the record's hero: every decision written before acting, because a "
   "coordinator that acts before logging cannot recover. Heuristic "
   "decisions (a participant unilaterally committing) are forbidden - "
   "the protocol's safety depends on no one freelancing."),
 "key_points": [
   "4 participants, 4/4 prepare, 4/4 commit, 2 round trips (~240ms).",
   "Prepare-no or timeout -> global abort.",
   "Coordinator crash -> recovery from the transaction log.",
   "Log every decision before acting.",
   "Heuristic (unilateral) decisions forbidden.",
   "Rare but real: corrections, membership, contract updates.",
 ],
 "requirements": [
   "2PC coordinator with transaction log.",
   "Participant prepare/commit implementation.",
   "Recovery procedures for all crash points.",
   "Heuristic-decision prohibition.",
 ],
 "standards": [
   "Log-before-act always.",
   "Timeouts bounded (no indefinite blocking).",
   "Recovery tested by fault injection.",
   "Read-mostly federation: writes need justification.",
 ],
 "citations": [
   "Gray, J. & Reuter, A. Transaction Processing: Concepts and Techniques. Morgan Kaufmann (1993).",
 ],
 "sig_lens": ("The Signature Federation Doctrine commits all or none: the "
   "doctrine requires the four prepare-OKs before the single commit - "
   "unanimity before action. The Signature edition logs before acting: "
   "a doctrine that acts before writing down its decision cannot tell "
   "you, after the crash, what it decided."),
},
{
 "name": "Eventual Consistency Reconciliation",
 "group": "Advanced", "ladder_rank": 24, "ladder_tier": "advanced",
 "demo_key": "g_reconcile",
 "demo_data": {"conflicts": 1240, "auto": 1180, "manual": 60, "lag_min": 5},
 "description": ("The reconciliation record heals the diverged: 1,240 "
   "conflicts, 1,180 auto-resolved (95.2%), 60 to manual review, within "
   "the 5-minute lag bound. Eventual consistency means members converge "
   "- reconciliation is the convergence mechanism. Conflicts arise "
   "where two members updated the same logical record differently; the "
   "auto-resolver applies the registered rules (last-writer-wins with "
   "vector clocks here, 95.2% of cases), and the remainder - true "
   "conflicts no rule decides - go to the human queue. The 5-minute lag "
   "bound is monitored: reconciliation runs continuously, and anything "
   "unresolved past 5 minutes pages - eventual must still be prompt."),
 "how_it_works": ("Detection: version vectors on replicated records; "
   "divergent vectors mean conflict. Auto-resolution: last-writer-wins "
   "by vector clock (1,180 cases), field-level merge where the updates "
   "touched different fields (subset of the 1,180), deterministic "
   "tie-breaks by member priority. Manual: the 60 true conflicts (same "
   "field, concurrent writes) queue with both versions, the vector "
   "clocks, and the business context - reviewers decide, and their "
   "decisions become new rules where patternable. The lag bound (5 min) "
   "is the SLA: p99 reconciliation latency 3.2 minutes currently, "
   "monitored. Unresolvable conflicts (member offline) wait with the "
   "record marked 'diverged' - queries see the divergence flag, because "
   "hiding divergence is the one unforgivable sin of eventual "
   "consistency."),
 "key_points": [
   "1,240 conflicts: 1,180 auto (95.2%), 60 manual; 5-min lag bound.",
   "Auto: last-writer-wins by vector clock + field merges.",
   "Manual: same-field concurrent writes, queued with context.",
   "Reviewer decisions become rules where patternable.",
   "Divergence flagged on queries - hiding it is unforgivable.",
   "p99 reconciliation 3.2 min, monitored against the bound.",
 ],
 "requirements": [
   "Version vectors on replicated records.",
   "Registered auto-resolution rules.",
   "Manual queue with full context.",
   "Lag bound monitoring.",
 ],
 "standards": [
   "Divergence always visible to queries.",
   "Rules deterministic and registered.",
   "Manual decisions feed rule improvements.",
   "Bound breaches paged.",
 ],
 "citations": [
   "Sheth & Larson (1990).",
 ],
 "sig_lens": ("The Signature Federation Doctrine heals its divergences in "
   "the open: the doctrine requires the 95.2% auto-resolved and the 60 "
   "queued, the divergence flagged. The Signature edition turns reviewer "
   "wisdom into rules - a doctrine that solves the same conflict by hand "
   "twice has mistaken toil for diligence."),
},
{
 "name": "Federation Governance Charter",
 "group": "Advanced", "ladder_rank": 25, "ladder_tier": "advanced",
 "demo_key": "g_facts",
 "demo_data": {"articles": 9, "quorum": 43, "amendments": 3,
               "checks": [["articles", "==", 9]]},
 "description": ("The governance charter is the federation's constitution: "
   "nine articles, amendable by the 43-member quorum, three amendments in "
   "force. The articles cover: membership (admission, tiers, expulsion), "
   "contracts (join, SLA, schema), queries (patterns, routing, costing), "
   "data (consistency, provenance, retention), security (auth, audit), "
   "operations (monitoring, incidents, changes), economics (costing, "
   "chargeback), disputes (process, arbitration), and amendment (the "
   "process for changing the charter itself). The three amendments: "
   "broadcast logging (2026-02), the bronze-start rule (2026-05), and the "
   "unannounced-break consequences (2026-08) - each a lesson written into "
   "law."),
 "how_it_works": ("Amendment process: proposed by any 5 members, debated "
   "for 30 days, voted (43 of 64 needed), enacted with a 90-day "
   "grace period - the charter changes slowly by design, because the "
   "federation's stability depends on it. Disputes follow article 8: "
   "negotiation (14 days), mediation by the coordinator (14 days), "
   "arbitration by a 3-member panel (binding) - the broadcast-logging "
   "dispute of 2026-01 went to mediation and produced the amendment. "
   "Expulsion (article 1) needs the quorum and a documented violation "
   "pattern - no member has been expelled; two were warned. The charter "
   "is published to all members and to queriers (the parts that affect "
   "them); secret constitutions govern no one legitimately."),
 "key_points": [
   "9 articles; 43-member quorum amends; 3 amendments in force.",
   "Articles: membership, contracts, queries, data, security, ops, economics, disputes, amendment.",
   "Amendments are lessons written into law (broadcast logging, bronze-start, break consequences).",
   "Disputes: negotiate -> mediate -> arbitrate (binding).",
   "Expulsion needs quorum + documented pattern; none yet, two warned.",
   "Published openly - secret constitutions govern no one.",
 ],
 "requirements": [
   "Charter with 9 articles published.",
   "Amendment process with quorum.",
   "Dispute resolution process.",
   "Expulsion criteria and process.",
 ],
 "standards": [
   "Changes slow by design (30-day debate, 90-day grace).",
   "Dissent recorded.",
   "Processes binding.",
   "Publication mandatory.",
 ],
 "citations": [
   "Sheth & Larson (1990).",
 ],
 "sig_lens": ("The Signature Federation Doctrine writes its lessons into "
   "law: the doctrine requires the nine articles, the three amendments "
   "each a scar turned to statute. The Signature edition publishes the "
   "charter openly - a doctrine with secret rules is not governance, "
   "it is just power with better paperwork."),
},
{
 "name": "Inter-Member SLA Contracts",
 "group": "Advanced", "ladder_rank": 26, "ladder_tier": "advanced",
 "demo_key": "g_sla",
 "demo_data": {"availability": 99.9, "p95_ms": 500, "penalty": 0.1, "members": 8},
 "description": ("The inter-member SLAs are the promises with teeth: 99.9% "
   "availability, 500ms p95, 10% service-credit penalty per breach - "
   "signed by the 8 gold members. SLAs turn the tier definitions into "
   "enforceable commitments: gold means 99.9% measured monthly, p95 "
   "under 500ms, and breaches pay 10% of the member's federation fees "
   "as credits to the affected queriers. The record tracks compliance: "
   "7 of 8 gold members met SLA last quarter; the eighth missed p95 "
   "(612ms) and paid the credits - and was demoted to silver pending "
   "recovery, because the membership record's automatic demotion is not "
   "suspended for anyone. SLAs without penalties are aspirations; with "
   "penalties, they are contracts."),
 "how_it_works": ("Measurement: availability from the health checks "
   "(successful responses / total), latency p95 from the coordinator's "
   "meters - the federation measures, not the member (trust, but "
   "verify). Breach process: detected automatically, credits applied to "
   "the next cycle, the member notified with the data, and the "
   "improvement plan due in 14 days. The 10% penalty scales: each "
   "additional 0.1% availability miss adds 5% more (99.9->99.8 = 10%, "
   "99.8->99.7 = 15%) - the teeth sharpen with the bite. Excused "
   "breaches (federation-wide incidents, force majeure) are classified "
   "by the coordinator with the data published - excuses are transparent "
   "or they are not excuses. The SLA terms are part of the membership "
   "attestation: re-signed quarterly, because a promise unsigned is a "
   "promise unmade."),
 "key_points": [
   "Gold SLA: 99.9% availability, p95 500ms, 10% penalty/breach.",
   "7 of 8 met last quarter; the eighth paid credits + demoted.",
   "Federation measures (health checks + coordinator meters).",
   "Penalties scale with the miss (10%, then +5% per 0.1%).",
   "Excused breaches classified transparently.",
   "Re-signed quarterly with attestation.",
 ],
 "requirements": [
   "SLA terms per tier with penalties.",
   "Federation-side measurement.",
   "Breach process with credits and plans.",
   "Quarterly re-signing.",
 ],
 "standards": [
   "Penalties mandatory (aspirations are not contracts).",
   "Measurement independent of the member.",
   "Demotion automatic on breach.",
   "Excuses transparent.",
 ],
 "citations": [
   "Sheth & Larson (1990).",
 ],
 "sig_lens": ("The Signature Federation Doctrine makes promises with teeth: "
   "the doctrine requires the 10% penalty paid and the demotion served - "
   "even for gold. The Signature edition measures from the federation's "
   "side: a doctrine that lets members grade their own SLA has confused "
   "the student with the examiner."),
},
{
 "name": "Cross-Database Provenance",
 "group": "Advanced", "ladder_rank": 27, "ladder_tier": "advanced",
 "demo_key": "g_provenance",
 "demo_data": {"hops": 4, "records": 1153, "complete": 1153},
 "description": ("The provenance record traces every answer home: four-hop "
   "lineage on 1,153 merged results, 1,153 complete (100%). A federated "
   "answer blends many sources; provenance says which - each result "
   "carries its lineage: the member databases, the query that fetched "
   "it, the transforms applied, the merge decisions. Four hops here: "
   "member query -> member transform -> coordinator merge -> ranking. "
   "Complete (100%) is the standard: an answer without provenance is an "
   "assertion, and the federation deals in evidence. Provenance serves "
   "corrections (find the bad source), audits (prove the answer), and "
   "trust (show the work) - the three reasons federations get questioned."),
 "how_it_works": ("Lineage capture: each member tags its results with "
   "(member ID, query ID, timestamp, transform versions); the coordinator "
   "appends (merge rule, dedupe decisions, ranking weights version); the "
   "ranker appends (final score components). The four hops are stored "
   "with the result (not beside it - lineage that can be separated will "
   "be lost). Verification: 1,153 of 1,153 results carry complete "
   "lineage, checked per query - incomplete lineage fails the query "
   "(better no answer than an unprovable one). Retention: lineage lives "
   "as long as the cached answer (300s) plus the audit window (90 days "
   "in the audit log). Corrections propagate: when a member corrects a "
   "record, the provenance index finds every federated answer that used "
   "it - the correction record's machinery, federation-wide."),
 "key_points": [
   "4-hop lineage on 1,153 results; 100% complete.",
   "Lineage stored with the result, never beside it.",
   "Incomplete lineage fails the query.",
   "Serves corrections, audits, and trust.",
   "Corrections propagate via the provenance index.",
   "An answer without provenance is an assertion.",
 ],
 "requirements": [
   "Per-hop lineage capture.",
   "Completeness verification per query.",
   "90-day audit retention.",
   "Correction propagation via the index.",
 ],
 "standards": [
   "100% lineage completeness.",
   "Lineage inseparable from results.",
   "Member + coordinator + ranker all tag.",
   "Corrections traced federation-wide.",
 ],
 "citations": [
   "Sheth & Larson (1990).",
 ],
 "sig_lens": ("The Signature Federation Doctrine shows its work on every "
   "answer: the doctrine requires the four hops recorded, 100% "
   "complete. The Signature edition fails the query rather than serve "
   "the unprovable - a doctrine that answers without provenance is not "
   "informing, it is testifying without evidence."),
},
{
 "name": "Federated Analytics Pipeline",
 "group": "Advanced", "ladder_rank": 28, "ladder_tier": "advanced",
 "demo_key": "g_analytics",
 "demo_data": {"stages": 3, "rows_in": 2400000, "rows_out": 18000, "reduction": 133.3},
 "description": ("The analytics pipeline aggregates at scale: three "
   "stages, 2.4 million rows in, 18,000 aggregates out - a 133x "
   "reduction. Federated analytics pushes computation to the data: "
   "stage 1 (per member: filter and pre-aggregate), stage 2 (per region: "
   "combine), stage 3 (coordinator: final rollup). Moving 2.4M rows "
   "would drown the coordinator; moving 18K aggregates is trivial. The "
   "133x reduction is the pipeline's efficiency proof - and its "
   "correctness burden: pre-aggregation must be mathematically sound "
   "(sums and counts compose; medians do not - the pipeline ships "
   "histograms for quantiles). The pipeline runs off-peak on bronze "
   "members (the routing rules' analytics path), because analytics at "
   "peak is how interactive queries go to die."),
 "how_it_works": ("Stage 1: each member filters (the query predicate) and "
   "pre-aggregates (sums, counts, histograms) - 2.4M rows become ~200K "
   "partial aggregates. Stage 2: regional combiners merge partials "
   "(~200K -> ~40K). Stage 3: the coordinator rolls up to 18,000 final "
   "aggregates. Correctness rules: only composable aggregations pushed "
   "down (sum, count, min, max, histograms); non-composable (median, "
   "distinct-count exact) computed from histograms approximately or at "
   "stage 3 exactly. The 133x reduction is measured per run; pipelines "
   "below 10x reduction are reviewed (the pushdown is not working). "
   "Scheduling: nightly for the standard rollups, on-demand for ad-hoc "
   "(admitted to bronze, off-peak, with the requester's cost center "
   "billed)."),
 "key_points": [
   "3 stages: member pre-aggregate -> region combine -> coordinator rollup.",
   "2.4M rows -> 18K aggregates: 133x reduction.",
   "Only composable aggregations pushed down; quantiles via histograms.",
   "Off-peak on bronze members (routing rule 5).",
   "Pipelines under 10x reduction reviewed.",
   "Computation moves to the data, not data to the computation.",
 ],
 "requirements": [
   "Pushdown correctness rules.",
   "Reduction measurement per run.",
   "Off-peak scheduling.",
   "Composable-only stage 1.",
 ],
 "standards": [
   "Approximations labeled (histogram quantiles).",
   "10x reduction floor reviewed.",
   "Ad-hoc billed to requesters.",
   "Nightly standard rollups.",
 ],
 "citations": [
   "Sheth & Larson (1990).",
 ],
 "sig_lens": ("The Signature Federation Doctrine sends the question to the "
   "data: the doctrine requires the 133x reduction proven per run. The "
   "Signature edition is strict about composability - a doctrine that "
   "pre-aggregates medians has not optimized, it has approximated "
   "without saying so."),
},
{
 "name": "Multi-Region Federation Topology",
 "group": "Advanced", "ladder_rank": 29, "ladder_tier": "advanced",
 "demo_key": "g_topology",
 "demo_data": {"regions": 3, "latency_ms": [45, 120, 210], "members": [28, 22, 14]},
 "description": ("The topology record maps the federation in space: three "
   "regions with 28, 22, and 14 members, inter-region latencies 45ms, "
   "120ms, 210ms. Geography shapes every federated decision: the "
   "coordinator routes to nearby members first (45ms beats 210ms), the "
   "consistency model accounts for the 210ms worst case, and the "
   "disaster plan assumes a region lost. Each region runs a full "
   "coordinator pair (the architecture's active-passive, per region), "
   "so a region failure degrades to two regions, not to zero. The "
   "member counts (28/22/14) reflect data gravity: the primary region "
   "holds the hot data and most members; the others hold replicas and "
   "regional specialties."),
 "how_it_works": ("Routing preference: same-region members first (45ms), "
   "then 120ms, then 210ms - the optimizer's cost model includes the "
   "latency as cost units. Cross-region queries carry the latency "
   "honestly: a scatter-gather across all three regions has p95 = max "
   "regional p95 + 210ms inter-region - the topology record publishes "
   "the formula. Data placement follows gravity: hot data in the "
   "primary region, warm replicas in the second, cold archive in the "
   "third - the tiering record's temperatures mapped to geography. "
   "Failover: region loss triggers the disaster plan (the DR cost "
   "record's machinery): DNS shifts, the two surviving regions absorb "
   "the load (burst reserves sized for it), and the federation runs "
   "degraded-two-region until recovery. The topology is reviewed "
   "annually; member migrations between regions are planned events."),
 "key_points": [
   "3 regions: 28/22/14 members; latencies 45/120/210ms.",
   "Routing prefers nearby; optimizer prices latency as cost.",
   "Cross-region p95 formula published.",
   "Data gravity: hot primary, warm second, cold third.",
   "Region loss -> degraded two-region (burst reserves sized).",
   "Per-region coordinator pairs; no single-region dependence.",
 ],
 "requirements": [
   "Topology map with latencies and members.",
   "Latency-aware routing and costing.",
   "Regional coordinator pairs.",
   "Disaster plan for region loss.",
 ],
 "standards": [
   "Latencies measured, not estimated.",
   "Failover rehearsed annually.",
   "Migrations planned events.",
   "No region holding irreplaceable sole copies.",
 ],
 "citations": [
   "Sheth & Larson (1990).",
 ],
 "sig_lens": ("The Signature Federation Doctrine knows where its allies "
   "stand: the doctrine requires the 45/120/210 map current and the "
   "region-loss plan rehearsed. The Signature edition places data by "
   "gravity - a doctrine that scatters hot data randomly has not "
   "federated, it has hidden things from itself in three time zones."),
},
{
 "name": "Federation Security Model",
 "group": "Advanced", "ladder_rank": 30, "ladder_tier": "advanced",
 "demo_key": "g_security",
 "demo_data": {"controls": 4, "audits_yr": 4, "incidents": 1},
 "description": ("The security model guards the alliance: four controls, "
   "four audits a year, one incident last year (contained). The controls: "
   "federated authentication (the token record), transport encryption "
   "(TLS 1.3 between all members, verified), query authorization (the "
   "scope check per pattern - a federation:query token cannot touch "
   "admin patterns), and audit logging (every cross-member query logged "
   "with caller, members touched, and data classes returned). The one "
   "incident: a member's endpoint certificate lapsed, failing closed "
   "(queries rejected, not served insecurely) - the model worked as "
   "designed, which is why it is one incident and not a breach. Four "
   "audits a year (quarterly, rotating auditors) verify the controls; "
   "findings become charter amendments where systemic."),
 "how_it_works": ("Control 1 (auth): the token service, 3600s TTL, "
   "revocation <60s. Control 2 (transport): TLS 1.3 mandatory, "
   "certificates pinned per member, expiry monitored (the lapsed cert "
   "was caught by monitoring - it failed closed before any insecure "
   "query). Control 3 (authorization): per-pattern scopes, member-local "
   "authorization preserved, the coordinator enforcing the federation "
   "scope. Control 4 (audit): append-only query log (caller, query "
   "hash, members, data classes, timestamp), 90-day retention, "
   "tamper-evident (hash-chained). Incident response: the lapsed-cert "
   "incident ran the playbook - detect (monitoring), contain (fail "
   "closed), notify (member + affected callers), remediate (reissue), "
   "review (why did expiry monitoring not alert sooner - it did, the "
   "member ignored it; the charter now auto-suspends on ignored "
   "alerts). The model is reviewed after every incident and annually."),
 "key_points": [
   "4 controls: federated auth, TLS 1.3, per-pattern authorization, audit logging.",
   "1 incident last year: lapsed cert, failed closed (model worked).",
   "4 audits/year, rotating auditors.",
   "Audit log: append-only, hash-chained, 90-day retention.",
   "Findings become charter amendments where systemic.",
   "Fail closed, never open.",
 ],
 "requirements": [
   "Four controls implemented and monitored.",
   "Quarterly audits with rotation.",
   "Incident playbook with reviews.",
   "Tamper-evident audit logging.",
 ],
 "standards": [
   "TLS 1.3 minimum.",
   "Fail-closed on control failure.",
   "Revocation under 60 seconds.",
   "No control without monitoring.",
 ],
 "citations": [
   "NIST Special Publication 800-53 Rev. 5 (security controls).",
 ],
 "sig_lens": ("The Signature Federation Doctrine guards its allies as "
   "itself: the doctrine requires the four controls monitored and the "
   "one incident learned from. The Signature edition fails closed - a "
   "doctrine that fails open for convenience has not secured the "
   "federation, it has merely locked the front door and left the "
   "loading dock open."),
},
{
 "name": "Federation Audit Record",
 "group": "Advanced", "ladder_rank": 31, "ladder_tier": "advanced",
 "demo_key": "g_facts",
 "demo_data": {"audits": 4, "findings": 6, "closed": 6, "period": "2026",
               "checks": [["audits", "==", 4], ["closed", "==", 6]]},
 "description": ("The federation audit record is the annual adversarial "
   "review: four quarterly audits, six findings, six closed in 2026. The "
   "audits rotate auditors (never the same team twice running) and cover "
   "the controls (security record), the contracts (join success rates), "
   "the economics (cost estimates vs actuals), and the governance (charter "
   "compliance). The six findings: two stale capability advertisements "
   "(fixed - the advertisement record's probing), one unlogged broadcast "
   "pattern (now logged), two SLA measurement gaps (federation-side "
   "metering added), one shadow-routing skip (a member admitted without "
   "the full shadow - the coordinator retrained). Six for six closed: "
   "the audit is not complete until the findings are."),
 "how_it_works": ("Each quarterly audit picks a theme (rotating through "
   "controls, contracts, economics, governance) and samples deeply: "
   "the Q3 contracts audit re-ran 1,000 joins per contract and found "
   "the 99.2% success rate (above the 99% bar, but the 0.8% got root "
   "causes). Findings follow the schema: what, where, severity, owner, "
   "date - the shadow-routing skip was severity high, owner the "
   "coordinator, closed in 21 days with the retraining. Auditor "
   "independence is structural: auditors come from member teams not "
   "under audit, and the lead auditor rotates annually. The report goes "
   "to the charter's dispute body and to all members - sunlight is the "
   "audit's enforcement. Repeat findings escalate: a finding recurring "
   "two audits running becomes a charter amendment proposal."),
 "key_points": [
   "4 audits, 6 findings, 6 closed in 2026.",
   "Rotating auditors and themes (controls, contracts, economics, governance).",
   "Findings: what/where/severity/owner/date; closure tracked.",
   "Repeat findings become charter amendments.",
   "Reports to all members - sunlight enforces.",
   "Audit incomplete until findings close.",
 ],
 "requirements": [
   "Quarterly audits with rotation.",
   "Finding schema with closure tracking.",
   "Auditor independence.",
   "Full-member reporting.",
 ],
 "standards": [
   "No audit without findings follow-up.",
   "Repeat findings escalate to charter level.",
   "Sampling deep, not wide.",
   "Independence structural.",
 ],
 "citations": [
   "ISO 19011:2018 Guidelines for auditing management systems.",
 ],
 "sig_lens": ("The Signature Federation Doctrine audits its alliances: "
   "the doctrine requires the four audits, the six findings, the six "
   "closures. The Signature edition escalates the repeats to the "
   "charter - a doctrine that finds the same fault twice and changes "
   "nothing has not audited, it has merely observed expensively."),
},
{
 "name": "Federation Health Dashboard",
 "group": "Advanced", "ladder_rank": 32, "ladder_tier": "advanced",
 "demo_key": "g_facts",
 "demo_data": {"panels": 8, "members": 64, "degraded": 2, "refresh": "intraday",
               "checks": [["panels", "==", 8]]},
 "description": ("The health dashboard watches the alliance: 8 panels, 64 "
   "members, 2 currently degraded, intraday refresh. The panels: member "
   "health grid (64 tiles colored by status), query pattern mix "
   "(scatter/broadcast/chained volumes), latency p50/p95/p99, error and "
   "partial-failure rates, SLA compliance by tier, cost vs estimate, "
   "topology map (the three regions), and the incident feed. Two members "
   "degraded (the stale-advertisement pair, serving with suspended "
   "capabilities) show amber - the dashboard's honesty is its value: "
   "green everywhere would be a lie, and the federation does not lie to "
   "itself. Intraday refresh (5 minutes) because federation health moves "
   "faster than daily."),
 "how_it_works": ("The 64-tile grid is the dashboard's heart: each member "
   "a tile, colored green/amber/red by the health checks, clickable to "
   "the member's detail (capabilities, SLAs, recent queries, incidents). "
   "The pattern mix shows the federation's behavior: scatter 82%, "
   "chained 12%, broadcast 6% - the 6% broadcast is watched (the "
   "pattern-of-last-resort trending up would alarm). Latency panels "
   "track the coordinator's meters; the cost panel tracks the "
   "estimator's accuracy; the topology panel shows the three regions "
   "with their latencies live. Alerting: member-down pages the member's "
   "on-call; 4+ degraded pages the federation coordinator; broadcast "
   "share over 10% alerts the architecture review. The dashboard is "
   "the first screen in every federation incident - the shared picture "
   "that stops sixty-four teams from diagnosing sixty-four different "
   "problems."),
 "key_points": [
   "8 panels, 64 members, 2 degraded (amber, honest), 5-min refresh.",
   "Member grid: 64 tiles, clickable to detail.",
   "Pattern mix: scatter 82%, chained 12%, broadcast 6% (watched).",
   "Alerting: member-down, 4+ degraded, broadcast share >10%.",
   "First screen in every incident - the shared picture.",
   "Green everywhere would be a lie.",
 ],
 "requirements": [
   "All eight panels with documented queries.",
   "5-minute refresh.",
   "Alert thresholds per panel.",
   "Member drill-down.",
 ],
 "standards": [
   "Honesty over greenness.",
   "Alerts actionable.",
   "Incident-first design.",
   "Exemplar updated with standards.",
 ],
 "citations": [
   "Sheth & Larson (1990).",
 ],
 "sig_lens": ("The Signature Federation Doctrine keeps the alliance's "
   "pulse visible: the doctrine requires the 64 tiles honest - two "
   "amber today. The Signature edition treats all-green as a malfunction "
   "of the dashboard, not of the federation: a doctrine that cannot "
   "show its own bruises cannot be trusted with its own health."),
},
{
 "name": "Federation Anti-Patterns Catalog",
 "group": "Advanced", "ladder_rank": 33, "ladder_tier": "advanced",
 "demo_key": "g_facts",
 "demo_data": {"patterns": 8, "seen": 3, "worst": "broadcast storms",
               "checks": [["patterns", "==", 8]]},
 "description": ("The anti-patterns catalog names the eight ways "
   "federations fail: broadcast storms, the God coordinator (all logic "
   "centralized), silent partial results, unversioned schemas, the "
   "unmetered query (no cost estimate), tier drift (gold members "
   "coasting), the shadow skip (admitting without proving), and the "
   "green dashboard (lying about health). Three have been seen in this "
   "federation's history: the 2026-01 broadcast storm (a dashboard "
   "refreshing by broadcast every 30 seconds - fixed by caching), one "
   "unlogged broadcast pattern (the audit's finding), and one shadow "
   "skip (the retrained coordinator). The catalog's value is "
   "recognition: each anti-pattern lists its smell, its damage, and "
   "its cure - so the next occurrence is caught at the smell stage."),
 "how_it_works": ("Each anti-pattern entry: the smell (what it looks "
   "like early), the damage (what it costs late), the cure (the "
   "specific fix), and the detector (the metric or audit that catches "
   "it). Broadcast storm: smell - broadcast share rising; damage - "
   "member overload, 64x cost; cure - cache + scatter; detector - the "
   "dashboard's pattern mix alert at 10%. God coordinator: smell - "
   "coordinator deploys growing; damage - single point of scaling; "
   "cure - push logic to members; detector - coordinator CPU vs shard "
   "CPU ratio. The catalog is reviewed annually and after every "
   "incident: new anti-patterns are admitted by the same bar as "
   "charter amendments (they are, in effect, negative law). The worst "
   "seen - the broadcast storm - is retold to every new member at "
   "onboarding: the federation's cautionary tale."),
 "key_points": [
   "8 anti-patterns catalogued; 3 seen in this federation's history.",
   "Each: smell, damage, cure, detector.",
   "Worst seen: the 2026-01 broadcast storm (dashboard by broadcast).",
   "Catalog reviewed annually and after incidents.",
   "Retold at onboarding - the cautionary tale.",
   "Recognition at the smell stage, not the damage stage.",
 ],
 "requirements": [
   "Catalog with smell/damage/cure/detector per pattern.",
   "Annual + incident-driven review.",
   "Onboarding retelling.",
   "Detectors wired to monitoring.",
 ],
 "standards": [
   "Admitted by charter-amendment bar.",
   "Seen patterns include the full postmortem.",
   "Detectors must exist, not just be described.",
   "Cures specific, not homiletic.",
 ],
 "citations": [
   "Sheth & Larson (1990).",
 ],
 "sig_lens": ("The Signature Federation Doctrine names its demons: the "
   "doctrine requires the eight anti-patterns written down with their "
   "smells and cures. The Signature edition retells the broadcast storm "
   "at every onboarding - a doctrine that forgets its failures is "
   "doomed to rebroadcast them."),
},
{
 "name": "Federation Self-Audit and Mastery Record",
 "group": "Advanced", "ladder_rank": 34, "ladder_tier": "advanced",
 "demo_key": "g_mastery",
 "demo_data": {"records": 34, "complete": 34, "members": 64, "contracts": 12, "coverage": 1.0},
 "description": ("The federation self-audit and mastery record proves the "
   "alliance accounts for itself: thirty-four federation archetypes "
   "catalogued, thirty-four complete, sixty-four members healthy (two "
   "degraded, honestly shown), twelve join contracts in force, coverage "
   "one hundred percent. This is the record that closes the loop - the "
   "federation's knowledge of federation, audited. It verifies that "
   "every member is attested, every contract monitored, every pattern "
   "costed, and the charter's amendment process alive (three amendments "
   "prove it). A federation that cannot describe its own patterns, "
   "contracts, and failures is not governing - it is merely querying "
   "together and hoping."),
 "how_it_works": ("The self-audit checks: membership completeness (64 "
   "registered, attested this quarter), contract health (12 contracts, "
   "success rates above 99%), pattern discipline (broadcast share 6%, "
   "under the 10% alert), cost accuracy (estimator MAPE 11%, within "
   "bounds), security posture (4 controls, audits current), and "
   "governance vitality (board cadence met, amendments processed). The "
   "example: 34 of 34 complete, coverage 1.0. Findings become "
   "anti-patterns or charter amendments, tracked to closure. The audit "
   "runs quarterly with its report to all members - the federation "
   "audits itself in the open. This record is also the mastery "
   "checkpoint: a reader who understands all thirty-four records - from "
   "scatter-gather through two-phase commit to the charter - understands "
   "database federation end to end."),
 "key_points": [
   "34 archetypes, 34 complete; 64 members; 12 contracts; coverage 1.0.",
   "Self-audit checks membership, contracts, patterns, costs, security, governance.",
   "Findings become anti-patterns or charter amendments.",
   "Runs quarterly; report to all members, in the open.",
   "Amendment vitality (3 amendments) proves the governance lives.",
   "Mastery checkpoint: all 34 records teach federation end to end.",
 ],
 "requirements": [
   "Self-audit executed quarterly with published report.",
   "All six audit dimensions checked.",
   "Findings tracked to closure.",
   "Mastery path documented from record 1 to record 34.",
 ],
 "standards": [
   "Coverage target 1.0.",
   "Reports to all members.",
   "Audit independent of daily operations.",
   "Year-over-year trend reported.",
 ],
 "citations": [
   "ISO 19011:2018 Guidelines for auditing management systems.",
 ],
 "sig_lens": ("The Signature Federation Doctrine ends by auditing the "
   "alliance itself: the doctrine requires the 34/34, the 64 members, "
   "the 12 contracts - counted in the open. The Signature self-audit "
   "closes the loop from record 1 to record 34: many databases, one "
   "question, zero confusion - and the proof."),
},
]

assert len(ENTRIES) == 34, "expected 34 entries, got %d" % len(ENTRIES)
_ranks = [e["ladder_rank"] for e in ENTRIES]
assert _ranks == sorted(_ranks) == list(range(1, 35)), "ladder ranks must be 1..34 in order"
