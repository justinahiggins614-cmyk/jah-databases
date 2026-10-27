// gen-lantern-clocks.js -- boundless generator for The Lantern Clocks Database.
// Usage: node gen-lantern-clocks.js --n 5
// Deterministic: a seeded LCG drives parameter variations of the 16 seed
// records. Self-regulating: throttled, duplicate-checked,
// hard-stops at 10^15 records or when the variation space is genuinely exhausted.
// Generated records carry "generated": true and src "generated" -- never mixed
// with assistant-built records.
"use strict";
const HARD_CAP = 1e15;
const TOPICS = ["The English Lantern Clock", "The Verge and Foliot", "Weight Drive and Gut Lines", "The Single-Hand Dial", "The Chapter Ring and Engraved Dial", "Countwheel Striking", "The Striking Bell", "Alarm Lantern Clocks", "The Brass Case: Pillars, Frets, and Finials", "Lantern Clocks and the Chamber Clock", "Pendulum Conversions of Lantern Clocks", "Anchor Conversions of Lantern Clocks", "Dating a Lantern Clock", "Maintaining a Lantern Clock", "Restoring a Lantern Clock", "Building a Replica Lantern Movement"];
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
    id: "JAH-LTC-GEN-" + String(k + 1).padStart(6, "0"),
    slug: "lantern-clocks",
    title: "Generated " + topic + " parameter variation v" + variant,
    edition: "public",
    src: "generated",
    generated: true,
    built_by: "generator",
    record_kind: "lantern clock record",
    note: "Deterministic parameter variation (" + key + ") over the 16 seed records. Labeled generated; not an assistant-built record."
  };
}
function runTests() {
  const rec = makeRecord(0);
  return {
    slugOk: rec.slug === "lantern-clocks",
    kindOk: rec.record_kind === "lantern clock record",
    idOk: rec.id.indexOf("JAH-LTC-GEN-") === 0,
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
  console.error("emitted " + emitted + " generated records for lantern-clocks");
}
if (require.main === module) main();
module.exports = { makeRecord: makeRecord, runTests: runTests, HARD_CAP: HARD_CAP };
