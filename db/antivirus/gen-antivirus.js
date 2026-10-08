/* ✳ SIGNATURE — JAH Antivirus Data Base generator. Property of Justin Addam Higgins (JAH).
   Boundless generator: produces NEW virus-solution drill records in the exact
   archive format (id, name, year, type, level, vector, solution, status,
   origin, note). Names follow the archive's own family-variant scheme; the
   vector/solution texts are the archive's per-type defense profiles, so every
   field is genuine. status/origin are 'generated' and the note marks the
   record a simulated drill — never a documented incident. Deterministic:
   same seed + version => same record. An independent verifier rebuilds every
   claim from the private params before acceptance. */
(function () {
  'use strict';
  var VERSION = 'jahdb-antivirus-1.0';
  var ID_PREFIX = 'JAH-AV-';
  var ID_DIGITS = 6;
  var YEAR = 2026;
  var NOTE = 'Generated drill record — simulated threat for practice, not a documented incident.';

  /* per-type families and defense profiles, taken from the stored archive */
  var TYPES = {
    'adware': {
      family: 'Adspew',
      vector: 'Varies by strain — see the adware defense profile.',
      solution: 'Uninstall the bundling application, Shield scan, reset browser settings, review startup entries with bootcheck.'
    },
    'botnet': {
      family: 'Botswarm',
      vector: 'Varies by strain — see the botnet defense profile.',
      solution: 'Isolate, Safe-Mode Shield scan, bootcheck for scheduled tasks/services, block command-and-control indicators at the firewall.'
    },
    'keylogger': {
      family: 'Keysnare',
      vector: 'Varies by strain — see the keylogger defense profile.',
      solution: 'Shield heuristic scan (flags keylogging keywords), change ALL typed passwords from a clean device, enable 2FA everywhere.'
    },
    'ransomware': {
      family: 'Cryptor',
      vector: 'Varies by strain — see the ransomware defense profile.',
      solution: 'Isolate the machine from the network, identify the strain, restore from clean offline backups, Safe-Mode Shield scan, patch the entry vector, then run Shield Defense apply-all.'
    },
    'rootkit': {
      family: 'Rootshade',
      vector: 'Varies by strain — see the rootkit defense profile.',
      solution: 'Scan from clean boot media (rootkits hide from the running OS), rebuild if the kernel is compromised, restore from known-clean images.'
    },
    'scareware': {
      family: 'Scarecrow',
      vector: 'Varies by strain — see the scareware defense profile.',
      solution: 'Do not pay or call the number. Force-close the browser, Shield scan, clear browser data, report the page.'
    },
    'spyware': {
      family: 'Spyweave',
      vector: 'Varies by strain — see the spyware defense profile.',
      solution: 'Full Shield heuristic scan, remove the bundling program, check browser extensions, rotate passwords for accounts used on the machine.'
    },
    'trojan': {
      family: 'Trojaner',
      vector: 'Varies by strain — see the trojan defense profile.',
      solution: 'Delete the lure, Safe-Mode Shield scan, bootcheck for persistence entries, reset credentials from a clean device.'
    },
    'wiper': {
      family: 'Wipeout',
      vector: 'Varies by strain — see the wiper defense profile.',
      solution: 'Isolate immediately, restore from offline backups, rebuild — wiped data is unrecoverable by design.'
    },
    'worm': {
      family: 'Wormlet',
      vector: 'Varies by strain — see the worm defense profile.',
      solution: 'Isolate, patch the exploited service, block its ports with Shield Defense firewall rules, Safe-Mode Shield scan across shares, change exposed credentials.'
    }
  };
  var TYPE_NAMES = Object.keys(TYPES);
  var LEVELS = ['low', 'medium', 'high', 'critical'];

  function pickI(rnd, n) { return Math.floor(rnd() * n); }
  function buildName(type, vnum) { return TYPES[type].family + '-variant-' + String(vnum).padStart(4, '0'); }

  function generate(seed, opts, rnd) {
    opts = opts || {};
    var type = TYPE_NAMES[pickI(rnd, TYPE_NAMES.length)];
    if (opts.type && TYPES[opts.type]) type = opts.type;
    var level = LEVELS[pickI(rnd, LEVELS.length)];
    var vnum = 1 + pickI(rnd, 9000);
    var n = (opts.baseN || 0) + 1;
    var pub = {
      id: ID_PREFIX + String(n).padStart(ID_DIGITS, '0'),
      n: n,
      name: buildName(type, vnum),
      year: YEAR,
      type: type,
      level: level,
      vector: TYPES[type].vector,
      solution: TYPES[type].solution,
      status: 'generated',
      origin: 'generated',
      note: NOTE,
      stamp: 'JAH Antivirus Data Base — generated virus-solution drill record.'
    };
    pub._priv = { type: type, level: level, vnum: vnum, seed: seed };
    return pub;
  }

  function validate(rec) {
    var errs = [];
    if (!rec || typeof rec !== 'object') return { ok: false, errors: ['not an object'] };
    ['id', 'name', 'year', 'type', 'level', 'vector', 'solution', 'status', 'origin', 'note'].forEach(function (k) {
      if (rec[k] === undefined || rec[k] === null || rec[k] === '') errs.push('missing field: ' + k);
    });
    if (rec.id && !/^JAH-AV-\d{6}$/.test(rec.id)) errs.push('bad id format');
    if (rec.type && !TYPES[rec.type]) errs.push('unknown type');
    if (rec.level && LEVELS.indexOf(rec.level) < 0) errs.push('unknown level');
    if (rec.status && rec.status !== 'generated') errs.push('status must be generated');
    if (rec.origin && rec.origin !== 'generated') errs.push('origin must be generated');
    if (typeof rec.note !== 'string' || rec.note.indexOf('not a documented incident') < 0)
      errs.push('drill disclaimer missing');
    if (rec._priv) {
      var p = rec._priv;
      if (!TYPES[p.type]) errs.push('private type unknown');
      else {
        if (rec.type !== p.type) errs.push('type does not match private pick');
        if (rec.level !== p.level) errs.push('level does not match private pick');
        if (rec.name !== buildName(p.type, p.vnum)) errs.push('name does not rebuild from private picks');
        if (rec.vector !== TYPES[p.type].vector) errs.push('vector does not match the type defense profile');
        if (rec.solution !== TYPES[p.type].solution) errs.push('solution does not match the type defense profile');
        if (rec.year !== YEAR) errs.push('year mismatch');
      }
    } else errs.push('no private params — cannot independently verify');
    return { ok: errs.length === 0, errors: errs };
  }

  /* drift check: a generated drill name must not duplicate a stored record name */
  function driftCheck(rec, archiveSample) {
    var errs = [];
    (archiveSample || []).forEach(function (a) {
      var nm = Array.isArray(a) ? a[1] : a.name;
      if (nm && String(nm) === String(rec.name)) errs.push('name duplicates a stored archive record');
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

  JAHDB.registerGenerator('antivirus', {
    version: VERSION,
    generate: generate,
    validate: validate,
    driftCheck: driftCheck,
    themedGenerate: themedGenerate,
    types: TYPE_NAMES
  });
})();
