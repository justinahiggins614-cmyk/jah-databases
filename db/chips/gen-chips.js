(function () {
  'use strict';
  var VERSION = 'jahdb-chips-2.0';
/* ✳ SIGNATURE — JAH Chip Data Base generator. Property of Justin Addam Higgins (JAH).
   Boundless generator: produces NEW chip design entries in the exact FULL
   archive record format (ChipEngine.canonicalRecord schema: id, fam, era,
   name, sigpart, label, node, transistors, die, pins, tdp, clk, pkg, isa,
   arch, blocks, specs, pin_groups, diagram, designOrigin, fabrication
   readiness, lineage, statuses — the complete design file).
   Deterministic: same seed + version => same record. Every record is
   re-solved INDEPENDENTLY (fresh canonicalRecord) before acceptance. */

  function pad6(n) { return String(n).padStart(6, '0'); }
  var ID_PREFIX = 'JAH-CHIP-';
  var ERAS = ['Historic', 'Modern', 'Projected'];

  function engine() {
    if (typeof window !== 'undefined' && window.ChipEngine) return window.ChipEngine;
    if (typeof self !== 'undefined' && self.ChipEngine) return self.ChipEngine;
    if (typeof require === 'function') {
      try { var m = require('./chip-engine.js'); return m.ChipEngine || m; } catch (e) {}
    }
    return null;
  }

  function generate(seed, opts, rnd) {
    var E = engine();
    if (!E) throw new Error('ChipEngine not loaded');
    opts = opts || {};
    var FAMS = E.FAMS;
    var fam = (opts.type && FAMS.indexOf(opts.type) >= 0) ? opts.type : FAMS[Math.floor(rnd() * FAMS.length)];
    var era = (opts.era && ERAS.indexOf(opts.era) >= 0) ? opts.era : ERAS[Math.floor(rnd() * ERAS.length)];
    var n = (opts.baseN || 0) + 1;
    var id = ID_PREFIX + pad6(n);
    var nameIdx = Math.floor(rnd() * 6750 * 4);
    var name = E.chipName(nameIdx);
    var row = { id: id, fam: fam, era: era, seed: seed, name: name };
    var rec = E.canonicalRecord(row);
    /* full-record hygiene: canonical URL points at this database's own page */
    rec.canonical_url = 'https://justinahiggins614-cmyk.github.io/jah-databases/db/chips/#' + encodeURIComponent(id);
    rec._priv = { fam: fam, era: era, seed: seed, nameIdx: nameIdx, id: id };
    return rec;
  }
  function validate(rec) {
    var errs = [];
    if (!rec || typeof rec !== 'object') return { ok: false, errors: ['not an object'] };
    ['id', 'fam', 'era', 'name', 'sigpart', 'node', 'arch', 'transistors', 'die',
     'pins', 'tdp', 'clk', 'pkg', 'isa', 'blocks', 'specs', 'pin_groups',
     'diagram', 'designOrigin', 'fabRemain', 'lineage'].forEach(function (k) {
      if (rec[k] === undefined || rec[k] === null || rec[k] === '') errs.push('missing full-record field: ' + k);
    });
    if (rec.id && !/^JAH-CHIP-\d{6}$/.test(rec.id)) errs.push('bad id format');
    if (rec._priv) {
      try {
        var E = engine(), p = rec._priv;
        var row = { id: p.id, fam: p.fam, era: p.era, seed: p.seed, name: E.chipName(p.nameIdx) };
        var fresh = E.canonicalRecord(row);
        fresh.canonical_url = rec.canonical_url;
        var a = JSON.stringify(fresh), b = JSON.stringify(rec);
        var aj = JSON.parse(a), bj = JSON.parse(b);
        delete aj._priv; delete bj._priv; delete bj._gen_version; delete bj._seed;
        if (JSON.stringify(aj) !== JSON.stringify(bj)) errs.push('independent re-solve mismatch — not deterministic');
      } catch (e) { errs.push('re-solve threw: ' + e.message); }
    } else errs.push('no private params — cannot independently verify');
    if (!Array.isArray(rec.blocks) || !rec.blocks.length) errs.push('blocks[] empty');
    if (!Array.isArray(rec.specs) || !rec.specs.length) errs.push('specs[] empty');
    if (!Array.isArray(rec.pin_groups) || !rec.pin_groups.length) errs.push('pin_groups[] empty');
    return { ok: errs.length === 0, errors: errs };
  }
  function driftCheck(rec, archiveSample) {
    var errs = [];
    (archiveSample || []).forEach(function (a) {
      var nm = a[1];
      if (nm && String(nm) === String(rec.name)) errs.push('duplicate of archived chip name: ' + rec.name);
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
    JAHDB.registerGenerator('chips', {
      version: VERSION,
      generate: generate,
      validate: validate,
      driftCheck: driftCheck,
      themedGenerate: themedGenerate,
      types: (typeof window !== 'undefined' && window.ChipEngine) ? window.ChipEngine.FAMS : []
    });
  }
  /* node harness export */
  if (typeof module !== 'undefined' && module.exports) {
    module.exports = { version: VERSION, generate: generate, validate: validate, driftCheck: driftCheck, themedGenerate: themedGenerate };
  }
})();
