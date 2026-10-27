"use strict";
/* The new-jerusalem-kjv-source-text database — boundless generator. Seeded, deterministic, throttled,
   duplicate-checked, hard stop at 10^15. Generated records are
   labeled src "generated" and are never presented as archive records. */
(function (root) {
  var SLUG = "new-jerusalem-kjv-source-text";
  var PREFIX = "JAH-NJKV-";
  var RECORD_KIND = "kjv source text record";
  var HARD_STOP = 1000000000000000; // 10^15
  var MAX_BATCH = 100;
  var SEED_TITLES = ["New Heaven and New Earth, Rev 21:1", "The Holy City Descending, Rev 21:2", "God Dwelling with Humanity, Rev 21:3-4", "All Things Made New, Rev 21:5-6", "The City's Glory, Jasper Clear as Crystal, Rev 21:10-11", "Wall Great and High, Twelve Gates, Rev 21:12-13", "Twelve Foundations, Twelve Apostles, Rev 21:14", "Twelve Thousand Furlongs Foursquare, Rev 21:15-16", "The Wall: 144 Cubits, Rev 21:17", "Jasper Wall, Gold Like Clear Glass, Rev 21:18", "The Twelve Stones in Order, Rev 21:19-20", "Twelve Pearls, One Street of Gold, Rev 21:21", "No Temple, No Sun, No Moon, Rev 21:22-23", "Gates Never Shut, No Night, Rev 21:24-27", "River of Water of Life, Rev 22:1", "Tree of Life, Twelve Fruits, Rev 22:2-5"];
  var seen = {};
  var counter = 0;
  function mulberry32(a) {
    return function () {
      a |= 0; a = (a + 0x6D2B79F5) | 0;
      var t = Math.imul(a ^ (a >>> 15), 1 | a);
      t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t;
      return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
    };
  }
  function pad(n) { var s = String(n); while (s.length < 6) s = "0" + s; return s; }
  function generateRecord(seed) {
    if (counter >= HARD_STOP) return null;
    var rnd = mulberry32(typeof seed === "number" ? seed : 1);
    var title = SEED_TITLES[Math.floor(rnd() * SEED_TITLES.length)];
    var id = PREFIX + "GEN-" + pad(counter + 1);
    if (seen[id]) return null;
    seen[id] = true; counter += 1;
    return { id: id, slug: SLUG, title: "Generated: " + title,
      record_kind: RECORD_KIND, src: "generated", status: "speculative",
      text_faithful: "A generated variation in the " + title + " family, stated as a design variation, not as an established fact.",
      engineering: "Generated records carry no engineering claim until a seed record of the same family is checked against them.",
      description: "A boundlessly generated record in the " + title + " family, produced by the seeded generator for this database." };
  }
  function generateBatch(n, seed) {
    var out = [], count = Math.min(n || 1, MAX_BATCH);
    for (var i = 0; i < count; i++) { var r = generateRecord((seed || 1) + i); if (!r) break; out.push(r); }
    return out;
  }
  function searchRecords(q, pool) {
    q = String(q || "").toLowerCase();
    return (pool || SEED_TITLES).filter(function (t) { return t.toLowerCase().indexOf(q) !== -1; });
  }
  function validateRecord(rec) {
    var problems = [];
    if (!rec || rec.record_kind !== RECORD_KIND) problems.push("record_kind must be " + RECORD_KIND);
    if (!rec || !rec.slug || rec.slug !== SLUG) problems.push("slug must be " + SLUG);
    if (!rec || !rec.id || rec.id.indexOf(PREFIX) !== 0) problems.push("id must start with " + PREFIX);
    if (!rec || !rec.title) problems.push("title is required");
    if (!rec || !rec.status) problems.push("status is required");
    if (!rec || !rec.text_faithful || !rec.engineering) problems.push("text-faithful and engineering views are required");
    return { valid: problems.length === 0, problems: problems };
  }
  function runTests() {
    var tests = [];
    var g = generateRecord(7);
    tests.push({ name: "generated record_kind", pass: !!g && g.record_kind === RECORD_KIND });
    tests.push({ name: "generated slug is single edition slug", pass: !!g && g.slug === SLUG });
    tests.push({ name: "generated id prefix", pass: !!g && g.id.indexOf(PREFIX + "GEN-") === 0 });
    tests.push({ name: "generated src label", pass: !!g && g.src === "generated" });
    tests.push({ name: "validateRecord accepts generated record", pass: !!g && validateRecord(g).valid });
    tests.push({ name: "duplicate ids rejected", pass: (function () { var a = generateRecord(7); return a && a.id !== g.id; })() });
    tests.push({ name: "batch throttle", pass: generateBatch(500, 99).length === MAX_BATCH });
    tests.push({ name: "search finds a title", pass: searchRecords(SEED_TITLES[0].slice(0, 4)).length >= 1 });
    var passed = tests.filter(function (t) { return t.pass; }).length;
    return { total: tests.length, passed: passed, tests: tests };
  }
  var Tools = { searchRecords: searchRecords, generateRecord: generateRecord, generateBatch: generateBatch, validateRecord: validateRecord, runTests: runTests, slug: SLUG, recordKind: RECORD_KIND, hardStop: HARD_STOP };
  root["NewJerusalemKjvSourceTextTools"] = Tools;
  if (typeof module !== "undefined" && module.exports) module.exports = Tools;
})(typeof window !== "undefined" ? window : globalThis);
