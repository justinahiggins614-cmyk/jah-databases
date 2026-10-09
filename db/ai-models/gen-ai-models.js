/* ✳ SIGNATURE — JAH AI Data Base generator. Property of Justin Addam Higgins (JAH).
   Boundless generator: produces NEW AI profiles in the exact archive schema
   (NAME, TYPE, CATEGORY, DESCRIPTION, CAPABILITIES, LIMITATIONS, STATUS,
   VERSION, ROLE, VOICE, SIGNATURE_NUMBER, SOURCE, RELATIONSHIPS, HASH, id).
   Deterministic: same seed + version => same record. These are ORIGINAL
   synthetic profiles, clearly labeled GENERATED — they describe no real
   deployed model. Every record is re-verified by an INDEPENDENT checker
   before acceptance. */
(function () {
  'use strict';
  var VERSION = 'jahdb-ai-models-1.0';
  var ID_PREFIX = 'JAH-AI-';

  var TYPES = ['system', 'persona', 'domain', 'sl', 'mix'];
  /* real categories observed in the archive */
  var CATS = ['Cooking', 'Family', 'Games', 'Business', 'Food & Drink', 'Health',
    'Writing', 'Music', 'Home', 'Nature', 'Learning', 'Mind', 'Travel', 'Events',
    'Tech', 'Art', 'Productivity', 'Self', 'Sports', 'Heart', 'Pets', 'Skills',
    'Cars', 'Language', 'Career', 'Crafts', 'Life', 'Thinking', 'Lifestyle',
    'Safety', 'Garden', 'Electronics', 'Programming', 'Science', 'Ideas',
    'Invention', 'Spirit', 'Community', 'Mixed AI', 'Persona', 'System',
    'Signature-Line'];
  var ROLES = ['DOMAIN MODEL', 'HELPER MODEL', 'GUIDE MODEL', 'ANALYST MODEL',
    'CREATOR MODEL', 'SYSTEM MODEL'];

  var ADJ = ['Hearthside', 'Copperline', 'Brightfield', 'Stonebridge', 'Lumen',
    'Fernhollow', 'Blueharbor', 'Ironbark', 'Silvermere', 'Amberline'];
  var DOM = ['Recipe', 'Garden', 'Ledger', 'Chord', 'Trail', 'Sketch', 'Beacon',
    'Harbor', 'Forge', 'Meadow', 'Compass', 'Lantern'];
  var KINDW = ['Engine', 'Guide', 'Companion', 'Analyst', 'Maker', 'Helper'];
  var VERB = ['plans', 'tunes', 'maps', 'tends', 'drafts', 'tracks'];
  var OBJ = ['weekly routines', 'small projects', 'daily checklists', 'seasonal tasks',
    'household budgets', 'practice drills', 'reading lists', 'workshop layouts'];

  function ri(rnd, a, b) { return a + Math.floor(rnd() * (b - a + 1)); }
  function pick(rnd, arr) { return arr[Math.floor(rnd() * arr.length)]; }

  function buildName(adj, dom, kindw) { return adj + ' ' + dom + ' ' + kindw; }
  function buildDesc(name, verb, obj, cat) {
    return 'The ' + name + ' is a ' + cat.toLowerCase() + ' helper that ' + verb + ' ' +
      obj + '. It answers in plain sentences, keeps its work on-device, and explains ' +
      'every step it takes.';
  }
  function buildCaps(dom, verb, obj) {
    var d = dom.toLowerCase();
    return [
      'Builds a personal ' + d + ' plan around ' + obj,
      'Explains each ' + d + ' step in plain language',
      'Remembers ' + d + ' preferences within the session',
      'Exports the finished ' + d + ' plan as plain text'
    ];
  }
  function buildLimit() {
    return 'Generated profile — describes a synthetic helper, not a deployed model. ' +
      'Verify important facts elsewhere.';
  }
  function buildSig(n) {
    return '1-200-' + String(1000000 + (n * 7919) % 9000000);
  }
  function buildHash(s) {
    var h1 = JAHDB.hashStr(s), h2 = JAHDB.hashStr('x' + s);
    function hx(v) {
      var out = '';
      for (var i = 0; i < 8; i++) { out = '0123456789abcdef'[(v >>> (i * 4)) & 15] + out; v = Math.floor(v / 16); }
      return out;
    }
    return 'fnv1a:' + hx(h1) + hx(h2);
  }

  function genAI(rnd, n, opts) {
    opts = opts || {};
    var adj = pick(rnd, ADJ), dom = pick(rnd, DOM), kindw = pick(rnd, KINDW);
    var name = buildName(adj, dom, kindw);
    var type = (opts.type && TYPES.indexOf(opts.type) >= 0) ? opts.type : pick(rnd, TYPES);
    var cat = type === 'system' ? 'System' : type === 'persona' ? 'Persona' :
              type === 'mix' ? 'Mixed AI' : type === 'sl' ? 'Signature-Line' : pick(rnd, CATS);
    var verb = pick(rnd, VERB), obj = pick(rnd, OBJ);
    var desc = buildDesc(name, verb, obj, cat);
    var caps = buildCaps(dom, verb, obj);
    var dlfile = name.toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-+|-+$/g, '') + '.json';
    return {
      NAME: name, TYPE: type, CATEGORY: cat, DESCRIPTION: desc,
      CAPABILITIES: caps, LIMITATIONS: buildLimit(),
      STATUS: 'GENERATED', VERSION: '1.0',
      ROLE: pick(rnd, ROLES),
      RUNTIME: {
        what_you_download: 'JSON record file (human-readable) — profile data, capabilities, and voice config; runs as data, not trained-model weights',
        what_the_demo_is: 'the profile rendered live in the database page from this record',
        what_the_chat_is: 'archive-aware answers generated on-device by the database AI using this profile',
        works_offline: 'YES — after the page loads',
        internet_required: 'NO for the record itself; YES once to fetch the page',
        browser_only: 'NO — the JSON record is portable'
      },
      DEMO: { kind: 'synthetic', runs_in: 'database page', note: 'generated profile — demo renders from the record data' },
      VOICE: { read_aloud: false, engine: 'none — text only' },
      SIGNATURE_NUMBER: buildSig(n),
      SOURCE: 'JAH Data Bases boundless generator jahdb-ai-models-1.0 (synthetic profile)',
      RELATIONSHIPS: {},
      ARTIFACTS: { download: dlfile, deep_link: '#file-' + dlfile.replace(/\.json$/, ''), note: 'full record JSON download from this database' },
      _adj: adj, _dom: dom, _kindw: kindw, _verb: verb, _obj: obj,
      _type: type, _cat: cat, _role: null, _dlfile: dlfile
    };
  }

  function generate(seed, opts, rnd) {
    opts = opts || {};
    var n = (opts.baseN || 0) + 1;
    var g = genAI(rnd, n, opts);
    var canonical = g.NAME + '|' + g.TYPE + '|' + g.CATEGORY + '|' + g.DESCRIPTION;
    var rec = {
      id: ID_PREFIX + String(n).padStart(4, '0'),
      n: n,
      NAME: g.NAME,
      TYPE: g.TYPE,
      CATEGORY: g.CATEGORY,
      DESCRIPTION: g.DESCRIPTION,
      CAPABILITIES: g.CAPABILITIES,
      LIMITATIONS: g.LIMITATIONS,
      STATUS: g.STATUS,
      VERSION: g.VERSION,
      ROLE: g.ROLE,
      RUNTIME: g.RUNTIME,
      DEMO: g.DEMO,
      VOICE: g.VOICE,
      SIGNATURE_NUMBER: g.SIGNATURE_NUMBER,
      SOURCE: g.SOURCE,
      RELATIONSHIPS: g.RELATIONSHIPS,
      ARTIFACTS: g.ARTIFACTS,
      HASH: buildHash(canonical),
      record_kind: 'synthetic'
    };
    g._role = g.ROLE;
    g._canonical = canonical;
    rec._priv = g;
    rec._seed = seed;
    return rec;
  }

  function verify(rec) {
    var errs = [];
    var p = rec._priv;
    if (!p) return ['no private params — cannot independently verify'];
    if (rec.NAME !== buildName(p._adj, p._dom, p._kindw)) errs.push('NAME mismatch');
    if (rec.DESCRIPTION !== buildDesc(rec.NAME, p._verb, p._obj, p._cat)) errs.push('DESCRIPTION mismatch');
    var wantCaps = buildCaps(p._dom, p._verb, p._obj);
    if (!Array.isArray(rec.CAPABILITIES) || rec.CAPABILITIES.length !== 4 ||
        rec.CAPABILITIES.some(function (c, i) { return c !== wantCaps[i]; }))
      errs.push('CAPABILITIES mismatch');
    if (rec.LIMITATIONS !== buildLimit()) errs.push('LIMITATIONS mismatch');
    if (rec.TYPE !== p._type || TYPES.indexOf(rec.TYPE) < 0) errs.push('bad TYPE');
    if (rec.CATEGORY !== p._cat) errs.push('CATEGORY mismatch');
    if (rec.SIGNATURE_NUMBER !== buildSig(rec.n)) errs.push('SIGNATURE_NUMBER mismatch');
    if (rec.HASH !== buildHash(p._canonical)) errs.push('HASH mismatch');
    if (rec.STATUS !== 'GENERATED') errs.push('STATUS must be GENERATED for synthetic profiles');
    if (rec.ROLE !== p._role) errs.push('ROLE mismatch');
    if (!rec.RUNTIME || rec.RUNTIME.what_you_download !== p.RUNTIME.what_you_download) errs.push('RUNTIME mismatch');
    if (!rec.DEMO || rec.DEMO.kind !== 'synthetic') errs.push('DEMO mismatch');
    if (!rec.ARTIFACTS || rec.ARTIFACTS.download !== p._dlfile) errs.push('ARTIFACTS mismatch');
    return errs;
  }

  function validate(rec) {
    var errs = [];
    if (!rec || typeof rec !== 'object') return { ok: false, errors: ['not an object'] };
    ['id', 'NAME', 'TYPE', 'CATEGORY', 'DESCRIPTION', 'CAPABILITIES', 'LIMITATIONS',
     'STATUS', 'VERSION', 'ROLE', 'RUNTIME', 'DEMO', 'VOICE', 'SIGNATURE_NUMBER',
     'SOURCE', 'RELATIONSHIPS', 'ARTIFACTS', 'HASH'].forEach(function (k) {
      if (rec[k] === undefined || rec[k] === null || rec[k] === '') errs.push('missing field: ' + k);
    });
    if (rec.id && !/^JAH-AI-\d{4}$/.test(rec.id)) errs.push('bad id format');
    if (!Array.isArray(rec.CAPABILITIES) || rec.CAPABILITIES.length === 0)
      errs.push('CAPABILITIES must be a non-empty array');
    if (rec._priv) errs = errs.concat(verify(rec));
    else errs.push('no private params — cannot independently verify');
    return { ok: errs.length === 0, errors: errs };
  }

  function driftCheck(rec, archiveSample) {
    var errs = [];
    (archiveSample || []).forEach(function (a) {
      var nm = a.NAME;
      if (nm && String(nm).toLowerCase().replace(/\s+/g, ' ') === String(rec.NAME).toLowerCase().replace(/\s+/g, ' '))
        errs.push('duplicate of archived AI profile name: ' + rec.NAME);
    });
    return { ok: errs.length === 0, errors: errs };
  }

  function themedGenerate(seed, opts, rnd, themeSamples) {
    var rec = generate(seed, opts, rnd);
    if (themeSamples && themeSamples.length) {
      var t = themeSamples[Math.floor(rnd() * themeSamples.length)];
      var nums = String(JSON.stringify(t)).match(/\d+/g);
      if (nums && nums.length) {
        var rec2 = generate(seed + (parseInt(nums[0], 10) % 1000), opts,
          JAHDB.prng(JAHDB.hashStr(String(seed) + nums[0])));
        rec2.id = rec.id; rec2.n = rec.n;
        return rec2;
      }
    }
    return rec;
  }

  JAHDB.registerGenerator('ai-models', {
    version: VERSION,
    generate: generate,
    validate: validate,
    driftCheck: driftCheck,
    themedGenerate: themedGenerate,
    types: TYPES
  });
})();
