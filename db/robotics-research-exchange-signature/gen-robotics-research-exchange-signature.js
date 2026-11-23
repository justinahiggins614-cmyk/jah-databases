// Seeded boundless generator for the Robotics Research Exchange Database
// (signature edition). Deterministic: the same seed always emits the same
// record. Usage: node gen-robotics-research-exchange-signature.js [seed]  (prints one JSON record)
// or: node gen-robotics-research-exchange-signature.js --test (runTests).
// Package-only; outputs are generated, not stored files.
"use strict";
const crypto = require("crypto");

const SLUG = "robotics-research-exchange-signature";
const RECORD_KIND = "robotics research exchange record";
const ID_PREFIX = "JAH-RREX-S-";
const AI_NAME = "JAH Robotics Research Librarian (Signature)";
const EDITION = "signature";
const CEILING = "Generator ceiling: up to 1,000,000,000 scales per file, generated on demand by the file AI \u2014 not stored files.";

const TOPICS = [
  {
    "title": "The Early Draft Desk",
    "subject": "A Signature design for a desk where robotics papers appear months early.",
    "description": "The Early Draft Desk is a Signature design-study: A Signature design for a desk where robotics papers appear months early. The Early Draft Desk is a Signature-made design: a preprint desk where robotics papers appear months before formal review. Its novelty is a comment ledger that ties every reader comment to a line of the paper, so authors can answer in place. The Desk is meant for fast-moving fields where waiting for review means waiting too long. This is a Signature-made design, presented as a design study only, never as an established fact and never as a built product. The design is judge",
    "label": "robotics-research-exchange-signature-000001",
    "figures": {
      "robots": 0,
      "papers": 260,
      "months_early": 6,
      "comments": 20,
      "citations": 46,
      "success_pct": 95
    }
  },
  {
    "title": "The Society Hall",
    "subject": "A Signature design for a hall where the world's robotics researchers meet.",
    "description": "The Society Hall is a Signature design-study: A Signature design for a hall where the world's robotics researchers meet. The Society Hall is a Signature-made design: a hall that gathers the field's society, its committees and its conferences under one roof. Its novelty is a committee map that shows every niche topic and its people, so a newcomer can find their corner in an afternoon. The Hall is meant for a field that grows faster than its directories. This is a Signature-made design, presented as a design study only, never as an established fact and never as a built product. The design is jud",
    "label": "robotics-research-exchange-signature-000002",
    "figures": {
      "robots": 0,
      "members": 16000,
      "committees": 32,
      "conferences": 2,
      "journals": 4,
      "success_pct": 96
    }
  },
  {
    "title": "The Single Track",
    "subject": "A Signature design for a conference with one track, so everyone hears everything.",
    "description": "The Single Track is a Signature design-study: A Signature design for a conference with one track, so everyone hears everything. The Single Track is a Signature-made design: a conference where every talk is heard by every attendee, so the discussion is sharp. Its novelty is a debate hour after each session, where the audience argues the claim before the speaker leaves the room. The Track is meant for science that needs arguing, not just presenting. This is a Signature-made design, presented as a design study only, never as an established fact and never as a built product. The design is judged o",
    "label": "robotics-research-exchange-signature-000003",
    "figures": {
      "robots": 0,
      "papers": 130,
      "reviewers": 3,
      "accept_pct": 27,
      "workshops": 13,
      "success_pct": 94
    }
  },
  {
    "title": "The Big Hall",
    "subject": "A Signature design for the largest robotics gathering in the world.",
    "description": "The Big Hall is a Signature design-study: A Signature design for the largest robotics gathering in the world. The Big Hall is a Signature-made design: a gathering of thousands of robotics papers, people and machines in one place. Its novelty is a competition floor where student teams test their machines against each other in public. The Hall is meant for a field that needs to see the machines, not just read about them. This is a Signature-made design, presented as a design study only, never as an established fact and never as a built product. The design is judged on its own terms: whether its ",
    "label": "robotics-research-exchange-signature-000004",
    "figures": {
      "robots": 0,
      "papers": 1250,
      "attendees": 5200,
      "days": 5,
      "exhibitors": 85,
      "success_pct": 95
    }
  },
  {
    "title": "The Rotating Forum",
    "subject": "A Signature design for a forum that rotates between continents.",
    "description": "The Rotating Forum is a Signature design-study: A Signature design for a forum that rotates between continents. The Rotating Forum is a Signature-made design: a conference that moves between Asia, Europe and the Americas, so every region hosts in turn. Its novelty is a future forum where senior researchers debate where the field should go next. The Forum is meant for intelligent robots, which need many kinds of intelligence. This is a Signature-made design, presented as a design study only, never as an established fact and never as a built product. The design is judged on its own terms: whethe",
    "label": "robotics-research-exchange-signature-000005",
    "figures": {
      "robots": 0,
      "papers": 1150,
      "attendees": 4600,
      "days": 5,
      "regions": 3,
      "success_pct": 95
    }
  },
  {
    "title": "The Shared Shelf",
    "subject": "A Signature design for a shelf of open datasets every lab can test on.",
    "description": "The Shared Shelf is a Signature design-study: A Signature design for a shelf of open datasets every lab can test on. The Shared Shelf is a Signature-made design: a shelf of open datasets, labelled and public, so every lab tests on the same data. Its novelty is a weakness flag: when an algorithm passes one dataset and fails another, the shelf flags that it learned the dataset, not the task. The Shelf is meant for fair comparison, which is the only kind that counts. This is a Signature-made design, presented as a design study only, never as an established fact and never as a built product. The d",
    "label": "robotics-research-exchange-signature-000006",
    "figures": {
      "robots": 0,
      "datasets": 26,
      "records": 16000,
      "labels": 8,
      "splits": 3,
      "success_pct": 94
    }
  },
  {
    "title": "The Scoreboard",
    "subject": "A Signature design for a public scoreboard that ranks robot algorithms fairly.",
    "description": "The Scoreboard is a Signature design-study: A Signature design for a public scoreboard that ranks robot algorithms fairly. The Scoreboard is a Signature-made design: a public scoreboard for robot algorithms, run by an independent party on fixed tasks. Its novelty is a rotation rule that changes the task every year, so no team can tune itself to one test forever. The Scoreboard is meant for progress you can see. This is a Signature-made design, presented as a design study only, never as an established fact and never as a built product. The design is judged on its own terms: whether its rules ar",
    "label": "robotics-research-exchange-signature-000007",
    "figures": {
      "robots": 0,
      "benchmarks": 13,
      "entries": 64,
      "tasks": 9,
      "scores": 64,
      "success_pct": 93
    }
  },
  {
    "title": "The Repeat Bench",
    "subject": "A Signature design for a bench that repeats published robot results.",
    "description": "The Repeat Bench is a Signature design-study: A Signature design for a bench that repeats published robot results. The Repeat Bench is a Signature-made design: a bench that repeats published experiments with the same code, data and hardware. Its novelty is a badge for papers whose results were repeated, so readers can trust the badge at a glance. The Bench is meant for a field where a result nobody can repeat is a rumour. This is a Signature-made design, presented as a design study only, never as an established fact and never as a built product. The design is judged on its own terms: whether i",
    "label": "robotics-research-exchange-signature-000008",
    "figures": {
      "robots": 0,
      "papers": 54,
      "repeated": 41,
      "code_shared": 47,
      "badges": 13,
      "success_pct": 93
    }
  },
  {
    "title": "The Virtual Proving Ground",
    "subject": "A Signature design for proving robot algorithms in simulation first.",
    "description": "The Virtual Proving Ground is a Signature design-study: A Signature design for proving robot algorithms in simulation first. The Virtual Proving Ground is a Signature-made design: a virtual world where robot algorithms are tested thousands of times before touching hardware. Its novelty is a reality-gap meter that measures how far simulation results drift from real-robot results. The Ground is meant for learning methods that need trials no real robot can survive. This is a Signature-made design, presented as a design study only, never as an established fact and never as a built product. The des",
    "label": "robotics-research-exchange-signature-000009",
    "figures": {
      "robots": 0,
      "simulators": 4,
      "trials": 1100,
      "gap_pct": 11,
      "benchmarks": 9,
      "success_pct": 94
    }
  },
  {
    "title": "The Open Workbench",
    "subject": "A Signature design for a workbench of open robot designs anyone can build.",
    "description": "The Open Workbench is a Signature design-study: A Signature design for a workbench of open robot designs anyone can build. The Open Workbench is a Signature-made design: a workbench of open robot designs with drawings, parts lists and software. Its novelty is a change log that records every builder's improvement, so the design gets better with every build. The Workbench is meant for students and small labs that cannot afford closed machines. This is a Signature-made design, presented as a design study only, never as an established fact and never as a built product. The design is judged on its ",
    "label": "robotics-research-exchange-signature-000010",
    "figures": {
      "robots": 0,
      "designs": 20,
      "parts": 260,
      "builds": 64,
      "cost_usd": 340,
      "success_pct": 93
    }
  },
  {
    "title": "The Goal Post",
    "subject": "A Signature design for a football pitch where robot teams push research forward.",
    "description": "The Goal Post is a Signature design-study: A Signature design for a football pitch where robot teams push research forward. The Goal Post is a Signature-made design: a football competition for robot teams, with the stated goal of beating the human champions by 2050. Its novelty is a rulebook that changes every year, so the competition never goes stale. The Post is meant for research that needs perception, planning, teamwork and speed all at once. This is a Signature-made design, presented as a design study only, never as an established fact and never as a built product. The design is judged on",
    "label": "robotics-research-exchange-signature-000011",
    "figures": {
      "robots": 11,
      "teams": 42,
      "goals": 14,
      "matches": 9,
      "leagues": 5,
      "success_pct": 94
    }
  },
  {
    "title": "The Disaster Course",
    "subject": "A Signature design for a disaster course that tests robots like real emergencies do.",
    "description": "The Disaster Course is a Signature design-study: A Signature design for a disaster course that tests robots like real emergencies do. The Disaster Course is a Signature-made design: a course of eight tasks drawn from real disasters, from driving to turning valves. Its novelty is a fall-and-recover test: a robot that falls must get up without human help or lose the run. The Course is meant for robots that must work where people should not go. This is a Signature-made design, presented as a design study only, never as an established fact and never as a built product. The design is judged on its ",
    "label": "robotics-research-exchange-signature-000012",
    "figures": {
      "robots": 0,
      "teams": 26,
      "tasks": 8,
      "finalists": 12,
      "falls": 5,
      "success_pct": 92
    }
  },
  {
    "title": "The Long Paper Room",
    "subject": "A Signature design for a room where the longest, most careful robotics papers are read.",
    "description": "The Long Paper Room is a Signature design-study: A Signature design for a room where the longest, most careful robotics papers are read. The Long Paper Room is a Signature-made design: a journal room for long papers with full proofs and full experiments. Its novelty is a predecessor rule: every paper must cite its predecessors fairly, so the record stays honest. The Room is meant for work that must last, not just impress. This is a Signature-made design, presented as a design study only, never as an established fact and never as a built product. The design is judged on its own terms: whether i",
    "label": "robotics-research-exchange-signature-000013",
    "figures": {
      "robots": 0,
      "papers": 64,
      "review_months": 6,
      "accept_pct": 21,
      "citations": 190,
      "success_pct": 94
    }
  },
  {
    "title": "The Wide Lens",
    "subject": "A Signature design for a journal that shows robotics to the whole of science.",
    "description": "The Wide Lens is a Signature design-study: A Signature design for a journal that shows robotics to the whole of science. The Wide Lens is a Signature-made design: a journal that publishes robotics with impact beyond robotics, written for scientists in other fields. Its novelty is a plain-words rule: every paper must explain why it matters outside the lab. The Lens is meant for work that changes more than one field. This is a Signature-made design, presented as a design study only, never as an established fact and never as a built product. The design is judged on its own terms: whether its rule",
    "label": "robotics-research-exchange-signature-000014",
    "figures": {
      "robots": 0,
      "papers": 50,
      "fields": 8,
      "reviewers": 4,
      "citations": 250,
      "success_pct": 94
    }
  },
  {
    "title": "The Conscience Table",
    "subject": "A Signature design for a table where the moral questions of robots are argued.",
    "description": "The Conscience Table is a Signature design-study: A Signature design for a table where the moral questions of robots are argued. The Conscience Table is a Signature-made design: a table where engineers, philosophers and lawyers argue what robots should and should not do. Its novelty is a responsibility map that assigns every harm a possible bearer, so no harm is left ownerless. The Table is meant for decisions that shape standards and laws. This is a Signature-made design, presented as a design study only, never as an established fact and never as a built product. The design is judged on its o",
    "label": "robotics-research-exchange-signature-000015",
    "figures": {
      "robots": 0,
      "papers": 38,
      "questions": 13,
      "standards": 5,
      "debates": 9,
      "success_pct": 93
    }
  },
  {
    "title": "The Classroom Kit",
    "subject": "A Signature design for a kit that lets any teacher teach robotics.",
    "description": "The Classroom Kit is a Signature design-study: A Signature design for a kit that lets any teacher teach robotics. The Classroom Kit is a Signature-made design: a kit of courses, labs and cheap robots for teaching robotics anywhere. Its novelty is a teacher's guide for fixing robots and debugging code, since a course is only as good as its teacher. The Kit is meant for schools that never had robotics before. This is a Signature-made design, presented as a design study only, never as an established fact and never as a built product. The design is judged on its own terms: whether its rules are cl",
    "label": "robotics-research-exchange-signature-000016",
    "figures": {
      "robots": 0,
      "courses": 22,
      "students": 850,
      "labs": 44,
      "kits": 130,
      "success_pct": 95
    }
  },
  {
    "title": "The Driving Library",
    "subject": "A Signature design for a library of driving recordings every car researcher can use.",
    "description": "The Driving Library is a Signature design-study: A Signature design for a library of driving recordings every car researcher can use. The Driving Library is a Signature-made design: a library of camera and lidar recordings from a car driving through a city, with labelled benchmarks. Its novelty is a leaderboard that never closes, so a new method can be scored against every published method at any time. The Library is meant for perception research that needs honest comparison. This is a Signature-made design, presented as a design study only, never as an established fact and never as a built pr",
    "label": "robotics-research-exchange-signature-000017",
    "figures": {
      "robots": 0,
      "images": 16000,
      "lidar_scans": 16000,
      "benchmarks": 8,
      "methods": 210,
      "success_pct": 94
    }
  },
  {
    "title": "The Show-Me Bench",
    "subject": "A Signature design for a bench where robots learn by watching a person work.",
    "description": "The Show-Me Bench is a Signature design-study: A Signature design for a bench where robots learn by watching a person work. The Show-Me Bench is a Signature-made design: a bench where a person performs a task and the robot learns to repeat it. Its novelty is a mistake filter that removes clumsy moments from the demonstration before the robot learns them. The Bench is meant for tasks that are easy to show and hard to program. This is a Signature-made design, presented as a design study only, never as an established fact and never as a built product. The design is judged on its own terms: whethe",
    "label": "robotics-research-exchange-signature-000018",
    "figures": {
      "robots": 0,
      "demos": 26,
      "tasks": 6,
      "trials": 130,
      "success_trials": 118,
      "success_pct": 94
    }
  },
  {
    "title": "The Shared Wheel",
    "subject": "A Signature design for a wheel that blends human and robot control.",
    "description": "The Shared Wheel is a Signature design-study: A Signature design for a wheel that blends human and robot control. The Shared Wheel is a Signature-made design: a controller that blends a person's input with a robot's help on one machine. Its novelty is a help dial the user can turn, so the robot helps more when the task is hard and less when the person wants control. The Wheel is meant for wheelchairs, arms and tools where full autonomy is not wanted. This is a Signature-made design, presented as a design study only, never as an established fact and never as a built product. The design is judge",
    "label": "robotics-research-exchange-signature-000019",
    "figures": {
      "robots": 0,
      "users": 32,
      "tasks": 5,
      "trials": 160,
      "satisfaction": 89,
      "success_pct": 93
    }
  },
  {
    "title": "The Safe Cell",
    "subject": "A Signature design for a robot cell where every hazard has a named control.",
    "description": "The Safe Cell is a Signature design-study: A Signature design for a robot cell where every hazard has a named control. The Safe Cell is a Signature-made design: a robot cell where every hazard is listed and every hazard has a guard, a sensor or a procedure. Its novelty is a risk card on the cell door, so anyone entering can read the hazards at a glance. The Cell is meant for factories where robots and people share the floor. This is a Signature-made design, presented as a design study only, never as an established fact and never as a built product. The design is judged on its own terms: whethe",
    "label": "robotics-research-exchange-signature-000020",
    "figures": {
      "robots": 0,
      "standards": 6,
      "hazards": 15,
      "controls": 15,
      "tests": 44,
      "success_pct": 96
    }
  },
  {
    "title": "The Gentle Arm",
    "subject": "A Signature design for an arm that works beside people without a fence.",
    "description": "The Gentle Arm is a Signature design-study: A Signature design for an arm that works beside people without a fence. The Gentle Arm is a Signature-made design: a collaborative arm that works beside people, with force limits and a hand-teach mode. Its novelty is a touch budget that counts every contact, so the arm can prove it never exceeded the safe force. The Arm is meant for assembly and packing where judgement and patience must share a bench. This is a Signature-made design, presented as a design study only, never as an established fact and never as a built product. The design is judged on i",
    "label": "robotics-research-exchange-signature-000021",
    "figures": {
      "robots": 0,
      "cobots": 11,
      "tasks": 8,
      "force_n": 115,
      "trials": 84,
      "success_pct": 94
    }
  },
  {
    "title": "The Soft Hand",
    "subject": "A Signature design for a hand of rubber and air that grips without bruising.",
    "description": "The Soft Hand is a Signature design-study: A Signature design for a hand of rubber and air that grips without bruising. The Soft Hand is a Signature-made design: a gripper of rubber chambers that curls with air pressure and grips fruit and organs without bruising. Its novelty is a shape sense built into the soft body, so the hand knows its own curl without a camera. The Hand is meant for delicate work that hard fingers would ruin. This is a Signature-made design, presented as a design study only, never as an established fact and never as a built product. The design is judged on its own terms: ",
    "label": "robotics-research-exchange-signature-000022",
    "figures": {
      "robots": 0,
      "grippers": 7,
      "objects": 22,
      "pressure_kpa": 82,
      "trials": 110,
      "success_pct": 93
    }
  },
  {
    "title": "The Walking Mirror",
    "subject": "A Signature design for a mirror that teaches humanoids to walk by watching themselves.",
    "description": "The Walking Mirror is a Signature design-study: A Signature design for a mirror that teaches humanoids to walk by watching themselves. The Walking Mirror is a Signature-made design: a walking school where a humanoid practises in simulation thousands of times before one real step. Its novelty is a fall diary that records every fall and its fix, so the same fall never happens twice. The Mirror is meant for humanoids that must use doors, stairs and tools built for people. This is a Signature-made design, presented as a design study only, never as an established fact and never as a built product. ",
    "label": "robotics-research-exchange-signature-000023",
    "figures": {
      "robots": 0,
      "humanoids": 4,
      "sim_steps": 5200,
      "real_steps": 850,
      "falls": 3,
      "success_pct": 92
    }
  },
  {
    "title": "The Exchange Itself",
    "subject": "A Signature design for the exchange as a whole: one hall for all robotics research.",
    "description": "The Exchange Itself is a Signature design-study: A Signature design for the exchange as a whole: one hall for all robotics research. The Exchange Itself is a Signature-made design: a single hall where papers, datasets, benchmarks, hardware and people meet. Its novelty is a reputation ledger that records who shared what and who repeated it, so generosity is visible. The Exchange is meant for a field that advances fastest when it shares fastest. This is a Signature-made design, presented as a design study only, never as an established fact and never as a built product. The design is judged on it",
    "label": "robotics-research-exchange-signature-000024",
    "figures": {
      "robots": 0,
      "papers": 300,
      "datasets": 30,
      "benchmarks": 15,
      "repeats": 60,
      "success_pct": 95
    }
  }
];

