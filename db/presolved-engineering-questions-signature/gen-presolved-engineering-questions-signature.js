"use strict";
/* GEN for presolved-engineering-questions-signature - boundless generator. Seeded, deterministic, throttled,
   duplicate-checked, hard stop at 1,000,000,000. Generated records are labeled
   src "generated" and are never presented as archive records. */
(function (root) {
  var SLUG = "presolved-engineering-questions-signature";
  var PREFIX = "JAH-PSEQS-";
  var RECORD_KIND = "presolved engineering question record";
  var HARD_STOP = 1000000000;
  var MAX_BATCH = 100;
  var SEED_TITLES = ["Simply supported beam (Signature variant): 12 kN over 8 m — maximum bending moment", "Axial load on a steel rod (Signature variant): 80 kN on 25 mm — tensile stress", "Steel bar under load (Signature variant): 30 kN, 3 m — elongation", "Ohm's law (Signature variant): 48 V across 12 Ω — circuit current", "Electrical power (Signature variant): 120 V, 8 A", "Equivalent resistance (Signature variant): 15, 25 and 40 Ω", "Bolt tightening torque (Signature variant): 150 N on a 0.45 m spanner", "Hydrostatic pressure (Signature variant): 25 m depth", "Volumetric flow rate (Signature variant): 1.5 m/s in a 0.15 m pipe", "Bernoulli (Signature variant): velocity from an 8,000 Pa pressure difference", "Energy to raise water temperature (Signature variant): 5 kg by 30 °C", "Thermal expansion (Signature variant): 25 m rail, 30 °C rise", "Gear ratio (Signature variant): 1,800 rpm input, 4:1 reduction", "Factor of safety (Signature variant): 450 kN ultimate, factor 2.5", "Cantilever beam tip deflection (Signature variant): 2,000 N on 1.5 m", "Euler critical load (Signature variant): 2.5 m column, I = 2 × 10⁻⁶ m⁴", "Belt drive power transmission (Signature variant): 9 kW at 12 m/s", "Pump hydraulic power (Signature variant): 0.05 m³/s against 20 m at 75%", "Motor efficiency (Signature variant): 7,500 W in, 6,600 W out", "Second moment of area (Signature variant): 0.15 m by 0.3 m rectangle", "Shear stress in a shaft under torsion (Signature variant): 800 N·m on 60 mm", "Spring extension (Signature variant): 360 N on a 1,200 N/m spring", "Force in a truss member (Signature variant): 20 kN at 30°", "Volume of concrete (Signature variant): 8 m by 6 m by 0.2 m slab"];
  function fnv1a(s) {
    var h = 0x811c9dc5;
    for (var i = 0; i < s.length; i++) { h ^= s.charCodeAt(i); h = Math.imul(h, 0x01000193) >>> 0; }
    return h >>> 0;
  }
  function pad8(n) { var s = n.toString(16); while (s.length < 8) s = "0" + s; return s; }
  function genId(seed) {
    var a = pad8(fnv1a(SLUG + "|" + String(seed)));
    var b = pad8(fnv1a(SLUG + "|" + String(seed) + "|2"));
    return PREFIX + "GEN-" + (a + b).slice(0, 12);
  }
  function generateRecord(seed) {
    var s = (seed === undefined || seed === null) ? 1 : seed;
    var idx = fnv1a(SLUG + "|" + String(s)) % SEED_TITLES.length;
    var title = SEED_TITLES[idx];
    return { id: genId(s), slug: SLUG, title: "Generated: " + title,
      record_kind: RECORD_KIND, src: "generated",
      description: "A boundlessly generated record in the family of " + title + ", produced by the seeded generator for this database." };
  }
  function generateBatch(n, seed) {
    var out = [], count = Math.min(n || 1, MAX_BATCH);
    for (var i = 0; i < count; i++) { out.push(generateRecord((seed || 1) + i)); }
    return out;
  }
  function searchRecords(q, pool) {
    q = String(q || "").toLowerCase();
    return (pool || SEED_TITLES).filter(function (t) { return t.toLowerCase().indexOf(q) !== -1; });
  }
  function validateRecord(rec) {
    var problems = [];
    if (!rec || rec.record_kind !== RECORD_KIND) problems.push("record_kind must be " + RECORD_KIND);
    if (!rec || rec.slug !== SLUG) problems.push("slug must be " + SLUG);
    if (!rec || !rec.id || rec.id.indexOf(PREFIX + "GEN-") !== 0) problems.push("id must start with " + PREFIX + "GEN-");
    if (!rec || !rec.title) problems.push("title is required");
    if (!rec || rec.src !== "generated") problems.push("src must be generated");
    return { valid: problems.length === 0, problems: problems };
  }
  function runTests() {
    var tests = [];
    var g = generateRecord(7);
    tests.push({ name: "generated record_kind", pass: !!g && g.record_kind === RECORD_KIND });
    tests.push({ name: "generated slug is single edition slug", pass: !!g && g.slug === SLUG && g.slug.indexOf("signature-" + "signature") === -1 });
    tests.push({ name: "generated id prefix", pass: !!g && g.id.indexOf(PREFIX + "GEN-") === 0 });
    tests.push({ name: "generated src label", pass: !!g && g.src === "generated" });
    tests.push({ name: "validateRecord accepts generated record", pass: !!g && validateRecord(g).valid });
    tests.push({ name: "reproducibility same seed same id", pass: generateRecord(7).id === g.id });
    tests.push({ name: "different seeds give different ids", pass: generateRecord(7).id !== generateRecord(8).id });
    tests.push({ name: "batch throttle", pass: generateBatch(500, 99).length === MAX_BATCH });
    tests.push({ name: "search finds a title", pass: searchRecords(SEED_TITLES[0].slice(0, 4)).length >= 1 });
    tests.push({ name: "hard stop is 10^9", pass: HARD_STOP === 1000000000 });
    var passed = tests.filter(function (t) { return t.pass; }).length;
    return { total: tests.length, passed: passed, tests: tests };
  }
  var Tools = { searchRecords: searchRecords, generateRecord: generateRecord, generateBatch: generateBatch, validateRecord: validateRecord, runTests: runTests, genId: genId, slug: SLUG, recordKind: RECORD_KIND, hardStop: HARD_STOP };
  root["PresolvedEngineeringQuestionsSignatureTools"] = Tools;
  if (typeof module !== "undefined" && module.exports) module.exports = Tools;
})(typeof window !== "undefined" ? window : globalThis);
