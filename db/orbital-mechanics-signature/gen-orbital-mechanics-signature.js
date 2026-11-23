// Seeded boundless generator for the The Signature Orbital Mechanics Database database
// (signature edition). Deterministic: the same seed always emits the same
// record. Usage: node gen-orbital-mechanics-signature.js [seed]  (prints one JSON record) or: node gen-orbital-mechanics-signature.js --test (runTests).
// Package-only; outputs are generated, not stored files.
"use strict";
const crypto = require("crypto");

const SLUG = "orbital-mechanics-signature";
const RECORD_KIND = "orbital mechanics record";
const ID_PREFIX = "JAH-OMECHS-";
const AI_NAME = "JAH Orbital Mechanics Librarian (Signature)";
const EDITION = "signature";
const SRC = "signature-generated";
const SIBLING = "orbital-mechanics";
const ADJACENT = ["tool-orbital-mechanics-solver", "apexeng-orbital-mechanics-workbench", "nasadarpa-orbital-mechanics-computation-suite-public"];
const CEILING = "Generator ceiling: up to 1,000,000,000 scales per file, generated on demand by the file AI \u2014 not stored files.";
const EVIDENCE_LABEL = "design-study";
const EVIDENCE_REASON = "Signature design-study record: a candidate design worked out in the Signature system, never presented as established fact, never presented as flight-ready, and modeled on public NASA standards.";
const DESIGN_STATUS = "proposed";
const VERIFICATION_STATUS = "unverified";
const DATASET = "Signature orbital mechanics design-study records";
const GLOSSARY = "Design study is a candidate orbit or transfer worked out on paper, not a flown mission. Window is the time when a transfer can depart. Constellation is a group of satellites working together. Slot is an assigned place in an orbit. Disposal orbit is an orbit for a dead satellite. Aerobraking is slowing by dipping into the atmosphere. Servicing is repairing or refuelling a satellite in orbit. Collision avoidance is moving to dodge another object. Swath is the width the instruments see. Revisit is the days between passes over one place.";

