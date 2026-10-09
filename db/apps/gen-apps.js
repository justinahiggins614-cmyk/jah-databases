(function () {
  'use strict';
  var VERSION = 'jahdb-apps-2.0';
/* ✳ SIGNATURE — JAH App Data Base generator. Property of Justin Addam Higgins (JAH).
   Boundless generator: produces NEW app catalog entries in the exact FULL
   archive record format (same schema as the migrated archive records —
   SigApp.solve canonical output: id, family, seed, name, tagline, icon,
   catName, demo, description, features, how_to, versions, requirements,
   platforms, lineage).
   Deterministic: same seed + version => same record. Every record is
   re-solved INDEPENDENTLY (fresh SigApp.solve) before acceptance. */

  function pad6(n) { return String(n).padStart(6, '0'); }
  var ID_PREFIX = 'JAH-APP-';
  var FULL_FIELDS = ['id', 'family', 'seed', 'name', 'tagline', 'icon', 'catName',
    'demo', 'description', 'features', 'how_to', 'versions', 'requirements', 'platforms', 'lineage'];

  function engine() {
    if (typeof window !== 'undefined' && window.SigApp) return window.SigApp;
    if (typeof self !== 'undefined' && self.SigApp) return self.SigApp;
    if (typeof require === 'function') {
      try { return require('./sigapp-engine.js'); } catch (e) {}
    }
    return null;
  }
  function catKeys() {
    var S = engine();
    if (S && S.families) {
      var f = S.families();
      if (Array.isArray(f) && f.length && typeof f[0] === 'string') return f.slice().sort();
      if (Array.isArray(f)) return f.map(function (x) { return x.key; }).filter(Boolean).sort();
    }
    return [];
  }
  var TYPES = null;
  function types() {
    if (!TYPES) {
      TYPES = catKeys();
      if (!TYPES.length) TYPES = ['word', 'sheet', 'slides', 'mail', 'calendar', 'notes', 'browser', 'music', 'games', 'utils', 'photo', 'video', 'code', 'db'];
    }
    return TYPES;
  }

  function generate(seed, opts, rnd) {
    var S = engine();
    if (!S) throw new Error('SigApp engine not loaded');
    opts = opts || {};
    var T = types();
    var cat = (opts.type && T.indexOf(opts.type) >= 0) ? opts.type : T[Math.floor(rnd() * T.length)];
    var n = (opts.baseN || 0) + 1;
    var id = ID_PREFIX + pad6(n);
    var rec = S.solve(cat, seed, id);
    /* full-record hygiene: stamp + private params for independent re-verification */
    rec.stamp = 'Official JAH App Archive — generated boundlessly in archive style.';
    rec._priv = { cat: cat, seed: seed, id: id };
    return rec;
  }
  function validate(rec) {
    var errs = [];
    if (!rec || typeof rec !== 'object') return { ok: false, errors: ['not an object'] };
    FULL_FIELDS.forEach(function (k) {
      if (rec[k] === undefined || rec[k] === null || rec[k] === '') errs.push('missing full-record field: ' + k);
    });
    if (rec.id && !/^JAH-APP-\d{6}$/.test(rec.id)) errs.push('bad id format');
    if (rec._priv) {
      try {
        var S = engine(), p = rec._priv;
        var fresh = S.solve(p.cat, p.seed, p.id);
        var a = JSON.parse(JSON.stringify(fresh)), b = JSON.parse(JSON.stringify(rec));
        delete a._priv; delete b._priv; delete b.stamp; delete b._gen_version; delete b._seed;
        if (JSON.stringify(a) !== JSON.stringify(b)) errs.push('independent re-solve mismatch — not deterministic');
      } catch (e) { errs.push('re-solve threw: ' + e.message); }
    } else errs.push('no private params — cannot independently verify');
    if (!Array.isArray(rec.features) || !rec.features.length) errs.push('features[] empty');
    if (!Array.isArray(rec.versions) || !rec.versions.length) errs.push('versions[] empty');
    return { ok: errs.length === 0, errors: errs };
  }
  function driftCheck(rec, archiveSample) {
    var errs = [];
    (archiveSample || []).forEach(function (a) {
      var nm = a[3] || a.name;
      if (nm && String(nm) === String(rec.name)) errs.push('duplicate of archived app name: ' + rec.name);
    });
    return { ok: errs.length === 0, errors: errs };
  }
  /* cross-database: borrow a theme from another database's sample */
  function themedGenerate(seed, opts, rnd, themeSamples) {
    var rec = generate(seed, opts, rnd);
    if (themeSamples && themeSamples.length) {
      var t = themeSamples[Math.floor(rnd() * themeSamples.length)];
      var nums = String(JSON.stringify(t)).match(/\d+/g);
      if (nums && nums.length) {
        var rec2 = generate(seed + (parseInt(nums[0], 10) % 1000), opts, rnd);
        rec2.id = rec.id; rec2.n = rec.n;
        return rec2;
      }
    }
    return rec;
  }
  if (typeof JAHDB !== 'undefined' && JAHDB.registerGenerator) {
    JAHDB.registerGenerator('apps', {
      version: VERSION,
      generate: generate,
      validate: validate,
      driftCheck: driftCheck,
      themedGenerate: themedGenerate,
      types: types()
    });
  }
  /* node harness export */
  if (typeof module !== 'undefined' && module.exports) {
    module.exports = { version: VERSION, generate: generate, validate: validate, driftCheck: driftCheck, themedGenerate: themedGenerate, types: types, FULL_FIELDS: FULL_FIELDS };
  }
})();
