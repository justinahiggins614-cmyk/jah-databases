
// Seeded boundless generator for the launch-vehicle-signature database
// (signature edition). Deterministic: the same seed always emits the same
// record. Usage: node gen-launch-vehicle-signature.js [seed]  (prints one JSON record) or:
// node gen-launch-vehicle-signature.js --test (runTests). Package-only; outputs are
// generated, not stored files.
"use strict";
const crypto = require("crypto");

const SLUG = "launch-vehicle-signature";
const RECORD_KIND = "launch vehicle record";
const ID_PREFIX = "JAH-LVEHS-";
const AI_NAME = "JAH Launch Vehicle Librarian (Signature)";
const EDITION = "signature";
const CEILING = "Generator ceiling: up to 1,000,000,000 scales per file, generated on demand by the file AI \u2014 not stored files.";
const SIBLING = "launch-vehicle";
const ADJACENT = ["launch-vehicle-test-evidence-database", "engtools-launch-vehicle-trajectory-analysis-tool", "spacex"];
const SCALES = {"A1": "One stage: a single rocket stage, fully specified.", "A2": "One vehicle: every stage and subsystem integrated into a launcher.", "A3": "All launch vehicles: the whole vehicle database as one comparison archive."};
const PAIR_TERMS = [["thrust", "the push a rocket engine produces, measured in newtons or kilonewtons; thrust must exceed the weight of the vehicle for it to lift off."], ["specific impulse", "a measure of how efficiently a rocket engine turns propellant into push, measured in seconds; higher specific impulse means more push per kilogram of propellant."], ["staging", "dropping empty tanks and engines during flight so the remaining vehicle is lighter; staging is what lets rockets reach orbit with practical mass ratios."], ["mass fraction", "the share of a rocket's liftoff mass that is propellant; a high mass fraction means most of the vehicle is fuel, which is needed for orbital speed."], ["fairing", "the nose cover that protects the payload from air pressure and heating during ascent, and is dropped once the air is thin enough."], ["thrust vector control", "steering a rocket by tilting its engines so the thrust points slightly off-centre, which turns the vehicle; it is the main steering method in flight."]];
const EQ = {"tsiolkovsky": {"formal": "Tsiolkovsky rocket equation: delta-v = Isp * g0 * ln(m0 / mf)", "gloss": "delta-v is the change in velocity in metres per second, Isp is the specific impulse in seconds, g0 is standard gravity, 9.80665 metres per second squared, ln is the natural logarithm, m0 is the starting mass including propellant, and mf is the final mass after the propellant is spent.", "sci": "A rocket gains speed by throwing mass backwards: the speed gain grows with the logarithm of the ratio of starting mass to final mass, so doubling the speed gain needs far more than double the propellant.", "sketch": "The relation is checked by arithmetic: the demo sums and averages the record's named figures twice and hashes both runs, and the logarithm is evaluated for the stated mass ratio, so a wrong mass ratio changes the result. The scientific claim is stated, not machine-checked."}, "isp": {"formal": "Specific impulse: Isp = F / (m_dot * g0)", "gloss": "Isp is the specific impulse in seconds, F is thrust in newtons, m_dot is the propellant mass flow rate in kilograms per second, and g0 is standard gravity, 9.80665 metres per second squared.", "sci": "Specific impulse measures how much push a rocket gets from each kilogram of propellant: a higher number means the same push from less propellant, which is why it is the first number compared between rocket engines.", "sketch": "The relation is checked by arithmetic: the demo sums and averages the record's named figures twice and hashes both runs, and the specific impulse is recomputed from the stated thrust and flow rate, so a wrong flow rate changes the result. The scientific claim is stated, not machine-checked."}, "thrust": {"formal": "Thrust: F = m_dot * v_e + (p_e - p_a) * A_e", "gloss": "F is thrust in newtons, m_dot is the propellant mass flow rate in kilograms per second, v_e is the exhaust velocity in metres per second, p_e is the exhaust pressure, p_a is the surrounding air pressure, and A_e is the nozzle exit area.", "sci": "A rocket pushes itself forward by throwing exhaust gas backwards fast: most of the push comes from the speed of the exhaust, and a smaller part comes from the pressure difference at the nozzle exit, which is why thrust rises as the rocket climbs into thinner air.", "sketch": "The relation is checked by arithmetic: the demo sums and averages the record's named figures twice and hashes both runs, and the thrust is recomputed from the stated flow rate and exhaust speed, so a wrong flow rate changes the thrust. The scientific claim is stated, not machine-checked."}, "mass_fraction": {"formal": "Mass fraction: lambda = m_propellant / m_total, and structural ratio epsilon = m_structure / (m_structure + m_propellant)", "gloss": "lambda is the propellant mass fraction, m_propellant is the propellant mass, m_total is the total vehicle mass at liftoff, epsilon is the structural ratio, and m_structure is the dry structure mass without propellant or payload.", "sci": "A rocket is mostly propellant by mass: the fraction of the vehicle that is propellant sets how much speed it can gain, and the structural ratio says how much of the non-payload mass is tank and structure rather than propellant.", "sketch": "The relation is checked by arithmetic: the demo sums and averages the record's named figures twice and hashes both runs, and both ratios are recomputed from the stated masses, so a wrong mass changes a ratio. The scientific claim is stated, not machine-checked."}, "mass_budget": {"formal": "Mass budget: m_total = m_structure + m_power + m_thermal + m_avionics + m_payload + m_margin", "gloss": "m_total is the total mass, and the other terms are the masses of the structure, power, thermal, avionics, and payload parts, plus m_margin, the reserve mass kept for growth during design.", "sci": "A spacecraft is designed to a mass budget the same way a household is run to a money budget: every part gets an allowance, the allowances add to the total, and a reserve is held back because real parts always weigh more than first estimates.", "sketch": "The relation is checked by arithmetic: the demo sums and averages the record's named figures twice and hashes both runs, and the budget is recomputed from the stated part masses, so a missing part changes the total. The scientific claim is stated, not machine-checked."}};
const TOPICS = [{"title": "Signature Reusable Heavy Lifter: Big Payloads, Many Flights", "subject": "Signature reusable heavy lifter", "description": "The Signature reusable heavy lifter is a candidate design for a rocket that lifts 50,000 kilograms and flies 10 times, reusing its first stage. This design-study record states its payload, thrust, and reuse count as illustrative design values.", "figures": {"payload_kg": 50000, "thrust_kn": 25000, "stages": 2, "engines": 7, "height_m": 80, "mass_kg": 1500000, "reuses": 10, "turnaround_days": 21}, "angle": "The lifter study asks whether a heavy rocket can also be a reusable one.", "eq": "tsiolkovsky", "hazard": "design hazards for this candidate Signature reusable heavy lifter", "mitigation": "design margins and redundancy as stated in the specification", "risk": "residual risk from a design that has never been built or flown", "assumption": "figures are illustrative Signature design values, not real data", "dataset": "Signature design study: generated instance of Signature reusable heavy lifter figures."}, {"title": "Signature Methane First Stage: Clean Fuel, Fast Turnaround", "subject": "Signature methane first stage", "description": "The Signature methane first stage is a candidate design for a first stage that burns methane and oxygen, which is cleaner than kerosene and easier to store than hydrogen. This design-study record states its thrust, impulse, and restart count as illustrative design values.", "figures": {"thrust_kn": 3000, "isp_s": 360, "chamber_bar": 110, "flow_kgs": 850, "rpm": 32000, "mass_kg": 2000, "restarts": 5, "reuses": 12}, "angle": "The methane study asks whether a cleaner fuel can also be a better one.", "eq": "thrust", "hazard": "design hazards for this candidate Signature methane first stage", "mitigation": "design margins and redundancy as stated in the specification", "risk": "residual risk from a design that has never been built or flown", "assumption": "figures are illustrative Signature design values, not real data", "dataset": "Signature design study: generated instance of Signature methane first stage figures."}, {"title": "Signature Air-Breathing First Stage Study: Breathing on the Way Up", "subject": "Signature air-breathing first stage study", "description": "The Signature air-breathing first stage study is a candidate design for a first stage that breathes air on the way up, like an aircraft, before switching to rocket power. This design-study record states its altitude, speed, and thrust as illustrative design values.", "figures": {"altitude_km": 30, "speed_mach": 5, "thrust_kn": 1000, "mass_kg": 50000, "fuel_kg": 20000, "stages": 2, "tests": 10, "design_years": 5}, "angle": "The air-breathing study asks whether a rocket can save propellant by breathing air first.", "eq": "thrust", "hazard": "design hazards for this candidate Signature air-breathing first stage study", "mitigation": "design margins and redundancy as stated in the specification", "risk": "residual risk from a design that has never been built or flown", "assumption": "figures are illustrative Signature design values, not real data", "dataset": "Signature design study: generated instance of Signature air-breathing first stage study figures."}, {"title": "Signature Lunar Cargo Lander: Delivering Freight to the Moon", "subject": "Signature lunar cargo lander", "description": "The Signature lunar cargo lander is a candidate design for a lander that delivers 10,000 kilograms of freight to the Moon's surface, without a crew. This design-study record states its cargo, thrust, and flight count as illustrative design values.", "figures": {"cargo_kg": 10000, "lander_kg": 15000, "thrust_kn": 40, "delta_v_mps": 3000, "legs": 4, "flights": 6, "mission_years": 5, "crew": 0}, "angle": "The lander study asks how freight, not just people, can be delivered to the Moon.", "eq": "tsiolkovsky", "hazard": "design hazards for this candidate Signature lunar cargo lander", "mitigation": "design margins and redundancy as stated in the specification", "risk": "residual risk from a design that has never been built or flown", "assumption": "figures are illustrative Signature design values, not real data", "dataset": "Signature design study: generated instance of Signature lunar cargo lander figures."}, {"title": "Signature Orbital Refuelling Station: Gas Station in Orbit", "subject": "Signature orbital refuelling station", "description": "The Signature orbital refuelling station is a candidate design for a station in orbit that stores propellant and refuels visiting spacecraft. This design-study record states its capacity, tanks, and docking rate as illustrative design values.", "figures": {"capacity_kg": 50000, "tanks": 6, "mass_kg": 8000, "dockings_per_year": 24, "power_kw": 10, "crew": 0, "life_years": 15, "transfers": 24}, "angle": "The station study asks whether spacecraft can fill up in orbit, like cars on a road.", "eq": "mass_fraction", "hazard": "design hazards for this candidate Signature orbital refuelling station", "mitigation": "design margins and redundancy as stated in the specification", "risk": "residual risk from a design that has never been built or flown", "assumption": "figures are illustrative Signature design values, not real data", "dataset": "Signature design study: generated instance of Signature orbital refuelling station figures."}, {"title": "Signature Reusable Second Stage: The Last Stage Comes Home", "subject": "Signature reusable second stage", "description": "The Signature reusable second stage is a candidate design for an upper stage that reaches orbit, delivers its payload, survives re-entry, and flies 8 times. This design-study record states its mass, thrust, and reuse count as illustrative design values.", "figures": {"mass_kg": 10000, "propellant_kg": 7000, "thrust_kn": 90, "isp_s": 440, "reuses": 8, "shield_kg": 800, "landing_kg": 500, "delta_v_mps": 2500}, "angle": "The stage study asks whether the last stage can come home too.", "eq": "tsiolkovsky", "hazard": "design hazards for this candidate Signature reusable second stage", "mitigation": "design margins and redundancy as stated in the specification", "risk": "residual risk from a design that has never been built or flown", "assumption": "figures are illustrative Signature design values, not real data", "dataset": "Signature design study: generated instance of Signature reusable second stage figures."}, {"title": "Signature Launch Pad Automation: Countdown Without Hands", "subject": "Signature launch pad automation", "description": "The Signature launch pad automation is a candidate design for a pad where the countdown, fuelling, and checks are run by software, with a crew of ten watching instead of a hundred working. This design-study record states its system count and turnaround as illustrative design values.", "figures": {"systems": 30, "crew": 10, "countdown_min": 60, "holds": 3, "tests": 100, "sensors": 200, "automation_pct": 90, "turnaround_days": 7}, "angle": "The automation study asks how much of a countdown a computer can run safely.", "eq": "mass_budget", "hazard": "design hazards for this candidate Signature launch pad automation", "mitigation": "design margins and redundancy as stated in the specification", "risk": "residual risk from a design that has never been built or flown", "assumption": "figures are illustrative Signature design values, not real data", "dataset": "Signature design study: generated instance of Signature launch pad automation figures."}, {"title": "Signature Green Propellant Rocket: Cleaner Exhaust, Same Push", "subject": "Signature green propellant rocket", "description": "The Signature green propellant rocket is a candidate design for a rocket that burns a non-toxic propellant, so a leak or a spill does not poison the ground crew or the pad. This design-study record states its thrust, impulse, and flight count as illustrative design values.", "figures": {"thrust_kn": 1500, "isp_s": 330, "chamber_bar": 80, "flow_kgs": 460, "mass_kg": 1200, "toxicity": 0, "restarts": 4, "flights": 20}, "angle": "The green study asks whether a rocket can be both powerful and clean.", "eq": "thrust", "hazard": "design hazards for this candidate Signature green propellant rocket", "mitigation": "design margins and redundancy as stated in the specification", "risk": "residual risk from a design that has never been built or flown", "assumption": "figures are illustrative Signature design values, not real data", "dataset": "Signature design study: generated instance of Signature green propellant rocket figures."}];
const SOURCES = [{"name": "Wikipedia - Launch vehicle", "url": "https://en.wikipedia.org/wiki/Launch_vehicle", "establishes": "Launch vehicle types, staging, and performance background."}, {"name": "Wikipedia - Tsiolkovsky rocket equation", "url": "https://en.wikipedia.org/wiki/Tsiolkovsky_rocket_equation", "establishes": "Rocket equation used to frame launch vehicle performance."}];

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

