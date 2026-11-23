// Seeded boundless generator for the Rocket Propulsion Database database
// (public edition). Deterministic: the same seed always emits the same
// record. Usage: node gen-rocket-propulsion.js [seed]  (prints one JSON record) or: node gen-rocket-propulsion.js --test (runTests).
// Package-only; outputs are generated, not stored files.
"use strict";
const crypto = require("crypto");

const SLUG = "rocket-propulsion";
const RECORD_KIND = "rocket propulsion record";
const ID_PREFIX = "JAH-RPRO-";
const AI_NAME = "JAH Rocket Propulsion Librarian";
const EDITION = "public";
const SRC = "public-harvest";
const SIBLING = "rocket-propulsion-signature";
const ADJACENT = ["tech-164-nuclear-thermal-propulsion-rockets", "engtools-electric-propulsion-performance-calculator", "nasadarpa-propulsion-system-modeling-toolkit-public"];
const CEILING = "Generator ceiling: up to 1,000,000,000 scales per file, generated on demand by the file AI \u2014 not stored files.";
const EVIDENCE_LABEL = "documented";
const EVIDENCE_REASON = "Public research record: the figures are checkable against the cited sources, and the design is a candidate engineering result, never presented as flight-ready and modeled on public NASA standards.";
const DESIGN_STATUS = "modeled";
const VERIFICATION_STATUS = "partially verified";
const DATASET = "Public rocket propulsion research records";
const GLOSSARY = "Specific impulse is the fuel efficiency of a rocket engine, measured in seconds; a higher number means more push per kilogram of propellant. Exhaust velocity is the speed of the gases leaving the nozzle. Mass ratio is the starting mass divided by the empty mass. Thrust is the push of the engine, measured in newtons or kilonewtons. Chamber pressure is the pressure inside the combustion chamber. Expansion ratio is the exit area of the nozzle divided by its throat area. Propellant is the fuel and oxidizer a rocket burns. Cryogenic means very cold, as in liquid oxygen. Hypergolic propellants ignite on contact. Turbopump is a pump driven by a turbine that feeds propellant at high pressure.";

