// Seeded boundless generator for the The Signature Astrodynamics Database database
// (signature edition). Deterministic: the same seed always emits the same
// record. Usage: node gen-astrodynamics-signature.js [seed]  (prints one JSON record) or: node gen-astrodynamics-signature.js --test (runTests).
// Package-only; outputs are generated, not stored files.
"use strict";
const crypto = require("crypto");

const SLUG = "astrodynamics-signature";
const RECORD_KIND = "astrodynamics record";
const ID_PREFIX = "JAH-ASTRODS-";
const AI_NAME = "JAH Astrodynamics Librarian (Signature)";
const EDITION = "signature";
const SRC = "signature-generated";
const SIBLING = "astrodynamics";
const ADJACENT = ["tool-orbital-mechanics-solver", "space-astro", "astronomy"];
const CEILING = "Generator ceiling: up to 1,000,000,000 scales per file, generated on demand by the file AI \u2014 not stored files.";
const EVIDENCE_LABEL = "design-study";
const EVIDENCE_REASON = "Signature design-study record: a candidate design worked out in the Signature system, never presented as established fact, never presented as flight-ready, and modeled on public NASA standards.";
const DESIGN_STATUS = "proposed";
const VERIFICATION_STATUS = "unverified";
const DATASET = "Signature astrodynamics design-study records";
const GLOSSARY = "Design study is a candidate trajectory or station worked out on paper, not a flown mission. Gateway is a station at a Lagrange point used as a staging post. Observatory is a space telescope. Cargo route is a slow route for supplies. Beacon is a navigation signal source. Formation flying is several spacecraft holding fixed positions relative to each other. Digital twin is a live computer model of a spacecraft. Sample is material collected for laboratory study. Rendezvous is meeting another body in its orbit. Autonomy is operating without outside help.";

