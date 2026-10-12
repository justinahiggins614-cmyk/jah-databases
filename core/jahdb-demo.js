/*! JAH Demo Engine — jahdb-demo-1.0
 * Property of Justin Addam Higgins (JAH).
 *
 * Usable-or-demo rule: every database record ships a REAL runnable demo
 * program (record.demo.program). Programs are plain JavaScript using only
 * console.log — they run as-is on any PC (`node demo.js`), pasted into a
 * browser console, or executed in-page by the Demo Lab tab.
 *
 * UMD: works in browsers (registers as window.JAHDB.demo and hooks the
 * page's Demo Lab pane) and in Node (module.exports) for backfills and
 * generator harnesses.
 */
(function (root, factory) {
  'use strict';
  var D = factory();
  if (typeof module !== 'undefined' && module.exports) module.exports = D;
  root.JAHDB = root.JAHDB || {};
  root.JAHDB.demo = D;
  try { if (root.JAHDB.setDemoBuilder) root.JAHDB.setDemoBuilder(D.build); } catch (e) {}
})(typeof self !== 'undefined' ? self : this, function () {
'use strict';

var VERSION = 'jahdb-demo-1.0';

/* ---------------- small helpers ---------------- */
function isObj(v) { return v !== null && typeof v === 'object' && !Array.isArray(v); }
function jsq(v, max) {
  var s;
  try { s = JSON.stringify(v); } catch (e) { s = '"(unserializable)"'; }
  if (max && s.length > max) s = s.slice(0, max) + '…"';
  return s == null ? 'null' : s;
}
function escH(s) {
  return String(s == null ? '' : s).replace(/[&<>"]/g, function (c) {
    return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c];
  });
}
function titleOf(rec) {
  return rec.title || rec.name || rec.signature_name || rec.task_text ||
         rec.goal || rec.station_name || rec.id || rec.api_id || 'record';
}
function idOf(rec) { return String(rec.id || rec.api_id || rec.task_id || rec.trajectory_id || rec.record_id || 'rec'); }
function trunc(s, n) { s = String(s == null ? '' : s); return s.length > n ? s.slice(0, n) + '…' : s; }

var CODE_KEYS = { code: 1, snippet: 1, program: 1, script: 1, source_code: 1, implementation: 1, example_code: 1, solution: 1, query: 1, sample_code: 1 };
var STEP_KEYS = { steps: 1, stages: 1, phases: 1, actions: 1, instructions: 1, procedure: 1, method_steps: 1, rounds: 1 };
var SKIP_KEYS = { demo: 1 };
var LONG_SKIP_PREFIX = '_';

function looksLikeCode(s) {
  if (typeof s !== 'string' || s.length < 12) return false;
  var marks = 0;
  if (/\n/.test(s) && s.split('\n').length >= 3) marks++;
  if (/(^|\n)\s*(function\s+\w+|const\s+\w+\s*=|let\s+\w+\s*=|def\s+\w+\s*\(|import\s+\w+|from\s+\w+\s+import|SELECT\s+.+\s+FROM|console\.log\(|print\(|#include|public\s+static|=>)/i.test(s)) marks++;
  if (/[{};]/.test(s) && /\(.*\)/.test(s)) marks++;
  return marks >= 2;
}
function detectLang(rec, code) {
  var l = String(rec.language || rec.lang || '').toLowerCase();
  if (/python/.test(l)) return 'python';
  if (/sql/.test(l)) return 'sql';
  if (/javascript|node|js\b/.test(l)) return 'javascript';
  if (/^\s*def\s+\w|^import\s+\w+[\s,]|print\(/m.test(code)) return 'python';
  if (/^\s*SELECT\b/i.test(code)) return 'sql';
  if (/<\?php/.test(code)) return 'php';
  return 'javascript';
}

/* Collect field intelligence from a record (top level only, deterministic). */
function collect(rec) {
  var nums = {}, texts = [], codes = [], stepArr = null, stepKey = '', urls = [], objs = [];
  Object.keys(rec).forEach(function (k) {
    if (SKIP_KEYS[k] || k.charAt(0) === LONG_SKIP_PREFIX) return;
    var v = rec[k];
    if (typeof v === 'number' && isFinite(v)) { nums[k] = v; return; }
    if (typeof v === 'string') {
      if (/^https?:\/\//i.test(v)) { urls.push({ k: k, v: v }); return; }
      if ((CODE_KEYS[k] || looksLikeCode(v)) && v.length < 20000) { codes.push({ k: k, v: v }); return; }
      if (v.length >= 60) texts.push({ k: k, v: v });
      return;
    }
    if (Array.isArray(v)) {
      if (STEP_KEYS[k] && v.length >= 2 && !stepArr) { stepArr = v; stepKey = k; return; }
      if (v.length && v.length <= 40) objs.push({ k: k, v: v });
      return;
    }
    if (isObj(v)) { objs.push({ k: k, v: v }); return; }
  });
  return { nums: nums, texts: texts, codes: codes, stepArr: stepArr, stepKey: stepKey, urls: urls, objs: objs };
}

/* ---------------- PC-slug specializations ---------------- */
var PC_BUILDERS = {};
function pc(slug, fn) { PC_BUILDERS[slug] = fn; }

function header(slug, rec, what) {
  return '/* JAH interactive demo program — ' + VERSION + '\n' +
    ' * Database: ' + slug + ' · Record: ' + idOf(rec) + ' · ' + trunc(titleOf(rec), 60) + '\n' +
    ' * ' + what + '\n' +
    ' * RUN ON PC: save as demo.js, then run:  node demo.js\n' +
    ' * RUN IN BROWSER: press F12, paste this program into the console, press Enter.\n' +
    ' * RUN IN-PAGE: open this record and press "Run interactive demo". */\n';
}

/* --- api-docs: runnable mock of the documented endpoint --- */
pc('api-docs', function (slug, rec) {
  var params = rec.parameters && isObj(rec.parameters) ? rec.parameters : {};
  var pnames = Object.keys(params);
  var defaults = {};
  pnames.forEach(function (p) {
    var t = String((params[p] && params[p].type) || '').toLowerCase();
    defaults[p] = /int|number/.test(t) ? 1 : /bool/.test(t) ? true : /array/.test(t) ? [] : /object/.test(t) ? {} : 'demo';
  });
  var exCall = String(rec.example_call || '').replace(/`/g, '');
  var exResp = String(rec.example_response || '').replace(/`/g, '');
  var errs = Array.isArray(rec.error_codes) ? rec.error_codes : [];
  var prog = header(slug, rec, 'Runnable mock of the "' + (rec.name || 'api') + '" endpoint — validates args, returns the documented example response.') +
    '(function(){\n' +
    'var SPEC=' + jsq({ name: rec.name, description: rec.description, parameters: params, error_codes: errs }) + ';\n' +
    'function call(args){\n' +
    '  args=args||{};\n' +
    '  console.log("> "+SPEC.name+"("+JSON.stringify(args)+")");\n' +
    '  var missing=Object.keys(SPEC.parameters).filter(function(p){return args[p]===undefined;});\n' +
    '  if(missing.length){console.log("! missing parameters: "+missing.join(", "));return {error:"E_ARGS",missing:missing};}\n' +
    '  var resp=' + jsq(exResp || '{"ok":true}') + ';\n' +
    '  console.log("< "+resp);\n' +
    '  return resp;\n' +
    '}\n' +
    'console.log("API: "+SPEC.name+" — "+SPEC.description);\n' +
    'console.log("Parameters: "+Object.keys(SPEC.parameters).map(function(p){return p+":"+SPEC.parameters[p].type;}).join(", "));\n' +
    'console.log("Error codes: "+SPEC.error_codes.map(function(e){return e.code;}).join(", "));\n' +
    'console.log("--- documented example ---");\n' +
    'console.log("call: ' + trunc(exCall, 120).replace(/\\/g, '\\\\').replace(/"/g, '\\"') + '");\n' +
    'console.log("--- live mock run ---");\n' +
    'call(' + jsq(defaults) + ');\n' +
    'console.log("Tip: call your own args and watch the mock validate + respond.");\n' +
    '})();\n';
  return { kind: 'api', title: 'Runnable API mock — ' + (rec.name || idOf(rec)), program: prog, language: 'javascript' };
});

/* --- binary-encoding: round-trip converter demo --- */
pc('binary-encoding', function (slug, rec) {
  var out = isObj(rec.output) ? rec.output : {};
  var inp = isObj(rec.input) ? rec.input : {};
  var prog = header(slug, rec, 'Byte/encoding round-trip demo for the "' + (rec.method || 'encoding') + '" method.') +
    '(function(){\n' +
    'var REC=' + jsq({ method: rec.method, concept: rec.concept, input: inp, output: out, spec: rec.spec }, 1200) + ';\n' +
    'function toBin(n){return (n>>>0).toString(2).padStart(8,"0");}\n' +
    'function toHex(n){return (n>>>0).toString(16).toUpperCase().padStart(2,"0");}\n' +
    'function toOct(n){return (n>>>0).toString(8);}\n' +
    'function convert(n){console.log("dec "+n+" → bin "+toBin(n)+" · hex "+toHex(n)+" · oct "+toOct(n)+" · char "+(n>=32&&n<127?String.fromCharCode(n):"·"));return {dec:n,bin:toBin(n),hex:toHex(n),oct:toOct(n)};}\n' +
    'console.log("Method: "+REC.method);\n' +
    'console.log("Concept: "+REC.concept);\n' +
    'console.log("Recorded conversion: "+JSON.stringify(REC.input)+" → "+JSON.stringify(REC.output));\n' +
    'console.log("--- round-trip check ---");\n' +
    'var vals=[0,1,42,65,127,255].filter(function(n){return n!==undefined;});\n' +
    'vals.forEach(convert);\n' +
    'console.log("Try: convert(72)  — converts any byte value 0–255.");\n' +
    '})();\n';
  return { kind: 'encode', title: 'Encoding round-trip demo — ' + trunc(titleOf(rec), 50), program: prog, language: 'javascript' };
});

/* --- tool-schemas / system-api: schema validator demo --- */
function schemaBuilder(slug, rec) {
  var fields = [];
  Object.keys(rec).forEach(function (k) {
    if (k.charAt(0) === '_' || k === 'demo' || k === 'id') return;
    var v = rec[k], t = Array.isArray(v) ? 'array' : (v === null ? 'null' : typeof v);
    fields.push({ name: k, type: t });
  });
  var prog = header(slug, rec, "Validates a sample object against this record's schema, field by field.") +
    '(function(){\n' +
    'var SCHEMA=' + jsq(fields.slice(0, 24)) + ';\n' +
    'var SAMPLE=' + jsq(pickSample(rec), 1500) + ';\n' +
    'function validate(obj){\n' +
    '  var errs=[];\n' +
    '  SCHEMA.forEach(function(f){\n' +
    '    var v=obj[f.name];\n' +
    '    var t=Array.isArray(v)?"array":(v===null?"null":typeof v);\n' +
    '    if(v===undefined){errs.push("missing field: "+f.name);}\n' +
    '    else if(t!==f.type){errs.push("type mismatch on "+f.name+": expected "+f.type+", got "+t);}\n' +
    '    else{console.log("  ✓ "+f.name+" ("+f.type+")");}\n' +
    '  });\n' +
    '  return errs;\n' +
    '}\n' +
    'console.log("Schema for '+ idOf(rec).replace(/"/g, '') + ' — "+SCHEMA.length+" fields");\n' +
    'console.log("--- validating sample record ---");\n' +
    'var errs=validate(SAMPLE);\n' +
    'if(!errs.length)console.log("RESULT: valid ✓");\n' +
    'else{console.log("RESULT: "+errs.length+" problem(s)");errs.forEach(function(e){console.log("  ✗ "+e);});}\n' +
    'console.log("--- validating a broken sample ---");\n' +
    'var bad=Object.assign({},SAMPLE);delete bad[SCHEMA[0]&&SCHEMA[0].name];\n' +
    'var errs2=validate(bad);\n' +
    'console.log("RESULT: "+errs2.length+" problem(s) (expected ≥1)");\n' +
    'console.log("Try: validate(yourObject) with your own data.");\n' +
    '})();\n';
  return { kind: 'schema', title: 'Schema validator demo — ' + trunc(titleOf(rec), 50), program: prog, language: 'javascript' };
}
function pickSample(rec) {
  var o = {};
  Object.keys(rec).forEach(function (k) {
    if (k.charAt(0) === '_' || k === 'demo') return;
    var v = rec[k];
    o[k] = typeof v === 'string' ? trunc(v, 120) : (isObj(v) ? { '(object)': Object.keys(v).slice(0, 6) } : (Array.isArray(v) ? v.slice(0, 3) : v));
  });
  return o;
}
pc('tool-schemas', schemaBuilder);
pc('system-api', schemaBuilder);

/* --- tool-trajectories: step replay --- */
pc('tool-trajectories', function (slug, rec) {
  var steps = Array.isArray(rec.steps) ? rec.steps.slice(0, 20) : [];
  var prog = header(slug, rec, 'Replays this tool-use trajectory step by step, exactly as recorded.') +
    '(function(){\n' +
    'var STEPS=' + jsq(steps.map(function (s, i) {
      return { n: i + 1, tool: s.tool || s.action || s.name || 'step', args: s.args || s.input || s.target || '', result: trunc(String(s.result || s.output || s.observation || ''), 160) };
    }), 4000) + ';\n' +
    'console.log("Task: ' + trunc(String(rec.task_text || rec.title || ''), 120).replace(/\\/g, '\\\\').replace(/"/g, '\\"') + '");\n' +
    'console.log("Tools: "+' + jsq(((rec.tool_schema && rec.tool_schema.tools) || []).map(function (t) { return t.name || t; })) + ');\n' +
    'STEPS.forEach(function(s){\n' +
    '  console.log("\\n[step "+s.n+"/"+STEPS.length+"] "+s.tool);\n' +
    '  if(s.args)console.log("  args:   "+JSON.stringify(s.args).slice(0,160));\n' +
    '  if(s.result)console.log("  result: "+s.result);\n' +
    '});\n' +
    'console.log("\\nFinal answer: ' + trunc(String(rec.final_answer || ''), 200).replace(/\\/g, '\\\\').replace(/"/g, '\\"') + '");\n' +
    'console.log("Success: ' + (rec.success ? 'yes ✓' : 'no') + '");\n' +
    '})();\n';
  return { kind: 'trajectory', title: 'Trajectory replay — ' + trunc(titleOf(rec), 50), program: prog, language: 'javascript' };
});

/* --- web-browsing-tasks: task plan executor --- */
pc('web-browsing-tasks', function (slug, rec) {
  var acts = Array.isArray(rec.actions) ? rec.actions.slice(0, 20) : [];
  var prog = header(slug, rec, 'Executes this web-task plan step by step (simulated fetch — no network needed).') +
    '(function(){\n' +
    'var ACTIONS=' + jsq(acts.map(function (a, i) {
      return { n: i + 1, action: a.action || a.type || 'step', target: trunc(String(a.target || a.url || ''), 120), result: trunc(String(a.result || ''), 160) };
    }), 4000) + ';\n' +
    'function validUrl(u){return /^https?:\\/\\/[^\\s/$.?#].[^\\s]*$/i.test(u);}\n' +
    'console.log("Goal: ' + trunc(String(rec.goal || rec.title || ''), 140).replace(/\\/g, '\\\\').replace(/"/g, '\\"') + '");\n' +
    'ACTIONS.forEach(function(a){\n' +
    '  console.log("\\n[action "+a.n+"/"+ACTIONS.length+"] "+a.action.toUpperCase()+" → "+a.target);\n' +
    '  if(/^https?:/i.test(a.target))console.log("  url check: "+(validUrl(a.target)?"valid ✓":"INVALID ✗"));\n' +
    '  if(a.result)console.log("  result: "+a.result);\n' +
    '});\n' +
    'console.log("\\nFinal answer: ' + trunc(String(rec.final_answer || ''), 220).replace(/\\/g, '\\\\').replace(/"/g, '\\"') + '");\n' +
    'console.log("Pages visited: ' + (rec.pages_visited == null ? 'n/a' : jsq(rec.pages_visited)) + '");\n' +
    '})();\n';
  return { kind: 'task', title: 'Web-task plan demo — ' + trunc(titleOf(rec), 50), program: prog, language: 'javascript' };
});

/* --- websites / website-information --- */
function siteBuilder(slug, rec) {
  var prog = header(slug, rec, 'Renders this website entry as a launch card and checks its link shape.') +
    '(function(){\n' +
    'var R=' + jsq({ title: rec.title, description: trunc(rec.description || rec.content || '', 300), type: rec.type, genre: rec.genre, url: rec.url || rec.link || rec.site_url || '' }, 900) + ';\n' +
    'function validUrl(u){return /^https?:\\/\\/[^\\s/$.?#].[^\\s]*$/i.test(u);}\n' +
    'console.log("┌─ "+R.title);\n' +
    'console.log("│ "+R.description);\n' +
    'if(R.type)console.log("│ type: "+R.type+(R.genre?" · genre: "+R.genre:""));\n' +
    'if(R.url){console.log("│ url: "+R.url+"  ["+(validUrl(R.url)?"valid ✓":"INVALID ✗")+"]");}\n' +
    'console.log("└─ launch checklist: title ✓ · description ✓ · link "+(R.url?(validUrl(R.url)?"✓":"✗"):"(none)"));\n' +
    '})();\n';
  return { kind: 'site', title: 'Website launch-card demo — ' + trunc(titleOf(rec), 50), program: prog, language: 'javascript' };
}
pc('websites', siteBuilder);
pc('website-information', siteBuilder);

/* --- weather-climate --- */
pc('weather-climate', function (slug, rec) {
  var prog = header(slug, rec, 'Station report: converts units and charts this observation.') +
    '(function(){\n' +
    'var R=' + jsq({ station: rec.station_name || rec.station_id, lat: rec.lat, lon: rec.lon, time: rec.timestamp, temp_c: rec.temp_c, humidity: rec.humidity, precip_mm: rec.precip_mm, condition: rec.condition }) + ';\n' +
    'function cToF(c){return c*9/5+32;}\n' +
    'function mmToIn(m){return m/25.4;}\n' +
    'function bar(label,val,max,w){var n=Math.max(0,Math.round(val/max*w));console.log(label.padEnd(12," ")+"|"+"#".repeat(n)+" "+val);}\n' +
    'console.log("Station: "+R.station+" ("+R.lat+", "+R.lon+")");\n' +
    'console.log("Time: "+R.time+" · Condition: "+R.condition);\n' +
    'console.log(R.temp_c+"°C = "+cToF(R.temp_c).toFixed(1)+"°F · humidity "+R.humidity+"% · precip "+R.precip_mm+"mm ("+mmToIn(R.precip_mm).toFixed(2)+"in)");\n' +
    'console.log("--- observation chart ---");\n' +
    'bar("temp(C)",R.temp_c,40,30);bar("humidity%",R.humidity,100,30);bar("precip(mm)",R.precip_mm,50,30);\n' +
    'console.log("Try: cToF(20), mmToIn(25.4)");\n' +
    '})();\n';
  return { kind: 'weather', title: 'Weather station demo — ' + trunc(titleOf(rec), 50), program: prog, language: 'javascript' };
});

/* --- database-builder: scaffold generator --- */
pc('database-builder', function (slug, rec) {
  var prog = header(slug, rec, 'Generates a starter database scaffold from this construction pattern.') +
    '(function(){\n' +
    'var PATTERN=' + jsq(trunc(String(rec.title || ''), 80)) + ';\n' +
    'var SLUG="my-database";\n' +
    'function files(){\n' +
    '  return [\n' +
    '    "db/"+SLUG+"/manifest.json  — name, tagline, record_kind, id_prefix",\n' +
    '    "db/"+SLUG+"/gen-"+SLUG+".js — deterministic generator (seed → record)",\n' +
    '    "db/"+SLUG+"/index.html     — archive + generator + AI chat + Demo Lab tabs",\n' +
    '    "data/"+SLUG+"/index.jsonl.gz — archive index (id, title, chunk, group)",\n' +
    '    "data/"+SLUG+"/chunks/chunk-0001.jsonl.gz — full records, each with a demo program"\n' +
    '  ];\n' +
    '}\n' +
    'var starter=[\n' +
    '  "/* generator for "+SLUG+" — deterministic: same seed → same record */",\n' +
    '  "function generate(seed){",\n' +
    '  "  return { id:\\"PREFIX-\\"+String(seed).padStart(6,\\"0\\"), title:\\"Record \\"+seed };",\n' +
    '  "}",\n' +
    '  "function validate(r){ return { ok: !!r.id && !!r.title, errors: [] }; }"\n' +
    '].join("\\n");\n' +
    'console.log("Pattern: "+PATTERN);\n' +
    'console.log("--- scaffold files ---");\n' +
    'files().forEach(function(f){console.log("  "+f);});\n' +
    'console.log("--- starter generator (copy-paste ready) ---");\n' +
    'console.log(starter);\n' +
    'console.log("Try: files() to list the scaffold again.");\n' +
    '})();\n';
  return { kind: 'scaffold', title: 'Database scaffold demo — ' + trunc(titleOf(rec), 50), program: prog, language: 'javascript' };
});

/* --- apple: product spec program --- */
pc('apple', function (slug, rec) {
  var prog = header(slug, rec, 'Spec-sheet program: prints the full spec card and compares key specs.') +
    '(function(){\n' +
    'var R=' + jsq({ name: rec.signature_name || rec.title, alludes_to: rec.alludes_to, category: rec.category, year: rec.year, specs: rec.specs, description: trunc(rec.description || '', 260) }, 1400) + ';\n' +
    'console.log("=== "+R.name+" ===");\n' +
    'if(R.alludes_to)console.log("Signature-line edition · alludes to: "+R.alludes_to);\n' +
    'console.log("Category: "+R.category+(R.year?" · Year: "+R.year:""));\n' +
    'console.log("--- specs ---");\n' +
    'Object.keys(R.specs||{}).forEach(function(k){console.log("  "+k+": "+R.specs[k]);});\n' +
    'console.log("--- description ---");\n' +
    'console.log(R.description);\n' +
    '})();\n';
  return { kind: 'product', title: 'Product spec demo — ' + trunc(titleOf(rec), 50), program: prog, language: 'javascript' };
});

/* --- code-database / code-problems: runnable code --- */
function codeBuilderFor(slug) {
  return function (slug2, rec) {
    var c = collect(rec);
    var cf = c.codes[0] || { k: 'code', v: String(rec.code || '') };
    var lang = detectLang(rec, cf.v);
    var code = cf.v;
    var runHint, runnerNote;
    if (lang === 'javascript') {
      runHint = 'PC: save as demo.js, run `node demo.js`. In-page: press Run.';
      runnerNote = '';
    } else if (lang === 'python') {
      runHint = 'PC: save as demo.py, run `python3 demo.py`.';
      runnerNote = '';
    } else if (lang === 'sql') {
      runHint = 'PC: save as demo.sql, run `sqlite3 :memory: < demo.sql`.';
      runnerNote = '';
    } else { runHint = 'PC: save the file with a .' + lang + ' extension and run with its toolchain.'; runnerNote = ''; }
    var prog;
    if (lang === 'javascript') {
      prog = header(slug, rec, 'Runnable code from this record ("' + cf.k + '") — executes with console output captured.') +
        '(function(){\n' +
        '"use strict";\n' +
        '/* ---- record code (' + cf.k + ') ---- */\n' +
        code + '\n' +
        '/* ---- auto-run: call main/demo/solve if the snippet defines one ---- */\n' +
        'try{\n' +
        '  if(typeof main==="function"){console.log("--- main() output ---");main();}\n' +
        '  else if(typeof demo==="function"){console.log("--- demo() output ---");demo();}\n' +
        '  else if(typeof solve==="function"){console.log("--- solve() output ---");console.log(solve());}\n' +
        '}catch(e){console.log("runtime note: "+e.message);}\n' +
        '})();\n';
    } else {
      prog = '# JAH demo program — ' + VERSION + '\n' +
        '# Database: ' + slug + ' · Record: ' + idOf(rec) + '\n' +
        '# RUN: ' + runHint + '\n\n' + code + '\n';
    }
    var tc = Array.isArray(rec.test_cases) ? rec.test_cases.slice(0, 4) : [];
    return {
      kind: 'code', title: 'Runnable code demo — ' + trunc(titleOf(rec), 50),
      program: prog, language: lang, run_hint: runHint,
      test_cases: tc, how_it_works: trunc(rec.how_it_works || '', 300)
    };
  };
}
pc('code-database', codeBuilderFor('code-database'));
pc('code-problems', codeBuilderFor('code-problems'));
['basic-programmes-published', 'basic-programmes-study',
 'electronics-automation-published', 'electronics-automation-study',
 'software-development-published', 'software-development-study'
].forEach(function (s) { pc(s, codeBuilderFor(s)); });

/* ---------------- generic kind builders ---------------- */
function bExplore(slug, rec, c) {
  var keys = Object.keys(rec).filter(function (k) { return k.charAt(0) !== '_' && k !== 'demo'; }).slice(0, 14);
  var summary = {};
  keys.forEach(function (k) {
    var v = rec[k];
    summary[k] = typeof v === 'string' ? trunc(v, 200) : (isObj(v) ? { '(object keys)': Object.keys(v).slice(0, 8) } : (Array.isArray(v) ? '[array ×' + v.length + ']' : v));
  });
  var prog = header(slug, rec, 'Interactive record inspector: tours every field, with a searchable field index.') +
    '(function(){\n' +
    'var FIELDS=' + jsq(summary, 2500) + ';\n' +
    'var keys=Object.keys(FIELDS);\n' +
    'function show(i){var k=keys[i];if(k===undefined){console.log("no field "+i);return;}console.log("["+i+"] "+k+" ("+(typeof FIELDS[k])+"):");console.log("    "+JSON.stringify(FIELDS[k]).slice(0,300));}\n' +
    'function find(word){word=String(word).toLowerCase();var hits=keys.filter(function(k){return (k+" "+JSON.stringify(FIELDS[k])).toLowerCase().indexOf(word)>=0;});console.log("fields matching \\""+word+"\\": "+(hits.join(", ")||"(none)"));return hits;}\n' +
    'console.log("=== ' + trunc(titleOf(rec), 70).replace(/\\/g, '\\\\').replace(/"/g, '\\"') + ' ===");\n' +
    'console.log("Record ' + idOf(rec).replace(/"/g, '') + ' · "+keys.length+" fields:");\n' +
    'keys.forEach(function(k,i){console.log("  ["+i+"] "+k);});\n' +
    'console.log("--- field tour ---");\n' +
    'keys.forEach(function(k,i){show(i);});\n' +
    'try{globalThis.jahDemoAPI={show:show,find:find};}catch(e){}\n' +
    'console.log("Try: jahDemoAPI.show(0) · jahDemoAPI.find(\\"word\\")");\n' +
    '})();\n';
  return { kind: 'explore', title: 'Interactive record tour — ' + trunc(titleOf(rec), 50), program: prog, language: 'javascript' };
}

function bChart(slug, rec, c) {
  var names = Object.keys(c.nums).slice(0, 10);
  var nums = {}; names.forEach(function (k) { nums[k] = c.nums[k]; });
  var prog = header(slug, rec, 'Charts this record\'s numeric fields as ASCII bars with summary statistics.') +
    '(function(){\n' +
    'var N=' + jsq(nums) + ';\n' +
    'var ks=Object.keys(N);\n' +
    'var mx=Math.max.apply(null,ks.map(function(k){return Math.abs(N[k]);}).concat([1]));\n' +
    'function bar(k){var v=N[k];var n=Math.round(Math.abs(v)/mx*36);console.log(k.padEnd(18," ").slice(0,18)+" | "+(v<0?"-":"")+"#".repeat(n)+" "+v);}\n' +
    'console.log("=== ' + trunc(titleOf(rec), 70).replace(/\\/g, '\\\\').replace(/"/g, '\\"') + ' ===");\n' +
    'ks.forEach(bar);\n' +
    'var vs=ks.map(function(k){return N[k];});\n' +
    'var sum=vs.reduce(function(a,b){return a+b;},0);\n' +
    'console.log("--- stats ---");\n' +
    'console.log("count "+vs.length+" · sum "+(+sum.toFixed(4))+" · mean "+(+(sum/vs.length).toFixed(4))+" · max "+Math.max.apply(null,vs)+" · min "+Math.min.apply(null,vs));\n' +
    'function whatif(f){console.log("scaled ×"+f+":");ks.forEach(function(k){console.log("  "+k+": "+N[k]+" → "+(+(N[k]*f).toFixed(4)));});}\n' +
    'try{globalThis.jahDemoAPI={whatif:whatif};}catch(e){}\n' +
    'console.log("Try: jahDemoAPI.whatif(2)  — scales every value and re-prints.");\n' +
    '})();\n';
  return { kind: 'chart', title: 'Data chart demo — ' + trunc(titleOf(rec), 50), program: prog, language: 'javascript' };
}

function bSim(slug, rec, c) {
  var arr = c.stepArr.slice(0, 16), key = c.stepKey;
  var steps = arr.map(function (s, i) {
    if (isObj(s)) return { n: i + 1, label: trunc(String(s.title || s.name || s.action || s.tool || s.label || s.step || ('step ' + (i + 1))), 70), detail: trunc(String(s.description || s.result || s.text || s.detail || JSON.stringify(s)).slice(0, 140), 140) };
    return { n: i + 1, label: trunc(String(s), 70), detail: '' };
  });
  var prog = header(slug, rec, 'Step-by-step simulation of "' + key + '" (' + steps.length + ' steps).') +
    '(function(){\n' +
    'var STEPS=' + jsq(steps, 3500) + ';\n' +
    'function render(i){\n' +
    '  var s=STEPS[i];if(!s){console.log("no step "+i);return;}\n' +
    '  var pct=Math.round(((i+1)/STEPS.length)*100);\n' +
    '  var filled=Math.round(pct/5), bar2="█".repeat(filled)+"░".repeat(20-filled);\n' +
    '  console.log("\\n[step "+s.n+"/"+STEPS.length+"] "+bar2+" "+pct+"%");\n' +
    '  console.log("  "+s.label);\n' +
    '  if(s.detail)console.log("  → "+s.detail);\n' +
    '}\n' +
    'console.log("Simulating ' + key.replace(/"/g, '') + ' — "+STEPS.length+" steps");\n' +
    'for(var i=0;i<STEPS.length;i++)render(i);\n' +
    'try{globalThis.jahDemoAPI={render:render};}catch(e){}\n' +
    'console.log("\\nSimulation complete ✓  Try: jahDemoAPI.render(0) to replay step 1.");\n' +
    '})();\n';
  return { kind: 'simulate', title: 'Step simulation — ' + trunc(titleOf(rec), 50), program: prog, language: 'javascript' };
}

function longTextOf(rec, c) {
  var best = c.texts.slice().sort(function (a, b) { return b.v.length - a.v.length; })[0] || null;
  ['chapters', 'pages', 'sections', 'entries'].forEach(function (k) {
    var arr = rec[k];
    if (Array.isArray(arr) && arr.length) {
      var txt = arr.slice(0, 2).map(function (ch) {
        if (typeof ch === 'string') return ch;
        if (isObj(ch)) return String(ch.text || ch.content || ch.body || ch.b || ch.dialogue || ch.caption || ch.t || '');
        return '';
      }).join('\n\n');
      if (txt.length > (best ? best.v.length : 400)) best = { k: k + '[0..1]', v: txt };
    }
  });
  return best || { k: 'text', v: '' };
}
function bRead(slug, rec, c) {
  var t = longTextOf(rec, c);
  var words = t.v.split(/\s+/).filter(Boolean);
  var freq = {};
  words.forEach(function (w) {
    w = w.toLowerCase().replace(/[^a-z0-9'-]/g, '');
    if (w.length > 3) freq[w] = (freq[w] || 0) + 1;
  });
  var top = Object.keys(freq).sort(function (a, b) { return freq[b] - freq[a]; }).slice(0, 8);
  var sentences = t.v.split(/[.!?]+/).filter(function (s) { return s.trim().length > 10; });
  var prog = header(slug, rec, 'Text analysis + guided reading of this record\'s main text field ("' + t.k + '").') +
    '(function(){\n' +
    'var TEXT=' + jsq(trunc(t.v, 1800)) + ';\n' +
    'var words=TEXT.split(/\\s+/).filter(Boolean);\n' +
    'var sents=TEXT.split(/[.!?]+/).filter(function(s){return s.trim().length>10;});\n' +
    'console.log("=== ' + trunc(titleOf(rec), 70).replace(/\\/g, '\\\\').replace(/"/g, '\\"') + ' ===");\n' +
    'console.log("field: ' + t.k.replace(/"/g, '') + ' · "+words.length+" words · "+sents.length+" sentences · ~"+Math.max(1,Math.round(words.length/200))+" min read");\n' +
    'console.log("top words: ' + top.join(', ') + '");\n' +
    'console.log("--- guided read (first 5 sentences) ---");\n' +
    'sents.slice(0,5).forEach(function(s,i){console.log((i+1)+". "+s.trim().slice(0,160));});\n' +
    'if(sents.length>5)console.log("… +"+(sents.length-5)+" more sentences in the full record.");\n' +
    '})();\n';
  return { kind: 'read', title: 'Guided reading demo — ' + trunc(titleOf(rec), 50), program: prog, language: 'javascript' };
}

/* ---------------- main build ---------------- */
function kindFor(slug, rec, c) {
  if (PC_BUILDERS[slug]) return 'pc:' + slug;
  if (c.codes.length) return 'code';
  if (c.stepArr) return 'simulate';
  if (Object.keys(c.nums).length >= 3) return 'chart';
  if (c.texts.some(function (t) { return t.v.length >= 500; })) return 'read';
  var lt = null;
  try { lt = longTextOf(rec, c); } catch (e) {}
  if (lt && lt.v && lt.v.length >= 500) return 'read';
  return 'explore';
}

function build(slug, rec) {
  try {
    slug = String(slug || 'db');
    rec = rec || {};
    if (PC_BUILDERS[slug]) {
      var r = PC_BUILDERS[slug](slug, rec);
      if ((r.language || 'javascript') === 'javascript' && r.kind === 'code' && !smokeTest(r.program)) {
        r = bExplore(slug, rec, collect(rec));
      }
      return finalize(r, slug, rec);
    }
    var c = collect(rec);
    var kind = kindFor(slug, rec, c);
    var out;
    if (kind === 'code') {
      out = codeBuilderFor(slug)(slug, rec);
      if ((out.language || 'javascript') === 'javascript' && !smokeTest(out.program)) {
        out = bExplore(slug, rec, c); /* record text only looked like code */
      }
    }
    else if (kind === 'simulate') out = bSim(slug, rec, c);
    else if (kind === 'chart') out = bChart(slug, rec, c);
    else if (kind === 'read') out = bRead(slug, rec, c);
    else out = bExplore(slug, rec, c);
    return finalize(out, slug, rec);
  } catch (e) {
    return {
      engine: VERSION, kind: 'explore', language: 'javascript', runnable: true,
      title: 'Demo — ' + idOf(rec),
      program: '/* demo builder note: ' + String(e.message).slice(0, 120) + ' */\nconsole.log(' + jsq('Record ' + idOf(rec)) + ');',
      how_to_run: HOW
    };
  }
}
var HOW = 'PC: save the program as demo.js (or demo.py/demo.sql per language) and run it with node/python3/sqlite3. In-page: open the record, Demo Lab tab, press Run.';
function finalize(r, slug, rec) {
  return {
    engine: VERSION,
    kind: r.kind,
    title: r.title,
    language: r.language || 'javascript',
    program: r.program,
    run_hint: r.run_hint || HOW,
    how_to_run: HOW,
    runnable: true,
    extras: r.test_cases ? { test_cases: r.test_cases } : undefined,
    note: r.how_it_works ? trunc(r.how_it_works, 300) : undefined
  };
}

/* ---------------- in-page sandboxed runner ---------------- */
var UNSAFE = [/while\s*\(\s*true\s*\)/, /for\s*\(\s*;\s*;\s*\)/, /process\.exit/, /require\s*\(/];
/* Build-time smoke test (Node only): runs the generated JS in a 1.5s-timeout vm
   sandbox. Anything that throws or hangs -> caller falls back to a safe
   explore demo. Never runs in the browser. */
/* Node only: async record code (e.g. an invoked async fn) can reject AFTER the
   synchronous smoke test finishes. Swallow those late rejections so batch
   harnesses never crash; the demo program itself is still the record's code. */
try {
  if (typeof process !== 'undefined' && process.on && !process._jahDemoGuard) {
    process._jahDemoGuard = 1;
    process.on('unhandledRejection', function () {});
  }
} catch (e) {}
var _vm = undefined;
function getVM() {
  if (_vm !== undefined) return _vm;
  _vm = null;
  try { if (typeof require === 'function') _vm = require('vm'); } catch (e) {}
  return _vm;
}
function smokeTest(program) {
  var vm = getVM();
  if (!vm) return true;
  try {
    var n = 0;
    var sandbox = { console: { log: function () { if (++n > 800) throw new Error('output cap'); }, warn: function () {}, error: function () {}, info: function () {} } };
    vm.runInNewContext('"use strict";\n' + program, sandbox, { timeout: 1500 });
    return true;
  } catch (e) { return false; }
}
function safeToRun(program) {
  if (typeof program !== 'string') return { ok: false, reason: 'not a program' };
  for (var i = 0; i < UNSAFE.length; i++) {
    if (UNSAFE[i].test(program)) return { ok: false, reason: 'needs review before running (unbounded loop / system call?)' };
  }
  return { ok: true };
}
function fmtArg(a) {
  if (typeof a === 'string') return a;
  try { return JSON.stringify(a); } catch (e) { return String(a); }
}
function runProgram(program, outEl) {
  var lines = [];
  function push(prefix, args) { lines.push(prefix + Array.prototype.map.call(args, fmtArg).join(' ')); }
  var fake = {
    log: function () { push('', arguments); },
    info: function () { push('', arguments); },
    warn: function () { push('⚠ ', arguments); },
    error: function () { push('✗ ', arguments); }
  };
  var chk = safeToRun(program);
  if (!chk.ok) {
    outEl.innerHTML = '<p class="bad">Not auto-run: ' + escH(chk.reason) + '. Copy the program and run it on your PC.</p>';
    return;
  }
  try {
    new Function('console', '"use strict";\n' + program)(fake);
  } catch (e) {
    lines.push('✗ runtime error: ' + e.message);
  }
  if (!lines.length) lines.push('(program ran — no output)');
  outEl.innerHTML = '<pre class="steps">' + escH(lines.join('\n').slice(0, 20000)) + '</pre>';
}

/* ---------------- Demo Lab page UI (auto-init) ---------------- */
function demoCardHTML(spec, rec) {
  var lang = spec.language || 'javascript';
  var ext = lang === 'python' ? 'py' : (lang === 'sql' ? 'sql' : 'js');
  return '<div class="card"><div class="rec"><div style="flex:1;min-width:0">' +
    '<h3 class="mono" style="font-size:1.05em">▶ ' + escH(spec.title || 'Demo') + '</h3>' +
    '<div><span class="badge">' + escH(idOf(rec)) + '</span>' +
    '<span class="badge ok">' + escH(spec.kind || 'demo') + '</span>' +
    '<span class="badge">' + escH(lang) + '</span>' +
    (spec.runnable ? '<span class="badge ok">runnable as-is</span>' : '') + '</div>' +
    '<p class="dim">' + escH(spec.run_hint || HOW) + '</p>' +
    '<div class="row">' +
    '<button class="go" data-jahrun>Run interactive demo</button>' +
    '<button data-jahview>View program</button>' +
    '<button data-jahcopy>Copy program</button>' +
    '<button data-jahdl data-ext="' + ext + '">Download demo.' + ext + '</button>' +
    '</div>' +
    '<div data-jahout style="margin-top:8px"></div>' +
    '<details class="grp" data-jahprog style="display:none"><summary>Demo program source</summary><pre class="steps"></pre></details>' +
    '</div></div></div>';
}
function currentSpec(card) { return card._jahSpec; }
function wireCard(card, spec, rec) {
  card._jahSpec = spec; card._jahRec = rec;
  function q(s) { return card.querySelector(s); }
  q('[data-jahrun]').addEventListener('click', function () {
    if ((spec.language || 'javascript') !== 'javascript') {
      q('[data-jahout]').innerHTML = '<p class="dim">' + escH(spec.run_hint || HOW) + '</p>';
      return;
    }
    runProgram(spec.program, q('[data-jahout]'));
  });
  q('[data-jahview]').addEventListener('click', function () {
    var d = q('[data-jahprog]');
    d.style.display = d.style.display === 'none' ? '' : 'none';
    d.querySelector('pre').textContent = spec.program;
  });
  q('[data-jahcopy]').addEventListener('click', function (e) {
    var b = e.target, done = function (ok) { b.textContent = ok ? '✓ Copied' : 'Copy failed'; setTimeout(function () { b.textContent = 'Copy program'; }, 1500); };
    if (navigator.clipboard && navigator.clipboard.writeText) navigator.clipboard.writeText(spec.program).then(function () { done(true); }, function () { done(false); });
    else { var ta = document.createElement('textarea'); ta.value = spec.program; document.body.appendChild(ta); ta.select(); try { done(document.execCommand('copy')); } catch (x) { done(false); } document.body.removeChild(ta); }
  });
  q('[data-jahdl]').addEventListener('click', function (e) {
    var ext = e.target.getAttribute('data-ext') || 'js';
    var blob = new Blob([spec.program], { type: 'text/plain' });
    var a = document.createElement('a');
    a.href = URL.createObjectURL(blob);
    a.download = 'demo-' + idOf(rec).replace(/[^A-Za-z0-9_-]+/g, '_') + '.' + ext;
    document.body.appendChild(a); a.click();
    setTimeout(function () { URL.revokeObjectURL(a.href); a.remove(); }, 600);
  });
}
function renderDemoInto(box, spec, rec) {
  box.innerHTML = demoCardHTML(spec, rec);
  wireCard(box.firstChild, spec, rec);
  var runBtn = box.querySelector('[data-jahrun]');
  if (runBtn) runBtn.click();
}

function initPage() {
  try {
    var pane = document.getElementById('p-demo');
    if (!pane || pane.dataset.jahwired) return;
    pane.dataset.jahwired = '1';
    var slug = (typeof window.SLUG === 'string' && window.SLUG) || 'db';
    var seedEl = document.getElementById('dSeed');
    var outEl = document.getElementById('dOut');
    function needIds() { return document.getElementById('dOut'); }
    function doGenerate() {
      var out = needIds(); if (!out) return;
      var seed = Math.max(1, parseInt(seedEl.value, 10) || 1);
      var gen = (window.JAHDB && JAHDB.getGenerator) ? JAHDB.getGenerator(slug) : null;
      if (!gen || !JAHDB.runGenerator) { out.innerHTML = '<p class="bad">Generator not loaded on this page.</p>'; return; }
      var r = JAHDB.runGenerator(slug, seed, {});
      if (!r.ok) { out.innerHTML = '<p class="bad">Generate failed: ' + escH(r.errors.join('; ')) + '</p>'; return; }
      var spec = r.record.demo || build(slug, r.record);
      renderDemoInto(out, spec, r.record);
      try { seedEl.value = seed + 1; } catch (e) {}
    }
    function chunkUrlFor(c) {
      try {
        if (typeof window.chunkName === 'function') {
          var local = (typeof window.LOCAL === 'string' && window.LOCAL) || '../../data/' + slug + '/';
          return local + window.chunkName(c);
        }
      } catch (e) {}
      return null;
    }
    function doRandom() {
      var out = needIds(); if (!out) return;
      var idx = window.archiveIdx;
      if (!idx || !idx.length) { out.innerHTML = '<p class="dim">Archive index not loaded on this page — use Generate instead.</p>'; return; }
      var pick = idx[(Math.random() * idx.length) | 0];
      fetchChunkAndDemo(pick, out);
    }
    function fetchChunkAndDemo(ix, out) {
      var url = chunkUrlFor(ix.c);
      if (!url) { out.innerHTML = '<p class="dim">Chunk addressing unavailable here — use Generate instead.</p>'; return; }
      out.innerHTML = '<p class="dim">Loading record ' + escH(ix.id) + '…</p>';
      JAHDB.fetchJsonlGz(url).then(function (recs) {
        var r = null;
        for (var i = 0; i < recs.length; i++) if (recs[i].id === ix.id) { r = recs[i]; break; }
        if (!r) { out.innerHTML = '<p class="bad">Record not found in chunk.</p>'; return; }
        renderDemoInto(out, r.demo || build(slug, r), r);
      }).catch(function (e) { out.innerHTML = '<p class="bad">Load failed: ' + escH(e.message) + '</p>'; });
    }
    function doFind() {
      var out = needIds(); if (!out) return;
      var qEl = document.getElementById('dFind');
      var q = (qEl.value || '').trim().toLowerCase();
      if (!q) return;
      var idx = window.archiveIdx;
      if (!idx || !idx.length) { out.innerHTML = '<p class="dim">Archive index not loaded — use Generate instead.</p>'; return; }
      var hit = null;
      for (var i = 0; i < idx.length; i++) {
        if (String(idx[i].id).toLowerCase() === q || String(idx[i].t || '').toLowerCase().indexOf(q) >= 0) { hit = idx[i]; break; }
      }
      if (!hit) { out.innerHTML = '<p class="bad">No archive record matches "' + escH(q) + '".</p>'; return; }
      fetchChunkAndDemo(hit, out);
    }
    var b;
    b = document.getElementById('dGen'); if (b) b.addEventListener('click', doGenerate);
    b = document.getElementById('dRand'); if (b) b.addEventListener('click', doRandom);
    b = document.getElementById('dFindGo'); if (b) b.addEventListener('click', doFind);
    var f = document.getElementById('dFind');
    if (f) f.addEventListener('keydown', function (e) { if (e.key === 'Enter') doFind(); });
    if (seedEl) seedEl.addEventListener('keydown', function (e) { if (e.key === 'Enter') doGenerate(); });
  } catch (e) { /* never break the page */ }
}

var D = {
  version: VERSION,
  build: build,
  kindFor: kindFor,
  runProgram: runProgram,
  renderDemoInto: renderDemoInto,
  initPage: initPage
};

if (typeof document !== 'undefined') {
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', initPage);
  else initPage();
}
return D;
});