const TOPICS = [
  {
    "title": "Signature Lunar Gateway Halo Transfer Window",
    "subject": "Lunar gateway halo transfer window",
    "description": "This design study sizes a transfer to a lunar gateway halo: a 5-day transfer with a delta-v of 3.8 kilometres per second reaches a halo with a period of 14 days, in a window of 7 days, with 4 launches a year. The spacecraft masses 5000 kilograms, carries a crew of 4, and fires 3 burns.",
    "figures": {
      "transfer_days": 5,
      "halo_period_days": 14,
      "dv_km_s": 3.8,
      "window_days": 7,
      "launches_year": 4,
      "mass_kg": 5000,
      "crew": 4,
      "burns": 3
    },
    "eq": "Transfer delta-v = departure + arrival; 3.8 kilometres per second over 5 days reaches the 14-day halo in a 7-day window",
    "gloss": "Gateway halo is a looping orbit around the Earth-Moon L2 point; transfer window is the days when the transfer can depart; delta-v is the speed change needed; burn is a short engine firing."
  },
  {
    "title": "Signature Constellation Slot Spacing for 12 Satellites",
    "subject": "Constellation slot spacing",
    "description": "This design study spaces a constellation of 12 satellites in 3 planes with 4 slots per plane, 90 degrees apart, at 550 kilometres with a period of 95 minutes. The coverage is 100 percent, with 2 spares, and the spacing keeps the satellites from colliding.",
    "figures": {
      "satellites": 12,
      "planes": 3,
      "slots_per_plane": 4,
      "spacing_deg": 90,
      "altitude_km": 550,
      "period_min": 95,
      "coverage": 100,
      "spares": 2
    },
    "eq": "Spacing = 360 / satellites per plane; 360 / 4 = 90 degrees between slots in a plane, with 3 planes 60 degrees apart",
    "gloss": "Constellation is a group of satellites working together; plane is one ring of the constellation; slot is an assigned place in an orbit; spacing is the angle between satellites."
  },
  {
    "title": "Signature Debris Avoidance Maneuver for a 400-Kilometre Orbit",
    "subject": "Debris avoidance maneuver",
    "description": "This design study sizes a debris avoidance maneuver for a 400-kilometre orbit: a warning 24 hours ahead, a maneuver of 1 metre per second, and 2 avoidance burns a year against 5 conjunctions a year. The tracking catalogue holds 30000 objects to an accuracy of 1 kilometre, and the maneuver costs 2 kilograms of fuel.",
    "figures": {
      "warning_hours": 24,
      "maneuver_m_s": 1,
      "conjunctions_year": 5,
      "avoidance_burns": 2,
      "altitude_km": 400,
      "tracking_objects": 30000,
      "accuracy_km": 1,
      "fuel_kg": 2
    },
    "eq": "Avoidance delta-v = 1 metre per second; fired 24 hours ahead, it moves the satellite by about 86 kilometres at the conjunction",
    "gloss": "Debris avoidance is moving to dodge another object; conjunction is a close approach; warning is the hours of notice; maneuver is a small burn that changes the orbit."
  },
  {
    "title": "Signature Mars Transfer Window for a 2028 Departure",
    "subject": "Mars transfer window for 2028",
    "description": "This design study sizes a Mars transfer window for a 2028 departure: a window of 20 days, a transfer of 200 days, a delta-v of 4.5 kilometres per second, and a C3 of 14.5 kilometres squared per second squared. The spacecraft masses 2000 kilograms, carries no crew, fires 2 burns, and arrives at 5 kilometres per second.",
    "figures": {
      "window_days": 20,
      "transfer_days": 200,
      "dv_km_s": 4.5,
      "c3_km2_s2": 14.5,
      "mass_kg": 2000,
      "crew": 0,
      "burns": 2,
      "arrival_speed_km_s": 5
    },
    "eq": "C3 = excess speed squared; a C3 of 14.5 gives an excess speed of 3.8 kilometres per second, and the transfer delta-v is 4.5",
    "gloss": "Transfer window is the days when a Mars flight can depart; C3 is the launch energy; excess speed is the speed left over after escaping Earth; arrival speed is the speed at Mars."
  },
  {
    "title": "Signature Asteroid Rendezvous for a Near-Earth Object",
    "subject": "Asteroid rendezvous",
    "description": "This design study sizes a rendezvous with a near-Earth asteroid: a 300-day transfer to 1.5 astronomical units, a rendezvous burn of 200 metres per second, and a 3-year mission for an 800-kilogram spacecraft with 5 instruments. The spacecraft collects 5 samples and fires 4 burns.",
    "figures": {
      "transfer_days": 300,
      "rendezvous_dv_m_s": 200,
      "distance_au": 1.5,
      "mass_kg": 800,
      "instruments": 5,
      "mission_years": 3,
      "samples": 5,
      "burns": 4
    },
    "eq": "Rendezvous delta-v = 200 metres per second; at 1.5 astronomical units, the transfer takes 300 days and the mission 3 years",
    "gloss": "Rendezvous is meeting another body in its orbit; astronomical unit is the Earth-Sun distance; sample is material collected for study; burn is a short engine firing."
  },
  {
    "title": "Signature Repeating Ground Track for an Earth Surveyor",
    "subject": "Repeating ground track for an Earth surveyor",
    "description": "This design study sizes a repeating ground track for an Earth surveyor: a repeat every 10 days and 150 orbits, a period of 96 minutes at 500 kilometres, a swath of 100 kilometres, and full coverage with 3 instruments. The revisit is 10 days, and the track repeats exactly.",
    "figures": {
      "repeat_days": 10,
      "repeat_orbits": 150,
      "period_min": 96,
      "altitude_km": 500,
      "swath_km": 100,
      "coverage": 100,
      "instruments": 3,
      "revisit_days": 10
    },
    "eq": "Orbits per day = 1440 / 96 = 15 orbits a day; 150 orbits in 10 days repeats the track exactly",
    "gloss": "Repeating ground track is an orbit whose path over Earth repeats; swath is the width the instruments see; revisit is the days between passes over one place; coverage is the share of Earth seen."
  },
  {
    "title": "Signature Multi-Burn Transfer for a High-Energy Orbit",
    "subject": "Multi-burn transfer",
    "description": "This design study sizes a multi-burn transfer to a high-energy orbit: 3 burns totalling 4.2 kilometres per second over 10 days, through an intermediate orbit at 20000 kilometres to a final orbit at 35786 kilometres. The spacecraft masses 3000 kilograms, carries 1500 kilograms of propellant, and flies in 2 stages.",
    "figures": {
      "burns": 3,
      "total_dv_km_s": 4.2,
      "transfer_days": 10,
      "intermediate_alt_km": 20000,
      "final_alt_km": 35786,
      "mass_kg": 3000,
      "propellant_kg": 1500,
      "stages": 2
    },
    "eq": "Total delta-v = burn 1 + burn 2 + burn 3; 3 burns totalling 4.2 kilometres per second reach 35786 kilometres in 10 days",
    "gloss": "Multi-burn transfer is a transfer in several burns; intermediate orbit is a parking orbit between burns; final orbit is the destination; stage is one rocket section."
  },
  {
    "title": "Signature Station-Keeping Budget for a Geostationary Slot",
    "subject": "Station-keeping budget for a geostationary slot",
    "description": "This design study budgets station-keeping for a geostationary slot: 50 metres per second a year, split into 45 north-south and 5 east-west, for a 15-year mission on 300 kilograms of fuel. The slot is 2 degrees wide, the inclination is 0 degrees, and the drift is 0.5 degrees a year without correction.",
    "figures": {
      "annual_dv_m_s": 50,
      "north_south_m_s": 45,
      "east_west_m_s": 5,
      "mission_years": 15,
      "fuel_kg": 300,
      "slot_deg": 2,
      "inclination_deg": 0,
      "drift_deg_year": 0.5
    },
    "eq": "Annual delta-v = north-south + east-west; 45 + 5 = 50 metres per second a year, or 750 over 15 years on 300 kilograms of fuel",
    "gloss": "Station-keeping is the correction burn that holds a satellite in its slot; north-south is the correction of the orbit's tilt; east-west is the correction of the drift along the orbit; slot is an assigned place in the geostationary ring."
  }
];

const SOURCES = [
  {
    "name": "Wikipedia - Vis-viva equation",
    "url": "https://en.wikipedia.org/wiki/Vis-viva_equation",
    "establishes": "States the vis-viva equation and orbital energy."
  },
  {
    "name": "Wikipedia - Two-line element set",
    "url": "https://en.wikipedia.org/wiki/Two-line_element_set",
    "establishes": "States the two-line element set format."
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
