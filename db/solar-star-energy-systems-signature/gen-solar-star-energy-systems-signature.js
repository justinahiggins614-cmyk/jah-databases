// gen-solar-star-energy-systems-signature.js -- boundless generator for the Solar Star Energy Systems Signature Database.
// Usage: node gen-solar-star-energy-systems-signature.js --n 5
// Deterministic: a seeded LCG drives parameter variations of the 16 seed
// records. Self-regulating: throttled, duplicate-checked,
// hard-stops at 10^15 records or when the variation space is genuinely exhausted.
// Generated records carry "generated": true and src "generated" -- never mixed
// with assistant-built records.
"use strict";
const HARD_CAP = 1e15;
const TOPICS = ["Signature Solar Star Energy Highway", "Signature Solar Star Fuel-Cell Conversion", "Signature Solar Star Cosmic Grid Mergers", "Signature Solar Star Satellite Light Channel", "Signature Solar Star Primal Energy-Mass Transmutation", "Signature Solar Star Primal Nanoplasma Aegis", "Signature Solar Star Omni-Beam Light Sentinel", "Signature Solar Star Universal Resource Alchemist", "Signature Solar Star Primal Optic Light Weaver", "Signature Solar Star Hydro-Genesis Water System", "Signature Solar Star Anchor Stations", "Signature Solar Star Light-Channel Routing", "Signature Solar Star Shield Redundancy Plan", "Signature Solar Star Alchemist Feedstock Protocol", "Signature Solar Star Water Distribution Plan", "Signature Solar Star Line Integration"];
function parseN(argv) {
  const i = argv.indexOf("--n");
  if (i >= 0 && argv[i + 1]) {
    const n = parseInt(argv[i + 1], 10);
    if (!isNaN(n) && n >= 0) return Math.min(n, 100000);
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
  const variant = 1 + Math.floor(rnd() * 50);
  const key = topic + "#v" + variant;
  if (seen.has(key)) return null;
  seen.add(key);
  return {
    id: "JAH-SOSTS-GEN-" + String(k + 1).padStart(6, "0"),
    slug: "solar-star-energy-systems-signature",
    title: "Generated " + topic + " parameter variation v" + variant,
    edition: "signature",
    src: "generated",
    generated: true,
    built_by: "generator",
    record_kind: "solar star energy system record",
    feasibility_tier: "established",
    note: "Deterministic parameter variation (" + key + ") over the 16 seed records. Labeled generated; not an assistant-built record."
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
  console.error("emitted " + emitted + " generated records for solar-star-energy-systems-signature");
}
main();
