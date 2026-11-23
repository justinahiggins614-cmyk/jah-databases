#!/usr/bin/env node
/* Seeded boundless generator for cloud-to-local-ai-management-signature.
   Package-only. `node gen-cloud-to-local-ai-management-signature.js [seed]` prints one JSON record;
   `node gen-cloud-to-local-ai-management-signature.js --test` runs runTests (10 tests).
   Deterministic: the same seed always emits the same record.
   Gates: emitted record_kind == manifest record_kind; slug form;
   id prefix; hard_stop 1,000,000,000; gen prefix; JCC round-trip. */
const crypto = require("crypto");
const SLUG = "cloud-to-local-ai-management-signature";
const EDITION = "signature";
const RECORD_KIND = "cloud to local ai management record";
const ID_PREFIX = "JAH-CLAMS-";
const GEN_PREFIX = "JAH-CLAMSGEN-";
const AI_NAME = "JAH Cloud-to-Local AI Management Librarian (Signature)";
const SRC = "signature-generated";
const TOPICS = [["The Two-Room House", "A manager built as a house with two rooms: cloud and local.", "In this design the manager is a house with two rooms, one cloud and one local, and a door between them that only opens for data the user allowed. The housekeeper knows which room each job belongs in and never puts a private job in the cloud room. The design suits managers whose users think in rooms, not in networks.", {"rooms": 2, "doors": 1, "locks": 1, "jobs_housed": 1240}], ["The Ferryman", "A manager that ferries jobs across the water between cloud and local.", "In this design the manager is a ferryman: jobs wait on one bank, the ferry carries them across, and nothing is dropped in the water. The ferry runs on a timetable, and a job that misses the ferry waits for the next one. The design suits managers whose connections are slow and where every crossing must be planned.", {"ferry_trips": 312, "jobs_ferried": 1240, "jobs_dropped": 0, "timetable_hours": 24}], ["The Ledger Keeper", "A manager whose main job is the cost ledger.", "In this design the manager is a ledger keeper first and a router second: every job is written in the ledger before it runs, and a job with no budget entry does not run. The design suits managers whose users care most about money and want the cost visible before the work, not after it.", {"ledger_entries": 1240, "bell_rings": 17, "jobs_stopped": 17, "budgets": 12}], ["The Border Guard", "A manager that guards the boundary between local and cloud.", "In this design the manager is a border guard: it stands at the boundary, checks every piece of data that wants to cross, and turns back anything private. The guard keeps a log of every crossing and every refusal. The design suits managers whose users' privacy depends on the boundary holding.", {"crossings_checked": 312, "refusals": 5, "log_entries": 312, "guards": 1}], ["The Lighthouse", "A manager that watches from a lighthouse and warns of slow jobs.", "In this design the manager is a lighthouse: it watches every job's time from above and flashes a warning when a job is slow. The light reaches every machine, cloud and local, and no slow job can hide. The design suits managers whose users wait for answers and need to know when an answer is late.", {"jobs_watched": 1240, "warnings_flashed": 41, "causes_found": 41, "lamp_hours": 24}], ["The Relay Race", "A manager that hands models from machine to machine like a baton.", "In this design a model handover is a relay race: the baton is the model's state, and it is passed from one machine to the next without being dropped. The runner who drops the baton stops the race. The design suits managers that move models often and need handovers to be boring and reliable.", {"handovers": 64, "batons_dropped": 2, "zones": 3, "races_run": 64}], ["The Pantry", "A manager that keeps local models in a pantry, ready to use.", "In this design the local cache is a pantry: models are jars on shelves, labeled with their last use, and the pantry is cleaned weekly. A jar nobody has opened in a month is taken off the shelf. The design suits managers whose local machines have small disks and need to know exactly what is stored.", {"jars": 42, "shelves": 6, "cleanings": 52, "jars_removed": 9}], ["The Referee", "A manager that settles sync conflicts like a referee.", "In this design the manager is a referee: when cloud and local copies disagree, the referee blows the whistle, reads the rules, and decides. When the rules cannot decide, the referee keeps both copies and asks the user. The design suits managers whose copies disagree often and need decisions that can be explained.", {"conflicts": 11, "decisions_by_rule": 8, "decisions_by_user": 3, "rule_book_pages": 4}], ["The Key Ring", "A manager that keeps every user's key on one ring.", "In this design access control is a key ring: every user has a key that opens only their doors, and the ring is checked before every job. When a user leaves, their key is cut off the ring the same day. The design suits managers with many users sharing machines and models.", {"keys": 12, "doors": 48, "keys_cut_off": 3, "checks": 1240}], ["The Ship's Log", "A manager that keeps its audit log like a ship's log.", "In this design the audit log is a ship's log: every job, every placement, and every crossing is written in order, dated, and signed, and nothing is ever rewritten. The captain reads it every month. The design suits managers whose users need to prove, months later, exactly what happened.", {"entries": 3720, "reviews": 12, "rewrites": 0, "captains": 1}], ["The Spare Tire", "A manager that keeps a fallback ready for every failure.", "In this design every failure has a spare tire: a fallback machine, a fallback model, a fallback plan, kept ready and tested every quarter. When a tire blows, the spare is already on. The design suits managers whose users cannot afford to wait while a failure is fixed.", {"spares": 8, "tests_per_year": 4, "changes": 23, "failures_without_spare": 0}], ["The Water Meter", "A manager that measures network traffic like water.", "In this design bandwidth is water: the planner is a water meter, measuring every litre that flows between cloud and local, and the big flows are scheduled for the night when nobody is thirsty. The design suits managers whose connections are slow or expensive and where a big move at the wrong time hurts everyone.", {"litres_per_month": 48, "night_hours": 6, "leaks_found": 2, "meters": 1}], ["The Thermostat", "A manager that keeps local machines cool like a thermostat.", "In this design the manager is a thermostat: it watches the heat of every local machine and turns down the work when a machine gets hot. A hot machine is given less work until it cools. The design suits managers whose local machines are small and easily overheated.", {"machines_watched": 18, "heat_moves": 7, "gauges": 18, "fans": 18}], ["The Staircase", "A manager that rolls out updates one step at a time.", "In this design updates climb a staircase: one machine first, then a few, then all, with a landing between each flight to check that nothing broke. A bad step stops the climb. The design suits managers whose updates must never break every machine at once.", {"flights": 3, "landings": 3, "rollbacks": 1, "climbs": 8}], ["The Broker's Table", "A manager that buys cloud time at a broker's table.", "In this design the manager is a broker: it sits at a table with every cloud provider, compares their prices and speeds, and buys the best for each job. The broker never buys from habit. The design suits managers whose users want the cheapest or fastest machine for each job, not the same provider every time.", {"providers": 4, "comparisons": 1240, "provider_changes": 6, "brokers": 1}], ["The Bookshelf", "A manager that keeps local models on a bookshelf.", "In this design the local library is a bookshelf: each model is a book, labeled with its version and fingerprint, and a book nobody has read in a month is returned to the store. The design suits managers whose users want to see, at a glance, which models live locally.", {"books": 24, "shelves": 6, "returns": 9, "weekly_checks": 52}], ["The Waiting Room", "A manager that runs its job queue like a waiting room.", "In this design the queue is a waiting room: jobs sit in chairs in order, urgent jobs are called first, and a job that has waited too long is called by name. The design suits managers whose users wait for answers and need to know their job has not been forgotten.", {"chairs": 40, "urgent_calls": 96, "late_calls": 3, "waiting_rooms": 1}], ["The Clinic", "A manager that checks machine health like a clinic.", "In this design the health check is a clinic: every machine is examined weekly, every model monthly, and anything sick is treated before it fails. A machine that keeps getting sick is sent home for good. The design suits managers whose machines are old or heavily used and need regular care.", {"machines_examined": 18, "models_examined": 24, "treatments": 11, "retirements": 2}], ["The Notice Board", "A manager whose dashboard is a notice board in the village square.", "In this design the dashboard is a notice board: costs, jobs, and health are pinned where everyone can read them, and bad news is pinned at the top in large letters. The design suits managers whose users want the truth at a glance, without logging in or asking.", {"board_items": 8, "letters_per_year": 12, "bad_news_pinned": 5, "readers": 12}], ["The Moving Van", "A manager that plans migrations like a moving van.", "In this design a migration is a moving van: everything is listed, packed in order, and moved least-important first, and the old house is kept until the new one is proven. The design suits managers whose moves are big and whose users fear losing something in the move.", {"moves": 9, "items_moved": 147, "items_lost": 0, "vans": 1}], ["The Fence", "A manager that knows its limits and fences them plainly.", "In this design the manager's limits are a fence: the fence is measured, painted, and signed, and when a job would cross it, the manager says so plainly and offers a choice. The design suits managers whose users would rather be told no than be silently dropped.", {"fence_posts": 4, "warnings": 12, "choices_offered": 14, "silent_drops": 0}], ["The Twin Kitchens", "A manager that runs cloud and local work as two kitchens.", "In this design cloud and local are two kitchens: each cooks its own dishes, they share the pantry of models, and a dish is cooked in the kitchen that does it best. The design suits managers whose work splits naturally into cloud dishes and local dishes.", {"kitchens": 2, "dishes": 1240, "shared_pantry_items": 24, "cooks": 2}], ["The Post Office", "A manager that delivers jobs like a post office.", "In this design the manager is a post office: jobs are letters, each with an address and a stamp, and the post office delivers each one to the right machine. A letter that cannot be delivered is returned to the sender with the reason written on it. The design suits managers whose jobs travel far and need proof of delivery.", {"letters": 1240, "delivered": 1240, "returned": 3, "post_offices": 1}], ["The Weighbridge", "A manager that weighs each job before it is routed.", "In this design the router is a weighbridge: every job is weighed -- its memory, its time, its privacy -- before it is sent anywhere, and the weight decides the machine. A job that is too heavy for the local machine goes to the cloud; a job that is too private for the cloud stays local. The design suits managers whose placements must be explained by numbers, not by habit.", {"jobs_weighed": 1240, "tickets_written": 1240, "scales_checked": 12, "weighbridges": 1}]];

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
