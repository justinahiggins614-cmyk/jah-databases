// Seeded boundless generator for the autonomous-systems database
// (public edition). Deterministic: the same seed always emits the same
// record. Usage: node gen-autonomous-systems.js [seed]  (prints one
// JSON record) or: node gen-autonomous-systems.js --test (runTests).
// Package-only; outputs are generated, not stored files.
"use strict";
const crypto = require("crypto");

const SLUG = "autonomous-systems";
const RECORD_KIND = "autonomous systems record";
const ID_PREFIX = "JAH-AUTSYS-";
const AI_NAME = "JAH Autonomous Systems Librarian";
const EDITION = "public";
const SRC = "public-harvest";
const CEILING = "Generator ceiling: up to 1,000,000,000 scales per file, generated on demand by the file AI \u2014 not stored files.";

const TOPICS = [
  {
    "title": "Autonomous Systems: Overview and Autonomy Mission",
    "subject": "Autonomous systems overview",
    "description": "This record is the front door of the Autonomous Systems Database. It states the mission: to record autonomous decision-making and control for civilian use, so that a machine can perceive its surroundings, plan what to do, act on that plan, and check whether the action worked, while a human still sets the mission, the limits, and the authority to stop the machine.",
    "figures": {
      "autonomy_functions": 8,
      "capabilities": 12,
      "evidence_rungs": 9,
      "platform_types": 6,
      "mission_types": 10,
      "safety_layers": 5,
      "test_environments": 7,
      "review_gates": 6
    },
    "label": "autonomous-systems-overview"
  },
  {
    "title": "Perception and World Modeling: How Machines Understand Surroundings",
    "subject": "Perception and world modeling",
    "description": "Perception is the work of turning sensor measurements into an understanding of the surroundings, and a world model is the machine's internal record of what is around it: where things are, what they are, and how they move. This record covers how perception systems are built, how world models are kept up to date, and how their errors are measured.",
    "figures": {
      "sensor_types": 7,
      "world_model_layers": 4,
      "object_classes": 60,
      "tracking_targets": 40,
      "update_rate_hz": 10,
      "model_checks": 12,
      "failure_modes": 8,
      "review_rounds": 3
    },
    "label": "perception-world-modeling"
  },
  {
    "title": "Path Planning: Finding a Safe Route Through the World",
    "subject": "Path planning",
    "description": "Path planning is the work of finding a route from where a machine is to where it must go, through a world that contains obstacles, limits, and other moving things. A path is a sequence of positions; a plan is a path plus the speeds and the rules for following it. This record covers how paths are found, checked for safety, and replanned when the world changes.",
    "figures": {
      "planning_algorithms": 6,
      "route_tests": 80,
      "obstacle_types": 12,
      "map_resolutions": 4,
      "replan_triggers": 5,
      "safety_margins_m": 2,
      "route_lengths_km": 15,
      "review_rounds": 3
    },
    "label": "path-planning"
  },
  {
    "title": "Motion Control: Making a Machine Follow Its Plan",
    "subject": "Motion control",
    "description": "Motion control is the work of making a machine follow its planned path: measuring where it is, comparing that with where it should be, and adjusting its actuators, which are the motors and steering devices that move it. A control loop is the repeated cycle of measure, compare, and correct. This record covers how control loops are designed, tuned, and checked for stability.",
    "figures": {
      "control_loops": 5,
      "control_rate_hz": 100,
      "tracking_tests": 60,
      "disturbance_types": 8,
      "stability_checks": 10,
      "actuator_limits": 6,
      "error_budgets": 4,
      "review_rounds": 3
    },
    "label": "motion-control"
  },
  {
    "title": "Localization and Mapping: Knowing Where You Are",
    "subject": "Localization and mapping",
    "description": "Localization is the work of knowing where a machine is, and mapping is the work of building a record of the surroundings it moves through. Simultaneous localization and mapping, shortened to SLAM (simultaneous localization and mapping), does both at once: the machine builds the map while finding itself inside it. This record covers how SLAM systems are built and judged.",
    "figures": {
      "mapping_methods": 5,
      "map_tiles": 200,
      "loop_closures": 30,
      "position_tests": 90,
      "drift_measurements": 12,
      "landmark_types": 10,
      "update_rate_hz": 10,
      "review_rounds": 3
    },
    "label": "localization-mapping"
  },
  {
    "title": "Decision Making under Uncertainty: Choosing When Facts Are Incomplete",
    "subject": "Decision making under uncertainty",
    "description": "Decision making under uncertainty is the work of choosing an action when the facts are incomplete: sensors are noisy, the future is unknown, and every option carries risk. A decision model is a written rule for weighing options, their likely outcomes, and their costs. This record covers how such decisions are made, bounded, and audited.",
    "figures": {
      "decision_models": 5,
      "uncertain_factors": 18,
      "scenario_tests": 45,
      "risk_thresholds": 6,
      "fallback_plans": 8,
      "decision_audits": 20,
      "review_rounds": 3,
      "escalation_rules": 7
    },
    "label": "decision-under-uncertainty"
  },
  {
    "title": "Human Supervision and Override: Keeping People in Charge",
    "subject": "Human supervision and override",
    "description": "Human supervision is the work of a person watching an autonomous system, understanding what it is doing, and being able to stop it or take over. Override is the mechanism by which a person takes control back: a stop button, a command, or an automatic handoff. This record covers how supervision is organized, how overrides are built, and how both are tested.",
    "figures": {
      "supervision_modes": 4,
      "override_mechanisms": 5,
      "alert_types": 9,
      "response_time_tests": 30,
      "operator_tasks": 12,
      "handoff_drills": 14,
      "monitoring_screens": 6,
      "review_rounds": 3
    },
    "label": "human-supervision-override"
  },
  {
    "title": "Fleet Coordination: Many Machines Working as One Team",
    "subject": "Fleet coordination",
    "description": "Fleet coordination is the work of making many autonomous machines share work, space, and communication without colliding or duplicating effort. A fleet is a group of machines under one coordinating plan; task allocation is the assignment of jobs to machines. This record covers how fleets are coordinated, how conflicts are resolved, and how a fleet recovers when a member fails.",
    "figures": {
      "fleet_sizes": 5,
      "coordination_rules": 12,
      "task_allocations": 40,
      "conflict_tests": 25,
      "communication_links": 10,
      "recovery_plans": 6,
      "throughput_tests": 15,
      "review_rounds": 3
    },
    "label": "fleet-coordination"
  }
];