function canonical(o) {
  if (o === null || typeof o !== "object") return JSON.stringify(o);
  if (Array.isArray(o)) return "[" + o.map(canonical).join(",") + "]";
  return "{" + Object.keys(o).sort().map(k => JSON.stringify(k) + ":" + canonical(o[k])).join(",") + "}";
}

function mulberry32(a) {
  return function () {
    a |= 0; a = (a + 0x6D2B79F5) | 0;
    let t = Math.imul(a ^ (a >>> 15), 1 | a);
    t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t;
    return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
  };
}

function generate(seed) {
  const rnd = mulberry32(seed);
  const t = TOPICS[Math.floor(rnd() * TOPICS.length)];
  const n = 1 + Math.floor(rnd() * 24);
  const id = ID_PREFIX + String(n).padStart(6, "0");
  const rec = {
    id: id,
    slug: SLUG,
    edition: EDITION,
    record_kind: RECORD_KIND,
    title: t.title,
    subject: t.subject,
    status: "generated",
    src: "signature-generated",
    ai_name: AI_NAME,
    description: t.description,
    label: t.label,
    figures: t.figures,
    sources: SOURCES,
    generator: { type: "seeded boundless generator", gen_id_prefix: ID_PREFIX + "GEN-", hard_stop: 1000000000, throttle_per_call: 100, ceiling_note: CEILING },
    scales: { A1: "One record: a single entry, fully specified and checkable.", A2: "The whole type: every part of the type, specified and tested together.", A3: "The type against the network: the type feeding websites, generators, and the generator database." },
  };
  const slim = {};
  for (const k of Object.keys(rec)) slim[k] = rec[k];
  rec.jcc_key = "k=" + crypto.createHash("sha256").update(canonical(slim)).digest("hex").slice(0, 8);
  rec.jcc_code = "JAHDB/" + SLUG + "#" + id;
  return rec;
}