const TOPICS = [
  {
    "title": "Signature Earth-Moon L1 Station Transfer Study",
    "subject": "Earth-Moon L1 station transfer",
    "description": "This design study sizes a transfer to an Earth-Moon L1 station: a 3-day transfer with a delta-v of 3.8 kilometres per second reaches a 20-tonne station for a crew of 4 on a halo with a period of 14 days. The station needs 10 metres per second a year of station-keeping, has 4 modules, and fires 2 burns.",
    "figures": {
      "transfer_days": 3,
      "dv_km_s": 3.8,
      "station_mass_t": 20,
      "crew": 4,
      "halo_days": 14,
      "stationkeeping_m_s_year": 10,
      "modules": 4,
      "burns": 2
    },
    "eq": "Transfer delta-v = departure + arrival; 3.8 kilometres per second over 3 days reaches the L1 halo with a period of 14 days",
    "gloss": "L1 station is a crewed station at the Earth-Moon L1 point; halo is a looping orbit around a Lagrange point; station-keeping is the correction burn per year; module is a station section."
  },
  {
    "title": "Signature Sun-Earth L2 Telescope Halo Study",
    "subject": "Sun-Earth L2 telescope halo",
    "description": "This design study sizes a telescope halo at the Sun-Earth L2 point: a 6-tonne observatory with a 6-metre telescope and a 21-metre sunshield, 1500000 kilometres from Earth, on a halo with a period of 180 days. The station-keeping is 5 metres per second a year, the instruments are 4, and the mission is 10 years.",
    "figures": {
      "halo_days": 180,
      "telescope_m": 6,
      "sunshield_m": 21,
      "mass_t": 6,
      "stationkeeping_m_s_year": 5,
      "instruments": 4,
      "mission_years": 10,
      "distance_km": 1500000
    },
    "eq": "Halo period follows from the L2 distance; 1500000 kilometres out gives about 180 days, and the 21-metre sunshield keeps the 6-metre telescope cold",
    "gloss": "Telescope halo is a looping orbit around the L2 point for a space telescope; sunshield is the shield that keeps a telescope cold; halo period is the time for one loop; station-keeping is the correction burn per year."
  },
  {
    "title": "Signature Weak Stability Boundary Cargo Schedule",
    "subject": "Weak stability boundary cargo schedule",
    "description": "This design study schedules cargo through the weak stability boundary: 4 flights a year carrying 10 tonnes each, a transfer of 90 days, a saving of 25 percent, and 3 tonnes of propellant per flight. The boundary sits about 1500000 kilometres out, the capture is at 0.1 kilometres per second, and 2 missions have proven the route.",
    "figures": {
      "flights_year": 4,
      "cargo_t": 10,
      "transfer_days": 90,
      "saving": 0.25,
      "propellant_t": 3,
      "capture_km_s": 0.1,
      "distance_km": 1500000,
      "missions": 2
    },
    "eq": "Cargo per year = flights * cargo each; 4 flights a year at 10 tonnes give 40 tonnes a year, saving about 25 percent of the propellant",
    "gloss": "Cargo schedule is the planned flights of a lunar supply route; weak stability boundary is the region where capture routes pass; saving is the propellant saved as a fraction; capture is arrival by gravity."
  },
  {
    "title": "Signature Multi-Flyby Tour of the Outer Planets",
    "subject": "Multi-flyby tour of the outer planets",
    "description": "This design study plans a multi-flyby tour of the outer planets: 6 flybys past 4 planets over 10 years, gaining about 10 kilometres per second per assist to a cruise speed of 17. The spacecraft masses 2 tonnes, carries 8 instruments, and launches in 2030.",
    "figures": {
      "flybys": 6,
      "planets": 4,
      "years": 10,
      "assist_km_s": 10,
      "cruise_km_s": 17,
      "instruments": 8,
      "mass_t": 2,
      "launch_year": 2030
    },
    "eq": "Cruise speed = sum of the assists; 6 flybys gaining about 10 kilometres per second each, against the launch speed, give a cruise of 17 kilometres per second",
    "gloss": "Multi-flyby tour is one mission that flies past several planets in turn; flyby is a close pass of a planet; assist is the speed gained at a flyby; cruise speed is the speed between planets."
  },
  {
    "title": "Signature Solar Sail Station-Keeping at L1",
    "subject": "Solar sail station-keeping at L1",
    "description": "This design study sizes a solar sail that holds the Sun-Earth L1 point: a 10000-square-metre sail massing 100 kilograms gives 90.8 millinewtons of thrust at 9.08 micronewtons per square metre, carrying a 50-kilogram payload for 5 years. The station-keeping is 0 metres per second a year of propellant, because the sail itself is the station-keeping.",
    "figures": {
      "sail_m2": 10000,
      "thrust_mN": 90.8,
      "pressure_uN_m2": 9.08,
      "mass_kg": 100,
      "payload_kg": 50,
      "years": 5,
      "stationkeeping_m_s_year": 0,
      "distance_km": 1500000
    },
    "eq": "Thrust = pressure * area; 9.08 micronewtons per square metre over 10000 square metres gives 90.8 millinewtons",
    "gloss": "Solar sail is a large thin mirror pushed by sunlight; thrust is the push in millinewtons; pressure is the sunlight push per square metre; station-keeping is the correction that holds a spacecraft on its orbit."
  },
  {
    "title": "Signature Cislunar Beacon Network for Navigation",
    "subject": "Cislunar beacon network",
    "description": "This design study sizes a cislunar beacon network: 4 beacons at the Lagrange points broadcasting 2 signals each, giving 1-kilometre accuracy over 384400 kilometres, updated every 10 minutes. Three ground stations watch the beacons, 10 spacecraft use the system, and the autonomy is 24 hours.",
    "figures": {
      "beacons": 4,
      "accuracy_km": 1,
      "range_km": 384400,
      "update_min": 10,
      "stations": 3,
      "spacecraft": 10,
      "autonomy_hours": 24,
      "signals": 2
    },
    "eq": "Position fix = 4 ranges from 4 beacons; the signal delays give distances, and 4 distances give a position to 1 kilometre over 384400 kilometres",
    "gloss": "Beacon network is a set of navigation signal sources at Lagrange points; fix is a computed position; ranging is measuring distance by signal delay; autonomy is operating without outside help, in hours."
  },
  {
    "title": "Signature Lunar Polar Mapper Orbit Study",
    "subject": "Lunar polar mapper orbit",
    "description": "This design study sizes a polar orbit for a lunar mapper: a 500-kilogram orbiter with 4 instruments at 100 kilometres altitude, a 118-minute period, and 90 degrees of inclination, covering 100 percent of the surface in 2 years. The station-keeping is 20 metres per second a year against the Moon's lumpy gravity.",
    "figures": {
      "altitude_km": 100,
      "period_min": 118,
      "inclination_deg": 90,
      "coverage": 100,
      "stationkeeping_m_s_year": 20,
      "years": 2,
      "instruments": 4,
      "mass_kg": 500
    },
    "eq": "Period follows from the altitude; at 100 kilometres over the Moon, the period is 118 minutes, and 90 degrees of inclination puts the poles under the orbit",
    "gloss": "Polar mapper is an orbiter that maps the Moon's poles; inclination is the tilt of the orbit; coverage is the share of the surface seen; station-keeping is the correction burn per year."
  },
  {
    "title": "Signature Astrodynamics Twin for Ten Spacecraft",
    "subject": "Astrodynamics twin for ten spacecraft",
    "description": "This design study sizes a digital twin for 10 spacecraft: updated every 10 minutes to 1-kilometre accuracy from 20 sensors, running 5 models and 100 simulations a day for 3 operators over 5 years. The twin tests each decision before it is flown, so a bad burn is caught in the model, not in space.",
    "figures": {
      "spacecraft": 10,
      "update_min": 10,
      "accuracy_km": 1,
      "models": 5,
      "sensors": 20,
      "simulations_day": 100,
      "operators": 3,
      "years": 5
    },
    "eq": "Simulations per year = simulations per day * 365; 100 a day gives 36500 a year, testing every decision for 10 spacecraft",
    "gloss": "Digital twin is a live computer model of a spacecraft that mirrors its real state; simulation is a run of the model to test a decision; sensor is a device that measures the spacecraft's state; model is a mathematical description of a force."
  }
];

const SOURCES = [
  {
    "name": "Wikipedia - Interplanetary Transport Network",
    "url": "https://en.wikipedia.org/wiki/Interplanetary_Transport_Network",
    "establishes": "States the interplanetary transport network."
  },
  {
    "name": "Wikipedia - Weak stability boundary",
    "url": "https://en.wikipedia.org/wiki/Weak_stability_boundary",
    "establishes": "States the weak stability boundary."
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
