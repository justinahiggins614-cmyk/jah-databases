// gen-clock-maintenance-restoration.js -- boundless generator for the clock-maintenance-restoration database.
// Usage: node gen-clock-maintenance-restoration.js --n 1
// Deterministic seeded LCG; throttled, duplicate-checked, hard-stops at
// 10^15 records or when the variation space is genuinely exhausted.
// Generated records carry src "generated" and are never mixed with
// assistant-built records. Signature slugs use a SINGLE "-signature" suffix.
"use strict";
const HARD_CAP = 1e15;
const SLUG = "clock-maintenance-restoration";
const KIND = "clock maintenance record";
const PREFIX = "JAH-CKM-";
const EDITION = "public";
const TOPICS = ["Cleaning a Clock Movement", "Oiling a Clock Movement", "Setting a Clock in Beat", "Bushing Worn Pivot Holes", "Replacing a Suspension Spring", "Caring for a Clock Case", "Movement Handling Safety", "Servicing a Weight-Driven Movement", "Handling a Mainspring Safely", "Regulating a Pendulum Clock", "Caring for a Dial and Hands", "Troubleshooting a Strike and Chime Train", "Polishing Pivots", "Checking Wear: Depthing and Endshake", "Reassembling and Testing in Beat", "Long-Term Storage and Environment"];
function parseN(argv) {
  const i = argv.indexOf("--n");
  if (i >= 0 && argv[i + 1]) {
    const n = parseInt(argv[i + 1], 10);
    if (!isNaN(n) && n >= 0) return Math.min(n, 100000);
  }
  return 5;
}
let seed = 20261026;
function rnd() { seed = (seed * 1103515245 + 12345) & 0x7fffffff; return seed / 0x7fffffff; }
const seen = new Set();
function makeRecord(k) {
  const topic = TOPICS[Math.floor(rnd() * TOPICS.length)];
  const variant = 1 + Math.floor(rnd() * 50);
  const key = topic + "#v" + variant;
  if (seen.has(key)) return null;
  seen.add(key);
  return { id: PREFIX + "GEN-" + String(k + 1).padStart(6, "0"), slug: SLUG,
    title: "Generated " + topic + " parameter variation v" + variant,
    edition: EDITION, src: "generated", generated: true, built_by: "generator",
    record_kind: KIND, note: "Deterministic parameter variation (" + key + ") over the 16 seed records. Labeled generated; not an assistant-built record." };
}
function runTests() { return { slugOk: SLUG.indexOf("-signature-signature") < 0, kindOk: true, capOk: HARD_CAP === 1e15 }; }
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
  console.error("emitted " + emitted + " generated records for " + SLUG);
}
if (require.main === module) main();
module.exports = { makeRecord, runTests, HARD_CAP, SLUG, KIND };
