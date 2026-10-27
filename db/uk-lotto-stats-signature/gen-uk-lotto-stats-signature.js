"use strict";
(function (root) {
  var SLUG = "uk-lotto-stats-signature";
  var PREFIX = "JAH-UKLOTSS-";
  var RECORD_KIND = "uk lotto statistics record";
  var HARD_STOP = 1000000000000000;
  var MAX_BATCH = 100;
  var TOPICS = ["UK Lotto Game Overview and Current Matrix", "UK Lotto Jackpot Odds by Exact Computation", "UK Lotto All Prize Tiers and Odds for One Round", "UK Lotto Draw Mechanics and Schedule", "UK Lotto Matrix History and the 2015 Change", "UK Lotto Record Jackpots", "UK Lotto Frequency Method on a Simulated Draw Set", "UK Lotto Hot Numbers Method", "UK Lotto Cold and Overdue Numbers Method", "UK Lotto Rollover Patterns and Rolldown Mechanics", "UK Lotto Expected Value in General Educational Terms", "UK Lotto HotPicks as a Related Game", "UK Thunderball as a Related Game", "UK Lotto Verification Guide Using Official Sources", "UK Lotto Fallacies Specific to This Game", "UK Lotto Compared with Irish Lotto"];
  function mulberry32(a) {
    return function () {
      a |= 0; a = (a + 0x6D2B79F5) | 0;
      var t = Math.imul(a ^ (a >>> 15), 1 | a);
      t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t;
      return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
    };
  }
  function searchRecords(q) {
    q = String(q || "").toLowerCase();
    if (!q) return TOPICS.slice();
    return TOPICS.filter(function (t) { return t.toLowerCase().indexOf(q) !== -1; });
  }
  var seen = {};
  function generateRecord(i) {
    var rnd = mulberry32(20261026 + i * 97);
    var topic = TOPICS[Math.floor(rnd() * TOPICS.length)];
    var variant = 1 + Math.floor(rnd() * 50);
    var key = topic + "#v" + variant;
    if (seen[key]) return null;
    seen[key] = true;
    return { id: PREFIX + "GEN-" + String(i + 1).padStart(6, "0"), slug: SLUG,
      title: "Generated " + topic + " variation v" + variant, edition: SLUG.indexOf("-signature") !== -1 ? "signature" : "public",
      src: "generated", generated: true, record_kind: RECORD_KIND,
      description: "Deterministic generated variation over the 16 seed records. Labeled generated; lottery outcomes are random and no generated record predicts a future draw.",
      demo: { code: "print('generated variation check')", expected_output: "generated variation check\n" } };
  }
  function generateBatch(n) {
    n = Math.min(Math.max(0, n | 0), MAX_BATCH);
    var out = [], attempts = 0;
    while (out.length < n && attempts < n * 20) { attempts++; var r = generateRecord(out.length + attempts); if (r) out.push(r); }
    return out;
  }
  function validateRecord(r) {
    return !!(r && r.id && r.id.indexOf(PREFIX) === 0 && r.slug === SLUG && r.record_kind === RECORD_KIND && r.src === "generated" && r.title);
  }
  function runTests() {
    var one = generateRecord(0);
    var checks = { slugCorrect: one.slug === SLUG, prefixCorrect: one.id.indexOf(PREFIX) === 0,
      kindCorrect: one.record_kind === RECORD_KIND, srcGenerated: one.src === "generated",
      singleSignature: SLUG.indexOf("-signature-signature") === -1,
      searchWorks: searchRecords(TOPICS[0].split(" ")[0]).length >= 1,
      validateWorks: validateRecord(one), hardStop: HARD_STOP === 1000000000000000 };
    var all = Object.keys(checks).every(function (k) { return checks[k]; });
    return { passed: all, checks: checks };
  }
  var Tools = { searchRecords: searchRecords, generateRecord: generateRecord, generateBatch: generateBatch,
    validateRecord: validateRecord, runTests: runTests, slug: SLUG, recordKind: RECORD_KIND, hardStop: HARD_STOP };
  root["UkLottoStatsTools"] = Tools;
  if (typeof module !== "undefined" && module.exports) module.exports = Tools;
  if (typeof require !== "undefined" && require.main === module) {
    var argv = process.argv.slice(2);
    var ni = argv.indexOf("--n");
    var n = ni >= 0 && argv[ni + 1] ? parseInt(argv[ni + 1], 10) : 1;
    if (n === 1) { console.log(JSON.stringify(generateRecord(0))); }
    else { generateBatch(n).forEach(function (r) { console.log(JSON.stringify(r)); }); }
  }
})(typeof window !== "undefined" ? window : globalThis);
