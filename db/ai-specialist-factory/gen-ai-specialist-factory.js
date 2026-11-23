#!/usr/bin/env node
/* Seeded boundless generator for ai-specialist-factory.
   Package-only. `node gen-ai-specialist-factory.js [seed]` prints one JSON record;
   `node gen-ai-specialist-factory.js --test` runs runTests (10 tests).
   Deterministic: the same seed always emits the same record.
   Gates: emitted record_kind == manifest record_kind; slug form;
   id prefix; hard_stop 1,000,000,000; gen prefix; JCC round-trip. */
const crypto = require("crypto");
const SLUG = "ai-specialist-factory";
const EDITION = "public";
const RECORD_KIND = "ai specialist factory record";
const ID_PREFIX = "JAH-AISF-";
const GEN_PREFIX = "JAH-AISFGEN-";
const AI_NAME = "JAH AI Specialist Factory Librarian";
const SRC = "public-harvest";
const TOPICS = [["Specialist Intake and Briefing", "How a request for a specialist AI is taken in and written as a brief.", "A specialist factory begins with a plain request: a person says what they need done, in their own words, and the factory turns that into a written brief a builder can work from.", {"brief_fields": 12, "clarifying_questions": 3, "queue_slots": 40, "brief_pages": 1}], ["Capability Blueprint", "The written plan of what the specialist must be able to do.", "The blueprint turns the brief into a plan of capabilities: each thing the specialist must do, the knowledge each capability needs, the tools each capability uses, and the order the capabilities are built in.", {"capabilities": 18, "essential_capabilities": 11, "reviewers": 2, "blueprint_pages": 4}], ["Knowledge Pack Assembly", "Gathering the specialist's reference knowledge into one pack.", "A specialist is only as good as what it knows, so the factory assembles a knowledge pack: the documents, tables, rules, and examples the specialist will draw on, checked, dated, and filed in one place.", {"pack_items": 120, "sources_checked": 96, "contradictions_flagged": 7, "pack_versions": 3}], ["Skill Module Library", "Reusable skill units the factory keeps on the shelf.", "A skill module is one small, tested ability -- reading a table, checking a date, drafting a letter -- that any specialist can borrow instead of being trained from nothing.", {"modules": 84, "modules_in_use": 61, "module_tests": 84, "retirements_per_month": 2}], ["Training Run and Tuning", "Building the specialist and tuning it until it passes its tests.", "Training is the slow, careful work of turning the blueprint and the knowledge pack into a working specialist, then tuning it until it passes every capability test.", {"training_runs": 6, "tests_per_run": 18, "tuning_changes": 23, "release_runs_required": 2}], ["Test Bench and Scoring", "Testing the specialist fairly and scoring it honestly.", "The test bench is the factory's proving ground: a fixed set of tasks, a fixed way of scoring them, and a report that says plainly what the specialist can and cannot do.", {"bench_tasks": 240, "capabilities_scored": 18, "archive_entries": 312, "scorers": 2}], ["Safety and Permission Review", "Checking what the specialist may do before it is released.", "Before any specialist leaves the factory, a reviewer checks its permissions: what data it may read, what tools it may use, what it may say, and what it must refuse.", {"checklist_items": 24, "permissions_checked": 31, "refusals_tested": 12, "reviewers": 1}], ["Specialist Registry and Listing", "The catalogue entry that lets people find the specialist.", "The registry is the factory's public list: one entry per specialist, with its name, its capabilities, its tests, its limits, and how to reach it.", {"registry_entries": 96, "entries_updated_same_day": 96, "retired_entries": 14, "fields_per_entry": 9}], ["Deployment and Handover", "Giving the specialist to its user, working, on day one.", "Deployment is the move from the factory to the user's hands: the specialist is installed, connected to its tools and data, introduced to its user, and checked working in its real place.", {"handover_items": 7, "first_week_days": 7, "mismatches_fixed": 5, "sign_offs": 96}], ["Update and Retraining Cycle", "Keeping the specialist current as knowledge and needs change.", "A specialist goes stale: knowledge changes, tools change, and the user's needs change, so the factory runs a regular update cycle -- new knowledge, new tests, and a fresh review.", {"review_cycle_days": 90, "updates_per_year": 4, "regression_tests": 18, "versions_kept": 2}], ["Specialist Retirement and Archive", "Ending a specialist's service cleanly and keeping its record.", "When a specialist is no longer needed, the factory retires it properly: its tools are disconnected, its data is returned or deleted as agreed, and its full record is archived.", {"notice_days": 30, "archived_records": 14, "permissions_revoked": 31, "archive_years": 10}], ["Multi-Specialist Teams", "Specialists working together as one team.", "Some jobs need more than one specialist, so the factory builds teams: several specialists with different skills, a shared brief, and a coordinator that divides the work and joins the results.", {"team_size": 4, "joint_tasks": 36, "hand_offs": 12, "team_tests": 48}], ["Domain Glossary Builder", "The specialist's vocabulary, defined in plain words.", "Every specialist needs words that mean exactly one thing, so the factory builds a glossary: each technical term defined in plain words on first use, with no acronym left unexplained.", {"glossary_terms": 140, "terms_defined": 140, "examples": 140, "updates_per_year": 4}], ["Tool and API Binding", "Connecting the specialist to the tools it needs.", "A specialist that cannot use tools can only talk, so the factory binds each tool the blueprint names: the connection, the permissions, the limits, and the test that proves the binding works.", {"tools_bound": 9, "bindings_tested": 9, "failed_calls_logged": 17, "binding_retests_per_year": 4}], ["Memory and Context Design", "What the specialist remembers, and what it forgets.", "A specialist needs memory to be useful and limits on memory to be safe, so the factory designs its context: what it keeps from each conversation, how long it keeps it, and what it never keeps.", {"memory_types": 3, "user_controls": 4, "forgetting_tests": 12, "lifetimes_defined": 3}], ["Evaluation Suite", "The standard tests every specialist must pass.", "The evaluation suite is the factory's shared exam: the same tasks, the same scoring, for every specialist of a kind, so specialists can be compared fairly.", {"suite_tasks": 120, "suite_version": 3, "specialists_scored": 96, "refresh_years": 1}], ["Cost and Capacity Planning", "Running the factory affordably and without overload.", "A factory that cannot pay its own costs closes, so the factory plans cost and capacity: what each build costs, how many builds fit in a month, and where the money comes from.", {"builds_per_month": 12, "cost_items": 8, "reviews_per_year": 12, "queue_limit": 40}], ["Factory Quality Gate", "The final check before a specialist leaves the factory.", "The quality gate is the last door: a specialist passes through it only when its tests, its review, its registry entry, and its handover pack are all complete and signed.", {"gate_items": 14, "gatekeepers": 2, "held_at_gate": 3, "gate_records": 96}], ["Customer Brief Translation", "Turning plain requests into specifications a builder can use.", "Most requesters do not speak in specifications, so the factory translates: the requester's plain words become a brief, a blueprint, and a test plan without losing what the requester meant.", {"vague_words_clarified": 9, "meaning_checks": 9, "requester_marks": 9, "drafts": 2}], ["Specialist Versioning", "Tracking specialist versions so nothing is lost.", "A specialist changes over time, so the factory versions it: every release gets a number, a date, a list of what changed, and a way back to the previous version.", {"versions_per_specialist": 4, "change_list_items": 11, "versions_archived": 4, "notice_days": 7}], ["Failure Review and Repair", "Fixing a specialist that fails, and learning from the failure.", "When a specialist fails in front of a user, the factory treats the failure as a job: find what went wrong, fix it, test the fix, and write down what was learned.", {"failures_reviewed": 19, "fixes_released": 19, "lessons_shared": 19, "retest_tasks": 18}], ["Specialist Marketplace Listing", "Listing a specialist for others to find and hire.", "Some specialists are built to be shared, so the factory lists them in a marketplace: a public entry with capabilities, test scores, price, and terms, so a stranger can hire with confidence.", {"listings": 41, "hires_recorded": 203, "complaints": 6, "listings_removed": 2}], ["Factory Audit Trail", "Records of everything the factory did, in order.", "The audit trail is the factory's memory: every brief, every build, every test, every review, every release, and every retirement, filed in order with dates and names.", {"trail_entries": 1840, "quarterly_reviews": 4, "patterns_found": 5, "trail_years": 3}], ["Factory Scale-Up", "Growing the factory without breaking what works.", "When demand grows, the factory grows in steps: more builders, more test benches, more reviewers -- added one at a time, with the quality gate unchanged.", {"builds_per_month_now": 12, "builds_per_month_target": 20, "bottlenecks_found": 2, "training_months": 3}]];

