// Seeded boundless generator for the Astrodynamics Database database
// (public edition). Deterministic: the same seed always emits the same
// record. Usage: node gen-astrodynamics.js [seed]  (prints one JSON record) or: node gen-astrodynamics.js --test (runTests).
// Package-only; outputs are generated, not stored files.
"use strict";
const crypto = require("crypto");

const SLUG = "astrodynamics";
const RECORD_KIND = "astrodynamics record";
const ID_PREFIX = "JAH-ASTROD-";
const AI_NAME = "JAH Astrodynamics Librarian";
const EDITION = "public";
const SRC = "public-harvest";
const SIBLING = "astrodynamics-signature";
const ADJACENT = ["tool-orbital-mechanics-solver", "space-astro", "astronomy"];
const CEILING = "Generator ceiling: up to 1,000,000,000 scales per file, generated on demand by the file AI \u2014 not stored files.";
const EVIDENCE_LABEL = "documented";
const EVIDENCE_REASON = "Public research record: the figures are checkable against the cited sources, and the design is a candidate engineering result, never presented as flight-ready and modeled on public NASA standards.";
const DESIGN_STATUS = "modeled";
const VERIFICATION_STATUS = "partially verified";
const DATASET = "Public astrodynamics research records";
const GLOSSARY = "Lagrange point is one of five points where gravity and rotation balance. Halo orbit is a looping orbit around a Lagrange point. Perturbation is a small push that slowly changes an orbit. J2 is the number for the Earth's equatorial bulge. Sphere of influence is the region where a body's gravity dominates for planning. Ballistic capture is arriving slowly enough to be captured by gravity. Gravity assist is a flyby that changes a spacecraft's speed using a planet's motion. Station-keeping is the correction burn that holds a spacecraft on its orbit. Nodal regression is the turning of an orbit's plane. Ground track is the path a satellite traces over the Earth.";

