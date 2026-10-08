/* ✳ SIGNATURE — JAH Solved Equations Data Base generator. Property of Justin Addam Higgins (JAH).
   Boundless generator: produces NEW solved equations in the exact archive format
   (type, title, equation, steps, solution, check, id, stamp). Deterministic:
   same seed + version => same record. Every record is validated by an
   INDEPENDENT re-solver before it is accepted. */
(function () {
  'use strict';
  var VERSION = 'jahdb-equations-1.0';
  var ID_PREFIX = 'JAH-EQ-';
  var STAMP = 'Official JAH Equation Archive — solved once, published officially, retrieved thereafter.';

  function ri(rnd, a, b) { return a + Math.floor(rnd() * (b - a + 1)); }
  function pick(rnd, arr) { return arr[Math.floor(rnd() * arr.length)]; }
  function fmt(n) { return (n < 0 ? '−' : '') + Math.abs(n); }
  function term(coef, variable) {
    if (coef === 0) return '';
    var a = Math.abs(coef);
    var s = (a === 1 && variable) ? '' : String(a);
    return s + (variable || '');
  }
  /* pretty "ax + b" with proper signs, a != 0 */
  function lin(a, b) {
    var s = term(a, 'x');
    if (b > 0) s += ' + ' + b;
    else if (b < 0) s += ' − ' + Math.abs(b);
    return s;
  }

  var TYPES = ['linear', 'quadratic', 'system', 'arithmetic'];

  function genLinear(rnd) {
    var a = ri(rnd, 2, 12), x = ri(rnd, -9, 9), b = ri(rnd, -20, 20);
    if (x === 0) x = 3;
    var c = a * x + b;
    var eq = lin(a, b) + ' = ' + c;
    return {
      type: 'linear', equation: eq,
      title: 'Solve ' + eq,
      steps: [
        eq,
        a + 'x = ' + c + ' ' + (b >= 0 ? '−' : '+') + ' ' + Math.abs(b) + ' = ' + (a * x),
        'x = ' + (a * x) + ' / ' + a + ' = ' + x
      ],
      solution: 'x = ' + x,
      check: 'Substitute x = ' + x + ': ' + a + '·' + x + (b >= 0 ? '+' : '−') + Math.abs(b) + ' = ' + c + ' ✓',
      _a: a, _b: b, _c: c, _x: x
    };
  }

  function genQuadratic(rnd) {
    var r1 = ri(rnd, -8, 8), r2 = ri(rnd, -8, 8), a = ri(rnd, 1, 5);
    if (r1 === r2) r2 = r1 + ri(rnd, 1, 4);
    /* a(x-r1)(x-r2) = ax^2 - a(r1+r2)x + a*r1*r2 */
    var b = -a * (r1 + r2), c = a * r1 * r2;
    var lhs = term(a, 'x²');
    lhs += b > 0 ? ' + ' + term(b, 'x') : (b < 0 ? ' − ' + term(-b, 'x') : '');
    lhs += c > 0 ? ' + ' + c : (c < 0 ? ' − ' + Math.abs(c) : '');
    var eq = lhs + ' = 0';
    var sols = [r1, r2].sort(function (p, q) { return p - q; });
    return {
      type: 'quadratic', equation: eq,
      title: 'Solve ' + eq,
      steps: [
        eq,
        'Factors as ' + a + '(x ' + (r1 >= 0 ? '−' : '+') + ' ' + Math.abs(r1) + ')(x ' + (r2 >= 0 ? '−' : '+') + ' ' + Math.abs(r2) + ') = 0',
        'x = ' + sols[0] + ' or x = ' + sols[1]
      ],
      solution: 'x = ' + sols[0] + ' or x = ' + sols[1],
      check: 'Roots verify: a(x−x1)(x−x2) expands back ✓',
      _a: a, _b: b, _c: c, _roots: sols
    };
  }

  function genSystem(rnd) {
    /* build from solution (x0, y0): pick a1,b1 then c1; pick a2,b2 (det != 0) then c2 */
    var x0 = ri(rnd, -6, 6), y0 = ri(rnd, -6, 6);
    var a1 = ri(rnd, 1, 6), b1 = ri(rnd, 1, 6);
    var a2 = ri(rnd, 1, 6), b2 = ri(rnd, 1, 6);
    if (a1 * b2 === a2 * b1) b2 += 1;
    var c1 = a1 * x0 + b1 * y0, c2 = a2 * x0 + b2 * y0;
    var e1 = lin(a1, b1).replace('x', 'x') + ' + ' + 0; /* placeholder replaced below */
    e1 = term(a1, 'x') + ' + ' + term(b1, 'y') + ' = ' + c1;
    var e2 = term(a2, 'x') + ' + ' + term(b2, 'y') + ' = ' + c2;
    return {
      type: 'system', equation: e1 + '; ' + e2,
      title: 'Solve the system: ' + e1 + ' , ' + e2,
      steps: [
        e1, e2,
        'Eliminate: determinant D = ' + a1 + '·' + b2 + ' − ' + a2 + '·' + b1 + ' = ' + (a1 * b2 - a2 * b1),
        'x = ' + x0 + ', y = ' + y0
      ],
      solution: 'x = ' + x0 + ', y = ' + y0,
      check: 'Substitution in both equations holds ✓',
      _x: x0, _y: y0, _a1: a1, _b1: b1, _c1: c1, _a2: a2, _b2: b2, _c2: c2
    };
  }

  function genArithmetic(rnd) {
    var op = pick(rnd, ['+', '−', '×', '÷']);
    var a, b, ans, eq;
    if (op === '+') { a = ri(rnd, 11, 999); b = ri(rnd, 11, 999); ans = a + b; eq = a + ' + ' + b; }
    else if (op === '−') { a = ri(rnd, 50, 999); b = ri(rnd, 11, a - 1); ans = a - b; eq = a + ' − ' + b; }
    else if (op === '×') { a = ri(rnd, 3, 25); b = ri(rnd, 3, 25); ans = a * b; eq = a + ' × ' + b; }
    else { b = ri(rnd, 2, 12); ans = ri(rnd, 2, 25); a = b * ans; eq = a + ' ÷ ' + b; }
    return {
      type: 'arithmetic', equation: eq,
      title: 'Compute ' + eq,
      steps: [eq, '= ' + ans],
      solution: String(ans),
      check: 'Direct computation ✓',
      _a: a, _b: b, _ans: ans, _op: op
    };
  }

  /* ---------- independent re-solver (validation) ---------- */
  function verify(rec) {
    var errs = [];
    function numok(v) { return typeof v === 'number' && isFinite(v); }
    if (rec.type === 'linear') {
      if (!(numok(rec._a) && rec._a !== 0 && numok(rec._x))) errs.push('bad linear params');
      else if (rec._a * rec._x + rec._b !== rec._c) errs.push('linear solution does not satisfy equation');
      if (rec.solution !== 'x = ' + rec._x) errs.push('linear solution string mismatch');
    } else if (rec.type === 'quadratic') {
      if (!(numok(rec._a) && rec._a !== 0)) errs.push('bad quadratic params');
      else {
        var ok = rec._roots.every(function (r) { return rec._a * r * r + rec._b * r + rec._c === 0; });
        if (!ok) errs.push('quadratic roots do not satisfy equation');
      }
    } else if (rec.type === 'system') {
      var p = rec;
      if (!(numok(p._x) && numok(p._y))) errs.push('bad system params');
      else if (p._a1 * p._x + p._b1 * p._y !== p._c1 || p._a2 * p._x + p._b2 * p._y !== p._c2)
        errs.push('system solution does not satisfy equations');
      if ((p._a1 * p._b2 - p._a2 * p._b1) === 0) errs.push('system is singular');
    } else if (rec.type === 'arithmetic') {
      var want = rec._op === '+' ? rec._a + rec._b : rec._op === '−' ? rec._a - rec._b : rec._op === '×' ? rec._a * rec._b : rec._a / rec._b;
      if (want !== rec._ans) errs.push('arithmetic mismatch');
      if (String(rec.solution) !== String(rec._ans)) errs.push('arithmetic solution string mismatch');
    } else errs.push('unknown type ' + rec.type);
    return errs;
  }

  function generate(seed, opts, rnd) {
    opts = opts || {};
    var type = opts.type && TYPES.indexOf(opts.type) >= 0 ? opts.type : TYPES[Math.floor(rnd() * TYPES.length)];
    var rec = type === 'linear' ? genLinear(rnd) : type === 'quadratic' ? genQuadratic(rnd) :
              type === 'system' ? genSystem(rnd) : genArithmetic(rnd);
    var n = (opts.baseN || 0) + 1;
    rec.id = ID_PREFIX + String(n).padStart(8, '0');
    rec.n = n;
    rec.stamp = STAMP;
    rec._seed = seed;
    /* strip private fields for the public record */
    var pub = {};
    ['id', 'n', 'type', 'title', 'equation', 'steps', 'solution', 'check', 'stamp'].forEach(function (k) { pub[k] = rec[k]; });
    pub._priv = rec;
    return pub;
  }

  function validate(rec) {
    var errs = [];
    if (!rec || typeof rec !== 'object') return { ok: false, errors: ['not an object'] };
    ['id', 'type', 'title', 'equation', 'steps', 'solution', 'check'].forEach(function (k) {
      if (rec[k] === undefined || rec[k] === null || rec[k] === '') errs.push('missing field: ' + k);
    });
    if (rec.id && !/^JAH-EQ-\d{8}$/.test(rec.id)) errs.push('bad id format');
    if (rec.type && TYPES.indexOf(rec.type) < 0) errs.push('bad type');
    if (!Array.isArray(rec.steps) || rec.steps.length === 0) errs.push('steps must be a non-empty array');
    if (rec._priv) {
      var v = verify(rec._priv);
      errs = errs.concat(v);
    } else errs.push('no private solution params — cannot independently verify');
    return { ok: errs.length === 0, errors: errs };
  }

  /* drift check: generated record must not duplicate an archive sample's equation text */
  function driftCheck(rec, archiveSample) {
    var errs = [];
    (archiveSample || []).forEach(function (a) {
      var eq = a.equation || (a[2] /* idx row */);
      if (eq && String(eq).replace(/\s+/g, '') === String(rec.equation).replace(/\s+/g, ''))
        errs.push('duplicate of archived equation: ' + rec.equation);
    });
    return { ok: errs.length === 0, errors: errs };
  }

  /* cross-database: borrow a number theme from another database's sample */
  function themedGenerate(seed, opts, rnd, themeSamples) {
    var rec = generate(seed, opts, rnd);
    if (themeSamples && themeSamples.length) {
      var t = themeSamples[Math.floor(rnd() * themeSamples.length)];
      var nums = String(JSON.stringify(t)).match(/\d+/g);
      if (nums && nums.length) {
        /* nudge: re-seed with a theme number folded in — still deterministic */
        var rec2 = generate(seed + (parseInt(nums[0], 10) % 1000), opts, JAHDB.prng(JAHDB.hashStr(String(seed) + nums[0])));
        rec2.id = rec.id; rec2.n = rec.n;
        return rec2;
      }
    }
    return rec;
  }

  JAHDB.registerGenerator('equations', {
    version: VERSION,
    generate: generate,
    validate: validate,
    driftCheck: driftCheck,
    themedGenerate: themedGenerate,
    types: TYPES
  });
})();
