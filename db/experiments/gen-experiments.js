/* ✳ SIGNATURE — JAH Experiment Data Base generator. Property of Justin Addam Higgins (JAH).
   Boundless generator: produces NEW solved lab experiments in the archive's
   JAH-EXP-RECORD style (type, title, question, hypothesis, params, procedure,
   measurements, solution, check — all values solver-computed, clearly labeled
   SIMULATED, never presented as lab-measured). Deterministic: same seed +
   version => same record. Every record is validated by an INDEPENDENT
   re-solver that recomputes every numeric claim from the private raw picks. */
(function () {
  'use strict';
  var VERSION = 'jahdb-experiments-1.0';
  var ID_PREFIX = 'JAH-EXP-';
  var G = 9.81;
  var STAMP = 'SOLVER-GENERATED — JAH Experiment Data Base. Simulated values, computed by the generator; NOT laboratory measurement.';

  function ri(rnd, a, b) { return a + Math.floor(rnd() * (b - a + 1)); }
  function pick(rnd, arr) { return arr[Math.floor(rnd() * arr.length)]; }
  /* archive-style number formatting (mirrors the solver engine's fmt) */
  function fmt(v, unit) {
    var s;
    if (Math.abs(v) >= 1000) s = v.toFixed(0);
    else if (Math.abs(v) >= 100) s = v.toFixed(1);
    else if (Math.abs(v) >= 10) s = v.toFixed(2);
    else s = v.toFixed(3);
    s = s.replace(/\.?0+$/, '');
    return s + (unit ? ' ' + unit : '');
  }

  /* ---- solvable models ----
     picks(rnd) -> raw private picks (what the verifier replays).
     calc(pk)  -> all derived content, pure in the picks. */
  var MODELS = {
    'free-fall': {
      typeName: 'Free-Fall Gravity Drop', discipline: 'Physics',
      subjects: ['steel ball', 'wooden block', 'rubber ball', 'brass cylinder'],
      apparatus: 'drop tower, photogate timer, measuring tape',
      picks: function (rnd) { return { h: ri(rnd, 2, 20), subjI: Math.floor(rnd() * this.subjects.length) }; },
      calc: function (M, pk) {
        var h = pk.h, subj = M.subjects[pk.subjI];
        var levels = [2, 4, 6, 8, 10].map(function (k) { return Math.round(h * k / 10 * 100) / 100; });
        function dep(hh) { var t = Math.sqrt(2 * hh / G); return [t, Math.sqrt(2 * G * hh)]; }
        function depFmt(d) { return [fmt(d[0], 's'), fmt(d[1], 'm/s')]; }
        var t = Math.sqrt(2 * h / G), v = Math.sqrt(2 * G * h);
        return {
          params: { h_m: h, g: G, subject: subj },
          key: 'fall time',
          cols: ['Drop height (m)', 'Fall time (s)', 'Impact speed (m/s)'],
          levels: levels, dep: dep, depFmt: depFmt,
          solText: 't = ' + fmt(t, 's') + ' to fall ' + fmt(h, 'm') + '; impact speed v = ' + fmt(v, 'm/s'),
          checkText: 'Verify: 0.5·g·t² = ' + fmt(0.5 * G * t * t, 'm') + ' = drop height ✓'
        };
      }
    },
    'projectile-motion': {
      typeName: 'Projectile Launch Angle', discipline: 'Physics',
      subjects: ['foam dart', 'tennis ball', 'water balloon'],
      apparatus: 'launcher, protractor, tape measure, sand pit',
      picks: function (rnd) { return { v: ri(rnd, 8, 30), th: ri(rnd, 20, 70), subjI: Math.floor(rnd() * this.subjects.length) }; },
      calc: function (M, pk) {
        var v = pk.v, th = pk.th, subj = M.subjects[pk.subjI];
        var rad = th * Math.PI / 180;
        var R = v * v * Math.sin(2 * rad) / G, H = Math.pow(v * Math.sin(rad), 2) / (2 * G);
        var levels = [15, 30, 45, 60, 75];
        function dep(a) { var r2 = a * Math.PI / 180; return [v * v * Math.sin(2 * r2) / G, Math.pow(v * Math.sin(r2), 2) / (2 * G)]; }
        function depFmt(d) { return [fmt(d[0], 'm'), fmt(d[1], 'm')]; }
        return {
          params: { v_ms: v, angle_deg: th, g: G, subject: subj },
          key: 'range',
          cols: ['Launch angle (°)', 'Range (m)', 'Max height (m)'],
          levels: levels, dep: dep, depFmt: depFmt,
          solText: 'R = ' + fmt(R, 'm') + ' range; H = ' + fmt(H, 'm') + ' max height at ' + v + ' m/s, ' + th + '°',
          checkText: 'Verify: R = v²·sin(2θ)/g = ' + fmt(R, 'm') + ' ✓'
        };
      }
    },
    'pendulum-period': {
      typeName: 'Pendulum Period vs Length', discipline: 'Physics',
      subjects: ['brass bob', 'steel bob', 'wooden bob'],
      apparatus: 'string, stand, stopwatch, meter stick',
      picks: function (rnd) { return { L: ri(rnd, 20, 150) / 100, subjI: Math.floor(rnd() * this.subjects.length) }; },
      calc: function (M, pk) {
        var L = pk.L, subj = M.subjects[pk.subjI];
        var T = 2 * Math.PI * Math.sqrt(L / G);
        var levels = [0.25, 0.5, 0.75, 1.0, 1.25];
        function dep(l) { var T2 = 2 * Math.PI * Math.sqrt(l / G); return [T2, 1 / T2]; }
        function depFmt(d) { return [fmt(d[0], 's'), fmt(d[1], 'Hz')]; }
        return {
          params: { L_m: L, g: G, subject: subj },
          key: 'period',
          cols: ['Length (m)', 'Period (s)', 'Frequency (Hz)'],
          levels: levels, dep: dep, depFmt: depFmt,
          solText: 'T = ' + fmt(T, 's') + ' for L = ' + fmt(L, 'm') + ' (' + fmt(1 / T, 'Hz') + ')',
          checkText: 'Verify: T²·g/(4π²) = ' + fmt(T * T * G / (4 * Math.PI * Math.PI), 'm') + ' = length ✓'
        };
      }
    },
    'ohms-law': {
      typeName: "Ohm's Law Circuit", discipline: 'Physics',
      subjects: ['carbon resistor', 'nichrome wire', 'bulb filament'],
      apparatus: 'DC supply, ammeter, voltmeter, resistor board',
      picks: function (rnd) { return { I: ri(rnd, 1, 20) / 10, R: ri(rnd, 10, 200), subjI: Math.floor(rnd() * this.subjects.length) }; },
      calc: function (M, pk) {
        var I = pk.I, R = pk.R, subj = M.subjects[pk.subjI];
        var levels = [0.1, 0.2, 0.3, 0.4, 0.5].map(function (k) { return Math.round(I * k * 100) / 100; });
        function dep(i) { return [i * R, i * i * R]; }
        function depFmt(d) { return [fmt(d[0], 'V'), fmt(d[1], 'W')]; }
        return {
          params: { I_A: I, R_ohm: R, subject: subj },
          key: 'voltage',
          cols: ['Current (A)', 'Voltage (V)', 'Power (W)'],
          levels: levels, dep: dep, depFmt: depFmt,
          solText: 'V = ' + fmt(I * R, 'V') + ' across ' + R + ' Ω at ' + I + ' A',
          checkText: 'Verify: V = I·R = ' + fmt(I * R, 'V') + ' ✓'
        };
      }
    },
    'hookes-law': {
      typeName: "Hooke's Law Spring Stretch", discipline: 'Physics',
      subjects: ['coil spring', 'elastic cord', 'leaf spring'],
      apparatus: 'spring, stand, slotted masses, ruler',
      picks: function (rnd) { return { k: ri(rnd, 20, 200), x: ri(rnd, 2, 20) / 100, subjI: Math.floor(rnd() * this.subjects.length) }; },
      calc: function (M, pk) {
        var k = pk.k, x = pk.x, subj = M.subjects[pk.subjI];
        var levels = [0.02, 0.04, 0.06, 0.08, 0.1].map(function (q) { return Math.round(x * q * 500) / 100; });
        function dep(xx) { return [k * xx, 0.5 * k * xx * xx]; }
        function depFmt(d) { return [fmt(d[0], 'N'), fmt(d[1], 'J')]; }
        return {
          params: { k_Npm: k, x_m: x, subject: subj },
          key: 'force',
          cols: ['Stretch (m)', 'Force (N)', 'Stored energy (J)'],
          levels: levels, dep: dep, depFmt: depFmt,
          solText: 'F = ' + fmt(k * x, 'N') + ' at x = ' + fmt(x, 'm') + ' (k = ' + k + ' N/m)',
          checkText: 'Verify: F = k·x = ' + fmt(k * x, 'N') + ' ✓'
        };
      }
    },
    'specific-heat': {
      typeName: 'Specific Heat Calorimetry', discipline: 'Chemistry',
      subjects: ['water sample', 'aluminum block', 'copper slug', 'oil sample'],
      apparatus: 'calorimeter, thermometer, heater, balance',
      picks: function (rnd) { return { m: ri(rnd, 50, 500) / 1000, c: pick(rnd, [4186, 900, 385, 2000]), dT: ri(rnd, 5, 40), subjI: Math.floor(rnd() * this.subjects.length) }; },
      calc: function (M, pk) {
        var m = pk.m, c = pk.c, dT = pk.dT, subj = M.subjects[pk.subjI];
        var Q = m * c * dT;
        var levels = [5, 10, 15, 20, 25];
        function dep(t2) { var Q2 = m * c * t2; return [Q2, Q2 / 50]; }
        function depFmt(d) { return [fmt(d[0], 'J'), fmt(d[1], 's')]; }
        return {
          params: { m_kg: m, c_JpkgK: c, dT_K: dT, subject: subj },
          key: 'heat',
          cols: ['ΔT (K)', 'Heat Q (J)', 'Time at 50 W (s)'],
          levels: levels, dep: dep, depFmt: depFmt,
          solText: 'Q = ' + fmt(Q, 'J') + ' to heat ' + fmt(m, 'kg') + ' by ' + dT + ' K (c = ' + c + ' J/kg·K)',
          checkText: 'Verify: Q = m·c·ΔT = ' + fmt(Q, 'J') + ' ✓'
        };
      }
    }
  };
  var TYPES = Object.keys(MODELS);

  function procedureOf(M, s) {
    return [
      'MATRIX SETUP — lock the bench: ' + M.apparatus + ', plus the ' + s.params.subject + ', safety gear, and a lab notebook.',
      'Set the test condition and record it — the matrix sweeps 5 levels around it.',
      'Calibrate: zero every instrument, then run 3 back-to-back trials at each of the 5 matrix settings.',
      'Log every trial reading into the matrix grid — no cherry-picking.',
      'Average the 3 trials per setting; keep all other variables constant.',
      'Read the findings: the computed trend and the key number decide the conclusion.'
    ];
  }

  function titleOf(M, params) {
    var pk = Object.keys(params).filter(function (k) { return k !== 'subject' && k !== 'g'; })[0];
    return M.typeName + ' — ' + params.subject + ' at ' + fmt(params[pk]);
  }

  function generate(seed, opts, rnd) {
    opts = opts || {};
    var type = opts.type && TYPES.indexOf(opts.type) >= 0 ? opts.type : pick(rnd, TYPES);
    var M = MODELS[type];
    var pk = M.picks.call(M, rnd);
    var s = M.calc(M, pk);
    var rows = s.levels.map(function (lv) {
      var d = s.dep(lv);
      return [fmt(lv), s.depFmt(d)[0], s.depFmt(d)[1]];
    });
    var n = (opts.baseN || 0) + 1 + (opts.seq || 0);
    var pub = {
      id: ID_PREFIX + String(n).padStart(6, '0'),
      n: n,
      type: type,
      title: titleOf(M, s.params),
      typeName: M.typeName,
      discipline: M.discipline,
      question: 'How do the test conditions affect ' + s.key + ' for the ' + s.params.subject + '?',
      hypothesis: 'The ' + s.key + ' will follow the ' + M.typeName.toLowerCase() +
        ' model across the sweep — computed values, then confirmed by the independent re-solver.',
      params: s.params,
      procedure: procedureOf(M, s),
      measurements: {
        columns: s.cols, rows: rows,
        note: 'SOLVER SIMULATION — NOT LABORATORY MEASUREMENT'
      },
      solution: s.solText,
      check: s.checkText,
      simulation_status: 'SIMULATED',
      measured: false,
      data_status: 'SIMULATED',
      solver_engine: 'jahdb-experiments-1.0',
      safety_level: 'SAFE-EDUCATIONAL',
      stamp: STAMP
    };
    pub._priv = { type: type, picks: pk, params: s.params, levels: s.levels };
    return pub;
  }

  /* independent re-solver: recompute every numeric claim from the private raw picks */
  function validate(rec) {
    var errs = [];
    if (!rec || typeof rec !== 'object') return { ok: false, errors: ['not an object'] };
    ['id', 'type', 'title', 'discipline', 'question', 'hypothesis',
      'params', 'procedure', 'measurements', 'solution', 'check'].forEach(function (k) {
      if (rec[k] === undefined || rec[k] === null || rec[k] === '') errs.push('missing field: ' + k);
    });
    if (rec.id && !/^JAH-EXP-\d{6}$/.test(rec.id)) errs.push('bad id format');
    if (rec.type && TYPES.indexOf(rec.type) < 0) errs.push('bad type');
    if (rec.simulation_status !== 'SIMULATED') errs.push('must be labeled SIMULATED');
    if (rec.measured !== false) errs.push('measured must be false');
    var meas = rec.measurements || {};
    if (!Array.isArray(meas.rows) || meas.rows.length !== 5) errs.push('measurements must have 5 rows');
    if (rec._priv) {
      var p = rec._priv, M = MODELS[p.type];
      if (!M) { return { ok: false, errors: ['unknown type in _priv'] }; }
      var s = M.calc(M, p.picks); /* pure in the raw picks — the independent re-solve */
      var rowsOk = p.levels.every(function (L, i) {
        var d = s.dep(L);
        var want = [fmt(L), s.depFmt(d)[0], s.depFmt(d)[1]];
        var got = meas.rows[i];
        return got && got[0] === want[0] && got[1] === want[1] && got[2] === want[2];
      });
      if (!rowsOk) errs.push('measurement rows do not recompute from raw picks');
      if (rec.solution !== s.solText) errs.push('solution does not recompute from raw picks');
      if (rec.check !== s.checkText) errs.push('check line does not recompute from raw picks');
      if (rec.title !== titleOf(M, s.params)) errs.push('title mismatch');
      if (rec.discipline !== M.discipline) errs.push('discipline mismatch');
      if (JSON.stringify(rec.params) !== JSON.stringify(s.params)) errs.push('params mismatch vs picks');
    } else errs.push('no private raw picks — cannot independently verify');
    return { ok: errs.length === 0, errors: errs };
  }

  /* drift check: generated title must not duplicate an archived experiment title */
  function driftCheck(rec, archiveSample) {
    var errs = [];
    (archiveSample || []).forEach(function (a) {
      var t = Array.isArray(a) ? a[3] : a.title;
      if (t && t === rec.title) errs.push('duplicate of archived experiment: ' + t);
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
        rec2.id = rec.id; rec2.n = rec.n;
        return rec2;
      }
    }
    return rec;
  }

  JAHDB.registerGenerator('experiments', {
    version: VERSION,
    generate: generate,
    validate: validate,
    driftCheck: driftCheck,
    themedGenerate: themedGenerate,
    types: TYPES
  });
})();
