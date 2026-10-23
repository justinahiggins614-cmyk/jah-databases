// gen-technology.js -- boundless generator for the Technology Database.
// Usage: node gen-technology.js --n 5
// Deterministic: a seeded LCG drives per-topic parameter variations of the 48
// landmark technologies. Self-regulating: throttled, duplicate-checked,
// hard-stops at 10^15 records or when the variation space is genuinely exhausted.
// Generated records carry "generated": true and src "generated" -- never mixed
// with assistant-built records.
"use strict";
const HARD_CAP = 1e15;

const TOPICS = [
  "Transistor","Integrated Circuit","World Wide Web","Relational Database",
  "Public-Key Cryptography","Graphics Processing Unit",
  "Steam Engine","Photovoltaic Cell","Lithium-Ion Battery","Nuclear Fission Reactor",
  "Wind Turbine","Hydroelectric Dam",
  "Steam Locomotive","Automobile (internal combustion)","Jet Engine","Container Shipping",
  "Maglev Train","Bicycle",
  "Germ Theory & Antisepsis","Vaccination","Antibiotics (Penicillin)","X-Ray Imaging",
  "MRI","mRNA Vaccines",
  "Steel (Bessemer Process)","Reinforced Concrete","Plastic (Bakelite)","Carbon Fiber",
  "Semiconductor Silicon","Graphene",
  "Telegraph","Telephone","Radio","Television","Fiber Optics","Smartphone",
  "Interchangeable Parts","Assembly Line","Programmable Logic Controller","CNC Machine",
  "Industrial Robot","3D Printing",
  "Seed Drill","Mechanical Reaper","Haber-Bosch Process","Tractor",
  "Drip Irrigation","Dwarf Wheat (Green Revolution)"
];

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

const seen = new Set();
function makeRecord(k) {
  const topic = TOPICS[Math.floor(rnd() * TOPICS.length)];
  const variant = 1 + Math.floor(rnd() * 50);   // parameter-set variant 1..50
  const key = topic + "#v" + variant;
  if (seen.has(key)) return null;
  seen.add(key);
  return {
    id: "JAH-TECH-GEN-" + String(k + 1).padStart(6, "0"),
    slug: "technology",
    title: "Generated " + topic + " parameter variation v" + variant,
    edition: "public",
    src: "generated",
    generated: true,
    built_by: "generator",
    record_kind: "technology record",
    feasibility_tier: "established",
    note: "Deterministic parameter variation (" + key + ") over the 48 landmark " +
          "technologies. Labeled generated; not an assistant-built record."
  };
}

function main() {
  const n = parseN(process.argv.slice(2));
  if (n >= HARD_CAP) { console.error("hard cap reached"); process.exit(1); }
  const space = TOPICS.length * 50;
  let emitted = 0, attempts = 0;
  while (emitted < n && attempts < n * 20 && seen.size < space) {
    attempts++;
    const rec = makeRecord(emitted);
    if (rec) { console.log(JSON.stringify(rec)); emitted++; }
  }
  console.error("emitted " + emitted + " generated records for technology");
}
main();
