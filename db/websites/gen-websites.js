/* ✳ SIGNATURE — JAH Website Data Base generator. Property of Justin Addam Higgins (JAH).
   Boundless generator: produces NEW website build-concept records in the exact
   format of the Creator's option archive (name, cat, style, palette, desc),
   built from the same deterministic category/style/word pools. Generated ids
   live in the JAH-SITE- space and can never collide with the JAH-TPL- option
   ids. Deterministic: same seed + version => same record. An independent
   verifier rebuilds the name and description from the private pool indices
   before acceptance. */
(function () {
  'use strict';
  var VERSION = 'jahdb-websites-1.0';
  var ID_PREFIX = 'JAH-SITE-';
  var ID_DIGITS = 6;

  /* pools from the Creator's deterministic option generator (builder4.js) */
  var OPT_CATS = [
    'Bakery & Food', 'Portfolio', 'Blog & Writing', 'Local Business', 'Online Store',
    'Restaurant', 'Photography', 'Music & Band', 'Fitness & Health', 'Real Estate',
    'Salon & Beauty', 'Auto & Repair', 'Pet Care', 'Kids & Family', 'Education',
    'Nonprofit', 'Church & Faith', 'Events & Parties', 'Travel & Tours', 'Tech & Apps'
  ];
  var OPT_STYLES = ['Cozy Classic', 'Bold Modern', 'Soft Pastel', 'Dark Neon',
    'Sunny Bright', 'Earthy Calm', 'Ocean Fresh', 'Royal Gold'];
  var ADJ = ['Sunny', 'Golden', 'Happy', 'Bright', 'Cozy', 'Swift', 'Clever', 'Kind',
    'Lucky', 'Merry', 'Noble', 'Prime', 'Rapid', 'Shiny', 'True', 'Vivid', 'Warm', 'Zesty'];
  var NOUN = ['Corner', 'House', 'Studio', 'Works', 'Place', 'Hub', 'Spot', 'Nest',
    'Garden', 'Harbor', 'Lane', 'Market', 'Point', 'Post', 'Shop', 'Station'];
  var OPT_PALETTES = [
    ['#16264a', '#59d6ff'], ['#3a1b4a', '#f0a6ff'], ['#0f3a2e', '#5ff2b8'],
    ['#4a2a10', '#ffc46b'], ['#33122b', '#ff8fb2'], ['#122a4a', '#8fd0ff'],
    ['#2a1a08', '#ffd166'], ['#0e2a3a', '#7ef0d4']
  ];

  function pickI(rnd, n) { return Math.floor(rnd() * n); }
  function catWord(cat) { return cat.split(' ')[0].replace('&', '').trim(); }
  function buildName(ai, ci, ni) {
    return (ADJ[ai] + ' ' + catWord(OPT_CATS[ci]) + ' ' + NOUN[ni]).replace(/\s+/g, ' ').trim();
  }
  function buildDesc(si, ci) {
    return 'A ' + OPT_STYLES[si].toLowerCase() + ' ' + OPT_CATS[ci].toLowerCase() +
      ' website build. Hero, intro, tab bar, archive and contact page included \u2014 ready to build.';
  }

  function generate(seed, opts, rnd) {
    opts = opts || {};
    var ci = pickI(rnd, OPT_CATS.length), si = pickI(rnd, OPT_STYLES.length);
    if (opts.type && OPT_CATS.indexOf(opts.type) >= 0) ci = OPT_CATS.indexOf(opts.type);
    var ai = pickI(rnd, ADJ.length), ni = pickI(rnd, NOUN.length), pi = pickI(rnd, OPT_PALETTES.length);
    var n = (opts.baseN || 0) + 1;
    var pub = {
      id: ID_PREFIX + String(n).padStart(ID_DIGITS, '0'),
      n: n,
      kind: 'build-concept',
      name: buildName(ai, ci, ni),
      cat: OPT_CATS[ci],
      style: OPT_STYLES[si],
      palette: OPT_PALETTES[pi].slice(),
      desc: buildDesc(si, ci),
      origin: 'generated',
      stamp: 'JAH Website Data Base — generated website build-concept record.'
    };
    pub._priv = { ci: ci, si: si, ai: ai, ni: ni, pi: pi, seed: seed };
    return pub;
  }

  function validate(rec) {
    var errs = [];
    if (!rec || typeof rec !== 'object') return { ok: false, errors: ['not an object'] };
    ['id', 'kind', 'name', 'cat', 'style', 'palette', 'desc'].forEach(function (k) {
      if (rec[k] === undefined || rec[k] === null || rec[k] === '') errs.push('missing field: ' + k);
    });
    if (rec.id && !/^JAH-SITE-\d{6}$/.test(rec.id)) errs.push('bad id format');
    if (rec.kind && rec.kind !== 'build-concept') errs.push('kind must be build-concept');
    if (rec.cat && OPT_CATS.indexOf(rec.cat) < 0) errs.push('unknown category');
    if (rec.style && OPT_STYLES.indexOf(rec.style) < 0) errs.push('unknown style');
    if (rec._priv) {
      var p = rec._priv;
      var idxok = p.ci >= 0 && p.ci < OPT_CATS.length && p.si >= 0 && p.si < OPT_STYLES.length &&
                  p.ai >= 0 && p.ai < ADJ.length && p.ni >= 0 && p.ni < NOUN.length &&
                  p.pi >= 0 && p.pi < OPT_PALETTES.length;
      if (!idxok) errs.push('private pool indices out of range');
      else {
        if (rec.cat !== OPT_CATS[p.ci]) errs.push('cat does not match private pick');
        if (rec.style !== OPT_STYLES[p.si]) errs.push('style does not match private pick');
        if (rec.name !== buildName(p.ai, p.ci, p.ni)) errs.push('name does not rebuild from private picks');
        if (rec.desc !== buildDesc(p.si, p.ci)) errs.push('desc does not rebuild from private picks');
        if (!Array.isArray(rec.palette) || rec.palette[0] !== OPT_PALETTES[p.pi][0] || rec.palette[1] !== OPT_PALETTES[p.pi][1])
          errs.push('palette does not match private pick');
      }
    } else errs.push('no private params — cannot independently verify');
    return { ok: errs.length === 0, errors: errs };
  }

  /* drift check: generated ids live in the JAH-SITE- space, which the stored
     JAH-TPL- option archive never uses — verified against the sample */
  function driftCheck(rec, archiveSample) {
    var errs = [];
    (archiveSample || []).forEach(function (a) {
      var code = a.code || a.id;
      if (code && String(code) === String(rec.id)) errs.push('id duplicates an archived record');
    });
    if (!/^JAH-SITE-\d{6}$/.test(rec.id)) errs.push('generated id outside the JAH-SITE- space');
    return { ok: errs.length === 0, errors: errs };
  }

  /* cross-database: borrow a theme number from another database's sample */
  function themedGenerate(seed, opts, rnd, themeSamples) {
    var rec = generate(seed, opts, rnd);
    if (themeSamples && themeSamples.length) {
      var t = themeSamples[Math.floor(rnd() * themeSamples.length)];
      var nums = String(JSON.stringify(t)).match(/\d+/g);
      if (nums && nums.length) {
        var rec2 = generate(seed + (parseInt(nums[0], 10) % 1000), opts, JAHDB.prng(JAHDB.hashStr(String(seed) + nums[0])));
        rec2.id = rec.id; rec2.n = rec.n;
        return rec2;
      }
    }
    return rec;
  }

  JAHDB.registerGenerator('websites', {
    version: VERSION,
    generate: generate,
    validate: validate,
    driftCheck: driftCheck,
    themedGenerate: themedGenerate,
    types: OPT_CATS.slice()
  });
})();