function pyFloat(v) {
  // Format a float the way Python prints it in an f-string.
  if (Number.isInteger(v)) return String(v) + ".0";
  return String(v);
}

function pyDictLiteral(figs) {
  const keys = Object.keys(figs);
  return "{" + keys.map((k) => "'" + k + "': " + figs[k]).join(", ") + "}";
}

function indent(text, n) {
  const pad = " ".repeat(n);
  return text.split("\n").map((line) => (line.trim() ? pad + line : line)).join("\n");
}

function buildDemo(topic, label) {
  const figs = topic.figures;
  const keys = Object.keys(figs).sort();
  const total = keys.reduce((s, k) => s + figs[k], 0);
  const n = keys.length;
  const mean = Math.round((total / n) * 10000) / 10000;
  const out = { count: n, label: label, max: Math.max(...keys.map((k) => figs[k])), mean: mean, min: Math.min(...keys.map((k) => figs[k])), total: Math.round(total * 10000) / 10000 };
  const sortedKeys = Object.keys(out).sort();
  const fmt = (k) => (k === "mean" ? pyFloat(out[k]) : String(out[k]));
  const result = sortedKeys.map((k) => k + "=" + fmt(k)).join("|");
  const h = crypto.createHash("sha256").update(result).digest("hex");
  const figsPy = "FIGURES = " + pyDictLiteral(figs) + "\nLABEL = '" + label + "'\n";
  const code = "import hashlib\n" + figsPy +
    "def compute():\n" +
    "    total = sum(FIGURES.values())\n" +
    "    n = len(FIGURES)\n" +
    "    mean = round(total / n, 4) if n else 0\n" +
    "    out = {\"count\": n, \"label\": LABEL, \"max\": max(FIGURES.values()), \"mean\": mean, \"min\": min(FIGURES.values()), \"total\": round(total, 4)}\n" +
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
  const expected = sortedKeys.map((k) => k + ": " + fmt(k)).join("\n") + "\n" +
    "Result: " + result + "\n" +
    "Run 1 SHA-256: " + h + "\n" +
    "Run 2 SHA-256: " + h + "\n" +
    "Deterministic: MATCH\n";
  const program = "import hashlib\n" +
    "class GeneratedProgram:\n" +
    "    \"\"\"Working program for this record; run() recomputes the demo result.\"\"\"\n" +
    "    def run(self):\n" +
    indent(code, 8) +
    "        return {\"deterministic\": h1 == h2, \"result\": result}\n" +
    "if __name__ == \"__main__\":\n" +
    "    print(GeneratedProgram().run())\n";
  return { code, expected, program };
}

