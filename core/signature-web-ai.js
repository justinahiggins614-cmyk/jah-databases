/* ✳ SIGNATURE — Signature Web AI bridge. Property of Justin Addam Higgins (JAH).
   ---------------------------------------------------------------------------
   ADDITIVE SIDE-CHANNEL ONLY — "fax" design (Manon's order):
   - The on-device database AI is NEVER modified, replaced, or disrupted.
   - This module only ADDS: (1) a top notice banner, (2) an "Ask Signature Web AI"
     button in the chat UI. Tapping it faxes the question to the offsite
     Signature Web AI (cloud, API key) and displays the answer in the chat.
   - No existing behavior, UI, or logic is touched. If this script fails to
     load, the page works exactly as before.

   ARCHITECTURE (his spec 2026-10-12):
   - Each Database → own AI (archive + network aware) — already on-page, untouched.
   - Signature Web AI → the unified all-capable cloud AI (ONE ai, all abilities,
     adapts to need) + the master AI every database AI can reach.
   - The button is the bridge: Database AI --fax--> Signature Web AI.
   - API key: Manon provides it later ("then give my key"). This module reads it
     from localStorage ('sig_webai_key'); falls back to the Apex key if present.
     With no key it says so plainly and changes nothing else.
*/
var SigWebAI = (function () {
  'use strict';

  var KEY_NAME = 'sig_webai_key';          /* Manon pastes his key here later */
  var BANNER_FLAG = 'sig_webai_banner_off';
  var API = 'https://api.groq.com/openai/v1/chat/completions';
  var MODEL = 'llama-3.3-70b-versatile';

  /* ---------- paths (this file lives in core/, pages live in db/<slug>/) ---------- */
  function coreDir() {
    try {
      var scripts = document.getElementsByTagName('script');
      for (var i = scripts.length - 1; i >= 0; i--) {
        var s = scripts[i].src || '';
        if (/core\/signature-web-ai\.js/.test(s)) return s.replace(/signature-web-ai\.js.*$/, '');
      }
    } catch (e) {}
    return '../../core/';
  }
  function siteRoot() { return coreDir().replace(/core\/$/, ''); } /* repo root */
  function manifestURL() { return siteRoot() + 'data/manifest.json'; }
  function webAIURL() { return siteRoot() + 'web-ai/'; }

  /* ---------- key ---------- */
  function getKey() {
    try {
      var k = (localStorage.getItem(KEY_NAME) || '').trim();
      if (k) return k;
      if (typeof ApexAI !== 'undefined' && ApexAI.key) {
        var a = (ApexAI.key() || '').trim();
        if (a) return a;
      }
    } catch (e) {}
    return '';
  }
  function hasKey() { return !!getKey(); }

  /* ---------- ecosystem context (cached) ---------- */
  var manifestCache = null;
  function getManifest() {
    if (manifestCache) return Promise.resolve(manifestCache);
    return fetch(manifestURL()).then(function (r) {
      if (!r.ok) throw new Error('manifest ' + r.status);
      return r.json();
    }).then(function (m) { manifestCache = m; return m; });
  }
  function dbNames(m, limit) {
    try {
      var names = (m.databases || []).map(function (d) { return d.name; }).filter(Boolean);
      limit = limit || 120;
      return names.slice(0, limit).join('; ') + (names.length > limit ? '; …and ' + (names.length - limit) + ' more' : '');
    } catch (e) { return ''; }
  }
  function currentDB() {
    /* pages define var db={...} inside an IIFE (not global) — match via URL slug */
    try {
      var m = location.pathname.match(/\/db\/([^\/]+)\//);
      if (m && manifestCache) {
        var dbs = manifestCache.databases || [];
        for (var i = 0; i < dbs.length; i++) {
          if (dbs[i].slug === m[1]) return dbs[i];
        }
      }
      if (m) return { slug: m[1], name: m[1].replace(/-/g, ' ') };
    } catch (e) {}
    try {
      var meta = document.querySelector('meta[property="og:title"]');
      if (meta) return { name: meta.content };
    } catch (e2) {}
    return { name: 'a JAH Database' };
  }

  /* ---------- the unified all-capable system prompt ---------- */
  function systemPrompt(m) {
    var n = (m.databases && m.databases.length) || 0;
    var here = currentDB();
    return 'You are Signature Web AI — the unified cloud intelligence of the JAH Databases network, ' +
      'built by Justin Addam Higgins (JAH). You are ONE all-capable AI, not a narrow specialist: ' +
      'you adapt to whatever is needed. ' +
      'Research questions → deep, factual, precise. ' +
      'Creative requests → original, vivid, full-length work. ' +
      'Technical problems → exact, step-by-step, working code. ' +
      'Explanations → clear plain language at the right depth. ' +
      'Cross-database questions → draw on the whole network. ' +
      'You know the full ecosystem: ' + n + ' databases including: ' + dbNames(m) + '. ' +
      'The user is currently on "' + here.name + '". ' +
      'You are the master AI every database AI can fax questions to — answer as the top of the hierarchy: ' +
      'authoritative, complete, warm. ' +
      'Format for chat: short paragraphs, bullets for lists, no essays unless asked. ' +
      'Never claim to be Muse or Meta\u2019s model. ' +
      'If you do not know something, say so plainly and say what you do know. ' +
      'Everything is free forever; nothing here costs the user money.';
  }

  /* ---------- fax: send question, get answer ---------- */
  function ask(question, onDone) {
    var q = String(question || '').trim();
    if (!q) { onDone('Type a question first, then tap Ask Web AI.'); return; }
    if (!hasKey()) {
      onDone('🌐 Signature Web AI isn\u2019t connected yet — Manon will add the API key soon. ' +
        'Your on-device database AI above works fine without it.');
      return;
    }
    getManifest().then(function (m) {
      var body = {
        model: MODEL,
        messages: [
          { role: 'system', content: systemPrompt(m) },
          { role: 'user', content: q }
        ],
        temperature: 0.7,
        max_tokens: 1200
      };
      return fetch(API, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json', 'Authorization': 'Bearer ' + getKey() },
        body: JSON.stringify(body)
      });
    }).then(function (r) {
      if (!r.ok) throw new Error('webai ' + r.status);
      return r.json();
    }).then(function (d) {
      var t = '';
      try { t = d.choices[0].message.content; } catch (e) {}
      onDone(t || 'The Web AI returned an empty answer. Try again.');
    }).catch(function (e) {
      onDone('🌐 Web AI call failed (' + (e.message || 'network') + '). Your on-device AI still works — try it, or try the Web AI again in a moment.');
    });
  }

  /* ---------- chat rendering (own renderer — never touches page say()) ---------- */
  function esc(s) {
    return String(s == null ? '' : s).replace(/[&<>"]/g, function (c) {
      return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c];
    });
  }
  function bubble(html, label) {
    var log = document.getElementById('chatlog');
    if (!log) return;
    var d = document.createElement('div');
    d.className = 'msg a';
    d.innerHTML = '<span class="b" style="border:1px solid #2b6cb0">' +
      (label ? '<div style="font-size:.78em;color:#7fb3ff;margin-bottom:4px">🌐 ' + esc(label) + '</div>' : '') +
      html + '</span>';
    log.appendChild(d);
    log.scrollTop = log.scrollHeight;
    return d;
  }
  function fmt(t) {
    /* light markdown: paragraphs + bullets, escaped */
    var parts = esc(t).split(/\n{2,}/).map(function (p) {
      p = p.trim();
      if (/^([-*•]\s)/m.test(p)) {
        var items = p.split(/\n/).map(function (l) {
          return '<li>' + l.replace(/^[-*•]\s*/, '') + '</li>';
        }).join('');
        return '<ul style="margin:4px 0;padding-left:18px">' + items + '</ul>';
      }
      return '<p style="margin:4px 0">' + p.replace(/\n/g, '<br>') + '</p>';
    });
    return parts.join('');
  }

  /* ---------- UI injection (additive only) ---------- */
  function injectButton() {
    var send = document.getElementById('chatGo');
    var input = document.getElementById('chatIn');
    if (!send || !input || document.getElementById('sigWebAIBtn')) return;
    var b = document.createElement('button');
    b.id = 'sigWebAIBtn';
    b.className = 'go';
    b.type = 'button';
    b.style.marginLeft = '6px';
    b.textContent = '🌐 Ask Web AI';
    b.title = 'Fax this question to Signature Web AI — the all-capable cloud AI that knows all databases';
    send.parentNode.insertBefore(b, send.nextSibling);
    b.addEventListener('click', function () {
      var q = input.value.trim();
      if (!q) { input.focus(); input.placeholder = 'Type your question first…'; return; }
      /* echo the question as the user, then fax it */
      var log = document.getElementById('chatlog');
      if (log) {
        var u = document.createElement('div');
        u.className = 'msg u';
        u.innerHTML = '<span class="b">' + esc(q) + '</span>';
        log.appendChild(u); log.scrollTop = log.scrollHeight;
      }
      input.value = '';
      var thinking = bubble('<span class="dim">🌐 Faxing to Signature Web AI…</span>', '');
      ask(q, function (answer) {
        if (thinking && thinking.parentNode) thinking.parentNode.removeChild(thinking);
        bubble(fmt(answer), 'Signature Web AI');
      });
    });
  }

  function injectBanner() {
    try { if (localStorage.getItem(BANNER_FLAG)) return; } catch (e) {}
    if (document.getElementById('sigWebAIBanner')) return;
    var wrap = document.querySelector('.wrap') || document.body;
    var n = 0;
    try { n = (manifestCache && manifestCache.databases && manifestCache.databases.length) || 0; } catch (e) {}
    var bar = document.createElement('div');
    bar.id = 'sigWebAIBanner';
    bar.style.cssText = 'background:linear-gradient(90deg,#0b2a5b,#123c85);border:1px solid #2b6cb0;border-radius:10px;padding:10px 14px;margin:10px 0;display:flex;align-items:center;gap:10px;flex-wrap:wrap';
    bar.innerHTML =
      '<span style="font-size:1.2em">✳</span>' +
      '<span style="flex:1;min-width:200px"><b>NEW: Signature Web AI is here.</b> ' +
      '<span class="dim">Every database AI can now fax hard questions to the all-capable cloud AI that knows all ' +
      (n || '1000+') + ' databases. Tap <b>🌐 Ask Web AI</b> in any chat.</span></span>' +
      '<a class="go" style="text-decoration:none;padding:6px 12px" href="' + webAIURL() + '">Visit Web AI</a>' +
      '<button id="sigWebAIBannerX" aria-label="Dismiss" style="background:none;border:1px solid #2b6cb0;color:#9fc0ee;border-radius:8px;padding:4px 10px;cursor:pointer">✕</button>';
    if (wrap.firstChild) wrap.insertBefore(bar, wrap.firstChild);
    else wrap.appendChild(bar);
    var x = document.getElementById('sigWebAIBannerX');
    if (x) x.addEventListener('click', function () {
      try { localStorage.setItem(BANNER_FLAG, '1'); } catch (e) {}
      if (bar.parentNode) bar.parentNode.removeChild(bar);
    });
    /* refresh the count once the manifest loads */
    getManifest().then(function (m) {
      try {
        var c = (m.databases || []).length;
        bar.innerHTML = bar.innerHTML.replace(/all \d+|all 1000\+/, 'all ' + c);
      } catch (e) {}
    }).catch(function () {});
  }

  /* ---------- public API ---------- */
  function init() {
    injectBanner();
    injectButton();
  }

  /* key management for the Web AI site / future settings UI */
  function setKey(k) {
    try { localStorage.setItem(KEY_NAME, String(k || '').trim()); return true; }
    catch (e) { return false; }
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
  /* re-try button injection late (some pages build chat UI after load) */
  setTimeout(injectButton, 1500);
  setTimeout(injectButton, 4000);

  return {
    ask: ask,
    hasKey: hasKey,
    setKey: setKey,
    getKey: getKey,
    init: init,
    webAIURL: webAIURL
  };
})();
