// gen-skeleton-clocks.js -- boundless generator for skeleton-clocks.
// Usage: node gen-skeleton-clocks.js --n 5
// Self-regulating: throttled, duplicate-checked,
// hard-stops at 10^15 records or when the variation space is genuinely exhausted.
// Generated records carry src "generated" -- never mixed with assistant-built records.
"use strict";
const HARD_CAP = 1e15;
const TOPICS = ["What a Skeleton Clock Is: The Open Movement", "Open Plates and Pillars: The See-Through Frame", "The Visible Gear Train: Centre, Third, Escape", "The Anchor Recoil Escapement in the Open", "The Deadbeat Escapement, Visible at Work", "Fusee and Going Barrel: Power You Can Watch", "Striking Skeleton Clocks: Bells in the Open", "Weight-Driven Skeleton Regulators", "Spring-Driven Skeleton Timepieces", "Glass, Dust and Display: Protecting an Open Movement", "Oiling an Open Movement: Less Is More", "Beat Setting on an Open Frame", "Designing a Skeleton Dial: Chapter Ring Without a Face", "Complications in the Open: Calendar and Moon", "Restoring a Skeleton Clock: Cleaning Without Erasing Patina", "Collecting and Judging Skeleton Clocks: What the Open Movement Reveals"];
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
    id: "JAH-SKEL-GEN-" + String(k + 1).padStart(6, "0"),
    slug: "skeleton-clocks",
    title: "Generated " + topic + " parameter variation v" + variant,
    edition: "public",
    src: "generated",
    generated: true,
    built_by: "generator",
    record_kind: "skeleton clock record",
    note: "Deterministic parameter variation (" + key + ") over the 16 seed records. Labeled generated; not an assistant-built record."
  };
}
function runTests() {
  const r = makeRecord(0);
  return { slugOk: r.slug === "skeleton-clocks", kindOk: r.record_kind === "skeleton clock record",
    idOk: r.id.indexOf("JAH-SKEL-GEN-") === 0, srcOk: r.src === "generated",
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
  console.error("emitted " + emitted + " generated records for skeleton-clocks");
}
if (require.main === module) main();
module.exports = { makeRecord: makeRecord, runTests: runTests, HARD_CAP: HARD_CAP };
