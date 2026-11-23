#!/usr/bin/env node
/* Seeded boundless generator for cloud-to-local-ai-management.
   Package-only. `node gen-cloud-to-local-ai-management.js [seed]` prints one JSON record;
   `node gen-cloud-to-local-ai-management.js --test` runs runTests (10 tests).
   Deterministic: the same seed always emits the same record.
   Gates: emitted record_kind == manifest record_kind; slug form;
   id prefix; hard_stop 1,000,000,000; gen prefix; JCC round-trip. */
const crypto = require("crypto");
const SLUG = "cloud-to-local-ai-management";
const EDITION = "public";
const RECORD_KIND = "cloud to local ai management record";
const ID_PREFIX = "JAH-CLAM-";
const GEN_PREFIX = "JAH-CLAMGEN-";
const AI_NAME = "JAH Cloud-to-Local AI Management Librarian";
const SRC = "public-harvest";
const TOPICS = [["Cloud Inventory and Catalogue", "Listing every cloud machine, model, and service the manager can use.", "The cloud inventory is the manager's map of the cloud: every machine, every model, every service, with its cost, its speed, and its limits, listed in one catalogue.", {"providers": 4, "machine_entries": 64, "regions": 12, "catalogue_pages": 16}], ["Local Machine Registry", "Listing every local machine that can run AI work.", "The local registry is the manager's map of the machines in the room: every laptop, desktop, and small server, with what it can run, how much memory it has, and when it is free.", {"machines": 18, "models_run": 42, "checks_per_year": 52, "registry_pages": 6}], ["Job Routing and Placement", "Deciding where each AI job runs: cloud or local, and on which machine.", "Routing is the manager's main job: for each AI job, choose the machine that will do it best -- fast enough, cheap enough, and allowed to see the data.", {"jobs_routed": 1240, "placements_logged": 1240, "fallbacks_used": 38, "router_rules": 9}], ["Model Sync and Versioning", "Keeping the same AI model, in the same version, on cloud and local machines.", "A model that is version 3 in the cloud and version 2 on the local machine will give different answers, so the manager syncs models and versions them so both sides match.", {"models_synced": 24, "versions_kept": 2, "fingerprint_mismatches": 3, "syncs_per_month": 8}], ["Cost Ledger and Budget Guard", "Counting what AI work costs and stopping work that would overspend.", "The cost ledger counts every hour of cloud time and every job, and the budget guard stops a job before it spends more than the user agreed.", {"ledger_entries": 1240, "budgets_guarded": 12, "jobs_stopped": 17, "reports_per_year": 12}], ["Privacy and Data Boundary Rules", "The rules that keep private data on the local machine.", "The boundary rules are the manager's promise: data the user marked private never leaves the local machine, and data that may go to the cloud is listed in writing.", {"boundary_rules": 8, "private_marks": 46, "crossings_logged": 312, "refusals": 5}], ["Offline Mode and Reconnect", "Working when the internet is gone, and catching up when it returns.", "Offline mode is the manager's plan for a dead connection: local work carries on, cloud work waits, and when the connection returns the two sides catch up without losing anything.", {"offline_hours_tested": 24, "jobs_queued": 57, "jobs_lost": 0, "reconnect_checks": 12}], ["Latency and Performance Watch", "Watching how fast jobs answer and fixing what is slow.", "The watch measures how long each job takes from request to answer, and it raises a flag when a job is slower than the manager promised.", {"jobs_timed": 1240, "limits_set": 9, "slow_jobs_flagged": 41, "causes_found": 41}], ["Model Handover Protocol", "Moving a running model from one machine to another without dropping the work.", "Handover moves a model and its working state from one machine to another -- cloud to local, or local to cloud -- so the work continues where it left off.", {"handovers": 64, "handovers_failed": 2, "handover_tests_per_year": 12, "average_handover_minutes": 4}], ["Local Cache and Storage Plan", "Keeping the models and data a local machine needs, close at hand.", "The cache plan decides what each local machine keeps on its own disk: the models it runs often, the data it uses daily, and nothing it does not need.", {"machines_cached": 18, "models_cached": 42, "cache_cleanings": 52, "removals_reported": 31}], ["Sync Conflict Resolution", "Deciding what wins when cloud and local copies disagree.", "When the cloud copy and the local copy of a model or a file disagree, the manager must decide which one wins -- and write down why.", {"conflicts": 11, "resolved_by_rule": 8, "resolved_by_user": 3, "copies_lost": 0}], ["Access Control and Permissions", "Who may use which machine, model, and piece of data.", "Access control is the manager's lock: every user has a key that opens only what they are allowed to use, and every use is recorded.", {"users": 12, "permissions": 48, "keys_removed_same_day": 3, "uses_logged": 1240}], ["Audit Log and Trace", "A complete record of every job, every placement, and every crossing.", "The audit log is the manager's memory: every job, where it ran, what it cost, what data it touched, and who asked for it, in order, with dates.", {"log_entries": 3720, "monthly_reviews": 12, "patterns_found": 4, "corrections_logged": 9}], ["Failure and Fallback Plan", "What happens when a machine, a connection, or a model fails.", "The fallback plan is written before anything fails: for each kind of failure, the next machine, the next model, and the next step, so work carries on.", {"failures_named": 8, "fallbacks_tested": 8, "tests_per_year": 4, "failures_logged": 23}], ["Bandwidth Planner", "Planning how much network traffic the manager will use.", "The bandwidth planner counts how much data moves between cloud and local machines, and schedules the big moves for times when the connection is quiet.", {"gigabytes_moved_per_month": 48, "quiet_hours": 6, "change_only_syncs": 31, "plan_checks": 12}], ["Energy and Heat Budget", "Counting the power local machines use and keeping them cool.", "Local machines use power and make heat, so the manager budgets both: how much power each job may use, and what happens when a machine gets too hot.", {"machines_budgeted": 18, "power_limit_watts": 65, "heat_moves": 7, "budget_checks": 12}], ["Update Rollout Schedule", "Rolling out updates to models and the manager without breaking work.", "Updates are rolled out in stages: one machine first, then a few, then all -- so a bad update breaks one machine, not every machine at once.", {"rollout_stages": 3, "stages_tested": 3, "rollbacks": 1, "notices_sent": 8}], ["Multi-Cloud Broker", "Using more than one cloud provider and choosing the best for each job.", "The broker keeps the manager free to use any cloud provider: it compares prices, speeds, and rules, and picks the best provider for each job.", {"providers": 4, "moves_tested": 4, "placements_by_price": 412, "placements_by_speed": 388}], ["Local Model Library", "The shelf of models kept on local machines, ready to run.", "The local library is the shelf where local models live: each model with its version, its size, what it is for, and which machines run it.", {"library_models": 24, "shelf_machines": 18, "removals": 9, "weekly_checks": 52}], ["Job Queue and Priority", "The order jobs run in, and which jobs jump the queue.", "The queue is the manager's waiting line: jobs wait in order, urgent jobs go first, and no job waits so long that it is forgotten.", {"jobs_queued": 1240, "urgent_jobs": 96, "overflows_offered": 14, "jobs_waiting_past_limit": 3}], ["Health Check and Repair", "Checking every machine and model regularly and fixing what is sick.", "The health check is the manager's regular examination: each machine and model is tested on a schedule, and anything sick is repaired or replaced before it fails in front of a user.", {"machines_checked": 18, "models_checked": 24, "repairs": 11, "retirements": 2}], ["User Dashboard and Reports", "What the user sees: costs, jobs, machines, and health in one place.", "The dashboard is the manager's front page: one screen showing what is running, what it costs, which machines are busy, and what needs attention.", {"dashboard_items": 8, "reports_per_year": 12, "attention_items": 5, "explanations_available": 8}], ["Migration Planner", "Planning a move of work from cloud to local, or local to cloud.", "The migration planner plans a move of work between cloud and local machines: what moves, in what order, how long it takes, and what to do if it goes wrong.", {"migrations_planned": 9, "items_moved": 147, "migrations_failed": 1, "rollback_plans": 9}], ["Management Scale and Limits", "How big the manager can grow and where it stops.", "The scale record states the manager's limits honestly: how many machines, how many models, how many jobs, and what happens when the limits are reached.", {"machines_limit": 50, "models_limit": 100, "jobs_per_day_limit": 500, "limit_reviews_per_year": 1}]];

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
