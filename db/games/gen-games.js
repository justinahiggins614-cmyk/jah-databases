/* ✳ SIGNATURE — JAH Game Data Base generator. Property of Justin Addam Higgins (JAH).
   Boundless generator: produces NEW game-concept records in the exact archive
   format (id, title, genre, era, concept, desc, controls, rules, win,
   difficulty, cover, ai). Built from the store's own deterministic pools, with
   ids above the store's 1,000,000-record deterministic tail. Deterministic:
   same seed + version => same record. An independent verifier rebuilds every
   claim from the private pool indices before acceptance. */
(function () {
  'use strict';
  var VERSION = 'jahdb-games-1.0';
  var ID_PREFIX = 'JAH-GAME-';
  var ID_DIGITS = 6;
  var STORE_TAIL_MAX = 1000000; /* the store's deterministic concept tail ends here */

  var GENRES = ['arcade', 'shooter', 'racer', 'platformer', 'puzzle', 'explorer',
    'combat', 'maze', 'miner', 'defense', 'pong', 'flyer'];
  var ERAS = ['1970s Arcade', '8-bit', '16-bit', '90s', 'Modern', 'Mobile', 'Future'];
  var T1 = ['Neon', 'Turbo', 'Quantum', 'Crimson', 'Shadow', 'Pixel', 'Astro', 'Iron',
    'Storm', 'Ghost', 'Solar', 'Vortex', 'Ember', 'Frost', 'Blaze', 'Echo'];
  var T2 = ['Strike', 'Drift', 'Quest', 'Siege', 'Run', 'Legends', 'Force', 'Realm',
    'Dash', 'Arena', 'Voyage', 'Clash', 'Rising', 'Prime', 'Zero', 'X'];
  var HOOKS = {
    arcade: 'Dodge the patterns, chase the high score — pure reflex joy.',
    shooter: 'Blast the swarm, dodge the storm, beat the boss.',
    racer: 'Out-drive the pack across wild tracks.',
    platformer: 'Jump, bounce and climb to the goal flag.',
    puzzle: 'Think three moves ahead and clear the board.',
    explorer: 'Chart strange sectors and uncover their secrets.',
    combat: 'Hold the line through escalating waves.',
    maze: 'Find the exit before your energy runs out.',
    miner: 'Harvest the belt and bank your credits.',
    defense: 'Build, upgrade, and hold the road.',
    pong: 'The eternal duel of paddle and ball.',
    flyer: 'Thread the gates — one more try.'
  };
  var DIFFS = ['Easy', 'Medium', 'Hard'];
  var CONTROLS = 'Concept — controls ship with the full build.';
  var RULES = 'Concept record — the full build ships with complete rules and win conditions.';
  var WIN = 'Concept record — win conditions ship with the full build.';
  var DESC_TAIL = ' (Concept record — full build queued in the generator.)';
  var AI = { id: 'JAH-AI-DOM-074', name: 'Game Master (RPG)', role: 'Concept narrator', line: 'Weaves worlds from dice and dreams.' };

  /* the store catalog's own palette hash — replicated exactly */
  function catalogHash(s) {
    var h = 1779033703 ^ String(s).length;
    for (var i = 0; i < String(s).length; i++) {
      h = Math.imul(h ^ String(s).charCodeAt(i), 3432918353);
      h = (h << 13) | (h >>> 19);
    }
    return h >>> 0;
  }
  function pickI(rnd, n) { return Math.floor(rnd() * n); }
  function pick(rnd, arr) { return arr[pickI(rnd, arr.length)]; }
  function buildDesc(genre, era) {
    return 'A Signature-line ' + genre + ' concept in ' + era + ' style. ' + HOOKS[genre] + DESC_TAIL;
  }
  function buildName(i1, i2) { return T1[i1] + ' ' + T2[i2]; }

  function generate(seed, opts, rnd) {
    opts = opts || {};
    var gi = pickI(rnd, GENRES.length), ei = pickI(rnd, ERAS.length);
    if (opts.type && GENRES.indexOf(opts.type) >= 0) gi = GENRES.indexOf(opts.type);
    var i1 = pickI(rnd, T1.length), i2 = pickI(rnd, T2.length), di = pickI(rnd, DIFFS.length);
    var n = (opts.baseN || 0) + 1;
    var id = ID_PREFIX + String(n).padStart(ID_DIGITS, '0');
    var genre = GENRES[gi], era = ERAS[ei];
    var pub = {
      id: id,
      n: n,
      title: buildName(i1, i2),
      genre: genre,
      era: era,
      concept: true,
      desc: buildDesc(genre, era),
      controls: CONTROLS,
      rules: RULES,
      win: WIN,
      difficulty: DIFFS[di],
      cover: { palette: catalogHash(id) % 8, motif: genre },
      ai: { id: AI.id, name: AI.name, role: AI.role, line: AI.line },
      origin: 'generated',
      stamp: 'JAH Game Data Base — generated game-concept record.'
    };
    pub._priv = { gi: gi, ei: ei, i1: i1, i2: i2, di: di, seed: seed };
    return pub;
  }

  function validate(rec) {
    var errs = [];
    if (!rec || typeof rec !== 'object') return { ok: false, errors: ['not an object'] };
    ['id', 'title', 'genre', 'era', 'desc', 'difficulty', 'cover', 'ai'].forEach(function (k) {
      if (rec[k] === undefined || rec[k] === null || rec[k] === '') errs.push('missing field: ' + k);
    });
    if (rec.id && !/^JAH-GAME-\d{6,}$/.test(rec.id)) errs.push('bad id format');
    if (rec.id) {
      var n = parseInt(rec.id.slice(9), 10);
      if (!(n > STORE_TAIL_MAX)) errs.push('id is inside the store\'s deterministic tail — must be above ' + STORE_TAIL_MAX);
    }
    if (rec.genre && GENRES.indexOf(rec.genre) < 0) errs.push('unknown genre');
    if (rec.era && ERAS.indexOf(rec.era) < 0) errs.push('unknown era');
    if (rec.concept !== true) errs.push('concept flag must be true');
    if (rec._priv) {
      var p = rec._priv;
      var idxok = p.gi >= 0 && p.gi < GENRES.length && p.ei >= 0 && p.ei < ERAS.length &&
                  p.i1 >= 0 && p.i1 < T1.length && p.i2 >= 0 && p.i2 < T2.length &&
                  p.di >= 0 && p.di < DIFFS.length;
      if (!idxok) errs.push('private pool indices out of range');
      else {
        var genre = GENRES[p.gi], era = ERAS[p.ei];
        if (rec.genre !== genre) errs.push('genre does not match private pick');
        if (rec.era !== era) errs.push('era does not match private pick');
        if (rec.title !== buildName(p.i1, p.i2)) errs.push('title does not rebuild from private picks');
        if (rec.desc !== buildDesc(genre, era)) errs.push('desc does not rebuild from private picks');
        if (rec.difficulty !== DIFFS[p.di]) errs.push('difficulty does not match private pick');
        if (rec.controls !== CONTROLS) errs.push('controls text mismatch');
        if (rec.rules !== RULES) errs.push('rules text mismatch');
        if (rec.win !== WIN) errs.push('win text mismatch');
        if (!rec.cover || rec.cover.palette !== catalogHash(rec.id) % 8 || rec.cover.motif !== genre)
          errs.push('cover does not recompute (palette hash / motif)');
      }
    } else errs.push('no private params — cannot independently verify');
    return { ok: errs.length === 0, errors: errs };
  }

  /* drift check: generated ids live beyond the store's tail and must not
     collide with any archived record id */
  function driftCheck(rec, archiveSample) {
    var errs = [];
    var n = parseInt(String(rec.id).slice(9), 10);
    if (!(n > STORE_TAIL_MAX)) errs.push('id inside the store tail');
    (archiveSample || []).forEach(function (a) {
      var aid = a.id || (Array.isArray(a) ? a[0] : null);
      if (aid && String(aid) === String(rec.id)) errs.push('id duplicates an archived record');
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

  JAHDB.registerGenerator('games', {
    version: VERSION,
    generate: generate,
    validate: validate,
    driftCheck: driftCheck,
    themedGenerate: themedGenerate,
    types: GENRES.slice()
  });
})();
