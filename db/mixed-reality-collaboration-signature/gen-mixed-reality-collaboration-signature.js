#!/usr/bin/env node
/* Seeded boundless generator for mixed-reality-collaboration-signature.
   Package-only. `node gen-mixed-reality-collaboration-signature.js [seed]` prints one JSON record;
   `node gen-mixed-reality-collaboration-signature.js --test` runs runTests (10 tests).
   Deterministic: the same seed always emits the same record.
   Gates: emitted record_kind == manifest record_kind; slug form;
   id prefix; hard_stop 1,000,000,000; gen prefix; JCC round-trip. */
const crypto = require("crypto");
const SLUG = "mixed-reality-collaboration-signature";
const EDITION = "signature";
const RECORD_KIND = "mixed reality collaboration record";
const ID_PREFIX = "JAH-MXRCS-";
const GEN_PREFIX = "JAH-MXRCSGEN-";
const AI_NAME = "JAH Mixed Reality Collaboration Librarian (Signature)";
const SRC = "signature-generated";
const TOPICS = [["The Round Table", "A room built around one round table where all sit equal.", "In this design the room is a round table in an empty field: no head, no foot, and every person the same distance from the work. The table is the only furniture, and the work sits in the middle where all can reach it. The design suits groups that decide together and want no one to sit at the head.", {"seats": 8, "table_diameter_m": 3, "reach_distance_m": 1, "decisions_together": 12}], ["The Anchor Garden", "A room where anchors grow like plants in a garden.", "In this design anchors are planted like seeds: each virtual thing grows from a real feature, and the garden is tended so nothing drifts. A gardener walks the room each morning and re-plants what has moved. The design suits rooms whose furniture moves often and whose anchors must be replanted, not rebuilt.", {"anchors_planted": 16, "gardener_walks": 52, "replantings": 4, "garden_maps": 12}], ["The Mask Shop", "A room where avatars are chosen like masks in a shop.", "In this design avatars hang in a shop: a person walks in, tries a mask, and wears the one that feels right. No mask is a real face, and every mask carries a name tag. The design suits rooms where people want to choose how they appear and change it as they like.", {"masks": 24, "try_ons": 96, "name_tags": 96, "shops": 1}], ["The Shared Loom", "A room where the whiteboard is a loom and every stroke is a thread.", "In this design the whiteboard is a loom: each person's strokes are threads, and the finished cloth is the group's thinking. A thread can be followed back to its author, and a thread that is pulled out leaves a visible gap. The design suits groups whose thinking is built together, stroke by stroke.", {"threads": 480, "colours": 8, "cloths_kept": 12, "looms": 1}], ["The Whispering Gallery", "A room where voices travel along the walls to the right ears.", "In this design the room is a whispering gallery: a quiet word to a neighbour stays with the neighbour, and a word to the room reaches the room. The gallery is built so that distance is respected and no one is overheard by accident. The design suits rooms where side conversations matter and privacy is part of the work.", {"whisper_seats": 8, "room_voices": 1, "overheard": 0, "galleries": 1}], ["The Glove Box", "A room where hands are the only tools and they are shown truly.", "In this design the room is a glove box: hands go in, work is done, and the hands shown are the hands that are there -- never guessed, never faked. When tracking is lost, the gloves go grey and wait. The design suits rooms where the work is done by hand and a false hand is worse than no hand.", {"glove_ports": 8, "grey_waitings": 3, "sessions_tested": 12, "false_hands": 0}], ["The Key Ceremony", "A room where roles are given in a small ceremony at the door.", "In this design roles are given at the door, in a short ceremony: the host names each person's role in plain words, hands them their key, and the room records it. No one enters without a role, and no role is given in secret. The design suits rooms where who may do what must be beyond doubt.", {"ceremonies": 96, "keys_given": 96, "roles_disputed": 0, "doors": 1}], ["The Echo Library", "A room where sessions are kept as echoes that can be replayed.", "In this design recordings are echoes kept in a library: each session is an echo on a shelf, labeled with its date and its decisions, and anyone who was there may listen. Echoes fade after the agreed time and are never kept in secret. The design suits groups that need to remember what was decided and prove it later.", {"echoes": 12, "labels": 12, "fades": 12, "listeners": 96}], ["The Three Doors", "A room with three doors: headset, phone, and computer.", "In this design the room has three doors, one for each device, and all three open into the same room. A person who enters by the phone door finds the same table as the person who entered by the headset door. The design suits rooms whose people join from whatever they have in their pocket.", {"doors": 3, "rooms_behind": 1, "tests_per_year": 52, "late_entries": 14}], ["The Concert Hall", "A room where sound is placed like instruments in an orchestra.", "In this design the room is a concert hall: each voice is an instrument, placed where its player sits, and the room's own sound is the hall itself. A voice from the back sounds like it comes from the back. The design suits rooms where listening matters as much as speaking.", {"instruments": 8, "hall_size_sqm": 24, "listeners": 8, "tunings": 12}], ["The Passing of the Baton", "A room where the object is a baton passed from hand to hand.", "In this design a shared object is a baton: it is passed, never grabbed, and the pass is visible to all. The person who holds it is lit in their colour, and the next holder is named before the pass. The design suits rooms where turns matter and a grabbed object breaks the trust.", {"passes": 96, "grabs": 0, "holders_lit": 96, "passes_logged": 96}], ["The Side Chapel", "A room with small chapels off the main hall for quiet work.", "In this design breakout rooms are side chapels: small, quiet, and separate, where two or three people can work without disturbing the hall. Each chapel has its own board, and the work is carried back to the hall when it is done. The design suits groups that need quiet corners inside a busy room.", {"chapels": 3, "boards": 3, "returns": 36, "disturbances": 0}], ["The Market of Files", "A room where shared files are goods on market stalls.", "In this design shared files are goods on stalls: each file is laid out where all can see it, with its owner's name on a card, and anyone may pick it up and look -- but the original stays on the stall. The design suits rooms where files are passed around and must never be lost or changed by looking.", {"stalls": 48, "owner_cards": 48, "originals_lost": 0, "goods_filed": 48}], ["The Rest Garden", "A room with a garden for breaks, built into the session.", "In this design the room has a garden: every hour the group steps into it, rests, and returns. The garden has no work in it -- no boards, no objects -- only quiet. The design suits rooms whose sessions are long and whose people need rest to keep working well.", {"gardens": 1, "bells_rung": 12, "benches": 8, "rests_taken": 12}], ["The Metronome", "A room that keeps time like a metronome so no one sees a different room.", "In this design sync is a metronome: it ticks, and every person's room moves on the tick. When the network cannot keep the beat, the metronome slows and everyone slows together, so no one sees a different room. The design suits rooms on slow networks where a split room is the worst failure.", {"beats_per_second": 7, "slowings": 5, "split_rooms": 0, "metronomes": 1}], ["The Pattern Book", "A room library where every good room is a pattern in a book.", "In this design templates are patterns in a book: each good room is drawn as a pattern, with notes on what it suits, and a group may copy a pattern and change it. The book is kept by the librarian, who retires patterns nobody uses. The design suits groups that meet often and want to start from what worked.", {"patterns": 12, "copies": 96, "retirements": 2, "librarians": 1}], ["The Mirror of the Group", "A room with a mirror that shows the group how it worked.", "In this design the collaboration score is a mirror: after the session the group looks into it and sees who spoke, who drew, and what was decided -- as a pattern, never as blame. The group decides what to change. The design suits groups that want to get better together and will not use a score to punish.", {"mirrors": 1, "patterns_shown": 12, "changes_chosen": 9, "blame_events": 0}], ["The Far Window", "A room with a window through which a far expert looks in.", "In this design the remote expert looks through a window: the worker opens it, the expert sees what the worker sees, and the expert's marks appear on the glass. The worker may close the window at any time. The design suits work where an expert's eye is needed but the expert cannot travel.", {"windows": 1, "marks_drawn": 240, "marks_accepted": 228, "closures_by_worker": 18}], ["The Pin Board", "A room where every thought is pinned to the thing it is about.", "In this design annotations are pins on a board: each note is pinned to the thing it concerns, with its author's name on the pin, and an unanswered pin stays visible until it is answered. The design suits rooms where thoughts are easily lost and must stay attached to their subject.", {"pins": 320, "answered": 288, "open_pins": 32, "boards": 1}], ["The Sleeping Room", "A room that sleeps when the group leaves and wakes exactly as it was.", "In this design persistence is sleep: when the group leaves, the room sleeps, and when they return it wakes with everything where it was -- the boards, the objects, the notes. The room is never tidied in its sleep. The design suits groups whose work spans many sessions and must never be lost between them.", {"rooms_sleeping": 12, "wakings": 12, "things_lost": 0, "weekly_tests": 52}], ["The Open Door", "A room built so anyone can enter, whatever their body or senses.", "In this design accessibility is an open door: captions, spoken descriptions, seated places, and one-hand controls are built into the room from the start, not added later. The door is wide enough for everyone. The design suits rooms that must welcome anyone who is invited.", {"door_width_cm": 120, "caption_coverage": 100, "seated_places": 8, "control_modes": 3}], ["The Map Table", "A room where a small map on the table shows every room and door.", "In this design navigation is a map on the table: every room is drawn on it, every door is marked, and a person touches a room to go there. The way back is always the same touch. The design suits people who move between many rooms and must never get lost.", {"rooms_mapped": 12, "doors_marked": 12, "moves": 96, "lost_persons": 0}], ["The Post Box", "A room where decisions are posted into the task list like letters.", "In this design integration is a post box: decisions are written as letters during the session and posted into the task list when it ends. Only marked decisions are posted; remarks stay in the room. The design suits groups whose meetings must turn into work, not just talk.", {"letters_posted": 84, "remarks_posted": 0, "tasks_filed": 84, "post_boxes": 1}], ["The Measured Hall", "A room that knows its own size and says so plainly.", "In this design the platform's limits are written on the hall's wall: how many people, how many objects, how many rooms -- and what happens when the hall is full. The writing is large and no one can miss it. The design suits platforms whose users would rather be told no than be silently dropped.", {"people_limit": 8, "objects_limit": 100, "rooms_limit": 50, "silent_drops": 0}]];

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
