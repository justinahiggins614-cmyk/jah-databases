/* ✳ SIGNATURE — JAH Space Map Data Base generator. Property of Justin Addam Higgins (JAH).
   Boundless generator: produces NEW space maps in the exact archive format
   (id, name, kind, blurb, rooms[{x,y,w,h,label}], doors[{x,y}]). Deterministic:
   same seed + version => same record. Maps are built constructively as a
   left-to-right room tiling; an INDEPENDENT verifier re-checks the tiling,
   door placement, and blurb consistency before acceptance. */
(function () {
  'use strict';
  var VERSION = 'jahdb-space-1.0';
  var ID_PREFIX = 'JAH-SPACE-';

  function ri(rnd, a, b) { return a + Math.floor(rnd() * (b - a + 1)); }
  function pick(rnd, arr) { return arr[Math.floor(rnd() * arr.length)]; }
  function f2(v) { return Math.round(v * 100) / 100; }

  /* real archive layout patterns: name pattern + room labels */
  var LAYOUTS = [
    { pat: 'One-Bedroom', rooms: ['living', 'bedroom', 'kitchen', 'bath'] },
    { pat: 'Two-Bedroom', rooms: ['living', 'bedroom A', 'bedroom B', 'kitchen', 'bath'] },
    { pat: 'Studio Flat', rooms: ['living', 'kitchen nook', 'bath'] },
    { pat: 'Loft', rooms: ['loft', 'studio', 'bath'] },
    { pat: 'Cabin', rooms: ['great room', 'bunk', 'porch'] },
    { pat: 'Kitchen Diner', rooms: ['kitchen', 'dining', 'pantry'] },
    { pat: 'Home Office', rooms: ['office', 'hall', 'bath'] },
    { pat: 'Garage Workshop', rooms: ['garage', 'workshop', 'storage'] }
  ];
  var PLACE = ['West', 'Oak', 'Elm', 'North', 'Maple', 'River', 'Cedar', 'Hill', 'Park', 'Lake', 'Stone', 'Birch'];

  function generate(seed, opts, rnd) {
    opts = opts || {};
    var layouts = LAYOUTS.map(function (l) { return l.pat; });
    var pat = opts.layout && layouts.indexOf(opts.layout) >= 0 ? opts.layout : pick(rnd, layouts);
    var layout = LAYOUTS[layouts.indexOf(pat)];

    /* build the tiling left to right from x=0, like the archive */
    var x = 0, rooms = [];
    layout.rooms.forEach(function (label) {
      var w = f2(8 + rnd() * 6), h = f2(8 + rnd() * 6);
      rooms.push({ x: f2(x), y: 0.0, w: w, h: h, label: label });
      x = f2(x + w);
    });
    var totalW = x;
    /* doors sit on room boundaries, at a height inside the room */
    var doors = [];
    for (var i = 1; i < rooms.length; i++) {
      var bx = rooms[i].x;
      var hh = Math.min(rooms[i - 1].h, rooms[i].h);
      doors.push({ x: f2(bx), y: f2(2 + rnd() * Math.max(1, hh - 4)) });
    }

    var n = (opts.baseN || 0) + 1;
    var name = pick(rnd, PLACE) + ' ' + pat + ' ' + n;
    var blurb = pat.toLowerCase() + ' generated layout: ' + layout.rooms.join(', ') + '.';
    var rec = {
      id: ID_PREFIX + String(n).padStart(6, '0'),
      n: n,
      name: name,
      kind: 'generated',
      blurb: blurb,
      rooms: rooms,
      doors: doors
    };
    var pub = {};
    ['id', 'n', 'name', 'kind', 'blurb', 'rooms', 'doors'].forEach(function (k) { pub[k] = rec[k]; });
    pub._priv = { rooms: rooms, doors: doors, labels: layout.rooms, pat: pat, totalW: totalW };
    return pub;
  }

  /* independent re-verification: re-check tiling, doors, blurb from scratch */
  function verify(rec) {
    var errs = [];
    var p = rec._priv, rooms = p.rooms;
    if (!Array.isArray(rooms) || rooms.length < 2) { errs.push('need 2+ rooms'); return errs; }
    if (rooms[0].x !== 0 || rooms[0].y !== 0) errs.push('tiling must start at x=0,y=0');
    for (var i = 0; i < rooms.length; i++) {
      var r = rooms[i];
      if (!(r.w > 0 && r.h > 0)) errs.push('room ' + i + ' has non-positive size');
      if (r.label !== p.labels[i]) errs.push('room label mismatch at ' + i);
      if (i > 0) {
        var prev = rooms[i - 1];
        if (Math.abs(r.x - (prev.x + prev.w)) > 0.011) errs.push('tiling gap/overlap at room ' + i);
        if (r.y !== 0) errs.push('room y must be 0');
      }
    }
    var bounds = {};
    rooms.forEach(function (r) { bounds[r.x] = 1; });
    bounds[f2(rooms[rooms.length - 1].x + rooms[rooms.length - 1].w)] = 1;
    p.doors.forEach(function (d, i) {
      if (!bounds[d.x]) errs.push('door ' + i + ' x=' + d.x + ' is not on a room boundary');
      if (!(d.y > 0 && d.y < 14)) errs.push('door ' + i + ' y out of range');
    });
    if (p.doors.length !== rooms.length - 1) errs.push('door count must be rooms-1');
    p.labels.forEach(function (lab) {
      if (rec.blurb.toLowerCase().indexOf(lab.toLowerCase()) < 0)
        errs.push('blurb omits room label: ' + lab);
    });
    return errs;
  }

  function validate(rec) {
    var errs = [];
    if (!rec || typeof rec !== 'object') return { ok: false, errors: ['not an object'] };
    ['id', 'name', 'kind', 'blurb', 'rooms', 'doors'].forEach(function (k) {
      if (rec[k] === undefined || rec[k] === null || rec[k] === '') errs.push('missing field: ' + k);
    });
    if (rec.id && !/^JAH-SPACE-\d{6}$/.test(rec.id)) errs.push('bad id format');
    if (rec.kind && ['sample', 'generated'].indexOf(rec.kind) < 0) errs.push('bad kind');
    if (!Array.isArray(rec.rooms) || !Array.isArray(rec.doors)) errs.push('rooms/doors must be arrays');
    if (rec._priv) errs = errs.concat(verify(rec));
    else errs.push('no private params — cannot independently verify');
    return { ok: errs.length === 0, errors: errs };
  }

  function driftCheck(rec, archiveSample) {
    var errs = [];
    (archiveSample || []).forEach(function (a) {
      if (a.name && String(a.name).toLowerCase() === String(rec.name).toLowerCase())
        errs.push('duplicate of archived map name: ' + rec.name);
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

  JAHDB.registerGenerator('space', {
    version: VERSION,
    generate: generate,
    validate: validate,
    driftCheck: driftCheck,
    themedGenerate: themedGenerate,
    layouts: LAYOUTS.map(function (l) { return l.pat; })
  });
})();
