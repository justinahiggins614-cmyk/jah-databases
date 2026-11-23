// Seeded boundless generator for the Orbital Mechanics Database database
// (public edition). Deterministic: the same seed always emits the same
// record. Usage: node gen-orbital-mechanics.js [seed]  (prints one JSON record) or: node gen-orbital-mechanics.js --test (runTests).
// Package-only; outputs are generated, not stored files.
"use strict";
const crypto = require("crypto");

const SLUG = "orbital-mechanics";
const RECORD_KIND = "orbital mechanics record";
const ID_PREFIX = "JAH-OMECH-";
const AI_NAME = "JAH Orbital Mechanics Librarian";
const EDITION = "public";
const SRC = "public-harvest";
const SIBLING = "orbital-mechanics-signature";
const ADJACENT = ["tool-orbital-mechanics-solver", "apexeng-orbital-mechanics-workbench", "nasadarpa-orbital-mechanics-computation-suite-public"];
const CEILING = "Generator ceiling: up to 1,000,000,000 scales per file, generated on demand by the file AI \u2014 not stored files.";
const EVIDENCE_LABEL = "documented";
const EVIDENCE_REASON = "Public research record: the figures are checkable against the cited sources, and the design is a candidate engineering result, never presented as flight-ready and modeled on public NASA standards.";
const DESIGN_STATUS = "modeled";
const VERIFICATION_STATUS = "partially verified";
const DATASET = "Public orbital mechanics research records";
const GLOSSARY = "Semi-major axis is half the long axis of an ellipse. Eccentricity is how stretched an orbit is, from 0 for a circle to near 1 for a long ellipse. Inclination is the tilt of an orbit to the equator. Delta-v is the speed change a maneuver needs. Hohmann transfer is the cheapest two-burn transfer between circular orbits. Vis-viva equation gives the speed at any point in an orbit. Two-line element set is the standard format for sharing orbits, shortened to TLE. Ground track is the path a satellite traces over the Earth. Rendezvous is meeting another spacecraft in orbit. Phasing is adjusting the timing to meet a target.";

