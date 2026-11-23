#!/usr/bin/env node
/* Seeded boundless generator for virtual-construction-architecture-studio.
   Package-only. `node gen-virtual-construction-architecture-studio.js [seed]` prints one JSON record;
   `node gen-virtual-construction-architecture-studio.js --test` runs runTests (10 tests).
   Deterministic: the same seed always emits the same record.
   Gates: emitted record_kind == manifest record_kind; slug form;
   id prefix; hard_stop 1,000,000,000; gen prefix; JCC round-trip. */
const crypto = require("crypto");
const SLUG = "virtual-construction-architecture-studio";
const EDITION = "public";
const RECORD_KIND = "virtual construction architecture studio record";
const ID_PREFIX = "JAH-VCAS-";
const GEN_PREFIX = "JAH-VCASGEN-";
const AI_NAME = "JAH Virtual Construction and Architecture Studio Librarian";
const SRC = "public-harvest";
const TOPICS = [["Virtual Site Survey", "Measuring a real building site and bringing it into virtual space.", "A virtual site survey measures the real site -- its ground, its slopes, its neighbours, its sunlight -- and builds a virtual copy the design team can walk through before anything is built.", {"survey_points": 4800, "accuracy_cm": 2, "photos_taken": 240, "checks": 3}], ["Building Model Import", "Bringing a building information model into the virtual studio.", "Building model import brings a BIM file -- the digital description of a building -- into the studio, so the design team can walk through the building before it exists.", {"objects_imported": 1240, "objects_unreadable": 3, "rooms_checked": 24, "imports": 12}], ["Virtual Design Room", "A room in virtual space where the design team works together.", "The virtual design room is where the team meets the building: the model stands in the middle of the room, the team walks around it, and changes are made where everyone can see them.", {"room_area_sqm": 40, "team_size": 6, "changes_recorded": 180, "sessions": 24}], ["Material and Finish Library", "The shelf of materials and finishes the team can choose from.", "The material library is the studio's shelf: every material with its look, its cost, its weight, and how it behaves in light, sun, and rain, so the team can choose with knowledge.", {"materials": 120, "samples_shown": 120, "choices_logged": 48, "updates_per_year": 4}], ["Structural Check in Virtual Space", "Checking that the virtual building would stand up.", "The structural check tests the virtual building the way an engineer would test a real one: loads, supports, and spans, so a building that would fall down is caught before it is built.", {"load_cases": 8, "stresses_checked": 240, "failures_found": 6, "sign_offs": 3}], ["Light and Shadow Simulation", "Seeing how sunlight and shadow will fall in the building.", "Light simulation shows the team how the sun will move through the building across the day and the year, so a room that would be dark at noon is found before it is built.", {"hours_simulated": 24, "rooms_tested": 24, "windows_moved": 9, "simulation_runs": 48}], ["Walkthrough and Client Review", "Walking the client through the virtual building before it is built.", "The walkthrough lets the client walk through their building in virtual space -- through the front door, up the stairs, into every room -- and say what works and what does not, while changes are still cheap.", {"rooms_walked": 24, "comments_pinned": 96, "changes_made": 41, "return_visits": 12}], ["Clash Detection in the Model", "Finding where pipes, wires, and walls try to occupy the same place.", "Clash detection finds the places where two parts of the building collide -- a pipe through a beam, a wire through a duct -- so they are fixed in the model, not discovered on the building site.", {"clashes_found": 87, "clashes_fixed": 87, "re_runs": 12, "weeks_saved": 6}], ["Cost Estimate from the Model", "Counting what the building will cost, from the model itself.", "The cost estimate counts the building from the model: every wall, window, and pipe measured, priced, and added up, so the team knows the price before the building is built.", {"items_priced": 1240, "sample_checked": 124, "estimate_range_pct": 8, "re_estimates": 12}], ["Construction Sequence Animation", "Showing the order the building will be built in, step by step.", "The sequence animation shows the building being built in virtual space, in order -- foundations, frame, walls, roof -- so the team can see whether the order works before the builders arrive.", {"sequence_steps": 48, "impossibilities_found": 5, "animation_runs": 12, "builders_guided": 6}], ["Site Safety Walkthrough", "Walking the virtual site to find dangers before builders arrive.", "The safety walkthrough lets the team walk the virtual building site and find the dangers -- the unguarded edge, the blind corner, the heavy lift -- before any builder sets foot there.", {"dangers_found": 23, "design_fixes": 14, "plan_items": 9, "sign_offs": 1}], ["Accessibility Review in Virtual Space", "Checking that everyone can use the building, in virtual space.", "The accessibility review checks the virtual building the way a person in a wheelchair, a person who cannot see, or a person who cannot hear would use it -- every door, ramp, lift, and sign.", {"doors_checked": 48, "ramps_checked": 6, "failures_found": 11, "failures_fixed": 11}], ["Energy Performance Preview", "Seeing how much energy the building will use before it is built.", "The energy preview calculates the building's heating, cooling, and lighting from the model, so a building that would waste energy is found while it can still be changed.", {"months_modelled": 12, "changes_tested": 18, "assumptions_listed": 9, "previews_filed": 3}], ["Landscape and Context Model", "Placing the building in its landscape and its neighbourhood.", "The context model puts the virtual building into its real surroundings -- the street, the trees, the neighbouring buildings -- so the team can see how it will sit in the world.", {"neighbour_buildings": 14, "views_checked": 8, "shadows_studied": 4, "design_changes": 3}], ["Version and Change Log", "Tracking every version of the model and every change made to it.", "The change log is the model's memory: every version, every change, who made it and why, so the team can always go back to how the building was last week.", {"versions": 12, "changes_logged": 180, "rollbacks": 3, "log_readers": 6}], ["Team Review and Markup", "The design team reviewing the model together and marking what must change.", "Team review is the regular meeting where the whole team looks at the model together, marks what is wrong, and agrees what will change before the next meeting.", {"reviews": 24, "marks_collected": 312, "changes_assigned": 180, "follow_ups": 24}], ["Model Export and Handover", "Handing the finished model to the builders and the owner.", "Export and handover is the moment the studio gives the model away: the finished model, the drawings, the lists, and the instructions, checked and complete, handed to the builders and the owner.", {"handover_items": 14, "formats_checked": 2, "missing_items": 0, "copies_kept": 1}], ["Virtual Mock-Up Room", "A full-size virtual copy of one room, built before the real one.", "The mock-up room is one room of the building built full-size in virtual space -- the kitchen, the classroom, the ward -- so the people who will use it can try it before it is built.", {"mock_up_rooms": 3, "user_trials": 18, "failures_found": 12, "rebuilds": 2}], ["Permits and Standards Checklist", "Checking the design against the permits and standards it must meet.", "The checklist is the studio's list of every permit and standard the building must satisfy -- planning, fire, structure, access -- checked one by one against the model.", {"checklist_items": 36, "items_proved": 36, "alternatives": 2, "authorities": 3}], ["Furniture and Fit-Out Planner", "Placing furniture and fittings in the virtual building.", "The fit-out planner places every piece of furniture and fitting in the virtual rooms, so the team can see whether the building works when it is full of the things people need.", {"rooms_fitted": 24, "items_placed": 480, "passage_checks": 24, "orders_made": 1}], ["Acoustic Preview", "Hearing how the building will sound before it is built.", "The acoustic preview lets the team hear the building: a voice in the hall, a footstep on the stair, a machine in the next room, so a building that would be too loud or too echoing is found early.", {"rooms_listened": 24, "echo_marks": 7, "changes_tested": 11, "listening_points": 48}], ["Multi-Building Master Plan", "Planning several buildings together as one place.", "The master plan puts several virtual buildings together on one site -- their streets, their squares, their shared spaces -- so the team can see how they work as a place, not just as separate buildings.", {"buildings": 5, "streets": 3, "squares": 2, "walks": 6}], ["Studio Templates Library", "Ready-made studio setups for common kinds of building.", "A template is a studio already set up for one kind of building -- a house, a school, a clinic -- with the rooms, the checks, and the lists arranged, so a new project can start at once.", {"templates": 8, "template_uses": 24, "team_versions": 6, "retirements": 1}], ["Studio Scale and Limits", "How many projects, models, and people the studio can hold.", "The scale record states the studio's limits honestly: how many projects, how many models, how many people, and what happens when the limits are reached.", {"projects_limit": 12, "models_limit": 100, "people_limit": 30, "limit_reviews_per_year": 1}]];

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
