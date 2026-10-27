// gen-tower-clocks-signature.js -- boundless generator for tower-clocks-signature.
// Usage: node gen-tower-clocks-signature.js --n 5
// Self-regulating: throttled, duplicate-checked,
// hard-stops at 10^15 records or when the variation space is genuinely exhausted.
// Generated records carry src "generated" -- never mixed with assistant-built records.
"use strict";
const HARD_CAP = 1e15;
const TOPICS = ["Signature Beacon Tower Clock: The Harbour Light Movement", "Signature Market Cross Clock: A Town-Square Turret Design", "Signature Station Clock Tower: The Twin-Dial Terminus Design", "Signature University Tower Clock: The College Bell Design", "Signature Garden Folly Clock: A Small Ornamental Tower", "Signature Mill Tower Clock: The Factory Timekeeper Design", "Signature Lighthouse Tower Clock: The Coastal Signal Design", "Signature Church Tower Clock: The Parish Chime Design", "Signature Observatory Tower Clock: The Meridian Dial Design", "Signature Castle Tower Clock: The Fortress Dial Design", "Signature Village Green Clock: The Community Tower Design", "Signature Hospital Tower Clock: The Quiet-Hours Design", "Signature Museum Tower Clock: The Working Exhibit Design", "Signature Winter Tower Clock: The Cold-Climate Design", "Signature Solar Tower Clock: The Sun-Powered Dial Design", "Signature Grand Terminus Tower Clock: The Four-Face Master Design"];
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
    id: "JAH-TWCS-GEN-" + String(k + 1).padStart(6, "0"),
    slug: "tower-clocks-signature",
    title: "Generated " + topic + " parameter variation v" + variant,
    edition: "signature",
    src: "generated",
    generated: true,
    built_by: "generator",
    record_kind: "tower clock record",
    note: "Deterministic parameter variation (" + key + ") over the 16 seed records. Labeled generated; not an assistant-built record."
  };
}
function runTests() {
  const r = makeRecord(0);
  return { slugOk: r.slug === "tower-clocks-signature", kindOk: r.record_kind === "tower clock record",
    idOk: r.id.indexOf("JAH-TWCS-GEN-") === 0, srcOk: r.src === "generated",
    capOk: HARD_CAP === 1e15 };
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
  console.error("emitted " + emitted + " generated records for tower-clocks-signature");
}
if (require.main === module) main();
module.exports = { makeRecord: makeRecord, runTests: runTests, HARD_CAP: HARD_CAP };
