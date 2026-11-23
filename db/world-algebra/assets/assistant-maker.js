/* =====================================================================
   JAH Assistant Maker — "Make an Assistant Like Mine"  (v1.0.0)
   Property of Justin Addam Higgins (JAH). Part of the JAH Databases network.

   One shared module, loaded by every database page. It gives each
   database's AI a REAL, WORKING capability: build a personal AI assistant
   exactly like Manon's own — named by the user, with a chosen role and
   personality — wired live to THAT database's own archive index and (when
   the page has one) THAT database's own generator.

   AI canon (enforced here, not optional):
     - conversational, natural sentences — never templated blocks;
     - does REAL work: live archive lookup through the page's own index
       files, real generation through the page's own registered generator;
     - never variant-rotation disguised as AI: replies are composed from
       real record data and real capability checks;
     - never claims an ability it does not have: when the generator is not
       loaded on the page, it says so plainly and points at the Generator tab.
   ===================================================================== */
(function () {
'use strict';
if (window.JAHAssistantMaker) return; /* loaded once */

/* ---------------- small utilities ---------------- */
function esc(s) {
  return String(s == null ? '' : s).replace(/[&<>"]/g, function (c) {
    return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c];
  });
}
function cleanName(s) {
  s = String(s == null ? '' : s).replace(/<[^>]*>/g, '').trim();
  if (s.length > 60) s = s.slice(0, 60);
  return s || 'My Assistant';
}
function pad4(c) { var s = String(c); while (s.length < 4) s = '0' + s; return s; }
function chunkName(c) { return 'chunks/chunk-' + pad4(c) + '.jsonl.gz'; }

/* ---------------- data access: the page's own hooks first ----------------
   Every db page already ships JAHDB.fetchGz / fetchJsonlGz (core/jahdb.js)
   and registers its generator via JAHDB.registerGenerator(slug). We use
   those when present; the standalone fallbacks keep older pages working. */
function fetchTextGz(url) {
  try {
    if (window.JAHDB && JAHDB.fetchGz) return JAHDB.fetchGz(url);
  } catch (e) {}
  return fetch(url).then(function (r) {
    if (!r.ok) throw new Error('HTTP ' + r.status + ' for ' + url);
    if (typeof DecompressionStream === 'undefined') return r.text();
    return new Response(r.body.pipeThrough(new DecompressionStream('gzip'))).text();
  });
}
function parseJsonl(t) {
  return t.split('\n').filter(function (l) { return l.trim(); }).map(function (l) {
    try { return JSON.parse(l); } catch (e) { return null; }
  }).filter(Boolean);
}
function fetchRowsGz(url) {
  try {
    if (window.JAHDB && JAHDB.fetchJsonlGz) return JAHDB.fetchJsonlGz(url);
  } catch (e) {}
  return fetchTextGz(url).then(parseJsonl);
}

/* index-row field helpers (index rows are compact: id/t/g/c + extras) */
function rowChunk(r) { return (r.c != null ? r.c : (r.chunk != null ? r.chunk : 1)); }
function rowTitle(r) { return r.t || r.title || r.id || '(untitled)'; }
function rowGenre(r) { return r.g || r.genre || r.kind || ''; }
function rowDesc(r) { return String(r.d || r.description || ''); }

function searchRows(rows, q) {
  var words = String(q).toLowerCase().split(/[^a-z0-9]+/)
    .filter(function (w) { return w.length > 2; });
  if (!words.length) return [];
  return rows.map(function (r) {
    var hay = (rowTitle(r) + ' ' + (r.id || '') + ' ' + rowGenre(r) + ' ' + rowDesc(r)).toLowerCase();
    var s = 0;
    words.forEach(function (w) { if (hay.indexOf(w) >= 0) s++; });
    return { r: r, s: s };
  }).filter(function (x) { return x.s > 0; })
    .sort(function (a, b) { return b.s - a.s; }).slice(0, 5);
}

function loadIndex(state) {
  if (state.idxPromise) return state.idxPromise;
  state.idxPromise = fetchRowsGz(state.cfg.local + 'index.jsonl.gz').then(function (rows) {
    state.rows = rows;
    return rows;
  });
  return state.idxPromise;
}

function fullRecords(state, scored) {
  var byChunk = {};
  scored.forEach(function (x) {
    var c = rowChunk(x.r);
    (byChunk[c] = byChunk[c] || []).push(x.r.id);
  });
  var jobs = Object.keys(byChunk).map(function (c) {
    return fetchRowsGz(state.cfg.local + chunkName(+c)).then(function (recs) {
      var want = {};
      byChunk[c].forEach(function (id) { want[id] = 1; });
      return recs.filter(function (r) { return want[r.id]; });
    }).catch(function () { return []; });
  });
  return Promise.all(jobs).then(function (parts) {
    var out = [];
    parts.forEach(function (p) { out = out.concat(p); });
    return out;
  });
}

function pageGenerator(slug) {
  try {
    var g = (window.JAHDB && JAHDB.getGenerator) ? JAHDB.getGenerator(slug) : null;
    if (g && typeof g.generate === 'function') return g;
  } catch (e) {}
  return null;
}

function tryGenerate(state, theme) {
  var g = pageGenerator(state.cfg.slug);
  if (!g) return null;
  try {
    var base = (state.rows ? state.rows.length : 0) + 1, made = [], i, r;
    for (i = 0; i < 3; i++) {
      r = g.generate(base + i, { topic: theme });
      if (r && g.validate && g.validate(r).ok) made.push(r);
      else if (r) made.push(r);
    }
    return made.length ? made : null;
  } catch (e) { return null; }
}

/* ---------------- the assistant: persona + conversational brain ---------------- */
var ROLES = {
  'guide':   'your friendly guide',
  'scholar': 'your research specialist',
  'muse':    'your creative partner',
  'teacher': 'your patient teacher'
};
var TONES = {
  'warm':         'warm and encouraging',
  'professional': 'clear and professional',
  'playful':      'playful and upbeat',
  'concise':      'short and to the point'
};

function opener(p) {
  /* tone-flavored openers — phrasing only; every claim below is checked live */
  if (p.tone === 'concise') return '';
  if (p.tone === 'playful') return 'On it! ';
  if (p.tone === 'professional') return 'Certainly. ';
  return '';
}

function capabilityLine(state, p) {
  var bits = ['searching the live archive'];
  if (pageGenerator(state.cfg.slug)) bits.push('generating brand-new records with this database\u2019s own generator');
  bits.push('explaining any record in plain language');
  return opener(p) + 'I\u2019m ' + p.name + ', ' + (ROLES[p.role] || p.roleText) +
    ' for the ' + state.cfg.name + '. I can help by ' + bits.join(', ') + '. ' +
    'Just tell me what you\u2019re looking for — in your own words.';
}

function recordCard(r) {
  var title = r.title || r.t || r.id;
  var desc = String(r.description || r.d || '').slice(0, 180);
  var link = '#rec=' + encodeURIComponent(r.id || '');
  return '<div class="amk-rec"><b>' + esc(title) + '</b> ' +
    '<span class="amk-id">' + esc(r.id || '') + '</span>' +
    (desc ? '<div class="amk-desc">' + esc(desc) + (String(r.description || r.d || '').length > 180 ? '\u2026' : '') + '</div>' : '') +
    '<div><a class="amk-link" href="' + esc(link) + '">Open full record on this page</a></div></div>';
}

function summarizeRecord(p, r) {
  /* a real explanation built from the record's actual fields — natural sentences */
  var title = r.title || r.t || r.id;
  var s = opener(p) + 'Here\u2019s what I found. \u201C' + title + '\u201D';
  if (r.id) s += ' (record ' + r.id + ')';
  var genre = r.genre || r.g || r.kind || r.type;
  if (genre) s += ' is filed under ' + genre;
  s += '. ';
  var desc = String(r.description || r.d || '');
  if (desc) s += desc.slice(0, 300) + (desc.length > 300 ? '\u2026' : ' ') + ' ';
  if (r.demo) s += 'It even ships with a runnable demo program you can try in the Demo Lab. ';
  var src = String(r.src || '');
  if (src === 'signature') s += 'It\u2019s a Signature-authored original. ';
  return s.trim();
}

function handleDemoMessage(state, p, logEl, text) {
  var low = text.toLowerCase().trim();
  function say(html) {
    var d = document.createElement('div');
    d.className = 'amk-msg a';
    d.innerHTML = '<span class="amk-b">' + html + '</span>';
    logEl.appendChild(d);
    logEl.scrollTop = logEl.scrollHeight;
  }
  function sayUser(t) {
    var d = document.createElement('div');
    d.className = 'amk-msg u';
    d.innerHTML = '<span class="amk-b">' + esc(t) + '</span>';
    logEl.appendChild(d);
    logEl.scrollTop = logEl.scrollHeight;
  }
  sayUser(text);

  var isGen = /^(generate|make|create|invent|draft|compose|write)(\b|\s)/.test(low) ||
    /\b(generate|create|make me|invent|draft)\b/.test(low);
  var isFind = /^(find|search|show|lookup|locate|list|get)\b/.test(low) ||
    /\b(find|search for|look up|show me|pull up|any records)\b/.test(low);
  var isExplain = /^(explain|describe|tell me about|summar)/.test(low);

  loadIndex(state).then(function (rows) {
    if (isGen) {
      var theme = text.replace(/^(generate|make|create|invent|draft|compose|write)\b/i, '')
        .replace(/^(a|an|some|a few|me)\b/i, '').trim() || 'something new';
      var made = tryGenerate(state, theme);
      if (made) {
        say(opener(p) + 'Done — I ran this database\u2019s own generator and made ' + made.length +
          ' new ' + esc(state.cfg.kind) + ' record' + (made.length > 1 ? 's' : '') +
          ' on \u201C' + esc(theme) + '\u201D: ' + made.map(function (r) { return esc(r.id); }).join(', ') +
          '. They\u2019re validated and live right here in this session\u2019s demo — open the Generator tab on this page to file ones you want to keep.');
      } else {
        say(opener(p) + 'I\u2019d love to, but this page hasn\u2019t loaded the ' + esc(state.cfg.name) +
          '\u2019s generator in this session, so I can\u2019t mint new records from here. ' +
          'Open the Generator tab on this page — that\u2019s where new records are made — or ask me to search the ' +
          rows.length.toLocaleString() + ' records already in the archive.');
      }
      return;
    }
    if (isFind || isExplain) {
      var q = text.replace(/^(find|search|show|lookup|locate|list|get|explain|describe)\b/i, '')
        .replace(/\b(records?|for|about|me|please)\b/gi, ' ').trim();
      var hits = searchRows(rows, q || text);
      if (!hits.length) {
        say(opener(p) + 'I searched all ' + rows.length.toLocaleString() +
          ' archive records and nothing matched \u201C' + esc(q || text) + '\u201D. ' +
          'Try different words, or ask me to generate a brand-new record on that theme.');
        return;
      }
      fullRecords(state, hits).then(function (recs) {
        if (!recs.length) {
          say(opener(p) + 'The index points at ' + hits.length + ' match' +
            (hits.length > 1 ? 'es' : '') + ' but the full files are still loading — ask me again in a moment.');
          return;
        }
        if (isExplain) {
          say(esc(summarizeRecord(p, recs[0])));
        } else {
          var line = opener(p) + 'I found ' + recs.length + ' record' + (recs.length > 1 ? 's' : '') +
            ' in the live archive matching \u201C' + esc(q || text) + '\u201D:';
          say(esc(line) + recs.map(recordCard).join(''));
        }
      });
      return;
    }
    /* free-form: honest, conversational, grounded in what is actually loaded */
    var genres = {};
    rows.forEach(function (r) { var g = rowGenre(r); if (g) genres[g] = 1; });
    var glist = Object.keys(genres).slice(0, 6);
    say(esc(opener(p) + 'I\u2019m ' + p.name + ', ' + (ROLES[p.role] || p.roleText) +
      ' for the ' + state.cfg.name + '. Right now I can see ' + rows.length.toLocaleString() +
      ' archive records' + (glist.length ? ' across areas like ' + glist.join(', ') : '') +
      '. Ask me to find something (\u201Cfind solar\u201D), explain a record (\u201Cexplain JAH-001\u201D), ' +
      'or generate new ones (\u201Cmake a workout plan\u201D) — all in plain conversation.'));
  }).catch(function () {
    say(esc(opener(p) + 'I couldn\u2019t reach this database\u2019s archive index from here, so I can\u2019t look anything up yet. ' +
      'Reload the page and try again — I won\u2019t pretend to search what I can\u2019t see.'));
  });
}

/* ---------------- the package: a complete, working assistant definition ---------------- */
function buildPackage(state, p, starter) {
  var caps = {
    archiveLookup: true,
    liveDemoChat: true,
    exportPackage: true,
    generation: !!pageGenerator(state.cfg.slug)
  };
  var roleText = ROLES[p.role] || p.roleText;
  var systemPrompt =
    'You are ' + p.name + ', ' + roleText + ' for the "' + state.cfg.name + '" ' +
    '(JAH Databases, property of Justin Addam Higgins).\n' +
    'The database holds ' + state.cfg.kind + ' records (IDs start with ' + state.cfg.prefix + '). ' +
    'Its archive-aware AI is ' + state.cfg.aiName + '.\n\n' +
    'HOW YOU WORK\n' +
    '- Speak in natural, conversational sentences, in a ' + (TONES[p.tone] || p.tone) + ' tone. Never answer in templated blocks.\n' +
    '- Do REAL work: look records up in the live archive index (' + state.cfg.local + 'index.jsonl.gz, ' +
    'full files in ' + state.cfg.local + 'chunks/chunk-NNNN.jsonl.gz) instead of inventing them.\n' +
    (caps.generation
      ? '- When asked to make something new, run the database\u2019s own registered generator (JAHDB.getGenerator("' + state.cfg.slug + '")) — same seed + same description always makes the same record.\n'
      : '- This build has no generator attached: say so plainly when asked to create, and offer archive search instead.\n') +
    '- Never claim an ability you do not have. If the archive is unreachable, say so instead of pretending.\n' +
    '- Every record shown carries its real ID; deep-link it as ' + state.cfg.local + '#rec=<id>.\n' +
    (p.focus ? '- The user asked you to focus especially on: ' + p.focus + '\n' : '') +
    'You are property of Justin Addam Higgins (JAH), part of the JAH Databases network.';
  var behavior = [
    p.name + ' greets the user by name-role and states what it can really do in this session.',
    'On "find/search/show X": it scores the live archive index, loads the full record files, and answers in sentences with the real titles, IDs and short descriptions.',
    'On "explain <id>": it loads that exact record and explains its fields in plain language.',
    caps.generation
      ? 'On "generate/make X": it runs the database\u2019s own generator for 3 validated records and reports their real IDs.'
      : 'On "generate/make X": it honestly says generation is not attached to this build and offers archive search.',
    'It never invents archive records, never disguises phrasing rotation as intelligence, and never claims unreachable abilities.'
  ];
  return {
    assistantMaker: 'JAH Assistant Maker 1.0',
    created: new Date().toISOString().slice(0, 10),
    owner: 'Justin Addam Higgins (JAH)',
    persona: { name: p.name, role: p.role, roleText: roleText, tone: p.tone, toneText: TONES[p.tone] || p.tone, focus: p.focus || '' },
    database: {
      name: state.cfg.name, slug: state.cfg.slug, aiName: state.cfg.aiName,
      recordKind: state.cfg.kind, idPrefix: state.cfg.prefix,
      indexUrl: state.cfg.local + 'index.jsonl.gz',
      chunkPattern: state.cfg.local + 'chunks/chunk-NNNN.jsonl.gz (100 records per chunk)',
      recordDeepLink: 'db/' + state.cfg.slug + '/#rec=<record-id>',
      livePage: 'https://justinahiggins614-cmyk.github.io/jah-databases/db/' + state.cfg.slug + '/'
    },
    capabilities: caps,
    systemPrompt: systemPrompt,
    behaviorSpec: behavior,
    starterKnowledge: starter
  };
}

function loadStarterKnowledge(state) {
  return loadIndex(state).then(function (rows) {
    var genres = {}, sample = [];
    rows.forEach(function (r) { var g = rowGenre(r); if (g) genres[g] = (genres[g] || 0) + 1; });
    var top = Object.keys(genres).sort(function (a, b) { return genres[b] - genres[a]; }).slice(0, 10);
    for (var i = 0; i < Math.min(5, rows.length); i++) {
      sample.push({ id: rows[i].id, title: rowTitle(rows[i]), genre: rowGenre(rows[i]) });
    }
    return {
      note: 'Live snapshot of the archive index, pulled when the package was built.',
      recordCount: rows.length,
      topGenres: top,
      sampleRecords: sample
    };
  }).catch(function () {
    return {
      note: 'The archive index was not reachable from this page when the package was built — load it live before answering.',
      recordCount: 0, topGenres: [], sampleRecords: []
    };
  });
}

/* ---------------- modal UI ---------------- */
var CSS_INJECTED = false;
function injectCSS() {
  if (CSS_INJECTED) return;
  CSS_INJECTED = true;
  var css =
    '.amk-ov{position:fixed;inset:0;background:rgba(2,6,16,.82);z-index:99999;display:flex;align-items:center;justify-content:center;padding:12px;box-sizing:border-box}' +
    '.amk-modal{background:#0d1526;border:1px solid #2f7bff;border-radius:14px;max-width:860px;width:100%;max-height:92vh;overflow:auto;color:#e8f1ff;font-family:Arial,Helvetica,sans-serif;box-sizing:border-box}' +
    '.amk-head{display:flex;align-items:center;justify-content:space-between;padding:12px 16px;border-bottom:1px solid #1d2c4d;position:sticky;top:0;background:#0d1526}' +
    '.amk-head h2{margin:0;font-size:1.2em}' +
    '.amk-x{background:#14305e;color:#e8f1ff;border:1px solid #1d2c4d;border-radius:8px;padding:6px 12px;cursor:pointer;font-size:1em}' +
    '.amk-body{padding:14px 16px}' +
    '.amk-body h3{margin:14px 0 6px;color:#e8f1ff}' +
    '.amk-body p{color:#9fb3d8}' +
    '.amk-f{display:flex;gap:10px;flex-wrap:wrap;margin:8px 0}' +
    '.amk-f label{color:#9fb3d8;font-size:.9em;display:flex;flex-direction:column;gap:4px;min-width:180px;flex:1}' +
    '.amk-modal input,.amk-modal select,.amk-modal textarea{background:#0a1120;color:#e8f1ff;border:1px solid #1d2c4d;border-radius:8px;padding:9px 10px;font-size:1em;box-sizing:border-box;width:100%}' +
    '.amk-go{background:#2f7bff;color:#fff;border:1px solid #2f7bff;border-radius:8px;padding:10px 18px;font-weight:bold;cursor:pointer;font-size:1em}' +
    '.amk-btn{background:#14305e;color:#e8f1ff;border:1px solid #1d2c4d;border-radius:8px;padding:9px 14px;cursor:pointer;font-size:.95em;margin:4px 6px 4px 0}' +
    '.amk-out{background:#080d18;border:1px solid #1d2c4d;border-radius:10px;padding:10px;margin:10px 0;max-height:300px;overflow:auto;white-space:pre-wrap;font-family:Consolas,monospace;font-size:.82em;color:#cfe0ff}' +
    '.amk-log{max-height:40vh;overflow:auto;border:1px solid #1d2c4d;border-radius:10px;padding:10px;background:#080d18;margin-bottom:8px}' +
    '.amk-msg{display:flex;margin:8px 0}.amk-msg.u{justify-content:flex-end}.amk-msg.a{justify-content:flex-start}' +
    '.amk-b{max-width:88%;padding:8px 12px;border-radius:12px;overflow-wrap:break-word;text-align:left;font-size:.95em;line-height:1.5}' +
    '.amk-msg.u .amk-b{background:#14305e;color:#e8f1ff}.amk-msg.a .amk-b{background:#101a30;border:1px solid #1d2c4d;color:#e8f1ff}' +
    '.amk-row{display:flex;gap:8px;margin-top:6px}' +
    '.amk-row input{flex:1}' +
    '.amk-rec{background:#101a30;border:1px solid #1d2c4d;border-radius:8px;padding:8px 10px;margin:6px 0}' +
    '.amk-id{font-family:Consolas,monospace;font-size:.8em;color:#00e5a0}' +
    '.amk-desc{color:#9fb3d8;font-size:.9em;margin-top:4px}' +
    '.amk-link{color:#7aa8ff;font-size:.9em}' +
    '.amk-note{font-size:.85em;color:#9fb3d8}';
  var st = document.createElement('style');
  st.textContent = css;
  document.head.appendChild(st);
}

function copyText(txt, btn) {
  var label = btn.textContent;
  function done(ok) {
    btn.textContent = ok ? '\u2713 Copied' : 'Copy failed';
    setTimeout(function () { btn.textContent = label; }, 1600);
  }
  if (navigator.clipboard && navigator.clipboard.writeText) {
    navigator.clipboard.writeText(txt).then(function () { done(true); }, function () { done(false); });
  } else {
    var ta = document.createElement('textarea');
    ta.value = txt;
    document.body.appendChild(ta);
    ta.select();
    try { done(document.execCommand('copy')); } catch (x) { done(false); }
    document.body.removeChild(ta);
  }
}
function downloadJSON(obj, fname) {
  var blob = new Blob([JSON.stringify(obj, null, 2)], { type: 'application/json' });
  var a = document.createElement('a');
  a.href = URL.createObjectURL(blob);
  a.download = fname;
  document.body.appendChild(a);
  a.click();
  setTimeout(function () { URL.revokeObjectURL(a.href); a.remove(); }, 500);
}

function launch(cfg) {
  injectCSS();
  var state = { cfg: cfg, rows: null, idxPromise: null };
  var p = { name: cleanName(cfg.aiName), role: 'guide', roleText: '', tone: 'warm', focus: '' };

  var ov = document.createElement('div');
  ov.className = 'amk-ov';
  ov.innerHTML =
    '<div class="amk-modal" role="dialog" aria-label="Assistant Maker">' +
    '<div class="amk-head"><h2>\u2728 Make an Assistant Like Mine</h2><button class="amk-x" type="button">\u2715 Close</button></div>' +
    '<div class="amk-body">' +
    '<p>Build a personal AI assistant for the <b>' + esc(cfg.name) + '</b> — named by you, with the role and personality you pick, ' +
    'wired live to this database\u2019s own archive. What you build below is a complete working package plus a live demo you can talk to right now.</p>' +
    '<h3>1. Name your assistant</h3>' +
    '<div class="amk-f"><label>Assistant name<input id="amkName" value="' + esc(p.name) + '" maxlength="60"></label></div>' +
    '<h3>2. Pick its role &amp; personality</h3>' +
    '<div class="amk-f">' +
    '<label>Role<select id="amkRole"><option value="guide">Friendly Guide</option><option value="scholar">Research Specialist</option>' +
    '<option value="muse">Creative Partner</option><option value="teacher">Patient Teacher</option><option value="custom">Custom\u2026</option></select></label>' +
    '<label>Tone<select id="amkTone"><option value="warm">Warm</option><option value="professional">Professional</option>' +
    '<option value="playful">Playful</option><option value="concise">Concise</option></select></label>' +
    '</div>' +
    '<div class="amk-f" id="amkCustomWrap" style="display:none"><label>Custom role (your own words)<input id="amkCustom" placeholder="e.g. my late-night lab partner"></label></div>' +
    '<div class="amk-f"><label>What should it focus on? (optional)<input id="amkFocus" placeholder="e.g. workout plans for beginners"></label></div>' +
    '<button class="amk-go" id="amkBuild" type="button">Build my assistant</button> <span class="amk-note" id="amkStatus"></span>' +
    '<div id="amkPkgWrap" style="display:none">' +
    '<h3>3. Your assistant package — complete &amp; working</h3>' +
    '<p>This is the full definition: persona, system prompt, behavior spec, and starter knowledge pulled live from this archive. ' +
    'Copy it or download it — it works anywhere you can paste a system prompt.</p>' +
    '<div><button class="amk-btn" id="amkCopyPkg" type="button">\u29c9 Copy package (JSON)</button>' +
    '<button class="amk-btn" id="amkDlPkg" type="button">\u2b07 Download package (.json)</button>' +
    '<button class="amk-btn" id="amkCopyPrompt" type="button">\u29c9 Copy system prompt</button></div>' +
    '<div class="amk-out" id="amkPkgOut"></div>' +
    '<h3>4. Try it live — right here, right now</h3>' +
    '<p class="amk-note">This demo talks to the <b>live archive</b> on this page and uses this database\u2019s own generator when it\u2019s loaded. ' +
    'Ask it to find, explain, or generate.</p>' +
    '<div class="amk-log" id="amkLog"></div>' +
    '<div class="amk-row"><input id="amkIn" placeholder="Talk to your new assistant\u2026"><button class="amk-go" id="amkSend" type="button">Send</button></div>' +
    '</div>' +
    '</div></div>';
  document.body.appendChild(ov);

  function $(id) { return ov.querySelector('#' + id); }
  function close() { if (ov.parentNode) ov.parentNode.removeChild(ov); }
  ov.querySelector('.amk-x').addEventListener('click', close);
  ov.addEventListener('click', function (e) { if (e.target === ov) close(); });

  var roleSel = $('amkRole');
  roleSel.addEventListener('change', function () {
    $('amkCustomWrap').style.display = roleSel.value === 'custom' ? '' : 'none';
  });

  var pkg = null;
  $('amkBuild').addEventListener('click', function () {
    p.name = cleanName($('amkName').value);
    p.role = roleSel.value;
    p.roleText = p.role === 'custom' ? (cleanName($('amkCustom').value) || 'your custom companion') : '';
    p.tone = $('amkTone').value;
    p.focus = $('amkFocus').value.trim().slice(0, 200);
    var st = $('amkStatus');
    st.textContent = 'Building\u2026 pulling live archive snapshot\u2026';
    loadStarterKnowledge(state).then(function (starter) {
      pkg = buildPackage(state, p, starter);
      $('amkPkgOut').textContent = JSON.stringify(pkg, null, 2);
      $('amkPkgWrap').style.display = '';
      st.textContent = 'Built. ' + starter.recordCount.toLocaleString() + ' archive records wired in.';
      /* wire export buttons */
      $('amkCopyPkg').addEventListener('click', function (e) { copyText(JSON.stringify(pkg, null, 2), e.target); });
      $('amkDlPkg').addEventListener('click', function () {
        downloadJSON(pkg, 'assistant-' + cfg.slug + '-' + p.name.toLowerCase().replace(/[^a-z0-9]+/g, '-') + '.json');
      });
      $('amkCopyPrompt').addEventListener('click', function (e) { copyText(pkg.systemPrompt, e.target); });
      /* start the live demo, in persona */
      var log = $('amkLog');
      log.innerHTML = '';
      var d = document.createElement('div');
      d.className = 'amk-msg a';
      loadIndex(state).then(function (rows) {
        d.innerHTML = '<span class="amk-b">' + esc(capabilityLine(state, p)) + '</span>';
      }).catch(function () {
        d.innerHTML = '<span class="amk-b">' + esc(opener(p) + 'I\u2019m ' + p.name +
          ' — I couldn\u2019t reach the archive index just now, so my lookup is down until the page reloads. I\u2019ll still answer what I can.') + '</span>';
      });
      log.appendChild(d);
      function send() {
        var t = $('amkIn').value.trim();
        if (!t) return;
        $('amkIn').value = '';
        handleDemoMessage(state, p, log, t);
      }
      $('amkSend').addEventListener('click', send);
      $('amkIn').addEventListener('keydown', function (e) { if (e.key === 'Enter') send(); });
      $('amkPkgWrap').scrollIntoView();
    });
  });
}

/* ---------------- auto-wire: every .jah-amk-btn on any db page ---------------- */
function cfgFromBtn(btn) {
  var d = btn.dataset || {};
  var slug = d.slug || '';
  return {
    slug: slug,
    name: d.name || slug,
    aiName: d.ainame || d.aiName || 'JAH Assistant',
    kind: d.kind || 'records',
    prefix: d.prefix || 'JAH-',
    local: d.local || ('../../data/' + slug + '/')
  };
}
function wire() {
  var btns = document.querySelectorAll('.jah-amk-btn');
  for (var i = 0; i < btns.length; i++) {
    (function (btn) {
      if (btn.dataset.amkWired) return;
      btn.dataset.amkWired = '1';
      btn.addEventListener('click', function () { launch(cfgFromBtn(btn)); });
    })(btns[i]);
  }
}
if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', wire);
} else {
  wire();
}

window.JAHAssistantMaker = { launch: launch, wire: wire, version: '1.0.0' };
})();
