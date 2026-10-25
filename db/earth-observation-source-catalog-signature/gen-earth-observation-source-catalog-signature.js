// gen-earth-observation-source-catalog-signature.js -- boundless generator for the Signature Earth Observation Source Catalog Database.
// Usage: node gen-earth-observation-source-catalog-signature.js --n 5
// Deterministic: a seeded LCG drives per-topic parameter variations of the
// 12 seed collection-topic records. Self-regulating: throttled,
// duplicate-checked, hard-stops at 10^15 records or when the variation
// space is genuinely exhausted. Generated records carry "generated": true
// and src "generated" -- never mixed with assistant-built records.
// Catalog records only: nothing here claims a dataset has been ingested.
"use strict";
const HARD_CAP = 1e15;

const TOPICS = [
  "Atmospheric Science",
  "Land Processes",
  "Oceanography",
  "Cryosphere",
  "Hydrology",
  "Biogeochemistry and Ecosystems",
  "Geodesy and Solid Earth",
  "Socioeconomic Data",
  "Climate Data Records",
  "Earth Engine Satellite Imagery Collections",
  "National Weather and Climate Services",
  "Land Resources and Mapping"
];

function parseN(argv) {
  const i = argv.indexOf("--n");
  if (i >= 0 && argv[i + 1]) {
    const n = parseInt(argv[i + 1], 10);
    if (!isNaN(n) && n >= 0) return Math.min(n, 100000); // throttle per run
  }
  return 5;
}

let seed = 20261025;
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
    id: "JAH-G29-EOBS-GEN-" + String(k + 1).padStart(6, "0"),
    slug: "earth-observation-source-catalog-signature",
    title: "Generated " + topic + " catalog variation v" + variant,
    edition: "signature",
    src: "generated",
    generated: true,
    built_by: "generator",
    record_kind: "source catalog record",
    feasibility_tier: "signature",
    note: "Deterministic parameter variation (" + key + ") over the 12 seed " +
          "collection-topic records. Labeled generated and simulated; not an " +
          "assistant-built record and not a claim that any dataset was ingested."
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
  console.error("emitted " + emitted + " generated records for earth-observation-source-catalog-signature");
}
main();
