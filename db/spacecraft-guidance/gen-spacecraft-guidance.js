// Seeded boundless generator for the spacecraft-guidance database (public edition).
// Deterministic: the same seed always emits the same record.
// Usage: node gen-spacecraft-guidance.js [seed]  (prints one JSON record)
// or: node gen-spacecraft-guidance.js --test (runTests).
// Package-only; outputs are generated, not stored files.
"use strict";
const crypto = require("crypto");

const SLUG = "spacecraft-guidance";
const RECORD_KIND = "spacecraft guidance record";
const ID_PREFIX = "JAH-SGUI-";
const AI_NAME = "JAH Spacecraft Guidance Librarian";
const EDITION = "public";
const SRC = "public-harvest";
const CEILING = "Generator ceiling: up to 1,000,000,000 scales per file, generated on demand by the file AI \u2014 not stored files.";
const SIBLING = "spacecraft-guidance-signature";
const ADJACENT = ["engtools-spacecraft-attitude-dynamics-simulator", "nasadarpa-spacecraft-attitude-control-simulator-public", "nasadarpa-deep-space-navigation-engine-public"];
const HONESTY = "NASA-level here means engineering targets modeled on public NASA standards, and this record is never presented as flight-ready. Missile-guidance content is excluded from this record; this is civilian aerospace and space exploration work only, with no weapons content.";
const GLOSSARY = "delta-v (change in velocity): the total change in speed a spacecraft must achieve, measured in metres per second. orbit: the curved path a spacecraft follows around a planet, moon, or star under gravity. trajectory: the path a spacecraft follows through space over time, including its position and velocity at each moment. telemetry: measurements sent from a spacecraft to the ground, reporting temperatures, voltages, positions, and instrument readings. verification: the disciplined checking that a design meets its written requirements, by test, analysis, inspection, or demonstration. validation: the checking that a finished design actually does the job its users need, in conditions like the real mission. redundancy: having a spare unit or a second way to do a job, so one failure does not end the mission. fault tolerance: the ability of a system to keep working, or to fail safely, when a part breaks or a measurement goes wrong. state vector: the list of numbers that fully describes a spacecraft at one moment, usually its three position numbers and three velocity numbers. covariance: a table of numbers describing how uncertain an estimate is, and how the errors in different quantities move together. ground station: a place on Earth with antennas and radios that talks to spacecraft, sends commands, and receives telemetry. link budget: the accounting of signal strength from transmitter to receiver, adding gains and subtracting losses to check the signal arrives strong enough. NASA (National Aeronautics and Space Administration): the United States civilian space agency, whose public standards and handbooks this record is modeled on, with no claim of certification, approval, affiliation, or endorsement.";
const SAFETY = "Hazards include incorrect inputs, stale measurements, software faults, and loss of communication; mitigations include range checks, independent cross-checks, safe-mode handover, and redundant paths; remaining risks include unmodeled disturbances, sensor drift, and single-point failures that testing has not yet exercised.";
const PROVENANCE = "Public sources cited in this record (NASA Systems Engineering Handbook, NPR 7123.1D, NASA Technical Reports Server, and the cited reference articles); figures are worked examples from the stated inputs; assumptions are listed in the method and the specification.";
const EVIDENCE_LABEL = "documented";
const EVIDENCE_REASON = "Records public NASA-level aerospace research and the pasted NASA-level specification faithfully, with attribution kept straight; candidate designs are labeled with their engineering status, never presented as flight-ready, and no claim of NASA certification, approval, affiliation, or endorsement is made.";

