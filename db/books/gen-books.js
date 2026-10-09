/* ✳ SIGNATURE — JAH Book Data Base generator. Property of Justin Addam Higgins (JAH).
   Boundless generator: produces NEW finished-book records in the archive's
   exact schema (id, title, author, genre, gkey, desc, words, chapters,
   note, sources, origin). All prose is assembled combinatorially from clean
   word pools — no real-world claims, all names/places invented — and the
   word count is genuinely computed from the generated chapters. Honestly
   marked GENERATED. Deterministic: same seed + version => same record.
   An INDEPENDENT verifier rebuilds every field from the private pool
   indices before acceptance. */
(function () {
  'use strict';
  var VERSION = 'jahdb-books-1.0';
  var ID_PREFIX = 'JAH-BOOK-';
  var AUTHOR = 'Justin Addam Higgins';
  var STAMP = 'Official JAH Book Archive — generated boundlessly, verified independently.';
  /* real archive genres -> gkey (matches the archive's own volume chunks) */
  var GENRES = ['Science Fiction', 'Fantasy', 'Mystery', 'Romance', 'Horror', 'Mathematics',
                'Physics', 'Chemistry', 'Biology', 'History', 'Computer Science', "Children's",
                'Poetry', 'Technical Manual', 'Philosophy', 'Business'];
  var GKEY = { 'Science Fiction': 'sf', 'Fantasy': 'fantasy', 'Mystery': 'mystery', 'Romance': 'romance',
    'Horror': 'horror', 'Mathematics': 'math', 'Physics': 'physics', 'Chemistry': 'chemistry',
    'Biology': 'biology', 'History': 'history', 'Computer Science': 'cs', "Children's": 'children',
    'Poetry': 'poetry', 'Technical Manual': 'manual', 'Philosophy': 'philosophy', 'Business': 'business' };
  var GNOUN = { 'Science Fiction': 'courage', 'Fantasy': 'loyalty', 'Mystery': 'curiosity',
    'Romance': 'devotion', 'Horror': 'dread', 'Mathematics': 'precision', 'Physics': 'wonder',
    'Chemistry': 'discovery', 'Biology': 'life', 'History': 'memory', 'Computer Science': 'logic',
    "Children's": 'joy', 'Poetry': 'longing', 'Technical Manual': 'clarity',
    'Philosophy': 'reflection', 'Business': 'ambition' };

  var TA = ['Echoes', 'Whispers', 'Shadows', 'Songs', 'Tales', 'Dreams', 'Secrets', 'Legends',
            'Embers', 'Tides', 'Lanterns', 'Storms', 'Veils', 'Comets', 'Riddles', 'Harbors'];
  var TB = ['Nebula', 'Deep', 'Hollow', 'Ember', 'Tide', 'Storm', 'Vale', 'Machine',
            'Garden', 'Tower', 'River', 'Crown', 'Forge', 'Harbor', 'Star', 'Thicket'];
  var TC = ['Spell', 'Affair', 'Crossing', 'Ledger', 'Voyage', 'Cipher', 'Oath', 'Signal'];
  var SYL = ['hal', 'cor', 'wen', 'kam', 'fen', 'dor', 'lus', 'mar', 'sel', 'tor',
             'vel', 'ris', 'nor', 'bel', 'ash', 'elm', 'ira', 'oth'];
  var PLACE = ['Kepler Belt', 'Elderwood', 'Lantern Row', 'Stonebridge', 'Meridian City',
               'Aldermere', 'Frostgate', 'Juniper Quay', 'Emberline', 'Tarnwick'];
  var THING = ['variant beacon', 'tide lantern', 'brass compass', 'paper atlas', 'signal drum',
               'copper key', 'glass astrolabe', 'inkwell charter'];
  var CHT = ['The Oath', 'Into the Wild', 'The Old Road', 'Shadows Gather', 'The Price',
             'The Turning', 'The Last Stand', 'The Crown', 'Launch Window', 'The Long Dark',
             'Signal Lost', 'New Ceres', 'The Core', 'Rogue Vector', 'Event Horizon',
             'The Choice', 'Burn', 'Home Signal', 'First Light', 'The Crossing'];
  var S1 = ['The plan was fragile: reach the {P} before the {T} did.',
            '{N1} never meant to chase the {T}, but the {P} left no choice.',
            'Every map agreed on one thing: the {T} belonged in the {P}.',
            'Dawn came late to the {P}, and {N1} was already packed.'];
  var S2 = ['{N2} read the signs twice, then folded the chart away.',
            'The {T} hummed low, as if it remembered the {P}.',
            'No one at the {P} would say the word aloud — not even {N2}.',
            '{N1} traded the spare {T} for passage, and asked no questions.'];
  var S3 = ['By nightfall the {P} was behind them, and the {T} ahead.',
            'What happened at the {P} would be sung about for years.',
            '{N2} laughed for the first time in weeks, and meant it.',
            'The {T} kept its secret; the {P} kept them both.'];
  var PUB_KEYS = ['id', 'title', 'author', 'genre', 'gkey', 'desc', 'words', 'chapters', 'note',
                  'sources', 'origin', 'creation_mode', 'stamp'];

  function ri(rnd, a, b) { return a + Math.floor(rnd() * (b - a + 1)); }
  function pick(rnd, arr) { return arr[Math.floor(rnd() * arr.length)]; }
  function picki(rnd, arr) { return Math.floor(rnd() * arr.length); }
  function cap(s) { return s.charAt(0).toUpperCase() + s.slice(1); }
  function mkName(rnd, rec) { var a = picki(rnd, SYL), b = picki(rnd, SYL), c = picki(rnd, SYL), d = picki(rnd, SYL); rec.push(a, b, c, d); return cap(SYL[a] + SYL[b]) + ' ' + cap(SYL[c] + SYL[d]); }
  function fill(tpl, n1, n2, pl, th) {
    return tpl.split('{N1}').join(n1).split('{N2}').join(n2).split('{P}').join(pl).split('{T}').join(th);
  }
  function wordCount(s) { return s.trim().split(/\s+/).length; }

  /* builders take explicit pool indices so the verifier can rebuild exactly */
  function titleFrom(ti) {
    if (ti[0] === 0) return 'The ' + TA[ti[1]] + ' of ' + TB[ti[2]];
    if (ti[0] === 1) return TA[ti[1]] + ' ' + TB[ti[2]] + ' ' + TC[ti[3]];
    return 'The ' + TA[ti[1]] + ' ' + TC[ti[3]];
  }
  function descFrom(genre, di, n1, n2, nCh) {
    var pl = PLACE[di[0]], th = THING[di[1]];
    return 'A sweeping tale of ' + GNOUN[genre] + ': ' + n1 + ' and ' + n2 +
      ' journey toward the ' + pl + ', where the ' + th +
      ' will decide everything. A finished Signature novel: ' + nCh +
      ' chapters, full text, ready to read aloud.';
  }
  function chapBodyFrom(ci, n1, n2) {
    var pl = PLACE[ci[3]], th = THING[ci[4]];
    return fill(S1[ci[0]], n1, n2, pl, th) + ' ' + fill(S2[ci[1]], n1, n2, pl, th) + ' ' +
           fill(S3[ci[2]], n1, n2, pl, th);
  }

  function generate(seed, opts, rnd) {
    opts = opts || {};
    var genre = opts.type && GENRES.indexOf(opts.type) >= 0 ? opts.type : pick(rnd, GENRES);
    var ti = [ri(rnd, 0, 2), picki(rnd, TA), picki(rnd, TB), picki(rnd, TC)];
    var nameRec = [];
    var n1 = mkName(rnd, nameRec), n2 = mkName(rnd, nameRec);
    var di = [picki(rnd, PLACE), picki(rnd, THING)];
    var nCh = ri(rnd, 6, 10);
    var chaps = [], words = 0;
    for (var i = 0; i < nCh; i++) {
      var ci = [picki(rnd, S1), picki(rnd, S2), picki(rnd, S3), picki(rnd, PLACE), picki(rnd, THING)];
      var cti = picki(rnd, CHT);
      var body = chapBodyFrom(ci, n1, n2);
      words += wordCount(body);
      chaps.push({ t: CHT[cti], b: body, _ci: ci, _cti: cti });
    }
    var n = (opts.baseN || 0) + 1;
    var rec = {
      id: ID_PREFIX + String(n).padStart(6, '0'),
      title: titleFrom(ti),
      author: AUTHOR,
      genre: genre,
      gkey: GKEY[genre],
      desc: descFrom(genre, di, n1, n2, nCh),
      words: words,
      chapters: chaps.map(function (c) { return { t: c.t, b: c.b }; }),
      note: 'GENERATED SAMPLE — an original generated work created by the Signature generator. All names, places, and events are invented. Not a stored archive book.',
      sources: [],
      origin: 'generated',
      creation_mode: 'GENERATED',
      stamp: STAMP,
      _ti: ti, _di: di, _nameRec: nameRec, _chaps: chaps, _genre: genre, _seed: seed
    };
    var pub = {};
    PUB_KEYS.forEach(function (k) { pub[k] = rec[k]; });
    pub._priv = rec;
    return pub;
  }

  /* independent verifier: rebuilds title, desc, chapters from pool indices */
  function verify(priv) {
    var errs = [];
    if (GENRES.indexOf(priv._genre) < 0) return ['bad genre'];
    if (priv.gkey !== GKEY[priv._genre]) errs.push('gkey mismatch');
    if (priv.title !== titleFrom(priv._ti)) errs.push('title rebuild mismatch');
    var nr = priv._nameRec;
    if (!Array.isArray(nr) || nr.length !== 8) return errs.concat(['bad name recipe']);
    var n1 = cap(SYL[nr[0]] + SYL[nr[1]]) + ' ' + cap(SYL[nr[2]] + SYL[nr[3]]);
    var n2 = cap(SYL[nr[4]] + SYL[nr[5]]) + ' ' + cap(SYL[nr[6]] + SYL[nr[7]]);
    if (priv.desc !== descFrom(priv._genre, priv._di, n1, n2, priv._chaps.length))
      errs.push('desc rebuild mismatch');
    var words = 0, i;
    if (!Array.isArray(priv._chaps) || priv._chaps.length !== priv.chapters.length)
      return errs.concat(['chapter recipe mismatch']);
    for (i = 0; i < priv._chaps.length; i++) {
      var c = priv._chaps[i], pub2 = priv.chapters[i];
      var body = chapBodyFrom(c._ci, n1, n2);
      if (pub2.t !== CHT[c._cti] || pub2.b !== body) { errs.push('chapter rebuild mismatch at ' + i); break; }
      words += wordCount(body);
    }
    if (priv.words !== words) errs.push('word count mismatch: claimed ' + priv.words + ', actual ' + words);
    return errs;
  }

  function validate(rec) {
    var errs = [];
    if (!rec || typeof rec !== 'object') return { ok: false, errors: ['not an object'] };
    ['id', 'title', 'author', 'genre', 'gkey', 'desc', 'words', 'chapters', 'note'].forEach(function (k) {
      if (rec[k] === undefined || rec[k] === null || rec[k] === '') errs.push('missing field: ' + k);
    });
    if (rec.id && !/^JAH-BOOK-\d{6}$/.test(rec.id)) errs.push('bad id format');
    if (rec.genre && GENRES.indexOf(rec.genre) < 0) errs.push('bad genre');
    if (!Array.isArray(rec.chapters) || rec.chapters.length < 6) errs.push('chapters must have 6+ entries');
    if (rec._priv) {
      var p = rec._priv;
      PUB_KEYS.forEach(function (k) {
        if (JSON.stringify(rec[k]) !== JSON.stringify(p[k])) errs.push('field diverged from verified copy: ' + k);
      });
      errs = errs.concat(verify(p));
    }
    else errs.push('no private recipe — cannot independently verify');
    return { ok: errs.length === 0, errors: errs };
  }

  function driftCheck(rec, archiveSample) {
    var errs = [];
    (archiveSample || []).forEach(function (a) {
      var t = a.title || a.t;
      if (t && String(t).toLowerCase() === String(rec.title).toLowerCase())
        errs.push('duplicate of archived book title: ' + rec.title);
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
        rec2.id = rec.id;
        return rec2;
      }
    }
    return rec;
  }

  JAHDB.registerGenerator('books', {
    version: VERSION,
    generate: generate,
    validate: validate,
    driftCheck: driftCheck,
    themedGenerate: themedGenerate,
    types: GENRES
  });
})();
