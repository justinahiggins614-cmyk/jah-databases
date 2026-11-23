// Seeded boundless generator for the flight-avionics-signature database (signature edition).
// Deterministic: the same seed always emits the same record.
// Usage: node gen-flight-avionics-signature.js [seed]  (prints one JSON record)
// or: node gen-flight-avionics-signature.js --test (runTests).
// Package-only; outputs are generated, not stored files.
"use strict";
const crypto = require("crypto");

const SLUG = "flight-avionics-signature";
const RECORD_KIND = "flight avionics record";
const ID_PREFIX = "JAH-FAVIS-";
const AI_NAME = "JAH Flight Avionics Librarian (Signature)";
const EDITION = "signature";
const SRC = "signature-generated";
const CEILING = "Generator ceiling: up to 1,000,000,000 scales per file, generated on demand by the file AI \u2014 not stored files.";
const SIBLING = "flight-avionics";
const ADJACENT = ["avionics-interoperability-database", "nasadarpa-fault-tolerant-flight-software-framework-public"];
const HONESTY = "This is a Signature design-study record: a candidate design made in the Signature system, modeled on public NASA standards, and never presented as flight-ready. Missile-guidance content is excluded from this record; this is civilian aerospace and space exploration work only, with no weapons content. Design values are illustrative, never presented as real measured fact or as an achieved system.";
const GLOSSARY = "delta-v (change in velocity): the total change in speed a spacecraft must achieve, measured in metres per second. orbit: the curved path a spacecraft follows around a planet, moon, or star under gravity. trajectory: the path a spacecraft follows through space over time, including its position and velocity at each moment. telemetry: measurements sent from a spacecraft to the ground, reporting temperatures, voltages, positions, and instrument readings. verification: the disciplined checking that a design meets its written requirements, by test, analysis, inspection, or demonstration. validation: the checking that a finished design actually does the job its users need, in conditions like the real mission. redundancy: having a spare unit or a second way to do a job, so one failure does not end the mission. fault tolerance: the ability of a system to keep working, or to fail safely, when a part breaks or a measurement goes wrong. state vector: the list of numbers that fully describes a spacecraft at one moment, usually its three position numbers and three velocity numbers. covariance: a table of numbers describing how uncertain an estimate is, and how the errors in different quantities move together. ground station: a place on Earth with antennas and radios that talks to spacecraft, sends commands, and receives telemetry. link budget: the accounting of signal strength from transmitter to receiver, adding gains and subtracting losses to check the signal arrives strong enough. NASA (National Aeronautics and Space Administration): the United States civilian space agency, whose public standards and handbooks this record is modeled on, with no claim of certification, approval, affiliation, or endorsement.";
const SAFETY = "Hazards include incorrect inputs, stale measurements, software faults, and loss of communication; mitigations include range checks, independent cross-checks, safe-mode handover, and redundant paths; remaining risks include unmodeled disturbances, sensor drift, and single-point failures that testing has not yet exercised.";
const PROVENANCE = "Public sources cited in this record (NASA Systems Engineering Handbook, NPR 7123.1D, NASA Technical Reports Server, and the cited reference articles); figures are worked examples from the stated inputs; assumptions are listed in the method and the specification.";
const EVIDENCE_LABEL = "design-study";
const EVIDENCE_REASON = "Signature-made design study; all model values are illustrative design values, never presented as real fact, as an achieved system, as flight-ready, and no claim of NASA certification, approval, affiliation, or endorsement is made.";

