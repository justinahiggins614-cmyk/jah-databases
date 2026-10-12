/*! JAH Boundless Alternatives Engine — jahdb-alt-1.0
 * Property of Justin Addam Higgins (JAH).
 *
 * Every file scales boundlessly: A1 is the file as made; A2, A3, A4… are
 * generated alternatives that swap out components or restrict the design to
 * find workarounds — until one works or fits the user's need.
 *
 * Strategies (deterministic, seeded by record id + alternative number):
 *   swap       — same record, different demo kind (swapped design)
 *   restrict   — minimal restricted version (core only, nothing extra)
 *   workaround — defensive version (validates, catches, falls back)
 *
 * UMD: browsers (window.JAHDBAlt) and Node (module.exports).
 */
(function (root, factory) {
  'use strict';
  var A = factory();
  if (typeof module !== 'undefined' && module.exports) module.exports = A;
  root.JAHDBAlt = A;
  try { if (root.JAHDB) root.JAHDB.alt = A; } catch (e) {}
})(typeof self !== 'undefined' ? self : this, function () {
'use strict';

var VERSION = 'jahdb-alt-1.0';
var STRATEGIES = ['swap', 'restrict', 'workaround'];
var KIND_CYCLE = ['explore', 'simulate', 'chart', 'read', 'code'];

function hashStr(s) {
  var h = 2166136261; s = String(s);
  for (var i = 0; i < s.length; i++) { h ^= s.charCodeAt(i); h = Math.imul(h, 16777619); }
  return h >>> 0;
}
function prng(seed) {
  var a = (seed >>> 0) || 1;
  return function () {
    a |= 0; a = (a + 0x6D2B79F5) | 0;
    var t = Math.imul(a ^ (a >>> 15), 1 | a);
    t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t;
    return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
  };
}
function escJ(s) { return JSON.stringify(String(s == null ? '' : s)); }
function idOf(rec) { return String(rec.id || rec.api_id || rec.record_id || 'rec'); }
function titleOf(rec) {
  return rec.title || rec.name || rec.signature_name || rec.label || rec.display_name || idOf(rec);
}
function demoOf(rec) { return (rec && rec.demo && rec.demo.program) ? rec.demo : null; }

/* Pick a demo kind different from the original (deterministic). */
function swapKind(origKind, rnd) {
  var pool = KIND_CYCLE.filter(function (k) { return k !== origKind; });
  return pool[Math.floor(rnd() * pool.length)];
}

/* ---------------- strategy: swap ----------------
   Same record, rebuilt as a different demo kind — the design is swapped out. */
function buildSwap(slug, rec, rnd) {
  var orig = demoOf(rec) || {};
  var origKind = orig.kind || 'explore';
  var kind = swapKind(origKind, rnd);
  var D = (typeof window !== 'undefined' ? window.JAHDB : null);
  var demo = null;
  try {
    if (D && D.demo && D.demo.buildKind) demo = D.demo.buildKind(slug, rec, kind);
  } catch (e) { demo = null; }
  if (!demo || !demo.program) {
    /* Fallback: kind-swapped hand-built demo from record fields. */
    demo = handBuiltKind(rec, kind);
  }
  demo.kind = kind;
  demo.title = 'Alternative (' + kind + ' design) — ' + titleOf(rec);
  return demo;
}

/* Hand-built kind demos when the engine's buildKind is unavailable. */
function handBuiltKind(rec, kind) {
  var t = titleOf(rec), id = idOf(rec);
  var fields = Object.keys(rec).filter(function (k) { return k.charAt(0) !== '_' && k !== 'demo'; }).slice(0, 8);
  var fjson = escJ(fields);
  var prog;
  if (kind === 'simulate') {
    prog = '/* Alternative A: step simulation (swapped design) — ' + id + ' */\n' +
      '(function(){\nvar FIELDS=' + fjson + ';\nvar RECORD=' + escJ(JSON.stringify(rec, function (k, v) { return k === 'demo' ? undefined : v; }).slice(0, 3000)) + ';\n' +
      'console.log("SIMULATION — ' + id.replace(/"/g, '') + '");\n' +
      'FIELDS.forEach(function(f,i){ console.log(" step "+(i+1)+": field ["+f+"] = "+JSON.stringify(RECORD[f]).slice(0,120)); });\n' +
      'console.log("done: "+FIELDS.length+" steps simulated.");\n})();';
  } else if (kind === 'chart') {
    prog = '/* Alternative A: data chart (swapped design) — ' + id + ' */\n' +
      '(function(){\nvar NUMS={};\nObject.keys(' + escJ(JSON.stringify(rec, function (k, v) { return k === 'demo' ? undefined : v; }).slice(0, 3000)) + '.constructor === Object ? {} : {});\n' +
      'var R=' + escJ(JSON.stringify(rec, function (k, v) { return k === 'demo' ? undefined : v; }).slice(0, 3000)) + ';\n' +
      'var rec=JSON.parse(R);\nObject.keys(rec).forEach(function(k){ if(typeof rec[k]==="number" && isFinite(rec[k])) NUMS[k]=rec[k]; });\n' +
      'var keys=Object.keys(NUMS);\nconsole.log("CHART — ' + id.replace(/"/g, '') + ' ("+keys.length+" numeric fields)");\n' +
      'keys.forEach(function(k){ var v=NUMS[k], bar=""; var n=Math.min(40,Math.round(Math.abs(v)%41)); for(var i=0;i<n;i++) bar+="#"; console.log(" "+k+": "+bar+" "+v); });\n' +
      'if(!keys.length) console.log(" (no numeric fields — chart shows record shape: "+Object.keys(rec).length+" fields)");\n})();';
  } else if (kind === 'read') {
    prog = '/* Alternative A: guided reading (swapped design) — ' + id + ' */\n' +
      '(function(){\nvar R=JSON.parse(' + escJ(JSON.stringify(rec, function (k, v) { return k === 'demo' ? undefined : v; }).slice(0, 4000)) + ');\n' +
      'console.log("GUIDED READ — "+' + escJ(t) + ');\n' +
      'Object.keys(R).forEach(function(k){ var v=R[k]; var s=typeof v==="string"?v:String(JSON.stringify(v)); console.log("\\n["+k+"]\\n"+s.slice(0,300)); });\n})();';
  } else if (kind === 'code') {
    prog = '/* Alternative A: runnable code (swapped design) — ' + id + ' */\n' +
      '(function(){\nvar R=JSON.parse(' + escJ(JSON.stringify(rec, function (k, v) { return k === 'demo' ? undefined : v; }).slice(0, 4000)) + ');\n' +
      'function describe(r){ return Object.keys(r).map(function(k){ return k+": "+String(JSON.stringify(r[k])).slice(0,80); }); }\n' +
      'describe(R).forEach(function(line){ console.log(line); });\nconsole.log("OK — record described programmatically.");\n})();';
  } else { /* explore */
    prog = '/* Alternative A: record tour (swapped design) — ' + id + ' */\n' +
      '(function(){\nvar R=JSON.parse(' + escJ(JSON.stringify(rec, function (k, v) { return k === 'demo' ? undefined : v; }).slice(0, 4000)) + ');\n' +
      'var keys=Object.keys(R);\nconsole.log("TOUR — "+' + escJ(t) + '+" ("+keys.length+" fields)");\n' +
      'keys.forEach(function(k,i){ console.log(" "+(i+1)+". "+k); });\n})();';
  }
  return { kind: kind, title: 'Alternative (' + kind + ') — ' + t, language: 'javascript', program: prog };
}

/* ---------------- strategy: restrict ----------------
   Minimal version: core fields only, smallest runnable program. */
function buildRestrict(slug, rec) {
  var t = titleOf(rec), id = idOf(rec);
  var core = {};
  ['title', 'name', 'label', 'display_name', 'id'].forEach(function (k) { if (rec[k] !== undefined) core[k] = rec[k]; });
  /* Plus the single most informative other field (longest string). */
  var best = '', bestK = '';
  Object.keys(rec).forEach(function (k) {
    if (k.charAt(0) === '_' || k === 'demo' || core[k] !== undefined) return;
    var v = rec[k];
    var s = typeof v === 'string' ? v : '';
    if (s.length > best.length && s.length <= 500) { best = s; bestK = k; }
  });
  if (bestK) core[bestK] = best;
  var prog = '/* Alternative (restricted — core only) — ' + id + ' */\n' +
    '(function(){\nvar CORE=' + escJ(JSON.stringify(core)) + ';\n' +
    'var c=JSON.parse(CORE);\nconsole.log(' + escJ(t) + ');\n' +
    'Object.keys(c).forEach(function(k){ console.log(" "+k+": "+String(c[k]).slice(0,160)); });\n})();';
  return {
    kind: 'minimal', title: 'Alternative (restricted) — ' + t,
    language: 'javascript', program: prog,
    note: 'Restricted design: core fields only. Nothing extra.'
  };
}

/* ---------------- strategy: workaround ----------------
   Defensive version: validates, catches, falls back — finds a way to work. */
function buildWorkaround(slug, rec) {
  var t = titleOf(rec), id = idOf(rec);
  var orig = demoOf(rec);
  var origProg = orig ? String(orig.program) : '';
  /* Take the original program body and wrap it defensively. If the original
     is missing, the workaround still produces a working fallback. */
  var inner = origProg
    .replace(/^\/\*[\s\S]*?\*\//, '')   /* strip leading banner comment */
    .trim() || 'console.log("record present");';
  /* Indent inner for the wrapper. */
  inner = inner.split('\n').map(function (l) { return '    ' + l; }).join('\n');
  var prog = '/* Alternative (workaround — defensive) — ' + id + ' */\n' +
    '(function(){\n' +
    'var RECORD_ID=' + escJ(id) + ';\n' +
    'var RECORD_TITLE=' + escJ(t) + ';\n' +
    'function fallback(reason){\n' +
    '  console.log("[workaround] primary path failed ("+reason+") — fallback:");\n' +
    '  console.log(" "+RECORD_TITLE+" ["+RECORD_ID+"]");\n' +
    '  console.log("[workaround] record acknowledged without primary demo.");\n' +
    '}\n' +
    'try{\n' +
    '  if(!RECORD_ID || !RECORD_TITLE) throw new Error("missing identity");\n' +
    inner + '\n' +
    '  console.log("[workaround] primary path OK.");\n' +
    '}catch(e){ fallback(e.message); }\n' +
    '})();';
  return {
    kind: 'workaround', title: 'Alternative (workaround) — ' + t,
    language: 'javascript', program: prog,
    note: 'Workaround design: validates inputs, catches failures, always produces output.'
  };
}

/* ---------------- main entry ----------------
   n = 1 → the file as made (A1). n >= 2 → generated alternative. */
function alternative(slug, rec, n) {
  n = Math.max(1, Math.floor(n) || 1);
  var id = idOf(rec);
  if (n === 1) {
    var orig = demoOf(rec);
    return {
      alt_id: 'A1', strategy: 'original',
      title: (orig && orig.title) || ('Original — ' + titleOf(rec)),
      kind: (orig && orig.kind) || 'demo',
      language: (orig && orig.language) || 'javascript',
      program: (orig && orig.program) || 'console.log(' + escJ('Record ' + id) + ');',
      note: 'The file as made — no alternative applied.'
    };
  }
  var seed = hashStr(id + ':alt:' + n);
  var rnd = prng(seed);
  var strat = STRATEGIES[(n - 2) % STRATEGIES.length];
  var round = Math.floor((n - 2) / STRATEGIES.length); /* A5+ vary further */
  var demo;
  if (strat === 'swap') demo = buildSwap(slug, rec, prng(seed + round * 7919));
  else if (strat === 'restrict') demo = buildRestrict(slug, rec);
  else demo = buildWorkaround(slug, rec);
  if (round > 0) demo.title += ' (v' + (round + 1) + ')';
  return {
    alt_id: 'A' + n, strategy: strat,
    title: demo.title, kind: demo.kind,
    language: demo.language || 'javascript', program: demo.program,
    note: demo.note || strategyNote(strat)
  };
}

function strategyNote(s) {
  if (s === 'swap') return 'Swapped design: same record, different demo kind.';
  if (s === 'restrict') return 'Restricted design: minimal core only.';
  return 'Workaround design: defensive, always produces output.';
}

/* Rank an alternative with the ranking engine when available. */
function rankAlternative(alt) {
  try {
    var R = (typeof window !== 'undefined' ? window.JAHDBRank : null) ||
            (typeof JAHDBRank !== 'undefined' ? JAHDBRank : null);
    if (R && R.scoreDemo) return R.scoreDemo({ program: alt.program, language: alt.language, title: alt.title });
  } catch (e) {}
  return { score: 50, tier: 'C', checks: [['unranked', 50, 'ranking engine unavailable']] };
}

/* Scale: generate alternatives A2..An until one scores >= target or n hits max. */
function scaleToFit(slug, rec, opts) {
  opts = opts || {};
  var target = opts.targetScore || 75, maxN = opts.max || 10;
  var out = [Object.assign(alternative(slug, rec, 1), { rank: rankAlternative(alternative(slug, rec, 1)) })];
  for (var n = 2; n <= maxN; n++) {
    var a = alternative(slug, rec, n);
    a.rank = rankAlternative(a);
    out.push(a);
    if (a.rank.score >= target) break;
  }
  return out;
}

return {
  version: VERSION,
  strategies: STRATEGIES,
  alternative: alternative,
  rankAlternative: rankAlternative,
  scaleToFit: scaleToFit
};
});
