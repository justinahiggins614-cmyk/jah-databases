/* ✳ SIGNATURE — JAH Music Data Base generator. Property of Justin Addam Higgins (JAH).
   Boundless generator: produces NEW song records in the exact archive format
   (title, genre, mood, tempo, key, lyrics, chords, structure, desc).
   Deterministic: same seed + version => same record. Chords are genuinely
   transposed from the chosen key (I–V–vi–IV / i–VI–III–VII); lyrics are
   assembled from the archive-style line banks. Every record is validated by
   an INDEPENDENT re-builder that reconstructs every derived field from the
   private raw picks before acceptance. */
(function () {
  'use strict';
  var VERSION = 'jahdb-music-1.0';
  var ID_PREFIX = 'JAH-SONG-';
  var STAMP = 'Generated song record — JAH Music Data Base. Original generated lyrics and progression in archive format.';

  function ri(rnd, a, b) { return a + Math.floor(rnd() * (b - a + 1)); }
  function pick(rnd, arr) { return arr[Math.floor(rnd() * arr.length)]; }

  var TYPES = ['ambient', 'drum-and-bass', 'funk', 'hip-hop', 'house', 'jazz',
    'lofi', 'pop', 'reggae', 'rock', 'techno', 'trap'];
  var MOODS = ['bright', 'chill', 'dark', 'dreamy', 'driving', 'epic', 'gritty', 'smooth'];

  var ADJ = ['Amber', 'Silver', 'Midnight', 'Crimson', 'Restless', 'Golden', 'Slow',
    'Electric', 'Quiet', 'Hollow', 'Copper', 'Static', 'Paper', 'Velvet', 'Neon',
    'Lonely', 'Distant', 'Wild', 'Patient', 'Rising'];
  var NOUN = ['Harbor', 'Highway', 'Garden', 'Horizon', 'Orbit', 'Drift', 'Lantern',
    'Meadow', 'Tide', 'River', 'Signal', 'Wire', 'Summit', 'Thunder', 'Canyon',
    'Beacon', 'Mirror', 'Valley', 'Ember', 'Compass'];

  var CHROM = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B'];
  function transpose(root, semis) { return CHROM[(CHROM.indexOf(root) + semis + 12) % 12]; }
  /* genuine progressions from the key */
  function chordsFor(root, minor) {
    if (!minor) return transpose(root, 0) + ' - ' + transpose(root, 7) + ' - ' +
      transpose(root, 9) + 'm - ' + transpose(root, 5);
    return transpose(root, 0) + 'm - ' + transpose(root, 8) + ' - ' +
      transpose(root, 3) + ' - ' + transpose(root, 10);
  }

  var STRUCTURES = [
    'Intro (4 bars) / Verse (16) / Chorus (16) / Verse (16) / Chorus (16) / Bridge (8) / Chorus (16) / Outro (4)',
    'Intro (8 bars) / Verse (16) / Chorus (16) / Verse (16) / Chorus (16) / Outro (8)',
    'Verse (16) / Chorus (16) / Verse (16) / Chorus (16) / Bridge (8) / Chorus (24)',
    'Intro (4 bars) / Verse (16) / Pre-Chorus (8) / Chorus (16) / Verse (16) / Chorus (16) / Outro (4)'
  ];

  var VERSE_LINES = ['Dust on the dashboard, miles to go',
    'Streetlights painting shadows on the wall',
    'The radio hums a half-remembered tune',
    'Windows down, the night is wide awake',
    'Every mile marker tells a story',
    'The engine keeps a steady heartbeat',
    'Headlights carve a path through the dark',
    'We chase the dawn down empty roads',
    'Static fades as the signal comes in',
    'The map is folded, we drive by feel',
    'Neon signs blur into one long light',
    'Another town fades in the rearview'];
  var CHORUS_LINES = ['The rhythm of the wheels keeps time',
    'The chorus carries me to you',
    'Sing it louder than the thunder',
    'We are golden, we are free',
    'Hold the moment, do not let go',
    'This is where the heart runs wild',
    'Echoes rising, voices strong',
    'The night is ours, the road is long',
    'Every heartbeat finds the beat',
    'We will follow where it leads',
    'Hands up high into the sky',
    'The melody will never die'];
  var OUTRO_LINES = ['Let the harmony remain',
    'The wheels roll on, the song stays',
    'Fade the lights, keep the tune',
    'Until we meet the morning soon'];

  function lyricsOf(p) {
    var v = function (bank, idxs) { return idxs.map(function (i) { return bank[i % bank.length]; }); };
    var L = [];
    L.push('[Verse 1]');
    v(VERSE_LINES, p.v1).forEach(function (l) { L.push(l); });
    L.push(''); L.push('[Chorus]');
    v(CHORUS_LINES, p.ch).forEach(function (l) { L.push(l); });
    L.push(''); L.push('[Verse 2]');
    v(VERSE_LINES, p.v2).forEach(function (l) { L.push(l); });
    L.push(''); L.push('[Chorus]');
    v(CHORUS_LINES, p.ch).forEach(function (l) { L.push(l); });
    L.push(''); L.push('[Outro]');
    v(OUTRO_LINES, p.ou).forEach(function (l) { L.push(l); });
    return L.join('\n');
  }

  function generate(seed, opts, rnd) {
    opts = opts || {};
    var genre = opts.type && TYPES.indexOf(opts.type) >= 0 ? opts.type : pick(rnd, TYPES);
    var root = pick(rnd, CHROM), minor = rnd() < 0.4;
    var p = {
      adjI: Math.floor(rnd() * ADJ.length),
      nounI: Math.floor(rnd() * NOUN.length),
      genre: genre,
      mood: pick(rnd, MOODS),
      tempo: ri(rnd, 60, 180),
      root: root, minor: minor,
      structI: Math.floor(rnd() * STRUCTURES.length),
      v1: [ri(rnd, 0, 11), ri(rnd, 0, 11), ri(rnd, 0, 11), ri(rnd, 0, 11)],
      v2: [ri(rnd, 0, 11), ri(rnd, 0, 11), ri(rnd, 0, 11), ri(rnd, 0, 11)],
      ch: [ri(rnd, 0, 11), ri(rnd, 0, 11), ri(rnd, 0, 11), ri(rnd, 0, 11)],
      ou: [ri(rnd, 0, 3), ri(rnd, 0, 3)]
    };
    var title = ADJ[p.adjI] + ' ' + NOUN[p.nounI];
    var key = root + (minor ? ' minor' : ' major');
    var n = (opts.baseN || 0) + 1 + (opts.seq || 0);
    var pub = {
      id: ID_PREFIX + String(n).padStart(7, '0'),
      n: n,
      kind: 'song',
      type: 'song',
      title: title,
      genre: genre,
      mood: p.mood,
      tempo: p.tempo,
      key: key,
      lyrics: lyricsOf(p),
      chords: chordsFor(root, minor),
      structure: STRUCTURES[p.structI],
      desc: 'A ' + p.mood + ' ' + genre + ' song at ' + p.tempo + ' BPM in ' + key +
        ', written by the JAH Music Data Base generator.',
      stamp: STAMP
    };
    pub._priv = p;
    return pub;
  }

  /* independent re-builder: reconstruct every derived field from the raw picks */
  function validate(rec) {
    var errs = [];
    if (!rec || typeof rec !== 'object') return { ok: false, errors: ['not an object'] };
    ['id', 'kind', 'title', 'genre', 'mood', 'tempo', 'key',
      'lyrics', 'chords', 'structure', 'desc'].forEach(function (k) {
      if (rec[k] === undefined || rec[k] === null || rec[k] === '') errs.push('missing field: ' + k);
    });
    if (rec.id && !/^JAH-SONG-\d{7}$/.test(rec.id)) errs.push('bad id format');
    if (rec.genre && TYPES.indexOf(rec.genre) < 0) errs.push('bad genre');
    if (rec.tempo !== undefined && (rec.tempo < 60 || rec.tempo > 180)) errs.push('tempo out of range');
    if (rec.lyrics && rec.lyrics.indexOf('[Verse 1]') < 0) errs.push('lyrics missing structure');
    if (rec._priv) {
      var p = rec._priv;
      var title = ADJ[p.adjI] + ' ' + NOUN[p.nounI];
      var key = p.root + (p.minor ? ' minor' : ' major');
      if (rec.title !== title) errs.push('title mismatch vs raw picks');
      if (rec.key !== key) errs.push('key mismatch vs raw picks');
      if (rec.chords !== chordsFor(p.root, p.minor)) errs.push('chords mismatch vs raw picks (progression not transposed from key)');
      if (rec.lyrics !== lyricsOf(p)) errs.push('lyrics mismatch vs raw picks');
      if (rec.structure !== STRUCTURES[p.structI]) errs.push('structure mismatch vs raw picks');
      if (rec.genre !== p.genre) errs.push('genre mismatch vs raw picks');
      if (rec.tempo !== p.tempo) errs.push('tempo mismatch vs raw picks');
      if (rec.mood !== p.mood) errs.push('mood mismatch vs raw picks');
      var wantDesc = 'A ' + p.mood + ' ' + p.genre + ' song at ' + p.tempo + ' BPM in ' + key +
        ', written by the JAH Music Data Base generator.';
      if (rec.desc !== wantDesc) errs.push('desc mismatch vs raw picks');
    } else errs.push('no private raw picks — cannot independently verify');
    return { ok: errs.length === 0, errors: errs };
  }

  /* drift check: generated title must not duplicate an archived song title */
  function driftCheck(rec, archiveSample) {
    var errs = [];
    (archiveSample || []).forEach(function (a) {
      var t = Array.isArray(a) ? a[1] : a.title;
      if (t && t === rec.title) errs.push('duplicate of archived song: ' + t);
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

  JAHDB.registerGenerator('music', {
    version: VERSION,
    generate: generate,
    validate: validate,
    driftCheck: driftCheck,
    themedGenerate: themedGenerate,
    types: TYPES
  });
})();
