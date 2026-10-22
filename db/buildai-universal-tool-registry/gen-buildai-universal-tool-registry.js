/*
 * Boundless generator for buildai-universal-tool-registry — item 179.
 * Dual node+browser: node prints JSONL records; browser registers with JAHDB.
 * Deterministic: same seed + topic = same record. HARD_CAP = 1e15.
 */
'use strict';
var SLUG = 'buildai-universal-tool-registry';
var PREFIX = 'JAH-BAI-';
var HARD_CAP = 1e15;
var ARCHETYPES = [{"kind": "capability-query", "title": "Querying the Registry by Capability", "body": "Capability queries are substring matches over every tool's capability list, case-insensitive. This archetype's demo runs the real matching logic on a miniature tool list at generation time and records the output.", "demoCode": "var tools=[{n:'node',c:['execute code','javascript runtime']},{n:'linter',c:['static analysis']}];return tools.filter(function(t){return t.c.join(' ').indexOf('code')>=0;}).map(function(t){return t.n;}).join(', ');", "ladder": "simple", "vstat": "tested", "caps": ["capability search"]}, {"kind": "name-lookup", "title": "Looking Up a Tool by Name", "body": "Name lookup is exact and case-insensitive. The generation-time demo resolves a name against a miniature registry and prints the capability list.", "demoCode": "var tools={node:['execute code'],git:['version control']};var k='NODE'.toLowerCase();return k+' -> '+(tools[k]||['not found']).join(', ');", "ladder": "simple", "vstat": "tested", "caps": ["name lookup"]}, {"kind": "status-ladder", "title": "Promoting a Tool Along the Status Ladder", "body": "Statuses move only through the six canonical values. The demo promotes a miniature entry and prints the result.", "demoCode": "var ok=['proposed','generated','executable','tested','independently-verified','verified-on-this-host'];var t={name:'demo',status:'proposed'};var next='tested';if(ok.indexOf(next)>=0)t.status=next;return t.name+' is now '+t.status;", "ladder": "competitive", "vstat": "tested", "caps": ["status lifecycle"]}, {"kind": "seed-provenance", "title": "Seed Entry Provenance", "body": "Seed entries carry their source: paste-derived entries are proposed, host-verified tools are verified-on-this-host. The demo counts a miniature seed set by status.", "demoCode": "var s=[{s:'proposed'},{s:'proposed'},{s:'verified-on-this-host'},{s:'tested'}];var c={};s.forEach(function(x){c[x.s]=(c[x.s]||0)+1;});return JSON.stringify(c);", "ladder": "simple", "vstat": "tested", "caps": ["provenance tracking"]}, {"kind": "schema-validation", "title": "Validating a Tool Record", "body": "The validator requires a name and restricts execution_status to the canonical list. The demo validates a bad record and prints the errors.", "demoCode": "function v(t){var e=[];if(!t.name)e.push('name required');return e;}return 'errors: '+v({}).join('; ');", "ladder": "simple", "vstat": "tested", "caps": ["schema validation"]}, {"kind": "duplicate-reject", "title": "Duplicate Names Are Rejected", "body": "Names are unique case-insensitively. The demo attempts a duplicate add on a miniature registry and prints the rejection.", "demoCode": "var names={node:1};var n='Node';var k=n.toLowerCase();return names[k]?'rejected duplicate: '+n:'added '+n;", "ladder": "competitive", "vstat": "tested", "caps": ["input rejection"]}, {"kind": "platform-filter", "title": "Filtering Tools by Platform", "body": "List filters slice by platform, status, or capability. The demo filters a miniature set by platform.", "demoCode": "var tools=[{n:'node',p:['linux','windows']},{n:'xcode',p:['macos']}];return tools.filter(function(t){return t.p.indexOf('linux')>=0;}).map(function(t){return t.n;}).join(', ');", "ladder": "competitive", "vstat": "tested", "caps": ["filtered listing"]}, {"kind": "paste-profile", "title": "Paste Entry Profile: Code Formatter", "body": "A verbatim capability from his 2026-10-21 tools paste (entry #7): proposed, not running software. No demo executes here; the record catalogs the proposal honestly.", "demoCode": "return 'cataloged as proposed: Code Formatter \u2014 automatically standardize code formatting';", "ladder": "simple", "vstat": "proposed", "caps": ["paste provenance"]}];

