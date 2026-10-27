"use strict";
/* The US State Lotteries Statistics Signature Database — boundless generator. Seeded, deterministic, throttled,
   duplicate-checked, hard stop at 10^15. Generated records are
   labeled src "generated" and are never presented as archive records. */
(function (root) {
  var SLUG = "us-state-lotteries-stats-signature";
  var PREFIX = "JAH-USLOTS-";
  var RECORD_KIND = "us state lottery statistics record";
  var HARD_STOP = 1000000000000000; // 10^15
  var MAX_BATCH = 100;
  var SEED_TITLES = ["New York Lotto Statistics", "California SuperLotto Plus Statistics", "Florida Lotto Statistics", "Texas Lotto Statistics", "Cash4Life Statistics (Multi-State)", "Pennsylvania Match 6 Statistics", "New Jersey Pick-6 Statistics", "Ohio Classic Lotto Statistics", "Michigan Lotto 47 Statistics", "Illinois Lotto Statistics", "Georgia Fantasy 5 Statistics", "Lucky for Life Statistics (Multi-State Daily)", "State Games Versus Multi-State Games: Odds Comparison Method", "How State Draw Archives Work and How to Verify Them", "State Tax and Payout Variation: General Information", "Responsible Play and Common Fallacies"];
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
      record_kind: RECORD_KIND, src: "generated",
      description: "A boundlessly generated statistics study record in the " + title + " family, produced by the seeded generator for this database. Lottery outcomes are random; no generated record predicts any draw.",
      matrix: "Generated teaching matrix; see the archive record for the verified matrix.",
      jackpot_odds: null, data_note: "Generated record; not a verified game matrix." };
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
    if (!rec || rec.slug !== SLUG) problems.push("slug must be " + SLUG);
    if (!rec || !rec.id || rec.id.indexOf(PREFIX) !== 0) problems.push("id must start with " + PREFIX);
    if (!rec || !rec.title) problems.push("title is required");
    if (!rec || !rec.description) problems.push("description is required");
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
  root["UsStateLotteriesStatsTools"] = Tools;
  if (typeof module !== "undefined" && module.exports) module.exports = Tools;
  if (typeof module !== "undefined" && require.main === module) {
    var argv = process.argv.slice(2);
    var ni = argv.indexOf("--n");
    var n = ni >= 0 && argv[ni + 1] ? parseInt(argv[ni + 1], 10) : 1;
    if (n === 1) { console.log(JSON.stringify(generateRecord(1))); }
    else { console.log(JSON.stringify(generateBatch(n, 1))); }
  }
})(typeof window !== "undefined" ? window : globalThis);
