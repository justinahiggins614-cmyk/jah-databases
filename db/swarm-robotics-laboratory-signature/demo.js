// Working demo for JAH-SWRB-S-000001 (Node port of the record's Python demo).
// Run: node demo.js  — output is byte-identical to the record's expected_output.
const crypto = require("crypto");
const FIGURES = {"best_m": 40, "paths": 130, "robots": 32, "rounds": 26, "scent": 88, "success_pct": 94};
const LABEL = "swarm-robotics-laboratory-signature-000001";
function compute() {
  const vals = Object.values(FIGURES);
  const total = vals.reduce((a, b) => a + b, 0);
  const n = vals.length;
  const mean = Math.round((total / n) * 10000) / 10000;
  return { count: n, label: LABEL, max: Math.max(...vals), mean: mean, min: Math.min(...vals), total: total };
}
// Python prints a float like 40.0, while JS prints 40: format mean the Python way.
function py(v, k) { if (k === "mean") return Number.isInteger(v) ? v + ".0" : String(v); return String(v); }
const outputs = compute();
const result = Object.keys(outputs).sort().map(k => k + "=" + py(outputs[k], k)).join("|");
const h1 = crypto.createHash("sha256").update(result).digest("hex");
const outputs2 = compute();
const result2 = Object.keys(outputs2).sort().map(k => k + "=" + py(outputs2[k], k)).join("|");
const h2 = crypto.createHash("sha256").update(result2).digest("hex");
for (const k of Object.keys(outputs).sort()) console.log(k + ": " + py(outputs[k], k));
console.log("Result: " + result);
console.log("Run 1 SHA-256: " + h1);
console.log("Run 2 SHA-256: " + h2);
console.log("Deterministic: " + (h1 === h2 ? "MATCH" : "MISMATCH"));