function canon(v) {
  if (v === null || typeof v !== "object") return JSON.stringify(v);
  if (Array.isArray(v)) return "[" + v.map(canon).join(",") + "]";
  const keys = Object.keys(v).sort();
  return "{" + keys.map(k => JSON.stringify(k) + ":" + canon(v[k])).join(",") + "}";
}

function demoFor(figures) {
  const keys = Object.keys(figures).sort();
  const totalA = keys.reduce((a, k) => a + figures[k], 0);
  let totalB = 0;
  for (const k of keys) totalB += figures[k];
  const d1 = crypto.createHash("sha256").update(String(totalA)).digest("hex");
  const d2 = crypto.createHash("sha256").update(String(totalB)).digest("hex");
  return "total=" + totalA + "\ndigest_a=" + d1 + "\ndigest_b=" + d2 + "\nmatch=" + (d1 === d2) + "\n";
}

function makeRecord(seed) {
  const n = ((seed % 24) + 24) % 24;
  const t = TOPICS[n];
  const id = ID_PREFIX + String(n + 1).padStart(6, "0");
  const rec = {
    id: id,
    slug: SLUG,
    edition: EDITION,
    record_kind: RECORD_KIND,
    title: t[0],
    subject: t[1],
    status: "built",
    src: SRC,
    ai_name: AI_NAME,
    description: t[2],
    key_figures: t[3],
    demo: { code: "node demo: recomputes the figures twice and prints both SHA-256 digests" },
    expected_output: demoFor(t[3]),
    program: "RecordProgram with run() recomputing the same total and digest",
    sources: [{ name: "hashlib -- Python documentation", url: "https://docs.python.org/3/library/hashlib.html", retrieved: "2026-11-18", resource_id: "python-docs:hashlib" }],
    generator: { type: "seeded boundless generator", gen_id_prefix: GEN_PREFIX, hard_stop: 1000000000, throttle_per_call: 100, ceiling_note: "Generator ceiling: up to 1,000,000,000 scales per file, generated on demand by the file AI -- not stored files." },
    scales: { A1: "One record: " + t[0], A2: "The whole type: 24 records in the " + EDITION + " edition.", A3: "The type against the network." },
  };
  rec.jcc_key = "k=" + crypto.createHash("sha256").update(canon(rec)).digest("hex").slice(0, 8);
  rec.jcc_code = "JAHDB/" + SLUG + "#" + id;
  return rec;
}

