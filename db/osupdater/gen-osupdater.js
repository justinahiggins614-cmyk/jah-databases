/* ✳ SIGNATURE — JAH OS Update Data Base generator. Property of Justin Addam Higgins (JAH).
   Boundless generator: produces NEW upgrade-pack records in the exact archive
   format (id, title, era, os, focus, focus_label, components, blurb, best).
   The title, blurb and component sets are rebuilt from the archive's own
   per-focus pack names and templates, so every field is genuine. Deterministic:
   same seed + version => same record. An independent verifier rebuilds every
   claim from the private params before acceptance. */
(function () {
  'use strict';
  var VERSION = 'jahdb-osupdater-1.0';
  var ID_PREFIX = 'JAH-UPG-';
  var ID_DIGITS = 6;

  var ERAS = ['1990s', '2000s', '2010s', 'modern'];
  var OS = ['Windows', 'macOS', 'Linux'];
  var FOCUS = {
    'office':   { label: 'Office work',      pack: 'Office Renewal',
      blurb: 'Documents, email and video calls running smooth on your {era} {os} machine.' },
    'creative': { label: 'Creative work',    pack: 'Creator Refresh',
      blurb: 'Art, music and video tools refreshed for {era}-era {os}.' },
    'coding':   { label: 'Coding & building', pack: 'Builder Tune-Up',
      blurb: 'Editors, terminals and dev tools tuned for {era} {os}.' },
    'school':   { label: 'School & study',   pack: 'Study Revival',
      blurb: 'Study apps, notes and research tools on {era} {os}, good as new.' },
    'web':      { label: 'Web & email',      pack: 'Web Ready',
      blurb: 'A fast, safe modern web on your {era} {os} machine.' },
    'gaming':   { label: 'Games & play',     pack: 'Play Boost',
      blurb: 'Honest tune-up for play on {era} {os} — we say plainly what old hardware can and can\'t run.' },
    'general':  { label: 'Everyday use',     pack: 'Full Refresh',
      blurb: 'The complete refresh: every compatible upgrade for {era} {os}.' }
  };
  var FOCUS_NAMES = Object.keys(FOCUS);
  var COMP_BASE = ['apps', 'software', 'tools', 'lenses', 'pc_models', 'ai_sweeper', 'sweep', 'ai_online'];
  var COMP_SETS = [
    COMP_BASE.slice(),
    COMP_BASE.concat(['ai_offline'])
  ];

  function pickI(rnd, n) { return Math.floor(rnd() * n); }
  function eraTitle(era) { return era === 'modern' ? 'Modern' : era; }
  function buildTitle(era, os, focus, edition) {
    var t = eraTitle(era) + ' ' + os + ' — ' + FOCUS[focus].pack;
    if (edition > 1) t += ' Mk ' + edition;
    return t;
  }
  function buildBlurb(era, os, focus) {
    return FOCUS[focus].blurb.replace('{era}', era).replace('{os}', os);
  }

  function generate(seed, opts, rnd) {
    opts = opts || {};
    var era = ERAS[pickI(rnd, ERAS.length)], os = OS[pickI(rnd, OS.length)];
    var focus = FOCUS_NAMES[pickI(rnd, FOCUS_NAMES.length)];
    if (opts.type && FOCUS[opts.type]) focus = opts.type;
    var edition = 1 + pickI(rnd, 400);
    var offline = pickI(rnd, 2) === 1;
    var n = (opts.baseN || 0) + 1;
    var pub = {
      id: ID_PREFIX + String(n).padStart(ID_DIGITS, '0'),
      n: n,
      title: buildTitle(era, os, focus, edition),
      era: era,
      os: os,
      focus: focus,
      focus_label: FOCUS[focus].label,
      components: COMP_SETS[offline ? 1 : 0].slice(),
      blurb: buildBlurb(era, os, focus),
      best: false,
      origin: 'generated',
      stamp: 'JAH OS Update Data Base — generated upgrade-pack record.'
    };
    pub._priv = { era: era, os: os, focus: focus, edition: edition, offline: offline, seed: seed };
    return pub;
  }

  function validate(rec) {
    var errs = [];
    if (!rec || typeof rec !== 'object') return { ok: false, errors: ['not an object'] };
    ['id', 'title', 'era', 'os', 'focus', 'focus_label', 'components', 'blurb'].forEach(function (k) {
      if (rec[k] === undefined || rec[k] === null || rec[k] === '') errs.push('missing field: ' + k);
    });
    if (rec.id && !/^JAH-UPG-\d{6}$/.test(rec.id)) errs.push('bad id format');
    if (rec.era && ERAS.indexOf(rec.era) < 0) errs.push('unknown era');
    if (rec.os && OS.indexOf(rec.os) < 0) errs.push('unknown os');
    if (rec.focus && !FOCUS[rec.focus]) errs.push('unknown focus');
    if (!Array.isArray(rec.components) || rec.components.length === 0) errs.push('components must be a non-empty array');
    if (rec._priv) {
      var p = rec._priv;
      if (ERAS.indexOf(p.era) < 0 || OS.indexOf(p.os) < 0 || !FOCUS[p.focus])
        errs.push('private pool values out of range');
      else {
        if (rec.era !== p.era) errs.push('era does not match private pick');
        if (rec.os !== p.os) errs.push('os does not match private pick');
        if (rec.focus !== p.focus) errs.push('focus does not match private pick');
        if (rec.focus_label !== FOCUS[p.focus].label) errs.push('focus_label does not match focus');
        if (rec.title !== buildTitle(p.era, p.os, p.focus, p.edition)) errs.push('title does not rebuild from private picks');
        if (rec.blurb !== buildBlurb(p.era, p.os, p.focus)) errs.push('blurb does not rebuild from private picks');
        var want = COMP_SETS[p.offline ? 1 : 0];
        if (JSON.stringify(rec.components.slice().sort()) !== JSON.stringify(want.slice().sort()))
          errs.push('components do not match the private set');
      }
    } else errs.push('no private params — cannot independently verify');
    return { ok: errs.length === 0, errors: errs };
  }

  /* drift check: upgrade-pack titles are unique per record in the archive —
     a generated title must not duplicate a stored one */
  function driftCheck(rec, archiveSample) {
    var errs = [];
    (archiveSample || []).forEach(function (a) {
      var t = a.title;
      if (t && String(t) === String(rec.title)) errs.push('title duplicates a stored upgrade pack');
    });
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

  JAHDB.registerGenerator('osupdater', {
    version: VERSION,
    generate: generate,
    validate: validate,
    driftCheck: driftCheck,
    themedGenerate: themedGenerate,
    types: FOCUS_NAMES
  });
})();
