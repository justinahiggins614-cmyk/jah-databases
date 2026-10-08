/* ✳ SIGNATURE — JAH Data Bases core. Property of Justin Addam Higgins (JAH).
   Shared framework for all 37 databases: manifest, archive browsing, the
   generator registry, cross-database sampling, validation, sessions, and the
   archive-aware AI (Standard 1.0 on-device + Apex backend when configured).
   No API key is ever required from the user. */
var JAHDB = (function () {
  'use strict';
  var MANIFEST_URL = '../data/manifest.json';
  var _manifest = null;

  /* ---------- deterministic PRNG (mulberry32) ---------- */
  function prng(seed) {
    var a = (seed >>> 0) || 1;
    return function () {
      a |= 0; a = (a + 0x6D2B79F5) | 0;
      var t = Math.imul(a ^ (a >>> 15), 1 | a);
      t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t;
      return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
    };
  }
  function hashStr(s) {
    var h = 2166136261;
    s = String(s);
    for (var i = 0; i < s.length; i++) { h ^= s.charCodeAt(i); h = Math.imul(h, 16777619); }
    return h >>> 0;
  }

  /* ---------- manifest ---------- */
  function loadManifest() {
    if (_manifest) return Promise.resolve(_manifest);
    return fetch(MANIFEST_URL).then(function (r) {
      if (!r.ok) throw new Error('manifest ' + r.status);
      return r.json();
    }).then(function (m) { _manifest = m; return m; });
  }
  function dbBySlug(m, slug) {
    for (var i = 0; i < m.databases.length; i++)
      if (m.databases[i].slug === slug) return m.databases[i];
    return null;
  }
  function dataBase(db) {
    return 'https://justinahiggins614-cmyk.github.io/' + db.source + '/';
  }

  /* ---------- deterministic emblem SVG (per-record / per-database image) ---------- */
  var PALETTES = [
    ['#0b1e3a', '#2f7bff', '#9fd0ff'], ['#101418', '#00e5a0', '#b8ffe9'],
    ['#1c0f2e', '#b04dff', '#e3c2ff'], ['#2e1408', '#ff8a2f', '#ffd9a8'],
    ['#0a2e1c', '#34d399', '#c9f5e1'], ['#2b0a12', '#ff4d6d', '#ffc2cf'],
    ['#0f2b33', '#22d3ee', '#bdf3ff'], ['#2e2a08', '#eab308', '#fdf0b3']
  ];
  function emblemSVG(label, sub) {
    var h = hashStr(label), p = PALETTES[h % PALETTES.length];
    var motif = h % 4, inner = '';
    var c = 60, r = 34;
    if (motif === 0) inner = '<circle cx="60" cy="60" r="34" fill="' + p[1] + '" opacity="0.85"/>';
    else if (motif === 1) inner = '<rect x="28" y="28" width="64" height="64" rx="10" fill="' + p[1] + '" opacity="0.85"/>';
    else if (motif === 2) inner = '<polygon points="60,22 96,92 24,92" fill="' + p[1] + '" opacity="0.85"/>';
    else inner = '<ellipse cx="60" cy="60" rx="40" ry="26" fill="' + p[1] + '" opacity="0.85"/>';
    var initials = String(label || '?').split(/[\s-]+/).map(function (w) { return w[0]; }).join('').slice(0, 3).toUpperCase();
    return 'data:image/svg+xml,' + encodeURIComponent(
      '<svg xmlns="http://www.w3.org/2000/svg" width="120" height="120" viewBox="0 0 120 120">' +
      '<rect width="120" height="120" rx="18" fill="' + p[0] + '"/>' + inner +
      '<text x="60" y="68" text-anchor="middle" font-family="Arial,sans-serif" font-size="26" font-weight="bold" fill="' + p[0] + '">' + initials + '</text>' +
      (sub ? '<text x="60" y="106" text-anchor="middle" font-family="Arial,sans-serif" font-size="11" fill="' + p[2] + '">' + sub.slice(0, 18) + '</text>' : '') +
      '</svg>');
  }

  /* ---------- gz fetch ---------- */
  function fetchGz(url) {
    return fetch(url).then(function (r) {
      if (!r.ok) throw new Error('fetch ' + r.status + ' ' + url);
      if (typeof DecompressionStream === 'undefined') return r.text();
      var ds = new DecompressionStream('gzip');
      return new Response(r.body.pipeThrough(ds)).text();
    });
  }
  function fetchJsonlGz(url) {
    return fetchGz(url).then(function (t) {
      return t.split('\n').filter(function (l) { return l.trim(); }).map(function (l) {
        try { return JSON.parse(l); } catch (e) { return null; }
      }).filter(Boolean);
    });
  }

  /* ---------- generator registry ---------- */
  var generators = {};
  function registerGenerator(slug, gen) { generators[slug] = gen; }
  /* gen = { version, generate(seed, opts, rnd) -> record,
             validate(record) -> {ok, errors[]},
             driftCheck(record, archiveSample) -> {ok, errors[]} (optional) } */
  function runGenerator(slug, seed, opts) {
    var gen = generators[slug];
    if (!gen) return { ok: false, errors: ['no generator registered for ' + slug] };
    var rnd = prng(typeof seed === 'number' ? seed : hashStr(String(seed)));
    var rec;
    try { rec = gen.generate(seed, opts || {}, rnd); }
    catch (e) { return { ok: false, errors: ['generate threw: ' + e.message] }; }
    var v = gen.validate(rec);
    if (!v.ok) return { ok: false, errors: v.errors, record: rec };
    rec._gen_version = gen.version;
    rec._seed = seed;
    return { ok: true, record: rec };
  }
  function batchGenerate(slug, n, seedBase, opts) {
    var out = [], fails = 0;
    for (var i = 0; i < n; i++) {
      var r = runGenerator(slug, (seedBase || 1) + i, opts);
      if (r.ok) out.push(r.record); else fails++;
    }
    return { records: out, failures: fails };
  }

  /* ---------- cross-database sampling (the network) ---------- */
  function sampleOther(m, slug, n) {
    var db = dbBySlug(m, slug);
    if (!db || !db.index) return Promise.resolve([]);
    var url = dataBase(db) + db.index;
    return fetchGz(url).then(function (t) {
      var lines = t.split('\n').filter(function (l) { return l.trim(); });
      var rnd = prng(hashStr(slug + Date.now() % 100000));
      var out = [];
      for (var i = 0; i < Math.min(n, lines.length); i++) {
        try { out.push(JSON.parse(lines[(rnd() * lines.length) | 0])); } catch (e) {}
      }
      return out;
    }).catch(function () { return []; });
  }

  /* ---------- sessions: every user gets a fresh screen ---------- */
  function sessionKey(slug) { return 'jahdb_' + slug + '_session'; }
  function newSession(slug) {
    var s = { id: 'S' + Date.now().toString(36) + Math.floor(Math.random() * 1e6).toString(36), started: Date.now(), turns: [] };
    try { localStorage.setItem(sessionKey(slug), JSON.stringify(s)); } catch (e) {}
    return s;
  }
  function getSession(slug) {
    try {
      var s = localStorage.getItem(sessionKey(slug));
      if (s) return JSON.parse(s);
    } catch (e) {}
    return newSession(slug);
  }

  /* ---------- archive-aware AI ---------- */
  /* Uses Standard 1.0 on-device always (no key). If an Apex backend URL or key
     is configured (shared with The Signature AI), cloud answers come from there. */
  function aiAnswer(db, userText, context) {
    var persona = 'You are ' + db.ai_name + ', the archive-aware librarian of the ' +
      db.name + ' (JAH Data Bases, property of Justin Addam Higgins). ' +
      'This database holds ' + db.record_kind + ' records. Answer in natural sentences. ' +
      'When the user asks you to make something, describe the record you would generate ' +
      'in this archive\'s format, or run the generator if one is available on the page. ' +
      'Never invent archive records as if they already exist — say what is generated vs stored.';
    var full = persona + '\n\nArchive context:\n' + (context || '(no archive records loaded yet)') +
      '\n\nUser: ' + userText;
    try {
      if (typeof ApexAI !== 'undefined' && (ApexAI.backend() || ApexAI.key())) {
        return ApexAI.ask(full, { system: persona }).then(function (t) { return String(t); })
          .catch(function () { return standardAnswer(db, userText); });
      }
    } catch (e) {}
    return Promise.resolve(standardAnswer(db, userText));
  }
  function standardAnswer(db, userText) {
    try {
      if (typeof LlamaStandard !== 'undefined' && LlamaStandard.chat)
        return String(LlamaStandard.chat(db.ai_name + ' of the ' + db.name + '. ' + userText));
    } catch (e) {}
    var t = userText.toLowerCase();
    if (/generat|make|create|new/.test(t))
      return 'I can generate new ' + db.record_kind + ' records in this archive\'s exact format. ' +
        'Open the Generator tab, pick a seed, and I\'ll produce validated records — or tell me a theme and I\'ll shape the next batch around it.';
    if (/search|find|look/.test(t))
      return 'Use the Archive tab to search the stored ' + db.record_kind + ' records. ' +
        'Tell me what you\'re hunting for and I\'ll help narrow it down.';
    return 'I\'m ' + db.ai_name + ', keeper of the ' + db.name + '. Ask me to search the archive, ' +
      'explain a record, or generate new ' + db.record_kind + ' records in archive style.';
  }

  return {
    loadManifest: loadManifest, dbBySlug: dbBySlug, dataBase: dataBase,
    emblemSVG: emblemSVG, fetchGz: fetchGz, fetchJsonlGz: fetchJsonlGz,
    prng: prng, hashStr: hashStr,
    registerGenerator: registerGenerator, getGenerator: function (slug) { return generators[slug]; },
    runGenerator: runGenerator, batchGenerate: batchGenerate,
    sampleOther: sampleOther,
    newSession: newSession, getSession: getSession,
    aiAnswer: aiAnswer
  };
})();
