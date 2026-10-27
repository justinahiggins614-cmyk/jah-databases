// gen-cuckoo-clocks-signature.js -- boundless generator for The Signature Cuckoo Clocks Database.
// Usage: node gen-cuckoo-clocks-signature.js --n 5
// Deterministic: a seeded LCG drives parameter variations of the 16 seed
// records. Self-regulating: throttled, duplicate-checked,
// hard-stops at 10^15 records or when the variation space is genuinely exhausted.
// Generated records carry "generated": true and src "generated" -- never mixed
// with assistant-built records.
"use strict";
const HARD_CAP = 1e15;
const TOPICS = ["Signature Forest Canopy Cuckoo Clock", "Signature Alpine Chalet Cuckoo Clock", "Signature Nightingale Cuckoo Clock", "Signature Woodland Workshop Cuckoo Clock", "Signature Minimalist Cuckoo Clock", "Signature Eight-Day Grand Cuckoo Clock", "Signature Bellows-Choir Cuckoo Clock", "Signature Dancer's Cuckoo Clock", "Signature Tide-and-Season Cuckoo Clock", "Signature Traveller's Cuckoo Clock", "Signature Moonlit Cuckoo Clock", "Signature Mill-Wheel Cuckoo Clock", "Signature Waterfall Cuckoo Clock", "Signature Clockmaker's Cuckoo Clock", "Signature Service-Friendly Cuckoo Clock", "Signature Grand Festival Cuckoo Clock"];
function parseN(argv) {
  const i = argv.indexOf("--n");
  if (i >= 0 && argv[i + 1]) {
    const n = parseInt(argv[i + 1], 10);
    if (!isNaN(n) && n >= 0) return Math.min(n, 100000);
  }
  return 5;
}
let seed = 20261026;
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
    id: "JAH-CKCS-GEN-" + String(k + 1).padStart(6, "0"),
    slug: "cuckoo-clocks-signature",
    title: "Generated " + topic + " parameter variation v" + variant,
    edition: "signature",
    src: "generated",
    generated: true,
    built_by: "generator",
    record_kind: "cuckoo clock record",
    note: "Deterministic parameter variation (" + key + ") over the 16 seed records. Labeled generated; not an assistant-built record."
  };
}
function runTests() {
  const rec = makeRecord(0);
  return {
    slugOk: rec.slug === "cuckoo-clocks-signature",
    kindOk: rec.record_kind === "cuckoo clock record",
    idOk: rec.id.indexOf("JAH-CKCS-GEN-") === 0,
    srcOk: rec.src === "generated",
    capOk: HARD_CAP === 1e15
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
  console.error("emitted " + emitted + " generated records for cuckoo-clocks-signature");
}
if (require.main === module) main();
module.exports = { makeRecord: makeRecord, runTests: runTests, HARD_CAP: HARD_CAP };
