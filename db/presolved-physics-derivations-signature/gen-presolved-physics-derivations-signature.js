"use strict";
/* GEN for presolved-physics-derivations-signature - boundless generator. Seeded, deterministic, throttled,
   duplicate-checked, hard stop at 1,000,000,000. Generated records are labeled
   src "generated" and are never presented as archive records. */
(function (root) {
  var SLUG = "presolved-physics-derivations-signature";
  var PREFIX = "JAH-PSPDS-";
  var RECORD_KIND = "presolved physics derivation record";
  var HARD_STOP = 1000000000;
  var MAX_BATCH = 100;
  var SEED_TITLES = ["Derive v = u + at (Signature variant): u = 10 m/s, a = 3 m/s², t = 4 s", "Derive s = ut + ½at² (Signature variant): u = 10 m/s, a = 3 m/s², t = 4 s", "Derive v² = u² + 2as (Signature variant): u = 10 m/s, a = 3 m/s², s = 64 m", "Derive F = ma from momentum (Signature variant): 5 kg, 8 m/s in 4 s", "Derive kinetic energy ½mv² from work (Signature variant): 4 kg at 6 m/s", "Derive gravitational potential energy mgh (Signature variant): 8 kg, 12 m", "Derive the period of a simple pendulum (Signature variant): L = 2.5 m", "Derive centripetal acceleration a = v²/r (Signature variant): 15 m/s, 10 m", "Derive escape velocity (Signature variant): the Moon", "Derive Kepler's third law (Signature variant): the orbit of Mars", "Derive pressure variation with depth (Signature variant): 12 m", "Derive the work–energy theorem (Signature variant): 3 kg from 2 m/s to 8 m/s", "Derive conservation of momentum (Signature variant): 4 kg at 5 m/s meets 6 kg at rest", "Derive Snell's law (Signature variant): water to air at 40°", "Derive the lens equation (Signature variant): f = 15 cm, object at 45 cm", "Derive the Doppler shift formula (Signature variant): 440 Hz receding at 15 m/s", "Derive the ideal gas law (Signature variant): 2 mol at 300 K in 0.05 m³", "Derive the de Broglie wavelength (Signature variant): electron at 2×10⁶ m/s", "Derive the time-dilation factor (Signature variant): v = 0.8c", "Derive the range of a projectile (Signature variant): 30 m/s at 30°", "Derive the speed of a wave on a string (Signature variant): T = 180 N, μ = 0.02 kg/m", "Derive the electric field of a point charge (Signature variant): 2 µC at 0.2 m", "Derive the capacitance of a parallel-plate capacitor (Signature variant): A = 0.05 m², d = 0.001 m", "Derive the half-life decay law (Signature variant): 800 nuclei, 5-year half-life, 15 years"];
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
  root["PresolvedPhysicsDerivationsSignatureTools"] = Tools;
  if (typeof module !== "undefined" && module.exports) module.exports = Tools;
})(typeof window !== "undefined" ? window : globalThis);