const SOURCES = [
  {
    "name": "arXiv (Wikipedia)",
    "url": "https://en.wikipedia.org/wiki/ArXiv",
    "retrieved": "2026-11-18"
  },
  {
    "name": "Robotics (Wikipedia)",
    "url": "https://en.wikipedia.org/wiki/Robotics",
    "retrieved": "2026-11-18"
  }
];

function runTests() {
  let passed = 0, failed = 0;
  function t(name, ok) { if (ok) { passed++; } else { failed++; console.log("FAIL: " + name); } }
  const a = generate(42), b = generate(42);
  t("same seed twice identical", JSON.stringify(a) === JSON.stringify(b));
  t("record_kind", a.record_kind === RECORD_KIND);
  t("slug form", a.slug === SLUG);
  t("id prefix own family", a.id.indexOf(ID_PREFIX) === 0);
  t("generator hard_stop 1e9", a.generator.hard_stop === 1000000000);
  t("generator gen prefix own family", a.generator.gen_id_prefix === ID_PREFIX + "GEN-");
  t("jcc_code form", a.jcc_code === "JAHDB/" + SLUG + "#" + a.id);
  const slim = {}; for (const k of Object.keys(a)) { if (k !== "jcc_code" && k !== "jcc_key") slim[k] = a[k]; }
  t("jcc_key round-trip", a.jcc_key === "k=" + crypto.createHash("sha256").update(canonical(slim)).digest("hex").slice(0, 8));
  t("different seeds differ", JSON.stringify(generate(42)) !== JSON.stringify(generate(43)));
  t("17 keys", Object.keys(a).length === 17);
  console.log("Tests: " + passed + " passed, " + failed + " failed");
  return failed === 0;
}

if (require.main === module) {
  const arg = process.argv[2];
  if (arg === "--test") {
    process.exit(runTests() ? 0 : 1);
  }
  const seed = arg === undefined ? 1 : parseInt(arg, 10);
  if (!Number.isFinite(seed)) { console.error("seed must be an integer"); process.exit(2); }
  console.log(JSON.stringify(generate(seed)));
}
module.exports = { generate, runTests };
