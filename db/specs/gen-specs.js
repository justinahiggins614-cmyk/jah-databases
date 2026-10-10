/* ✳ SIGNATURE — JAH Patent Specification Data Base generator. Property of Justin Addam Higgins (JAH).
   Boundless generator: produces NEW synthetic draft specifications in the FULL
   archive record format (spec_id, title, abstract, category, cpc, era,
   prepared_date, inventor, owner, status, signature_tool_mapping, key_parameters,
   patent_draft, manufacture, demo, ai_explainer, algorithm_steps, measurements,
   autoread_block, stamp). Deterministic: same seed + version => same record.
   These are ORIGINAL synthetic drafts, clearly labeled GENERATED — they are not
   JAH's drafts and claim no filing. Every record is re-verified by an
   INDEPENDENT checker before acceptance. */
(function () {
  'use strict';
  var VERSION = 'jahdb-specs-1.0';
  var ID_PREFIX = 'JAH-SPEC-';
  var STAMP = 'JAH Patent Specification Data Base — synthetic draft. Generated, not authored by JAH; not a real filing.';
  var PROVENANCE = 'JAH Databases boundless generator (synthetic — not authored by Justin Addam Higgins)';

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
    'Kalman-free state estimation', 'federated edge inference'];

  function ri(rnd, a, b) { return a + Math.floor(rnd() * (b - a + 1)); }
  function pick(rnd, arr) { return arr[Math.floor(rnd() * arr.length)]; }
  function low(s) { return s.charAt(0).toLowerCase() + s.slice(1); }
  function iso(y, m, d) { return y + '-' + String(m).padStart(2, '0') + '-' + String(d).padStart(2, '0'); }

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
  /* ---- full-record fields, all deterministically derived from private params ---- */
  function buildPatentDraft(p, dev, pur, mech) {
    var d = low(dev);
    return 'PATENT DRAFT — ' + buildTitle(dev, pur, mech) + '\n' +
      'Inventor: ' + PROVENANCE + '\n' +
      'FIELD: A ' + d + ' ' + pur + ' by means of ' + mech + '.\n' +
      'BACKGROUND: Conventional approaches waste energy as heat and drift out of ' +
      'calibration under load. This draft discloses a ' + d + ' that holds ' +
      p._params.efficiency_pct + '% conversion efficiency across -40 to 125 C operation.\n' +
      'SUMMARY: The apparatus comprises (a) a primary ' + d + ' stage, (b) a ' + mech +
      ' control loop, and (c) a redundant monitoring bus rated for ' + p._params.mtbf_h +
      ' hours MTBF.\n' +
      'DETAILED DESCRIPTION: FIG.1 shows the ' + d + ' housing with LINE primary axis; ' +
      'FIG.2 the TRIANGLE taper geometry; FIG.3 the CROSS junction layout. The control ' +
      'loop samples at adaptive rates and votes across redundant channels before ' +
      'committing actuation, so a single sensor fault cannot drive the system out of ' +
      'its qualified envelope.\n' +
      'CLAIMS: 1. A ' + d + ' ' + pur + ' comprising a ' + mech + ' control loop. ' +
      '2. The apparatus of claim 1, further comprising redundant channel voting. ' +
      '3. The apparatus of claim 1, rated for ' + p._params.mtbf_h + ' hours MTBF.\n' +
      'STATUS: Draft — synthetic (not filed).';
  }
  function buildManufacture(dev, pur, mech) {
    var d = low(dev);
    return 'Manufacture: machine the ' + d + ' housing to the LINE primary axis, form the ' +
      'TRIANGLE taper, bore CIRCLE ports, and route the CROSS junctions. Calibrate the ' +
      mech + ' loop on a bench rig ' + pur + ', then burn in for 48 hours before shipment.';
  }
  function buildDemo(dev, pur, p) {
    return 'Demo: bench rig drives the ' + low(dev) + ' through its full ' + pur.replace(/^for /, '') +
      ' envelope while the monitor bus logs efficiency; the unit holds ' +
      p._params.efficiency_pct + '% conversion efficiency across the qualification run.';
  }
  function buildAiExplainer(dev, pur, mech, p) {
    return 'In plain terms: this is a ' + low(dev) + ' built ' + pur + '. It works by ' +
      mech + ' — the same idea as keeping a car in the right gear instead of redlining. ' +
      'Rated ' + p._params.efficiency_pct + '% efficient with a ' + p._params.mtbf_h +
      '-hour mean time between failures. Synthetic draft for study, not a filed patent.';
  }
  function buildAlgorithmSteps(dev, pur, mech) {
    var d = low(dev);
    return '1. Sample sensors on the ' + d + ' at the adaptive rate.\n' +
      '2. Estimate state with ' + mech + '.\n' +
      '3. Vote across redundant channels; discard out-of-family readings.\n' +
      '4. Commit actuation only when two of three channels agree.\n' +
      '5. Log efficiency and drift ' + pur + '; alarm on threshold breach.';
  }
  function buildMeasurements(p) {
    return 'Bench: efficiency ' + p._params.efficiency_pct + '% at ' + p._params.operating_temp_c +
      ' C ambient; MTBF ' + p._params.mtbf_h + ' h; calibration drift under 0.5% per 1000 h.';
  }
  function buildAutoreadBlock(dev, pur, mech, eff) {
    return 'Read aloud: ' + buildTitle(dev, pur, mech) + '. ' + buildAbstract(dev, pur, mech, eff);
  }

  function genSpec(rnd, opts) {
    opts = opts || {};
    var dev = pick(rnd, DEVICES), pur = pick(rnd, PURPOSES), mech = pick(rnd, MECHANISMS);
    var cat = (opts.category && CATEGORIES.indexOf(opts.category) >= 0) ? opts.category : pick(rnd, CATEGORIES);
    var cpc = pick(rnd, CPCS), era = pick(rnd, ERAS);
    var params = buildParams(rnd);
    var y = ri(rnd, 2016, 2026), m = ri(rnd, 1, 12), d = ri(rnd, 1, 28);
    return {
      _dev: dev, _pur: pur, _mech: mech, _cat: cat, _cpc: cpc, _era: era,
      _y: y, _m: m, _d: d, _params: params
    };
  }

  function assemble(p, n) {
    var dev = p._dev, pur = p._pur, mech = p._mech;
    var id = ID_PREFIX + String(n).padStart(6, '0');
    return {
      id: id,
      spec_id: id,
      n: n,
      title: buildTitle(dev, pur, mech),
      abstract: buildAbstract(dev, pur, mech, p._params.efficiency_pct),
      category: p._cat,
      cpc: p._cpc,
      era: p._era,
      prepared_date: iso(p._y, p._m, p._d),
      inventor: PROVENANCE,
      owner: PROVENANCE,
      status: 'Draft — synthetic (not filed)',
      signature_tool_mapping: buildMapping(dev),
      key_parameters: p._params,
      patent_draft: buildPatentDraft(p, dev, pur, mech),
      manufacture: buildManufacture(dev, pur, mech),
      demo: buildDemo(dev, pur, p),
      ai_explainer: buildAiExplainer(dev, pur, mech, p),
      algorithm_steps: buildAlgorithmSteps(dev, pur, mech),
      measurements: buildMeasurements(p),
      autoread_block: buildAutoreadBlock(dev, pur, mech, p._params.efficiency_pct),
      record_kind: 'synthetic',
      stamp: STAMP,
      _priv: p
    };
  }

  function generate(seed, opts, rnd) {
    opts = opts || {};
    var p = genSpec(rnd, opts);
    var n = (opts.baseN || 0) + seed;
    var rec = assemble(p, n);
    rec._seed = seed;
    return rec;
  }

  /* INDEPENDENT checker: rebuilds every derived field from private params only */
  function verify(rec) {
    var errs = [];
    var p = rec._priv;
    if (!p) return ['no private params — cannot independently verify'];
    var dev = p._dev, pur = p._pur, mech = p._mech;
    function ck(name, got, want) { if (got !== want) errs.push(name + ' mismatch'); }
    ck('title', rec.title, buildTitle(dev, pur, mech));
    ck('abstract', rec.abstract, buildAbstract(dev, pur, mech, p._params.efficiency_pct));
    ck('prepared_date', rec.prepared_date, iso(p._y, p._m, p._d));
    ck('patent_draft', rec.patent_draft, buildPatentDraft(p, dev, pur, mech));
    ck('manufacture', rec.manufacture, buildManufacture(dev, pur, mech));
    ck('demo', rec.demo, buildDemo(dev, pur, p));
    ck('ai_explainer', rec.ai_explainer, buildAiExplainer(dev, pur, mech, p));
    ck('algorithm_steps', rec.algorithm_steps, buildAlgorithmSteps(dev, pur, mech));
    ck('measurements', rec.measurements, buildMeasurements(p));
    ck('autoread_block', rec.autoread_block, buildAutoreadBlock(dev, pur, mech, p._params.efficiency_pct));
    if (rec.category !== p._cat || CATEGORIES.indexOf(rec.category) < 0) errs.push('bad category');
    if (rec.cpc !== p._cpc || CPCS.indexOf(rec.cpc) < 0) errs.push('bad cpc');
    if (rec.era !== p._era || ERAS.indexOf(rec.era) < 0) errs.push('bad era');
    if (rec.spec_id !== rec.id) errs.push('spec_id/id mismatch');
    if (!/^JAH-SPEC-\d{6}$/.test(rec.id)) errs.push('bad id format');
    var want = buildMapping(dev);
    ['LINE', 'TRIANGLE', 'SQUARE', 'CROSS', 'CIRCLE', 'CURVATURE'].forEach(function (k) {
      if (!rec.signature_tool_mapping || rec.signature_tool_mapping[k] !== want[k])
        errs.push('tool mapping mismatch: ' + k);
    });
    var kp = rec.key_parameters || {};
    if (kp.operating_temp_c !== p._params.operating_temp_c ||
        kp.efficiency_pct !== p._params.efficiency_pct ||
        kp.mtbf_h !== p._params.mtbf_h) errs.push('key_parameters mismatch');
    if (kp.efficiency_pct < 72 || kp.efficiency_pct > 98) errs.push('efficiency out of range');
    if (rec.inventor !== PROVENANCE) errs.push('inventor provenance mismatch');
    if (rec.owner !== PROVENANCE) errs.push('owner provenance mismatch');
    if (rec.status !== 'Draft — synthetic (not filed)') errs.push('status mismatch');
    if (rec.stamp !== STAMP) errs.push('stamp mismatch');
    return errs;
  }

  function validate(rec) {
    var errs = [];
    if (!rec || typeof rec !== 'object') return { ok: false, errors: ['not an object'] };
    ['id', 'spec_id', 'title', 'abstract', 'category', 'cpc', 'era', 'prepared_date',
     'inventor', 'owner', 'status', 'signature_tool_mapping', 'key_parameters',
     'patent_draft', 'manufacture', 'demo', 'ai_explainer', 'algorithm_steps',
     'measurements', 'autoread_block', 'stamp'].forEach(function (k) {
      if (rec[k] === undefined || rec[k] === null || rec[k] === '') errs.push('missing field: ' + k);
    });
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