const SOURCES = [
  {
    "name": "Wikipedia - Autonomous robot",
    "url": "https://en.wikipedia.org/wiki/Autonomous_robot",
    "establishes": "Source for generated records in this edition."
  },
  {
    "name": "DARPA (Defense Advanced Research Projects Agency) - research programs, technology areas, solicitations and program information",
    "url": "https://www.darpa.mil",
    "establishes": "Source for generated records in this edition."
  }
];

function mulberry32(seed) {
  let a = seed >>> 0;
  return function () {
    a |= 0; a = (a + 0x6D2B79F5) | 0;
    let t = Math.imul(a ^ (a >>> 15), 1 | a);
    t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t;
    return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
  };
}

function canonical(obj) {
  if (obj === null || typeof obj !== "object") return JSON.stringify(obj);
  if (Array.isArray(obj)) return "[" + obj.map(canonical).join(",") + "]";
  const keys = Object.keys(obj).sort();
  return "{" + keys.map((k) => JSON.stringify(k) + ":" + canonical(obj[k])).join(",") + "}";
}

function buildDemo(topic, label) {
  const figs = topic.figures;
  const keys = Object.keys(figs).sort();
  const total = keys.reduce((s, k) => s + figs[k], 0);
  const out = { count: keys.length, label: label, max: Math.max(...keys.map((k) => figs[k])), min: Math.min(...keys.map((k) => figs[k])), total: total };
  const result = Object.keys(out).sort().map((k) => k + "=" + out[k]).join("|");
  const h = crypto.createHash("sha256").update(result).digest("hex");
  const figsPy = "FIGURES = {" + keys.map((k) => JSON.stringify(k) + ": " + figs[k]).join(", ") + "}\nLABEL = " + JSON.stringify(label) + "\n";
  const code = "import hashlib\n" + figsPy +
    "def compute():\n" +
    "    total = sum(FIGURES.values())\n" +
    "    n = len(FIGURES)\n" +
    "    out = {\"count\": n, \"label\": LABEL, \"max\": max(FIGURES.values()), \"min\": min(FIGURES.values()), \"total\": total}\n" +
    "    return out\n" +
    "outputs = compute()\n" +
    "result = \"|\".join(f\"{k}={v}\" for k, v in sorted(outputs.items()))\n" +
    "h1 = hashlib.sha256(result.encode()).hexdigest()\n" +
    "outputs2 = compute()\n" +
    "result2 = \"|\".join(f\"{k}={v}\" for k, v in sorted(outputs2.items()))\n" +
    "h2 = hashlib.sha256(result2.encode()).hexdigest()\n" +
    "for k, v in sorted(outputs.items()):\n" +
    "    print(f\"{k}: {v}\")\n" +
    "print(f\"Result: {result}\")\n" +
    "print(f\"Run 1 SHA-256: {h1}\")\n" +
    "print(f\"Run 2 SHA-256: {h2}\")\n" +
    "print(f\"Deterministic: {'MATCH' if h1 == h2 else 'MISMATCH'}\")\n";
  const expected = Object.keys(out).sort().map((k) => k + ": " + out[k]).join("\n") + "\n" +
    "Result: " + result + "\n" +
    "Run 1 SHA-256: " + h + "\n" +
    "Run 2 SHA-256: " + h + "\n" +
    "Deterministic: MATCH\n";
  return { code, expected };
}

