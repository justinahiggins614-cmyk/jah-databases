/* ✳ SIGNATURE — JAH Network Universal Search + AI Deep Search.
   Property of Justin Addam Higgins (JAH).
   One search engine for the whole network: query understanding, multi-pass
   deep search across every database's real records, and honest reporting.
   Loads additively via core/jahdb.js — never breaks pages if it fails. */
var JAHSearch = (function () {
  'use strict';

  /* ================= configuration ================= */
  var CFG = {
    indexCacheSize: 40,     /* parsed-index LRU entries per session */
    chunkCacheSize: 60,     /* parsed-chunk LRU entries per session */
    fetchConcurrency: 6,    /* parallel index fetches */
    chunkScanCap: 12,       /* max chunks scanned to find one record */
    quick:      { dbs: 12, results: 10, retrieve: 0,  connPasses: 0 },
    deep:       { dbs: 40, results: 15, retrieve: 12, connPasses: 1 },
    exhaustive: { dbs: 400, results: 25, retrieve: 20, connPasses: 2 }
  };

  /* ================= base URL (same derivation as jahdb.js) ================= */
  var CORE_BASE = (function () {
    try {
      var ss = document.getElementsByTagName('script');
      for (var i = 0; i < ss.length; i++) {
        var s = ss[i].src || '';
        if (/core\/jahdb-search\.js/.test(s)) return s.replace(/core\/jahdb-search\.js.*$/, '');
      }
      var c = document.currentScript && document.currentScript.src;
      if (c) return c.replace(/core\/jahdb-search\.js(\?.*)?(#.*)?$/, '');
    } catch (e) {}
    return '';
  })();
  function absUrl(u) { return (/^https?:\/\//i.test(u) ? '' : CORE_BASE) + u; }
  function deepLinkFor(slug, id) { return CORE_BASE + 'db/' + slug + '/#rec=' + encodeURIComponent(id); }

  /* ================= deterministic PRNG (for stable sampling) ================= */
  function hashStr(s) {
    var h = 2166136261; s = String(s);
    for (var i = 0; i < s.length; i++) { h ^= s.charCodeAt(i); h = Math.imul(h, 16777619); }
    return h >>> 0;
  }

  /* ================= PASS 0 — query understanding ================= */
  var STOP = { the:1,a:1,an:1,and:1,or:1,of:1,in:1,to:1,for:1,on:1,with:1,by:1,
    is:1,are:1,was:1,were:1,be:1,been:1,what:1,which:1,who:1,whom:1,whose:1,all:1,
    every:1,each:1,any:1,some:1,my:1,your:1,our:1,i:1,you:1,we:1,they:1,it:1,this:1,
    that:1,these:1,those:1,there:1,their:1,from:1,about:1,into:1,how:1,do:1,does:1,
    did:1,can:1,could:1,should:1,would:1,will:1,find:1,search:1,show:1,give:1,me:1,
    across:1,database:1,databases:1,db:1,please:1,than:1,then:1,also:1,just:1,like:1,
    has:1,have:1,had:1,not:1,no:1,yes:1,if:1,else:1,when:1,where:1,why:1,tell:1,
    get:1,got:1,know:1,deep:1,quick:1,exhaustive:1 };
  /* small synonym map — expanded terms score at half weight */
  var SYN = {
    movie:['film','cinema'], film:['movie','cinema'], tv:['television','series','show'],
    television:['tv','series'], show:['tv','series','television'], music:['song','audio','melody'],
    song:['music','melody'], car:['automobile','vehicle'], poem:['poetry','verse'],
    poetry:['poem','verse'], rhyme:['rhyming'], dog:['canine','puppy'], cat:['feline','kitten'],
    food:['recipe','cooking','meal'], recipe:['food','cooking'], game:['videogame','play'],
    book:['novel','ebook','publication'], picture:['image','photo','photograph'],
    image:['picture','photo'], photo:['picture','image'], video:['movie','clip','film'],
    health:['medical','medicine','wellness'], medicine:['drug','pharmaceutical','remedy'],
    surgery:['operation','surgical'], space:['cosmos','astronomy','universe'],
    planet:['world'], ai:['artificial intelligence','llm','model'], robot:['robotics','android'],
    money:['finance','currency','wealth'], law:['legal','statute'], history:['historical','past'],
    science:['scientific'], math:['mathematics','equation'], word:['term','vocabulary'],
    baby:['infant','newborn'], love:['romance'], war:['battle','conflict'], death:['mortality']
  };
  function understandQuery(q) {
    q = String(q || '');
    var phrases = [];
    q.replace(/"([^"]+)"/g, function (m, p) { phrases.push(p.toLowerCase()); return ' '; });
    var kws = [], seen = {};
    q.toLowerCase().replace(/[^a-z0-9\s]/g, ' ').split(/\s+/).forEach(function (w) {
      if (w.length < 3 || STOP[w] || seen[w]) return;
      seen[w] = 1; kws.push({ t: w, w: 1 });
    });
    /* synonym expansion at half weight */
    var extra = [];
    kws.forEach(function (k) {
      (SYN[k.t] || []).forEach(function (s) {
        if (!seen[s]) { seen[s] = 1; extra.push({ t: s, w: 0.5, via: k.t }); }
      });
    });
    var all = kws.concat(extra);
    var isQuestion = /^(what|which|who|whom|whose|when|where|why|how|is|are|was|were|do|does|did|can|could|should|would|will)\b/i.test(q.trim()) || /\?\s*$/.test(q);
    return { raw: q, keywords: all, phrases: phrases, isQuestion: isQuestion };
  }

  /* ================= manifest ================= */
  var _manifest = null;
  function loadManifest() {
    if (_manifest) return Promise.resolve(_manifest);
    if (typeof JAHDB !== 'undefined' && JAHDB.loadManifest) return JAHDB.loadManifest().then(function (m) { _manifest = m; return m; });
    return fetch(absUrl('data/manifest.json')).then(function (r) {
      if (!r.ok) throw new Error('manifest ' + r.status);
      return r.json();
    }).then(function (m) { _manifest = m; return m; });
  }
  function fetchableDb(d) {
    var idx = d.local_index || d.index;
    if (!idx || /^virtual:/i.test(String(idx))) return false;
    if (d.internal) return false;
    return true;
  }

  /* ================= PASS 1 — DISCOVERY: rank every database ================= */
  /* Scores ALL databases on metadata — never a fixed shortlist. The caller
     decides how many of the ranked candidates to actually open. */
  function discoverDatabases(manifest, qu) {
    var dbs = (manifest && manifest.databases) || [], out = [], i, k;
    for (i = 0; i < dbs.length; i++) {
      var d = dbs[i];
      if (!fetchableDb(d)) continue;
      var name = String(d.name || '').toLowerCase();
      var kind = String(d.record_kind || '').toLowerCase();
      var tag = String(d.tagline || '').toLowerCase();
      var ai = String(d.ai_name || '').toLowerCase();
      var s = 0, matched = 0;
      for (k = 0; k < qu.keywords.length; k++) {
        var kw = qu.keywords[k], w = kw.w, hit = false;
        if (name.indexOf(kw.t) >= 0) { s += 3 * w; hit = true; }
        if (kind.indexOf(kw.t) >= 0) { s += 2 * w; hit = true; }
        if (tag.indexOf(kw.t) >= 0) { s += 2 * w; hit = true; }
        if (ai.indexOf(kw.t) >= 0) { s += 1 * w; hit = true; }
        if (hit && w === 1) matched++;
      }
      qu.phrases.forEach(function (p) {
        if ((name + ' ' + kind + ' ' + tag).indexOf(p) >= 0) s += 5;
      });
      if (matched >= 2) s += 3;
      if (s > 0) out.push({ db: d, score: s });
    }
    out.sort(function (a, b) { return b.score - a.score; });
    return out;
  }

  /* ================= index fetching + parsing ================= */
  var _idxCache = {};   /* slug -> {rows, at} */
  var _idxOrder = [];
  function fetchGz(url) {
    return fetch(url).then(function (r) {
      if (!r.ok) throw new Error('fetch ' + r.status + ' ' + url);
      if (typeof DecompressionStream === 'undefined') return r.text();
      var ds = new DecompressionStream('gzip');
      return new Response(r.body.pipeThrough(ds)).text();
    });
  }
  function fetchIndexText(url) {
    return fetchGz(url).catch(function () {
      return fetch(url).then(function (r) {
        if (!r.ok) throw new Error('fetch ' + r.status + ' ' + url);
        return r.text();
      });
    });
  }
  function normRow(r) {
    var id, t;
    if (Array.isArray(r)) { id = r[0]; t = r[1]; }
    else if (r && typeof r === 'object') {
      id = r.id || r.i || r.record_id || r.spec_id || r.pub_no;
      t = r.t || r.title || r.name || r.headword || r.word;
    }
    if (typeof id !== 'string' && typeof id !== 'number') return null;
    if (typeof t !== 'string' || !t.trim()) return null;
    return { id: String(id), title: String(t).trim(), _raw: r };
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
    } catch (e) {}
    trimmed.split('\n').forEach(function (l) {
      l = l.trim();
      if (!l) return;
      try { var n = normRow(JSON.parse(l)); if (n) rows.push(n); } catch (e2) {}
    });
    return rows;
  }
  /* full text of a row: every scalar value, so search is not title-only */
  function rowText(row) {
    var r = row._raw, parts = [];
    if (Array.isArray(r)) {
      r.forEach(function (v) { if (typeof v === 'string' || typeof v === 'number') parts.push(String(v)); });
    } else if (r && typeof r === 'object') {
      Object.keys(r).forEach(function (k) {
        var v = r[k];
        if (typeof v === 'string' || typeof v === 'number') parts.push(String(v));
      });
    }
    return parts.join(' ');
  }
  function getIndexRows(d) {
    var key = d.slug;
    if (_idxCache[key]) {
      _idxOrder.splice(_idxOrder.indexOf(key), 1);
      _idxOrder.push(key);
      return Promise.resolve(_idxCache[key].rows);
    }
    var idx = d.local_index || d.index;
    var url = absUrl(idx);
    var p = fetchIndexText(url).then(parseIndexText).then(function (rows) {
      _idxCache[key] = { rows: rows, at: Date.now() };
      _idxOrder.push(key);
      while (_idxOrder.length > CFG.indexCacheSize) { delete _idxCache[_idxOrder.shift()]; }
      return rows;
    });
    p.catch(function () { /* don't cache failures */ });
    return p;
  }
  /* parallel map with concurrency cap */
  function pmap(items, fn, concurrency) {
    concurrency = concurrency || CFG.fetchConcurrency;
    var i = 0, results = new Array(items.length), active = 0;
    return new Promise(function (resolve) {
      function next() {
        if (i >= items.length && active === 0) { resolve(results); return; }
        while (active < concurrency && i < items.length) {
          (function (idx) {
            active++;
            Promise.resolve().then(function () { return fn(items[idx], idx); }).then(
              function (v) { results[idx] = { ok: true, v: v }; },
              function (e) { results[idx] = { ok: false, e: e }; }
            ).then(function () { active--; next(); });
          })(i++);
        }
      }
      next();
    });
  }

  /* ================= PASS 2 — INDEX SEARCH ================= */
  function scoreRow(row, qu) {
    var title = row.title.toLowerCase();
    var rest = rowText(row).toLowerCase();
    var s = 0, matched = 0;
    for (var k = 0; k < qu.keywords.length; k++) {
      var kw = qu.keywords[k];
      if (title.indexOf(kw.t) >= 0) { s += 3 * kw.w; if (kw.w === 1) matched++; }
      else if (rest.indexOf(kw.t) >= 0) { s += 1 * kw.w; if (kw.w === 1) matched++; }
    }
    qu.phrases.forEach(function (p) {
      if (title.indexOf(p) >= 0) s += 5;
      else if (rest.indexOf(p) >= 0) s += 2;
    });
    if (matched >= 2) s += 2;
    return { score: s, matched: matched };
  }
  /* Search the indexes of candidate DBs. Returns {hits, dbsSearched, dbsFailed, recordsExamined}. */
  function searchIndexes(candidates, qu, opts, onProgress) {
    opts = opts || {};
    var perDb = opts.perDb || 5;
    var stats = { dbsSearched: 0, dbsFailed: 0, recordsExamined: 0 };
    var allHits = [];
    return pmap(candidates, function (c) {
      var d = c.db;
      return getIndexRows(d).then(function (rows) {
        stats.dbsSearched++;
        stats.recordsExamined += rows.length;
        var hits = [];
        for (var i = 0; i < rows.length; i++) {
          var sc = scoreRow(rows[i], qu);
          if (sc.score > 0) {
            hits.push({ dbName: d.name, dbSlug: d.slug, recordKind: d.record_kind,
              recordId: rows[i].id, title: rows[i].title, score: sc.score,
              indexPos: i, deepLink: deepLinkFor(d.slug, rows[i].id) });
          }
        }
        hits.sort(function (a, b) { return b.score - a.score; });
        if (onProgress) onProgress({ dbsSearched: stats.dbsSearched, recordsExamined: stats.recordsExamined });
        return hits.slice(0, perDb);
      }).catch(function () { stats.dbsFailed++; return []; });
    }).then(function (res) {
      res.forEach(function (r) { if (r.ok) allHits = allHits.concat(r.v); });
      allHits.sort(function (a, b) { return b.score - a.score; });
      return { hits: allHits, dbsSearched: stats.dbsSearched, dbsFailed: stats.dbsFailed,
        recordsExamined: stats.recordsExamined };
    });
  }

  /* ================= PASS 3 — RECORD RETRIEVAL ================= */
  var _chunkCache = {};
  var _chunkOrder = [];
  function chunkUrlFor(db, n) {
    var pat = db.chunk_pattern;
    if (!pat) return null;
    var m = pat.match(/N+/);
    if (!m) return absUrl(pat);
    var num = String(n);
    while (num.length < m[0].length) num = '0' + num;
    return absUrl(pat.replace(/N+/, num));
  }
  function getChunk(db, n) {
    var key = db.slug + '#' + n;
    if (_chunkCache[key]) {
      _chunkOrder.splice(_chunkOrder.indexOf(key), 1);
      _chunkOrder.push(key);
      return Promise.resolve(_chunkCache[key]);
    }
    var url = chunkUrlFor(db, n);
    if (!url) return Promise.resolve(null);
    return fetchGz(url).then(function (t) {
      var recs = [];
      t.split('\n').forEach(function (l) {
        l = l.trim();
        if (!l) return;
        try { recs.push(JSON.parse(l)); } catch (e) {}
      });
      _chunkCache[key] = recs;
      _chunkOrder.push(key);
      while (_chunkOrder.length > CFG.chunkCacheSize) { delete _chunkCache[_chunkOrder.shift()]; }
      return recs;
    }).catch(function () { return null; });
  }
  function recIdOf(r) {
    if (!r || typeof r !== 'object') return null;
    var id = r.id || r.record_id || r.spec_id;
    return (typeof id === 'string' || typeof id === 'number') ? String(id) : null;
  }
  /* Find a full record by ID. Uses the index position as a chunk hint, then
     scans outward. Returns the record object or null. */
  function fetchRecord(db, recordId, indexPos) {
    var order = [], seen = {};
    function push(n) { if (n >= 0 && !seen[n]) { seen[n] = 1; order.push(n); } }
    if (typeof indexPos === 'number' && indexPos >= 0) {
      var g = Math.floor(indexPos / 100);
      push(g); push(g - 1); push(g + 1); push(g - 2); push(g + 2);
    }
    for (var i = 0; i < CFG.chunkScanCap; i++) push(i);
    var chain = Promise.resolve(null);
    order.forEach(function (n) {
      chain = chain.then(function (found) {
        if (found) return found;
        return getChunk(db, n).then(function (recs) {
          if (!recs) return null;
          for (var j = 0; j < recs.length; j++)
            if (recIdOf(recs[j]) === String(recordId)) return recs[j];
          return null;
        });
      });
    });
    return chain;
  }
  var EXCERPT_FIELDS = ['description', 'text', 'content', 'summary', 'definition',
    'overview', 'details', 'body', 'excerpt', 'analysis'];
  function excerptOf(rec) {
    if (!rec || typeof rec !== 'object') return '';
    var i, f, v;
    for (i = 0; i < EXCERPT_FIELDS.length; i++) {
      f = EXCERPT_FIELDS[i]; v = rec[f];
      if (typeof v === 'string' && v.trim().length > 40)
        return v.trim().slice(0, 260) + (v.trim().length > 260 ? '…' : '');
    }
    var best = '';
    Object.keys(rec).forEach(function (k) {
      v = rec[k];
      if (typeof v === 'string' && v.length > best.length && v.length < 2000
          && k !== 'id' && k !== 'demo' && k.indexOf('_') !== 0) best = v;
    });
    best = best.trim();
    return best.slice(0, 260) + (best.length > 260 ? '…' : '');
  }
  /* Enrich top hits with full records + excerpts. */
  function retrieveRecords(hits, manifest, n, onProgress) {
    var bySlug = {};
    (manifest.databases || []).forEach(function (d) { bySlug[d.slug] = d; });
    var top = hits.slice(0, n), done = 0;
    return pmap(top, function (h) {
      var d = bySlug[h.dbSlug];
      if (!d) return h;
      return fetchRecord(d, h.recordId, h.indexPos).then(function (rec) {
        done++;
        if (onProgress) onProgress({ retrieved: done, of: top.length });
        if (rec) {
          h.fullRecord = rec;
          h.excerpt = excerptOf(rec);
          h.src = rec.src || rec.s || null;
        }
        return h;
      }).catch(function () { done++; return h; });
    }, 4).then(function (res) {
      return res.map(function (r) { return r.ok ? r.v : null; }).filter(Boolean);
    });
  }

  /* ================= PASS 4 — CONNECTION SEARCH ================= */
  var IDREF_RE = /\bJAH-[A-Z]{1,8}-?\d{1,8}\b/g;
  function extractRefs(rec) {
    var refs = {}, out = [];
    if (!rec || typeof rec !== 'object') return out;
    ['related', 'see_also', 'seeAlso', 'links', 'related_ids', 'solution_ids',
     'paradox_id', 'based_on'].forEach(function (f) {
      var v = rec[f];
      if (Array.isArray(v)) v.forEach(function (x) { if (typeof x === 'string') refs[x] = 1; });
      else if (typeof v === 'string' && v) refs[v] = 1;
    });
    Object.keys(rec).forEach(function (k) {
      var v = rec[k];
      if (typeof v !== 'string' || v.length > 4000) return;
      var m;
      IDREF_RE.lastIndex = 0;
      while ((m = IDREF_RE.exec(v)) !== null) refs[m[0]] = 1;
    });
    Object.keys(refs).forEach(function (r) { out.push(r); });
    return out.slice(0, 12);
  }
  function dbForRefId(manifest, refId) {
    var dbs = manifest.databases || [], i;
    for (i = 0; i < dbs.length; i++) {
      var p = dbs[i].id_prefix;
      if (p && refId.indexOf(p) === 0) return dbs[i];
    }
    return null;
  }
  /* Follow references out of retrieved records into related records. */
  function connectionSearch(enriched, manifest, qu) {
    var connections = [], seenHit = {};
    enriched.forEach(function (h) { seenHit[h.recordId] = 1; });
    var jobs = [];
    enriched.forEach(function (h) {
      if (!h.fullRecord) return;
      extractRefs(h.fullRecord).forEach(function (ref) {
        if (seenHit[ref]) return;
        seenHit[ref] = 1;
        var d = dbForRefId(manifest, ref);
        if (!d || !fetchableDb(d)) return;
        jobs.push({ ref: ref, db: d, from: h });
      });
    });
    jobs = jobs.slice(0, 15);
    return pmap(jobs, function (job) {
      return fetchRecord(job.db, job.ref, -1).then(function (rec) {
        if (!rec) return null;
        return { dbName: job.db.name, dbSlug: job.db.slug, recordKind: job.db.record_kind,
          recordId: recIdOf(rec) || job.ref, title: rec.title || rec.name || rec.t || job.ref,
          excerpt: excerptOf(rec), score: 2, via: job.from.title,
          deepLink: deepLinkFor(job.db.slug, recIdOf(rec) || job.ref),
          fullRecord: rec, src: rec.src || null, connection: true };
      }).catch(function () { return null; });
    }, 4).then(function (res) {
      res.forEach(function (r) { if (r.ok && r.v) connections.push(r.v); });
      return connections;
    });
  }

  /* ================= PASS 5 — VERIFICATION ================= */
  function srcLabel(src) {
    if (!src) return { kind: 'archive', label: 'Archived record' };
    var s = String(src).toLowerCase();
    if (s.indexOf('public-harvest') >= 0) return { kind: 'archive', label: 'Public record (harvested)' };
    if (s.indexOf('generated-sample') >= 0 || s.indexOf('generated_sample') >= 0)
      return { kind: 'generated', label: 'Generated sample (labeled)' };
    if (s.indexOf('signature') >= 0) return { kind: 'archive', label: 'Signature original' };
    return { kind: 'archive', label: 'Archived record' };
  }
  function verifyHits(hits) {
    hits.forEach(function (h) {
      var sl = srcLabel(h.src);
      h.sourceKind = sl.kind;
      h.sourceLabel = sl.label;
    });
    return hits;
  }

  /* ================= PASS 6 — FINAL REPORT ================= */
  function buildReport(query, mode, qu, stats, findings, connections) {
    findings = verifyHits(findings);
    connections = verifyHits(connections);
    var uncertainties = [];
    if (stats.dbsFailed > 0)
      uncertainties.push(stats.dbsFailed + ' database index(es) could not be loaded and were skipped.');
    if (mode === 'exhaustive' && stats.coverageCapped)
      uncertainties.push('Exhaustive search was capped at ' + stats.dbsSearched +
        ' databases for this session; ' + stats.dbsDiscovered +
        ' matched the query. The remainder were not searched.');
    var genCount = findings.filter(function (h) { return h.sourceKind === 'generated'; }).length;
    if (genCount > 0)
      uncertainties.push(genCount + ' result(s) are labeled generated samples, not archived records.');
    if (!findings.length)
      uncertainties.push('No stored records matched. The query may need different terms, or the material may not be archived yet.');
    var further = [];
    var seenDb = {};
    findings.slice(0, 8).forEach(function (h) {
      if (!seenDb[h.dbSlug]) { seenDb[h.dbSlug] = 1; further.push(h.dbName); }
    });
    return {
      query: query, mode: mode, keywords: qu.keywords.map(function (k) { return k.t; }),
      stats: stats, findings: findings, connections: connections,
      uncertainties: uncertainties, furtherLeads: further.slice(0, 5)
    };
  }
  function escHtml(s) {
    return String(s == null ? '' : s).replace(/&/g, '&amp;').replace(/</g, '&lt;')
      .replace(/>/g, '&gt;').replace(/"/g, '&quot;');
  }
  /* Plain-text structured report for AI chat answers (with markdown links). */
  function formatReport(rep) {
    var L = [];
    L.push('Search: "' + rep.query + '" (' + rep.mode + ')');
    L.push('Searched ' + rep.stats.dbsSearched + ' databases, ' +
      rep.stats.recordsExamined.toLocaleString() + ' index records examined, ' +
      rep.findings.length + ' findings.');
    if (rep.findings.length) {
      L.push('');
      L.push('FINDINGS');
      rep.findings.slice(0, 12).forEach(function (h, i) {
        L.push((i + 1) + '. ' + h.title + ' — ' + h.dbName + ' [' + h.sourceLabel + ']');
        if (h.excerpt) L.push('   ' + h.excerpt);
        L.push('   Open: ' + h.deepLink);
      });
    }
    if (rep.connections.length) {
      L.push('');
      L.push('CONNECTED RECORDS');
      rep.connections.slice(0, 6).forEach(function (h, i) {
        L.push((i + 1) + '. ' + h.title + ' — ' + h.dbName + ' (via "' + (h.via || '?') + '")');
        L.push('   Open: ' + h.deepLink);
      });
    }
    if (rep.uncertainties.length) {
      L.push('');
      L.push('LIMITS');
      rep.uncertainties.forEach(function (u) { L.push('- ' + u); });
    }
    if (rep.furtherLeads.length) {
      L.push('');
      L.push('WORTH CHECKING NEXT: ' + rep.furtherLeads.join('; '));
    }
    return L.join('\n');
  }

  /* ================= mode entry points ================= */
  function emitProgress(cb, upd) { try { if (cb) cb(upd); } catch (e) {} }
  function runSearch(query, mode, onProgress) {
    var cfg = CFG[mode] || CFG.quick;
    var qu = understandQuery(query);
    if (!qu.keywords.length && !qu.phrases.length)
      return Promise.resolve(buildReport(query, mode, qu,
        { dbsDiscovered: 0, dbsSearched: 0, dbsFailed: 0, recordsExamined: 0 }, [], []));
    var manifest, discovered, stats;
    emitProgress(onProgress, { pass: 1, passName: 'Discovery — ranking every database', done: 0, total: 1 });
    return loadManifest().then(function (m) {
      manifest = m;
      discovered = discoverDatabases(m, qu);
      var totalFetchable = (m.databases || []).filter(fetchableDb).length;
      stats = { dbsDiscovered: discovered.length, dbsTotal: totalFetchable,
        dbsSearched: 0, dbsFailed: 0, recordsExamined: 0, coverageCapped: false };
      var cands = discovered.slice(0, cfg.dbs);
      if (mode === 'exhaustive' && discovered.length > cfg.dbs) stats.coverageCapped = true;
      emitProgress(onProgress, { pass: 2, passName: 'Index search — scanning ' + cands.length + ' databases',
        done: 0, total: cands.length });
      return searchIndexes(cands, qu, { perDb: 5 }, function (p) {
        emitProgress(onProgress, { pass: 2, passName: 'Index search', done: p.dbsSearched, total: cands.length,
          recordsExamined: p.recordsExamined });
      });
    }).then(function (res) {
      stats.dbsSearched = res.dbsSearched;
      stats.dbsFailed = res.dbsFailed;
      stats.recordsExamined = res.recordsExamined;
      var hits = res.hits.slice(0, cfg.results);
      /* per-database diversity: no single database dominates the results */
      var perDbCap = mode === 'quick' ? 3 : 4, seenDb = {}, diverse = [];
      for (var di = 0; di < hits.length; di++) {
        var dh = hits[di];
        seenDb[dh.dbSlug] = seenDb[dh.dbSlug] || 0;
        if (seenDb[dh.dbSlug] < perDbCap) { seenDb[dh.dbSlug]++; diverse.push(dh); }
        if (diverse.length >= cfg.results) break;
      }
      hits = diverse;
      if (!cfg.retrieve || !hits.length) {
        emitProgress(onProgress, { pass: 6, passName: 'Report', done: 1, total: 1 });
        return buildReport(query, mode, qu, stats, hits, []);
      }
      emitProgress(onProgress, { pass: 3, passName: 'Record retrieval — opening top records', done: 0, total: hits.length });
      return retrieveRecords(hits, manifest, cfg.retrieve, function (p) {
        emitProgress(onProgress, { pass: 3, passName: 'Record retrieval', done: p.retrieved, total: p.of });
      }).then(function (enriched) {
        if (!cfg.connPasses) {
          emitProgress(onProgress, { pass: 6, passName: 'Report', done: 1, total: 1 });
          return buildReport(query, mode, qu, stats, enriched, []);
        }
        emitProgress(onProgress, { pass: 4, passName: 'Connection search — following references', done: 0, total: 1 });
        return connectionSearch(enriched, manifest, qu).then(function (conns) {
          emitProgress(onProgress, { pass: 5, passName: 'Verification', done: 1, total: 1 });
          emitProgress(onProgress, { pass: 6, passName: 'Report', done: 1, total: 1 });
          return buildReport(query, mode, qu, stats, enriched, conns);
        });
      });
    });
  }
  function quickSearch(query, onProgress) { return runSearch(query, 'quick', onProgress); }
  function deepSearch(query, onProgress) { return runSearch(query, 'deep', onProgress); }
  function exhaustiveSearch(query, onProgress) { return runSearch(query, 'exhaustive', onProgress); }

  /* ================= AI integration ================= */
  /* Runs a deep investigation and returns the formatted report text for chat. */
  function aiDeepSearch(db, userText, onProgress) {
    var q = String(userText || '')
      .replace(/\b(deep search|investigate|investigation|research|exhaustive search)\b/gi, ' ')
      .replace(/\b(all|every)( of)?( the)? databases?\b/gi, ' ')
      .replace(/[?.!]+$/g, '').replace(/\s+/g, ' ').trim();
    if (!q) return Promise.resolve('Tell me what to investigate and I will run a deep multi-pass search across the network — for example, "deep search solar panel efficiency".');
    return deepSearch(q, onProgress).then(function (rep) {
      return formatReport(rep);
    }).catch(function () {
      return 'That deep search hiccuped partway through. Try again, or narrow the question and I will run it again.';
    });
  }
  function deepSearchIntent(q) {
    var low = String(q || '').toLowerCase();
    return /\bdeep search\b/.test(low) || /\binvestigat/.test(low) ||
      /\bresearch\b/.test(low) || /\bexhaustive search\b/.test(low);
  }

  return {
    understand: understandQuery,
    discover: function (q) { return loadManifest().then(function (m) { return discoverDatabases(m, understandQuery(q)); }); },
    quickSearch: quickSearch, deepSearch: deepSearch, exhaustiveSearch: exhaustiveSearch,
    aiDeepSearch: aiDeepSearch, deepSearchIntent: deepSearchIntent,
    formatReport: formatReport, escHtml: escHtml, deepLinkFor: deepLinkFor,
    fetchableCount: function () { return loadManifest().then(function (m) { return (m.databases || []).filter(fetchableDb).length; }); }
  };
})();
