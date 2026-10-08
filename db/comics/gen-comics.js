/* ✳ SIGNATURE — JAH Comic Data Base generator. Property of Justin Addam Higgins (JAH).
   Boundless generator: produces NEW comic records in the archive's exact
   schema (id, series, skey, num, title, chars, desc, pages, words, note,
   creation_mode). All names, dialogue, and captions are assembled
   combinatorially from clean pools — every character, place, and event is
   invented — and the word count is genuinely computed from the pages.
   Honestly marked GENERATED. Deterministic: same seed + version => same
   record. An INDEPENDENT verifier rebuilds every field from the private
   pool indices before acceptance. */
(function () {
  'use strict';
  var VERSION = 'jahdb-comics-1.0';
  var ID_PREFIX = 'JAH-COMIC-';
  var STAMP = 'Official JAH Comic Archive — generated boundlessly, verified independently.';
  /* real archive series -> skey (signature-comics data/index/comics.idx.json.gz) */
  var SERIES = ['THE SIGNALBEARERS', 'EMBERFALL', 'THE HOLLOW CIRCUIT', 'TIDEBOUND',
                'THE GLOAMING WATCH', "STARFARER'S LOG", 'THE CLOCKWORK MENAGERIE',
                'JUNIOR SIGNALS', 'COSMIC CROSSOVER EVENTS'];
  var SKEY = { 'THE SIGNALBEARERS': 'signal', 'EMBERFALL': 'ember', 'THE HOLLOW CIRCUIT': 'circuit',
    'TIDEBOUND': 'tide', 'THE GLOAMING WATCH': 'gloam', "STARFARER'S LOG": 'starlog',
    'THE CLOCKWORK MENAGERIE': 'clockwork', 'JUNIOR SIGNALS': 'junior', 'COSMIC CROSSOVER EVENTS': 'event' };
  var PUB_KEYS = ['id', 'series', 'skey', 'num', 'title', 'chars', 'desc', 'pages',
                  'words', 'note', 'creation_mode', 'stamp'];

  var TA = ['Relay', 'Pale', 'Ghosts', 'Ember', 'Tide', 'Signal', 'Hollow', 'Crimson',
            'Silent', 'Broken', 'Golden', 'Last', 'First', 'Hidden', 'Iron', 'Storm'];
  var TB = ['Signals', 'Vale', 'Sector Nine', 'Dawn', 'Circuit', 'Watch', 'Harbor', 'Crown',
            'Lanterns', 'Depths', 'Spire', 'Frontier', 'Archive', 'Tempest', 'Garden', 'Bridge'];
  var SYL = ['il', 'mir', 'vav', 'ix', 'rhe', 'ka', 'or', 'pha', 'syl', 'rak',
             'ol', 'rine', 'tam', 'ere', 'gal', 'bex', 'jog', 'sed'];
  var CODE = ['Illmir', 'Vavix', 'Rhekaor', 'Pharaka', 'Olrine', 'Sylrakia', 'Tamere', 'Galbex',
              'Rherine', 'Joglen', 'Emberlyn', 'Cinderjaw', 'Vesperine', 'Holloway', 'Tidecaller', 'Starlume'];
  var POWER = ['star charting', 'ember shaping', 'tide calling', 'signal weaving', 'storm reading',
               'iron mending', 'lantern lighting', 'frost tracing', 'echo stepping', 'gear turning'];
  var PLACE = ['Sector Nine rooftops', 'Cinderhold Keep', 'the deep orbit docks', 'Lantern Row',
               'the ash valley', 'Meridian harbor', 'the clockwork warrens', 'Frostgate ridge'];
  var CAPS = ['The call comes at shift change: {P} needs {C0}.',
              '{C0} hurries toward {P}, frost tracing flaring.',
              'Dawn breaks over {P} — and {C0} is already mid-stride.',
              '{C1} holds the line at {P} while {C0} moves in.',
              'Somewhere above {P}, the old signal fires again.'];
  var DLG = ['"The {P} crew can\'t have gone far. Look for frost on the inside of glass."',
             '"{C0}, the {P} route is collapsing — take the high line!"',
             '"I did not cross {P} to turn back now."',
             '"{C1} — cover the {P} gate. I will handle the rest."',
             '"Every light in {P} just went out at once."'];

  function ri(rnd, a, b) { return a + Math.floor(rnd() * (b - a + 1)); }
  function picki(rnd, arr) { return Math.floor(rnd() * arr.length); }
  function cap(s) { return s.charAt(0).toUpperCase() + s.slice(1); }
  function wordCount(s) { return s.trim().split(/\s+/).length; }
  function fill(tpl, c0, c1, pl) {
    return tpl.split('{C0}').join(c0).split('{C1}').join(c1).split('{P}').join(pl);
  }

  function titleFrom(ti) { return TA[ti[0]] + ' of ' + TB[ti[1]]; }
  function charFrom(ci) {
    return { name: cap(SYL[ci[0]] + SYL[ci[1]]) + ' ' + cap(SYL[ci[2]] + SYL[ci[3]]),
             code: CODE[ci[4]], power: POWER[ci[5]] };
  }

  function generate(seed, opts, rnd) {
    opts = opts || {};
    var series = opts.type && SERIES.indexOf(opts.type) >= 0 ? opts.type : SERIES[Math.floor(rnd() * SERIES.length)];
    var num = ri(rnd, 1, 999);
    var ti = [picki(rnd, TA), picki(rnd, TB)];
    var nCh = ri(rnd, 2, 4);
    var charIdx = [], chars = [];
    for (var i = 0; i < nCh; i++) {
      var ci = [picki(rnd, SYL), picki(rnd, SYL), picki(rnd, SYL), picki(rnd, SYL),
                picki(rnd, CODE), picki(rnd, POWER)];
      charIdx.push(ci);
      chars.push(charFrom(ci));
    }
    var c0 = chars[0].code, c1 = chars.length > 1 ? chars[1].code : chars[0].code;
    var pageIdx = [], pages = [], words = 0;
    for (var pg = 0; pg < 6; pg++) {
      var pi = [picki(rnd, CAPS), picki(rnd, DLG), picki(rnd, PLACE)];
      pageIdx.push(pi);
      var cp = fill(CAPS[pi[0]], c0, c1, PLACE[pi[2]]);
      var dg = fill(DLG[pi[1]], c0, c1, PLACE[pi[2]]);
      words += wordCount(cp) + wordCount(dg);
      pages.push({ cap: cp, dlg: dg });
    }
    var title = titleFrom(ti);
    var starring = chars.map(function (c) { return c.code + ' (' + c.name + ')'; }).join(', ');
    var n = (opts.baseN || 0) + 1;
    var rec = {
      id: ID_PREFIX + String(n).padStart(6, '0'),
      series: series,
      skey: SKEY[series],
      num: num,
      title: title,
      chars: chars,
      desc: series + ' #' + num + ' — ' + title + '. A new chapter in the Signature heroes universe: ' +
            pages[0].cap + ' Starring ' + starring + '.',
      pages: pages,
      words: words,
      note: 'GENERATED SAMPLE — an original generated comic created by the Signature generator. All characters, places, and events are invented. Not a stored archive comic.',
      creation_mode: 'GENERATED',
      stamp: STAMP,
      _ti: ti, _num: num, _charIdx: charIdx, _pageIdx: pageIdx, _series: series, _seed: seed
    };
    var pub = {};
    PUB_KEYS.forEach(function (k) { pub[k] = rec[k]; });
    pub._priv = rec;
    return pub;
  }

  /* independent verifier: rebuilds title, chars, pages from pool indices */
  function verify(priv) {
    var errs = [];
    if (SERIES.indexOf(priv._series) < 0) return ['bad series'];
    if (priv.skey !== SKEY[priv._series]) errs.push('skey mismatch');
    if (priv.num !== priv._num) errs.push('issue number mismatch');
    if (priv.title !== titleFrom(priv._ti)) errs.push('title rebuild mismatch');
    var chars = priv._charIdx.map(charFrom);
    if (JSON.stringify(chars) !== JSON.stringify(priv.chars)) errs.push('chars rebuild mismatch');
    var c0 = chars[0].code, c1 = chars.length > 1 ? chars[1].code : chars[0].code;
    var words = 0, i, cap0 = '';
    if (!Array.isArray(priv._pageIdx) || priv._pageIdx.length !== 6 ||
        !Array.isArray(priv.pages) || priv.pages.length !== 6)
      return errs.concat(['page recipe mismatch']);
    for (i = 0; i < 6; i++) {
      var pi = priv._pageIdx[i];
      var cp = fill(CAPS[pi[0]], c0, c1, PLACE[pi[2]]);
      var dg = fill(DLG[pi[1]], c0, c1, PLACE[pi[2]]);
      if (i === 0) cap0 = cp;
      if (priv.pages[i].cap !== cp || priv.pages[i].dlg !== dg) { errs.push('page rebuild mismatch at ' + i); break; }
      words += wordCount(cp) + wordCount(dg);
    }
    if (priv.words !== words) errs.push('word count mismatch: claimed ' + priv.words + ', actual ' + words);
    var starring = chars.map(function (c) { return c.code + ' (' + c.name + ')'; }).join(', ');
    var wantDesc = priv._series + ' #' + priv._num + ' — ' + titleFrom(priv._ti) +
      '. A new chapter in the Signature heroes universe: ' + cap0 +
      ' Starring ' + starring + '.';
    if (priv.desc !== wantDesc) errs.push('desc rebuild mismatch');
    return errs;
  }

  function validate(rec) {
    var errs = [];
    if (!rec || typeof rec !== 'object') return { ok: false, errors: ['not an object'] };
    ['id', 'series', 'skey', 'num', 'title', 'chars', 'desc', 'pages', 'words'].forEach(function (k) {
      if (rec[k] === undefined || rec[k] === null || rec[k] === '') errs.push('missing field: ' + k);
    });
    if (rec.id && !/^JAH-COMIC-\d{6}$/.test(rec.id)) errs.push('bad id format');
    if (rec.series && SERIES.indexOf(rec.series) < 0) errs.push('bad series');
    if (!Array.isArray(rec.pages) || rec.pages.length !== 6) errs.push('pages must have exactly 6 entries');
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
        errs.push('duplicate of archived comic title: ' + rec.title);
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

  JAHDB.registerGenerator('comics', {
    version: VERSION,
    generate: generate,
    validate: validate,
    driftCheck: driftCheck,
    themedGenerate: themedGenerate,
    types: SERIES
  });
})();
