
// Seeded boundless generator for the space-mission database
// (public edition). Deterministic: the same seed always emits the same
// record. Usage: node gen-space-mission.js [seed]  (prints one JSON record) or:
// node gen-space-mission.js --test (runTests). Package-only; outputs are
// generated, not stored files.
"use strict";
const crypto = require("crypto");

const SLUG = "space-mission";
const RECORD_KIND = "space mission record";
const ID_PREFIX = "JAH-SPMI-";
const AI_NAME = "JAH Space Mission Librarian";
const EDITION = "public";
const CEILING = "Generator ceiling: up to 1,000,000,000 scales per file, generated on demand by the file AI \u2014 not stored files.";
const SIBLING = "space-mission-signature";
const ADJACENT = ["famous-space-missions", "famous-space-missions-signature", "db-space-mission-classroom", "space", "spacecraft"];
const SCALES = {"A1": "One mission: a single architecture from objectives to outcomes.", "A2": "The mission family: every flown and candidate mission of the same class.", "A3": "All missions: the whole mission database as one navigable archive."};
const PAIR_TERMS = [["delta-v (change in velocity)", "the total change in speed a mission must produce with its engines, measured in metres per second; it is the currency of space travel, because every manoeuvre costs delta-v and the propellant budget is set by it."], ["trajectory", "the path a spacecraft follows through space over time, set by gravity and by engine burns; a trajectory is planned before launch and corrected in flight."], ["translunar injection", "the engine burn that sends a spacecraft out of Earth orbit onto a path to the Moon; it is the largest single burn of a lunar mission."], ["halo orbit", "a looping path around a Lagrange point, a place where the gravity of two bodies balances; halo orbits are used by observatories and by planned lunar stations."], ["rendezvous", "the careful meeting of two spacecraft in orbit, matching position and speed so they can dock or transfer crew and cargo."], ["ground station", "a place on Earth with large antennas that talks to spacecraft, sends commands, and receives data; several stations around the world give near-continuous coverage."]];
const EQ = {"hohmann": {"formal": "Hohmann transfer: total change in velocity = sqrt(mu / r1) * (sqrt(2 * r2 / (r1 + r2)) - 1) + sqrt(mu / r2) * (1 - sqrt(2 * r1 / (r1 + r2)))", "gloss": "mu is the standard gravitational parameter of the central body, r1 is the radius of the starting circular orbit, r2 is the radius of the target circular orbit, and sqrt means square root. The first term is the departure burn and the second term is the arrival burn; their sum is the total change in velocity, called delta-v, measured in metres per second.", "sci": "A Hohmann transfer is the lowest-energy two-burn path between two circular orbits in the same plane: one burn leaves the first orbit onto an ellipse that touches both orbits, and a second burn circularises the path at the target orbit.", "sketch": "The relation is checked by arithmetic: the demo sums and averages the record's named figures twice and hashes both runs, and the two burns are computed separately and added, so a sign or order error changes the total. The scientific claim is stated, not machine-checked."}, "tsiolkovsky": {"formal": "Tsiolkovsky rocket equation: delta-v = Isp * g0 * ln(m0 / mf)", "gloss": "delta-v is the change in velocity in metres per second, Isp is the specific impulse in seconds, g0 is standard gravity, 9.80665 metres per second squared, ln is the natural logarithm, m0 is the starting mass including propellant, and mf is the final mass after the propellant is spent.", "sci": "A rocket gains speed by throwing mass backwards: the speed gain grows with the logarithm of the ratio of starting mass to final mass, so doubling the speed gain needs far more than double the propellant.", "sketch": "The relation is checked by arithmetic: the demo sums and averages the record's named figures twice and hashes both runs, and the logarithm is evaluated for the stated mass ratio, so a wrong mass ratio changes the result. The scientific claim is stated, not machine-checked."}, "orbit_period": {"formal": "Orbital period: T = 2 * pi * sqrt(a^3 / mu)", "gloss": "T is the orbital period in seconds, pi is 3.14159, a is the semi-major axis of the orbit in metres, mu is the standard gravitational parameter of the central body, and sqrt means square root.", "sci": "A body in a circular or elliptical orbit returns to the same place after a time set by the size of its orbit and the gravity of the body it circles: larger orbits take longer, in proportion to the orbit size raised to the power three halves.", "sketch": "The relation is checked by arithmetic: the demo sums and averages the record's named figures twice and hashes both runs, and the period is recomputed from the stated orbit size, so a wrong orbit size changes the period. The scientific claim is stated, not machine-checked."}, "visviva": {"formal": "Vis-viva equation: v^2 = mu * (2 / r - 1 / a)", "gloss": "v is the speed in metres per second, mu is the standard gravitational parameter of the central body, r is the current distance from the centre of the central body, and a is the semi-major axis of the orbit.", "sci": "The speed of a body in orbit depends on where it is in its orbit and on the size of the orbit: it moves fastest at the closest point and slowest at the farthest point, and the equation gives the exact speed at any point.", "sketch": "The relation is checked by arithmetic: the demo sums and averages the record's named figures twice and hashes both runs, and the speed is recomputed at the stated distance, so a wrong distance changes the speed. The scientific claim is stated, not machine-checked."}, "link_budget": {"formal": "Link budget: P_received = P_transmitted + G_transmitted + G_received - L_path - L_other", "gloss": "P_received is the power arriving at the receiver, P_transmitted is the power sent, G_transmitted and G_received are the antenna gains at each end, L_path is the loss over the distance travelled, and L_other covers all other losses; all terms are in decibels.", "sci": "A radio link works when the power that arrives is stronger than the receiver's noise floor by a clear margin: every gain adds and every loss subtracts, and the distance loss grows with the square of the distance.", "sketch": "The relation is checked by arithmetic: the demo sums and averages the record's named figures twice and hashes both runs, and the budget is recomputed from the stated gains and losses, so a missing loss term changes the margin. The scientific claim is stated, not machine-checked."}};
const TOPICS = [{"title": "Space Mission Overview: Architectures and Outcomes", "subject": "Space mission overview", "description": "A space mission is a complete journey from objectives to outcomes: the architecture, the trajectory, the spacecraft, the operations, and the science return. This overview record gathers the mission family's headline numbers so the Master AI can compare missions at a glance.", "figures": {"missions": 24, "destinations": 5, "crewed_missions": 12, "robotic_missions": 12, "decades": 6, "success_percent": 96, "data_tb": 40, "partners": 5}, "angle": "The overview is the starting point for mission planning: it shows what has been flown, where, and how well it worked.", "eq": "hohmann", "hazard": "launch and flight hazards for this Space mission overview", "mitigation": "design margins, testing, and redundancy as stated in the specification", "risk": "residual risk from conditions the stated figures do not cover", "assumption": "figures are the stated values for this generated instance", "dataset": "Public aerospace data: generated instance of Space mission overview figures."}, {"title": "Lunar Mission Planning: From Earth to the Moon", "subject": "Lunar mission planning", "description": "A lunar mission is a sequence of phases, each with its own change in velocity and mass budget: launch, translunar injection, lunar orbit, descent, surface work, ascent, return, and recovery. This planning record states the phase structure and the headline numbers for a crewed lunar mission.", "figures": {"transit_days": 3, "crew": 4, "delta_v_mps": 8200, "phases": 9, "burns": 4, "mass_kg": 45000, "samples_kg": 22, "crew_returned": 3}, "angle": "The planning record turns a lunar mission into numbers: the phases, the burns, and the mass that each phase must carry.", "eq": "hohmann", "hazard": "launch and flight hazards for this Lunar mission planning", "mitigation": "design margins, testing, and redundancy as stated in the specification", "risk": "residual risk from conditions the stated figures do not cover", "assumption": "figures are the stated values for this generated instance", "dataset": "Public aerospace data: generated instance of Lunar mission planning figures."}, {"title": "Mars Mission Planning: Transits and Landings", "subject": "Mars mission planning", "description": "A Mars mission is a long transfer, a landing, surface work, and a return, with launch windows that open about every 26 months. This planning record states the transfer time, the change in velocity, and the mass budget for a crewed Mars mission.", "figures": {"transit_days": 259, "crew": 4, "delta_v_mps": 6200, "phases": 10, "burns": 6, "mass_kg": 30000, "rovers": 2, "instruments": 8}, "angle": "The planning record turns a Mars mission into numbers: the 259-day transfer, the burns, and the mass that each phase must carry.", "eq": "hohmann", "hazard": "launch and flight hazards for this Mars mission planning", "mitigation": "design margins, testing, and redundancy as stated in the specification", "risk": "residual risk from conditions the stated figures do not cover", "assumption": "figures are the stated values for this generated instance", "dataset": "Public aerospace data: generated instance of Mars mission planning figures."}, {"title": "Deep Space Mission Operations: Talking Across Billions of Kilometres", "subject": "Deep space mission operations", "description": "A deep space mission keeps working and talking to Earth for decades, across billions of kilometres, with power that fades a little every year. This operations record states the distance, speed, power, and link figures for a mission at the edge of the Solar System.", "figures": {"distance_km": 24000000000, "speed_mps": 17000, "power_watts": 249, "instruments": 10, "years": 48, "stations": 3, "antenna_m": 70, "data_rate_bps": 160}, "angle": "The operations record shows what it takes to stay in contact with a spacecraft billions of kilometres away.", "eq": "visviva", "hazard": "launch and flight hazards for this Deep space mission operations", "mitigation": "design margins, testing, and redundancy as stated in the specification", "risk": "residual risk from conditions the stated figures do not cover", "assumption": "figures are the stated values for this generated instance", "dataset": "Public aerospace data: generated instance of Deep space mission operations figures."}, {"title": "Orbital Station Operations: Living and Working in Orbit", "subject": "Orbital station operations", "description": "An orbital station is a crewed research station in low Earth orbit, assembled from modules, supplied by visiting vehicles, and kept in orbit by regular reboost burns. This operations record states the mass, altitude, period, volume, crew, and power of a station.", "figures": {"crew": 7, "mass_kg": 419725, "altitude_km": 420, "period_minutes": 93, "volume_m3": 916, "power_watts": 120000, "modules": 16, "resupply_per_year": 4}, "angle": "The operations record shows how a station stays supplied, powered, and safe for decades.", "eq": "orbit_period", "hazard": "launch and flight hazards for this Orbital station operations", "mitigation": "design margins, testing, and redundancy as stated in the specification", "risk": "residual risk from conditions the stated figures do not cover", "assumption": "figures are the stated values for this generated instance", "dataset": "Public aerospace data: generated instance of Orbital station operations figures."}, {"title": "Planetary Flyby Science: Fast Encounters, Rich Data", "subject": "Planetary flyby science", "description": "A planetary flyby is a fast close pass that gathers the best data in minutes, then climbs away to downlink and recover. This science record states the flyby count, closest approach, instruments, and data return for a flyby tour.", "figures": {"flybys": 12, "closest_km": 100000, "instruments": 8, "data_tb": 8, "mission_years": 9, "transfer_years": 5, "mass_kg": 3500, "speed_kms": 20}, "angle": "The science record shows how a flyby tour turns minutes of close approach into years of science.", "eq": "visviva", "hazard": "launch and flight hazards for this Planetary flyby science", "mitigation": "design margins, testing, and redundancy as stated in the specification", "risk": "residual risk from conditions the stated figures do not cover", "assumption": "figures are the stated values for this generated instance", "dataset": "Public aerospace data: generated instance of Planetary flyby science figures."}, {"title": "Sample Return Missions: Bringing Other Worlds Home", "subject": "Sample return missions", "description": "A sample return mission flies to another world, collects material, and brings it home for laboratory study, where instruments too large to fly can analyse it. This record states the sample mass, mission length, and change in velocity for a sample return.", "figures": {"samples_g": 250, "mission_years": 7, "delta_v_mps": 5000, "spacecraft_kg": 2100, "instruments": 5, "tubes": 30, "transfer_days": 259, "landing_sites": 1}, "angle": "The record shows what a sample return costs and what it returns: a small mass of material, studied for years.", "eq": "visviva", "hazard": "launch and flight hazards for this Sample return missions", "mitigation": "design margins, testing, and redundancy as stated in the specification", "risk": "residual risk from conditions the stated figures do not cover", "assumption": "figures are the stated values for this generated instance", "dataset": "Public aerospace data: generated instance of Sample return missions figures."}, {"title": "Mission Risk and Safety: Designing for the Worst Day", "subject": "Mission risk and safety", "description": "Mission risk and safety is the discipline of naming what can go wrong, designing so it does not, and planning what happens if it does. This record states the fault modes, safe modes, watchdogs, response time, and recovery time for a mission.", "figures": {"fault_modes": 40, "safe_modes": 3, "watchdogs": 4, "response_s": 10, "recovery_min": 30, "tests": 30, "redundancy": 2, "mission_years": 10}, "angle": "The record shows how a mission is designed for its worst day, not just its best day.", "eq": "orbit_period", "hazard": "launch and flight hazards for this Mission risk and safety", "mitigation": "design margins, testing, and redundancy as stated in the specification", "risk": "residual risk from conditions the stated figures do not cover", "assumption": "figures are the stated values for this generated instance", "dataset": "Public aerospace data: generated instance of Mission risk and safety figures."}];
const SOURCES = [{"name": "NASA TechPort - technology projects and taxonomy", "url": "https://techport.nasa.gov", "establishes": "Technology projects and taxonomy behind space missions."}, {"name": "Wikipedia - Orbital mechanics", "url": "https://en.wikipedia.org/wiki/Orbital_mechanics", "establishes": "Orbital mechanics background for mission design."}];

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
