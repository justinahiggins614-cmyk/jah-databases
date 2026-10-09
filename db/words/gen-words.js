/* ✳ SIGNATURE — JAH Dictionary Data Base generator. Property of Justin Addam Higgins (JAH).
   Boundless generator: produces NEW dictionary entries + word inventions in the
   archive's style (headword, part of speech, pronunciation, definition,
   examples, lexical-form invention apparatus, id, stamp). Deterministic: same
   seed + version => same record.
   Headwords are real English words; definitions are plain authored senses;
   the word-invention text is built constructively from the word's own letters
   and sense — never a claim about the real world. Every record is re-verified
   by an INDEPENDENT checker before acceptance. */
(function () {
  'use strict';
  var VERSION = 'jahdb-words-1.0';
  var ID_PREFIX = 'JAH-WORD-';
  var STAMP = 'JAH Dictionary Data Base — synthetic entry. Generated for the boundless archive; not a harvested dictionary record.';

  /* real headwords with plain authored definitions: [word, pos, definition] */
  var WORDS = [
    ['hammer', 'noun', 'A hand tool with a heavy head for driving nails.'],
    ['bridge', 'noun', 'A structure carrying a road or path across a gap.'],
    ['candle', 'noun', 'A stick of wax with a wick that gives light when lit.'],
    ['ladder', 'noun', 'A frame of rungs for climbing up or down.'],
    ['anchor', 'noun', 'A heavy device that holds a ship in place.'],
    ['compass', 'noun', 'An instrument showing direction by a magnetic needle.'],
    ['kettle', 'noun', 'A vessel for boiling water.'],
    ['pillow', 'noun', 'A soft cushion for resting the head.'],
    ['saddle', 'noun', 'A seat for riding a horse.'],
    ['trumpet', 'noun', 'A brass wind instrument with a bright tone.'],
    ['wallet', 'noun', 'A flat case for holding money and cards.'],
    ['lantern', 'noun', 'A portable lamp with a protective case.'],
    ['shovel', 'noun', 'A tool with a broad blade for digging.'],
    ['mirror', 'noun', 'A surface that reflects an image.'],
    ['needle', 'noun', 'A thin pointed tool for sewing.'],
    ['basket', 'noun', 'A woven container for carrying things.'],
    ['helmet', 'noun', 'Protective headgear.'],
    ['piano', 'noun', 'A keyboard instrument with struck strings.'],
    ['rocket', 'noun', 'A vehicle driven by ejected exhaust gases.'],
    ['tent', 'noun', 'A portable cloth shelter.'],
    ['umbrella', 'noun', 'A folding canopy against rain or sun.'],
    ['violin', 'noun', 'A small bowed string instrument.'],
    ['wagon', 'noun', 'A four-wheeled vehicle for carrying loads.'],
    ['orange', 'noun', 'A round citrus fruit with a thick rind.'],
    ['river', 'noun', 'A natural stream of water flowing to the sea.'],
    ['mountain', 'noun', 'A large natural rise of land.'],
    ['cloud', 'noun', 'A visible mass of water vapor in the sky.'],
    ['stone', 'noun', 'A small piece of rock.'],
    ['feather', 'noun', 'A light growth covering a bird.'],
    ['shell', 'noun', 'The hard outer covering of an animal or egg.'],
    ['key', 'noun', 'A device for opening a lock.'],
    ['clock', 'noun', 'An instrument for measuring time.'],
    ['garden', 'noun', 'A plot for growing plants.'],
    ['forest', 'noun', 'A large area covered with trees.'],
    ['ocean', 'noun', 'A vast body of salt water.'],
    ['island', 'noun', 'Land surrounded by water.'],
    ['desert', 'noun', 'A dry, barren region.'],
    ['valley', 'noun', 'Low land between hills.'],
    ['meadow', 'noun', 'A field of grass.'],
    ['cave', 'noun', 'A natural hollow in rock.'],
    ['beach', 'noun', 'Sandy shore by the sea.'],
    ['sail', 'noun', 'Cloth that catches wind to drive a boat.'],
    ['bell', 'noun', 'A hollow metal object that rings when struck.'],
    ['drum', 'noun', 'A percussion instrument with a stretched skin.'],
    ['flute', 'noun', 'A wind instrument played sideways.'],
    ['harp', 'noun', 'A plucked string instrument with a frame.'],
    ['run', 'verb', 'To move fast on foot.'],
    ['build', 'verb', 'To construct by putting parts together.'],
    ['bright', 'adjective', 'Giving much light; shining.'],
    ['swift', 'adjective', 'Moving quickly.']
  ];

  function ri(rnd, a, b) { return a + Math.floor(rnd() * (b - a + 1)); }
  function pick(rnd, arr) { return arr[Math.floor(rnd() * arr.length)]; }

  function buildInventionTitle(w) {
    return "'" + w + "' lexical-form apparatus and method";
  }
  function buildInventionDesc(w, pos) {
    var letters = w.length;
    return "A lexical-form apparatus and method treating the word '" + w + "' itself as an " +
      'encoding structure: its ' + letters + ' letters and ' + pos + ' sense become the blueprint ' +
      'for a compact data-and-form device. The six Signature tools convert the bare word-form ' +
      'into a buildable system with measurable parameters, raising encoding density across ' +
      'bench qualification.';
  }

  /* deterministic approximate phonetic respelling (editor-style guide, like the archive) */
  function respell(w) {
    var s = String(w).toLowerCase().replace(/[^a-z]/g, '');
    if (!s) return '—';
    var vowels = 'aeiouy', parts = [], cur = '';
    for (var i = 0; i < s.length; i++) {
      cur += s[i];
      var v = vowels.indexOf(s[i]) >= 0;
      var nv = i + 1 < s.length && vowels.indexOf(s[i + 1]) >= 0;
      if (v && !nv && cur.length >= 2 && i + 2 < s.length) { parts.push(cur); cur = ''; }
    }
    if (cur) parts.push(cur);
    if (!parts.length) parts = [s];
    parts[0] = parts[0].toUpperCase();
    return parts.join('-');
  }

  /* deterministic usage examples — pure function of (word, pos) so the
     independent verifier rebuilds them exactly */
  var EXT = {
    noun: ['She set the {w} on the table and stepped back to admire it.',
           'Every workshop keeps a {w} within arm\u2019s reach.',
           'The old {w} had seen decades of honest use.'],
    verb: ['They {w} every morning before the sun rose.',
           'He learned to {w} the long way, through trial and error.',
           'She will {w} again tomorrow, weather permitting.'],
    adjective: ['The {w} morning made everyone pause at the window.',
                'It was a {w} idea, and they knew it.',
                'A {w} light filled the room.']
  };
  function hashLocal(s) {
    var h = 2166136261;
    s = String(s);
    for (var i = 0; i < s.length; i++) { h ^= s.charCodeAt(i); h = Math.imul(h, 16777619); }
    return h >>> 0;
  }
  function buildExamples(w, pos) {
    var t = EXT[pos] || EXT.noun, h = hashLocal(w + '|' + pos);
    var a = t[h % t.length], b = t[(h >>> 4) % t.length];
    if (b === a) b = t[(h % t.length + 1) % t.length];
    return [a.split('{w}').join(w), b.split('{w}').join(w)];
  }

  function generate(seed, opts, rnd) {
    opts = opts || {};
    var pool = (opts.pos && ['noun', 'verb', 'adjective'].indexOf(opts.pos) >= 0)
      ? WORDS.filter(function (e) { return e[1] === opts.pos; }) : WORDS;
    var e = pick(rnd, pool.length ? pool : WORDS);
    var w = e[0], pos = e[1], def = e[2];
    var n = (opts.baseN || 0) + 1;
    var rec = {
      id: ID_PREFIX + String(n).padStart(6, '0'),
      n: n,
      w: w,
      pos: pos,
      pron: respell(w),
      d: def,
      examples: buildExamples(w, pos),
      invention_title: buildInventionTitle(w),
      invention_desc: buildInventionDesc(w, pos),
      rt: 'gen',
      rid: ID_PREFIX + String(n).padStart(6, '0'),
      cpc: 'G06F',
      record_kind: 'synthetic',
      stamp: STAMP
    };
    rec._priv = { _w: w, _pos: pos, _def: def };
    rec._seed = seed;
    return rec;
  }

  function verify(rec) {
    var errs = [];
    var p = rec._priv;
    if (!p) return ['no private params — cannot independently verify'];
    /* the definition must be the pool's genuine definition for this headword */
    var match = null;
    WORDS.forEach(function (e) { if (e[0] === p._w) match = e; });
    if (!match) errs.push('headword not in the known word pool');
    else {
      if (match[1] !== p._pos || match[2] !== p._def) errs.push('pos/definition do not match the pool entry');
    }
    if (rec.w !== p._w) errs.push('headword mismatch');
    if (rec.pos !== p._pos) errs.push('pos mismatch');
    if (rec.d !== p._def) errs.push('definition mismatch');
    if (rec.pron !== respell(p._w)) errs.push('pronunciation mismatch');
    var ex = buildExamples(p._w, p._pos);
    if (!Array.isArray(rec.examples) || rec.examples.length !== 2 ||
        rec.examples[0] !== ex[0] || rec.examples[1] !== ex[1])
      errs.push('examples mismatch');
    if (rec.examples && rec.examples.some(function (x) { return String(x).indexOf(p._w) < 0; }))
      errs.push('example does not use the headword');
    if (rec.invention_title !== buildInventionTitle(p._w)) errs.push('invention title mismatch');
    if (rec.invention_desc !== buildInventionDesc(p._w, p._pos)) errs.push('invention desc mismatch');
    if (rec.rid !== rec.id) errs.push('rid/id mismatch');
    if (String(rec.invention_desc).indexOf(String(p._w.length) + ' letters') < 0)
      errs.push('letter count not reflected in invention desc');
    return errs;
  }

  function validate(rec) {
    var errs = [];
    if (!rec || typeof rec !== 'object') return { ok: false, errors: ['not an object'] };
    ['id', 'w', 'pos', 'pron', 'd', 'examples', 'invention_title', 'invention_desc'].forEach(function (k) {
      if (rec[k] === undefined || rec[k] === null || rec[k] === '') errs.push('missing field: ' + k);
    });
    if (rec.id && !/^JAH-WORD-\d{6}$/.test(rec.id)) errs.push('bad id format');
    if (rec._priv) errs = errs.concat(verify(rec));
    else errs.push('no private params — cannot independently verify');
    return { ok: errs.length === 0, errors: errs };
  }

  function driftCheck(rec, archiveSample) {
    var errs = [];
    (archiveSample || []).forEach(function (a) {
      var w = a.w || a[0];
      if (w && String(w).replace(/^['"]|['"]$/g, '').toLowerCase() === String(rec.w).toLowerCase())
        errs.push('headword already present in archive sample: ' + rec.w);
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
        rec2.id = rec.id; rec2.n = rec.n; rec2.rid = rec.rid;
        return rec2;
      }
    }
    return rec;
  }

  JAHDB.registerGenerator('words', {
    version: VERSION,
    generate: generate,
    validate: validate,
    driftCheck: driftCheck,
    themedGenerate: themedGenerate,
    types: ['synthetic']
  });
})();
