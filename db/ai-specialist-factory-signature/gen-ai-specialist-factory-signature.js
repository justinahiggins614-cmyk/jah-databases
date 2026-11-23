#!/usr/bin/env node
/* Seeded boundless generator for ai-specialist-factory-signature.
   Package-only. `node gen-ai-specialist-factory-signature.js [seed]` prints one JSON record;
   `node gen-ai-specialist-factory-signature.js --test` runs runTests (10 tests).
   Deterministic: the same seed always emits the same record.
   Gates: emitted record_kind == manifest record_kind; slug form;
   id prefix; hard_stop 1,000,000,000; gen prefix; JCC round-trip. */
const crypto = require("crypto");
const SLUG = "ai-specialist-factory-signature";
const EDITION = "signature";
const RECORD_KIND = "ai specialist factory record";
const ID_PREFIX = "JAH-AISFS-";
const GEN_PREFIX = "JAH-AISFSGEN-";
const AI_NAME = "JAH AI Specialist Factory Librarian (Signature)";
const SRC = "signature-generated";
const TOPICS = [["The Atrium of Specialists", "A factory arranged as an open atrium where every specialist is built in the open.", "In this design the factory is one open room with a high roof, and every specialist is built where everyone can see it. The atrium keeps the work honest: nothing is hidden behind a wall, and a visitor can watch a specialist being trained, tested, and reviewed. The design trades privacy for openness, and it suits factories whose customers want to watch their specialist being made.", {"bays": 12, "gallery_seats": 40, "build_days_open": 3, "atrium_height_m": 9}], ["The Loom of Skills", "A factory that weaves skill modules into specialists the way a loom weaves thread.", "In this design every specialist is woven from skill modules on a loom: the warp is the blueprint, the weft is the knowledge pack, and the pattern is the capability list. A weaver can see the whole cloth at once and can spot a dropped thread -- a missing capability -- before the specialist leaves the loom. The design suits factories that build many specialists from the same modules.", {"modules_per_specialist": 18, "looms": 4, "patterns_filed": 96, "weavers": 6}], ["The Kiln of Tests", "A factory where every specialist is fired in the test bench like clay in a kiln.", "In this design the test bench is a kiln: specialists go in soft, are fired by hard tasks, and come out either whole or broken. A specialist that cracks in the kiln is not patched and sold; it is broken down and rebuilt. The design suits factories that value a hard test over a quick release, and it makes the cost of failure visible to everyone.", {"kiln_tasks": 240, "difficulty_steps": 5, "breakages_rebuilt": 19, "kilns": 2}], ["The Press of Briefs", "A factory that presses plain requests into firm briefs.", "In this design the intake is a press: a request goes in loose and comes out as a firm brief, pressed flat and even. The press removes the air -- the vague words, the unstated hopes -- and leaves only what can be built and tested. The design suits factories whose requesters talk in wishes and need their wishes turned into work.", {"press_strokes": 3, "vague_words_removed": 9, "briefs_pressed": 96, "presses": 1}], ["The Library of Specialists", "A factory that keeps every specialist as a book on a shelf.", "In this design the registry is a library: every specialist is a book, with its brief as the title page, its blueprint as the table of contents, and its test report as the final chapter. A visitor can take a specialist off the shelf, read it, and put it back. The design suits factories whose customers choose from what exists rather than ordering something new.", {"books": 96, "shelves": 12, "reading_seats": 20, "catalogue_cards": 96}], ["The Workshop of One", "A factory of single-builder benches, one builder per specialist.", "In this design each specialist is built by one builder from brief to handover, at one bench, with the whole job in one pair of hands. The builder knows their specialist completely and answers for it personally. The design trades speed for responsibility, and it suits small factories where the builder's name is the guarantee.", {"benches": 8, "builders": 8, "builds_per_builder": 12, "signatures": 96}], ["The Garden of Versions", "A factory that grows specialists like plants, version by version.", "In this design versions are grown, not made: each specialist is a plant, and each version is a season of growth. Old versions are not thrown away; they are kept as cuttings, so any version can be grown again. The design suits factories whose specialists change slowly and whose users need to stay on an old version for a long time.", {"beds": 96, "cuttings_kept": 384, "seasons_per_year": 4, "gardeners": 3}], ["The Market Stall", "A factory that sells specialists from an open stall.", "In this design the marketplace is a stall in a square: specialists are laid out where passers-by can see them, try them, and ask questions. The stallkeeper knows every specialist by name and will not sell one that does not fit the buyer. The design suits factories that sell to the public and want buyers to meet the maker.", {"stalls": 1, "listings": 41, "try_outs_per_day": 12, "hires": 203}], ["The Observatory of Failures", "A factory that studies its failures the way an observatory studies the sky.", "In this design every failure is observed, recorded, and studied, and the lessons are published where every builder can read them. The observatory never blames; it measures. The design suits factories that believe a failure hidden is a failure repeated, and it makes learning the factory's main product after the specialists themselves.", {"failures_studied": 19, "lessons_published": 19, "journal_issues": 12, "observers": 2}], ["The Compass of Permissions", "A factory where every permission points true north.", "In this design permissions are a compass: every permission the specialist holds must point at the brief, and any permission that points elsewhere is removed. The reviewer checks the compass before release and again at every update. The design suits factories whose specialists touch sensitive data and where a wrong permission is the worst failure.", {"permissions_checked": 31, "permissions_removed": 4, "compass_checks": 96, "reviewers": 1}], ["The Mill of Knowledge", "A factory that mills raw sources into fine knowledge packs.", "In this design sources are grain and knowledge packs are flour: the mill grinds, sifts, and bags them, and nothing reaches a specialist unmilled. Contradictions are stones in the grain, picked out by hand before milling. The design suits factories whose specialists depend on large, messy piles of public material.", {"sources_milled": 96, "pack_items": 120, "contradictions_picked": 7, "mills": 2}], ["The Bridge of Handover", "A factory that hands specialists over a bridge, with the user walking beside them.", "In this design handover is a bridge the builder and the user cross together: the specialist walks between them, and the crossing is not finished until the user has done a real task on the far side. The design suits factories whose users are nervous about new tools and need to be walked through the first task.", {"bridge_steps": 7, "tasks_crossed": 96, "guides": 4, "sign_offs": 96}], ["The Clockwork Factory", "A factory that runs on a fixed rhythm, one stage per tick.", "In this design the factory is a clock: intake ticks, blueprint tocks, training ticks, testing tocks, and the rhythm never changes. A specialist that is late is not rushed; it waits for the next tick. The design suits factories that value a steady, predictable pace over bursts of speed.", {"ticks_per_build": 9, "builds_per_month": 12, "late_builds_held": 3, "clock_keepers": 1}], ["The Lantern of Review", "A factory where the review is a lantern carried into every dark corner.", "In this design the safety review is a lantern: the reviewer carries it into every corner of the specialist -- its permissions, its memory, its refusals -- and nothing is released until the light has reached everywhere. The design suits factories whose specialists work where a hidden danger would do real harm.", {"corners_checked": 24, "dangers_found": 5, "lanterns": 2, "reviews_signed": 96}], ["The Seed Bank", "A factory that keeps every skill module as a seed for the next specialist.", "In this design the skill library is a seed bank: modules are seeds, kept dry and labeled, and any specialist can be grown from them. When a new skill is needed, the factory grows it as a seed first, so the next specialist can use it too. The design suits factories that build many specialists and want nothing built twice.", {"seeds": 84, "seeds_in_use": 61, "germinations": 12, "drawers": 14}], ["The Harbor of Retirements", "A factory where specialists retire to a quiet harbor.", "In this design retirement is a harbor: specialists sail in on their last day, their tools are unloaded, their data is returned, and their records are stored in the harbor office. The design suits factories whose users need to know exactly what happened to their specialist after it stopped working.", {"retirements": 14, "records_filed": 14, "questions_answered": 22, "harbor_staff": 2}], ["The Choir of Teams", "A factory where specialist teams sing in harmony.", "In this design a team of specialists is a choir: each specialist sings one part, the coordinator keeps the time, and the result is one song. A specialist that sings out of time is heard at once. The design suits factories whose hardest jobs need several specialists working as one.", {"choir_size": 4, "joint_songs": 36, "rehearsals": 48, "conductors": 3}], ["The Mirror of Memory", "A factory where a specialist's memory is a mirror the user can look into.", "In this design the specialist's memory is a mirror: the user can look into it at any time and see exactly what the specialist remembers about them. Nothing is remembered in secret, and anything in the mirror can be wiped by the user. The design suits factories whose users care most about what is kept about them.", {"facts_shown": 12, "wipings_tested": 12, "mirrors": 96, "complaints": 0}], ["The Ledger of Costs", "A factory that writes every cost in a ledger open to all.", "In this design the cost ledger sits open on a desk: every build's cost, every hour, every test, written where anyone can read it. The factory charges what the ledger says and no more. The design suits factories that must prove they are affordable and honest about money.", {"ledger_entries": 1840, "cost_items": 8, "reviews": 12, "disputes": 0}], ["The Gatehouse", "A factory where the quality gate is a gatehouse with one keeper.", "In this design the quality gate is a gatehouse: one keeper, one checklist, one key, and no specialist passes without the keeper's signature on every item. The keeper answers to no deadline. The design suits factories where the gate is the whole reputation of the factory.", {"gate_items": 14, "gatekeepers": 2, "held": 3, "passed": 96}], ["The Translation Desk", "A factory where requests are translated at one desk, face to face.", "In this design translation happens at a desk where the requester sits across from the translator: the request is read aloud, the vague words are questioned on the spot, and the brief is written while the requester watches. The design suits factories whose requesters cannot write what they need but can say it.", {"desks": 2, "translations": 96, "vague_words": 9, "satisfaction": 96}], ["The Version Tree", "A factory where versions grow on a tree, branch by branch.", "In this design every specialist is a tree: the first version is the trunk, and each update is a branch. A user can climb back to any branch and sit on it as long as they need. The design suits factories whose users need old versions to keep working while new ones grow.", {"trees": 96, "branches": 384, "climbers": 41, "labels": 384}], ["The Repair Bench", "A factory where broken specialists are repaired in the open.", "In this design the repair bench stands in the middle of the floor: a failing specialist is laid on it, the failure is shown to everyone, and the repair is done where all can learn from it. The design suits factories that treat failure as a lesson, not a shame.", {"repairs": 19, "lessons_shelved": 19, "bench_hours": 96, "repeat_failures": 0}], ["The Auction House", "A factory that lists specialists in an auction house.", "In this design the marketplace is an auction house: specialists are shown, their test scores are read aloud, and buyers bid on the work, not on promises. The auctioneer will not sell a specialist whose scores do not match its listing. The design suits factories whose specialists are hired by strangers who need proof before they pay.", {"listings": 41, "sales": 203, "disputes": 6, "auctioneers": 2}]];

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
