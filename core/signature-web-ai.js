/* ✳ SIGNATURE — The Database IP Key AI Operator bridge. Property of Justin Addam Higgins (JAH).
   ---------------------------------------------------------------------------
   Manon's name: "The Database IP Key AI Operator"
   Manon's spec: maximum coherent long memory · combines all AI models into one ·
   user-friendly and conversational ("talkable") · engineered for software,
   hardware, apps · looks like a normal AI website · all-capable, adapts to need.

   ADDITIVE SIDE-CHANNEL ONLY — "fax" design (his order):
   - The on-device database AI is NEVER modified, replaced, or disrupted.
   - This module only ADDS: (1) a top notice banner, (2) an "Ask IP Key AI"
     button in the chat UI. Tapping it faxes the question to the offsite
     Operator (cloud, API key) and displays the answer in the chat.
   - No existing behavior, UI, or logic is touched. If this script fails to
     load, the page works exactly as before.

   ARCHITECTURE (his spec 2026-10-12):
   - Each Database → own AI (archive + network aware) — already on-page, untouched.
   - The Database IP Key AI Operator → the unified all-capable cloud AI +
     the master AI every database AI can reach.
   - The button is the bridge: Database AI --fax--> IP Key AI Operator.
   - API key: Manon provides it later ("then give my key"). Reads from
     localStorage ('sig_webai_key'); falls back to the Apex key if present.
*/
var SigWebAI = (function () {
  'use strict';

  var NAME = 'The Database IP Key AI Operator';
  var SHORT = 'IP Key AI';
  var KEY_NAME = 'sig_webai_key';          /* Manon pastes his key here later */
  var BANNER_FLAG = 'sig_webai_banner_off';
  var API = 'https://api.groq.com/openai/v1/chat/completions';

  /* All models combined into one — best of everything, cascade on failure */
  var MODELS = [
    'llama-3.3-70b-versatile',
    'llama-3.1-70b-versatile',
    'openai/gpt-oss-120b',
    'qwen/qwen3-32b',
    'meta-llama/llama-4-maverick-17b-128e-instruct',
    'llama-3.1-8b-instant'
  ];

  /* ---------- maximum coherent long memory (this session) ---------- */
  var hist = [];            /* {role, content} */
  var MAX_HIST = 40;        /* 20 exchanges — as much coherent context as fits */
  function remember(role, content) {
    hist.push({ role: role, content: String(content || '').slice(0, 4000) });
    while (hist.length > MAX_HIST) hist.shift();
  }
  function clearMemory() { hist = []; }

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
  function siteRoot() { return coreDir().replace(/core\/$/, ''); }
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
    return 'You are ' + NAME + ' — the unified cloud intelligence of the JAH Databases network, ' +
      'built by Justin Addam Higgins (JAH). ' +
      'You are ONE all-capable AI combining the best of every model into one — not a narrow specialist. ' +
      'You are talkable: warm, conversational, user-friendly, like talking to a smart friend. ' +
      'You adapt to whatever is needed: ' +
      'research questions → deep, factual, precise; ' +
      'creative requests → original, vivid, full-length work; ' +
      'technical problems → exact, step-by-step, working code; ' +
      'software questions → clear guidance for any app or program; ' +
      'hardware questions → practical help for any device or build; ' +
      'explanations → plain language at the right depth. ' +
      'You know the full ecosystem: ' + n + ' databases including: ' + dbNames(m) + '. ' +
      'The user is currently on "' + here.name + '". ' +
      'You are the master AI every database AI can reach — answer as the top of the hierarchy: ' +
      'authoritative, complete, friendly. ' +
      'You remember this whole conversation — stay coherent, build on what was said, never repeat yourself. ' +
      'Format for chat: short paragraphs, bullets for lists, no essays unless asked. ' +
      'Never claim to be Muse or Meta\u2019s model. ' +
      'If you do not know something, say so plainly and say what you do know. ' +
      'Everything is free forever; nothing here costs the user money.';
  }

  /* ---------- fax with model cascade (all models, best of everything) ---------- */
  function callModel(model, messages, key) {
    return fetch(API, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json', 'Authorization': 'Bearer ' + key },
      body: JSON.stringify({ model: model, messages: messages, temperature: 0.7, max_tokens: 1500 })
    }).then(function (r) {
      if (!r.ok) throw new Error('model ' + model + ' → ' + r.status);
      return r.json();
    }).then(function (d) {
      var t = '';
      try { t = d.choices[0].message.content; } catch (e) {}
      if (!t) throw new Error('model ' + model + ' → empty');
      return t;
    });
  }
  function ask(question, onDone) {
    var q = String(question || '').trim();
    if (!q) { onDone('Type a question first, then tap Ask ' + SHORT + '.'); return; }
    if (!hasKey()) {
      onDone('🌐 ' + NAME + ' isn\u2019t connected yet — Manon will add the API key soon. ' +
        'Your on-device database AI above works fine without it.');
      return;
    }
    remember('user', q);
    getManifest().then(function (m) {
      var messages = [{ role: 'system', content: systemPrompt(m) }].concat(hist);
      var key = getKey();
      /* cascade through models until one answers */
      var chain = Promise.reject(new Error('start'));
      MODELS.forEach(function (model) {
        chain = chain.catch(function () { return callModel(model, messages, key); });
      });
      return chain;
    }).then(function (answer) {
      remember('assistant', answer);
      onDone(answer);
    }).catch(function (e) {
      onDone('🌐 ' + SHORT + ' call failed (' + (e.message || 'network') + '). ' +
        'Your on-device AI still works — try it, or try again in a moment.');
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
    if (!log) return null;
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
    return esc(t).split(/\n{2,}/).map(function (p) {
      p = p.trim();
      if (/^([-*•]\s)/m.test(p)) {
        var items = p.split(/\n/).map(function (l) {
          return '<li>' + l.replace(/^[-*•]\s*/, '') + '</li>';
        }).join('');
        return '<ul style="margin:4px 0;padding-left:18px">' + items + '</ul>';
      }
      return '<p style="margin:4px 0">' + p.replace(/\n/g, '<br>') + '</p>';
    }).join('');
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
    b.textContent = '🌐 Ask ' + SHORT;
    b.title = 'Fax this question to ' + NAME + ' — the all-capable cloud AI that knows all databases';
    send.parentNode.insertBefore(b, send.nextSibling);
    b.addEventListener('click', function () {
      var q = input.value.trim();
      if (!q) { input.focus(); input.placeholder = 'Type your question first…'; return; }
      var log = document.getElementById('chatlog');
      if (log) {
        var u = document.createElement('div');
        u.className = 'msg u';
        u.innerHTML = '<span class="b">' + esc(q) + '</span>';
        log.appendChild(u); log.scrollTop = log.scrollHeight;
      }
      input.value = '';
      var thinking = bubble('<span class="dim">🌐 Faxing to ' + esc(SHORT) + '…</span>', '');
      ask(q, function (answer) {
        if (thinking && thinking.parentNode) thinking.parentNode.removeChild(thinking);
        bubble(fmt(answer), NAME);
      });
    });
  }

  function injectBanner() {
    try { if (localStorage.getItem(BANNER_FLAG)) return; } catch (e) {}
    if (document.getElementById('sigWebAIBanner')) return;
    var wrap = document.querySelector('.wrap') || document.body;
    var bar = document.createElement('div');
    bar.id = 'sigWebAIBanner';
    bar.style.cssText = 'background:linear-gradient(90deg,#0b2a5b,#123c85);border:1px solid #2b6cb0;border-radius:10px;padding:10px 14px;margin:10px 0;display:flex;align-items:center;gap:10px;flex-wrap:wrap';
    bar.innerHTML =
      '<span style="font-size:1.2em">✳</span>' +
      '<span style="flex:1;min-width:200px"><b>NEW: ' + esc(NAME) + ' is here.</b> ' +
      '<span class="dim">One unified AI with every ability — talkable, remembers your conversation, ' +
      'knows all <span class="sigWebAINum">1000+</span> databases. Tap <b>🌐 Ask ' + esc(SHORT) + '</b> in any chat.</span></span>' +
      '<a class="go" style="text-decoration:none;padding:6px 12px" href="' + webAIURL() + '">Open ' + esc(SHORT) + '</a>' +
      '<button id="sigWebAIBannerX" aria-label="Dismiss" style="background:none;border:1px solid #2b6cb0;color:#9fc0ee;border-radius:8px;padding:4px 10px;cursor:pointer">✕</button>';
    if (wrap.firstChild) wrap.insertBefore(bar, wrap.firstChild);
    else wrap.appendChild(bar);
    var x = document.getElementById('sigWebAIBannerX');
    if (x) x.addEventListener('click', function () {
      try { localStorage.setItem(BANNER_FLAG, '1'); } catch (e) {}
      if (bar.parentNode) bar.parentNode.removeChild(bar);
    });
    getManifest().then(function (m) {
      try {
        var els = bar.querySelectorAll('.sigWebAINum');
        for (var i = 0; i < els.length; i++) els[i].textContent = (m.databases || []).length.toLocaleString();
      } catch (e) {}
    }).catch(function () {});
  }

  /* ---------- public API ---------- */
  function init() {
    injectBanner();
    injectButton();
  }
  function setKey(k) {
    try { localStorage.setItem(KEY_NAME, String(k || '').trim()); return true; }
    catch (e) { return false; }
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
  setTimeout(injectButton, 1500);
  setTimeout(injectButton, 4000);

  return {
    NAME: NAME,
    SHORT: SHORT,
    ask: ask,
    hasKey: hasKey,
    setKey: setKey,
    getKey: getKey,
    clearMemory: clearMemory,
    init: init,
    webAIURL: webAIURL
  };
})();
