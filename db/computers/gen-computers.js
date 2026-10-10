/* ✳ SIGNATURE — JAH Computer Systems Data Base generator. Property of Justin Addam Higgins (JAH).
   Boundless generator: produces NEW computer system records in the archive's
   exact schema (id, name, system_type, category, summary, specs).
   Every generated record is honestly marked category "generated" /
   system_type "GENERATED", like the archive's own generated systems.
   Deterministic: same seed + version => same record. An INDEPENDENT verifier
   rebuilds every record from its private pool indices before acceptance. */
(function () {
  'use strict';
  var VERSION = 'jahdb-computers-1.0';
  var ID_PREFIX = 'JAH-PC-';
  var STAMP = 'Official JAH Computer Systems Archive — generated boundlessly, verified independently.';
  /* real archive categories (data/systems-index.json), used as design families */
  var CATS = ['generated', 'signature', 'historic', 'modern', 'materials', 'quantum', 'predicted', 'mixes'];
  var PUB_KEYS = ['id', 'slug', 'name', 'system_type', 'category', 'design_family',
                  'summary', 'specs', 'note', 'stamp'];

  var PRE = ['Nova', 'Quantum', 'Hyper', 'Turbo', 'Aero', 'Cipher', 'Delta', 'Echo', 'Flux',
             'Grid', 'Helix', 'Ion', 'Jolt', 'Krypton', 'Lumen', 'Magnet', 'Nebula', 'Onyx',
             'Photon', 'Quark', 'Radar', 'Solar', 'Titan', 'Ultra', 'Vector', 'Warp'];
  var CORE = ['Core', 'Forge', 'Stack', 'Node', 'Array', 'Engine', 'Cluster', 'Frame',
              'Matrix', 'Drive', 'Works', 'Station', 'Rig', 'Tower', 'Deck', 'Vault'];
  var MODEL = ['X1', '2000', 'Pro', 'Ultra', 'Mark IV', 'GX', 'Prime', 'Elite',
               'S', 'Turbo-9', 'Classic', 'Plus', 'Max', 'Lite', '9K', 'Z'];
  var FORM = ['desktop tower', 'laptop', 'rack server', 'workstation', 'handheld unit',
              'mainframe cabinet', 'embedded board', 'all-in-one'];
  var CPU = ['8-core 3.2 GHz processor', '16-core 4.1 GHz processor', 'quad-core 2.8 GHz processor',
             '32-core 3.9 GHz processor', 'dual-core 1.8 GHz processor', '64-core 4.4 GHz processor'];
  var RAM = [4, 8, 16, 32, 64, 128, 256];
  var DISK = ['256 GB SSD', '512 GB SSD', '1 TB SSD', '2 TB HDD', '4 TB array', '128 GB flash'];

  function ri(rnd, a, b) { return a + Math.floor(rnd() * (b - a + 1)); }
  function pick(rnd, arr) { return arr[Math.floor(rnd() * arr.length)]; }
  function picki(rnd, arr) { return Math.floor(rnd() * arr.length); }

  function buildName(p) { return PRE[p[0]] + ' ' + CORE[p[1]] + ' ' + MODEL[p[2]]; }
  function buildSummary(p) {
    return 'Generated system record: the ' + buildName([p[0], p[1], p[2]]) +
      ' is a ' + FORM[p[3]] + ' in the ' + CATS[p[6]] + ' design family, built around a ' +
      CPU[p[4]] + ' with ' + RAM[p[5]] + ' GB of memory and ' + DISK[p[7]] +
      '. Assembled by the JAH Databases generator — a new entry in archive style, not a stored system.';
  }

  function generate(seed, opts, rnd) {
    opts = opts || {};
    var fam = opts.type && CATS.indexOf(opts.type) >= 0 ? opts.type : pick(rnd, CATS);
    /* private pool indices — the entire record is rebuilt from these */
    var p = [picki(rnd, PRE), picki(rnd, CORE), picki(rnd, MODEL), picki(rnd, FORM),
             picki(rnd, CPU), picki(rnd, RAM), CATS.indexOf(fam), picki(rnd, DISK)];
    var year = ri(rnd, 1975, 2026);
    var n = (opts.baseN || 0) + 1;
    var rec = {
      id: ID_PREFIX + String(n).padStart(8, '0'),
      slug: 'sys-gen-' + n,
      name: buildName(p),
      system_type: 'GENERATED',
      category: 'generated',
      design_family: fam,
      summary: buildSummary(p),
      specs: { form: FORM[p[3]], cpu: CPU[p[4]], ram_gb: RAM[p[5]], storage: DISK[p[7]], year: year },
      note: 'GENERATED RECORD — produced by the JAH Databases generator. Not a stored archive system.',
      stamp: STAMP,
      _p: p, _year: year, _n: n, _seed: seed
    };
    var pub = {};
    PUB_KEYS.forEach(function (k) { pub[k] = rec[k]; });
    pub._priv = rec;
    return pub;
  }

  /* independent verifier: rebuilds name, summary, specs from the pool indices */
  function verify(priv) {
    var errs = [];
    var p = priv._p;
    if (!Array.isArray(p) || p.length !== 8) return ['bad private pool indices'];
    var lim = [PRE.length, CORE.length, MODEL.length, FORM.length, CPU.length, RAM.length, CATS.length, DISK.length];
    for (var i = 0; i < 8; i++)
      if (!(p[i] >= 0 && p[i] < lim[i] && p[i] === Math.floor(p[i]))) { errs.push('pool index out of range at ' + i); break; }
    if (priv.name !== buildName(p)) errs.push('name rebuild mismatch');
    if (priv.summary !== buildSummary(p)) errs.push('summary rebuild mismatch');
    if (priv.specs.form !== FORM[p[3]] || priv.specs.cpu !== CPU[p[4]] ||
        priv.specs.ram_gb !== RAM[p[5]] || priv.specs.storage !== DISK[p[7]] ||
        priv.specs.year !== priv._year)
      errs.push('specs rebuild mismatch');
    if (!(priv._year >= 1975 && priv._year <= 2026)) errs.push('year out of range');
    if (priv.design_family !== CATS[p[6]]) errs.push('design family mismatch');
    if (priv.id !== ID_PREFIX + String(priv._n).padStart(8, '0')) errs.push('id rebuild mismatch');
    return errs;
  }

  function validate(rec) {
    var errs = [];
    if (!rec || typeof rec !== 'object') return { ok: false, errors: ['not an object'] };
    ['id', 'name', 'system_type', 'category', 'summary', 'specs'].forEach(function (k) {
      if (rec[k] === undefined || rec[k] === null || rec[k] === '') errs.push('missing field: ' + k);
    });
    if (rec.id && !/^JAH-PC-\d{8}$/.test(rec.id)) errs.push('bad id format');
    if (rec.system_type && rec.system_type !== 'GENERATED') errs.push('generated records must be system_type GENERATED');
    if (rec.category && rec.category !== 'generated') errs.push('generated records must be category generated');
    if (rec.design_family && CATS.indexOf(rec.design_family) < 0) errs.push('bad design family');
    if (rec._priv) {
      var p = rec._priv;
      PUB_KEYS.forEach(function (k) {
        if (JSON.stringify(rec[k]) !== JSON.stringify(p[k])) errs.push('field diverged from verified copy: ' + k);
      });
      errs = errs.concat(verify(p));
    }
    else errs.push('no private pool indices — cannot independently verify');
    return { ok: errs.length === 0, errors: errs };
  }

  function driftCheck(rec, archiveSample) {
    var errs = [];
    (archiveSample || []).forEach(function (a) {
      var nm = a.name || (a[1]);
      if (nm && String(nm).toLowerCase() === String(rec.name).toLowerCase())
        errs.push('duplicate of archived system name: ' + rec.name);
    });
    return { ok: errs.length === 0, errors: errs };
  }

  function themedGenerate(seed, opts, rnd, themeSamples) {
    var rec = generate(seed, opts, rnd);
    if (themeSamples && themeSamples.length) {
      var t = themeSamples[Math.floor(rnd() * themeSamples.length)];
      var nums = String(JSON.stringify(t)).match(/\d+/g);
      if (nums && nums.length) {
        var rec2 = generate(seed + (parseInt(nums[0], 10) % 1000), opts, JAHDB.prng(JAHDB.hashStr(String(seed) + nums[0])));
        rec2.id = rec.id; rec2.slug = rec.slug;
        return rec2;
      }
    }
    return rec;
  }

  JAHDB.registerGenerator('computers', {
    version: VERSION,
    generate: generate,
    validate: validate,
    driftCheck: driftCheck,
    themedGenerate: themedGenerate,
    types: CATS
  });
})();
