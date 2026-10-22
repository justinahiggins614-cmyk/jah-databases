// gen-ransac-recognition.js — boundless generator for the RANSAC Recognition database.
// Usage: node gen-ransac-recognition.js --n 5
// Deterministic: a seeded LCG sweeps the inlier tolerance x success confidence: the consensus grid.
// Self-regulating: throttled, duplicate-checked, hard-stops at 10^15 records or when
// the parameter space is genuinely exhausted. Generated records carry "generated": true
// and src "generated" — never mixed with assistant-built records.
"use strict";
const HARD_CAP = 1e15;
const PARAMS = ["tolerance", "confidence"];
const GRID = [[1.0, 1.5, 2.0], [0.95, 0.99]];

function parseN(argv) {
  const i = argv.indexOf("--n");
  if (i >= 0 && argv[i + 1]) {
    const n = parseInt(argv[i + 1], 10);
    if (!isNaN(n) && n >= 0) return Math.min(n, 100000); // throttle per run
  }
  return 5;
}

let seed = 1962;
function rnd() {
  seed = (seed * 1103515245 + 12345) & 0x7fffffff;
  return seed / 0x7fffffff;
}

const seen = new Set();
function totalSpace() {
  return GRID.reduce((a, g) => a * g.length, 1);
}
function makeRecord(k) {
  const combo = GRID.map(g => g[Math.floor(rnd() * g.length)]);
  const key = combo.join(":");
  if (seen.has(key)) return null;           // duplicate check
  seen.add(key);
  const p = {};
  PARAMS.forEach((name, i) => { p[name] = combo[i]; });
  return {
    id: "JAH-KW-RANSAC-GEN-" + String(k + 1).padStart(6, "0"),
    slug: "ransac-recognition",
    title: "Generated inlier tolerance x success confidence: the consensus grid variation " + key,
    params: p,
    edition: "public",
    src: "generated",
    generated: true,
    built_by: "generator",
    record_kind: "ransac recognition record",
    note: "Deterministic parameter-grid variation (inlier tolerance x success confidence: the consensus grid). " +
          "Labeled generated; not an assistant-built record."
  };
}

function main() {
  const n = parseN(process.argv.slice(2));
  if (n >= HARD_CAP) { console.error("hard cap reached"); process.exit(1); }
  const space = totalSpace();
  let emitted = 0, attempts = 0;
  while (emitted < n && attempts < n * 10 && seen.size < space) {
    attempts++;
    const rec = makeRecord(emitted);
    if (rec) { console.log(JSON.stringify(rec)); emitted++; }
  }
  if (seen.size >= space) console.error("parameter space exhausted: genuinely complete at " + space);
  console.error("emitted " + emitted + " generated records");
}
main();
