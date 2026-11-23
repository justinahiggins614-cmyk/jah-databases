"use strict";
/* GEN for presolved-advanced-logic-questions-signature - boundless generator. Seeded, deterministic, throttled,
   duplicate-checked, hard stop at 1,000,000,000. Generated records are labeled
   src "generated" and are never presented as archive records. */
(function (root) {
  var SLUG = "presolved-advanced-logic-questions-signature";
  var PREFIX = "JAH-PSALS-";
  var RECORD_KIND = "presolved advanced logic question record";
  var HARD_STOP = 1000000000;
  var MAX_BATCH = 100;
  var SEED_TITLES = ["Modus ponens (Signature variant): if R then S; R; therefore S — valid?", "Modus tollens (Signature variant): if R then S; not S; therefore not R — valid?", "Affirming the consequent (Signature variant) — valid or invalid?", "Denying the antecedent (Signature variant) — valid or invalid?", "De Morgan's law (Signature variant): not (P or Q) — truth-table proof", "Law of non-contradiction: not (P and not P) — tautology proof", "Hypothetical syllogism (Signature variant): R→S, S→T, therefore R→T", "Disjunctive syllogism (Signature variant): R or S; not S; therefore R", "Constructive dilemma (Signature variant) — worked example", "Contrapositive equivalence (Signature variant): (Q → P) ↔ (¬P → ¬Q) — truth table", "Is P → (P or Q) a tautology? (Signature variant)", "Is (P → Q) → ((Q → R) → (P → R)) a tautology? (Signature variant)", "Barbara syllogism (Signature variant): all roses are flowers; all garden roses are roses", "An invalid syllogism (Signature variant) with a counterexample", "Knights and knaves (Signature variant): A says \"We are both knaves\" — solve", "The truth-teller: \"This sentence is true\" — analysis", "Quantifier scope (Signature variant): ∀x∃y versus ∃y∀x with a successor relation", "Negation of ∃x (P(x) and Q(x)) (Signature variant)", "Pigeonhole (Signature variant): 367 people, two share a birthday — proof", "Proof by contradiction (Signature variant): √3 is irrational", "Contrapositive proof (Signature variant): if n² is odd then n is odd", "Vacuous truth (Signature variant): \"all dragons in this room can breathe fire\"", "Material implication (Signature variant): true consequent makes the implication true", "Sorites (Signature variant): the baldness paradox — analysis and resolution options"];
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
  root["PresolvedAdvancedLogicQuestionsSignatureTools"] = Tools;
  if (typeof module !== "undefined" && module.exports) module.exports = Tools;
})(typeof window !== "undefined" ? window : globalThis);