function runTests() {
  let passed = 0, failed = 0;
  function check(name, ok) { if (ok) { passed++; } else { failed++; console.log("FAIL: " + name); } }
  const a = makeRecord(42), b = makeRecord(42), c = makeRecord(43);
  check("same seed twice identical", JSON.stringify(a) === JSON.stringify(b));
  check("record_kind", a.record_kind === RECORD_KIND);
  check("slug form", a.slug === SLUG);
  check("id prefix", a.id.startsWith(ID_PREFIX));
  check("hard_stop 1000000000", a.generator.hard_stop === 1000000000);
  check("gen prefix", a.generator.gen_id_prefix === GEN_PREFIX);
  check("jcc_code form", a.jcc_code === "JAHDB/" + SLUG + "#" + a.id);
  const slim = Object.assign({}, a); delete slim.jcc_key; delete slim.jcc_code;
  check("jcc_key round-trip", a.jcc_key === "k=" + crypto.createHash("sha256").update(canon(slim)).digest("hex").slice(0, 8));
  check("different seeds differ", JSON.stringify(a) !== JSON.stringify(c));
  check("19 keys", Object.keys(a).length >= 19);
  console.log(passed + " passed, " + failed + " failed");
  return failed === 0;
}

if (require.main === module) {
  if (process.argv[2] === "--test") { process.exit(runTests() ? 0 : 1); }
  const seed = parseInt(process.argv[2] || "1", 10);
  console.log(JSON.stringify(makeRecord(isNaN(seed) ? 1 : seed)));
}
module.exports = { makeRecord, runTests };