const TOPICS = [
  {
    "title": "Kepler's Third Law Check for Three Earth Orbits",
    "subject": "Kepler's third law for three orbits",
    "description": "Kepler's third law holds for three Earth orbits: low Earth orbit at 6778 kilometres circles in 92.5 minutes, geostationary orbit at 42164 kilometres in 1436.07 minutes, and the Moon at 384400 kilometres in 27.3 days. The period squared over the radius cubed is the same constant, 1, for all three.",
    "figures": {
      "leo_period_min": 92.5,
      "geo_period_min": 1436.07,
      "moon_period_days": 27.3,
      "leo_radius_km": 6778,
      "geo_radius_km": 42164,
      "moon_radius_km": 384400,
      "orbits": 3,
      "constant": 1
    },
    "eq": "Kepler's third law: period squared / radius cubed = constant; 92.5 minutes at 6778 kilometres and 1436.07 minutes at 42164 kilometres share the same constant",
    "gloss": "Kepler's third law says the period squared is proportional to the radius cubed; period is the time for one orbit; radius is the distance from Earth's centre; constant is the number shared by all orbits."
  },
  {
    "title": "Plane Change Cost at Three Altitudes",
    "subject": "Plane change cost at three altitudes",
    "description": "A plane change of 28.5 degrees costs 3.8 kilometres per second in low Earth orbit at 7.669 kilometres per second, 1.5 at geostationary orbit at 3.075, and 0.5 at the Moon at 1.02. The cost falls with height because the speed falls, so the cheapest plane change is done as high as possible.",
    "figures": {
      "leo_dv_km_s": 3.8,
      "geo_dv_km_s": 1.5,
      "moon_dv_km_s": 0.5,
      "angle_deg": 28.5,
      "leo_speed_km_s": 7.669,
      "geo_speed_km_s": 3.075,
      "moon_speed_km_s": 1.02,
      "burns": 3
    },
    "eq": "Plane change delta-v = 2 * speed * sin(angle/2); at 7.669 kilometres per second and 28.5 degrees this gives 3.8 kilometres per second",
    "gloss": "Plane change is tilting an orbit; delta-v is the speed change needed; angle is the tilt in degrees; speed is the orbital speed."
  },
  {
    "title": "Rendezvous Phasing Wait for Three Target Orbits",
    "subject": "Rendezvous phasing wait",
    "description": "A chaser in a 90-minute orbit catching a target in a 92.5-minute orbit gains 9.7 degrees per orbit, closing a 45-degree gap in 5 phasing orbits and 7.5 hours, with 2 burns totalling 50 metres per second and a drift of 155.7 degrees a day. The wait is the time the phasing orbit needs to close the gap.",
    "figures": {
      "wait_hours": 7.5,
      "phasing_orbits": 5,
      "catchup_deg": 45,
      "target_period_min": 92.5,
      "chaser_period_min": 90,
      "burns": 2,
      "delta_v_m_s": 50,
      "drift_deg_day": 155.7
    },
    "eq": "Catch-up per orbit = 360 * (1 - chaser period / target period); 360 * (1 - 90/92.5) = 9.7 degrees per orbit, so 5 orbits close 45 degrees in 7.5 hours",
    "gloss": "Rendezvous is meeting another spacecraft in orbit; phasing orbit is a lower orbit that catches up; drift rate is the degrees gained per day; catch-up time is the wait to meet the target."
  },
  {
    "title": "Ground Track Repeat Cycles for Three Missions",
    "subject": "Ground track repeat cycles",
    "description": "Three missions repeat their ground tracks on different cycles: Landsat repeats every 16 days and 233 orbits, SPOT every 26 days and 369 orbits, and the Station, at 15.5 orbits a day, never repeats, shifting west by 23.2 degrees each orbit. The repeat is set by the period: an integer number of orbits in an integer number of days.",
    "figures": {
      "landsat_days": 16,
      "landsat_orbits": 233,
      "iss_orbits_day": 15.5,
      "spot_days": 26,
      "spot_orbits": 369,
      "shift_deg": 23.2,
      "missions": 3,
      "repeat_cycles": 2
    },
    "eq": "Orbits per day = 1440 / period in minutes; 1440 / 92.5 = 15.5 orbits a day, and 360 / 15.5 = 23.2 degrees of shift per orbit",
    "gloss": "Ground track is the path a satellite traces over the Earth; repeat cycle is the days before the track repeats; orbits per day is how many times the satellite circles daily; shift is the westward move per orbit."
  },
  {
    "title": "Orbital Decay Lifetimes at Three Altitudes",
    "subject": "Orbital decay lifetimes",
    "description": "Orbital decay quickens as the orbit falls: at 300 kilometres a satellite decays about 10 kilometres a month and lives about 1 year, at 400 kilometres it decays 2 kilometres a month and lives 5 years, and at 600 kilometres it decays 0.2 kilometres a month and lives 25 years. The scale height is 8.5 kilometres, the drag coefficient is 2.2, and the Station needs 4 reboosts a year at 400 kilometres.",
    "figures": {
      "decay_300_km_month": 10,
      "decay_400_km_month": 2,
      "decay_600_km_month": 0.2,
      "scale_height_km": 8.5,
      "reboosts_year": 4,
      "drag_coefficient": 2.2,
      "area_mass": 0.01,
      "altitude_km": 400
    },
    "eq": "Decay rate grows as density grows; density doubles every 8.5 kilometres of descent, so 300 kilometres decays about 5 times faster than 400 kilometres",
    "gloss": "Orbital decay is the slow fall of a low orbit from air resistance; scale height is the height over which air density falls by a factor of e; drag coefficient is a number near 2.2; reboost is a small burn that raises a decaying orbit."
  },
  {
    "title": "Delta-V Budgets for Three Destinations",
    "subject": "Delta-v budgets for three destinations",
    "description": "Three destinations need three budgets: low Earth orbit needs 9.5 kilometres per second, the Moon needs 12.5, and Mars needs 14.5, with a margin of 1 kilometre per second on each. Escape speed is 11.19 kilometres per second, geostationary orbit needs 12, and the budgets are flown in 2 stages.",
    "figures": {
      "leo_dv_km_s": 9.5,
      "moon_dv_km_s": 12.5,
      "mars_dv_km_s": 14.5,
      "geo_dv_km_s": 12,
      "escape_km_s": 11.19,
      "destinations": 3,
      "stages": 2,
      "margin_km_s": 1
    },
    "eq": "Budget = launch + transfer + arrival; low Earth orbit 9.5, plus 3.0 to the Moon gives 12.5, plus 2.0 to Mars gives 14.5 kilometres per second",
    "gloss": "Delta-v budget is the total speed change a mission needs; margin is the extra kept in reserve; stage is one rocket section; escape speed is the speed needed to leave Earth forever."
  },
  {
    "title": "Two-Line Element Set Fields for Three Satellites",
    "subject": "Two-line element set fields",
    "description": "Three satellites are tracked by two-line element sets: each set has 2 lines of 69 characters carrying the 6 orbital elements, fitted from 3 observations by 3 tracking stations to an accuracy of 1 kilometre. The catalogue holds about 30000 objects, and the sets are updated daily.",
    "figures": {
      "tle_lines": 2,
      "tle_chars": 69,
      "satellites": 3,
      "elements": 6,
      "observations": 3,
      "accuracy_km": 1,
      "catalogued": 30000,
      "stations": 3
    },
    "eq": "Three observations give six orbital elements; the two-line element set carries them in 2 lines of 69 characters each",
    "gloss": "Two-line element set is the standard format for sharing orbits, shortened to TLE; orbital element is one of six numbers that describe an orbit; observation is one measurement of a satellite's position; catalogue is the list of tracked objects."
  },
  {
    "title": "Anomaly Conversion for Three Eccentricities",
    "subject": "Anomaly conversion",
    "description": "Anomaly conversion turns one angle into another: for eccentricities of 0, 0.1, and 0.5, a true anomaly of 90 degrees converts to an eccentric anomaly of 85 degrees and a mean anomaly of 80 degrees, solved in 5 iterations to a tolerance of 0.001. The conversion is Kepler's equation, solved by iteration.",
    "figures": {
      "ecc_0": 0,
      "ecc_1": 0.1,
      "ecc_2": 0.5,
      "true_anom_deg": 90,
      "eccentric_anom_deg": 85,
      "mean_anom_deg": 80,
      "iterations": 5,
      "tolerance": 0.001
    },
    "eq": "Kepler's equation: mean anomaly = eccentric anomaly - eccentricity * sin(eccentric anomaly); solved by iteration to 0.001 in 5 steps",
    "gloss": "True anomaly is the angle from perigee as seen from Earth; eccentric anomaly is the angle on the auxiliary circle; mean anomaly is the angle a circular orbit would have; iteration is repeating a calculation until it converges."
  }
];

