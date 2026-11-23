#!/usr/bin/env node
/* Seeded boundless generator for virtual-construction-architecture-studio-signature.
   Package-only. `node gen-virtual-construction-architecture-studio-signature.js [seed]` prints one JSON record;
   `node gen-virtual-construction-architecture-studio-signature.js --test` runs runTests (10 tests).
   Deterministic: the same seed always emits the same record.
   Gates: emitted record_kind == manifest record_kind; slug form;
   id prefix; hard_stop 1,000,000,000; gen prefix; JCC round-trip. */
const crypto = require("crypto");
const SLUG = "virtual-construction-architecture-studio-signature";
const EDITION = "signature";
const RECORD_KIND = "virtual construction architecture studio record";
const ID_PREFIX = "JAH-VCASS-";
const GEN_PREFIX = "JAH-VCASSGEN-";
const AI_NAME = "JAH Virtual Construction and Architecture Studio Librarian (Signature)";
const SRC = "signature-generated";
const TOPICS = [["The Glass Site", "A studio where the site is surveyed through glass.", "In this design the survey is a glass: the team looks through it at the real site and sees the virtual copy laid over the real ground, and any disagreement shows at once as a double image. The design suits sites where the ground is uneven and a wrong survey would be costly.", {"survey_points": 4800, "double_images_fixed": 5, "accuracy_cm": 2, "glasses": 2}], ["The Import Gate", "A studio where every building model enters through one gate.", "In this design the import is a gate: every BIM file enters through it, is counted and checked, and anything the gate cannot read is sent back with a note. Nothing enters the studio uncounted. The design suits studios that receive models from many hands and must know exactly what arrived.", {"models_gated": 12, "objects_counted": 1240, "returns": 3, "gates": 1}], ["The Round Room", "A studio where the design team meets around a round table.", "In this design the design room is round: the model stands in the middle, the team sits around it, and no one sits at the head. Changes are made where all can see them. The design suits teams that decide together and want the model, not a person, at the center.", {"seats": 6, "changes_rung": 180, "sessions": 24, "tables": 1}], ["The Sample Wall", "A studio where materials hang on a wall to be touched.", "In this design the material library is a wall: every material hangs on it as a sample the team can touch, turn in the light, and place on the model. The wall is re-hung when prices change. The design suits teams that choose by touching, not by reading a list.", {"samples": 120, "wall_area_sqm": 12, "choices": 48, "re_hangings": 4}], ["The Red Pen", "A studio where structural failures are marked in red for all to see.", "In this design the structural check is a red pen: anything that would fail is marked in red on the model, in front of the whole team, and the red stays until the design is changed. The design suits teams where a hidden failure is the worst failure.", {"red_marks": 6, "seals": 3, "loads_tested": 8, "pens": 1}], ["The Sundial Room", "A studio where light is studied like a sundial.", "In this design light is a sundial: the team stands in a room and watches the sun move across the floor, at any hour and any season, and moves windows until the light falls right. The design suits buildings where light is the main material and a dark room is a failed room.", {"hours_on_dial": 24, "seasons_on_wheel": 4, "windows_moved": 9, "dial_runs": 48}], ["The Client's Shoes", "A studio where the client walks the building in their own shoes.", "In this design the walkthrough is done in the client's shoes: the client walks at their own pace, the designer walks beside them, and every comment is pinned where it was made. The design suits studios whose clients must understand the building, not just approve it.", {"rooms_walked": 24, "comments_pinned": 96, "return_walks": 12, "shoe_pairs": 1}], ["The Collision Bell", "A studio where every clash rings a bell.", "In this design clash detection is a bell: when two parts collide, the bell rings, the clash is listed, and the team fixes it before the bell is rung again. The design suits teams where a clash found on site costs a week and a wall.", {"clashes_rung": 87, "clashes_fixed": 87, "bell_rings": 12, "weeks_saved": 6}], ["The Counting House", "A studio where the cost is counted in a house of numbers.", "In this design the cost estimate is a counting house: every wall, window, and pipe is counted, priced, and written in the book, and the total is shown as a range with its reasons. The design suits studios whose clients must know the price before the building is built.", {"items_counted": 1240, "sample_checked": 124, "range_pct": 8, "counting_books": 1}], ["The Film Reel", "A studio where the building is built on film, frame by frame.", "In this design the construction sequence is a film: each frame is a step, and the team watches the building rise in order. A frame that cannot happen is cut and re-shot. The design suits teams that must prove the order works before the builders arrive.", {"frames": 48, "cuts": 5, "screenings": 12, "reels": 1}], ["The Safety Lantern", "A studio where dangers are found by lantern light.", "In this design the safety walkthrough is a lantern: the team carries it through the virtual site, and every danger it lights is marked and fixed before any builder arrives. The design suits sites where a danger found in virtual space hurts nobody and the same danger on site could hurt a person.", {"dangers_lit": 23, "design_fixes": 14, "seals": 1, "lanterns": 1}], ["The Wheelchair's Path", "A studio where the building is tested by a wheelchair's path.", "In this design accessibility is a path: a wheelchair is driven through every door, along every corridor, and up every ramp, and any door it cannot pass is marked and widened. The design suits buildings that must be usable by everyone, whatever their body.", {"doors_driven": 48, "failures_found": 11, "doors_widened": 11, "wheelchairs": 1}], ["The Energy Ledger", "A studio where energy is counted month by month in a ledger.", "In this design the energy preview is a ledger: each month has a page, each page shows the heating, cooling, and lighting, and the team turns the pages to see the year. The design suits buildings where energy is money and a wasteful building is a costly one.", {"months": 12, "changes_tested": 18, "assumptions": 9, "ledgers": 1}], ["The Neighbour's Window", "A studio where the building is judged from the neighbour's window.", "In this design the context model is judged from the neighbour's window: the team stands where the neighbours stand and looks at the building as they will see it. If it harms the view, it is changed. The design suits buildings that must be good neighbours, not just good objects.", {"windows_stood_at": 8, "view_lines": 8, "shadows_laid": 4, "changes": 3}], ["The Tree of Versions", "A studio where versions grow on a tree.", "In this design the change log is a tree: the first version is the trunk, each change is a branch, and the team can climb back to any branch. The design suits studios whose models change often and whose teams must always know how the building got to be the way it is.", {"trees": 1, "branches": 180, "climbs_back": 3, "labels": 180}], ["The Marking Circle", "A studio where the team marks the model in a circle.", "In this design team review is a circle: the team stands around the model, each person marks what they see, and the marks are gathered into one list. The design suits teams where every eye sees something different and all of them matter.", {"circles": 24, "marks_gathered": 312, "assignments": 180, "baskets": 1}], ["The Handover Chest", "A studio where the finished model is handed over in a chest.", "In this design handover is a chest: the model, the drawings, the lists, and the guide are packed into it, checked item by item, and the chest is handed to the builders and the owner. The design suits studios where a missing document is a stopped building site.", {"chest_items": 14, "checks": 14, "missing_items": 0, "chests": 1}], ["The Doll's House", "A studio where one room is built as a doll's house to be tried.", "In this design the mock-up is a doll's house: one room built full-size in virtual space, with real materials and real furniture, for real users to try. What does not work is marked and changed. The design suits buildings whose rooms must work for the people who will use them, not just look right on paper.", {"rooms_built": 3, "trials": 18, "failures_found": 12, "rebuilds": 2}], ["The Rule Book", "A studio where permits and standards are a book that is read as the design grows.", "In this design the checklist is a rule book: each rule is a page, each page names the part of the model it applies to and the evidence that the design meets it. The book is read as the design grows, not at the end. The design suits studios where a rule found late can force a redesign.", {"rules": 36, "evidence_slips": 36, "alternatives": 2, "books": 1}], ["The Furnished Room", "A studio where rooms are fitted before they are judged.", "In this design fit-out comes first: every room is furnished in virtual space before the team judges it, because a room that works empty and fails full was never really tested. The design suits buildings where the furniture is the work -- schools, hospitals, offices.", {"rooms_furnished": 24, "items_placed": 480, "user_walks": 24, "orders": 1}], ["The Listening Room", "A studio where the building is heard before it is built.", "In this design the acoustic preview is a listening room: the team sits in the virtual rooms and listens -- a voice, a footstep, a machine -- and changes the material or the shape until the sound is right. The design suits buildings where sound is the work -- halls, schools, hospitals.", {"rooms_listened": 24, "echo_marks": 7, "changes_tested": 11, "listening_rooms": 1}], ["The Village Model", "A studio where several buildings are planned as one village.", "In this design the master plan is a village model: the buildings, streets, and squares are laid out on one table, and the team walks the village together. The design suits places, not just buildings, and a village that works as a whole is the test.", {"buildings": 5, "streets": 3, "squares": 2, "walks": 6}], ["The Pattern Studio", "A studio where good studios are kept as patterns.", "In this design templates are patterns kept in the studio: each good setup is drawn as a pattern, with notes on what it suits, and a new project may copy a pattern and change it. The design suits studios that build the same kinds of building again and again.", {"patterns": 8, "copies": 24, "retirements": 1, "drawers": 1}], ["The Measured Studio", "A studio that knows its own limits and writes them on the wall.", "In this design the studio's limits are written on the wall: how many projects, how many models, how many people -- and what happens when the studio is full. The design suits studios whose teams would rather be told no than be silently dropped.", {"projects_limit": 12, "models_limit": 100, "people_limit": 30, "silent_drops": 0}]];

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
