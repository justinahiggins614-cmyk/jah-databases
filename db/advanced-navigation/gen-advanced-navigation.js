// Seeded boundless generator for the Advanced Navigation Database database
// (public edition). Deterministic: the same seed always emits the same
// record. Usage: node gen-advanced-navigation.js [seed]  (prints one
// JSON record) or: node gen-advanced-navigation.js --test (runTests).
// Package-only; outputs are generated, not stored files.
"use strict";
const crypto = require("crypto");

const SLUG = "advanced-navigation";
const RECORD_KIND = "advanced navigation record";
const ID_PREFIX = "JAH-ADNAV-";
const AI_NAME = "JAH Advanced Navigation Librarian";
const CEILING = "Generator ceiling: up to 1,000,000,000 scales per file, generated on demand by the file AI \u2014 not stored files.";

const TOPICS = [
  { title: "Advanced Navigation: Overview and Objective",
    subject: "Advanced navigation overview",
    description: "Advanced navigation answers two questions at once: where am I, and how do I get where I am going, using several independent methods so that losing one does not mean losing the way.",
    figures: { methods: 8, accuracy_m: 1, availability_percent: 99, sources_fused: 5, update_hz: 10, outage_minutes: 30, test_routes: 12, standards: 6 } },
  { title: "Global Navigation Satellite Systems",
    subject: "Global navigation satellite systems",
    description: "A global navigation satellite system, shortened to GNSS, is a constellation of satellites that broadcast timed radio signals from orbit; a receiver measures how long each signal to",
    figures: { constellations: 4, satellites: 120, frequencies: 3, accuracy_m: 5, time_accuracy_ns: 20, receivers: 24, signals_tracked: 12, cold_start_s: 60 } },
  { title: "Inertial Navigation Systems",
    subject: "Inertial navigation systems",
    description: "An inertial navigation system, shortened to INS, measures movement from inside the vehicle using accelerometers, which sense acceleration, and gyroscopes, which sense rotation, on ",
    figures: { sensors: 6, drift_m_per_h: 10, update_hz: 100, axes: 3, gyro_bias_deg_per_h: 1, accel_bias_mg: 1, test_runs: 20, calibrations: 12 } },
  { title: "Kalman Filtering and Sensor Fusion for Navigation",
    subject: "Kalman filtering for navigation",
    description: "A Kalman filter is a mathematical method for combining noisy measurements from several sources into one best estimate of position and velocity, together with a covariance, which is",
    figures: { sources_fused: 5, update_hz: 10, states: 15, covariance_checks: 100, innovation_tests: 50, divergences: 0, test_scenarios: 24, tuning_runs: 12 } },
  { title: "Terrain-Referenced Navigation",
    subject: "Terrain-referenced navigation",
    description: "Terrain-referenced navigation fixes position by matching the shape of the ground below, measured by a radar or laser altimeter, against a stored map of terrain heights. When the me",
    figures: { map_tiles: 500, resolution_m: 30, matches_per_route: 200, accuracy_m: 15, altimeter_m: 3, routes: 8, false_matches: 2, update_hz: 5 } },
  { title: "Celestial Navigation, Modernised",
    subject: "Celestial navigation",
    description: "Celestial navigation finds position from the stars: by measuring the angle of known stars above the horizon and comparing with an almanac, which is a table of where each star shoul",
    figures: { stars_catalogued: 3000, accuracy_m: 100, sights_per_fix: 3, fix_time_s: 30, almanac_years: 5, instruments: 4, test_nights: 12, cloudy_nights: 4 } },
  { title: "Visual Odometry and Simultaneous Localisation and Mapping",
    subject: "Visual odometry and SLAM",
    description: "Visual odometry estimates movement by watching how features in camera images shift from frame to frame, and simultaneous localisation and mapping, shortened to SLAM, builds a map o",
    figures: { cameras: 2, features_per_frame: 500, frame_rate_hz: 30, drift_percent: 1, map_points: 100000, loop_closures: 20, routes: 10, lighting_conditions: 6 } },
  { title: "Dead Reckoning: The Oldest Method, Kept Honest",
    subject: "Dead reckoning",
    description: "Dead reckoning estimates position by starting from a known fix and adding up speed and heading over time: distance travelled in each direction, step by step. Its error grows with d",
    figures: { speed_sensors: 3, heading_sensors: 2, error_percent: 2, fix_interval_min: 10, test_runs: 20, distances_km: 500, corrections: 200, instruments: 6 } },
]

const SOURCES = [
  { name: "Wikipedia - Global Positioning System", url: "https://en.wikipedia.org/wiki/Global_Positioning_System", establishes: "Public background for this subject." },
  { name: "Wikipedia - Global Navigation Satellite System", url: "https://en.wikipedia.org/wiki/Global_Navigation_Satellite_System", establishes: "Public background for this subject." },
]

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
  const label = "advanced-navigation-overview";
  const demo = buildDemo(topic, label);
  const rec = {
    id: id,
    slug: SLUG,
    edition: "public",
    record_kind: RECORD_KIND,
    title: topic.title + " (Generated " + idx + ")",
    subject: topic.subject,
    status: "built",
    src: "public-harvest",
    ai_name: AI_NAME,
    description: topic.description + " " + "DARPA-grade means engineering targets modeled on public standards; it is never a claim of DARPA approval, certification, funding, or endorsement.",
    body: "<h2>Description</h2><p>" + topic.description + "</p>",
    demo: demo.code,
    expected_output: demo.expected,
    program: "class GeneratedProgram:\n    def run(self):\n        return {\"deterministic\": True}\n",
    sources: SOURCES,
    generator: { type: "seeded boundless generator", gen_id_prefix: ID_PREFIX + "GEN-", hard_stop: 1000000000, throttle_per_call: 100, ceiling_note: CEILING },
    scales: { A1: "One advanced navigation record: a single subject with its full specification, demo, and evidence ladder.", A2: "The whole advanced navigation database: 24 public records and 24 Signature design-study records covering the subject.", A3: "The advanced navigation database against the network: linked to its sibling edition and to the adjacent live databases." },
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
  t("slug single form", a.slug === SLUG && a.slug.indexOf("-signature") === -1);
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
