"use strict";
(function (root) {
  var SLUG = "canada-lotto-stats-signature";
  var PREFIX = "JAH-CANLOTS-";
  var RECORD_KIND = "canada lotto statistics record";
  var EDITION = "signature";
  var HARD_STOP = 1000000000000000;
  var MAX_BATCH = 100;
  var TOPICS = ["Canada Lotto 6/49 Overview and Matrix", "Canada Lotto 6/49 Prize Tiers and Odds", "Canada Lotto Max Overview and Current Matrix", "Canada Lotto Max Prize Tiers and MaxMillions Mechanics", "Canada Daily Grand as a Related Game", "Canada Encore as a Related Game", "Canada Draw Mechanics and Schedules", "Canada Lotto Matrix History", "Canada Record Jackpots", "Canada Lotto Frequency Method and Simulated Set Demo", "Canada Lotto Hot Numbers Method", "Canada Lotto Cold and Overdue Numbers Method", "Canada Lotto Rollover Patterns", "Canada Lotto Expected Value and Tax-Free Status, General Information Only", "Canada Lotto Verification Guide", "Canada Lotto 6/49 Versus Lotto Max Comparison and Responsible Play"];
  var seedState = 20261026;
  function mulberry32() {
    seedState = (seedState + 0x6D2B79F5) | 0;
    var t = seedState;
    t = Math.imul(t ^ (t >>> 15), t | 1);
    t ^= t + Math.imul(t ^ (t >>> 7), t | 61);
    return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
  }
  var seen = {};
  function generateRecord(index) {
    var topic = TOPICS[Math.floor(mulberry32() * TOPICS.length)];
    var variant = 1 + Math.floor(mulberry32() * 50);
    var key = topic + "#v" + variant;
    if (seen[key]) { return null; }
    seen[key] = true;
    var n = (typeof index === "number" ? index + 1 : 1);
    return {
      id: PREFIX + "GEN-" + String(n).padStart(6, "0"),
      slug: SLUG,
      title: "Generated " + topic + " parameter variation v" + variant,
      edition: EDITION,
      src: "generated",
      generated: true,
      record_kind: RECORD_KIND,
      note: "Deterministic parameter variation over the 16 seed records. Labeled generated; not an assistant-built record. Lottery outcomes are random and no generated record predicts a future draw."
    };
  }
  function generateBatch(n) {
    var out = [];
    var attempts = 0;
    var total = Math.min(n, MAX_BATCH);
    while (out.length < total && attempts < total * 50) {
      attempts++;
      var r = generateRecord(out.length);
      if (r) { out.push(r); }
    }
    return out;
  }
  function searchRecords(query) {
    var q = String(query || "").toLowerCase();
    return TOPICS.filter(function (t) { return t.toLowerCase().indexOf(q) !== -1; });
  }
  function validateRecord(r) {
    return !!r && r.slug === SLUG && r.record_kind === RECORD_KIND &&
      r.src === "generated" && String(r.id).indexOf(PREFIX + "GEN-") === 0;
  }
  function runTests() {
    var recs = generateBatch(3);
    if (recs.length !== 3) { throw new Error("batch length"); }
    recs.forEach(function (r) { if (!validateRecord(r)) { throw new Error("validate"); } });
    if (searchRecords("odds").length < 1) { throw new Error("search"); }
    if (HARD_STOP !== 1000000000000000) { throw new Error("hard stop"); }
    return true;
  }
  var api = { searchRecords: searchRecords, generateRecord: generateRecord, generateBatch: generateBatch, validateRecord: validateRecord, runTests: runTests, slug: SLUG, recordKind: RECORD_KIND, hardStop: HARD_STOP };
  root["CanadaLottoStatsTools"] = api;
  root[SLUG.split("-").map(function (w) { return w.charAt(0).toUpperCase() + w.slice(1); }).join("") + "Tools"] = api;
  if (typeof module !== "undefined" && module.exports) { module.exports = api; }
  if (typeof require !== "undefined" && require.main === module) {
    var args = process.argv.slice(2);
    if (args.indexOf("--test") !== -1) {
      runTests();
      console.log("runTests PASS");
    } else {
      var ni = args.indexOf("--n");
      var n = (ni !== -1 && args[ni + 1]) ? parseInt(args[ni + 1], 10) : 5;
      if (isNaN(n) || n < 0) { n = 5; }
      var batch = generateBatch(Math.min(n, MAX_BATCH));
      batch.forEach(function (r) { console.log(JSON.stringify(r)); });
    }
  }
})(typeof globalThis !== "undefined" ? globalThis : this);
