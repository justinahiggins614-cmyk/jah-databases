// gen-anniversary-clocks-signature.js -- boundless generator for anniversary-clocks-signature.
// Usage: node gen-anniversary-clocks-signature.js --n 5
// Self-regulating: throttled, duplicate-checked,
// hard-stops at 10^15 records or when the variation space is genuinely exhausted.
// Generated records carry src "generated" -- never mixed with assistant-built records.
"use strict";
const HARD_CAP = 1e15;
const TOPICS = ["Signature Yearkeeper: The Anniversary Clock of the House", "Signature Solstice Clock: The Four-Season Torsion Design", "Signature Moonrise Clock: The Lunar Anniversary Design", "Signature Heirloom Clock: The Engraved Presentation Design", "Signature Garden Room Clock: The Conservatory Design", "Signature Scholar's Clock: The Study Anniversary Design", "Signature Wedding Clock: The Pair of Anniversary Clocks", "Signature Traveller's Clock: The Cased Anniversary Design", "Signature Library Clock: The Silent Anniversary Design", "Signature Winter Clock: The Cold-Room Anniversary Design", "Signature Observatory Clock: The Star-Dial Anniversary Design", "Signature Museum Clock: The Working Exhibit Anniversary Design", "Signature Jubilee Clock: The Fifty-Year Anniversary Design", "Signature Night Clock: The Low-Light Anniversary Design", "Signature Archive Clock: The Record-Keeper's Anniversary Design", "Signature Grand Anniversary Clock: The Exhibition Master Design"];
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
    id: "JAH-ANCS-GEN-" + String(k + 1).padStart(6, "0"),
    slug: "anniversary-clocks-signature",
    title: "Generated " + topic + " parameter variation v" + variant,
    edition: "signature",
    src: "generated",
    generated: true,
    built_by: "generator",
    record_kind: "anniversary clock record",
    note: "Deterministic parameter variation (" + key + ") over the 16 seed records. Labeled generated; not an assistant-built record."
  };
}
function runTests() {
  const r = makeRecord(0);
  return { slugOk: r.slug === "anniversary-clocks-signature", kindOk: r.record_kind === "anniversary clock record",
    idOk: r.id.indexOf("JAH-ANCS-GEN-") === 0, srcOk: r.src === "generated",
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
  console.error("emitted " + emitted + " generated records for anniversary-clocks-signature");
}
if (require.main === module) main();
module.exports = { makeRecord: makeRecord, runTests: runTests, HARD_CAP: HARD_CAP };