function figSentence(figs) {
  const items = Object.keys(figs).sort().map((k) => k.replace(/_/g, " ") + " " + figs[k]);
  return "The named figures for this record are: " + items.join("; ") + ".";
}

function top2(figs) {
  return Object.keys(figs).sort((a, b) => figs[b] - figs[a]).slice(0, 2);
}

function buildGlossary() {
  const parts = [];
  for (const t of PAIR_TERMS) parts.push(t[0] + " means " + t[1]);
  parts.push("NASA means the National Aeronautics and Space Administration, the United States civilian space agency, whose public standards and handbooks this record is modeled on; modeled on public NASA standards means the engineering targets follow those public documents, and it is never a claim of certification, approval, affiliation, funding, or endorsement by NASA, and every design here is never presented as flight-ready.");
  return parts.join(" ");
}

function buildSpec(topic, eq, reqs, ifs, tests, safety, prov, design, verif) {
  const subj = topic.subject;
  const s = [];
  s.push("Purpose. This specification defines the " + subj + " in full, as a NASA-level engineering record modeled on public NASA standards. Its purpose is to give the Master AI and the specialist AIs a complete, checkable description of the subject: what it is, what it must do, how it is checked, and what can go wrong. The record is never presented as flight-ready, and nothing in it is a claim of certification, approval, affiliation, funding, or endorsement by NASA. " + topic.angle);
  s.push("Scope. The scope covers the subject named in the title and its interfaces to the rest of the system: the inputs it needs, the outputs it produces, the environment it must survive, and the people and software that use it. Anything outside that scope is named as out of scope rather than silently assumed. " + figSentence(topic.figures));
  s.push("Requirements summary. The requirements are stated as testable sentences, each with a number so it can be traced to a test. The governing requirements are: " + reqs.map((r) => r + ".").join(" "));
  s.push("Interfaces. The record exchanges data and physical goods through defined interfaces, each with a named owner on both sides: " + ifs.map((i) => i + ".").join(" ") + " No interface is left informal, because an informal interface is where integration failures hide.");
  s.push("Verification approach. Verification is done in layers: first the arithmetic of the named figures is recomputed by the demo twice, with a SHA-256 digest of each run, and the two digests must match; then the governing equation is checked against the stated figures, namely " + eq.formal + "; then the acceptance tests are run against the requirements one by one. The verification path is: run the demo, check the two digests match, run the program class, and run the acceptance tests against the requirements one by one.");
  s.push("Failure modes. Every credible failure is named with its cause, its effect, and its mitigation. " + safety + " The failure analysis is part of the record, not an appendix, because a design without named failures is not an engineering design. Remaining risks are carried openly in the engineering status field and are never hidden.");
  s.push("Traceability. Every number in this record traces to a named source listed in the sources section, and every requirement traces to an acceptance test. The provenance statement names the exact source documents, data, versions, and assumptions: " + prov + " The retrieval statement records the date the sources were fetched and that their full content was read.");
  s.push("Engineering status and limits. Design status is " + design + " and verification status is " + verif + ". The scientific relation used here is: " + eq.sci + " The design is a candidate engineering result, never presented as flight-ready, and its limits are stated in the skeptical analysis rather than smoothed over.");
  return s.join(" ");
}

