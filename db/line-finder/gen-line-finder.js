// gen-line-finder.js -- boundless generator for the Line Finder database.
// Usage: node gen-line-finder.js --n 5
// Deterministic: a seeded LCG drives threshold and angle-step variations of the Hough line rule.
// Self-regulating: throttled, duplicate-checked, hard-stops at 10^15 records or when
// the variation space is genuinely exhausted. Generated records carry "generated": true
// and src "generated" -- never mixed with assistant-built records.
"use strict";
const HARD_CAP = 1e15;

function parseN(argv) {
  const i = argv.indexOf("--n");
  if (i >= 0 && argv[i + 1]) {
    const n = parseInt(argv[i + 1], 10);
    if (!isNaN(n) && n >= 0) return Math.min(n, 100000); // throttle per run
  }
  return 5;
}

let seed = 20241022;
function rnd() {
  seed = (seed * 1103515245 + 12345) & 0x7fffffff;
  return seed / 0x7fffffff;
}

const seen = new Set();
function makeRecord(k) {
  const voteMin = 8 + Math.floor(rnd() * 9);      // 8..16
  const tstep = [5, 10, 15][Math.floor(rnd() * 3)];
  const key = voteMin + ":" + tstep;
  if (seen.has(key)) return null;
  seen.add(key);
  return {
    id: "JAH-SF-LINE-GEN-" + String(k + 1).padStart(6, "0"),
    slug: "line-finder",
    title: "Generated Line Finder rule variation " + key,
    edition: "public",
    src: "generated",
    generated: true,
    built_by: "generator",
    record_kind: "shape finder record",
    note: "Deterministic variation of the Line Finder knowing-when rule (" + key + "). " +
          "Labeled generated; not an assistant-built record."
  };
}

function main() {
  const n = parseN(process.argv.slice(2));
  if (n >= HARD_CAP) { console.error("hard cap reached"); process.exit(1); }
  let emitted = 0, attempts = 0;
  while (emitted < n && attempts < n * 10 && seen.size < 27) {
    attempts++;
    const rec = makeRecord(emitted);
    if (rec) { console.log(JSON.stringify(rec)); emitted++; }
  }
  console.error("emitted " + emitted + " generated records for line-finder");
}
main();
