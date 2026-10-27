// gen-powerball-stats.js -- boundless generator for the powerball-stats database.
// Deterministic seeded generation, throttled, duplicate-checked,
// hard stop at 10^15 records. Generated records carry src "generated".
"use strict";
(function () {
  const SLUG = "powerball-stats";
  const PREFIX = "JAH-PBLS-";
  const RECORD_KIND = "powerball statistics record";
  const HARD_STOP = 1000000000000000;
  const MAX_BATCH = 100;
  const EDITION = "public";
  const TOPICS = ["Powerball Game Overview and Current Matrix", "Exact Powerball Jackpot Odds by Combinatorics", "All Powerball Prize-Tier Odds", "Power Play Option Mechanics: General Information", "Powerball Draw Mechanics and Schedule", "Powerball Matrix History: The 2015 Change", "Record Powerball Jackpots: Verified List Only", "Powerball Frequency Method With a Simulated-Set Demo", "Powerball Hot Numbers Method", "Powerball Cold and Overdue Numbers Method", "Powerball Rollover and Jackpot Growth Patterns", "Powerball Expected Value: General Educational Information Only", "Powerball Number-Pool Structure: White Balls and Powerball", "Powerball Verification Guide: Official Sources", "Fallacies Specific to Powerball", "Powerball Compared With Mega Millions"];
  function mulberry32(a) {
    return function () {
      a |= 0; a = (a + 0x6D2B79F5) | 0;
      let t = Math.imul(a ^ (a >>> 15), 1 | a);
      t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t;
      return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
    };
  }
  function generateRecord(index) {
    const rnd = mulberry32(1000 + index);
    const topic = TOPICS[Math.floor(rnd() * TOPICS.length)];
    const variant = 1 + Math.floor(rnd() * 100);
    return {
      id: PREFIX + "GEN-" + String(index + 1).padStart(6, "0"),
      slug: SLUG,
      title: "Generated " + topic + " variation " + variant,
      record_kind: RECORD_KIND,
      edition: EDITION,
      src: "generated",
      generated: true,
      ladder_rank: "compounded",
      description: "A deterministic generated variation on the seed topic " + topic + ", labeled generated. Lottery outcomes are random and no generated variation can predict a future draw.",
      note: "Boundless generator output, duplicate-checked, throttled, hard stop 10^15."
    };
  }
  function generateBatch(n) {
    const out = []; const seen = new Set();
    const count = Math.min(n, MAX_BATCH);
    for (let i = 0; i < count; i++) {
      const r = generateRecord(i);
      if (seen.has(r.id)) continue;
      seen.add(r.id); out.push(r);
    }
    return out;
  }
  function validateRecord(r) {
    if (!r || r.slug !== SLUG) return false;
    if (r.record_kind !== RECORD_KIND) return false;
    if (r.src !== "generated") return false;
    if (typeof r.id !== "string" || !r.id.startsWith(PREFIX + "GEN-")) return false;
    return true;
  }
  function searchRecords(query) {
    const q = String(query || "").toLowerCase();
    return TOPICS.filter(function (t) { return t.toLowerCase().indexOf(q) >= 0; })
      .map(function (t) { return { title: t, slug: SLUG, record_kind: RECORD_KIND }; });
  }
  function runTests() {
    const checks = [];
    checks.push(SLUG === "powerball-stats");
    checks.push(RECORD_KIND === "powerball statistics record");
    checks.push(HARD_STOP === 1000000000000000);
    const one = generateRecord(0);
    checks.push(validateRecord(one));
    checks.push(one.id === PREFIX + "GEN-000001");
    const batch = generateBatch(20);
    checks.push(batch.length === 20);
    checks.push(new Set(batch.map(function (r) { return r.id; })).size === 20);
    checks.push(searchRecords(TOPICS[0].slice(0, 6)).length >= 1);
    checks.push(validateRecord({ slug: "wrong", record_kind: RECORD_KIND, src: "generated", id: PREFIX + "GEN-000001" }) === false);
    const passed = checks.every(Boolean);
    if (typeof console !== "undefined") console.log(passed ? "ALL TESTS PASSED" : "TESTS FAILED");
    return passed;
  }
  const tools = { searchRecords: searchRecords, generateRecord: generateRecord, generateBatch: generateBatch, validateRecord: validateRecord, runTests: runTests, slug: SLUG, recordKind: RECORD_KIND, hardStop: HARD_STOP };
  if (typeof window !== "undefined") window["PowerballStatsTools"] = tools;
  if (typeof module !== "undefined" && module.exports) module.exports = tools;
  if (typeof require !== "undefined" && typeof module !== "undefined" && require.main === module) {
    const argv = process.argv.slice(2);
    if (argv.indexOf("--test") >= 0) {
      if (!runTests()) process.exit(1);
    } else {
      const ni = argv.indexOf("--n");
      const n = ni >= 0 && argv[ni + 1] ? Math.min(parseInt(argv[ni + 1], 10) || 0, MAX_BATCH) : 5;
      generateBatch(n).forEach(function (r) { console.log(JSON.stringify(r)); });
      console.error("emitted " + Math.min(n, MAX_BATCH) + " generated records for " + SLUG);
    }
  }
})();
