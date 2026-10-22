// gen-feature-hierarchy-recognition-signature.js — boundless generator for the Feature Hierarchy Recognition — Signature Edition database.
// Usage: node gen-feature-hierarchy-recognition-signature.js --n 5
// Deterministic: a seeded LCG sweeps the composition bar x wobble budget: the assembly grid.
// Self-regulating: throttled, duplicate-checked, hard-stops at 10^15 records or when
// the parameter space is genuinely exhausted. Generated records carry "generated": true
// and src "generated" — never mixed with assistant-built records.
"use strict";
const HARD_CAP = 1e15;
const PARAMS = ["tauScore", "wobbleBudget"];
const GRID = [[0.6, 0.7, 0.8], [2.0, 4.0, 8.0]];

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
    id: "JAH-KW-FEAT-GEN-" + String(k + 1).padStart(6, "0"),
    slug: "feature-hierarchy-recognition-signature",
    title: "Generated composition bar x wobble budget: the assembly grid variation " + key,
    params: p,
    edition: "signature",
    src: "generated",
    generated: true,
    built_by: "generator",
    record_kind: "feature hierarchy recognition record",
    note: "Deterministic parameter-grid variation (composition bar x wobble budget: the assembly grid). " +
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
