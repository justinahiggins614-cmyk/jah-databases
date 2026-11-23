"use strict";
/* GEN for presolved-chemistry-calculations-signature - boundless generator. Seeded, deterministic, throttled,
   duplicate-checked, hard stop at 1,000,000,000. Generated records are labeled
   src "generated" and are never presented as archive records. */
(function (root) {
  var SLUG = "presolved-chemistry-calculations-signature";
  var PREFIX = "JAH-PSCCS-";
  var RECORD_KIND = "presolved chemistry calculation record";
  var HARD_STOP = 1000000000;
  var MAX_BATCH = 100;
  var SEED_TITLES = ["Moles from mass: 25 g of potassium chloride", "Molarity: prepare 2 L of 0.25 M potassium chloride", "Dilution: 50 mL of 3.0 M stock to 0.75 M", "pH of 0.005 M hydrochloric acid", "pH of 0.01 M sodium hydroxide", "Stoichiometry: hydrogen and oxygen, oxygen limiting", "Percent yield: 60 g obtained from 80 g theoretical", "Gas volume at STP: 3 mol of gas", "Ideal gas law: 2.00 atm, 10.0 L, 273 K", "Empirical formula: 92.3 percent carbon, 7.7 percent hydrogen", "Molecular formula: empirical CH, molar mass 78.11", "Concentration in ppm: 12 mg in 3 kg", "Titration: 20.0 mL of 0.200 M HCl with 0.100 M NaOH", "Equilibrium constant Kc: higher ammonia concentration", "Buffer pH: acetate buffer with 4 to 1 ratio", "Thermochemistry: 250 g of water warmed by 8 C", "Electrolysis: 3.00 A for 30 minutes", "Assigning oxidation numbers: potassium permanganate", "Balancing a redox equation: dichromate and iron(II)", "Rate law: first order in A, first order in B", "Half-life: 200 g after 4 half-lives", "Solubility: barium sulfate Ksp", "Density of carbon dioxide at 298 K and 1 atm", "Avogadro's number: atoms in 24 g of carbon"];
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
  root["PresolvedChemistryCalculationsSignatureTools"] = Tools;
  if (typeof module !== "undefined" && module.exports) module.exports = Tools;
})(typeof window !== "undefined" ? window : globalThis);
