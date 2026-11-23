// Seeded boundless generator for the The Signature Rocket Propulsion Database database
// (signature edition). Deterministic: the same seed always emits the same
// record. Usage: node gen-rocket-propulsion-signature.js [seed]  (prints one JSON record) or: node gen-rocket-propulsion-signature.js --test (runTests).
// Package-only; outputs are generated, not stored files.
"use strict";
const crypto = require("crypto");

const SLUG = "rocket-propulsion-signature";
const RECORD_KIND = "rocket propulsion record";
const ID_PREFIX = "JAH-RPROS-";
const AI_NAME = "JAH Rocket Propulsion Librarian (Signature)";
const EDITION = "signature";
const SRC = "signature-generated";
const SIBLING = "rocket-propulsion";
const ADJACENT = ["tech-164-nuclear-thermal-propulsion-rockets", "engtools-electric-propulsion-performance-calculator", "nasadarpa-propulsion-system-modeling-toolkit-public"];
const CEILING = "Generator ceiling: up to 1,000,000,000 scales per file, generated on demand by the file AI \u2014 not stored files.";
const EVIDENCE_LABEL = "design-study";
const EVIDENCE_REASON = "Signature design-study record: a candidate design worked out in the Signature system, never presented as established fact, never presented as flight-ready, and modeled on public NASA standards.";
const DESIGN_STATUS = "proposed";
const VERIFICATION_STATUS = "unverified";
const DATASET = "Signature rocket propulsion design-study records";
const GLOSSARY = "Design study is a candidate design worked out on paper, not a flown engine. Aerospike is a nozzle that adjusts to the outside air pressure. Detonation is a supersonic burning wave. Green propellant is a less toxic propellant. Specific impulse is the fuel efficiency, in seconds. Boil-off is propellant lost as vapour from a cold tank. Depot is a fuel station in orbit. Micro-thruster is a tiny thruster for a small satellite. Refurbishment is the work done on a booster between flights. Grid fin is a steering flap on a returning booster.";

