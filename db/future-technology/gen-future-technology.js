// gen-future-technology.js -- boundless generator for the Future Technology Database.
// Usage: node gen-future-technology.js --n 5
// Deterministic: a seeded LCG drives topic selection and parameter variation.
// Self-regulating: throttled, duplicate-checked, hard-stops at 10^15 records or when
// the topic space is genuinely exhausted. Generated records carry "generated": true
// and src "generated" -- never mixed with assistant-built records.
"use strict";
const HARD_CAP = 1e15;
const SLUG = "future-technology";
const PREFIX = "JAH-FUT-TECH";

function parseN(argv) {
  const i = argv.indexOf("--n");
  if (i >= 0 && argv[i + 1]) {
    const n = parseInt(argv[i + 1], 10);
    if (!isNaN(n) && n >= 0) return Math.min(n, 100000); // throttle per run
  }
  return 5;
}

let seed = 20261023;
function rnd() {
  seed = (seed * 1103515245 + 12345) & 0x7fffffff;
  return seed / 0x7fffffff;
}

const TOPICS = [
  "solid-state batteries", "sodium-ion batteries", "iron-air storage", "flow batteries",
  "fusion power", "inertial-confinement fusion", "enhanced geothermal", "floating offshore wind",
  "perovskite solar tandems", "direct air capture", "green hydrogen", "small modular reactors",
  "eVTOL air taxis", "autonomous trucking", "hyperloop", "ocean thermal energy conversion",
  "quantum error correction", "photonic chips", "neuromorphic processors", "6G terahertz",
  "LEO mega-constellations", "AI-designed proteins", "bioprinted organs", "senolytics",
  "brain organoids", "digital olfaction", "smart contact lenses", "programmable mRNA",
  "cultivated seafood", "precision-fermentation dairy", "vertical farming", "desalination",
  "atmospheric water harvesting", "self-healing concrete", "mycelium materials",
  "fusion-fission hybrids", "digital twins", "collaborative robots", "predictive maintenance",
  "battery swapping", "second-life EV packs", "wireless charging roads", "AR windshields",
  "exoskeletons", "myoelectric prosthetics", "retinal implants", "closed-loop insulin",
  "lab-grown tissue", "de-extinction", "algae biofuel", "space-based solar",
  "carbon-negative concrete", "smart dust", "programmable matter", "mind uploading",
  "terraforming Mars", "ocean colonization", "interplanetary internet", "post-scarcity economics"
];
const LENSES = ["overview", "detailed", "applications", "faq", "history", "examples", "frontier outlook"];
const TIERS = ["buildable-now", "research-stage", "research-stage", "research-stage",
               "breakthrough-dependent", "theoretical"];

const seen = new Set();
function makeRecord(k) {
  const topic = TOPICS[Math.floor(rnd() * TOPICS.length)];
  const lens = LENSES[Math.floor(rnd() * LENSES.length)];
  const tier = TIERS[Math.floor(rnd() * TIERS.length)];
  const key = topic + "|" + lens + "|" + tier;
  if (seen.has(key)) return null; // dupe-check
  seen.add(key);
  const yr = 2026 + Math.floor(rnd() * 25);
  return {
    id: PREFIX + "-GEN-" + String(k + 1).padStart(6, "0"),
    slug: SLUG,
    title: topic.charAt(0).toUpperCase() + topic.slice(1) + " (" + lens + ")",
    edition: "public",
    src: "generated",
    generated: true,
    built_by: "generator",
    record_kind: "future technology exploration",
    ai_name: "JAH Future Technology Explorer",
    feasibility_tier: tier,
    body: "Generated exploration of " + topic + " (" + lens + "). Horizon year " + yr +
      ". Labeled generated; not an assistant-built record. Feasibility tier: " + tier + ".",
    note: "Deterministic generator output (seeded). Throttled; hard cap 10^15."
  };
}

function main() {
  const n = parseN(process.argv.slice(2));
  if (n >= HARD_CAP) { console.error("hard cap reached"); process.exit(1); }
  let emitted = 0, attempts = 0;
  const space = TOPICS.length * LENSES.length * TIERS.length;
  while (emitted < n && attempts < n * 10 && seen.size < space) {
    attempts++;
    const rec = makeRecord(emitted);
    if (rec) { console.log(JSON.stringify(rec)); emitted++; }
  }
  console.error("emitted " + emitted + " generated records for " + SLUG +
                " (variation space " + space + ")");
}
main();

// Browser registration (mirrors the JAHDB generator contract used by db pages).
if (typeof window !== "undefined") {
  window.__futureTechGen = { generate: makeRecord, HARD_CAP: HARD_CAP, slug: SLUG };
}
