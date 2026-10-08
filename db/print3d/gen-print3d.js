/* ✳ SIGNATURE — JAH 3D Print Data Base generator. Property of Justin Addam Higgins (JAH).
   Boundless generator: produces NEW 3D-model records in the archive's exact
   schema with internally consistent parameters (id, name, model_type,
   material, dims, volume, filament, print estimate). Deterministic: same
   seed + version => same record. An INDEPENDENT verifier recomputes volume,
   filament mass, layer count, and print-time estimate from the raw dims
   before acceptance. Estimates are labeled estimates, never measured facts. */
(function () {
  'use strict';
  var VERSION = 'jahdb-print3d-1.0';
  var ID_PREFIX = 'JAH-3D-';

  function ri(rnd, a, b) { return a + Math.floor(rnd() * (b - a + 1)); }
  function pick(rnd, arr) { return arr[Math.floor(rnd() * arr.length)]; }
  function f2(v) { return String(parseFloat(v.toFixed(2))); }
  function f4(v) { return String(parseFloat(v.toFixed(4))); }

  var TYPES = ['bracket', 'enclosure', 'gear', 'vase', 'hook', 'stand', 'knob', 'housing', 'mount', 'figurine'];
  var ADJ = ['Compact', 'Sturdy', 'Precision', 'Modular', 'Slim', 'Heavy-Duty', 'Mini', 'Pro'];
  /* genuine material densities (g/cm^3) used for the filament estimate */
  var MATERIALS = { PLA: 1.24, PETG: 1.27, ABS: 1.04, TPU: 1.21 };
  var MATNAMES = Object.keys(MATERIALS);
  var LAYERS = [0.12, 0.16, 0.2, 0.28];

  /* documented estimate formula: mass-driven print time + per-layer overhead */
  function estimate(p) {
    var volCm3 = p.w * p.h * p.d / 1000;
    var filamentG = volCm3 * (p.infill / 100) * MATERIALS[p.material];
    var layers = Math.ceil(p.h / p.layer);
    var hours = filamentG * 0.045 + layers * 0.0015;
    return { volCm3: volCm3, filamentG: filamentG, layers: layers, hours: hours };
  }

  function generate(seed, opts, rnd) {
    opts = opts || {};
    var type = opts.type && TYPES.indexOf(opts.type) >= 0 ? opts.type : pick(rnd, TYPES);
    var p = {
      w: parseFloat((20 + rnd() * 160).toFixed(2)),
      h: parseFloat((10 + rnd() * 120).toFixed(2)),
      d: parseFloat((20 + rnd() * 160).toFixed(2)),
      material: pick(rnd, MATNAMES),
      infill: pick(rnd, [10, 15, 20, 25, 30, 40, 50, 60, 80, 100]),
      layer: pick(rnd, LAYERS)
    };
    var e = estimate(p);
    var n = (opts.baseN || 0) + 1;
    var rec = {
      id: ID_PREFIX + String(n).padStart(6, '0'),
      n: n,
      name: pick(rnd, ADJ) + ' ' + type.charAt(0).toUpperCase() + type.slice(1) + ' ' + p.material,
      model_type: type,
      material: p.material,
      dims_mm: { w: f2(p.w), h: f2(p.h), d: f2(p.d) },
      volume_cm3: f4(e.volCm3),
      infill_pct: p.infill,
      layer_height_mm: p.layer,
      filament_g: f4(e.filamentG),
      layers: e.layers,
      est_print_hours: f2(e.hours),
      note: 'Estimate only — generated parameters, not a measured print.'
    };
    var pub = {};
    ['id', 'n', 'name', 'model_type', 'material', 'dims_mm', 'volume_cm3',
     'infill_pct', 'layer_height_mm', 'filament_g', 'layers', 'est_print_hours', 'note']
      .forEach(function (k) { pub[k] = rec[k]; });
    pub._priv = { p: p, e: { volCm3: e.volCm3, filamentG: e.filamentG, layers: e.layers, hours: e.hours }, name: rec.name };
    return pub;
  }

  /* independent re-verification: recompute everything from the raw params */
  function verify(rec) {
    var errs = [];
    var p = rec._priv.p;
    if (!MATERIALS[p.material]) errs.push('unknown material');
    if (!(p.w > 0 && p.h > 0 && p.d > 0)) errs.push('dims must be positive');
    var e = estimate(p);
    if (f4(e.volCm3) !== String(rec.volume_cm3)) errs.push('volume recompute mismatch');
    if (f4(e.filamentG) !== String(rec.filament_g)) errs.push('filament recompute mismatch');
    if (e.layers !== rec.layers) errs.push('layer count recompute mismatch');
    if (f2(e.hours) !== String(rec.est_print_hours)) errs.push('print-time recompute mismatch');
    if (rec.dims_mm.w !== f2(p.w) || rec.dims_mm.h !== f2(p.h) || rec.dims_mm.d !== f2(p.d))
      errs.push('dims mismatch');
    if (rec.material !== p.material) errs.push('material mismatch');
    if (rec._priv.name !== rec.name) errs.push('name mismatch');
    return errs;
  }

  function validate(rec) {
    var errs = [];
    if (!rec || typeof rec !== 'object') return { ok: false, errors: ['not an object'] };
    ['id', 'name', 'model_type', 'material', 'dims_mm', 'volume_cm3',
     'infill_pct', 'layer_height_mm', 'filament_g', 'layers', 'est_print_hours'].forEach(function (k) {
      if (rec[k] === undefined || rec[k] === null || rec[k] === '') errs.push('missing field: ' + k);
    });
    if (rec.id && !/^JAH-3D-\d{6}$/.test(rec.id)) errs.push('bad id format');
    if (rec.model_type && TYPES.indexOf(rec.model_type) < 0) errs.push('bad model_type');
    if (rec._priv) errs = errs.concat(verify(rec));
    else errs.push('no private params — cannot independently verify');
    return { ok: errs.length === 0, errors: errs };
  }

  function driftCheck(rec, archiveSample) {
    var errs = [];
    (archiveSample || []).forEach(function (a) {
      var t = a.title || a.name || a[1];
      if (t && String(t).toLowerCase() === String(rec.name).toLowerCase())
        errs.push('duplicate of archived model name: ' + rec.name);
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

  JAHDB.registerGenerator('print3d', {
    version: VERSION,
    generate: generate,
    validate: validate,
    driftCheck: driftCheck,
    themedGenerate: themedGenerate,
    types: TYPES
  });
})();
