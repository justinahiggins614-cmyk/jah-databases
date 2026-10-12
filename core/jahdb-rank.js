/*! JAH Internal Ranking Engine — jahdb-rank-1.0
 * Property of Justin Addam Higgins (JAH).
 *
 * INTERNAL SYSTEM — ranks every simulation, program, and demo across the
 * JAH database network. Scores are computed deterministically from the
 * artifact itself: presence, syntax validity, runnable smoke test,
 * documentation, and determinism. Nothing is guessed; every point cites
 * the check that earned it.
 *
 * UMD: browsers (window.JAHDBRank) and Node (module.exports) for audit
 * harnesses and generator backfills.
 */
(function (root, factory) {
  'use strict';
  var R = factory();
  if (typeof module !== 'undefined' && module.exports) module.exports = R;
  root.JAHDBRank = R;
  try { if (root.JAHDB) root.JAHDB.rank = R; } catch (e) {}
})(typeof self !== 'undefined' ? self : this, function () {
'use strict';

var VERSION = 'jahdb-rank-1.0';

/* ---------------- small helpers ---------------- */
function isStr(v) { return typeof v === 'string'; }
function trunc(s, n) { s = String(s == null ? '' : s); return s.length > n ? s.slice(0, n) + '…' : s; }

var _vm = undefined;
function getVM() {
  if (_vm !== undefined) return _vm;
  _vm = null;
  try { if (typeof require === 'function') _vm = require('vm'); } catch (e) {}
  return _vm;
}

/* Syntax check: parses without executing. Node uses vm.Script, browsers use
   the Function constructor (parse-only, never invoked). */
function syntaxValid(program, language) {
  if (!isStr(program) || !program.trim()) return { ok: false, reason: 'empty' };
  if ((language || 'javascript') !== 'javascript') {
    /* Non-JS: credit presence + basic sanity (non-trivial length, no NUL). */
    return program.length >= 20
      ? { ok: true, reason: 'non-js presence' }
      : { ok: false, reason: 'too short' };
  }
  var vm = getVM();
  if (vm) {
    try { new vm.Script(program, { timeout: 500 }); return { ok: true, reason: 'parsed' }; }
    catch (e) { return { ok: false, reason: 'syntax: ' + trunc(e.message, 90) }; }
  }
  try { new Function('"use strict";\n' + program); return { ok: true, reason: 'parsed' }; }
  catch (e) { return { ok: false, reason: 'syntax: ' + trunc(e.message, 90) }; }
}

/* Smoke test: actually runs the JS in a sandbox (Node vm only). Browsers
   report not-tested rather than guessing. */
function smokeValid(program) {
  var vm = getVM();
  if (!vm) return { ok: null, reason: 'not tested in browser' };
  if (!isStr(program) || !program.trim()) return { ok: false, reason: 'empty' };
  try {
    var n = 0;
    var sandbox = {
      console: {
        log: function () { if (++n > 800) throw new Error('output cap'); },
        warn: function () {}, error: function () {}, info: function () {}
      }
    };
    vm.runInNewContext('"use strict";\n' + program, sandbox, { timeout: 1500 });
    return { ok: true, reason: 'ran clean (' + n + ' logs)' };
  } catch (e) { return { ok: false, reason: 'threw: ' + trunc(e.message, 90) }; }
}

var UNSAFE_HARD = [/while\s*\(\s*true\s*\)/, /for\s*\(\s*;\s*;\s*\)/, /process\.exit/];
var UNSAFE_SOFT = [/require\s*\(/];
function safetyCheck(program) {
  if (!isStr(program)) return { ok: false, reason: 'not a program' };
  for (var i = 0; i < UNSAFE_HARD.length; i++)
    if (UNSAFE_HARD[i].test(program)) return { ok: false, hard: true, reason: 'unbounded loop or process exit' };
  for (var j = 0; j < UNSAFE_SOFT.length; j++)
    if (UNSAFE_SOFT[j].test(program)) return { ok: true, soft: true, reason: 'uses require() — fine on PC/Node, not in browser sandbox' };
  return { ok: true, reason: 'safe patterns' };
}

/* Determinism: unseeded randomness / wall-clock use costs points. */
function determinismCheck(program) {
  if (!isStr(program)) return { ok: true, reason: 'n/a', score: 10 };
  var bad = [];
  if (/\bMath\.random\s*\(/.test(program)) bad.push('Math.random');
  if (/\bDate\.now\s*\(/.test(program)) bad.push('Date.now');
  if (/\bnew\s+Date\s*\(/.test(program)) bad.push('new Date()');
  return bad.length
    ? { ok: false, reason: 'unseeded: ' + bad.join(', '), score: 0 }
    : { ok: true, reason: 'deterministic', score: 10 };
}

/* ---------------- demo scoring (0–100) ---------------- */
function scoreDemo(demo) {
  var checks = [], score = 0;
  demo = demo || {};
  var prog = demo.program, lang = demo.language || 'javascript';

  /* 1. Presence — 20 */
  if (isStr(prog) && prog.trim().length >= 20) { score += 20; checks.push(['presence', 20, 'program present (' + prog.length + ' chars)']); }
  else { checks.push(['presence', 0, 'missing or trivial program']); return { score: score, checks: checks, tier: tier(score) }; }

  /* 2. Syntax — 25 */
  var syn = syntaxValid(prog, lang);
  if (syn.ok) { score += 25; checks.push(['syntax', 25, syn.reason]); }
  else { checks.push(['syntax', 0, syn.reason]); }

  /* 3. Smoke (runnable) — 30. Browser: half credit on clean syntax. */
  var sm = smokeValid(prog);
  if (sm.ok === true) { score += 30; checks.push(['runnable', 30, sm.reason]); }
  else if (sm.ok === null) {
    if (syn.ok) { score += 15; checks.push(['runnable', 15, 'browser: syntax clean, run in Node/PC to verify']); }
    else checks.push(['runnable', 0, 'browser: cannot verify, syntax failed']);
  } else checks.push(['runnable', 0, sm.reason]);

  /* 4. Documentation — 10 */
  var docPts = 0, docWhy = [];
  if (demo.title) { docPts += 4; docWhy.push('title'); }
  if (demo.run_hint || demo.how_to_run) { docPts += 4; docWhy.push('run hint'); }
  if (demo.note) { docPts += 2; docWhy.push('note'); }
  score += docPts; checks.push(['documented', docPts, docWhy.join(', ') || 'undocumented']);

  /* 5. Determinism — 10 */
  var det = determinismCheck(prog);
  score += det.score; checks.push(['deterministic', det.score, det.reason]);

  /* 6. Language labeled — 5 */
  if (demo.language) { score += 5; checks.push(['language', 5, demo.language]); }
  else checks.push(['language', 0, 'unlabeled']);

  /* Safety is a gate, not points: hard-unsafe caps at 39. Soft (require) only notes. */
  var safe = safetyCheck(prog);
  if (!safe.ok && safe.hard && lang === 'javascript') {
    checks.push(['safety', 0, 'GATE: ' + safe.reason + ' — capped at 39']);
    score = Math.min(score, 39);
  } else checks.push(['safety', 0, safe.reason + (safe.hard ? ' (gate pass)' : safe.soft ? ' (soft note)' : ' (gate pass)')]);

  return { score: Math.min(100, score), checks: checks, tier: tier(score) };
}

function tier(score) {
  if (score >= 90) return 'S';
  if (score >= 75) return 'A';
  if (score >= 60) return 'B';
  if (score >= 40) return 'C';
  return 'D';
}

/* ---------------- record scoring ---------------- */
function scoreRecord(rec) {
  rec = rec || {};
  var out = { id: String(rec.id || rec.api_id || 'rec'), has_demo: false, demo_score: 0, tier: 'D', checks: [] };
  var demo = rec.demo;
  if (demo && isStr(demo.program)) {
    out.has_demo = true;
    var s = scoreDemo(demo);
    out.demo_score = s.score; out.tier = s.tier; out.checks = s.checks;
    out.demo_kind = demo.kind || 'demo'; out.demo_lang = demo.language || 'javascript';
  } else {
    /* No demo: score on record completeness (fields filled vs empty). */
    var keys = Object.keys(rec).filter(function (k) { return k.charAt(0) !== '_' && k !== 'demo'; });
    var filled = keys.filter(function (k) {
      var v = rec[k];
      return v !== null && v !== undefined && v !== '' && !(Array.isArray(v) && !v.length);
    }).length;
    var pct = keys.length ? Math.round(100 * filled / keys.length) : 0;
    out.demo_score = Math.round(pct * 0.5); /* completeness caps at 50 without a demo */
    out.tier = tier(out.demo_score);
    out.checks = [['completeness', out.demo_score, filled + '/' + keys.length + ' fields filled (no demo: capped at 50)']];
  }
  return out;
}

/* ---------------- database aggregate ---------------- */
function aggregateDatabase(slug, name, recordScores, totalRecords) {
  var n = recordScores.length;
  var sum = 0, withDemo = 0, tiers = { S: 0, A: 0, B: 0, C: 0, D: 0 };
  recordScores.forEach(function (r) {
    sum += r.demo_score;
    if (r.has_demo) withDemo++;
    tiers[r.tier] = (tiers[r.tier] || 0) + 1;
  });
  var mean = n ? sum / n : 0;
  var coverage = n ? withDemo / n : 0;
  /* Aggregate: 70% mean quality + 30% demo coverage, scaled 0–100. */
  var score = Math.round(0.7 * mean + 0.3 * coverage * 100);
  return {
    slug: slug, name: name,
    sampled: n, total_records: totalRecords || n,
    mean_demo_score: Math.round(mean * 10) / 10,
    demo_coverage: Math.round(coverage * 1000) / 10,
    score: score, tier: tier(score), tiers: tiers,
    ranked_at: new Date().toISOString().slice(0, 10)
  };
}

return {
  version: VERSION,
  scoreDemo: scoreDemo,
  scoreRecord: scoreRecord,
  aggregateDatabase: aggregateDatabase,
  tier: tier,
  syntaxValid: syntaxValid,
  smokeValid: smokeValid,
  safetyCheck: safetyCheck
};
});
