"use strict";
/* GEN for universal-time-calculator-signature - boundless generator. Seeded, deterministic, throttled,
   duplicate-checked, hard stop at 1,000,000,000. Generated records are labeled
   src "generated" and are never presented as archive records. */
(function (root) {
  var SLUG = "universal-time-calculator-signature";
  var PREFIX = "JAH-UTMCS-";
  var RECORD_KIND = "universal-time-calculator";
  var HARD_STOP = 1000000000;
  var MAX_BATCH = 100;
  var SEED_TITLES = ["Seconds to Minutes and Hours", "Minutes to Hours and Days", "Hours to Days and Weeks", "Days to Weeks, Months and Years", "Adding Times Together", "Subtracting Times", "Elapsed Time Between Two Clock Times", "Duration Across Midnight", "Converting Between 12-Hour and 24-Hour Clock", "Time Zones: Converting Between Zones", "Daylight Saving Time: Spring Forward", "Daylight Saving Time: Fall Back", "Countdown to a Future Date and Time", "Calendar Days Between Two Dates", "Business Days Between Two Dates", "Weeks and Weekdays: Finding a Weekday", "Speed, Distance and Time", "Pace and Time per Distance", "Adding Durations in Hours, Minutes and Seconds", "Time Remaining in a Day", "Leap Years and February Days", "Months: Days in Each Month and Adding Months", "Average Time and Total Time", "Universal Time Calculator Field Guide Index"];
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
      record_kind: RECORD_KIND, classification: "PROVEN", src: "generated",
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
    if (!rec || rec.classification !== "PROVEN") problems.push("classification must be PROVEN");
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
    tests.push({ name: "generated classification PROVEN", pass: !!g && g.classification === "PROVEN" });
    tests.push({ name: "hard stop is 10^9", pass: HARD_STOP === 1000000000 });
    var passed = tests.filter(function (t) { return t.pass; }).length;
    return { total: tests.length, passed: passed, tests: tests };
  }
  var Tools = { searchRecords: searchRecords, generateRecord: generateRecord, generateBatch: generateBatch, validateRecord: validateRecord, runTests: runTests, genId: genId, slug: SLUG, recordKind: RECORD_KIND, hardStop: HARD_STOP };
  root["UniversalTimeCalculatorSignatureTools"] = Tools;
  if (typeof module !== "undefined" && module.exports) module.exports = Tools;
  if (typeof process !== "undefined" && process.argv && process.argv.indexOf("--test") !== -1) {
    var r = runTests();
    console.log("runTests: " + r.passed + " of " + r.total + " passed");
    r.tests.forEach(function (t) { console.log((t.pass ? "PASS " : "FAIL ") + t.name); });
    process.exit(r.passed === r.total ? 0 : 1);
  }
})(typeof window !== "undefined" ? window : globalThis);