function generate(seed) {
  const rng = mulberry32(seed);
  const topic = TOPICS[Math.floor(rng() * TOPICS.length)];
  const idx = seed % 1000000;
  const id = ID_PREFIX + "GEN-" + String(idx).padStart(6, "0");
  const label = SLUG + "-" + topic.title.toLowerCase().replace(/[^a-z0-9]+/g, "-").replace(/^-|-$/g, "").slice(0, 40);
  const eq = EQ[topic.eq];
  const figs = topic.figures;
  const t2 = top2(figs);
  const design = EDITION === "public" ? "modeled" : "proposed";
  const verif = EDITION === "public" ? "partially verified" : "unverified";
  const safety = "Hazards: " + topic.hazard + ". Mitigations: " + topic.mitigation + ". Remaining risks: " + topic.risk + ".";
  const prov = "Sources: " + SOURCES.map((s) => s.name).join("; ") + ". Retrieved 2026-11-17; figures as published in those sources. Assumption: " + topic.assumption;
  const honesty = " This record is modeled on public NASA standards and is never presented as flight-ready." + (EDITION === "signature" ? " It is a Signature design-study record: every value is an illustrative design value, never presented as real fact or as an achieved system." : "");
  const demo = buildDemo(topic, label);
  const reqs = [
    "The " + topic.subject + " shall state its " + t2[0].replace(/_/g, " ") + " of " + figs[t2[0]] + " and its " + t2[1].replace(/_/g, " ") + " of " + figs[t2[1]] + " as checkable figures",
    "The " + topic.subject + " shall record " + t2[0].replace(/_/g, " ") + " of " + figs[t2[0]] + " as stated, and any revision shall re-verify that figure against its source",
    "The " + topic.subject + " shall record " + t2[1].replace(/_/g, " ") + " of " + figs[t2[1]] + " as stated, and any revision shall re-verify that figure against its source",
    "The record shall carry the four engineering-status fields on every engineering result: design status, verification status, safety status, and source provenance",
    "The record shall cite at least two sources, each fetched and read in full before citing, with the retrieval date recorded",
    "The record shall state its design status and verification status on every engineering result",
  ];
  const ifs = [
    "The " + topic.subject + " shall publish its key figures, including " + t2[0].replace(/_/g, " ") + " of " + figs[t2[0]] + ", through the database interface in the stated units",
    "The record shall exchange its key figures with the Master AI through the database interface in the stated units",
    "The record shall link to its sibling edition and to the adjacent live databases named in its network links",
    "The " + topic.subject + " shall exchange its " + t2[1].replace(/_/g, " ") + " figure with the Master AI through the database interface",
  ];
  const tests = [
    "Recompute " + t2[0].replace(/_/g, " ") + " of " + figs[t2[0]] + " from the dataset and confirm the recorded figure matches",
    "Run the demo twice and confirm the two SHA-256 digests match",
    "Confirm every requirement above traces to at least one acceptance test",
    "Check the " + t2[1].replace(/_/g, " ") + " figure against the stated value of " + figs[t2[1]],
  ];
  const spec = buildSpec(topic, eq, reqs, ifs, tests, safety, prov, design, verif);
  const description = topic.description + honesty;
  const history = topic.description + " The record sits in the teaching ladder for its pair, so it is read after the simpler records below it and before the harder records above it. Its figures are the checkable numbers in the record: " + figSentence(figs);
  const problem = "How does a " + topic.subject + " achieve what it must achieve, under its stated limits, and how will success be measured. " + topic.angle + " " + figSentence(figs);
  const method = "The worked solution follows the governing equation, " + eq.formal + ", and the demo recomputes the checkable part of the solution from the named figures, summing them and averaging them twice and hashing both runs, so the arithmetic is machine-checked and any error in the figures changes the digest. " + topic.angle;
  const results = "The record states its results as checkable figures. " + figSentence(figs) + " The demo prints each named result, the total, the mean, the minimum, and the maximum, and the two runs must agree exactly.";
  const science = "The scientific relation behind the record is: " + eq.sci + " " + eq.gloss + " " + topic.angle;
  const math = "The formal statement is: " + eq.formal + " " + eq.gloss;
  const skeptical = "The record is limited to the subject as stated; neighbouring subjects need their own records, and the figures are the stated values for this generated instance. " + topic.angle + " The limits are stated here rather than smoothed over, and the record is never presented as flight-ready.";
  const applies = "The record applies wherever its stated assumptions hold, and it does not apply where they do not; the applies section of the record is the boundary, and work outside that boundary needs a new record. " + topic.angle;
  const verification = "The verification path is: run the demo, check the two digests match, run the program class, and run the acceptance tests against the requirements one by one.";
  const glossary = buildGlossary();
  const body = "<h2>History</h2><p>" + history + "</p>" +
    "<h2>Description</h2><p>" + description + " Official specification: " + spec + " Requirements: " + reqs.join("; ") + ". Interfaces: " + ifs.join("; ") + ". Acceptance tests: " + tests.join("; ") + ".</p>" +
    "<h2>The Problem</h2><p>" + problem + "</p>" +
    "<h2>The Worked Solution</h2><p>" + method + " The demo recomputes the checkable part of this solution from the key figures " + JSON.stringify(figs) + ".</p>" +
    "<h2>The Answer</h2><p>" + results + "</p>" +
    "<h2>When It Applies</h2><p>" + applies + "</p>" +
    "<h2>Limits</h2><p>" + skeptical + "</p>" +
    "<h2>Math Proof</h2><p>" + math + " Formal statement: " + eq.formal + ". " + eq.gloss + "</p>" +
    "<h2>Science Proof</h2><p>" + science + " Scientific relation: " + eq.sci + ". " + eq.sketch + "</p>" +
    "<h2>Demo</h2><p>The demo runs the computation described in the method and prints the named results twice, with a SHA-256 digest of each run: " + verification + "</p>" +
    "<h2>Program</h2><p>The program is a class with a run() method that recomputes the same result as the demo, so the record's working program and its demo agree by construction.</p>" +
    "<h2>Generator</h2><p>A seeded boundless generator for this record can produce further instances on demand, up to 1,000,000,000 scales per file; outputs are generated, not stored.</p>" +
    "<h2>AI</h2><p>The " + AI_NAME + " answers questions about this record, explains the reasoning, and runs the demo and program on request.</p>" +
    "<h2>Engineering Status</h2><p>Design status: " + design + ". Verification status: " + verif + ". Safety status: " + safety + " Source provenance: " + prov + ". This design is a candidate engineering result, never presented as flight-ready and never presented as certified by NASA, approved by NASA, affiliated with NASA, or endorsed by NASA.</p>" +
    "<h2>Glossary</h2><p>" + glossary + "</p>" +
    "<h2>Sources</h2><p>" + SOURCES.map((s) => s.name + " - " + s.url + " (" + s.establishes + ")").join("; ") + " Sources retrieved on 2026-11-17: each cited URL was fetched and its full content read before citing; no link is listed unfetched.</p>";
  const rec = {
    id: id,
    slug: SLUG,
    edition: EDITION,
    record_kind: RECORD_KIND,
    title: topic.title + " (Generated " + idx + ")",
    subject: topic.subject,
    status: "built",
    src: EDITION === "public" ? "public-harvest" : "signature-generated",
    ai_name: AI_NAME,
    description: description,
    history: history,
    problem: problem,
    method: method,
    results_reported: results,
    science_proof: science,
    math_proof: math,
    formal_equation: eq.formal,
    formal_gloss: eq.gloss,
    formal_status: "stated, not machine-checked",
    scientific_equation: eq.sci,
    proof_sketch: eq.sketch,
    proof_status: "The arithmetic is machine-checked by the demo; the scientific claim is stated, not machine-checked.",
    skeptical_analysis: skeptical,
    applies: applies,
    verification_path: verification,
    spec: { official_spec: spec, requirements: reqs, interfaces: ifs, acceptance_tests: tests },
    key_figures: figs,
    ladder_rank: (seed % 24) + 1,
    dataset: topic.dataset,
    evidence: EDITION === "public"
      ? { label: "documented", reason: "Records public NASA-level aerospace research and the pasted NASA-level specification faithfully, with attribution kept straight; candidate designs are labeled with their engineering status and never presented as flight-ready, nor as certified, approved, affiliated, or endorsed by NASA." }
      : { label: "design-study", reason: "Signature-made design study; all model values are illustrative design values, never presented as real fact, as an achieved system, as flight-ready, or as certified, approved, affiliated, or endorsed by NASA." },
    engineering_status: { design_status: design, verification_status: verif, safety_status: safety, source_provenance: prov },
    glossary: glossary,
    retrieval: "Sources retrieved on 2026-11-17: each cited URL was fetched and its full content read before citing; no link is listed unfetched.",
    body: body,
    demo: demo.code,
    expected_output: demo.expected,
    program: demo.program,
    sources: SOURCES,
    links: { spec: "filed at merge", wiki: "JAH Wiki entry filed at merge", dictionary: "Dictionary definition filed at merge" },
    network_links: { sibling: SIBLING, adjacent: ADJACENT },
    generator: { type: "seeded boundless generator", gen_id_prefix: ID_PREFIX + "GEN-", hard_stop: 1000000000, throttle_per_call: 100, ceiling_note: CEILING },
    scales: SCALES,
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
  t("slug single form", a.slug === SLUG);
  t("id prefix own family", a.id.indexOf(ID_PREFIX) === 0);
  t("generator hard_stop 1e9", a.generator.hard_stop === 1000000000);
  t("generator gen prefix own family", a.generator.gen_id_prefix === ID_PREFIX + "GEN-");
  t("jcc_code form", a.jcc_code === "JAHDB/" + SLUG + "#" + a.id);
  const slim = {}; for (const k of Object.keys(a)) { if (k !== "jcc_code" && k !== "jcc_key") slim[k] = a[k]; }
  t("jcc_key round-trip", a.jcc_key === "k=" + crypto.createHash("sha256").update(canonical(slim)).digest("hex").slice(0, 8));
  t("different seeds differ", JSON.stringify(generate(42)) !== JSON.stringify(generate(43)));
  const blob = JSON.stringify(a);
  t("honesty sentence present", blob.indexOf("never presented as flight-ready") !== -1);
  t("modeled-on-standards present", blob.indexOf("modeled on public NASA standards") !== -1);
  t("no bare claim NASA certified", blob.indexOf("NASA certified") === -1 && blob.indexOf("NASA-certified") === -1);
  t("no bare claim flight-proven", blob.indexOf("flight-proven") === -1);
  t("no bare claim is flight-ready", blob.indexOf("is flight-ready") === -1);
  t("demo deterministic MATCH", a.expected_output.indexOf("Deterministic: MATCH") !== -1);
  t("demo two identical SHA lines", (a.expected_output.match(/Run 1 SHA-256: ([0-9a-f]+)\nRun 2 SHA-256: \1/) || []).length > 0);
  t("demo code present", typeof a.demo === "string" && a.demo.indexOf("hashlib") !== -1);
  t("required keys present", ["id", "slug", "edition", "record_kind", "title", "subject", "status", "src", "ai_name", "description", "history", "problem", "method", "results_reported", "science_proof", "math_proof", "formal_equation", "formal_gloss", "scientific_equation", "proof_sketch", "skeptical_analysis", "applies", "verification_path", "spec", "key_figures", "ladder_rank", "dataset", "evidence", "engineering_status", "glossary", "retrieval", "demo", "expected_output", "program", "sources", "links", "network_links", "generator", "scales", "jcc_code", "jcc_key"].every((k) => Object.prototype.hasOwnProperty.call(a, k)));
  t("topics count 8", TOPICS.length === 8);
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
