// Seeded boundless generator for the sensor-fusion database
// (public edition). Deterministic: the same seed always emits the same
// record. Usage: node gen-sensor-fusion.js [seed]  (prints one
// JSON record) or: node gen-sensor-fusion.js --test (runTests).
// Package-only; outputs are generated, not stored files.
"use strict";
const crypto = require("crypto");

const SLUG = "sensor-fusion";
const RECORD_KIND = "sensor fusion record";
const ID_PREFIX = "JAH-SENF-";
const AI_NAME = "JAH Sensor Fusion Librarian";
const EDITION = "public";
const SRC = "public-harvest";
const CEILING = "Generator ceiling: up to 1,000,000,000 scales per file, generated on demand by the file AI \u2014 not stored files.";

const TOPICS = [
  {
    "title": "Sensor Fusion: Overview and Fusion Mission",
    "subject": "Sensor fusion overview",
    "description": "This record is the front door of the Sensor Fusion Database. Sensor fusion is the process of combining sensor data, or data derived from separate sources, so that the resulting information has less uncertainty than would be possible if the sources were used individually. For example, a more accurate indoor location can come from combining video cameras and WiFi localization signals. This record states the mission and the methods.",
    "figures": {
      "fusion_methods": 9,
      "capabilities": 12,
      "evidence_rungs": 9,
      "sensor_types": 8,
      "fusion_levels": 3,
      "application_areas": 7,
      "test_scenarios": 40,
      "review_gates": 6
    },
    "label": "sensor-fusion-overview"
  },
  {
    "title": "Kalman Filtering: The Classic Recursive Estimator",
    "subject": "Kalman filtering",
    "description": "A Kalman filter is a recursive estimator, meaning a method that keeps a running estimate and updates it with each new measurement. It predicts where a moving thing will be, then corrects that prediction using the actual measurement, weighting the two by how much each can be trusted. This record covers how Kalman filters are built, tuned, and tested.",
    "figures": {
      "filter_states": 6,
      "measurement_types": 4,
      "update_rate_hz": 50,
      "test_tracks": 60,
      "noise_models": 5,
      "convergence_tests": 20,
      "tuning_parameters": 4,
      "review_rounds": 3
    },
    "label": "kalman-filtering"
  },
  {
    "title": "Extended and Unscented Kalman Filters: Filtering Nonlinear Motion",
    "subject": "Extended and unscented Kalman filters",
    "description": "The extended Kalman filter and the unscented Kalman filter are versions of the Kalman filter for nonlinear motion, meaning motion where the relationship between state and measurement is not a straight line. The extended filter linearizes, meaning it approximates the curve with a straight line at each step; the unscented filter uses sigma points, meaning carefully chosen sample points, to carry uncertainty through the curve. This record covers both.",
    "figures": {
      "filter_variants": 3,
      "nonlinear_tests": 45,
      "state_dimensions": 9,
      "sigma_points": 19,
      "linearization_checks": 12,
      "divergence_tests": 15,
      "tuning_parameters": 5,
      "review_rounds": 3
    },
    "label": "extended-unscented-kalman"
  },
  {
    "title": "Particle Filters: Tracking with Many Guesses at Once",
    "subject": "Particle filters",
    "description": "A particle filter is a tracking method that keeps many guesses, called particles, about where a thing is, instead of one estimate. Each particle is a possible state; particles that match the measurements survive and multiply, and particles that do not match die out. Resampling is the step that replaces bad particles with copies of good ones. This record covers how particle filters are built and tested.",
    "figures": {
      "particle_counts": 4,
      "tracking_tests": 50,
      "resampling_methods": 3,
      "state_dimensions": 6,
      "degeneracy_tests": 12,
      "multimodal_cases": 8,
      "compute_budgets": 5,
      "review_rounds": 3
    },
    "label": "particle-filters"
  },
  {
    "title": "Bayesian Fusion: Combining Evidence by the Rules of Probability",
    "subject": "Bayesian fusion",
    "description": "Bayesian fusion is the combining of evidence from several sources using the rules of probability. A prior is the belief before new evidence; a likelihood is how probable the evidence is under each possible truth; and the posterior is the updated belief after the evidence is weighed. This record covers how Bayesian fusion is built, calibrated, and tested.",
    "figures": {
      "evidence_sources": 6,
      "fusion_tests": 45,
      "prior_models": 5,
      "likelihood_models": 8,
      "calibration_tests": 12,
      "conflict_cases": 10,
      "update_steps": 30,
      "review_rounds": 3
    },
    "label": "bayesian-fusion"
  },
  {
    "title": "Dempster-Shafer Evidence Theory: Fusing Uncertain and Conflicting Reports",
    "subject": "Dempster-Shafer evidence theory",
    "description": "Dempster-Shafer evidence theory is a method for combining reports from several sources when the reports are uncertain, incomplete, or conflicting. Unlike ordinary probability, it can represent ignorance directly: a source can say it does not know, instead of being forced to split its belief among answers. A mass function is the assignment of belief to sets of possibilities. This record covers how the theory is applied and tested.",
    "figures": {
      "evidence_sources": 5,
      "hypothesis_sets": 8,
      "combination_tests": 30,
      "conflict_cases": 12,
      "ignorance_measures": 4,
      "decision_rules": 6,
      "calibration_tests": 10,
      "review_rounds": 3
    },
    "label": "dempster-shafer-evidence"
  },
  {
    "title": "Multi-Sensor Calibration: Making Sensors Agree on Reality",
    "subject": "Multi-sensor calibration",
    "description": "Calibration is the work of adjusting sensors so their readings match reality, and multi-sensor calibration is doing that for several sensors together, so they agree with each other as well as with reality. A reference standard is a known true value used to check a sensor. This record covers how calibration is planned, performed, and checked over time.",
    "figures": {
      "sensor_types": 7,
      "calibration_procedures": 10,
      "reference_standards": 6,
      "calibration_tests": 40,
      "drift_checks": 12,
      "recalibration_triggers": 5,
      "error_budgets": 4,
      "review_rounds": 3
    },
    "label": "multi-sensor-calibration"
  },
  {
    "title": "Time Synchronization: Giving Every Sensor the Same Clock",
    "subject": "Time synchronization",
    "description": "Time synchronization is the work of giving every sensor and every computer in a system the same sense of time, so that measurements taken at the same moment can be recognized as simultaneous. An offset is the difference between two clocks; drift is how that difference grows over time. This record covers how clocks are synchronized and how timing errors are measured.",
    "figures": {
      "clock_sources": 4,
      "sync_protocols": 5,
      "timing_tests": 30,
      "offset_measurements": 25,
      "drift_budgets_ms": 10,
      "sync_failures": 8,
      "timestamp_checks": 20,
      "review_rounds": 3
    },
    "label": "time-synchronization"
  }
];

const SOURCES = [
  {
    "name": "Wikipedia - Sensor fusion",
    "url": "https://en.wikipedia.org/wiki/Sensor_fusion",
    "establishes": "Source for generated records in this edition."
  },
  {
    "name": "Wikipedia - Kalman filter",
    "url": "https://en.wikipedia.org/wiki/Kalman_filter",
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
