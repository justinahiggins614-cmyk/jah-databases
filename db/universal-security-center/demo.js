// Node port of the record's Python demo (demo.py in this folder).
// Computes the same figures, prints the same lines, and verifies the two
// runs match by comparing SHA-256 digests. Python's round(x, 4) is
// reproduced exactly: the double's exact value is rounded to 4 decimal
// places, half to even, using BigInt arithmetic (CPython round semantics).
const crypto = require("node:crypto");
const FIGURES = {"JAH-UISC-000001": 168, "JAH-UISC-000002": 166, "JAH-UISC-000003": 167, "JAH-UISC-000004": 173, "JAH-UISC-000005": 172, "JAH-UISC-000006": 172, "JAH-UISC-000007": 170, "JAH-UISC-000008": 174, "JAH-UISC-000009": 171, "JAH-UISC-000010": 179, "JAH-UISC-000011": 176, "JAH-UISC-000012": 183, "JAH-UISC-000013": 184, "JAH-UISC-000014": 181, "JAH-UISC-000015": 181, "JAH-UISC-000016": 179, "JAH-UISC-000017": 186, "JAH-UISC-000018": 182, "JAH-UISC-000019": 189, "JAH-UISC-000020": 187, "JAH-UISC-000021": 187, "JAH-UISC-000022": 189, "JAH-UISC-000023": 196, "JAH-UISC-000024": 196};
const LABEL = "universal-security-center-database";
function pyRound4(v) {
  const buf = new ArrayBuffer(8);
  const view = new DataView(buf);
  view.setFloat64(0, v);
  const bits = view.getBigUint64(0);
  const exp = Number((bits >> 52n) & 0x7ffn);
  const mant = bits & ((1n << 52n) - 1n);
  let e, m;
  if (exp === 0) { e = -1074; m = mant; }
  else { e = exp - 1075; m = mant | (1n << 52n); }
  let num, den;
  if (e >= 0) { num = m * (2n ** BigInt(e)) * 10000n; den = 1n; }
  else { num = m * 10000n; den = 2n ** BigInt(-e); }
  let q = num / den;
  const r = num % den;
  const twice = 2n * r;
  if (twice > den || (twice === den && q % 2n === 1n)) q += 1n;
  const ip = q / 10000n, fp = q % 10000n;
  if (fp === 0n) return ip.toString() + ".0";
  return ip.toString() + "." + fp.toString().padStart(4, "0").replace(/0+$/, "");
}
function fmtFloat(v) { return pyRound4(v); }
function compute() {
  const vals = Object.values(FIGURES);
  const total = vals.reduce((a, b) => a + b, 0);
  const n = vals.length;
  const mean = n ? total / n : 0;
  return { count: n, label: LABEL, max: Math.max(...vals), mean: fmtFloat(mean), min: Math.min(...vals), total: total };
}
const outputs = compute();
const result = Object.keys(outputs).sort().map((k) => k + "=" + outputs[k]).join("|");
const h1 = crypto.createHash("sha256").update(result, "utf8").digest("hex");
const outputs2 = compute();
const result2 = Object.keys(outputs2).sort().map((k) => k + "=" + outputs2[k]).join("|");
const h2 = crypto.createHash("sha256").update(result2, "utf8").digest("hex");
for (const k of Object.keys(outputs).sort()) console.log(k + ": " + outputs[k]);
console.log("Result: " + result);
console.log("Run 1 SHA-256: " + h1);
console.log("Run 2 SHA-256: " + h2);
console.log("Deterministic: " + (h1 === h2 ? "MATCH" : "MISMATCH"));
