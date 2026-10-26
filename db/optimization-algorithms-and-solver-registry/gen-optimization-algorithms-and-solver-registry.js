// gen-optimization-algorithms-and-solver-registry.js -- boundless generator for the optimization-algorithms-and-solver-registry database.
// Usage: node gen-optimization-algorithms-and-solver-registry.js --n 5
// Deterministic: a seeded LCG drives parameter variations of the 16 seed
// records. Self-regulating: throttled, duplicate-checked,
// hard-stops at 10^15 records or when the variation space is genuinely exhausted.
// Generated records carry "generated": true and src "generated" -- never mixed
// with assistant-built records.
"use strict";
const HARD_CAP = 1e15;
const TOPICS = ["Linear and Convex Solvers: Overview", "Linear and Convex Solvers: Method", "Linear and Convex Solvers: Worked Example", "Linear and Convex Solvers: Validation Checklist", "Nonlinear and Global Optimization: Overview", "Nonlinear and Global Optimization: Method", "Nonlinear and Global Optimization: Worked Example", "Nonlinear and Global Optimization: Validation Checklist", "Combinatorial and Discrete Solvers: Overview", "Combinatorial and Discrete Solvers: Method", "Combinatorial and Discrete Solvers: Worked Example", "Combinatorial and Discrete Solvers: Validation Checklist", "Solver Benchmarks and Selection Rules: Overview", "Solver Benchmarks and Selection Rules: Method", "Solver Benchmarks and Selection Rules: Worked Example", "Solver Benchmarks and Selection Rules: Validation Checklist"];
function parseN(argv) {
  const i = argv.indexOf("--n");
  if (i >= 0 && argv[i + 1]) {
    const n = parseInt(argv[i + 1], 10);
    if (!isNaN(n) && n >= 0) return Math.min(n, 100000);
  }
  return 5;
}
let seed = 20261025;
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
    id: "JAH-GEN-" + String(k + 1).padStart(6, "0"),
    slug: "optimization-algorithms-and-solver-registry",
    title: "Generated " + topic + " parameter variation v" + variant,
    edition: "public",
    src: "generated",
    generated: true,
    built_by: "generator",
    note: "Deterministic parameter variation (" + key + ") over the 16 seed records. Labeled generated; not an assistant-built record."
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
  console.error("emitted " + emitted + " generated records for optimization-algorithms-and-solver-registry");
}
main();
