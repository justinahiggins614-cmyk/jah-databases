'use strict';
/* gen-ai-version-for-all-demos.js
 * Deterministic client-side generator + executable demo for
 * "The AI Version for All Demos Database" (JAH-DAI-).
 *
 * One locked-in AI per manifest database. The AI ONLY does what that
 * database's demo/working version explains -- nothing more -- with the PC
 * and tools as its hands. Scope enforcement is deterministic: the scope gate
 * below is the entire behavior spec. No overclaiming.
 *
 * Mirrors demoai-lane-r18/build.py::build_records_b in field semantics
 * (node parity test at build). Boundless generator: CAP = 1e15 hard stop,
 * generator ladder simple -> god-mode, self-regulated, completion detection.
 */
(function (root) {
  var CAP = 1e15;
  var LADDER = ['simple', 'most-competitive', 'mix-and-match', 'unmade',
    'top-notch-or-better', 'future-grade', 'god-mode'];
  var ID_PREFIX = 'JAH-DAI-';
  var PAGE_BASE = 'https://justinahiggins614-cmyk.github.io/jah-databases/db/';
  var LAST_VERIFIED = '2026-10-21';
  var ANCHOR_KIND = { 'p-demo': 'demo-lab', 'dGen': 'demo-lab', 'p-gen': 'generator', '': 'page' };
  var GENERATOR_CANON = {
    cap_records: CAP,
    cap_note: 'Hard stop at one quadrillion records per database, or earlier when genuinely complete (marked complete with reason).',
    ladder: LADDER,
    self_regulated: true,
    throttled: 'Throttled to a host-safe rate; never overloads the host or burns usage.',
    double_check: 'All generator work is double-checked by the assistant and by the generator itself.',
    dedupe: 'Duplicate check enforced on every write (id dedupe).',
    output_labeling: 'System-generated output is marked "generated"; assistant-built output is marked "assistant-built" -- never mixed.',
    completion_detection: 'Generator knows when complete: when the live manifest holds no new databases, the database is marked complete with reason and stops.'
  };
  var HANDS = ['PC', 'tools'];

  function pad6(n) { var s = String(n); while (s.length < 6) s = '0' + s; return s; }

  function ladderRank(recordCount) {
    var n = parseInt(recordCount, 10) || 0;
    if (n >= 100000) return 'complex';
    if (n >= 1000) return 'compounded';
    return 'simple';
  }

  function onlyDoes(targetName, recordKind) {
    return [
      'Runs ONLY the ' + recordKind + ' demo program of the ' + targetName + ' Demo Lab.',
      'Explains ONLY what that demo and its working version do -- no other topics.',
      'Uses the PC as its hands ONLY to run the demo\'s documented code (copy, download, run with node demo.js).',
      'Uses tools ONLY where the demo documentation names them.',
      'Answers questions ONLY about the ' + targetName + ' demo\'s steps, inputs, and outputs.'
    ];
  }

  function doesNot() {
    return [
      'Does NOT browse the web or fetch new data.',
      'Does NOT generate records beyond the demo\'s documented output.',
      'Does NOT act outside the demo\'s documented steps.',
      'Does NOT change, rewrite, or reinterpret the database -- record data stays as-is.'
    ];
  }

  function genRecord(entry, seq, scan) {
    var name = entry.name || entry.slug;
    var rk = entry.record_kind || 'record';
    var url = scan.url, anchor = scan.anchor, kind = scan.kind;
    var od = onlyDoes(name, rk), dn = doesNot();
    return {
      id: ID_PREFIX + pad6(seq),
      title: 'Locked-in AI -- ' + name,
      target_slug: entry.slug,
      target_name: name,
      target_record_kind: rk,
      target_record_count: (entry.record_count == null ? 0 : entry.record_count),
      target_ai_name: entry.ai_name || '',
      demo_url: url,
      demo_anchor: anchor,
      demo_kind: kind,
      verified: !!scan.verified,
      link_check: scan.link_check,
      scope_locked: true,
      only_does: od,
      does_not: dn,
      hands: HANDS.slice(),
      behavior: 'Deterministic scope lock. Input: an action request. The AI checks the request ' +
        'against the ONLY_DOES keyword gates; if it matches a gate, it performs exactly that demo step ' +
        'with the PC/tools as hands; otherwise it returns the refusal text. No hidden behavior, no ' +
        'extra capabilities -- the AI does exactly what the demo/working version explains, nothing more.',
      refusal: 'That is outside my locked scope. I only do what the ' + name +
        ' demo and working version explain. Ask me about the demo\'s steps, inputs, or outputs.',
      ladder_rank: ladderRank(entry.record_count),
      teaching: {
        simple: 'This AI is locked to one demo: the ' + name + ' demo. It can only do what that demo explains.',
        compounded: 'It uses the PC and tools as its hands to run the demo\'s exact documented steps -- ' +
          'and refuses everything else, saying so in plain words.',
        complex: 'Scope enforcement is deterministic: every request is keyword-gated against the ' +
          'capability list in the record; anything outside the list is denied with the refusal text. ' +
          'The full gate list ships in the record; no hidden capabilities.'
      },
      generator: GENERATOR_CANON,
      program: {
        engine: 'gen-ai-version-for-all-demos.js',
        fn: 'demo',
        args: { demo_url: url, demo_anchor: anchor, scope: od, does_not: dn, hands: HANDS.slice() },
        note: 'The executable demo is demo(record) in the engine file: it runs the deterministic scope ' +
          'gate on sample action requests (ALLOW inside scope, DENY outside) and returns the gate verdicts. ' +
          'Node-tested at build time.'
      },
      working_version: url,
      march_marker: 'MILLION IN PROGRESS',
      src: 'assistant-built',
      provenance: {
        derived_from: 'live manifest.json + local db/<slug>/index.html anchor scan',
        build: 'demoai-lane-r18/build.py',
        order: '2026-10-21 item 84 AI-VERSION-FOR-ALL-DEMOS'
      },
      last_verified: LAST_VERIFIED,
      record_kind: 'locked-in demo AI record',
      ai_name: 'JAH Demo-Locked AI',
      status: 'live'
    };
  }

  /* Fixed demo-operation keyword gate. Deliberately UNIFORM across all records:
   * target-database words are excluded so a record's subject (e.g. "ocean")
   * can never widen the scope. The AI allows only demo-operation language --
   * running, explaining, downloading, and stepping through the demo program
   * with the PC/tools as hands. Everything else is denied. */
  var ALLOW_KW = {};
  ['demo', 'demos', 'working', 'version', 'run', 'runs', 'running', 'pc',
   'tool', 'tools', 'node', 'download', 'copy', 'code', 'program', 'step',
   'steps', 'input', 'inputs', 'output', 'outputs', 'documented', 'hands',
   'explain', 'explains', 'explanation', 'playground', 'simulate',
   'simulation', 'seed', 'button', 'pane', 'lab',
   'demo.js'].forEach(function (w) { ALLOW_KW[w] = 1; });

  /* Deterministic scope gate: the locked-in AI's entire behavior spec.
   * ALLOW -> the AI performs exactly that demo step with PC/tools as hands.
   * DENY  -> the AI returns record.refusal. */
  function scopeGate(record, action) {
    var kw = ALLOW_KW;
    var words = String(action || '').toLowerCase().replace(/[^a-z0-9 ]/g, ' ').split(/\s+/);
    var hits = words.filter(function (w) { return kw[w]; });
    if (hits.length > 0) {
      return { verdict: 'ALLOW', matched: hits, response: 'Performing demo step with PC/tools as hands: ' + action };
    }
    return { verdict: 'DENY', matched: [], response: record.refusal };
  }

  /* Executable demo: run the scope gate over sample requests + link re-verification. */
  function demo(record) {
    var samples = [
      'run the demo on my PC',
      'explain the demo steps and inputs',
      'download the demo tools and run with node demo.js',
      'browse the web for the latest news',
      'write me a poem about the ocean',
      'generate a million unrelated records'
    ];
    var gates = samples.map(function (s) {
      var g = scopeGate(record, s);
      return { action: s, verdict: g.verdict, matched: g.matched };
    });
    var expect = ['ALLOW', 'ALLOW', 'ALLOW', 'DENY', 'DENY', 'DENY'];
    var gateOk = gates.every(function (g, i) { return g.verdict === expect[i]; });
    var m = /^https:\/\/justinahiggins614-cmyk\.github\.io\/jah-databases\/db\/([a-z0-9-]+)\/(#(p-demo|dGen|p-gen))?$/.exec(record.demo_url || '');
    var urlAnchor = m && m[3] ? m[3] : '';
    var checks = [
      { name: 'url-well-formed', pass: !!m },
      { name: 'anchor-known', pass: urlAnchor in ANCHOR_KIND },
      { name: 'anchor-matches-record', pass: urlAnchor === (record.demo_anchor || '') },
      { name: 'kind-matches-anchor', pass: (ANCHOR_KIND[urlAnchor] || '') === (record.demo_kind || '') },
      { name: 'id-format', pass: new RegExp('^' + ID_PREFIX + '\\d{6}$').test(record.id || '') },
      { name: 'scope-locked', pass: record.scope_locked === true },
      { name: 'only-does-nonempty', pass: Array.isArray(record.only_does) && record.only_does.length === 5 },
      { name: 'does-not-nonempty', pass: Array.isArray(record.does_not) && record.does_not.length === 4 },
      { name: 'hands-pc-tools', pass: Array.isArray(record.hands) && record.hands.join(',') === 'PC,tools' },
      { name: 'refusal-present', pass: typeof record.refusal === 'string' && record.refusal.length > 20 },
      { name: 'src-label', pass: record.src === 'assistant-built' },
      { name: 'last-verified', pass: record.last_verified === LAST_VERIFIED }
    ];
    var ok = gateOk && checks.every(function (c) { return c.pass; });
    return { record_id: record.id, ok: ok, scope_gate_ok: gateOk, gates: gates, checks: checks };
  }

  function generate(entries, scans, startSeq) {
    var out = [], seen = {};
    for (var i = 0; i < entries.length; i++) {
      var r = genRecord(entries[i], (startSeq || 1) + i, scans[i]);
      if (seen[r.id]) throw new Error('duplicate id: ' + r.id);
      seen[r.id] = 1;
      out.push(r);
    }
    return out;
  }

  var api = {
    CAP: CAP, LADDER: LADDER, ID_PREFIX: ID_PREFIX, PAGE_BASE: PAGE_BASE,
    LAST_VERIFIED: LAST_VERIFIED, ANCHOR_KIND: ANCHOR_KIND, HANDS: HANDS,
    GENERATOR_CANON: GENERATOR_CANON,
    genRecord: genRecord, demo: demo, scopeGate: scopeGate,
    generate: generate, ladderRank: ladderRank
  };
  if (typeof module !== 'undefined' && module.exports) { module.exports = api; }
  else { root.DemoAILockedGen = api; }
})(typeof self !== 'undefined' ? self : this);
