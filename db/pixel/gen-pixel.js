/* ✳ SIGNATURE — JAH Image and Video Data Base generator. Property of Justin Addam Higgins (JAH).
   Boundless generator: produces NEW creative-goods metadata records in the
   exact archive format (name, category, description, prompt, seed, palette,
   scene, keywords). Deterministic: same seed + version => same record.
   The generator emits structured metadata only — the record's image is the
   deterministic emblemSVG, never a hotlinked or fake image file. Every record
   is validated by an INDEPENDENT re-builder that reconstructs every derived
   field from the private raw picks before acceptance. */
(function () {
  'use strict';
  var VERSION = 'jahdb-pixel-1.0';
  var ID_PREFIX = 'JAH-GOODS-';
  var STAMP = 'Generated creative record — archive-format metadata for the JAH Image and Video Data Base. No image file is claimed; the emblem image is generated deterministically on view.';

  function pick(rnd, arr) { return arr[Math.floor(rnd() * arr.length)]; }

  var TYPES = ['backpack', 'banner', 'beach towel', 'calendar', 'flag', 'hat', 'hoodie',
    'keychain', 'lunchbox', 'mousepad', 'mug', 'notebook', 'number sticker', 'phone case',
    'playing cards', 'puzzle', 'room poster', 'socks', 'sticker', 'surfboard', 't-shirt',
    'tote bag', 'wall decal', 'water bottle'];

  var ADJ = ['Thunder', 'Golden', 'Velvet', 'Azure', 'Storm', 'Nova', 'Neon', 'Frozen',
    'Crimson', 'Blazing', 'Lunar', 'Wild', 'Solar', 'Midnight', 'Amber', 'Silver',
    'Cobalt', 'Ember', 'Ivory', 'Jade', 'Onyx', 'Pearl', 'Ruby', 'Sable'];
  var NOUN = ['Vista', 'Comet', 'Talon', 'Meadow', 'Summit', 'Ranger', 'Reef', 'Bolt',
    'Warden', 'Pioneer', 'Drift', 'Voyager', 'Harbor', 'Lantern', 'Falcon', 'Canyon',
    'Beacon', 'Monarch', 'Nomad', 'Oracle', 'Pinnacle', 'Quasar', 'Ridge', 'Sentry'];
  var PALETTES = ['Arctic Mint', 'Candy Pop', 'Cosmic Violet', 'Crimson Pulse',
    'Desert Gold', 'Forest Dawn', 'Meadow Pastel', 'Mono Ink', 'Neon Night',
    'Ocean Deep', 'Royal Indigo', 'Sunset Ember'];
  var SCENES = ['abstract', 'city', 'creature', 'landscape', 'object', 'ocean', 'space'];

  function cap(s) { return s.split(' ').map(function (w) { return w.charAt(0).toUpperCase() + w.slice(1); }).join(' '); }

  function generate(seed, opts, rnd) {
    opts = opts || {};
    var cat = opts.type && TYPES.indexOf(opts.type) >= 0 ? opts.type : pick(rnd, TYPES);
    var p = {
      adjI: Math.floor(rnd() * ADJ.length),
      nounI: Math.floor(rnd() * NOUN.length),
      cat: cat,
      palI: Math.floor(rnd() * PALETTES.length),
      sceneI: Math.floor(rnd() * SCENES.length),
      artSeed: Math.floor(rnd() * 4294967296)
    };
    var name = ADJ[p.adjI] + ' ' + NOUN[p.nounI] + ' ' + cap(cat);
    var n = (opts.baseN || 0) + 1 + (opts.seq || 0);
    var pub = {
      id: ID_PREFIX + String(n).padStart(6, '0'),
      n: n,
      type: 'creative',
      title: name,
      name: name,
      cat: cat,
      desc: 'A ' + name + ' design rendered as a ' + cat +
        ' — original Signature generative art, ready to print.',
      prompt: name.toLowerCase() + ' artwork',
      seed: p.artSeed,
      palette: PALETTES[p.palI],
      scene: SCENES[p.sceneI],
      kw: [ADJ[p.adjI].toLowerCase(), NOUN[p.nounI].toLowerCase(), cat],
      stamp: STAMP
    };
    pub._priv = p;
    return pub;
  }

  /* independent re-builder: reconstruct every derived field from the raw picks */
  function validate(rec) {
    var errs = [];
    if (!rec || typeof rec !== 'object') return { ok: false, errors: ['not an object'] };
    ['id', 'type', 'title', 'name', 'cat', 'desc', 'prompt', 'seed',
      'palette', 'scene', 'kw'].forEach(function (k) {
      if (rec[k] === undefined || rec[k] === null || rec[k] === '') errs.push('missing field: ' + k);
    });
    if (rec.id && !/^JAH-GOODS-\d{6}$/.test(rec.id)) errs.push('bad id format');
    if (rec.cat && TYPES.indexOf(rec.cat) < 0) errs.push('bad cat');
    if (!Array.isArray(rec.kw) || rec.kw.length !== 3) errs.push('kw must be 3 keywords');
    if (rec._priv) {
      var p = rec._priv;
      var name = ADJ[p.adjI] + ' ' + NOUN[p.nounI] + ' ' + cap(p.cat);
      if (rec.name !== name) errs.push('name mismatch vs raw picks');
      if (rec.title !== name) errs.push('title mismatch vs raw picks');
      if (rec.cat !== p.cat) errs.push('cat mismatch vs raw picks');
      if (rec.desc !== 'A ' + name + ' design rendered as a ' + p.cat +
        ' — original Signature generative art, ready to print.') errs.push('desc mismatch vs raw picks');
      if (rec.prompt !== name.toLowerCase() + ' artwork') errs.push('prompt mismatch vs raw picks');
      if (rec.seed !== p.artSeed) errs.push('seed mismatch vs raw picks');
      if (rec.palette !== PALETTES[p.palI]) errs.push('palette mismatch vs raw picks');
      if (rec.scene !== SCENES[p.sceneI]) errs.push('scene mismatch vs raw picks');
      var wantKw = [ADJ[p.adjI].toLowerCase(), NOUN[p.nounI].toLowerCase(), p.cat];
      if (JSON.stringify(rec.kw) !== JSON.stringify(wantKw)) errs.push('kw mismatch vs raw picks');
    } else errs.push('no private raw picks — cannot independently verify');
    return { ok: errs.length === 0, errors: errs };
  }

  /* drift check: generated title must not duplicate an archived goods title */
  function driftCheck(rec, archiveSample) {
    var errs = [];
    (archiveSample || []).forEach(function (a) {
      var t = Array.isArray(a) ? a[1] : a.title;
      if (t && t === rec.title) errs.push('duplicate of archived creative: ' + t);
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

  JAHDB.registerGenerator('pixel', {
    version: VERSION,
    generate: generate,
    validate: validate,
    driftCheck: driftCheck,
    themedGenerate: themedGenerate,
    types: TYPES
  });
})();
