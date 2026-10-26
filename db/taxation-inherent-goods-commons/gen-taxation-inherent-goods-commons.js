// gen-taxation-inherent-goods-commons.js -- boundless generator for the Taxation of Inherent Goods and the Commons Database.
// Usage: node gen-taxation-inherent-goods-commons.js --n 5
// Deterministic seeded variations of the 16 seed records. Self-regulating:
// throttled, duplicate-checked, hard-stops at 10^15 records or when the
// variation space is genuinely exhausted. Generated records carry
// "generated": true and src "generated" -- never mixed with built records.
"use strict";
const HARD_CAP = 1e15;
const TOPICS = ["The Public Trust Doctrine: Commons Held for Everyone", "Severance Taxes on Minerals, Oil, and Gas", "Fishing Licenses and Catch Rights", "Water Rights: Riparian Rules and Prior Appropriation", "Solar Access Laws and the Right to Sunlight", "Spectrum Auctions: Charging for the Airwaves", "Airspace Rights and the Sky Above Land", "The Argument: Tax Only What Government Establishes", "Carbon Pricing and the Cost of Pollution", "Land Value Taxation: Taxing Location, Not Improvement", "Commons Trusts: The Alaska Permanent Fund Model", "Grazing Fees on Public Lands", "Timber Sales on Public Lands", "Beach Access and Shoreline Ownership", "Wind Rights and Offshore Leases", "Inherent Property and Identity: Name, Signature, and DNA in Law"];
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
  return { id: "JAH-TIGC-GEN-" + String(k + 1).padStart(6, "0"), slug: "taxation-inherent-goods-commons",
    title: "Generated " + topic + " parameter variation v" + variant,
    edition: "public", src: "generated", generated: true, built_by: "generator",
    record_kind: "inherent goods taxation record", feasibility_tier: "established",
    note: "Deterministic parameter variation (" + key + ") over the 16 seed records. Labeled generated; not a built record." };
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
  console.error("emitted " + emitted + " generated records for taxation-inherent-goods-commons");
}
main();
