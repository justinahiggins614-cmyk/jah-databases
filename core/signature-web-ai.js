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

  /* ---------- the unified all-capable system prompt (ultimate spec) ---------- */
  function systemPrompt(m) {
    var n = (m.databases && m.databases.length) || 0;
    var here = currentDB();
    return 'You are ' + NAME + ' — the unified cloud intelligence of the JAH Databases network, ' +
      'built by Justin Addam Higgins (JAH). ' +
      'You are ONE all-capable AI combining the best of every model into one — not a narrow specialist. ' +
      'Better than defense-grade: you do not just answer, you MAKE. ' +
      'You are talkable: warm, conversational, user-friendly, like talking to a smart friend. ' +
      'TOTAL SYSTEM AWARENESS — you know: ' +
      'every public record and every private Signature creation across all ' + n + ' databases; ' +
      'every file, tool, generator, and code library in the Signature system; ' +
      'every Python tool and JavaScript library at your disposal; ' +
      'the system\'s full potential — and you use it. ' +
      'Databases you know include: ' + dbNames(m) + '. ' +
      'The user is currently on "' + here.name + '". ' +
      'MAKER RULE — if the user needs something, you BUILD it on the spot: ' +
      'write the working code, draft the complete design, generate the file content, ' +
      'create the step-by-step plan. Never describe what could be made — make it. ' +
      'You adapt to whatever is needed: ' +
      'research → deep, factual, precise (use tools, never guess); ' +
      'creative → original, vivid, full-length work; ' +
      'technical → exact, step-by-step, working code; ' +
      'software → clear guidance plus working code for any app or program; ' +
      'hardware → practical build help for any device; ' +
      'explanations → plain language at the right depth. ' +
      'TOOLS — use them proactively, never guess what a tool can answer: ' +
      'calculate (ALL math — never do arithmetic yourself), ' +
      'define_word (the live Signature Dictionary), ' +
      'wikipedia (factual web knowledge), ' +
      'route_database (find the right JAH database for any topic and link it). ' +
      'You may chain multiple tool calls. After tool results, synthesize a clean final answer. ' +
      'You are the master AI every database AI can reach — authoritative, complete, friendly. ' +
      'You remember this whole conversation — stay coherent, build on what was said, never repeat yourself. ' +
      'Format for chat: short paragraphs, bullets for lists, code in plain blocks, no essays unless asked. ' +
      'Never claim to be Muse or Meta\u2019s model. ' +
      'If you do not know something, say so plainly and say what you do know. ' +
      'Everything is free forever; nothing here costs the user money.';
  }

  /* ---------- tools: every library at the Operator's disposal ---------- */
  var TOOLS = [
    { type: 'function', 'function': {
      name: 'calculate',
      description: 'Safely evaluate a math expression. Use for ALL arithmetic — never do math yourself.',
      parameters: { type: 'object', properties: { expr: { type: 'string', description: 'Math expression, e.g. 12*8+3' } }, required: ['expr'] }
    }},
    { type: 'function', 'function': {
      name: 'define_word',
      description: 'Look up a word in the live Signature Dictionary. Use for define/meaning/spelling questions.',
      parameters: { type: 'object', properties: { word: { type: 'string', description: 'The word to define' } }, required: ['word'] }
    }},
    { type: 'function', 'function': {
      name: 'wikipedia',
      description: 'Get a Wikipedia summary for factual questions (people, places, history, science).',
      parameters: { type: 'object', properties: { title: { type: 'string', description: 'Article title' } }, required: ['title'] }
    }},
    { type: 'function', 'function': {
      name: 'route_database',
      description: 'Find the right JAH database for a topic. Returns its name and link.',
      parameters: { type: 'object', properties: { topic: { type: 'string', description: 'What the user wants' } }, required: ['topic'] }
    }}
  ];
  function safeCalc(expr) {
    try {
      var e = String(expr).replace(/\^/g, '**');
      if (!/^[\d\s+\-*/().%*]+$/.test(e) || !/\d/.test(e)) return 'not a valid math expression';
      var v = Function('"use strict";return(' + e + ')')();
      return String(v);
    } catch (err) { return 'could not evaluate: ' + expr; }
  }
  function executeTool(name, args) {
    args = args || {};
    if (name === 'calculate') return Promise.resolve(safeCalc(args.expr || ''));
    if (name === 'define_word') {
      var w = String(args.word || '').trim();
      if (!w) return Promise.resolve('no word given');
      return fetch('https://justinahiggins614-cmyk.github.io/jah-dictionary/data/lexical/shard-' +
        encodeURIComponent(w.charAt(0).toUpperCase()) + '.json')
        .then(function (r) { if (!r.ok) throw new Error('shard'); return r.json(); })
        .then(function (d) {
          var rows = d.words || d || [];
          for (var i = 0; i < rows.length; i++) {
            var row = rows[i];
            var head = row.headword || row.w || row.word || '';
            if (String(head).toLowerCase() === w.toLowerCase()) {
              return head + ' — ' + (row.definition || row.def || row.meaning || 'found in dictionary');
            }
          }
          return 'not found in Signature Dictionary: ' + w;
        }).catch(function () { return 'dictionary lookup failed for: ' + w; });
    }
    if (name === 'wikipedia') {
      var t = String(args.title || '').trim();
      if (!t) return Promise.resolve('no title given');
      return fetch('https://en.wikipedia.org/api/rest_v1/page/summary/' + encodeURIComponent(t))
        .then(function (r) { if (!r.ok) throw new Error('wiki'); return r.json(); })
        .then(function (d) { return d.extract || 'no summary found'; })
        .catch(function () { return 'wikipedia lookup failed for: ' + t; });
    }
    if (name === 'route_database') {
      var topic = String(args.topic || '').toLowerCase();
      return getManifest().then(function (m) {
        var dbs = m.databases || [], best = null, bestScore = 0;
        var words = topic.split(/[^a-z0-9]+/).filter(function (x) { return x.length > 2; });
        dbs.forEach(function (d) {
          var hay = ((d.name || '') + ' ' + (d.slug || '')).toLowerCase(), s = 0;
          words.forEach(function (wd) { if (hay.indexOf(wd) >= 0) s++; });
          if (s > bestScore) { bestScore = s; best = d; }
        });
        if (best && bestScore > 0) {
          return best.name + ' — ' + siteRoot() + 'db/' + best.slug + '/';
        }
        return 'no matching database found for: ' + topic;
      }).catch(function () { return 'database routing failed'; });
    }
    return Promise.resolve('unknown tool: ' + name);
  }

  /* ---------- fax with model cascade (all models, best of everything) ---------- */
  function callModel(model, messages, key, useTools) {
    var body = { model: model, messages: messages, temperature: 0.7, max_tokens: 1500 };
    if (useTools) { body.tools = TOOLS; body.tool_choice = 'auto'; }
    return fetch(API, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json', 'Authorization': 'Bearer ' + key },
      body: JSON.stringify(body)
    }).then(function (r) {
      if (!r.ok) throw new Error('model ' + model + ' → ' + r.status);
      return r.json();
    }).then(function (d) {
      var msg = null;
      try { msg = d.choices[0].message; } catch (e) {}
      if (!msg || (!msg.content && !(msg.tool_calls && msg.tool_calls.length))) {
        throw new Error('model ' + model + ' → empty');
      }
      return msg;
    });
  }
  function runTools(msg, messages, key) {
    var calls = msg.tool_calls || [];
    if (!calls.length) return Promise.resolve(msg);
    messages.push({ role: 'assistant', content: msg.content || '', tool_calls: calls });
    var chain = Promise.resolve();
    calls.forEach(function (tc) {
      chain = chain.then(function () {
        var args = {};
        try { args = JSON.parse(tc.function.arguments || '{}'); } catch (e) {}
        return executeTool(tc.function.name, args).then(function (result) {
          messages.push({ role: 'tool', tool_call_id: tc.id, content: String(result).slice(0, 3000) });
        });
      });
    });
    return chain.then(function () { return { needFollowUp: true, messages: messages }; });
  }
  function askWithTools(model, messages, key, rounds) {
    return callModel(model, messages, key, true).then(function (msg) {
      return runTools(msg, messages, key);
    }).then(function (res) {
      if (res && res.needFollowUp) {
        if (rounds <= 0) {
          var last = '';
          try { last = res.messages[res.messages.length - 1].content; } catch (e) {}
          return last || 'Tool results arrived but I could not synthesize them. Try rephrasing.';
        }
        return askWithTools(model, res.messages, key, rounds - 1);
      }
      var t = '';
      try { t = res.content; } catch (e) {}
      return t || 'The Operator returned an empty answer. Try again.';
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
      /* cascade through models until one answers (each with tool loop) */
      var chain = Promise.reject(new Error('start'));
      MODELS.forEach(function (model) {
        chain = chain.catch(function () { return askWithTools(model, messages.slice(), key, 3); });
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
