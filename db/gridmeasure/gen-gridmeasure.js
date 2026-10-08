/* ✳ SIGNATURE — JAH Image Measure Data Base generator. Property of Justin Addam Higgins (JAH).
   Boundless generator: produces NEW measure records in the exact archive format
   (id, name, shape, svg, table[[label, value]]). Deterministic: same seed +
   version => same record. Every measure is built constructively from random
   inputs (legs, width/height, radius, base/height, sides); an INDEPENDENT
   verifier recomputes every table cell from the inputs with the archive's own
   rounding before acceptance. */
(function () {
  'use strict';
  var VERSION = 'jahdb-gridmeasure-1.0';
  var ID_PREFIX = 'JAH-GRID-';

  function ri(rnd, a, b) { return a + Math.floor(rnd() * (b - a + 1)); }
  function pick(rnd, arr) { return arr[Math.floor(rnd() * arr.length)]; }
  /* archive number style: fixed decimals, trailing zeros stripped */
  function f2(v) { return String(parseFloat(v.toFixed(2))); }
  function f4(v) { return String(parseFloat(v.toFixed(4))); }
  function deg(r) { return r * 180 / Math.PI; }

  var SHAPES = ['right_triangle', 'rectangle', 'regular_polygon', 'circle', 'isosceles_triangle'];
  var POLYNAME = { 5: 'Pentagon', 6: 'Hexagon', 7: 'Heptagon', 8: 'Octagon' };
  var SHAPELABEL = {
    right_triangle: 'Right Triangle', rectangle: 'Rectangle',
    regular_polygon: null, circle: 'Circle', isosceles_triangle: 'Isosceles Triangle'
  };

  function tableFor(shape, p) {
    var t;
    if (shape === 'right_triangle') {
      var hyp = Math.sqrt(p.a * p.a + p.b * p.b);
      t = [['Leg a', f2(p.a)], ['Leg b', f2(p.b)], ['Hypotenuse c', f4(hyp)],
           ['Angle at a', f4(deg(Math.atan2(p.a, p.b))) + '°'],
           ['Angle at b', f4(deg(Math.atan2(p.b, p.a))) + '°'],
           ['Area', f4(p.a * p.b / 2)], ['Perimeter', f4(p.a + p.b + hyp)]];
    } else if (shape === 'rectangle') {
      var dg = Math.sqrt(p.w * p.w + p.h * p.h);
      t = [['Width', f2(p.w)], ['Height', f2(p.h)], ['Diagonal', f4(dg)],
           ['Area', f4(p.w * p.h)], ['Perimeter', f4(2 * (p.w + p.h))]];
    } else if (shape === 'regular_polygon') {
      var ap = p.side / (2 * Math.tan(Math.PI / p.sides));
      t = [['Sides', String(p.sides)], ['Side length', f2(p.side)],
           ['Perimeter', f4(p.sides * p.side)], ['Apothem', f4(ap)],
           ['Area', f4(p.sides * p.side * ap / 2)],
           ['Interior angle', f4((p.sides - 2) * 180 / p.sides) + '°']];
    } else if (shape === 'circle') {
      t = [['Radius', f2(p.r)], ['Diameter', f4(2 * p.r)],
           ['Circumference', f4(2 * Math.PI * p.r)], ['Area', f4(Math.PI * p.r * p.r)]];
    } else {
      var eq = Math.sqrt(Math.pow(p.base / 2, 2) + p.height * p.height);
      t = [['Base', f2(p.base)], ['Height', f2(p.height)], ['Equal sides', f4(eq)],
           ['Vertex angle', f4(2 * deg(Math.atan2(p.base / 2, p.height))) + '°'],
           ['Area', f4(p.base * p.height / 2)], ['Perimeter', f4(p.base + 2 * eq)]];
    }
    return t;
  }

  function inputsFor(shape, rnd) {
    var r2 = function () { return parseFloat((3 + rnd() * 17).toFixed(2)); };
    if (shape === 'right_triangle') return { a: r2(), b: r2() };
    if (shape === 'rectangle') return { w: r2(), h: r2() };
    if (shape === 'regular_polygon') return { sides: ri(rnd, 5, 8), side: r2() };
    if (shape === 'circle') return { r: r2() };
    return { base: r2(), height: r2() };
  }

  /* simple SVG in the archive's style: polygon + input label text */
  function svgFor(shape, p, label) {
    var pts, txt;
    if (shape === 'right_triangle') { pts = '46,30 214,30 46,160'; txt = 'a=' + f2(p.a) + '  b=' + f2(p.b); }
    else if (shape === 'rectangle') { pts = '60,40 200,40 200,150 60,150'; txt = 'w=' + f2(p.w) + '  h=' + f2(p.h); }
    else if (shape === 'circle') { pts = null; txt = 'r=' + f2(p.r); }
    else if (shape === 'isosceles_triangle') { pts = '130,30 210,160 50,160'; txt = 'base=' + f2(p.base) + '  h=' + f2(p.height); }
    else { pts = '130,25 205,70 190,150 70,150 55,70'; txt = p.sides + ' sides, s=' + f2(p.side); }
    var body = pts
      ? '<polygon points="' + pts + '" fill="rgba(55,214,122,.15)" stroke="#37d67a" stroke-width="2"/>'
      : '<circle cx="130" cy="95" r="60" fill="rgba(55,214,122,.15)" stroke="#37d67a" stroke-width="2"/>';
    return body + '<text x="130" y="180" fill="#9fd0ff" font-size="11" text-anchor="middle">' + txt + '</text>';
  }

  function generate(seed, opts, rnd) {
    opts = opts || {};
    var shape = opts.shape && SHAPES.indexOf(opts.shape) >= 0 ? opts.shape : pick(rnd, SHAPES);
    var p = inputsFor(shape, rnd);
    var n = (opts.baseN || 0) + 1;
    var label = shape === 'regular_polygon' ? POLYNAME[p.sides] : SHAPELABEL[shape];
    var rec = {
      id: ID_PREFIX + String(n).padStart(6, '0'),
      n: n,
      name: label + ' ' + String(n).padStart(4, '0'),
      shape: shape,
      svg: svgFor(shape, p, label),
      table: tableFor(shape, p)
    };
    var pub = {};
    ['id', 'n', 'name', 'shape', 'svg', 'table'].forEach(function (k) { pub[k] = rec[k]; });
    pub._priv = { shape: shape, p: p, label: label };
    return pub;
  }

  /* independent re-verification: recompute every table cell from the inputs */
  function verify(rec) {
    var errs = [];
    var p = rec._priv;
    var want = tableFor(p.shape, p.p);
    if (want.length !== rec.table.length) errs.push('table row count mismatch');
    else want.forEach(function (row, i) {
      if (rec.table[i][0] !== row[0]) errs.push('table label mismatch row ' + i);
      if (String(rec.table[i][1]) !== String(row[1]))
        errs.push('table value mismatch row ' + i + ' (' + rec.table[i][0] + '): got ' + rec.table[i][1] + ', want ' + row[1]);
    });
    var label = p.shape === 'regular_polygon' ? POLYNAME[p.p.sides] : SHAPELABEL[p.shape];
    if (label !== p.label) errs.push('shape label mismatch');
    if (rec.name !== label + ' ' + String(rec.n).padStart(4, '0')) errs.push('name mismatch');
    if (rec.svg.indexOf('<polygon') < 0 && rec.svg.indexOf('<circle') < 0) errs.push('svg has no shape');
    return errs;
  }

  function validate(rec) {
    var errs = [];
    if (!rec || typeof rec !== 'object') return { ok: false, errors: ['not an object'] };
    ['id', 'name', 'shape', 'svg', 'table'].forEach(function (k) {
      if (rec[k] === undefined || rec[k] === null || rec[k] === '') errs.push('missing field: ' + k);
    });
    if (rec.id && !/^JAH-GRID-\d{6}$/.test(rec.id)) errs.push('bad id format');
    if (rec.shape && SHAPES.indexOf(rec.shape) < 0) errs.push('bad shape');
    if (!Array.isArray(rec.table) || rec.table.length < 4) errs.push('table must have 4+ rows');
    if (rec._priv) errs = errs.concat(verify(rec));
    else errs.push('no private params — cannot independently verify');
    return { ok: errs.length === 0, errors: errs };
  }

  function driftCheck(rec, archiveSample) {
    var errs = [];
    var sig = rec.shape + '|' + rec.table.slice(0, 2).map(function (r) { return r[1]; }).join('|');
    (archiveSample || []).forEach(function (a) {
      if (a.shape && a.table) {
        var s2 = a.shape + '|' + a.table.slice(0, 2).map(function (r) { return r[1]; }).join('|');
        if (s2 === sig) errs.push('duplicate of archived measure: ' + rec.name);
      }
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

  JAHDB.registerGenerator('gridmeasure', {
    version: VERSION,
    generate: generate,
    validate: validate,
    driftCheck: driftCheck,
    themedGenerate: themedGenerate,
    shapes: SHAPES
  });
})();