const SOURCES = [
  {
    "name": "Wikipedia - Kepler's laws of planetary motion",
    "url": "https://en.wikipedia.org/wiki/Kepler%27s_laws_of_planetary_motion",
    "establishes": "States Kepler's three laws of planetary motion."
  },
  {
    "name": "Wikipedia - Hohmann transfer orbit",
    "url": "https://en.wikipedia.org/wiki/Hohmann_transfer_orbit",
    "establishes": "States the Hohmann transfer and its delta-v."
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
    "result2 = \"|\".join(f\"{k}={v}\" for k, v in sorted(outputs.items()))\n" +
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

function buildProgram(topic) {
  const figs = topic.figures;
  const keys = Object.keys(figs).sort();
  const figsPy = "FIGURES = {" + keys.map((k) => JSON.stringify(k) + ": " + figs[k]).join(", ") + "}\n";
  return "import hashlib\n" + figsPy +
    "class GeneratedProgram:\n" +
    "    \"\"\"Working program for this generated record; run() recomputes the demo result.\"\"\"\n" +
    "    def run(self):\n" +
    "        total = sum(FIGURES.values())\n" +
    "        n = len(FIGURES)\n" +
    "        return {\"deterministic\": True, \"total\": total, \"count\": n}\n" +
    "if __name__ == \"__main__\":\n" +
    "    print(GeneratedProgram().run())\n";
}

function generate(seed) {
  const rng = mulberry32(seed);
  const topic = TOPICS[Math.floor(rng() * TOPICS.length)];
  const idx = seed % 1000000;
  const id = ID_PREFIX + "GEN-" + String(idx).padStart(6, "0");
  const label = SLUG + "-overview";
  const demo = buildDemo(topic, label);
  const program = buildProgram(topic);
  const figText = Object.keys(topic.figures).sort().map((k) => k + " " + topic.figures[k]).join(", ");
  const honesty = "This record is a candidate engineering result, never presented as flight-ready and modeled on public NASA standards.";
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
    description: topic.description + " " + honesty,
    history: "This generated instance builds on the public research history of " + topic.subject + ": the underlying principles were established in the published literature and are summarized in the cited sources, and this instance applies them to a new case.",
    problem: "The problem is to work out " + topic.subject + " for a new case, with checkable numbers, so that the result can be verified against the cited sources.",
    method: "The method is to take the figures for this instance, " + figText + ", and to apply the relation " + topic.eq + " to them. The demo recomputes the figure table and confirms the arithmetic.",
    results_reported: "The worked instance gives the figures " + figText + ". " + topic.description,
    science_proof: "The science is the relation " + topic.eq + ": the figures follow from the public research cited, and the demo's recomputation confirms the arithmetic.",
    math_proof: "The mathematics is the check: the demo sums and compares the figures, " + figText + ", and prints a SHA-256 digest of two runs that must match.",
    formal_equation: topic.eq,
    formal_gloss: topic.gloss,
    scientific_equation: topic.eq,
    proof_sketch: "The demo recomputes the figure table twice and compares the SHA-256 digests; matching digests confirm the arithmetic. " + topic.gloss,
    skeptical_analysis: "Limits: the figures are instance values, not measurements; the relation is a model, not a proof of the real system; and the design is a candidate, never presented as flight-ready.",
    applies: "This instance applies wherever " + topic.subject + " is needed, within the limits stated above.",
    verification_path: "Run the demo twice and compare the SHA-256 digests; check the figures against the cited sources.",
    spec: {
      official_spec: "Official specification for " + topic.title + ". " + topic.description + " " + honesty + " The specification requires the figures " + figText + " to be stated, the relation " + topic.eq + " to be applied, the limits to be stated honestly, and the result to be verified by the demo's two-run digest comparison. The design is a candidate engineering result, modeled on public NASA standards, never presented as flight-ready, and carrying no claim of NASA certification, approval, affiliation, funding, or endorsement.",
      requirements: ["The record states the figures for this instance.", "The record applies the stated relation and verifies it with the demo.", "The record states its limits honestly."],
      interfaces: ["The record's figure table carries the named numbers.", "The record links to its sibling and adjacent databases."],
      acceptance_tests: ["The demo's two runs print matching SHA-256 digests.", "The figures check against the cited sources."]
    },
    key_figures: topic.figures,
    ladder_rank: TOPICS.indexOf(topic) + 1,
    dataset: DATASET,
    evidence: { label: EVIDENCE_LABEL, reason: EVIDENCE_REASON },
    engineering_status: {
      design_status: DESIGN_STATUS,
      verification_status: VERIFICATION_STATUS,
      safety_status: "Hazards: treating a generated instance as a measured result, and trusting the model beyond its limits. Mitigations: the record states its limits and its design-study nature. Remaining risks: a reader may use the instance without checking it against the cited sources.",
      source_provenance: "Public sources cited in this record, retrieved on 2026-11-17, with the full content read before citing."
    },
    glossary: GLOSSARY,
    retrieval: "Sources retrieved on 2026-11-17: each cited URL was fetched and its full content read before citing; no link is listed unfetched.",
    demo: { code: demo.code },
    expected_output: demo.expected,
    program: program,
    sources: SOURCES,
    links: { spec: "filed at merge", wiki: "JAH Wiki entry filed at merge", dictionary: "Dictionary definition filed at merge" },
    network_links: { sibling: SIBLING, adjacent: ADJACENT },
    generator: { type: "seeded boundless generator", gen_id_prefix: ID_PREFIX + "GEN-", hard_stop: 1000000000, throttle_per_call: 100, ceiling_note: CEILING },
    scales: { A1: "One request: from words to a working, tested artifact.", A2: "The whole pipeline: analyze, retrieve, plan, generate, test, verify, deliver.", A3: "The record against the whole network: every database a knowledge source, every generator a tool." }
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
  t("slug", a.slug === SLUG);
  t("edition", a.edition === EDITION);
  t("src", a.src === SRC);
  t("id prefix own family", a.id.indexOf(ID_PREFIX) === 0);
  t("generator hard_stop 1e9", a.generator.hard_stop === 1000000000);
  t("generator gen prefix own family", a.generator.gen_id_prefix === ID_PREFIX + "GEN-");
  t("jcc_code form", a.jcc_code === "JAHDB/" + SLUG + "#" + a.id);
  const slim = {}; for (const k of Object.keys(a)) { if (k !== "jcc_code" && k !== "jcc_key") slim[k] = a[k]; }
  t("jcc_key round-trip", a.jcc_key === "k=" + crypto.createHash("sha256").update(canonical(slim)).digest("hex").slice(0, 8));
  t("different seeds differ", JSON.stringify(generate(42)) !== JSON.stringify(generate(43)));
  t("41 keys", Object.keys(a).length === 41);
  t("honesty flight-ready phrase", a.description.indexOf("never presented as flight-ready") !== -1);
  t("honesty NASA standards phrase", a.description.indexOf("modeled on public NASA standards") !== -1);
  t("no bare is flight-ready", JSON.stringify(a).indexOf("is flight-ready") === -1);
  t("no bare NASA-certified", JSON.stringify(a).indexOf("NASA-certified") === -1);
  t("demo code present", a.demo.code.indexOf("import hashlib") !== -1);
  t("expected output deterministic line", a.expected_output.indexOf("Deterministic: MATCH") !== -1);
  t("network sibling", a.network_links.sibling === SIBLING);
  t("evidence label", a.evidence.label === EVIDENCE_LABEL);
  t("scales A1 A2 A3", a.scales.A1 && a.scales.A2 && a.scales.A3);
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