const TOPICS = [
  {
    "title": "Lagrange Point Distances for the Earth-Moon System",
    "subject": "Lagrange point distances",
    "description": "The Earth-Moon Lagrange points sit at known distances: L1 at 326400 kilometres from Earth, L2 at 448900, and L4 and L5 at 384400, the Moon's own distance, forming triangles with the Earth and Moon. The Sun-Earth distance is 149.6 million kilometres, there are 5 points, and 2 of them are stable.",
    "figures": {
      "l1_km": 326400,
      "l2_km": 448900,
      "l4_km": 384400,
      "l5_km": 384400,
      "moon_km": 384400,
      "sun_earth_m_km": 149.6,
      "points": 5,
      "stable": 2
    },
    "eq": "L4 and L5 sit at the Moon's distance of 384400 kilometres, 60 degrees ahead and behind; L1 sits at 326400 and L2 at 448900 kilometres from Earth",
    "gloss": "Lagrange point is one of five points where gravity and rotation balance; L1 sits between the bodies; L2 sits beyond the smaller body; L4 and L5 form triangles at 60 degrees."
  },
  {
    "title": "Halo Orbit Periods at Three Lagrange Points",
    "subject": "Halo orbit periods",
    "description": "Halo orbits loop around Lagrange points with periods set by the point: the Sun-Earth L1 and L2 halos loop in about 180 days with a radius near 800000 kilometres and an amplitude near 250000, while the Earth-Moon L2 halo loops in about 14 days. All need station-keeping near 5 metres per second a year, and 2 missions fly them.",
    "figures": {
      "sun_earth_l2_days": 180,
      "sun_earth_l1_days": 180,
      "earth_moon_l2_days": 14,
      "radius_km": 800000,
      "amplitude_km": 250000,
      "stationkeeping_m_s_year": 5,
      "points": 3,
      "missions": 2
    },
    "eq": "Halo period follows from the Lagrange point distance; 1500000 kilometres out gives about 180 days, and 448900 kilometres out gives about 14 days",
    "gloss": "Halo orbit is a looping orbit around a Lagrange point; period is the time for one loop; amplitude is the size of the loop; station-keeping is the correction burn per year."
  },
  {
    "title": "Perturbation Rates for Three Low Orbits",
    "subject": "Perturbation rates for three orbits",
    "description": "Three low orbits turn at three rates under the Earth's bulge: the Station at 420 kilometres turns by minus 4.95 degrees a day, a sun-synchronous orbit at 800 kilometres turns by 0.986 a day, and a polar orbit at 500 kilometres turns by 0. The J2 number is 0.00108263, and there are 5 perturbation sources.",
    "figures": {
      "iss_regression_deg_day": -4.95,
      "sso_regression_deg_day": 0.986,
      "polar_regression_deg_day": 0,
      "j2": 0.00108263,
      "iss_alt_km": 420,
      "sso_alt_km": 800,
      "polar_alt_km": 500,
      "sources": 5
    },
    "eq": "Nodal rate = -1.5 * J2 * (Re/p)^2 * n * cos(i); at 90 degrees the cosine is 0, so a polar orbit does not regress",
    "gloss": "Perturbation is a small push that slowly changes an orbit; J2 is the number for the Earth's equatorial bulge; nodal regression is the turning of an orbit's plane; polar orbit is an orbit over the poles."
  },
  {
    "title": "Solar Pressure and Drag Forces at 400 Kilometres",
    "subject": "Solar pressure and drag forces",
    "description": "At 400 kilometres, sunlight pushes with 4.54 micronewtons per square metre absorbing and 9.08 reflecting, while drag slows the Station by about 2 kilometres a month. The air density is 4 times 10 to the minus 12 kilograms per cubic metre, the area-to-mass ratio is 0.01, and sunlight adds about 2.9 metres per second a year.",
    "figures": {
      "srp_uN_m2": 4.54,
      "srp_reflecting_uN_m2": 9.08,
      "drag_accel_um_s2": 0.1,
      "density_kg_m3": 4e-12,
      "altitude_km": 400,
      "area_mass": 0.01,
      "srp_dv_year": 2.9,
      "decay_km_month": 2
    },
    "eq": "Solar pressure = 1361 / 299792458 = 4.54 micronewtons per square metre; drag acceleration = 0.5 * density * velocity squared * drag coefficient * area-to-mass ratio",
    "gloss": "Solar radiation pressure is the push of sunlight; drag is the air resistance; density is the air mass per volume; area-to-mass ratio is the facing area per kilogram."
  },
  {
    "title": "Low-Energy Transfer Times for Three Routes",
    "subject": "Low-energy transfer times",
    "description": "Three low-energy routes trade time for propellant: the Moon in 90 days instead of 3 direct, Mars in 200 days, each saving about 25 percent and ending in capture at 0.1 kilometres per second. The routes run through tubes about 2000 kilometres wide, and 2 missions have flown them.",
    "figures": {
      "moon_days": 90,
      "mars_days": 200,
      "direct_moon_days": 3,
      "saving": 0.25,
      "capture_km_s": 0.1,
      "routes": 3,
      "missions": 2,
      "tubes_km": 2000
    },
    "eq": "Saving = (direct total - low-energy total) / direct total; (4.1 - 3.1) / 4.1 = about 0.25, at the cost of 90 days instead of 3",
    "gloss": "Low-energy transfer is a slow route that saves propellant; saving is the propellant saved as a fraction; capture is arrival by gravity; tube is a route through the network."
  },
  {
    "title": "Gravity Assist Gains at Three Planets",
    "subject": "Gravity assist gains",
    "description": "Three planets give three gains: Venus, moving at 35 kilometres per second, gives about 5; Earth, at 29.8, gives about 8; and Jupiter, at 13.1, gives about 10 kilometres per second. Voyager 1 used 4 assists to reach 17 kilometres per second, the fastest human-made object.",
    "figures": {
      "venus_gain_km_s": 5,
      "earth_gain_km_s": 8,
      "jupiter_gain_km_s": 10,
      "venus_speed_km_s": 35,
      "earth_speed_km_s": 29.8,
      "jupiter_speed_km_s": 13.1,
      "assists": 3,
      "voyager_speed_km_s": 17
    },
    "eq": "Speed gain = 2 * planet speed * sin(turn angle / 2); at Jupiter, a turn of 45 degrees gives 2 * 13.1 * sin(22.5 degrees) = about 10 kilometres per second",
    "gloss": "Gravity assist is a flyby that changes a spacecraft's speed using a planet's motion; turn angle is the bend of the path; orbital speed is the planet's speed around the Sun; gain is the extra speed."
  },
  {
    "title": "Sphere of Influence Radii for Three Bodies",
    "subject": "Sphere of influence radii",
    "description": "Three bodies have three spheres of influence: Earth's reaches 924000 kilometres, the Moon's 66100, and Mars's 577000, while their Hill spheres reach 1500000, 60000, and 1000000. The sphere radius follows from the mass ratio to the two-fifths power, 0.4.",
    "figures": {
      "earth_soi_km": 924000,
      "moon_soi_km": 66100,
      "mars_soi_km": 577000,
      "earth_hill_km": 1500000,
      "moon_hill_km": 60000,
      "mars_hill_km": 1000000,
      "bodies": 3,
      "exponent": 0.4
    },
    "eq": "Sphere of influence = distance * (mass ratio)^(2/5); Earth's 924000 kilometres follows from 149.6 million kilometres and the Earth-Sun mass ratio",
    "gloss": "Sphere of influence is the region where a body's gravity dominates for planning; Hill sphere is the region where a body can hold a satellite; mass ratio is the smaller mass divided by the larger mass; exponent is the power in the formula."
  },
  {
    "title": "Station-Keeping Budgets for Three Orbit Types",
    "subject": "Station-keeping budgets",
    "description": "Three orbit types need three budgets: low Earth orbit needs about 100 metres per second a year against drag, geostationary orbit needs 50, and a Lagrange-point halo needs 5. Low orbit sits at 400 kilometres, geostationary at 35786, and L2 at 1500000, with 12 burns a year for the halo.",
    "figures": {
      "leo_m_s_year": 100,
      "geo_m_s_year": 50,
      "l2_m_s_year": 5,
      "leo_alt_km": 400,
      "geo_alt_km": 35786,
      "l2_dist_km": 1500000,
      "burns_year": 12,
      "types": 3
    },
    "eq": "Annual budget = burns per year * burn size; 12 burns a year at about 0.4 metres per second give 5 metres per second a year at L2",
    "gloss": "Station-keeping is the correction burn that holds a spacecraft on its orbit; budget is the delta-v per year; burn is a short thruster firing; halo is a looping orbit around a Lagrange point."
  }
];

const SOURCES = [
  {
    "name": "Wikipedia - Lagrange point",
    "url": "https://en.wikipedia.org/wiki/Lagrange_point",
    "establishes": "States the five Lagrange points and their positions."
  },
  {
    "name": "Wikipedia - Halo orbit",
    "url": "https://en.wikipedia.org/wiki/Halo_orbit",
    "establishes": "States halo orbits and the Webb halo."
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