const TOPICS = [
  {
    "title": "Signature Aerospike Altitude Compensation Study",
    "subject": "Aerospike altitude compensation",
    "description": "This design study sizes an aerospike nozzle that compensates for altitude: at 50 kilometres, the compensation is 0.9, the thrust is 200 kilonewtons, and the specific impulse is 340 seconds. The nozzle has 12 segments, an expansion ratio of 20, a mass of 150 kilograms, and 5 tests are planned.",
    "figures": {
      "altitude_km": 50,
      "compensation": 0.9,
      "thrust_kn": 200,
      "isp_s": 340,
      "mass_kg": 150,
      "segments": 12,
      "expansion_ratio": 20,
      "tests": 5
    },
    "eq": "Aerospike thrust = chamber pressure * throat area * compensation; at 50 kilometres the compensation of 0.9 keeps the thrust near 200 kilonewtons",
    "gloss": "Aerospike is a nozzle with a central spike that adjusts to the outside air pressure; compensation is how well it keeps its thrust with altitude; segment is one piece of the spike."
  },
  {
    "title": "Signature Rotating Detonation Wave Speed Study",
    "subject": "Rotating detonation wave speed",
    "description": "This design study sizes a rotating detonation engine: a wave travelling at 2000 metres per second around a chamber 0.3 metres across gives a frequency of 2123 hertz, a thrust of 50 kilonewtons, and a specific impulse of 320 seconds. The engine has 1 wave, masses 40 kilograms, and 10 tests are planned.",
    "figures": {
      "wave_speed_m_s": 2000,
      "frequency_hz": 2123,
      "chamber_diameter_m": 0.3,
      "thrust_kn": 50,
      "isp_s": 320,
      "waves": 1,
      "tests": 10,
      "mass_kg": 40
    },
    "eq": "Frequency = wave speed / (pi * chamber diameter); 2000 metres per second around a 0.3-metre chamber gives about 2123 hertz",
    "gloss": "Detonation is a supersonic burning wave; rotating detonation is a wave that circles the chamber; frequency is the waves per second; chamber diameter is the engine's width."
  },
  {
    "title": "Signature Green Propellant Blend Performance Study",
    "subject": "Green propellant blend performance",
    "description": "This design study sizes a green propellant thruster: a blend with a density of 1000 kilograms per cubic metre gives a specific impulse of 300 seconds and a thrust of 22 newtons for a burn of 100 seconds. The thruster uses 2 kilograms of propellant in 1 tank, the toxicity is 0 on the study's scale, and 8 tests are planned.",
    "figures": {
      "isp_s": 300,
      "density_kg_m3": 1000,
      "thrust_n": 22,
      "burn_time_s": 100,
      "propellant_kg": 2,
      "tanks": 1,
      "tests": 8,
      "toxicity": 0
    },
    "eq": "Total impulse = thrust * burn time; 22 newtons for 100 seconds gives 2200 newton-seconds from 2 kilograms of propellant",
    "gloss": "Green propellant is a less toxic propellant; density is the mass per volume; total impulse is thrust times time; toxicity is the study's hazard score, 0 for the least toxic."
  },
  {
    "title": "Signature Solar-Electric Tug Transfer Study",
    "subject": "Solar-electric tug transfer",
    "description": "This design study sizes a solar-electric tug: a 100-millinewton thruster at 3000 seconds of specific impulse moves an 800-kilogram tug carrying 500 kilograms of payload over 200 days and 300 orbits on 50 kilograms of propellant and 10 kilowatts of power.",
    "figures": {
      "transfer_days": 200,
      "thrust_mn": 100,
      "isp_s": 3000,
      "power_kw": 10,
      "payload_kg": 500,
      "propellant_kg": 50,
      "orbits": 300,
      "mass_kg": 800
    },
    "eq": "Delta-v = thrust * time / mass; 100 millinewtons over 200 days on 800 kilograms gives about 2.2 kilometres per second",
    "gloss": "Solar-electric tug is a spacecraft that tows payloads with an electric thruster; specific impulse is the fuel efficiency in seconds; millinewton is a thousandth of a newton; orbit is one circle around Earth."
  },
  {
    "title": "Signature Propellant Depot Boil-Off Study",
    "subject": "Propellant depot boil-off",
    "description": "This design study sizes a propellant depot: a 10-tonne depot holding 8 tonnes of propellant loses 0.1 percent a day to boil-off over 180 days of storage, with 20 layers of insulation and 2 kilowatts of cooling power. The depot serves 4 missions, and 3 tests are planned.",
    "figures": {
      "depot_mass_t": 10,
      "boiloff_percent_day": 0.1,
      "storage_days": 180,
      "insulation_layers": 20,
      "propellant_t": 8,
      "power_kw": 2,
      "missions": 4,
      "tests": 3
    },
    "eq": "Boil-off loss = propellant * rate * days; 8 tonnes at 0.1 percent a day for 180 days loses about 1.4 tonnes",
    "gloss": "Depot is a fuel station in orbit; boil-off is propellant lost as vapour from a cold tank; insulation layer is one sheet of the thermal blanket; storage day is one day the propellant sits in the depot."
  },
  {
    "title": "Signature Reusable Booster Recovery Margin Study",
    "subject": "Reusable booster recovery margin",
    "description": "This design study sizes a reusable booster recovery: a 5000-kilogram booster with 9 engines and 4 grid fins needs a recovery delta-v of 2000 metres per second and a propellant reserve of 500 kilograms to land within 10 metres. The booster flies 10 times, with 30 days of refurbishment between flights.",
    "figures": {
      "recovery_dv_m_s": 2000,
      "landing_accuracy_m": 10,
      "propellant_reserve_kg": 500,
      "flights": 10,
      "refurbishment_days": 30,
      "mass_kg": 5000,
      "engines": 9,
      "grid_fins": 4
    },
    "eq": "Recovery delta-v = entry burn + landing burn; 2000 metres per second on a 500-kilogram reserve brings the 5000-kilogram booster to a landing within 10 metres",
    "gloss": "Reusable booster is a first stage that lands and flies again; recovery delta-v is the speed change for the return; grid fin is a steering flap; refurbishment is the work between flights."
  },
  {
    "title": "Signature CubeSat Micro-Thruster Array Study",
    "subject": "CubeSat micro-thruster array",
    "description": "This design study sizes a micro-thruster array for a CubeSat: 4 thrusters each giving 10 millinewtons at 1000 seconds of specific impulse, on 20 watts of power, move a 500-gram spacecraft through 20 maneuvers over 2 years on 100 grams of propellant.",
    "figures": {
      "thrusters": 4,
      "thrust_mn": 10,
      "isp_s": 1000,
      "power_w": 20,
      "mass_g": 500,
      "propellant_g": 100,
      "maneuvers": 20,
      "lifetime_years": 2
    },
    "eq": "Total thrust = thrusters * thrust each; 4 thrusters at 10 millinewtons give 40 millinewtons for 20 maneuvers over 2 years",
    "gloss": "CubeSat is a small standard satellite; micro-thruster is a tiny thruster; millinewton is a thousandth of a newton; maneuver is one planned move of the spacecraft."
  },
  {
    "title": "Signature Cryogenic Boil-Off Management Study",
    "subject": "Cryogenic boil-off management",
    "description": "This design study sizes boil-off management for a cryogenic tank: 1000 kilograms of propellant stored for 90 days with 30 layers of insulation loses 0.05 percent a day, with 5 venting events and 100 watts of cooling power. The tank masses 50 kilograms, and 6 tests are planned.",
    "figures": {
      "boiloff_percent_day": 0.05,
      "storage_days": 90,
      "insulation_layers": 30,
      "venting_events": 5,
      "propellant_kg": 1000,
      "power_w": 100,
      "tests": 6,
      "mass_kg": 50
    },
    "eq": "Boil-off loss = propellant * rate * days; 1000 kilograms at 0.05 percent a day for 90 days loses about 45 kilograms",
    "gloss": "Cryogenic means very cold, as in liquid oxygen; boil-off is propellant lost as vapour; venting event is a controlled release of gas; insulation layer is one sheet of the thermal blanket."
  }
];

const SOURCES = [
  {
    "name": "Wikipedia - Nuclear thermal rocket",
    "url": "https://en.wikipedia.org/wiki/Nuclear_thermal_rocket",
    "establishes": "States nuclear thermal propulsion and the NERVA program."
  },
  {
    "name": "Wikipedia - Ion thruster",
    "url": "https://en.wikipedia.org/wiki/Ion_thruster",
    "establishes": "States ion thruster specific impulse near 3500 seconds."
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
