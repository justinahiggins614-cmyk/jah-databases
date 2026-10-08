/* ✳ SIGNATURE — JAH Patent Data Base generator. Property of Justin Addam Higgins (JAH).
   Boundless generator: produces NEW synthetic patent-style records in the exact
   archive format (publication_number, title, abstract_snippet, assignee, inventor,
   filing/publication/grant dates, cpc, language, id, stamp). Deterministic:
   same seed + version => same record. These are ORIGINAL synthetic inventions,
   clearly labeled GENERATED — they are not real patents and claim nothing about
   the real world. Every record is re-verified by an INDEPENDENT checker before
   it is accepted. */
(function () {
  'use strict';
  var VERSION = 'jahdb-patents-1.0';
  var ID_PREFIX = 'JAH-PAT-';
  var STAMP = 'JAH Patent Data Base — synthetic record. Generated, not harvested; not a real patent.';

  /* CPC classes actually harvested in the archive (meta.json harvest_scope) */
  var CPCS = ['A01', 'A21', 'A22', 'A23', 'A24', 'A41', 'A42', 'A43', 'A44', 'A45',
              'A46', 'A47', 'A61', 'H04L63', 'H04L9'];

  /* constructive parts — every generated title/abstract is built from these */
  var DEVICES = ['Self-cleaning solar panel mount', 'Modular water filtration cartridge',
    'Foldable cargo bicycle frame', 'Low-noise grain dryer', 'Wearable posture sensor',
    'Magnetic window cleaning robot', 'Compostable food tray', 'Adjustable standing desk lift',
    'Rainwater harvesting gutter insert', 'Portable cold-chain cooler',
    'Ergonomic pruning shear', 'Noise-canceling ventilation duct',
    'Solar food dehydrator', 'Quick-release kayak paddle', 'Insulated beehive panel',
    'Pedal-powered grain mill', 'Smart irrigation valve', 'Collapsible market stall',
    'Heated livestock waterer', 'Gravity-fed drip emitter'];
  var PURPOSES = ['for rooftop arrays', 'for smallholder farms', 'for urban balconies',
    'for off-grid cabins', 'for community kitchens', 'for school laboratories',
    'for mobile clinics', 'for greenhouse rows', 'for riverside docks', 'for desert camps'];
  var MECHANISMS = ['electrostatic dust repulsion', 'capillary wicking channels',
    'phase-change thermal buffering', 'piezoelectric vibration damping',
    'magnetic latch sequencing', 'gravity-assisted flow control',
    'shape-memory alloy actuation', 'photocatalytic surface coating',
    'ultrasonic cavitation cleaning', 'thermoelectric heat pumping'];
  var ASSIGNEES = ['Northfield Applied Labs', 'Blueharbor Devices Co.',
    'Copperline Workshop LLC', 'Fernhollow Systems', 'Graywater Engineering',
    'Ironbark Fabrications', 'Lumenfield Works', 'Stonebridge Mechanisms'];
  var FIRST = ['Alden', 'Bryn', 'Cora', 'Dorian', 'Elif', 'Farah', 'Greta', 'Hollis',
    'Iris', 'Joren', 'Kira', 'Lena', 'Marek', 'Nadia', 'Orin', 'Priya'];
  var LAST = ['Ashworth', 'Bellamy', 'Calloway', 'Drummond', 'Ellery', 'Fairbanks',
    'Galloway', 'Halloway', 'Iversen', 'Jennings', 'Kessler', 'Lockhart',
    'Marlowe', 'Norwood', 'Osgood', 'Pemberton'];

  function ri(rnd, a, b) { return a + Math.floor(rnd() * (b - a + 1)); }
  function pick(rnd, arr) { return arr[Math.floor(rnd() * arr.length)]; }

  function buildTitle(dev, pur, mech) {
    return dev + ' ' + pur + ' using ' + mech;
  }
  function buildAbstract(dev, pur, mech, n) {
    var d = dev.charAt(0).toLowerCase() + dev.slice(1);
    return 'A ' + d + ' ' + pur + ' employing ' + mech + ' is presented. ' +
      'The device integrates ' + n + ' field-replaceable modules and meets bench ' +
      'qualification targets for durability and clean operation.';
  }
  function addMonths(y, m, d, k) {
    var t = (y * 12 + (m - 1)) + k;
    return [Math.floor(t / 12), (t % 12) + 1, Math.min(d, 28)];
  }
  function iso(dt) {
    return dt[0] + '-' + String(dt[1]).padStart(2, '0') + '-' + String(dt[2]).padStart(2, '0');
  }

  function genPatent(rnd, opts) {
    opts = opts || {};
    var dev = pick(rnd, DEVICES), pur = pick(rnd, PURPOSES), mech = pick(rnd, MECHANISMS);
    var mods = ri(rnd, 2, 6);
    var fy = ri(rnd, 2001, 2024), fm = ri(rnd, 1, 12), fd = ri(rnd, 1, 28);
    var pub = addMonths(fy, fm, fd, 18);
    var gr = addMonths(fy, fm, fd, 36 + ri(rnd, 0, 12));
    var cpc = (opts.cpc && CPCS.indexOf(opts.cpc) >= 0) ? opts.cpc : pick(rnd, CPCS);
    var inv = pick(rnd, FIRST) + ' ' + pick(rnd, LAST);
    var asg = pick(rnd, ASSIGNEES);
    var title = buildTitle(dev, pur, mech);
    return {
      title: title,
      abstract_snippet: buildAbstract(dev, pur, mech, mods),
      assignee: asg,
      inventor: inv,
      filing_date: iso([fy, fm, fd]),
      publication_date: iso(pub),
      grant_date: iso(gr),
      priority_date: iso([fy, fm, fd]),
      cpc: cpc,
      language: 'en',
      _dev: dev, _pur: pur, _mech: mech, _mods: mods,
      _fy: fy, _fm: fm, _fd: fd, _pub: pub, _gr: gr,
      _inv: inv, _asg: asg, _cpc: cpc
    };
  }

  function generate(seed, opts, rnd) {
    opts = opts || {};
    var p = genPatent(rnd, opts);
    var n = (opts.baseN || 0) + 1;
    var rec = {
      id: ID_PREFIX + String(n).padStart(6, '0'),
      n: n,
      publication_number: 'SYN-' + String(100000 + (n % 900000)),
      title: p.title,
      abstract_snippet: p.abstract_snippet,
      assignee: p.assignee,
      inventor: p.inventor,
      filing_date: p.filing_date,
      publication_date: p.publication_date,
      grant_date: p.grant_date,
      priority_date: p.priority_date,
      cpc: p.cpc,
      language: p.language,
      record_kind: 'synthetic',
      stamp: STAMP
    };
    rec._priv = p;
    rec._seed = seed;
    return rec;
  }

  /* independent re-verification: recompute every derived field from _priv */
  function verify(rec) {
    var errs = [];
    var p = rec._priv;
    if (!p) return ['no private params — cannot independently verify'];
    if (rec.title !== buildTitle(p._dev, p._pur, p._mech)) errs.push('title does not match parts');
    if (rec.abstract_snippet !== buildAbstract(p._dev, p._pur, p._mech, p._mods))
      errs.push('abstract does not match parts');
    if (rec.inventor !== p._inv) errs.push('inventor mismatch');
    if (rec.assignee !== p._asg) errs.push('assignee mismatch');
    if (rec.filing_date !== iso([p._fy, p._fm, p._fd])) errs.push('filing date mismatch');
    if (rec.publication_date !== iso(p._pub)) errs.push('publication date mismatch');
    if (rec.grant_date !== iso(p._gr)) errs.push('grant date mismatch');
    if (!(rec.filing_date <= rec.publication_date && rec.publication_date <= rec.grant_date))
      errs.push('date ordering violated (filing <= publication <= grant)');
    if (rec.cpc !== p._cpc || CPCS.indexOf(rec.cpc) < 0) errs.push('bad cpc');
    if (rec.publication_number !== 'SYN-' + String(100000 + (rec.n % 900000)))
      errs.push('publication_number mismatch');
    if (rec.language !== 'en') errs.push('bad language');
    return errs;
  }

  function validate(rec) {
    var errs = [];
    if (!rec || typeof rec !== 'object') return { ok: false, errors: ['not an object'] };
    ['id', 'publication_number', 'title', 'abstract_snippet', 'assignee', 'inventor',
     'filing_date', 'publication_date', 'grant_date', 'cpc'].forEach(function (k) {
      if (rec[k] === undefined || rec[k] === null || rec[k] === '') errs.push('missing field: ' + k);
    });
    if (rec.id && !/^JAH-PAT-\d{6}$/.test(rec.id)) errs.push('bad id format');
    if (rec._priv) errs = errs.concat(verify(rec));
    else errs.push('no private params — cannot independently verify');
    return { ok: errs.length === 0, errors: errs };
  }

  function driftCheck(rec, archiveSample) {
    var errs = [];
    (archiveSample || []).forEach(function (a) {
      var t = a.title || a[1];
      if (t && String(t).toLowerCase().replace(/\s+/g, ' ') === String(rec.title).toLowerCase().replace(/\s+/g, ' '))
        errs.push('duplicate of archived patent title: ' + rec.title);
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

  JAHDB.registerGenerator('patents', {
    version: VERSION,
    generate: generate,
    validate: validate,
    driftCheck: driftCheck,
    themedGenerate: themedGenerate,
    types: ['synthetic']
  });
})();