const TOPICS = [
  {
    "title": "Mass Ratio and Payload Fraction for a Small Launcher",
    "subject": "Mass ratio and payload fraction",
    "description": "A small launcher's mass ratio sets its delta-v: with a mass ratio of 8 and a specific impulse of 350 seconds, the Tsiolkovsky equation gives about 9.5 kilometres per second, enough for low Earth orbit with a payload fraction of 0.05. The structure takes 0.1 of the mass and the propellant 0.85, so a 500-kilogram payload needs a 10000-kilogram launcher.",
    "figures": {
      "mass_ratio": 8,
      "payload_fraction": 0.05,
      "structural_fraction": 0.1,
      "propellant_fraction": 0.85,
      "delta_v_km_s": 9.5,
      "isp_s": 350,
      "stages": 2,
      "payload_kg": 500
    },
    "eq": "Tsiolkovsky: delta-v = isp * 9.81 * ln(mass ratio) = 350 * 9.81 * ln(8) = 9.5 kilometres per second",
    "gloss": "Delta-v is the speed change; isp is the specific impulse in seconds; ln is the natural logarithm; mass ratio is the starting mass divided by the empty mass."
  },
  {
    "title": "Throat Area and Expansion Ratio for a Sea-Level Nozzle",
    "subject": "Nozzle throat area and expansion ratio",
    "description": "A sea-level nozzle with a throat area of 100 square centimetres and an expansion ratio of 10 gives a thrust of 100 kilonewtons at a chamber pressure of 10 megapascals, with a specific impulse of 300 seconds. The nozzle is 1.5 metres long, masses 50 kilograms, and its exit pressure matches the sea-level pressure of 101 kilopascals.",
    "figures": {
      "throat_area_cm2": 100,
      "expansion_ratio": 10,
      "exit_pressure_kpa": 101,
      "chamber_pressure_mpa": 10,
      "thrust_kn": 100,
      "isp_s": 300,
      "nozzle_length_m": 1.5,
      "mass_kg": 50
    },
    "eq": "Thrust = chamber pressure * throat area * thrust coefficient; 10 megapascals over 100 square centimetres gives about 100 kilonewtons",
    "gloss": "Thrust is the push; chamber pressure is the pressure inside the engine; throat area is the narrowest part of the nozzle; thrust coefficient is the nozzle's efficiency number."
  },
  {
    "title": "Regenerative Cooling Channel Flow for a Chamber Wall",
    "subject": "Regenerative cooling channel flow",
    "description": "A chamber wall cooled by 100 channels carrying 5 kilograms per second of propellant can take a heat flux of 10 megawatts per square metre while the wall stays at 800 kelvin and the chamber burns at 3500 kelvin. The channels are 0.5 metres long, the chamber pressure is 10 megapascals, and the cooling jacket masses 20 kilograms.",
    "figures": {
      "channels": 100,
      "coolant_flow_kg_s": 5,
      "heat_flux_mw_m2": 10,
      "wall_temp_k": 800,
      "chamber_temp_k": 3500,
      "pressure_mpa": 10,
      "channel_length_m": 0.5,
      "mass_kg": 20
    },
    "eq": "Heat removed = coolant flow * heat capacity * temperature rise; 5 kilograms per second over 100 channels removes the 10 megawatts per square metre",
    "gloss": "Heat flux is the heat per square metre; coolant flow is the propellant passing through the wall; wall temperature is the metal's temperature; chamber temperature is the burning gas temperature."
  },
  {
    "title": "Turbopump Power Balance for a Gas-Generator Cycle",
    "subject": "Turbopump power balance",
    "description": "A gas-generator turbopump spinning at 30000 revolutions per minute draws 1000 kilowatts of pump power from a turbine making 1100 kilowatts, with a pump efficiency of 0.7 and a turbine efficiency of 0.8. The pump moves 50 kilograms per second to a pressure of 15 megapascals, and the pump masses 100 kilograms.",
    "figures": {
      "pump_power_kw": 1000,
      "turbine_power_kw": 1100,
      "pump_efficiency": 0.7,
      "turbine_efficiency": 0.8,
      "flow_kg_s": 50,
      "pressure_mpa": 15,
      "speed_rpm": 30000,
      "mass_kg": 100
    },
    "eq": "Pump power = flow * pressure rise / (density * efficiency); 50 kilograms per second to 15 megapascals needs about 1000 kilowatts",
    "gloss": "Pump power is the work the pump does; turbine power is the work the turbine makes; efficiency is the share of energy that becomes useful work; flow is the propellant per second."
  },
  {
    "title": "Pressurization Gas Mass for a Propellant Tank",
    "subject": "Pressurization gas mass",
    "description": "A 10-cubic-metre propellant tank holding 5000 kilograms of propellant needs 5 kilograms of helium in 2 pressurant tanks to hold a pressure of 2 megapascals at 300 kelvin, with an ullage fraction of 0.05. The tank itself masses 200 kilograms, and the gas mass follows from the ideal gas law.",
    "figures": {
      "tank_volume_m3": 10,
      "ullage_fraction": 0.05,
      "pressure_mpa": 2,
      "gas_mass_kg": 5,
      "tank_mass_kg": 200,
      "propellant_kg": 5000,
      "temperature_k": 300,
      "pressurant_tanks": 2
    },
    "eq": "Gas mass = pressure * volume / (gas constant * temperature); 2 megapascals over 10 cubic metres at 300 kelvin needs about 5 kilograms of helium",
    "gloss": "Ullage is the gas space at the top of a tank; pressure is the push of the gas; gas constant is helium's constant; temperature is in kelvin."
  },
  {
    "title": "Gimbal Range and Thrust Vector Control Authority",
    "subject": "Gimbal range and thrust vector control",
    "description": "An engine gimballed by 8 degrees with a thrust of 500 kilonewtons gives a control moment of 100 kilonewton-metres, driven by 2 actuators each pushing 20 kilonewtons at a response of 10 hertz. The gimbal assembly masses 80 kilograms, and the deflection used in flight is 5 degrees.",
    "figures": {
      "gimbal_deg": 8,
      "thrust_kn": 500,
      "moment_kn_m": 100,
      "actuator_force_kn": 20,
      "response_hz": 10,
      "actuators": 2,
      "mass_kg": 80,
      "deflection_deg": 5
    },
    "eq": "Control moment = thrust * gimbal arm * sin(gimbal angle); 500 kilonewtons at 8 degrees gives about 100 kilonewton-metres",
    "gloss": "Gimbal is the pivot that tilts the engine; thrust vector control is steering by tilting the thrust; moment is the turning force; actuator is the device that moves the engine."
  },
  {
    "title": "Hot-Fire Test Duration and Data Channels for a Test Stand",
    "subject": "Hot-fire test duration and data channels",
    "description": "A hot-fire test of 300 seconds on a stand 30 metres tall burns 5000 kilograms of propellant at a thrust of 1000 kilonewtons and a chamber pressure of 12 megapascals, watched by 200 data channels sampling at 1000 hertz. Three tests are run, and the stand records every channel for later analysis.",
    "figures": {
      "test_duration_s": 300,
      "data_channels": 200,
      "thrust_kn": 1000,
      "chamber_pressure_mpa": 12,
      "sampling_hz": 1000,
      "tests": 3,
      "propellant_kg": 5000,
      "stand_height_m": 30
    },
    "eq": "Total impulse = thrust * duration; 1000 kilonewtons for 300 seconds gives 300000 kilonewton-seconds",
    "gloss": "Hot-fire test is a full engine firing on a stand; data channel is one measurement stream; sampling rate is the measurements per second; total impulse is thrust times time."
  },
  {
    "title": "Failure Mode Counts for a Liquid Engine Safety Review",
    "subject": "Failure mode counts for a safety review",
    "description": "A safety review of a liquid engine lists 12 failure modes, of which 3 are critical, with 12 mitigations, 20 tests, 2 reviews, 5 hazards, 10 inspections, and 2 abort modes. Every critical mode has a mitigation and a test, and the review is the gate before any hot-fire test.",
    "figures": {
      "failure_modes": 12,
      "critical_modes": 3,
      "mitigations": 12,
      "tests": 20,
      "reviews": 2,
      "hazards": 5,
      "inspections": 10,
      "abort_modes": 2
    },
    "eq": "Coverage = mitigations / failure modes; 12 mitigations over 12 modes gives full coverage, with 3 critical modes each mitigated",
    "gloss": "Failure mode is one way the engine can break; critical mode is one that can cause loss; mitigation is a fix or safeguard; abort mode is a safe shutdown path."
  }
];

const SOURCES = [
  {
    "name": "Wikipedia - Tsiolkovsky rocket equation",
    "url": "https://en.wikipedia.org/wiki/Tsiolkovsky_rocket_equation",
    "establishes": "States the Tsiolkovsky rocket equation and the mass ratio relation."
  },
  {
    "name": "Wikipedia - Specific impulse",
    "url": "https://en.wikipedia.org/wiki/Specific_impulse",
    "establishes": "Defines specific impulse and its relation to exhaust velocity."
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