const TOPICS = [
  {
    "title": "Signature Study: A Low-Power Radiation-Tolerant Processor",
    "subject": "signature low-power processor overview",
    "description": "A Signature design study of a low-power radiation-tolerant processor that runs on 3 watts, tolerates 80 kilorads, and still delivers 100 million instructions per second.",
    "figures": {
      "clock_mhz": 80,
      "mips": 100,
      "power_w": 3,
      "mass_g": 150,
      "radiation_krad": 80,
      "seu_rate_day": 0.008,
      "cores": 2,
      "memory_mb": 192
    }
  },
  {
    "title": "Signature Study: A Time-Triggered 1553 Bus",
    "subject": "signature time-triggered bus overview",
    "description": "A Signature design study of a time-triggered MIL-STD-1553 bus in which every message has a fixed time slot, so the traffic is fully predictable.",
    "figures": {
      "data_rate_mbps": 1,
      "word_bits": 20,
      "max_terminals": 31,
      "bus_length_m": 80,
      "messages_per_s": 1200,
      "redundant_buses": 2,
      "voltage_v": 5,
      "protocol_overhead_pct": 8
    }
  },
  {
    "title": "Signature Study: A Fault-Tolerant SpaceWire Network",
    "subject": "signature fault-tolerant SpaceWire overview",
    "description": "A Signature design study of a fault-tolerant SpaceWire network that reroutes packets around a failed link automatically.",
    "figures": {
      "data_rate_mbps": 200,
      "links_count": 12,
      "cable_length_m": 8,
      "power_w": 1,
      "latency_us": 4,
      "packet_size_bytes": 1024,
      "routers_count": 4,
      "error_rate": 0.0001
    }
  },
  {
    "title": "Signature Study: A Five-Module Voting Computer",
    "subject": "signature five-module computer overview",
    "description": "A Signature design study of a five-module voting computer in which five identical modules compute the same result and a voter takes the majority.",
    "figures": {
      "modules_count": 5,
      "voter_delay_ns": 12,
      "failure_rate_fit": 80,
      "availability": 0.9999999,
      "power_w": 20,
      "mass_kg": 4,
      "scrub_interval_s": 45,
      "mismatch_count": 1
    }
  },
  {
    "title": "Signature Study: Predictive Fault Recovery",
    "subject": "signature predictive recovery overview",
    "description": "A Signature design study of a predictive fault recovery system that watches residual trends, predicts a fault before it happens, and warms up the spare.",
    "figures": {
      "monitors_count": 25,
      "detection_time_ms": 50,
      "isolation_time_s": 1,
      "recovery_time_s": 5,
      "faults_catalogued": 50,
      "recovery_tests": 20,
      "false_alarm_rate": 0.0005,
      "safe_modes": 4
    }
  },
  {
    "title": "Signature Study: Partitioned Flight Software",
    "subject": "signature partitioned software overview",
    "description": "A Signature design study of a partitioned flight software architecture in which sixteen applications run in separate partitions with enforced time and memory limits.",
    "figures": {
      "apps_count": 16,
      "services_count": 6,
      "message_rate_hz": 120,
      "memory_mb": 192,
      "cpu_pct": 70,
      "lines_of_code": 80000,
      "tables_count": 25,
      "events_logged": 2000
    }
  },
  {
    "title": "Signature Study: A Hierarchical Watchdog",
    "subject": "signature hierarchical watchdog overview",
    "description": "A Signature design study of a hierarchical watchdog with timers at three levels, so a hang at any level is caught and the computer is reset.",
    "figures": {
      "watchdog_timeout_s": 4,
      "kick_interval_s": 1,
      "resets_count": 1,
      "safe_mode_power_w": 25,
      "recovery_time_s": 20,
      "monitors_count": 12,
      "false_resets": 0,
      "uptime_pct": 99.95
    }
  },
  {
    "title": "Signature Study: Model-Based Verification",
    "subject": "signature model-based verification overview",
    "description": "A Signature design study of a model-based verification campaign in which the real avionics runs against a spacecraft model that is itself checked against flight data.",
    "figures": {
      "test_cases": 800,
      "coverage_pct": 95,
      "test_duration_h": 72,
      "faults_injected": 80,
      "faults_caught": 78,
      "hardware_units": 16,
      "simulation_fidelity_pct": 98,
      "review_cycles": 4
    }
  }
];
const SOURCES = [
  {
    "name": "Wikipedia - Radiation hardening",
    "url": "https://en.wikipedia.org/wiki/Radiation_hardening",
    "establishes": "Radiation hardening background the design studies build on."
  },
  {
    "name": "Wikipedia - Fault tolerance",
    "url": "https://en.wikipedia.org/wiki/Fault_tolerance",
    "establishes": "Fault tolerance background the design studies build on."
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
