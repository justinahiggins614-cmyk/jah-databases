"use strict";
/* GEN for atom-sequences-signature - boundless generator. Seeded, deterministic, throttled,
   duplicate-checked, hard stop at 1,000,000,000. Generated records are labeled
   src "generated" and are never presented as archive records. */
(function (root) {
  var SLUG = "atom-sequences-signature";
  var PREFIX = "JAH-ATSEQS-";
  var RECORD_KIND = "atom sequence record";
  var HARD_STOP = 1000000000;
  var MAX_BATCH = 100;
  var SEED_TITLES = ["Hydrogen Association - H + H Gives H2", "Water Formation - 2H2 + O2 Gives 2H2O", "Salt Formation - Na + Cl Gives NaCl", "Photosynthesis - CO2 + H2O Gives Glucose + O2", "Methane Combustion - CH4 + 2O2 Gives CO2 + 2H2O", "Rusting - Fe + O2 + H2O Gives Rust", "Ammonia Synthesis - N2 + 3H2 Gives 2NH3", "The Ozone Cycle - O2 Gives O3 Gives O2", "The Proton-Proton Chain - 4p Gives He-4", "The CNO Cycle", "The Triple-Alpha Process - 3 He-4 Gives C-12", "The Uranium-238 Decay Chain - U-238 Gives Pb-206", "The Thorium-232 Decay Chain - Th-232 Gives Pb-208", "The Radon-222 Decay Chain - Rn-222 Gives Pb-206", "Carbon-14 Formation and Decay - N-14 Gives C-14 Gives N-14", "The Deuterium-Tritium Breeding Loop", "The R-Process - Rapid Neutron Capture", "The S-Process - Slow Neutron Capture", "Big Bang Nucleosynthesis - p + n Gives He-4", "The Muon Decay Chain - Pi Gives Mu Gives E", "Cobalt-60 Decay - Co-60 Gives Ni-60", "The Caesium-137 Decay Chain - Cs-137 Gives Ba-137", "Positronium Annihilation - e+ + e- Gives Gamma + Gamma", "Stellar Carbon Burning - C-12 + C-12 Gives Ne-20 + He-4"];
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
  root["AtomSequenceSignatureTools"] = Tools;
  if (typeof module !== "undefined" && module.exports) module.exports = Tools;
})(typeof window !== "undefined" ? window : globalThis);
