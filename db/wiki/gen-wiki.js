/* ✳ SIGNATURE — JAH Wiki Data Base generator. Property of Justin Addam Higgins (JAH).
   Boundless generator: produces NEW wiki articles in the wiki's article format
   (id, title, kind, summary, analysis, see_also, stamp). The wiki's archive is
   every article it renders — spec, patent, word, and dossier articles.
   Deterministic: same seed + version => same article. */
(function () {
  'use strict';
  var VERSION = 'jahdb-wiki-1.0';
  var ID_PREFIX = 'JAH-WIKI-';
  var STAMP = 'JAH Wiki article — generated in archive style. New articles are candidates until validated.';
  var KINDS = ['spec', 'patent', 'word', 'dossier'];

  var SUBJECTS = [
    ['Quantum lattice', 'spec', 'A deterministic lattice framework for mapping discrete state transitions across bounded domains.'],
    ['Harmonic drive', 'spec', 'A mechanical transmission principle using flexible spline deformation for high-ratio motion control.'],
    ['Neural mesh', 'patent', 'An interlinked node architecture for distributed signal processing and adaptive weighting.'],
    ['Solar collector', 'patent', 'A surface engineered to capture radiant energy and convert it to storable form.'],
    ['Serendipity', 'word', 'The occurrence of valuable discoveries by accident while seeking something else.'],
    ['Liminal', 'word', 'Occupying a position at or on both sides of a boundary or threshold.'],
    ['Tunguska event', 'dossier', 'The 1908 Siberian atmospheric explosion and the investigations that followed.'],
    ['Oakville blobs', 'dossier', 'The 1994 Washington gelatinous rain reports and laboratory findings.'],
    ['Ferrofluid seal', 'spec', 'A liquid magnetic barrier maintaining pressure differentials in rotating assemblies.'],
    ['Piezo harvester', 'patent', 'A device converting ambient vibration into electrical charge via crystalline strain.'],
    ['Petrichor', 'word', 'The scent of rain falling on dry earth after a warm dry spell.'],
    ['Maxwell demon', 'dossier', 'The thought experiment probing the limits of thermodynamics and information.'],
    ['Gyroscopic compass', 'spec', 'A heading reference using angular momentum to hold true orientation.'],
    ['Ion thruster', 'patent', 'A propulsion unit accelerating charged particles for sustained low thrust.'],
    ['Sonder', 'word', 'The realization that each passerby lives a life as vivid as your own.'],
    ['Bloop signal', 'dossier', 'The 1997 ultra-low-frequency underwater sound and its analysis.']
  ];
  var ANGLES = [
    'Historical background and first principles',
    'Technical structure and key mechanisms',
    'Measured behavior and observed effects',
    'Applications and practical use',
    'Open questions and active investigation',
    'Cross-references and related articles'
  ];
  function ri(rnd, a, b) { return a + Math.floor(rnd() * (b - a + 1)); }
  function pick(rnd, arr) { return arr[Math.floor(rnd() * arr.length)]; }

  function generate(seed, opts, rnd) {
    opts = opts || {};
    var kind = opts.kind && KINDS.indexOf(opts.kind) >= 0 ? opts.kind : pick(rnd, KINDS);
    var pool = SUBJECTS.filter(function (s) { return s[1] === kind; });
    if (!pool.length) pool = SUBJECTS;
    var subj = pick(rnd, pool);
    var n = (opts.baseN || 0) + 1;
    var title = subj[0];
    /* deterministic variant titles so the generator is boundless, not a fixed list */
    var variant = ri(rnd, 0, 999);
    if (variant % 3 === 0) title = subj[0] + ' — ' + pick(rnd, ANGLES);
    var summary = subj[2] + ' This article treats ' + subj[0].toLowerCase() +
      ' in the JAH Wiki manner: definition first, then structure, then what is known and what remains open.';
    var analysis = 'Analysis. ' + subj[0] + ' is classified under ' + kind + ' articles. ' +
      'The treatment follows the archive standard: (1) ' + ANGLES[ri(rnd, 0, 5)] + '; (2) ' +
      ANGLES[ri(rnd, 0, 5)] + '; (3) ' + ANGLES[ri(rnd, 0, 5)] + '. ' +
      'Claims are stated plainly and separated from interpretation.';
    var seeAlso = [];
    var pool2 = SUBJECTS.filter(function (s) { return s[0] !== subj[0]; });
    for (var i = 0; i < 3; i++) seeAlso.push(pick(rnd, pool2)[0]);
    var rec = {
      id: ID_PREFIX + String(n).padStart(8, '0'),
      n: n, title: title, kind: kind,
      summary: summary, analysis: analysis, see_also: seeAlso,
      stamp: STAMP, _seed: seed
    };
    var pub = {};
    ['id', 'n', 'title', 'kind', 'summary', 'analysis', 'see_also', 'stamp'].forEach(function (k) { pub[k] = rec[k]; });
    pub._priv = { seed: seed, kind: kind, subject: subj[0] };
    return pub;
  }

  function validate(rec) {
    var errs = [];
    if (!rec || typeof rec !== 'object') return { ok: false, errors: ['not an object'] };
    ['id', 'title', 'kind', 'summary', 'analysis', 'see_also'].forEach(function (k) {
      if (rec[k] === undefined || rec[k] === null || rec[k] === '') errs.push('missing field: ' + k);
    });
    if (rec.id && !/^JAH-WIKI-\d{8}$/.test(rec.id)) errs.push('bad id format');
    if (rec.kind && KINDS.indexOf(rec.kind) < 0) errs.push('bad kind');
    if (rec.title && rec.title.length < 3) errs.push('title too short');
    if (rec.summary && rec.summary.length < 20) errs.push('summary too thin for a wiki article');
    if (!Array.isArray(rec.see_also) || rec.see_also.length === 0) errs.push('see_also must list related articles');
    if (rec._priv && rec._priv.subject && rec.title.indexOf(rec._priv.subject.split(' — ')[0]) < 0)
      errs.push('title drifted from generated subject');
    return { ok: errs.length === 0, errors: errs };
  }

  function driftCheck(rec, archiveSample) {
    var errs = [];
    (archiveSample || []).forEach(function (a) {
      var t = a.t || a[1];
      if (t && String(t).toLowerCase() === String(rec.title).toLowerCase())
        errs.push('an article with this exact title already exists: ' + rec.title);
    });
    return { ok: errs.length === 0, errors: errs };
  }

  JAHDB.registerGenerator('wiki', {
    version: VERSION, generate: generate, validate: validate, driftCheck: driftCheck, kinds: KINDS
  });
})();
