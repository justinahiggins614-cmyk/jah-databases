/* ✳ SIGNATURE — JAH Newspaper Data Base generator. Property of Justin Addam Higgins (JAH).
   Boundless generator: produces NEW edition records in the archive's exact
   schema (paper, date, issue, volume, articles, honesty, id, paper_id,
   fictionality_status, creation_mode, version, status, article_count,
   article_ids, content_hash). Every article is assembled combinatorially
   from clean pools — all people, places, and events are invented — and the
   content hash is genuinely computed from the article text.
   HONESTY: generated editions are ALWAYS marked creation_mode GENERATED,
   fictionality_status GENERATED_SAMPLE, status SAMPLE, with an explicit
   honesty note — they are sample article structures, NEVER presented as
   real published editions and NEVER reporting real events.
   Deterministic: same seed + version => same record. An INDEPENDENT
   verifier rebuilds every field from the private pool indices before
   acceptance. */
(function () {
  'use strict';
  var VERSION = 'jahdb-news-1.0';
  var ID_PREFIX = 'JAH-ED-';
  var ART_PREFIX = 'JAH-ARTICLE-';
  var STAMP = 'Official JAH Newspaper Archive — generated samples, verified independently.';
  /* real archive sections, matching the archived edition data */
  var SECTIONS = ['lead', 'culture', 'region', 'science', 'sports', 'weather',
                  'business', 'opinion', 'network'];
  var PUB_KEYS = ['paper', 'date', 'issue', 'volume', 'articles', 'honesty', 'id', 'paper_id',
                  'fictionality_status', 'creation_mode', 'version', 'status', 'coverage',
                  'created', 'updated', 'article_count', 'article_ids', 'content_hash', 'stamp'];
  var HONESTY = 'GENERATED SAMPLE — this edition was produced by the JAH Databases generator ' +
    'as a sample article structure in the archive\'s format. It is NOT a real published edition, ' +
    'and it reports no real events, people, or organizations. All names and places are invented.';

  var PLACE = ['Solara Heights', 'Emberline', 'Stonebridge', 'Aldermere', 'Frostgate',
               'Juniper Quay', 'Meridian City', 'Tarnwick', 'Lumenport', 'Halloway'];
  var THING = ['Riverside', 'Great Bell', 'Starwatch', 'Makers\'', 'Harborlight',
               'Clockwork', 'Lantern', 'Tidewater', 'Skybridge', 'Aurora'];
  var HEAD = ['{P} Council Approves the {T} Promenade',
              'Engineers Tune the {T} of {P}',
              '{P} Market Hall Reopens After Restoration',
              'Stargazers Report Clear Nights Over {P}',
              'Makers\' Guild Opens New Workshops in {P}',
              '{T} Championship Tightens as Season Closes in {P}',
              'Thousands Turn Out as the {T} Gala Opens in {P}',
              'New Ferry Route Joins {P} to the Outer Quays'];
  var BY = ['By Alistair Fenwick, Globe staff', 'By Odette Lorr, staff writer',
            'By Edmund Sable, correspondent', 'By Vivienne Lark, staff writer',
            'By Percival Odd, contributing editor', 'By Imogen Starr, Globe staff'];
  var P1 = ['Residents interviewed near the old market were broadly in favor, though several asked pointed questions about the timeline.',
            'Merchants report strong trade, and the night ferries have added an extra sailing on Fridays.',
            'Independent observers called the results careful, patient work of the best kind.',
            'The full paper, set in handsome type, runs to forty pages and is free to any reader who asks.'];
  var P2 = ['Council members said work crews would begin surveying within the fortnight.',
            'Tickets for the return fixture go on sale Friday; organizers expect another full house.',
            'Morning mists will burn off by mid-morning, giving way to the season\'s characteristic clear light.',
            'A second expedition is planned for the autumn, when conditions are expected to be ideal.'];

  function ri(rnd, a, b) { return a + Math.floor(rnd() * (b - a + 1)); }
  function picki(rnd, arr) { return Math.floor(rnd() * arr.length); }
  function fill(tpl, pl, th) { return tpl.split('{P}').join(pl).split('{T}').join(th); }
  function fnvHex(s) {
    var h = 2166136261;
    for (var i = 0; i < s.length; i++) { h ^= s.charCodeAt(i); h = Math.imul(h, 16777619); }
    return ('0000000' + (h >>> 0).toString(16)).slice(-8) +
           ('0000000' + (Math.imul(h, 16777619) >>> 0).toString(16)).slice(-8);
  }
  function artId(seed, i) {
    var sN = (typeof seed === 'number') ? seed : 0;
    return ART_PREFIX + String(900001 + (Math.abs(sN * 6 + i) % 89999)).padStart(6, '0');
  }
  function articleFrom(ai, byName, edId, artId) {
    var sec = SECTIONS[ai[0]];
    var h = fill(HEAD[ai[1]], PLACE[ai[3]], THING[ai[4]]);
    var body = [fill(P1[ai[5]], PLACE[ai[3]], THING[ai[4]]), fill(P2[ai[6]], PLACE[ai[3]], THING[ai[4]])];
    return {
      sec: sec,
      h: h,
      by: byName,
      body: body,
      id: artId,
      edition_id: edId,
      fictionality_status: 'GENERATED_SAMPLE',
      creation_mode: 'GENERATED',
      version: '1.0',
      content_hash: fnvHex(sec + '|' + h + '|' + byName + '|' + body.join(' '))
    };
  }

  function generate(seed, opts, rnd) {
    opts = opts || {};
    var leadSec = opts.type && SECTIONS.indexOf(opts.type) >= 0 ? opts.type : 'lead';
    var paper = ri(rnd, 0, 2);
    /* deterministic sample date: fixed base minus 0-60 days */
    var dayMs = 86400000;
    var d = new Date(Date.UTC(2026, 9, 8) - ri(rnd, 0, 60) * dayMs);
    var date = d.toISOString().slice(0, 10);
    var issue = ri(rnd, 600, 700), volume = ri(rnd, 1, 3);
    var leadIdx = SECTIONS.indexOf(leadSec);
    var secs = [leadIdx];
    while (secs.length < 6) {
      var s = picki(rnd, SECTIONS);
      if (secs.indexOf(s) < 0) secs.push(s);
    }
    var n = (opts.baseN || 0) + 1 + (opts.seq || 0);
    var edId = ID_PREFIX + String(n).padStart(6, '0');
    var artIdx = [], articles = [], i;
    var article_ids = [];
    for (i = 0; i < 6; i++) article_ids.push(artId(seed, i));
    for (i = 0; i < 6; i++) {
      var ai = [secs[i], picki(rnd, HEAD), picki(rnd, BY), picki(rnd, PLACE),
                picki(rnd, THING), picki(rnd, P1), picki(rnd, P2)];
      artIdx.push(ai);
      articles.push(articleFrom(ai, BY[ai[2]], edId, article_ids[i]));
    }
    var canonical = articles.map(function (a) { return a.sec + '|' + a.h + '|' + a.by + '|' + a.body.join(' '); }).join('‖');
    var rec = {
      paper: paper,
      date: date,
      issue: issue,
      volume: volume,
      articles: articles,
      honesty: HONESTY,
      id: edId,
      paper_id: 'JAH-PAPER-' + String(paper + 1).padStart(6, '0'),
      fictionality_status: 'GENERATED_SAMPLE',
      creation_mode: 'GENERATED',
      version: '1.0',
      status: 'SAMPLE',
      coverage: 'ecosystem',
      created: date,
      updated: date,
      article_count: 6,
      article_ids: article_ids,
      content_hash: fnvHex(canonical),
      stamp: STAMP,
      _artIdx: artIdx, _secs: secs, _paper: paper, _date: date, _issue: issue,
      _volume: volume, _leadIdx: leadIdx, _seed: seed
    };
    var pub = {};
    PUB_KEYS.forEach(function (k) { pub[k] = rec[k]; });
    pub._priv = rec;
    return pub;
  }

  /* independent verifier: rebuilds every article and the hash from indices */
  function verify(priv) {
    var errs = [];
    if (priv.paper !== priv._paper || priv.paper < 0 || priv.paper > 2) errs.push('paper mismatch');
    if (priv.date !== priv._date || !/^\d{4}-\d{2}-\d{2}$/.test(priv.date)) errs.push('date mismatch');
    if (priv.issue !== priv._issue || priv.volume !== priv._volume) errs.push('issue/volume mismatch');
    if (priv.paper_id !== 'JAH-PAPER-' + String(priv._paper + 1).padStart(6, '0')) errs.push('paper_id mismatch');
    if (priv.article_count !== 6) errs.push('article_count must be 6');
    if (!Array.isArray(priv._artIdx) || priv._artIdx.length !== 6 ||
        !Array.isArray(priv.articles) || priv.articles.length !== 6)
      return errs.concat(['article recipe mismatch']);
    if (priv._artIdx[0][0] !== priv._leadIdx) errs.push('lead section mismatch');
    var i, canonicalParts = [];
    for (i = 0; i < 6; i++) {
      var ai = priv._artIdx[i];
      if (SECTIONS.indexOf(SECTIONS[ai[0]]) < 0) { errs.push('bad section at ' + i); break; }
      var want = articleFrom(ai, BY[ai[2]], priv.id, priv.article_ids[i]);
      var got = priv.articles[i];
      if (got.sec !== want.sec || got.h !== want.h || got.by !== want.by ||
          got.body.length !== 2 || got.body[0] !== want.body[0] || got.body[1] !== want.body[1] ||
          got.id !== want.id || got.edition_id !== want.edition_id ||
          got.content_hash !== want.content_hash ||
          got.fictionality_status !== 'GENERATED_SAMPLE' || got.creation_mode !== 'GENERATED' ||
          got.version !== '1.0') {
        errs.push('article rebuild mismatch at ' + i); break;
      }
      if (priv.article_ids[i] !== artId(priv._seed, i)) { errs.push('article_id mismatch at ' + i); break; }
      canonicalParts.push(want.sec + '|' + want.h + '|' + want.by + '|' + want.body.join(' '));
    }
    if (priv.content_hash !== fnvHex(canonicalParts.join('‖'))) errs.push('content hash mismatch');
    if (priv.coverage !== 'ecosystem') errs.push('coverage altered');
    if (priv.created !== priv.date || priv.updated !== priv.date) errs.push('created/updated must equal edition date');
    if (priv.honesty !== HONESTY) errs.push('honesty note altered');
    if (priv.creation_mode !== 'GENERATED' || priv.fictionality_status !== 'GENERATED_SAMPLE' ||
        priv.status !== 'SAMPLE')
      errs.push('honesty markers altered');
    return errs;
  }

  function validate(rec) {
    var errs = [];
    if (!rec || typeof rec !== 'object') return { ok: false, errors: ['not an object'] };
    ['paper', 'date', 'issue', 'volume', 'articles', 'honesty', 'id', 'paper_id',
     'fictionality_status', 'creation_mode', 'version', 'status', 'coverage',
     'created', 'updated', 'article_count', 'article_ids', 'content_hash'].forEach(function (k) {
      if (rec[k] === undefined || rec[k] === null || rec[k] === '') errs.push('missing field: ' + k);
    });
    if (rec.id && !/^JAH-ED-\d{6}$/.test(rec.id)) errs.push('bad id format');
    if (!Array.isArray(rec.articles) || rec.articles.length !== 6) errs.push('articles must have exactly 6 entries');
    if (rec.creation_mode !== 'GENERATED') errs.push('generated editions must carry creation_mode GENERATED');
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
      var h = a.content_hash || (a[2]);
      if (h && String(h) === String(rec.content_hash)) errs.push('duplicate of archived edition content hash');
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

  JAHDB.registerGenerator('news', {
    version: VERSION,
    generate: generate,
    validate: validate,
    driftCheck: driftCheck,
    themedGenerate: themedGenerate,
    types: SECTIONS
  });
})();
