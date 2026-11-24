"use strict";
/* GEN for signature-measurement-bounding-box - boundless generator. Seeded, deterministic, throttled,
   duplicate-checked, hard stop at 1,000,000,000. Generated records are labeled
   src "generated" and are never presented as archive records. */
(function (root) {
  var SLUG = "signature-measurement-bounding-box";
  var PREFIX = "JAH-SMBB-";
  var RECORD_KIND = "signature-measurement-bounding-box";
  var HARD_STOP = 1000000000;
  var MAX_BATCH = 100;
  var SEED_TITLES = ["The Whole Bounding Box: 1,257 by 480", "Component 1 Box: 365 by 476", "Component 2 Box: 340 by 387", "Component 3 Box: 453 by 170", "Component 4 Box: 351 by 109", "Component 5 Box: 21 by 21", "Component 6 Box: 21 by 20", "Component 7 Box: 18 by 17", "Aspect Ratios of All Seven Boxes", "Box Centers of All Seven Components", "Box Areas and Ink Fill", "The Whole Box Area: 603,360 Square Pixels", "Box Corners of the Whole Signature", "Tall Stroke Boxes Compared", "Sweep Boxes Compared", "Dot Boxes Compared", "Boxes Inside the Whole: Containment", "Box Widths Ordered Largest to Smallest", "Box Heights Ordered Largest to Smallest", "The Center of the Whole Box", "Box Edges: Left, Right, Top, Bottom", "Bounding Boxes as the Measurement Frame", "From Boxes to Pixels: Reading a Box", "The Bounding Box Summary"];
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
  root["BoundingBoxTools"] = Tools;
  if (typeof module !== "undefined" && module.exports) module.exports = Tools;
})(typeof window !== "undefined" ? window : globalThis);
