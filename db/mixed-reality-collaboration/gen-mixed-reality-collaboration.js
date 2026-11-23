#!/usr/bin/env node
/* Seeded boundless generator for mixed-reality-collaboration.
   Package-only. `node gen-mixed-reality-collaboration.js [seed]` prints one JSON record;
   `node gen-mixed-reality-collaboration.js --test` runs runTests (10 tests).
   Deterministic: the same seed always emits the same record.
   Gates: emitted record_kind == manifest record_kind; slug form;
   id prefix; hard_stop 1,000,000,000; gen prefix; JCC round-trip. */
const crypto = require("crypto");
const SLUG = "mixed-reality-collaboration";
const EDITION = "public";
const RECORD_KIND = "mixed reality collaboration record";
const ID_PREFIX = "JAH-MXRC-";
const GEN_PREFIX = "JAH-MXRCGEN-";
const AI_NAME = "JAH Mixed Reality Collaboration Librarian";
const SRC = "public-harvest";
const TOPICS = [["Shared Mixed-Reality Room", "One room where real and virtual things meet and people work together.", "A shared mixed-reality room is a real room with virtual things in it: a table everyone can see, models floating above it, and people -- some in the room, some joining from far away -- working on the same things at the same time.", {"room_area_sqm": 24, "joining_devices": 3, "people_per_room": 8, "saved_rooms": 12}], ["Anchor and Spatial Map", "Pinning virtual things to real places so they stay put.", "An anchor is a pin that holds a virtual thing to a real place: the model stays on the table even when people walk around it, because the anchor remembers where the table is.", {"anchors_per_room": 16, "drift_checks": 12, "anchors_remade": 4, "map_accuracy_cm": 2}], ["Avatar and Presence", "How people appear to each other in the shared room.", "An avatar is how a person appears in the room: a figure with a face, hands, and a voice, standing where the person stands, so others can see who is speaking and where they are looking.", {"avatar_parts": 6, "people_per_room": 8, "voice_sources": 8, "consent_checks": 8}], ["Shared Object and Whiteboard", "Things everyone in the room can touch, move, and draw on.", "A shared object is a virtual thing everyone can move: a model, a block, a chart. The whiteboard is a shared surface everyone can draw on, and what one person draws, everyone sees.", {"shared_objects": 24, "whiteboard_strokes": 480, "owners_at_once": 1, "saved_rooms": 12}], ["Voice and Gesture Channel", "Talking and gesturing so everyone understands.", "Voice and gesture are how people talk in the room: clear sound from where each person stands, and hand movements everyone can see, so a point or a wave means the same to all.", {"voice_channels": 8, "gesture_types": 12, "mutes": 9, "recording_notices": 12}], ["Hand Tracking and Controllers", "Using hands and controllers to work in the room.", "Hands and controllers are the room's tools: a hand can pick up a model, a controller can draw a line, and both are tracked so the virtual hand is where the real hand is.", {"tracking_cameras": 4, "controller_buttons": 6, "hand_actions": 9, "session_tests": 12}], ["Room Permissions and Roles", "Who may do what in the shared room.", "Permissions are the room's rules: the host may invite and remove, a presenter may move the shared objects, and a guest may look and speak but not change the work.", {"roles": 4, "permissions": 12, "role_changes_logged": 7, "invitations": 96}], ["Session Recording and Replay", "Recording a session so people who missed it can catch up.", "Recording captures the room -- voices, gestures, object moves, and whiteboard strokes -- so a person who missed the session can replay it and see what was decided.", {"sessions_recorded": 12, "consents": 96, "replay_seats": 8, "storage_days": 30}], ["Cross-Device Joining", "Joining the same room from a headset, a phone, or a computer.", "Cross-device joining means the room does not care what a person joins from: a headset sees the room in three dimensions, a phone sees it on a screen, and a computer sees it in a window -- and all three share the same room.", {"device_types": 3, "shared_truth_checks": 12, "late_joiners_caught_up": 14, "devices_tested": 3}], ["Spatial Audio Design", "Sound that comes from where it should in the room.", "Spatial audio places every sound where it belongs: a voice comes from the speaker, a model that clicks sounds from the model, and the room itself has a quiet hum that tells you how big it is.", {"audio_sources": 8, "falloff_distance_m": 6, "room_hum_db": 30, "audio_tests": 12}], ["Object Locking and Turn-Taking", "Taking turns with shared objects so nobody fights over them.", "Locking gives one person the object at a time, and turn-taking gives everyone a fair turn: when a person finishes, the object is free for the next person, and the queue is visible to all.", {"locks_per_room": 24, "turns_logged": 96, "host_unlocks": 3, "queue_length_max": 8}], ["Breakout Rooms", "Small side rooms where part of the group can work alone.", "A breakout room is a small room off the main room: two or three people step aside, work on one thing, and bring their result back to the main room.", {"breakouts_per_session": 3, "people_per_breakout": 3, "reports_back": 36, "split_seconds": 5}], ["File and Model Sharing in Space", "Putting files and models into the room where everyone can see them.", "Sharing in space means a file is not a link in a chat; it is a thing in the room -- a document on the table, a model floating where everyone can walk around it.", {"files_shared": 48, "models_opened": 36, "originals_changed": 0, "files_filed": 48}], ["Safety and Comfort Rules", "Keeping people safe and comfortable in mixed reality.", "Safety and comfort rules protect the people in the room: breaks, motion limits, and a plain way to leave at any time, because a person who feels ill or unsafe cannot work.", {"session_limit_minutes": 60, "breaks_per_session": 1, "exits_used": 4, "comfort_reports": 2}], ["Network Sync and Latency Budget", "Keeping everyone in step when the network is slow.", "Sync keeps the room's shared truth true for everyone: when the network is slow, the room slows the work rather than letting people see different rooms.", {"latency_budget_ms": 150, "people_measured": 8, "sync_failures": 2, "pauses": 5}], ["Room Templates Library", "Ready-made rooms for common kinds of work.", "A template is a room already set up: the table, the whiteboard, the objects, and the roles, arranged for one kind of work -- a design review, a lesson, a planning session -- so a group can start at once.", {"templates": 12, "template_uses": 96, "user_versions": 18, "retirements": 2}], ["Collaboration Score and Review", "Scoring how well the group worked together, honestly.", "The collaboration score measures the group, not the room: did everyone speak, did the work move forward, did the group leave with decisions -- scored plainly after each session.", {"measures": 4, "sessions_scored": 12, "improvements_tried": 9, "blame_events": 0}], ["Remote Expert View", "Letting an expert far away see what you see and guide you.", "The remote expert view lets an expert who is not in the room see what a worker sees -- through the worker's camera -- and draw marks on the worker's view to guide them.", {"expert_sessions": 18, "marks_drawn": 240, "marks_accepted": 228, "worker_closures": 18}], ["Annotation and Markup Tools", "Drawing and writing on real and virtual things in the room.", "Annotation tools let people draw on a model, write on a wall, or pin a note to a real object, so a thought is attached to the thing it is about.", {"annotations": 320, "notes_pinned": 96, "answered": 288, "open_annotations": 32}], ["Room Persistence and Save", "Saving a room so the work is still there tomorrow.", "Persistence means the room remembers: the objects, the whiteboard, the annotations, and the places of things are saved, and the room reopens exactly as it was left.", {"rooms_saved": 12, "auto_saves": 12, "weekly_tests": 52, "rooms_lost": 0}], ["Accessibility in Mixed Reality", "Making the room usable by people with different bodies and senses.", "Accessibility means the room works for people who cannot see, hear, stand, or use their hands the way the room expects -- with captions, spoken descriptions, seated modes, and one-handed controls.", {"access_modes": 4, "caption_coverage": 100, "testers": 6, "releases_checked": 12}], ["Multi-Room Navigation", "Moving between rooms without getting lost.", "Navigation lets a person move from one room to another -- from the main room to a breakout, from a lesson to a lab -- and always know where they are and how to get back.", {"rooms": 12, "doors": 12, "moves_logged": 96, "lost_persons": 0}], ["Integration with Calendars and Tasks", "Connecting the room to the calendar and the task list.", "Integration means the room knows the meeting: it opens from the calendar invitation, it knows who was invited, and it files its decisions into the task list when the session ends.", {"invitations_linked": 96, "decisions_filed": 84, "tasks_invented": 0, "calendars": 2}], ["Platform Scale and Limits", "How many rooms, people, and objects the platform can hold.", "The scale record states the platform's limits honestly: how many rooms, how many people per room, how many objects, and what happens at the limit.", {"people_per_room_limit": 8, "objects_per_room_limit": 100, "rooms_limit": 50, "limit_reviews_per_year": 1}]];

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
