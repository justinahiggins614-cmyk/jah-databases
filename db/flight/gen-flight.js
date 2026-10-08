/* ✳ SIGNATURE — JAH Flight Data Base generator. Property of Justin Addam Higgins (JAH).
   Boundless generator: produces NEW flight-lesson records in the archive's exact
   format (id, name, letter, region, distance_km, skill, craft, highlights,
   waypoints, lesson_plan). Waypoints are built first; distance_km is computed
   from the waypoint chain, so every field is genuine. Deterministic:
   same seed + version => same record. An independent verifier recomputes every
   claim from the private params before acceptance. */
(function () {
  'use strict';
  var VERSION = 'jahdb-flight-1.0';
  var ID_PREFIX = 'JAH-FLIGHT-';
  var ID_DIGITS = 6;
  var DIST_SCALE = 2000; /* simulated km per 1000 waypoint units */

  var REGIONS = ['Jungle Region', 'Prairie Region', 'Mountain Region', 'Arctic Region',
    'Volcano Region', 'Desert Region', 'Canyon Region', 'Lakeside Region',
    'Coastal Region', 'Island Region'];
  var SKILLS = ['Student', 'Intermediate', 'Advanced', 'Ace'];
  var CRAFTS = ['t1', 'c2', 'g1', 'h4', 'r3', 'c9', 'a6', 'j7', 'g800', 's5', 'n2', 'x1'];
  var FIRST = ['Al', 'Be', 'Cor', 'Del', 'El', 'Fi', 'Gar', 'Hal', 'Il', 'Jor', 'Kal',
    'Lan', 'Mar', 'Nor', 'Or', 'Pal', 'Quil', 'Ros', 'Sal', 'Tar', 'Ul', 'Val',
    'Wil', 'Xan', 'Yor', 'Zal'];
  var WORDS = ['Hop', 'Tour', 'Canyon', 'Carve', 'Sunrise', 'Run', 'Summit', 'Loop',
    'River', 'Follow', 'Storm', 'Edge', 'Ride', 'Island', 'Thunderhead', 'Valley',
    'Harbor', 'Night', 'Lights', 'Glacier', 'Meadow', 'Ridge', 'Bay', 'Peak'];
  var HIGHLIGHTS = [
    'Weaves between mountain peaks — thrilling!',
    'A real pilot\'s workout: wind, hills, and tight turns.',
    'Tests your turns with a winding river below.',
    'Golden light over the water the whole way.',
    'Gentle route, perfect for a first cross-country.',
    'City lights sparkle under the wings at night.'
  ];
  var LESSONS = {
    'Student': 'Student lesson: takeoff briefing, pattern work over {region}, three touch-and-goes, then a full-stop landing debrief.',
    'Intermediate': 'Intermediate lesson: cross-country navigation across {region}, one diversion drill, short-field landing practice.',
    'Advanced': 'Advanced lesson: high-performance maneuvers over {region}, emergency-procedure drills, precision approaches.',
    'Ace': 'Ace sortie: low-level navigation through {region}, formation rejoins, night operations.'
  };

  function pickI(rnd, n) { return Math.floor(rnd() * n); }
  function pick(rnd, arr) { return arr[pickI(rnd, arr.length)]; }
  function chainDist(wp) {
    var d = 0;
    for (var i = 0; i + 1 < wp.length; i++) {
      var dx = wp[i + 1][0] - wp[i][0], dy = wp[i + 1][1] - wp[i][1], dz = wp[i + 1][2] - wp[i][2];
      d += Math.sqrt(dx * dx + dy * dy + dz * dz);
    }
    return d;
  }
  function distKm(wp) { return Math.round((chainDist(wp) / DIST_SCALE) * 10) / 10; }
  function lessonFor(skill, region) { return LESSONS[skill].replace('{region}', region); }

  function generate(seed, opts, rnd) {
    opts = opts || {};
    var region = pick(rnd, REGIONS), skill = pick(rnd, SKILLS), craft = pick(rnd, CRAFTS);
    if (opts.type && SKILLS.indexOf(opts.type) >= 0) skill = opts.type;
    var hi = pick(rnd, HIGHLIGHTS);
    var name = pick(rnd, FIRST) + ' ' + pick(rnd, WORDS) + ' ' + pick(rnd, WORDS);
    var letter = name.charAt(0).toUpperCase();
    var nw = 4 + pickI(rnd, 4); /* 4..7 waypoints */
    var wp = [], x = 0, y = 0, z = 1500;
    for (var i = 0; i < nw; i++) {
      x += 800 + pickI(rnd, 2200); y += -1500 + pickI(rnd, 3001); z += -800 + pickI(rnd, 1601);
      if (z < 500) z = 500; if (z > 4000) z = 4000;
      wp.push([x, y, z]);
    }
    var n = (opts.baseN || 0) + 1;
    var pub = {
      id: ID_PREFIX + String(n).padStart(ID_DIGITS, '0'),
      n: n,
      name: name,
      letter: letter,
      region: region,
      distance_km: distKm(wp),
      skill: skill,
      craft: craft,
      highlights: hi,
      waypoints: wp,
      lesson_plan: lessonFor(skill, region),
      origin: 'generated',
      stamp: 'JAH Flight Data Base — generated flight-lesson record.'
    };
    pub._priv = { region: region, skill: skill, craft: craft, hi: hi, name: name, wp: wp, seed: seed };
    return pub;
  }

  function validate(rec) {
    var errs = [];
    if (!rec || typeof rec !== 'object') return { ok: false, errors: ['not an object'] };
    ['id', 'name', 'letter', 'region', 'distance_km', 'skill', 'craft', 'highlights', 'waypoints', 'lesson_plan'].forEach(function (k) {
      if (rec[k] === undefined || rec[k] === null || rec[k] === '') errs.push('missing field: ' + k);
    });
    if (rec.id && !/^JAH-FLIGHT-\d{6}$/.test(rec.id)) errs.push('bad id format');
    if (rec.region && REGIONS.indexOf(rec.region) < 0) errs.push('unknown region');
    if (rec.skill && SKILLS.indexOf(rec.skill) < 0) errs.push('unknown skill');
    if (rec.craft && CRAFTS.indexOf(rec.craft) < 0) errs.push('unknown craft');
    if (rec.highlights && HIGHLIGHTS.indexOf(rec.highlights) < 0) errs.push('unknown highlights text');
    if (rec.letter && rec.name && rec.letter !== rec.name.charAt(0).toUpperCase()) errs.push('letter does not match name');
    if (rec.name) {
      var w = rec.name.split(' ');
      if (w.length !== 3 || FIRST.indexOf(w[0]) < 0 || WORDS.indexOf(w[1]) < 0 || WORDS.indexOf(w[2]) < 0)
        errs.push('name not built from known word pools');
    }
    if (rec._priv) {
      var p = rec._priv;
      if (!Array.isArray(p.wp) || p.wp.length < 4 || p.wp.length > 7) errs.push('bad private waypoint count');
      else {
        var want = distKm(p.wp);
        if (Math.abs(want - rec.distance_km) > 0.051) errs.push('distance_km does not recompute from waypoints (want ' + want + ')');
        if (JSON.stringify(rec.waypoints) !== JSON.stringify(p.wp)) errs.push('waypoints do not match private params');
      }
      if (p.skill !== rec.skill || p.region !== rec.region) errs.push('private region/skill mismatch');
      if (rec.lesson_plan !== lessonFor(p.skill, p.region)) errs.push('lesson_plan does not recompute from skill+region');
      if (p.name !== rec.name) errs.push('private name mismatch');
    } else errs.push('no private params — cannot independently verify');
    return { ok: errs.length === 0, errors: errs };
  }

  /* drift check: no generated lesson may reuse a stored lesson name */
  function driftCheck(rec, archiveSample) {
    var errs = [];
    (archiveSample || []).forEach(function (a) {
      var nm = a.name;
      if (nm && String(nm) === String(rec.name)) errs.push('lesson name duplicates a stored record');
    });
    return { ok: errs.length === 0, errors: errs };
  }

  /* cross-database: borrow a theme number from another database's sample */
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

  JAHDB.registerGenerator('flight', {
    version: VERSION,
    generate: generate,
    validate: validate,
    driftCheck: driftCheck,
    themedGenerate: themedGenerate,
    types: SKILLS.slice()
  });
})();
