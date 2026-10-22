// gen-pentagon-finder-signature.js -- boundless generator for the Pentagon Finder database.
// Usage: node gen-pentagon-finder-signature.js --n 5
// Deterministic: a seeded LCG drives angle-tolerance variations of the pentagon rule.
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

let seed = 20241033;
function rnd() {
  seed = (seed * 1103515245 + 12345) & 0x7fffffff;
  return seed / 0x7fffffff;
}

const seen = new Set();
function makeRecord(k) {
  const tol = 12 + Math.floor(rnd() * 13);        // 12..24 deg
  const key = "tol" + tol;
  if (seen.has(key)) return null;
  seen.add(key);
  return {
    id: "JAH-SF-PENT-GEN-" + String(k + 1).padStart(6, "0"),
    slug: "pentagon-finder-signature",
    title: "Generated Pentagon Finder rule variation " + key,
    edition: "public",
    src: "generated",
    generated: true,
    built_by: "generator",
    record_kind: "shape finder record",
    note: "Deterministic variation of the Pentagon Finder knowing-when rule (" + key + "). " +
          "Labeled generated; not an assistant-built record."
  };
}

function main() {
  const n = parseN(process.argv.slice(2));
  if (n >= HARD_CAP) { console.error("hard cap reached"); process.exit(1); }
  let emitted = 0, attempts = 0;
  while (emitted < n && attempts < n * 10 && seen.size < 13) {
    attempts++;
    const rec = makeRecord(emitted);
    if (rec) { console.log(JSON.stringify(rec)); emitted++; }
  }
  console.error("emitted " + emitted + " generated records for pentagon-finder-signature");
}
main();
