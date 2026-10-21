/* ✳ SIGNATURE — JAH Databases core. Property of Justin Addam Higgins (JAH).
   Shared framework for every database in the network (the live count comes
   from data/manifest.json at runtime): manifest, archive browsing, the
   generator registry, cross-database sampling, validation, sessions, and the
   archive-aware AI (Standard 1.0 on-device + Apex backend when configured).
   No API key is ever required from the user. */
var JAHDB = (function () {
  'use strict';
  /* Base URL of this project, derived from this script's own location so every
     page (hub at root, database pages at db/<slug>/) resolves data correctly. */
  var CORE_BASE = (function () {
    try {
      var s = document.currentScript && document.currentScript.src;
      if (s) return s.replace(/core\/jahdb\.js(\?.*)?(#.*)?$/, '');
    } catch (e) {}
    return '';
  })();
  var MANIFEST_URL = CORE_BASE + 'data/manifest.json';
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
    /* Local project base — databases are standalone; archive data lives in
       this project's own data/<slug>/ directories (or its data shard repos),
       never on the original websites. */
    return CORE_BASE;
  }

  /* ---------- live network size (from the manifest, fetched once, cached) ---------- */
  var _netCount = 0;
  function networkCount() {
    if (_netCount) return Promise.resolve(_netCount);
    return loadManifest().then(function (m) {
      _netCount = (m && m.databases && m.databases.length) || 0;
      return _netCount;
    }).catch(function () { return 0; });
  }
  function networkCountSync() { return _netCount; }

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
  /* Usable-or-demo rule: optional demo-program builder, registered by
     core/jahdb-demo.js via setDemoBuilder. Every generated record ships a
     runnable demo program (record.demo). Attached AFTER validation so no
     generator's validator ever sees the extra field. Without the demo
     engine loaded, generation behavior is byte-identical to before. */
  var demoBuilder = null;
  function setDemoBuilder(fn) { demoBuilder = (typeof fn === 'function') ? fn : null; }
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
    try { if (demoBuilder && !rec.demo) rec.demo = demoBuilder(slug, rec); } catch (e) {}
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

  /* ---------- cross-database sampling (the network) ----------
     Returns a Promise of an ARRAY of sampled records (callers unchanged).
     Failures are NOT silent: the resolved array carries an `.error` string
     describing what went wrong, the failure is console.warned, and it is
     recorded in JAHDB.sampleErrors for diagnostics. Sampling is WITHOUT
     replacement (a partial Fisher-Yates over line positions), so the same
     source record can never be selected twice in one call. */
  var sampleErrors = [];
  function sampleResult(records, error) {
    var out = records.slice();
    if (error) {
      var msg = String(error);
      try { out.error = msg; } catch (e) {}
      try { if (typeof console !== 'undefined' && console.warn) console.warn('[JAHDB] sampleOther: ' + msg); } catch (e) {}
      try {
        sampleErrors.push({ at: Date.now(), error: msg });
        if (sampleErrors.length > 50) sampleErrors.shift();
      } catch (e) {}
    }
    return out;
  }
  function sampleOther(m, slug, n) {
    var db = dbBySlug(m, slug);
    var idx = db && (db.local_index || db.index);
    if (!idx) return Promise.resolve(sampleResult([], 'no index configured for database "' + slug + '" — cross-database sampling unavailable'));
    var url = (/^https?:\/\//i.test(idx) ? '' : dataBase(db)) + idx;
    return fetchGz(url).then(function (t) {
      var lines = t.split('\n').filter(function (l) { return l.trim(); });
      if (!lines.length) return sampleResult([], 'index for "' + slug + '" fetched but contained no rows');
      var rnd = prng(hashStr(slug + (Date.now() % 100000)));
      var order = [];
      for (var i = 0; i < lines.length; i++) order.push(i);
      var k = Math.min(n, lines.length), out = [], bad = 0, p, j, tmp;
      for (p = 0; p < k; p++) {
        j = p + ((rnd() * (lines.length - p)) | 0);
        tmp = order[p]; order[p] = order[j]; order[j] = tmp;
        try { out.push(JSON.parse(lines[order[p]])); }
        catch (e) { bad++; }
      }
      if (!out.length) return sampleResult([], 'index for "' + slug + '" had ' + lines.length + ' lines but none parsed as JSON');
      return sampleResult(out, bad ? (bad + ' of ' + k + ' sampled lines failed JSON.parse and were skipped') : null);
    }).catch(function (err) {
      return sampleResult([], 'failed to fetch/parse index for "' + slug + '": ' + (err && err.message ? err.message : String(err)));
    });
  }

  /* ---------- cross-database query (AI reasoning across the network) ---------- */
  /* LAZY by design: the manifest loads once per session (cached above);
     another database's index is only fetched when cross-database intent is
     detected — never at page boot, so boot cost on phones stays zero.
     Every returned ID comes from a real fetched index — IDs are never invented. */
  var _idxRows = {};      /* slug -> Promise(rows) */
  var _idxOrder = [];     /* tiny LRU so phones don't hoard parsed indexes */
  var CROSS_STOP = { the:1,a:1,an:1,and:1,or:1,of:1,in:1,to:1,for:1,on:1,with:1,by:1,
    is:1,are:1,was:1,were:1,be:1,been:1,what:1,which:1,who:1,whom:1,whose:1,all:1,
    every:1,each:1,any:1,some:1,my:1,your:1,our:1,i:1,you:1,we:1,they:1,it:1,this:1,
    that:1,these:1,those:1,there:1,their:1,from:1,about:1,into:1,how:1,do:1,does:1,
    did:1,can:1,could:1,should:1,would:1,will:1,find:1,search:1,show:1,give:1,me:1,
    across:1,database:1,databases:1,db:1,please:1,than:1,then:1,also:1,just:1,like:1,
    has:1,have:1,had:1,not:1,no:1,yes:1,if:1,else:1,when:1,where:1,why:1 };
  function crossKeywords(q) {
    var out = [], seen = {};
    String(q || '').toLowerCase().replace(/[^a-z0-9\s]/g, ' ').split(/\s+/).forEach(function (w) {
      if (w.length < 3 || CROSS_STOP[w] || seen[w]) return;
      seen[w] = 1; out.push(w);
    });
    return out;
  }
  function crossDbIntent(q) {
    var low = String(q || '').toLowerCase();
    return /search (all|every|each)( of)?( the)? databases?\b/.test(low) ||
      /across all( of)?( the)? databases?\b/.test(low) ||
      /\bin (all|every)( of)?( the)? databases?\b/.test(low) ||
      (/\b(all|every)( of)?( the)? databases?\b/.test(low) &&
        /\b(search|find|look|check|query|scan|hunt)\b/.test(low));
  }
  function stripCrossIntent(q) {
    return String(q || '').toLowerCase()
      .replace(/search (all|every|each)( of)?( the)? databases?( for| about)?/g, ' ')
      .replace(/across all( of)?( the)? databases?/g, ' ')
      .replace(/in (all|every)( of)?( the)? databases?/g, ' ')
      .replace(/\b(all|every)( of)?( the)? databases?\b/g, ' ')
      .replace(/[?.!]+$/g, '').replace(/\s+/g, ' ').trim();
  }
  /* Fetch an index as text; gzipped files go through fetchGz, plain-JSON
     indexes fall back to a plain fetch (some indexes aren't gzipped). */
  function fetchIndexText(url) {
    return fetchGz(url).catch(function () {
      return fetch(url).then(function (r) {
        if (!r.ok) throw new Error('fetch ' + r.status + ' ' + url);
        return r.text();
      });
    });
  }
  /* One index row -> {id, title}, across the index shapes in the wild:
     {id,t,...} JSONL, patents-style [id,title,...] arrays, {i,t,...},
     {id,title,...} / {name,...} plain-JSON rows. Unparseable rows are skipped. */
  function normRow(r) {
    var id, t;
    if (Array.isArray(r)) { id = r[0]; t = r[1]; }
    else if (r && typeof r === 'object') {
      id = r.id || r.i || r.record_id || r.spec_id || r.pub_no;
      t = r.t || r.title || r.name || r.headword || r.word;
    }
    if (typeof id !== 'string' && typeof id !== 'number') return null;
    if (typeof t !== 'string' || !t.trim()) return null;
    return { id: String(id), title: String(t).trim() };
  }
  function parseIndexText(txt) {
    var rows = [], trimmed = String(txt || '').trim();
    if (!trimmed) return rows;
    try {
      var doc = JSON.parse(trimmed);
      if (Array.isArray(doc)) {
        doc.forEach(function (r) { var n = normRow(r); if (n) rows.push(n); });
        if (rows.length) return rows;
      }
    } catch (e) { /* not whole-document JSON — try JSONL below */ }
    trimmed.split('\n').forEach(function (l) {
      l = l.trim();
      if (!l) return;
      try { var n = normRow(JSON.parse(l)); if (n) rows.push(n); } catch (e) {}
    });
    return rows;
  }
  function deepLinkFor(slug, id) {
    return CORE_BASE + 'db/' + slug + '/#rec=' + encodeURIComponent(id);
  }
  function idxRowsFor(d) {
    var idx = d.local_index || d.index;
    var url = (/^https?:\/\//i.test(idx) ? '' : dataBase(d)) + idx;
    var key = d.slug;
    if (!_idxRows[key]) {
      _idxRows[key] = fetchIndexText(url).then(parseIndexText);
      _idxRows[key].catch(function () { delete _idxRows[key]; });
      _idxOrder.push(key);
      while (_idxOrder.length > 3) { delete _idxRows[_idxOrder.shift()]; }
    }
    return _idxRows[key];
  }
  function scanDbIndex(d, kws) {
    return idxRowsFor(d).then(function (rows) {
      var hits = [];
      for (var i = 0; i < rows.length; i++) {
        var hay = rows[i].title.toLowerCase(), s = 0;
        for (var k = 0; k < kws.length; k++) if (hay.indexOf(kws[k]) >= 0) s++;
        if (s > 0) hits.push({ dbName: d.name, dbSlug: d.slug, recordId: rows[i].id,
          title: rows[i].title, score: s, deepLink: deepLinkFor(d.slug, rows[i].id) });
      }
      hits.sort(function (a, b) { return b.score - a.score; });
      return hits.slice(0, 4);
    });
  }
  /* crossQuery(query, opts) -> Promise([{dbName, dbSlug, recordId, title, deepLink}]).
     Two stages: cheap manifest-metadata ranking picks the top candidate
     databases, then only those indexes are fetched and title-scanned.
     opts: {exclude: slug, n: max results (default 5)}. */
  function crossQuery(query, opts) {
    opts = opts || {};
    var n = opts.n || 5, exclude = opts.exclude || null;
    var kws = crossKeywords(query);
    if (!kws.length) return Promise.resolve([]);
    return loadManifest().then(function (m) {
      var dbs = (m && m.databases) || [], scored = [], i, k;
      for (i = 0; i < dbs.length; i++) {
        var d = dbs[i];
        if (exclude && d.slug === exclude) continue;
        var idx = d.local_index || d.index;
        if (!idx || /^virtual:/i.test(String(idx))) continue;
        var hay = ((d.name || '') + ' ' + (d.record_kind || '') + ' ' + (d.tagline || '')).toLowerCase();
        var s = 0;
        for (k = 0; k < kws.length; k++) if (hay.indexOf(kws[k]) >= 0) s++;
        if (s > 0) scored.push({ db: d, s: s });
      }
      scored.sort(function (a, b) { return b.s - a.s; });
      var cands = scored.slice(0, 6).map(function (x) { return x.db; });
      if (!cands.length) return [];
      return Promise.all(cands.map(function (d) {
        return scanDbIndex(d, kws).catch(function () { return []; });
      })).then(function (lists) {
        var all = [];
        lists.forEach(function (l) { all = all.concat(l); });
        all.sort(function (a, b) { return b.score - a.score; });
        var seen = {}, out = [];
        for (var t = 0; t < all.length && out.length < n; t++) {
          var h = all[t];
          seen[h.dbSlug] = seen[h.dbSlug] || 0;
          if (seen[h.dbSlug] < 2) {
            seen[h.dbSlug]++;
            out.push({ dbName: h.dbName, dbSlug: h.dbSlug, recordId: h.recordId,
              title: h.title, deepLink: h.deepLink });
          }
        }
        return out;
      });
    }).catch(function () { return []; });
  }
  /* Plain-language answer for an explicit cross-database question. */
  function crossAnswer(db, userText) {
    var topic = stripCrossIntent(userText);
    if (!topic) return Promise.resolve(
      'Tell me what to search for across the databases — for example, "search all databases for solar panels".');
    return networkCount().then(function (cnt) {
      return crossQuery(topic, { exclude: db && db.slug, n: 5 });
    }).then(function (hits) {
      var total = networkCountSync() || 444;
      if (!hits.length)
        return 'I searched across all ' + total + ' databases and found no stored records matching "' +
          topic + '". Tell me which database it might live in and I\'ll point you there — ' +
          'or ask me to generate a new record in this archive\'s style.';
      var lines = ['I searched across the databases and found ' + hits.length +
        ' stored record' + (hits.length === 1 ? '' : 's') + ':'];
      hits.forEach(function (h, i) {
        lines.push((i + 1) + '. ' + h.title + ' — in the ' + h.dbName + '. Open: ' + h.deepLink);
      });
      return lines.join('\n');
    }).catch(function () {
      return 'That cross-database search hiccuped. Try again, or tell me which database to look in.';
    });
  }

  /* ---------- per-record deep links ("links to works") ---------- */
  /* Pages set location.hash to #rec=<id> whenever a full record view opens,
     and offer a "Copy link" control that hands the user the absolute URL.
     Opening a page with #rec=<id> lets the page auto-open that record. */
  function recHashGet() {
    try {
      var m = String(location.hash || '').match(/#rec=([^&]+)/);
      return m ? decodeURIComponent(m[1]) : '';
    } catch (e) { return ''; }
  }
  function recHashSet(id) {
    try { if (id) location.hash = '#rec=' + encodeURIComponent(id); } catch (e) {}
  }
  function recHashClear() {
    try {
      if (String(location.hash || '').indexOf('#rec=') === 0)
        history.replaceState(null, '', location.pathname + location.search);
    } catch (e) {}
  }
  function recLink(id) {
    try { return location.origin + location.pathname + '#rec=' + encodeURIComponent(id); }
    catch (e) { return '#rec=' + encodeURIComponent(id); }
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
    /* Explicit cross-database questions get real cross-database answers —
       real stored records with deep links, never invented ones. */
    try { if (crossDbIntent(userText)) return crossAnswer(db, userText); } catch (e) {}
    /* Deep investigations ("deep search", "investigate", "research") get the
       multi-pass universal search engine when it is loaded. */
    try { if (typeof JAHSearch !== 'undefined' && JAHSearch.deepSearchIntent(userText)) return JAHSearch.aiDeepSearch(db, userText); } catch (e) {}
    var persona = 'You are ' + db.ai_name + ', the archive-aware librarian of the ' +
      db.name + ' (JAH Databases, property of Justin Addam Higgins). ' +
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
    networkCount: networkCount, networkCountSync: networkCountSync,
    emblemSVG: emblemSVG, fetchGz: fetchGz, fetchJsonlGz: fetchJsonlGz,
    prng: prng, hashStr: hashStr,
    registerGenerator: registerGenerator, setDemoBuilder: setDemoBuilder, getGenerator: function (slug) { return generators[slug]; },
    runGenerator: runGenerator, batchGenerate: batchGenerate,
    sampleOther: sampleOther, sampleErrors: sampleErrors,
    crossQuery: crossQuery, crossDbIntent: crossDbIntent, stripCrossIntent: stripCrossIntent,
    newSession: newSession, getSession: getSession,
    recHashGet: recHashGet, recHashSet: recHashSet, recHashClear: recHashClear, recLink: recLink,
    aiAnswer: aiAnswer
  };
})();

/* ---------- Universal Search + AI Deep Search loader (ADDITIVE) ----------
   Manon's order: one search bar for the whole network, real record search,
   multi-pass AI deep search. This only LOADS the separate jahdb-search.js
   module. Nothing above is modified. If the module 404s, every page works
   exactly as before. */
(function () {
  try {
    var scripts = document.getElementsByTagName('script'), base = null, i, s;
    for (i = 0; i < scripts.length; i++) {
      s = scripts[i].src || '';
      if (/core\/jahdb\.js/.test(s)) { base = s.replace(/jahdb\.js.*$/, ''); break; }
    }
    if (!base || typeof JAHSearch !== 'undefined') return;
    var el = document.createElement('script');
    el.src = base + 'jahdb-search.js';
    el.defer = true;
    el.onerror = function () { /* universal search optional — page works without it */ };
    document.head.appendChild(el);
  } catch (e) { /* never break the page */ }
})();