function mulberry32(a) {
  return function () {
    a |= 0; a = (a + 0x6D2B79F5) | 0;
    var t = Math.imul(a ^ (a >>> 15), 1 | a);
    t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t;
    return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
  };
}

function generate(seed, opts) {
  opts = opts || {};
  seed = Math.floor(Math.abs(Number(seed) || 1));
  var rng = mulberry32(seed);
  var ai = ARCHETYPES[Math.floor(rng() * ARCHETYPES.length)];
  var topic = opts.topic || 'the Signature engineering system';
  var idx = Math.floor(rng() * 1000);
  var demoOutput;
  try { demoOutput = String((new Function(ai.demoCode))()); }
  catch (e) { demoOutput = 'demo error: ' + String(e && e.message || e); }
  var title = ai.title + ' — ' + topic + ' #' + (idx + 1);
  return {
    id: PREFIX + 'G' + String(seed).padStart(4, '0') + '-' + String(idx).padStart(3, '0'),
    slug: SLUG, title: title, t: title, g: 'engineering systems', c: 1,
    description: ai.title + ': a generated record for ' + topic + '.',
    body: ai.body + ' This record was produced by the boundless generator for ' + topic +
      '; its demonstration ran at generation time and the captured output is stored below.',
    capabilities: ai.caps,
    demo: { program: ai.demoCode, output: demoOutput.slice(0, 2000) },
    provenance: 'Generated by the boundless generator for ' + SLUG + ' (item 179), seed ' + seed + '.',
    licensing: 'Original Signature software. Property of Justin Addam Higgins (JAH).',
    src: 'generated', edition: 'signature', ladder_rank: ai.ladder,
    generator: 'jahdb-buildai-universal-tool-registry-1.0', verification_status: ai.vstat,
    links: [], record_kind: 'tool registry record'
  };
}

function validate(r) {
  var errors = [];
  ['id', 'title', 'body', 'demo', 'src', 'edition', 'verification_status'].forEach(function (f) {
    if (r[f] === undefined || r[f] === null || r[f] === '') errors.push('missing ' + f);
  });
  if (r.demo && (r.demo.program === undefined || r.demo.output === undefined))
    errors.push('demo needs program and output');
  return { ok: errors.length === 0, errors: errors };
}

var api = { generate: generate, validate: validate, HARD_CAP: HARD_CAP, SLUG: SLUG };

if (typeof module !== 'undefined' && module.exports) module.exports = api;
if (typeof window !== 'undefined' && window.JAHDB && window.JAHDB.registerGenerator)
  window.JAHDB.registerGenerator(SLUG, api);
if (typeof process !== 'undefined' && process.argv && process.argv[1] &&
    process.argv[1].indexOf('gen-') >= 0) {
  (function main() {
    var n = 8, seed = 1, topic = null;
    var a = process.argv.slice(2);
    for (var i = 0; i < a.length; i++) {
      if (a[i] === '--n') n = parseInt(a[++i], 10);
      if (a[i] === '--seed') seed = parseInt(a[++i], 10);
      if (a[i] === '--topic') topic = a[++i];
    }
    if (!(n >= 1 && n <= HARD_CAP)) { console.error('n out of range'); process.exit(1); }
    for (var k = 0; k < n; k++) {
      var r = generate(seed + k, { topic: topic });
      var v = validate(r);
      if (!v.ok) { console.error('invalid record: ' + v.errors.join('; ')); process.exit(1); }
      console.log(JSON.stringify(r));
    }
  })();
}