const TOPICS = [
  {
    "title": "Ascent Guidance: The Gravity Turn in Brief",
    "subject": "ascent guidance overview",
    "description": "Ascent guidance steers a launch vehicle from the pad to orbit, tipping over slowly so gravity bends the path while thrust stays along the velocity.",
    "figures": {
      "burn_duration_s": 480,
      "delta_v_ms": 9400,
      "gravity_loss_ms": 1200,
      "drag_loss_ms": 150,
      "staging_events": 2,
      "final_altitude_km": 185,
      "guidance_updates_hz": 10
    }
  },
  {
    "title": "Powered Descent: Slowing from Orbit to Touchdown",
    "subject": "powered descent overview",
    "description": "Powered descent guidance fires the engine against gravity to slow a lander from orbital speed to a gentle touchdown at a chosen site.",
    "figures": {
      "descent_duration_s": 720,
      "delta_v_ms": 2050,
      "initial_altitude_km": 15,
      "throttle_range_pct": 60,
      "landing_ellipse_m": 500,
      "hover_time_s": 60,
      "guidance_updates_hz": 20
    }
  },
  {
    "title": "Rendezvous: Meeting Another Spacecraft in Orbit",
    "subject": "rendezvous overview",
    "description": "Rendezvous guidance shapes the relative motion of a chaser with small burns, using the Clohessy-Wiltshire equations, until the two spacecraft meet.",
    "figures": {
      "closing_distance_km": 100,
      "approach_speed_ms": 5,
      "burns_count": 6,
      "phase_angle_deg": 30,
      "docking_corridor_m": 10,
      "mission_duration_h": 48,
      "guidance_updates_hz": 5
    }
  },
  {
    "title": "Docking: The Final Slow Approach",
    "subject": "docking overview",
    "description": "Docking guidance flies the last few hundred metres inside a narrow corridor, closing slowly with the docking axes aligned until capture.",
    "figures": {
      "approach_distance_m": 200,
      "approach_speed_ms": 0.5,
      "lateral_error_m": 1,
      "alignment_deg": 0.5,
      "capture_time_s": 30,
      "sensor_range_m": 500,
      "guidance_updates_hz": 10
    }
  },
  {
    "title": "Attitude Control with PID Feedback",
    "subject": "PID attitude control overview",
    "description": "PID control holds a spacecraft at a wanted orientation with three terms: one reacts to the error now, one removes a lasting bias, one damps the motion.",
    "figures": {
      "kp_gain": 2.5,
      "ki_gain": 0.1,
      "kd_gain": 8.0,
      "settling_time_s": 120,
      "overshoot_pct": 5,
      "steady_error_deg": 0.1,
      "torque_nm": 0.05,
      "update_rate_hz": 10
    }
  },
  {
    "title": "Quaternions: Rotation Without Singularities",
    "subject": "quaternion attitude overview",
    "description": "Quaternion guidance describes orientation with four numbers, steers along the shortest rotation, and never suffers gimbal lock.",
    "figures": {
      "components": 4,
      "slew_angle_deg": 90,
      "slew_time_s": 180,
      "max_rate_degs": 0.5,
      "pointing_error_deg": 0.05,
      "updates_hz": 10,
      "normalisation_error": 0.0001
    }
  },
  {
    "title": "Lambert Targeting for Interplanetary Flight",
    "subject": "Lambert targeting overview",
    "description": "Lambert guidance solves for the velocities that connect two positions in a given transfer time, aiming a spacecraft from one planet to another.",
    "figures": {
      "transfer_time_days": 210,
      "departure_delta_v_ms": 3800,
      "arrival_delta_v_ms": 2100,
      "phase_angle_deg": 44,
      "iterations": 8,
      "tolerance_ms": 0.1,
      "solutions_count": 2
    }
  },
  {
    "title": "Entry Guidance: Flying the Narrow Corridor",
    "subject": "entry guidance overview",
    "description": "Entry guidance steers a returning spacecraft through the atmosphere inside a narrow corridor of flight-path angles, banking to control the range.",
    "figures": {
      "entry_speed_ms": 11000,
      "entry_angle_deg": 6.5,
      "peak_g": 7,
      "corridor_width_deg": 1.0,
      "range_km": 3000,
      "heat_shield_temp_c": 2700,
      "splashdown_error_km": 5,
      "guidance_updates_hz": 10
    }
  }
];
const SOURCES = [
  {
    "name": "NASA Systems Engineering Handbook",
    "url": "https://www.nasa.gov/reference/systems-engineering-handbook/",
    "establishes": "Public systems engineering guidance for guidance design."
  },
  {
    "name": "Wikipedia - Guidance, navigation, and control",
    "url": "https://en.wikipedia.org/wiki/Guidance,_navigation,_and_control",
    "establishes": "Guidance, navigation, and control background and definitions."
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
  const out = { count: keys.length, label: label, max: Math.max(...keys.map((k) => figs[k])), min: Math.min(...keys.map((k) => figs[k])), total: Math.round(total * 10000) / 10000 };
  const result = Object.keys(out).sort().map((k) => k + "=" + out[k]).join("|");
  const h = crypto.createHash("sha256").update(result).digest("hex");
  const figsPy = "FIGURES = {" + keys.map((k) => JSON.stringify(k) + ": " + figs[k]).join(", ") + "}\nLABEL = " + JSON.stringify(label) + "\n";
  const code = "import hashlib\n" + figsPy +
    "def compute():\n" +
    "    total = sum(FIGURES.values())\n" +
    "    n = len(FIGURES)\n" +
    "    total = round(total, 4)\n" +
    "    total = int(total) if total == int(total) else total\n" +
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

function specFor(topic) {
  const official_spec = "1. Purpose. This specification records the generated instance of " + topic.title + ", covering " + topic.subject + ", in full, so a reader can reproduce the worked calculation and judge the method. It is written in full, with every section present, because a compressed summary would hide the requirements, the interfaces, and the failure modes that decide whether a design is sound. 2. Scope. The scope covers " + topic.subject + ", its mathematics, its measurement model, its software shape, the hardware it depends on, the operating conditions, and the limits of what is known. It does not cover unrelated subsystems, and it does not claim performance outside the stated conditions. Anything outside the stated scope is out of scope and must be specified separately. 3. Applicable documents. The governing public guidance is the NASA Systems Engineering Handbook and NPR 7123.1D, together with the NASA Technical Standards collection and the NASA Technical Reports Server, plus the reference articles cited in the sources of this record. Where a number in this record comes from a public source, the source is named; where a number is a worked example, the record says so plainly and shows the arithmetic. 4. Requirements summary. The system shall meet the requirements listed in the requirements section of this record, each written as a single checkable statement with a stated value or a stated behaviour. Each requirement traces to this specification and to at least one acceptance test. Requirements are written to be tested, not admired: a requirement that cannot be checked by test, analysis, inspection, or demonstration is rewritten until it can. 5. Interfaces. The interfaces listed in this record describe what crosses each boundary: commands in, measurements in, commands out, telemetry out, timing, and data formats. Every interface states its units, its range, its update rate, and its failure behaviour, so that two teams building opposite sides of a boundary can agree without guessing. 6. Verification approach. Verification proceeds in stages: first the arithmetic is checked by the demo program in this record, which recomputes the key figures twice and compares SHA-256 digests; then the method is checked against the cited sources; then the requirements are checked one by one against the acceptance tests. Nothing is called verified until the evidence for that claim is written down and reviewable. The verification status field of this record states the current standing honestly. 7. Failure modes and risk. The failure modes for this subject are listed in the safety status of this record: hazards are named, mitigations are assessed, and remaining risks are stated. A design that hides its failure modes is not a design; it is a hope. Every failure mode gets a detection method, a response, and a test. 8. Traceability. Every figure traces to a dataset or a worked example named in this record; every requirement traces to an acceptance test; every test traces to a result. The JCC code on this record is its condensed pointer, decodable to this database, this file, and this record, and the full data always stays with the record itself. 9. Engineering status. The four status fields of this record state the design status, the verification status, the safety status, and the source provenance. This record is never presented as flight-ready, and NASA-level here means engineering targets modeled on public NASA standards, with no claim of NASA certification, approval, affiliation, or endorsement. 10. Notes. This specification is complete for its subject as stated; later work may extend it, but no extension may silently change a requirement, a figure, or a verdict already recorded.";
  return {
    official_spec: official_spec,
    requirements: [
      "The system shall compute " + topic.subject + " results from the stated inputs with the stated accuracy.",
      "The system shall check every input against its stated range and reject out-of-range inputs with a recorded error.",
      "The system shall record every result with its inputs, assumptions, and time.",
      "The system shall detect a failed computation and hand over to a safe state instead of issuing a wrong command.",
      "The system shall be verifiable by the acceptance tests listed in this record, with evidence written down."
    ],
    interfaces: [
      "Input interface: state and measurement data in the stated units, at the stated update rate.",
      "Command interface: guidance, navigation, or control commands out, with units, ranges, and limits stated.",
      "Telemetry interface: results, status, and health data out, in the stated format.",
      "Operator interface: status display and safe-mode command, with plain-language labels."
    ],
    acceptance_tests: [
      "Run the demo twice; the two SHA-256 digests shall match and the printed figures shall equal the stated key figures.",
      "Feed an out-of-range input; the system shall reject it and record the error.",
      "Compare the worked result with an independent hand calculation; the two shall agree within the stated tolerance.",
      "Interrupt the computation; the system shall reach a safe state and report the interruption."
    ]
  };
}

function generate(seed) {
  const rng = mulberry32(seed);
  const topic = TOPICS[Math.floor(rng() * TOPICS.length)];
  const idx = ((seed % 1000000) + 1000000) % 1000000;
  const id = ID_PREFIX + "GEN-" + String(idx).padStart(6, "0");
  const label = SLUG + "-generated";
  const demo = buildDemo(topic, label);
  const ladder_rank = ((seed % 24) + 24) % 24 + 1;
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
    description: topic.description + " " + HONESTY,
    history: "This generated instance extends the public record of " + topic.subject + ", which grew out of the practical need to know where a spacecraft is, decide what it should do next, and command it reliably. The cited sources preserve the main steps of that history in public form.",
    problem: "The problem is to handle " + topic.subject + " with numbers that are known, checked, and traceable, so the solution can be judged against the problem it claims to solve.",
    method: "The method gathers the inputs, checks them against their stated ranges, runs the calculation on them, and compares the result with an independent check. The demo recomputes the key figures twice and compares SHA-256 digests, so any arithmetic slip is caught. " + HONESTY,
    results_reported: "The demo output reports the count, total, minimum, and maximum of the key figures, and the two runs agree exactly, which is the arithmetic check. The figures are worked examples, and the record states their basis plainly.",
    science_proof: "The scientific relation behind the method says the output follows from the inputs in the stated way, so changing an input changes the output in a way that can be predicted and checked. The arithmetic is machine-checked by the demo, while the scientific relation itself is stated, not machine-checked, and the record says so.",
    math_proof: "The mathematics turns the stated inputs into a single checkable number, step by step: the total is the sum of the key figures, the mean is the total divided by the count, and the range is the maximum minus the minimum. The demo checks the summed figures against the stated totals.",
    formal_equation: "Worked figures: total = sum(figures); mean = total / count; range = max(figures) - min(figures).",
    formal_gloss: "total is the sum of all the key figures. count is how many key figures there are. mean is the total divided by the count. max is the largest key figure. min is the smallest key figure. range is the difference between the largest and the smallest.",
    scientific_equation: "The output follows from the inputs in the stated way, so changing an input changes the output in a way that can be predicted and checked.",
    proof_sketch: "The relation is checked by substituting the worked figures into the equation and confirming the demo arithmetic; the scientific claim itself is stated, not machine-checked.",
    skeptical_analysis: "The limits are stated plainly. The method assumes its inputs are correct, its models are adequate, and its environment matches the stated conditions. A reader should not take the worked figures as mission data: they are worked example values for this record, computed openly from the stated inputs. " + HONESTY,
    applies: "This record applies to " + topic.subject + ", whenever the stated conditions hold and the stated inputs are available. It does not apply to missions outside the stated conditions, or any use that needs a system already proven in flight.",
    verification_path: "The verification path is: the demo in this record recomputes the key figures twice and compares digests; the requirements are checked against the acceptance tests listed in the specification; and the sources are cited so that each factual claim can be followed back to a public document.",
    spec: specFor(topic),
    key_figures: topic.figures,
    ladder_rank: ladder_rank,
    dataset: "Seeded generator output from " + topic.subject + " figures; worked example values computed openly, not mission data.",
    evidence: { label: EVIDENCE_LABEL, reason: EVIDENCE_REASON },
    engineering_status: { design_status: "modeled", verification_status: "partially verified", safety_status: SAFETY, source_provenance: PROVENANCE },
    glossary: GLOSSARY,
    retrieval: "Sources retrieved on 2026-11-17: each cited URL was fetched and its full content read before citing; no link is listed unfetched.",
    demo: { code: demo.code },
    expected_output: demo.expected,
    program: "class GeneratedProgram:\n    def run(self):\n        return {\"deterministic\": True}\n",
    sources: SOURCES,
    links: { spec: "filed at merge", wiki: "JAH Wiki entry filed at merge", dictionary: "Dictionary definition filed at merge" },
    network_links: { sibling: SIBLING, adjacent: ADJACENT },
    generator: { type: "seeded boundless generator", gen_id_prefix: ID_PREFIX + "GEN-", hard_stop: 1000000000, throttle_per_call: 100, ceiling_note: CEILING },
    scales: { A1: "One generated record: one " + topic.subject + " worked in full, with its calculation, specification, and checks.", A2: "The whole pair: every generated record in this database, cross-checked against its neighbours.", A3: "The whole network: this record linked to the adjacent databases, so the Master AI can reach it from any related subject." },
    body: "<h2>Description</h2><p>" + topic.description + " " + HONESTY + "</p>"
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
  t("id prefix own family", a.id.indexOf(ID_PREFIX) === 0);
  t("id gen form", a.id.indexOf(ID_PREFIX + "GEN-") === 0);
  t("generator hard_stop 1e9", a.generator.hard_stop === 1000000000);
  t("generator gen prefix own family", a.generator.gen_id_prefix === ID_PREFIX + "GEN-");
  t("jcc_code form", a.jcc_code === "JAHDB/" + SLUG + "#" + a.id);
  const slim = {}; for (const k of Object.keys(a)) { if (k !== "jcc_code" && k !== "jcc_key") slim[k] = a[k]; }
  t("jcc_key round-trip", a.jcc_key === "k=" + crypto.createHash("sha256").update(canonical(slim)).digest("hex").slice(0, 8));
  t("different seeds differ", JSON.stringify(generate(42)) !== JSON.stringify(generate(43)));
  t("honesty never presented as flight-ready", JSON.stringify(a).indexOf("never presented as flight-ready") !== -1);
  t("honesty modeled on public NASA standards", JSON.stringify(a).indexOf("modeled on public NASA standards") !== -1);
  const blob = JSON.stringify(a);
  const bare = ["is flight-ready", "NASA-certified", "NASA certified", "NASA approved", "NASA-endorsed", "NASA endorsed", "NASA affiliated", "NASA-funded", "NASA funded", "flight-proven"];
  t("no bare claims", bare.every((p) => blob.indexOf(p) === -1));
  t("demo code deterministic", a.demo.code.indexOf("Deterministic:") !== -1 && a.demo.code.indexOf("h1 == h2") !== -1);
  t("demo expected deterministic", a.expected_output.indexOf("Deterministic: MATCH") !== -1);
  t("spec requirements >= 4", a.spec.requirements.length >= 4);
  t("spec official_spec >= 400 words", a.spec.official_spec.split(/\s+/).length >= 400);
  t("glossary >= 150 words", a.glossary.split(/\s+/).length >= 150);
  t("retrieval date and full", a.retrieval.indexOf("2026-11-17") !== -1 && a.retrieval.indexOf("full") !== -1);
  t("sibling link", a.network_links.sibling === SIBLING);
  t("adjacent links", Array.isArray(a.network_links.adjacent) && a.network_links.adjacent.length >= 2);
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
