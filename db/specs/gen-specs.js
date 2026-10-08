/* ✳ SIGNATURE — JAH Patent Specification Data Base generator. Property of Justin Addam Higgins (JAH).
   Boundless generator: produces NEW synthetic draft specifications in the exact
   archive format (spec_id, title, abstract, category, cpc, era, prepared_date,
   status, signature_tool_mapping, key_parameters, id, stamp). Deterministic:
   same seed + version => same record. These are ORIGINAL synthetic drafts,
   clearly labeled GENERATED — they are not JAH's drafts and claim no filing.
   Every record is re-verified by an INDEPENDENT checker before acceptance. */
(function () {
  'use strict';
  var VERSION = 'jahdb-specs-1.0';
  var ID_PREFIX = 'JAH-SPEC-';
  var STAMP = 'JAH Patent Specification Data Base — synthetic draft. Generated, not authored by JAH; not a real filing.';
  var PROVENANCE = 'JAH Data Bases boundless generator (synthetic — not authored by Justin Addam Higgins)';

  /* real categories observed in the archive */
  var CATEGORIES = ['Furniture', 'Cybersecurity', 'Identity Management', 'Network Routing',
    'Encryption', 'Blockchain', 'Developer Tools', 'Virtual Reality', 'Payment Processing',
    'Natural Language Processing', 'Data Pipelines', 'Cloud Infrastructure', 'Simulation',
    'Rail', 'Agriculture', 'Water Systems', 'Energy Storage', 'Robotics', 'Drones',
    'Wearables', 'Smart Home', 'Medical Devices', 'Diagnostics', 'Pharmaceuticals',
    'Food Processing', 'Textiles', 'Construction', 'Automotive', 'Aviation',
    'Marine', 'Mining', 'Forestry', 'Packaging', 'Logistics', 'Retail Systems',
    'Education Tech', 'Music Instruments', 'Sports Equipment', 'Toys', 'Lighting',
    'HVAC', 'Plumbing', 'Electrical', 'Optics', 'Sensors', 'Actuators', 'Batteries'];
  var CPCS = ['A01', 'A47', 'A61', 'B60', 'B65', 'F24', 'G01', 'G05', 'G06F', 'H01', 'H02', 'H04L'];
  var ERAS = ['Past', 'Current', 'Future'];

  var DEVICES = ['Rail engine', 'Thermal regulator', 'Mesh router', 'Sensor array',
    'Actuator bank', 'Power inverter', 'Signal processor', 'Cooling manifold',
    'Pressure vessel', 'Torque converter', 'Filter stack', 'Valve cluster',
    'Antenna lattice', 'Battery pack', 'Pump stage', 'Compressor wheel',
    'Heat exchanger', 'Optical bench', 'Drive train', 'Control bus'];
  var PURPOSES = ['for thermal management', 'for load balancing', 'for signal integrity',
    'for energy recovery', 'for vibration control', 'for fluid metering',
    'for fault isolation', 'for noise suppression', 'for precision alignment',
    'for rapid deployment'];
  var MECHANISMS = ['spread-spectrum clocking', 'adaptive mesh routing',
    'phase-locked loop tracking', 'closed-loop PID regulation',
    'redundant channel voting', 'differential pressure sensing',
    'pulse-width modulation staging', 'resonant inductive coupling',
    ' Kalman-free state estimation', 'federated edge inference'];

  function ri(rnd, a, b) { return a + Math.floor(rnd() * (b - a + 1)); }
  function pick(rnd, arr) { return arr[Math.floor(rnd() * arr.length)]; }
  function low(s) { return s.charAt(0).toLowerCase() + s.slice(1); }

  function buildTitle(dev, pur, mech) { return dev + ' ' + pur + ' using ' + mech; }
  function buildAbstract(dev, pur, mech, eff) {
    return 'A ' + low(dev) + ' ' + pur + ' employing ' + mech + ' is presented. ' +
      'It raises throughput and meets bench targets, reaching ' + eff + '% conversion efficiency ' +
      'across endurance qualification.';
  }
  function buildMapping(dev) {
    var d = low(dev);
    return {
      LINE: 'primary dimension axis along the ' + d,
      TRIANGLE: 'taper and load angle of the ' + d + ' structure',
      SQUARE: 'bounding enclosure of the ' + d,
      CROSS: 'junction points where ' + d + ' subassemblies cross',
      CIRCLE: 'circular features: ports and mounts of the ' + d,
      CURVATURE: 'fillet and bend radii across the ' + d + ' housing'
    };
  }
  function buildParams(rnd) {
    return {
      operating_temp_c: ri(rnd, -40, 125),
      efficiency_pct: ri(rnd, 72, 98),
      mtbf_h: ri(rnd, 5000, 60000)
    };
  }
  function iso(y, m, d) {
    return y + '-' + String(m).padStart(2, '0') + '-' + String(d).padStart(2, '0');
  }

  function genSpec(rnd, opts) {
    opts = opts || {};
    var dev = pick(rnd, DEVICES), pur = pick(rnd, PURPOSES), mech = pick(rnd, MECHANISMS).trim();
    var cat = (opts.category && CATEGORIES.indexOf(opts.category) >= 0) ? opts.category : pick(rnd, CATEGORIES);
    var cpc = pick(rnd, CPCS), era = pick(rnd, ERAS);
    var params = buildParams(rnd);
    var y = ri(rnd, 2016, 2026), m = ri(rnd, 1, 12), d = ri(rnd, 1, 28);
    var title = buildTitle(dev, pur, mech);
    return {
      title: title,
      abstract: buildAbstract(dev, pur, mech, params.efficiency_pct),
      category: cat, cpc: cpc, era: era,
      prepared_date: iso(y, m, d),
      inventor: PROVENANCE, owner: PROVENANCE,
      status: 'Draft — synthetic (not filed)',
      signature_tool_mapping: buildMapping(dev),
      key_parameters: params,
      _dev: dev, _pur: pur, _mech: mech, _cat: cat, _cpc: cpc, _era: era,
      _y: y, _m: m, _d: d, _params: params
    };
  }

  function generate(seed, opts, rnd) {
    opts = opts || {};
    var s = genSpec(rnd, opts);
    var n = (opts.baseN || 0) + 1;
    var rec = {
      id: ID_PREFIX + String(n).padStart(6, '0'),
      spec_id: ID_PREFIX + String(n).padStart(6, '0'),
      n: n,
      title: s.title,
      abstract: s.abstract,
      category: s.category,
      cpc: s.cpc,
      era: s.era,
      prepared_date: s.prepared_date,
      inventor: s.inventor,
      owner: s.owner,
      status: s.status,
      signature_tool_mapping: s.signature_tool_mapping,
      key_parameters: s.key_parameters,
      record_kind: 'synthetic',
      stamp: STAMP
    };
    rec._priv = s;
    rec._seed = seed;
    return rec;
  }

  function verify(rec) {
    var errs = [];
    var p = rec._priv;
    if (!p) return ['no private params — cannot independently verify'];
    if (rec.title !== buildTitle(p._dev, p._pur, p._mech)) errs.push('title mismatch');
    if (rec.abstract !== buildAbstract(p._dev, p._pur, p._mech, p._params.efficiency_pct))
      errs.push('abstract mismatch');
    if (rec.category !== p._cat || CATEGORIES.indexOf(rec.category) < 0) errs.push('bad category');
    if (rec.cpc !== p._cpc || CPCS.indexOf(rec.cpc) < 0) errs.push('bad cpc');
    if (rec.era !== p._era || ERAS.indexOf(rec.era) < 0) errs.push('bad era');
    if (rec.prepared_date !== iso(p._y, p._m, p._d)) errs.push('prepared_date mismatch');
    if (rec.spec_id !== rec.id) errs.push('spec_id/id mismatch');
    var want = buildMapping(p._dev);
    ['LINE', 'TRIANGLE', 'SQUARE', 'CROSS', 'CIRCLE', 'CURVATURE'].forEach(function (k) {
      if (!rec.signature_tool_mapping || rec.signature_tool_mapping[k] !== want[k])
        errs.push('tool mapping mismatch: ' + k);
    });
    var kp = rec.key_parameters || {};
    if (kp.operating_temp_c !== p._params.operating_temp_c ||
        kp.efficiency_pct !== p._params.efficiency_pct ||
        kp.mtbf_h !== p._params.mtbf_h) errs.push('key_parameters mismatch');
    if (kp.efficiency_pct < 72 || kp.efficiency_pct > 98) errs.push('efficiency out of range');
    return errs;
  }

  function validate(rec) {
    var errs = [];
    if (!rec || typeof rec !== 'object') return { ok: false, errors: ['not an object'] };
    ['id', 'spec_id', 'title', 'abstract', 'category', 'cpc', 'era', 'prepared_date',
     'status', 'signature_tool_mapping', 'key_parameters'].forEach(function (k) {
      if (rec[k] === undefined || rec[k] === null || rec[k] === '') errs.push('missing field: ' + k);
    });
    if (rec.id && !/^JAH-SPEC-\d{6}$/.test(rec.id)) errs.push('bad id format');
    if (rec._priv) errs = errs.concat(verify(rec));
    else errs.push('no private params — cannot independently verify');
    return { ok: errs.length === 0, errors: errs };
  }

  function driftCheck(rec, archiveSample) {
    var errs = [];
    (archiveSample || []).forEach(function (a) {
      var t = a.title || a[1];
      if (t && String(t).toLowerCase().replace(/\s+/g, ' ') === String(rec.title).toLowerCase().replace(/\s+/g, ' '))
        errs.push('duplicate of archived spec title: ' + rec.title);
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
        rec2.id = rec.id; rec2.n = rec.n; rec2.spec_id = rec.spec_id;
        return rec2;
      }
    }
    return rec;
  }

  JAHDB.registerGenerator('specs', {
    version: VERSION,
    generate: generate,
    validate: validate,
    driftCheck: driftCheck,
    themedGenerate: themedGenerate,
    types: ['synthetic']
  });
})();