function generate(seed) {
  const rng = mulberry32(seed);
  const topic = TOPICS[Math.floor(rng() * TOPICS.length)];
  const idx = seed % 1000000;
  const id = ID_PREFIX + "GEN-" + String(idx).padStart(6, "0");
  const label = topic.label;
  const demo = buildDemo(topic, label);
  const rec = {
    id: id,
    slug: SLUG,
    edition: EDITION,
    record_kind: RECORD_KIND,
    title: topic.title + " (Generated " + idx + ")",
    subject: topic.subject,
    status: "built",
    src: SRC,
    ai_name: AI_NAME,
    description: topic.description + " No claim of a proven breakthrough, of flight readiness, or of deployment readiness is established by this generated record." + " DARPA-grade here means engineering targets modeled on public standards, never a claim of DARPA approval, certification, funding, or endorsement.",
    body: "<h2>Description</h2><p>" + topic.description + "</p>",
    demo: demo.code,
    expected_output: demo.expected,
    program: "class GeneratedProgram:\n    def run(self):\n        return {\"deterministic\": True}\n",
    sources: SOURCES,
    generator: { type: "seeded boundless generator", gen_id_prefix: ID_PREFIX + "GEN-", hard_stop: 1000000000, throttle_per_call: 100, ceiling_note: CEILING },
    scales: { A1: "One generated record on this topic.", A2: "The pair: generated records extend the 24 filed records.", A3: "The network: every database a knowledge source, every generator a tool." },
  };
  const slim = {};
  for (const k of Object.keys(rec)) slim[k] = rec[k];
  rec.jcc_key = "k=" + crypto.createHash("sha256").update(canonical(slim)).digest("hex").slice(0, 8);
  rec.jcc_code = "JAHDB/" + SLUG + "#" + id;
  return rec;
}

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
  t("19 keys", Object.keys(a).length === 19);
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
