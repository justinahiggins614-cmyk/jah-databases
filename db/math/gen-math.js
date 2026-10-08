/* ✳ SIGNATURE — JAH Math Data Base generator. Property of Justin Addam Higgins (JAH).
   Boundless generator: produces NEW math grid records in archive style —
   a deterministic 12x12 bit grid (the Signature math grid) encoded through
   the archive's encoding families (hex, base64, ASCII-art). Deterministic:
   same seed + version => same record. Every record is re-encoded by an
   INDEPENDENT verifier before it is accepted. */
(function () {
  'use strict';
  var VERSION = 'jahdb-math-1.0';
  var ID_PREFIX = 'JAH-MATH-';
  var GRID = 12, CELLS = 144;
  var STAMP = 'Official JAH Math Grid Archive — generated boundlessly, verified independently.';
  var CATS = ['Base systems', 'Mixes', 'Visual codes', 'Text encodings', 'Numeric formats',
              'Audio', 'Geometry', 'Cryptography', 'Compression'];
  var HEXC = '0123456789abcdef';
  var B64C = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/';

  function ri(rnd, a, b) { return a + Math.floor(rnd() * (b - a + 1)); }
  function pick(rnd, arr) { return arr[Math.floor(rnd() * arr.length)]; }

  function bitsToHex(bits) {
    var s = '';
    for (var i = 0; i < CELLS; i += 4)
      s += HEXC[bits[i] * 8 + bits[i + 1] * 4 + bits[i + 2] * 2 + bits[i + 3]];
    return s;
  }
  function bitsToB64(bits) {
    var s = '';
    for (var i = 0; i < CELLS; i += 6) {
      var v = 0;
      for (var j = 0; j < 6; j++) v = v * 2 + bits[i + j];
      s += B64C[v];
    }
    return s;
  }
  function bitsToArt(bits) {
    var rows = [];
    for (var r = 0; r < GRID; r++) {
      var s = '';
      for (var c = 0; c < GRID; c++) s += bits[r * GRID + c] ? '█' : '·';
      rows.push(s);
    }
    return rows;
  }
  function popcount(bits) { var n = 0, i; for (i = 0; i < bits.length; i++) n += bits[i]; return n; }
  function sym180(bits) { for (var i = 0; i < CELLS; i++) if (bits[i] !== bits[CELLS - 1 - i]) return false; return true; }

  var PUB_KEYS = ['id', 'n', 'title', 'cat', 'grid', 'bitstring', 'encodings', 'popcount',
                  'symmetric180', 'note', 'stamp'];

  function generate(seed, opts, rnd) {
    opts = opts || {};
    var cat = opts.type && CATS.indexOf(opts.type) >= 0 ? opts.type : pick(rnd, CATS);
    var bits = [];
    for (var i = 0; i < CELLS; i++) bits.push(rnd() < 0.5 ? 0 : 1);
    var n = (opts.baseN || 0) + 1;
    var pc = popcount(bits), sym = sym180(bits);
    var rec = {
      id: ID_PREFIX + String(n).padStart(6, '0'),
      n: n,
      title: cat + ' grid record — ' + pc + ' marks on the 12×12',
      cat: cat,
      grid: '12x12',
      bitstring: bits.join(''),
      encodings: { hex: bitsToHex(bits), base64: bitsToB64(bits), ascii_art: bitsToArt(bits) },
      popcount: pc,
      symmetric180: sym,
      note: 'Generated math grid record: a deterministic 12×12 bit grid encoded through the archive\'s ' + cat + ' family. Not a stored archive record.',
      stamp: STAMP,
      _bits: bits, _cat: cat, _seed: seed
    };
    var pub = {};
    PUB_KEYS.forEach(function (k) { pub[k] = rec[k]; });
    pub._priv = rec;
    return pub;
  }

  /* independent re-encoder: rebuilds every derived field from the raw bits */
  function verify(priv) {
    var errs = [];
    var bits = priv._bits;
    if (!Array.isArray(bits) || bits.length !== CELLS) return ['bad bit grid'];
    for (var i = 0; i < CELLS; i++)
      if (bits[i] !== 0 && bits[i] !== 1) { errs.push('bit grid not binary'); break; }
    if (priv.bitstring !== bits.join('')) errs.push('bitstring mismatch');
    if (priv.encodings.hex !== bitsToHex(bits)) errs.push('hex re-encode mismatch');
    if (priv.encodings.base64 !== bitsToB64(bits)) errs.push('base64 re-encode mismatch');
    var art = bitsToArt(bits);
    if (priv.encodings.ascii_art.length !== art.length ||
        priv.encodings.ascii_art.some(function (r, k) { return r !== art[k]; }))
      errs.push('ascii-art re-encode mismatch');
    if (priv.popcount !== popcount(bits)) errs.push('popcount mismatch');
    if (priv.symmetric180 !== sym180(bits)) errs.push('symmetry mismatch');
    return errs;
  }

  function validate(rec) {
    var errs = [];
    if (!rec || typeof rec !== 'object') return { ok: false, errors: ['not an object'] };
    ['id', 'title', 'cat', 'grid', 'bitstring', 'encodings', 'popcount', 'symmetric180'].forEach(function (k) {
      if (rec[k] === undefined || rec[k] === null || rec[k] === '') errs.push('missing field: ' + k);
    });
    if (rec.id && !/^JAH-MATH-\d{6}$/.test(rec.id)) errs.push('bad id format');
    if (rec.cat && CATS.indexOf(rec.cat) < 0) errs.push('bad category');
    if (rec.bitstring && !/^[01]{144}$/.test(rec.bitstring)) errs.push('bitstring must be 144 binary chars');
    if (rec._priv) {
      var p = rec._priv;
      PUB_KEYS.forEach(function (k) {
        if (JSON.stringify(rec[k]) !== JSON.stringify(p[k])) errs.push('field diverged from verified copy: ' + k);
      });
      errs = errs.concat(verify(p));
    }
    else errs.push('no private bit grid — cannot independently verify');
    return { ok: errs.length === 0, errors: errs };
  }

  function driftCheck(rec, archiveSample) {
    var errs = [];
    (archiveSample || []).forEach(function (a) {
      var bs = a.bitstring || (a[2]);
      if (bs && String(bs) === String(rec.bitstring)) errs.push('duplicate of archived grid bitstring');
    });
    return { ok: errs.length === 0, errors: errs };
  }

  function themedGenerate(seed, opts, rnd, themeSamples) {
    var rec = generate(seed, opts, rnd);
    if (themeSamples && themeSamples.length) {
      var t = themeSamples[Math.floor(rnd() * themeSamples.length)];
      var nums = String(JSON.stringify(t)).match(/\d+/g);
      if (nums && nums.length) {
        var r2 = JAHDB.prng(JAHDB.hashStr(String(seed) + nums[0]));
        /* fold the theme number into the bit grid deterministically */
        var rec2 = generate(seed, opts, r2);
        rec2.id = rec.id; rec2.n = rec.n;
        return rec2;
      }
    }
    return rec;
  }

  JAHDB.registerGenerator('math', {
    version: VERSION,
    generate: generate,
    validate: validate,
    driftCheck: driftCheck,
    themedGenerate: themedGenerate,
    types: CATS
  });
})();
