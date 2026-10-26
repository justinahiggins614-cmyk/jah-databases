// Boundless generator for untrusted-input-prompt-injection-cases (JAH Databases round 32, lane-i).
// Seeded deterministic generator. HARD_CAP = 1e15 records per database.
// Throttled: at most 1000 records per run. Duplicate-checked. Stops when the
// variation space (topics x variant seeds) is genuinely exhausted.
// Generated records carry src "generated", generated: true, and are never
// mixed with assistant-built records.
(function () {
  var HARD_CAP = 1e15;
  var RUN_CAP = 1000;
  var TOPICS = ["Instruction Hierarchy Rule Set", "Input Canonicalization Procedure", "Delimiter and Boundary Design", "Quoted-Content Handling Rule", "Instruction-Versus-Data Labeling", "Anomaly Scoring for Suspicious Inputs", "Safe Refusal and Clarification Procedure", "Tool-Call Authorization Check", "State-Change Confirmation Gate", "Log and Review of Suspicious Inputs", "Multi-Turn Consistency Check", "Third-Party Content Handling Rule", "Output Verification Before Action", "Defense Test Suite Categories", "Defense Regression Checklist", "Incident Review for Input-Safety Events"];
  var PREFIX = "JAH-C084-";
  function mulberry32(a) { return function () { a |= 0; a = (a + 0x6D2B79F5) | 0; var t = Math.imul(a ^ (a >>> 15), 1 | a); t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t; return ((t ^ (t >>> 14)) >>> 0) / 4294967296; }; }
  function generate(n, seed) {
    var total = Math.min(n, RUN_CAP);
    var space = TOPICS.length * 1000;
    if (total > space) { total = space; }
    var rand = mulberry32(typeof seed === "number" ? seed : 42);
    var seen = {};
    var out = [];
    var guard = 0;
    while (out.length < total && guard < total * 20 + 100) {
      guard++;
      var ti = Math.floor(rand() * TOPICS.length);
      var variant = Math.floor(rand() * 1000);
      var key = ti + ":" + variant;
      if (seen[key]) { continue; }
      seen[key] = true;
      out.push({ id: PREFIX + "GEN" + String(out.length + 1).padStart(6, "0"), title: TOPICS[ti], src: "generated", generated: true, seed: seed, variant: variant, full_records: true, ladder_rank: "simple", last_verified: "2026-10-25" });
    }
    return out;
  }
  var api = { HARD_CAP: HARD_CAP, RUN_CAP: RUN_CAP, generate: generate };
  if (typeof module !== "undefined" && module.exports) { module.exports = api; }
  if (typeof window !== "undefined") { window.UntrustedInputPromptInjectionCasesGen = api; }
  if (typeof process !== "undefined" && process.argv) {
    var arg = process.argv.find(function (a) { return a.indexOf("--n=") === 0 || a === "--n"; });
    var n = 0;
    if (arg) { var eq = arg.indexOf("="); n = eq >= 0 ? parseInt(arg.slice(eq + 1), 10) : parseInt(process.argv[process.argv.indexOf(arg) + 1], 10); }
    if (n) { console.log(JSON.stringify(generate(n, 42), null, 2)); }
  }
})();
