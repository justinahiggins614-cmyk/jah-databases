/* ✳ SIGNATURE — Per-File AI + Boundless Alternatives. Property of Justin Addam Higgins (JAH).
   ---------------------------------------------------------------------------
   Manon's architecture (2026-10-12): each File has its own AI — aware of the
   ITEM, the DATABASE, and the SYSTEM. This module adds that AI to every full
   record view, ADDITIVELY:

   1. "Ask about this file" — per-file Q&A. The file's AI answers from the
      record itself (item-aware), names its database (database-aware), and
      knows the network (system-aware). It never invents record facts.
   2. "Alternatives A1 A2 A3…" — boundless alternatives. A1 is the file as
      made; A2+ swap out components or restrict the design to find
      workarounds. "Generate next" keeps scaling until one works or fits.
   3. Each alternative carries its internal rank (JAHDBRank).

   The database-level AI chat is NEVER touched. If this script fails, the
   page works exactly as before.
 */
(function () {
  'use strict';
  if (typeof document === 'undefined') return;

  var SLUG = null, DBNAME = '', AI_NAME = '';
  try {
    SLUG = (typeof window !== 'undefined' && window.SLUG) || null;
    /* Fall back: derive slug from URL path /db/<slug>/. */
    if (!SLUG) {
      var m = String(location.pathname).match(/\/db\/([^\/]+)\//);
      if (m) SLUG = m[1];
    }
  } catch (e) {}

  function esc(s) {
    return String(s == null ? '' : s).replace(/[&<>"]/g, function (c) {
      return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c];
    });
  }
  function idOf(r) { return String(r.id || r.api_id || r.record_id || 'rec'); }
  function titleOf(r) {
    return r.title || r.name || r.signature_name || r.label || r.display_name || idOf(r);
  }

  /* ---------- per-file AI: answer from the record ---------- */
  function fileAnswer(rec, q) {
    var t = String(q || '').toLowerCase();
    var title = titleOf(rec), id = idOf(rec);
    var keys = Object.keys(rec).filter(function (k) { return k.charAt(0) !== '_' && k !== 'demo'; });

    /* Alternative requests → generate, don't just talk. */
    if (/(alternative|another version|a2|a3|different way|other way)/.test(t))
      return { action: 'alt-next' };
    if (/(simpler|simplify|restrict|minimal|strip)/.test(t))
      return { action: 'alt-strategy', strategy: 'restrict' };
    if (/(workaround|work around|fix it|make it work|defensive)/.test(t))
      return { action: 'alt-strategy', strategy: 'workaround' };
    if (/(swap|different design|rebuild)/.test(t))
      return { action: 'alt-strategy', strategy: 'swap' };
    if (/(rank|score|how good|quality)/.test(t)) {
      var rk = rankOf(rec);
      return { text: 'This file ranks ' + rk.score + '/100 — tier ' + rk.tier + '. ' +
        (rk.score >= 75 ? 'Strong: it runs clean and is well documented.' :
         rk.score >= 60 ? 'Decent: it works, with room to tighten.' :
         'It needs work — try an alternative below; A2 onward are built to score higher.') };
    }
    if (/(what is|describe|explain|tell me about)/.test(t)) {
      var bits = keys.slice(0, 6).map(function (k) {
        var v = rec[k], s = Array.isArray(v) ? v.length + ' items' : String(v);
        return k + ': ' + s.slice(0, 140);
      });
      return { text: title + ' (' + id + ') — ' + bits.join(' · ') + '. Ask me for an alternative version any time.' };
    }
    if (/(how.*work|how.*run|run it|demo)/.test(t)) {
      var d = rec.demo;
      if (d && d.program)
        return { text: 'It ships a runnable ' + (d.language || 'javascript') + ' program (' + (d.kind || 'demo') + '). ' +
          'Open the Alternatives panel below and press Run on A1 — or ask me for a simpler or workaround version.' };
      return { text: 'This file has no runnable demo yet — its ' + keys.length + ' fields are the content. The generator can build one.' };
    }
    if (/(who made|whose|owner)/.test(t))
      return { text: 'Property of Justin Addam Higgins — Signature system file ' + id + '.' };
    return { text: 'I am the AI for this file — ' + title + '. I know this item, its database, and the network. ' +
      'Ask me what it is, how it runs, how it ranks, or say "alternative" and I will generate the next version (A2, A3…) until one fits.' };
  }

  function rankOf(rec) {
    try {
      var R = window.JAHDBRank;
      if (R && rec.demo && rec.demo.program) return R.scoreDemo(rec.demo);
      if (R) return R.scoreRecord(rec);
    } catch (e) {}
    return { score: 50, tier: 'C' };
  }

  /* ---------- alternatives state per record ---------- */
  var altState = {}; /* recId -> {n, list:[alt...]} */
  function getAlts(rec) {
    var id = idOf(rec);
    if (!altState[id]) {
      var A = window.JAHDBAlt;
      var a1 = A ? A.alternative(SLUG, rec, 1) : { alt_id: 'A1', strategy: 'original', title: titleOf(rec), program: '' };
      try { a1.rank = A.rankAlternative(a1); } catch (e) { a1.rank = { score: 50, tier: 'C' }; }
      altState[id] = { n: 1, list: [a1] };
    }
    return altState[id];
  }
  function nextAlt(rec, forceStrategy) {
    var st = getAlts(rec), A = window.JAHDBAlt;
    var n = st.n + 1, alt;
    if (forceStrategy && A) {
      /* Generate with a forced strategy: find the next n using it. */
      var tries = 0;
      do { n++; tries++; alt = A.alternative(SLUG, rec, n); }
      while (alt.strategy !== forceStrategy && tries < 12);
      st.n = n;
    } else {
      st.n = n;
      alt = A ? A.alternative(SLUG, rec, n) : { alt_id: 'A' + n, strategy: '?', title: titleOf(rec), program: '' };
    }
    try { alt.rank = A.rankAlternative(alt); } catch (e) { alt.rank = { score: 50, tier: 'C' }; }
    st.list.push(alt);
    return alt;
  }

  /* ---------- UI injection ---------- */
  function panelHTML(rec) {
    var id = idOf(rec);
    return '<div class="card" id="fileai-panel" style="margin-top:12px">' +
      '<h3 style="margin:.2em 0">✳ File AI — ask about this file</h3>' +
      '<p class="dim" style="margin:.2em 0">Aware of this item, its database, and the network. Say <b>alternative</b> for the next version.</p>' +
      '<div class="chatlog" id="fileai-log" style="max-height:30vh"></div>' +
      '<div class="row"><input id="fileai-in" placeholder="Ask about this file…" style="flex:1;min-width:180px">' +
      '<button class="go" id="fileai-go">Send</button></div>' +
      '<h3 style="margin:.8em 0 .2em">Alternatives <span class="dim">A1 · A2 · A3… — boundless</span></h3>' +
      '<div id="fileai-alts"></div>' +
      '<div class="row" style="margin-top:8px">' +
      '<button class="go" id="fileai-next">Generate next alternative ⤢</button>' +
      '<span class="dim" id="fileai-note">A1 is the file as made.</span></div>' +
      '</div>';
  }

  function altCard(a) {
    var r = a.rank || { score: '?', tier: '?' };
    return '<div class="card" style="margin:8px 0;padding:10px">' +
      '<div class="row" style="justify-content:space-between;flex-wrap:wrap">' +
      '<span><b class="mono">' + esc(a.alt_id) + '</b> <span class="badge">' + esc(a.strategy) + '</span> ' +
      '<span class="badge ' + (r.tier === 'S' || r.tier === 'A' ? 'ok' : '') + '">rank ' + esc(String(r.score)) + ' · ' + esc(String(r.tier)) + '</span></span>' +
      '<span class="row"><button class="go" data-altrun="' + esc(a.alt_id) + '">Run</button>' +
      '<button data-altcopy="' + esc(a.alt_id) + '">Copy</button></span></div>' +
      '<div style="font-size:.95em;margin:4px 0">' + esc(a.title || '') + '</div>' +
      (a.note ? '<div class="dim" style="font-size:.88em">' + esc(a.note) + '</div>' : '') +
      '<details><summary class="dim" style="cursor:pointer">program</summary>' +
      '<pre class="mono" style="max-height:220px;overflow:auto;font-size:.8em;background:#060a14;padding:8px;border-radius:8px">' +
      esc(String(a.program || '').slice(0, 6000)) + '</pre></details>' +
      '<div class="mono dim" data-altout="' + esc(a.alt_id) + '" style="font-size:.82em;margin-top:6px;white-space:pre-wrap"></div>' +
      '</div>';
  }

  function renderAlts(rec) {
    var box = document.getElementById('fileai-alts');
    if (!box) return;
    var st = getAlts(rec);
    box.innerHTML = st.list.map(altCard).join('');
    var note = document.getElementById('fileai-note');
    if (note) {
      var best = st.list.reduce(function (b, a) { return (a.rank && b.rank && a.rank.score > b.rank.score) ? a : b; }, st.list[0]);
      note.textContent = st.list.length + ' versions · best: ' + best.alt_id + ' (' + (best.rank ? best.rank.score : '?') + '/100)';
    }
  }

  function say(who, text) {
    var log = document.getElementById('fileai-log');
    if (!log) return;
    var d = document.createElement('div');
    d.style.cssText = 'margin:6px 0;display:flex;' + (who === 'u' ? 'justify-content:flex-end' : 'justify-content:flex-start');
    d.innerHTML = '<div style="max-width:88%;padding:8px 12px;border-radius:12px;' +
      (who === 'u' ? 'background:#12325e' : 'background:#0d1526;border:1px solid var(--line)') + '">' +
      esc(text) + '</div>';
    log.appendChild(d); log.scrollTop = log.scrollHeight;
  }

  function curRec() {
    try { if (window.CUR_FULL) return window.CUR_FULL; } catch (e) {}
    return null;
  }

  function onSend() {
    var inp = document.getElementById('fileai-in');
    var rec = curRec();
    if (!inp || !rec) return;
    var q = inp.value.trim();
    if (!q) return;
    inp.value = ''; say('u', q);
    var ans = fileAnswer(rec, q);
    if (ans.action === 'alt-next' || ans.action === 'alt-strategy') {
      var alt = nextAlt(rec, ans.action === 'alt-strategy' ? ans.strategy : null);
      say('a', 'Generated ' + alt.alt_id + ' (' + alt.strategy + ', rank ' +
        (alt.rank ? alt.rank.score : '?') + '/100). See the Alternatives panel — press Run to try it.');
      renderAlts(rec);
    } else say('a', ans.text);
  }

  function runAlt(rec, altId) {
    var st = getAlts(rec);
    var alt = st.list.filter(function (a) { return a.alt_id === altId; })[0];
    var out = document.querySelector('[data-altout="' + altId + '"]');
    if (!alt || !out) return;
    out.textContent = 'running…';
    try {
      var logs = [];
      var fn = new Function('console', '"use strict";\n' + String(alt.program || ''));
      fn({ log: function () { logs.push([].map.call(arguments, String).join(' ')); if (logs.length > 60) throw new Error('output cap'); } });
      out.textContent = logs.length ? logs.join('\n').slice(0, 2000) : '(ran clean — no output)';
    } catch (e) { out.textContent = 'error: ' + String(e.message).slice(0, 300); }
  }

  function inject(rec) {
    if (document.getElementById('fileai-panel')) return;
    var fv = document.getElementById('fullview');
    if (!fv || !fv.firstChild) return;
    var wrap = document.createElement('div');
    wrap.innerHTML = panelHTML(rec);
    fv.appendChild(wrap.firstChild);
    renderAlts(rec);
    say('a', 'I am this file\u2019s AI — ' + titleOf(rec) + '. Ask me anything about it, or say "alternative" and I\u2019ll build the next version.');
    document.getElementById('fileai-go').addEventListener('click', onSend);
    document.getElementById('fileai-in').addEventListener('keydown', function (e) { if (e.key === 'Enter') onSend(); });
    document.getElementById('fileai-next').addEventListener('click', function () {
      var alt = nextAlt(rec, null);
      say('a', 'Generated ' + alt.alt_id + ' (' + alt.strategy + ', rank ' +
        (alt.rank ? alt.rank.score : '?') + '/100). Scaling continues — ask again any time.');
      renderAlts(rec);
    });
    fv.addEventListener('click', function (e) {
      var t = e.target;
      var rid = t && t.getAttribute && (t.getAttribute('data-altrun') || t.getAttribute('data-altcopy'));
      if (!rid) return;
      var st = getAlts(rec);
      var alt = st.list.filter(function (a) { return a.alt_id === rid; })[0];
      if (!alt) return;
      if (t.getAttribute('data-altrun')) runAlt(rec, rid);
      else if (navigator.clipboard) navigator.clipboard.writeText(String(alt.program || ''));
    });
  }

  /* Watch for full-record renders; inject once per view. */
  function watch() {
    var fv = document.getElementById('fullview');
    if (!fv) { setTimeout(watch, 1500); return; }
    var lastId = null;
    new MutationObserver(function () {
      try {
        var rec = curRec();
        if (rec && fv.firstChild && idOf(rec) !== lastId) {
          lastId = idOf(rec);
          /* Small delay: let renderFull finish. */
          setTimeout(function () { inject(rec); }, 60);
        }
        if (!fv.firstChild) lastId = null;
      } catch (e) {}
    }).observe(fv, { childList: true });
  }

  /* Load rank + alt engines, then watch. Purely additive. */
  function boot() {
    try {
      var scripts = document.getElementsByTagName('script'), base = null;
      for (var i = 0; i < scripts.length; i++) {
        var s = scripts[i].src || '';
        if (/core\/guide-conv\.js/.test(s)) { base = s.replace(/guide-conv\.js.*$/, ''); break; }
      }
      if (!base) return;
      var need = ['jahdb-rank.js', 'jahdb-alt.js'], loaded = 0;
      need.forEach(function (f) {
        var el = document.createElement('script');
        el.src = base + f; el.defer = true;
        el.onload = el.onerror = function () { if (++loaded === need.length) watch(); };
        document.head.appendChild(el);
      });
    } catch (e) {}
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', boot);
  else boot();
})();
