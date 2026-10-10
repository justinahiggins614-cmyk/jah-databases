/* ✳ SIGNATURE — JAH Llama Data Base generator. Property of Justin Addam Higgins (JAH).
   Boundless generator: produces NEW mix-and-match Llama build records in
   archive style — assembled ONLY from the archive's real parts: the real
   engine versions (SIGLLAMA-V1/V2), the real sampling card, and the real
   125 tool libraries. Deterministic: same seed + version => same record.
   An INDEPENDENT verifier rebuilds every build from its private parts
   before it is accepted. */
(function () {
  'use strict';
  var VERSION = 'jahdb-llama-1.0';
  var ID_PREFIX = 'JAH-LLAMA-';
  var STAMP = 'Official JAH Llama Build Archive — mixed and matched boundlessly, verified independently.';

  /* real tool-library index, from signature-llama data/tool-libraries.json:
     [id, name, version, category, optimal] */
var LIBS=[
 ["text-shorten","Shorten","1.0","Text & Words",1],
 ["text-count","Count","1.0","Text & Words",1],
 ["text-clean","Clean","1.0","Text & Words",0],
 ["text-keywords","Keywords","1.0","Text & Words",0],
 ["text-summarize","Summarize","1.0","Text & Words",0],
 ["text-template","Template Fill","1.0","Text & Words",0],
 ["text-diff","Diff Words","1.0","Text & Words",0],
 ["text-wrap","Wrap","1.0","Text & Words",0],
 ["text-tone","Tone Shift","1.0","Text & Words",0],
 ["text-bullets","Bullets","1.0","Text & Words",0],
 ["think-steps","Step Thinker","1.0","Thinking & Reasoning",1],
 ["think-proscons","Pros & Cons","1.0","Thinking & Reasoning",0],
 ["think-decide","Decider","1.0","Thinking & Reasoning",0],
 ["think-why","Five Whys","1.0","Thinking & Reasoning",0],
 ["think-socratic","Socratic Questions","1.0","Thinking & Reasoning",0],
 ["think-fermi","Fermi Estimator","1.0","Thinking & Reasoning",0],
 ["think-invert","Invert","1.0","Thinking & Reasoning",0],
 ["think-analogy","Analogy","1.0","Thinking & Reasoning",0],
 ["think-assume","Find Assumptions","1.0","Thinking & Reasoning",0],
 ["think-checklist","Checklist","1.0","Thinking & Reasoning",0],
 ["mem-note","Notes","1.0","Memory",1],
 ["mem-facts","Fact Store","1.0","Memory",0],
 ["mem-pin","Pin Board","1.0","Memory",0],
 ["mem-timeline","Timeline","1.0","Memory",0],
 ["mem-review","Review Scheduler","1.0","Memory",0],
 ["mem-context","Context Packer","1.0","Memory",0],
 ["mem-session","Session Log","1.0","Memory",0],
 ["mem-export","Memory Export","1.0","Memory",0],
 ["mem-digest","Digest","1.0","Memory",0],
 ["mem-search","Memory Search","1.0","Memory",0],
 ["chat-persona","Persona","1.0","Chat & Persona",1],
 ["chat-greet","Greeter","1.0","Chat & Persona",0],
 ["chat-farewell","Farewell","1.0","Chat & Persona",0],
 ["chat-frames","Prompt Frames","1.0","Chat & Persona",0],
 ["chat-history","History Keeper","1.0","Chat & Persona",0],
 ["chat-suggest","Reply Suggester","1.0","Chat & Persona",0],
 ["chat-recap","Chat Recap","1.0","Chat & Persona",0],
 ["chat-emoji","Mood Emoji","1.0","Chat & Persona",0],
 ["chat-opener","Opener","1.0","Chat & Persona",0],
 ["chat-closer","Closer","1.0","Chat & Persona",0],
 ["search-score","Scorer","1.0","Search & Knowledge",1],
 ["search-highlight","Highlighter","1.0","Search & Knowledge",0],
 ["search-filter","Filter List","1.0","Search & Knowledge",0],
 ["search-suggest","Suggester","1.0","Search & Knowledge",0],
 ["search-rank","Ranker","1.0","Search & Knowledge",0],
 ["search-snippet","Snippet","1.0","Search & Knowledge",0],
 ["search-dedupe","Dedupe","1.0","Search & Knowledge",0],
 ["search-group","Group By","1.0","Search & Knowledge",0],
 ["search-page","Paginator","1.0","Search & Knowledge",0],
 ["search-recent","Recent Searches","1.0","Search & Knowledge",0],
 ["math-calc","Safe Calculator","1.0","Math & Logic",1],
 ["math-stats","Statistics","1.0","Math & Logic",0],
 ["math-percent","Percent","1.0","Math & Logic",0],
 ["math-convert","Unit Converter","1.0","Math & Logic",0],
 ["math-geometry","Geometry","1.0","Math & Logic",0],
 ["math-finance","Money Math","1.0","Math & Logic",0],
 ["math-random","Random","1.0","Math & Logic",0],
 ["math-seq","Sequences","1.0","Math & Logic",0],
 ["math-clamp","Clamp & Round","1.0","Math & Logic",0],
 ["math-logic","Logic","1.0","Math & Logic",0],
 ["web-query","Query Strings","1.0","Web & Network",0],
 ["web-url","URL Tools","1.0","Web & Network",0],
 ["web-share","Share Links","1.0","Web & Network",0],
 ["web-meta","Meta Tags","1.0","Web & Network",0],
 ["web-ping","Ping","1.0","Web & Network",0],
 ["web-get","Get JSON","1.0","Web & Network",1],
 ["web-retry","Retry","1.0","Web & Network",0],
 ["web-cache","Cache","1.0","Web & Network",0],
 ["web-embed","Embed Tags","1.0","Web & Network",0],
 ["web-sitemap","Sitemap","1.0","Web & Network",0],
 ["data-json","JSON Tools","1.0","Files & Data",1],
 ["data-csv","CSV Tools","1.0","Files & Data",0],
 ["data-table","Markdown Table","1.0","Files & Data",0],
 ["data-sort","Sort By","1.0","Files & Data",0],
 ["data-chunk","Chunk","1.0","Files & Data",0],
 ["data-flatten","Flatten","1.0","Files & Data",0],
 ["data-hash","Hash & ID","1.0","Files & Data",0],
 ["data-validate","Validate","1.0","Files & Data",0],
 ["data-download","Download Text","1.0","Files & Data",0],
 ["data-lines","Lines","1.0","Files & Data",0],
 ["voice-speak","Speak","1.0","Voice & Audio",1],
 ["voice-stop","Stop Voice","1.0","Voice & Audio",0],
 ["voice-chunk","Speech Chunks","1.0","Voice & Audio",0],
 ["voice-presets","Voice Presets","1.0","Voice & Audio",0],
 ["voice-queue","Speech Queue","1.0","Voice & Audio",0],
 ["voice-buttons","Read Buttons","1.0","Voice & Audio",0],
 ["voice-announce","Announce","1.0","Voice & Audio",0],
 ["voice-captions","Captions","1.0","Voice & Audio",0],
 ["voice-clean","Clean Transcript","1.0","Voice & Audio",0],
 ["voice-rate","Reading Time","1.0","Voice & Audio",0],
 ["safe-honesty","Honesty Notes","1.0","Safety & Honesty",1],
 ["safe-pii","Redact PII","1.0","Safety & Honesty",0],
 ["safe-clamp","Clamp Output","1.0","Safety & Honesty",0],
 ["safe-disclaimer","Disclaimers","1.0","Safety & Honesty",0],
 ["safe-hedge","Hedge Check","1.0","Safety & Honesty",0],
 ["safe-kid","Kid Filter","1.0","Safety & Honesty",0],
 ["safe-guard","Prompt Guard","1.0","Safety & Honesty",0],
 ["safe-ratelimit","Rate Limit","1.0","Safety & Honesty",0],
 ["safe-audit","Audit Log","1.0","Safety & Honesty",0],
 ["safe-license","License Text","1.0","Safety & Honesty",0],
 ["embed-snippet","Embed Code","1.0","Embed & Integrate",0],
 ["embed-ask","Ask Snippet","1.0","Embed & Integrate",1],
 ["embed-chatbox","Chat Box","1.0","Embed & Integrate",0],
 ["embed-dictlink","Dictionary Link","1.0","Embed & Integrate",0],
 ["embed-sectionlink","Section Link","1.0","Embed & Integrate",0],
 ["embed-loader","Library Loader","1.0","Embed & Integrate",0],
 ["embed-optimal","Optimal Apply","1.0","Embed & Integrate",0],
 ["embed-status","Status Pill","1.0","Embed & Integrate",0],
 ["embed-manifest","Manifest URL","1.0","Embed & Integrate",0],
 ["embed-copybtn","Copy Button","1.0","Embed & Integrate",0],
 ["fun-joke","Joke Setups","1.0","Fun & Creative",0],
 ["fun-story","Story Starters","1.0","Fun & Creative",0],
 ["fun-haiku","Haiku","1.0","Fun & Creative",0],
 ["fun-riddle","Riddles","1.0","Fun & Creative",0],
 ["fun-name","AI Namer","1.0","Fun & Creative",0],
 ["fun-praise","Praise","1.0","Fun & Creative",0],
 ["fun-quest","Quest Maker","1.0","Fun & Creative",0],
 ["fun-mashup","Mashup","1.0","Fun & Creative",0],
 ["fun-emoji","Emoji Story","1.0","Fun & Creative",0],
 ["fun-banner","Banner","1.0","Fun & Creative",0],
 ["conv-deep-talk","Deep Talk","1.0","Conversation",1],
 ["conv-ecosystem-guide","Ecosystem Guide","1.0","Conversation",1],
 ["conv-socratic","Socratic Reasoner","1.0","Conversation",1],
 ["conv-story-weaver","Story Weaver","1.0","Conversation",1],
 ["conv-debate","Debate Partner","1.0","Conversation",1],
];
  /* real engine versions, from signature-llama llama-manifest.json / model-status.json */
  var ENGINES = {
    v1: { model_id: 'SIGLLAMA-V1', name: 'Signature Llama v1', version: '1.0',
          params: 2983488, layers: 5, heads: 8, hidden: 192, status: 'superseded — preserved, still downloadable' },
    v2: { model_id: 'SIGLLAMA-V2', name: 'Signature Llama v2', version: '2.0',
          params: 4056768, layers: 5, heads: 8, hidden: 192, context: 96, status: 'live' }
  };
  /* build profiles — how many libraries the mix pulls in */
  var PROFILES = ['optimal', 'standard', 'maximal', 'minimal'];
  var PUB_KEYS = ['id', 'n', 'name', 'title', 'profile', 'engine', 'sampling', 'libraries',
                  'library_count', 'build_hash', 'mix_lineage', 'note', 'stamp'];

  var NAME_A = ['Ember', 'Signal', 'Lantern', 'Harbor', 'Cinder', 'Juniper', 'Marble', 'North',
                'Peregrine', 'Quill', 'Ridgeline', 'Solace', 'Tidewater', 'Umber', 'Vesper', 'Willow'];
  var NAME_B = ['Mind', 'Sage', 'Guide', 'Beacon', 'Atlas', 'Compass', 'Herald', 'Warden',
                'Scribe', 'Pilot', 'Sentinel', 'Weaver', 'Oracle', 'Steward', 'Ranger', 'Clerk'];
  var NAME_C = ['Mix', 'Build', 'Forge', 'Blend', 'Assembly', 'Edition', 'Compound', 'Fusion'];

  function ri(rnd, a, b) { return a + Math.floor(rnd() * (b - a + 1)); }
  function pick(rnd, arr) { return arr[Math.floor(rnd() * arr.length)]; }
  function libById(id) {
    for (var i = 0; i < LIBS.length; i++) if (LIBS[i][0] === id) return LIBS[i];
    return null;
  }
  /* local FNV-1a hex (no dependency on load order) */
  function fnvHex(s) {
    var h = 2166136261;
    for (var i = 0; i < s.length; i++) { h ^= s.charCodeAt(i); h = Math.imul(h, 16777619); }
    return ('0000000' + (h >>> 0).toString(16)).slice(-8);
  }

  function pickLibs(rnd, profile) {
    var ids = [], i;
    if (profile === 'optimal') {
      for (i = 0; i < LIBS.length; i++) if (LIBS[i][4] === 1) ids.push(LIBS[i][0]);
    } else if (profile === 'maximal') {
      for (i = 0; i < LIBS.length; i++) ids.push(LIBS[i][0]);
    } else {
      var want = profile === 'minimal' ? 5 : 40;
      var pool = [];
      for (i = 0; i < LIBS.length; i++) pool.push(i);
      /* deterministic Fisher-Yates using only rnd */
      for (i = pool.length - 1; i > 0; i--) {
        var j = Math.floor(rnd() * (i + 1));
        var t = pool[i]; pool[i] = pool[j]; pool[j] = t;
      }
      for (i = 0; i < want && i < pool.length; i++) ids.push(LIBS[pool[i]][0]);
      ids.sort();
    }
    return ids;
  }

  function generate(seed, opts, rnd) {
    opts = opts || {};
    var profile = opts.type && PROFILES.indexOf(opts.type) >= 0 ? opts.type : pick(rnd, PROFILES);
    var engKey = rnd() < 0.7 ? 'v2' : 'v1';
    var engine = ENGINES[engKey];
    var libIds = pickLibs(rnd, profile);
    var sampling = {
      temperature: ri(rnd, 40, 90) / 100,
      topK: pick(rnd, [20, 40, 60]),
      maxTokens: pick(rnd, [64, 96, 120, 256]),
      stopAtEos: true
    };
    var name = pick(rnd, NAME_A) + ' ' + pick(rnd, NAME_B) + ' ' + pick(rnd, NAME_C);
    var libs = libIds.map(function (id) {
      var l = libById(id);
      return { id: id, name: l[1], version: l[2] };
    });
    var canonical = engKey + '|' + libIds.join(',') + '|' +
      sampling.temperature + '/' + sampling.topK + '/' + sampling.maxTokens + '|' + name;
    var n = (opts.baseN || 0) + 1;
    var rec = {
      id: ID_PREFIX + String(n).padStart(6, '0'),
      n: n,
      name: name,
      title: name + ' — ' + engine.name + ' ' + profile + ' mix',
      profile: profile,
      engine: { model_id: engine.model_id, name: engine.name, version: engine.version,
                params: engine.params, layers: engine.layers, heads: engine.heads,
                hidden: engine.hidden, status: engine.status },
      sampling: sampling,
      libraries: libs,
      library_count: libs.length,
      build_hash: fnvHex(canonical),
      mix_lineage: engine.model_id + ' + ' + libs.length + ' tool libraries (' + profile + ' profile)',
      note: 'GENERATED mix-and-match build assembled by the JAH Databases generator from the archive\'s real engine versions and tool libraries. Not a stored build.',
      stamp: STAMP,
      _engKey: engKey, _libIds: libIds, _sampling: sampling, _name: name, _profile: profile, _seed: seed
    };
    var pub = {};
    PUB_KEYS.forEach(function (k) { pub[k] = rec[k]; });
    pub._priv = rec;
    return pub;
  }

  /* independent verifier: rebuilds the build from its private parts */
  function verify(priv) {
    var errs = [];
    if (!ENGINES[priv._engKey]) return ['unknown engine key'];
    var engine = ENGINES[priv._engKey];
    if (priv.engine.model_id !== engine.model_id || priv.engine.params !== engine.params ||
        priv.engine.layers !== engine.layers)
      errs.push('engine spec mismatch');
    if (PROFILES.indexOf(priv._profile) < 0) errs.push('bad profile');
    /* every library id must be a real archived library */
    var seen = {};
    for (var i = 0; i < priv._libIds.length; i++) {
      var l = libById(priv._libIds[i]);
      if (!l) { errs.push('library not in archive index: ' + priv._libIds[i]); break; }
      if (seen[priv._libIds[i]]) { errs.push('duplicate library: ' + priv._libIds[i]); break; }
      seen[priv._libIds[i]] = 1;
    }
    /* public library cards must match the embedded index entries */
    if (priv.libraries.length !== priv._libIds.length) errs.push('library card count mismatch');
    else for (var k = 0; k < priv._libIds.length; k++) {
      var e = libById(priv._libIds[k]), c = priv.libraries[k];
      if (!e) { errs.push('library card for unknown id: ' + priv._libIds[k]); break; }
      if (!c || c.id !== e[0] || c.name !== e[1] || c.version !== e[2]) { errs.push('library card mismatch at ' + k); break; }
    }
    if (priv.library_count !== priv._libIds.length) errs.push('library_count mismatch');
    var s = priv._sampling;
    if (!(s.temperature >= 0.4 && s.temperature <= 0.9)) errs.push('temperature out of range');
    if ([20, 40, 60].indexOf(s.topK) < 0) errs.push('topK out of range');
    if ([64, 96, 120, 256].indexOf(s.maxTokens) < 0) errs.push('maxTokens out of range');
    if (priv.name !== priv._name) errs.push('name mismatch');
    var canonical = priv._engKey + '|' + priv._libIds.join(',') + '|' +
      s.temperature + '/' + s.topK + '/' + s.maxTokens + '|' + priv._name;
    if (priv.build_hash !== fnvHex(canonical)) errs.push('build hash mismatch');
    var wantTitle = priv._name + ' — ' + engine.name + ' ' + priv._profile + ' mix';
    if (priv.title !== wantTitle) errs.push('title mismatch');
    return errs;
  }

  function validate(rec) {
    var errs = [];
    if (!rec || typeof rec !== 'object') return { ok: false, errors: ['not an object'] };
    ['id', 'name', 'title', 'profile', 'engine', 'sampling', 'libraries', 'build_hash'].forEach(function (k) {
      if (rec[k] === undefined || rec[k] === null || rec[k] === '') errs.push('missing field: ' + k);
    });
    if (rec.id && !/^JAH-LLAMA-\d{6}$/.test(rec.id)) errs.push('bad id format');
    if (rec.profile && PROFILES.indexOf(rec.profile) < 0) errs.push('bad profile');
    if (!Array.isArray(rec.libraries) || rec.libraries.length === 0) errs.push('libraries must be a non-empty array');
    if (rec._priv) {
      var p = rec._priv;
      PUB_KEYS.forEach(function (k) {
        if (JSON.stringify(rec[k]) !== JSON.stringify(p[k])) errs.push('field diverged from verified copy: ' + k);
      });
      errs = errs.concat(verify(p));
    }
    else errs.push('no private build parts — cannot independently verify');
    return { ok: errs.length === 0, errors: errs };
  }

  function driftCheck(rec, archiveSample) {
    var errs = [];
    (archiveSample || []).forEach(function (a) {
      var h = a.build_hash || (a[2]);
      if (h && String(h) === String(rec.build_hash)) errs.push('duplicate of archived build hash');
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

  JAHDB.registerGenerator('llama', {
    version: VERSION,
    generate: generate,
    validate: validate,
    driftCheck: driftCheck,
    themedGenerate: themedGenerate,
    types: PROFILES
  });
})();
