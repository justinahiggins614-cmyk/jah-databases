/* ✳ SIGNATURE — JAH Spelling Data Base generator. Property of Justin Addam Higgins (JAH).
   Boundless generator: produces NEW spelling records in the archive's style —
   real words drawn from the archive word list, each paired with a genuine
   misspelling produced by a mechanical edit operation (adjacent transposition,
   letter doubling, letter drop). Deterministic: same seed + version => same
   record. An INDEPENDENT verifier re-applies the operation to the word and
   requires the exact misspelling before acceptance. */
(function () {
  'use strict';
  var VERSION = 'jahdb-spelling-1.0';
  var ID_PREFIX = 'JAH-SPELL-';

  function ri(rnd, a, b) { return a + Math.floor(rnd() * (b - a + 1)); }
  function pick(rnd, arr) { return arr[Math.floor(rnd() * arr.length)]; }

  /* real words sampled from the archive words.txt (10 per letter, A-Z) */
  var WORDS = ["acetous","applicancy","adieu","absinthium","allochroic","ascribable","ammonic","avatar","authorized","astride","belle","barbaric","bolsa","beloved","brute","bridgey","breeziness","birthplace","barong","bepelt","crimpy","conspire","champion","cedar","cacochymy","corrivalry","coercion","conchite","cric","chironomy","diterebene","delay","dubious","deportment","dicyemata","dragnet","drumly","demiman","dehiscent","draftsman","ephemerous","encourage","ekename","elecampane","edenic","extender","eccritic","eolian","endorse","epistolize","friar","factious","fougade","forewarn","fellowly","flimsy","fibrin","fumigate","foreby","filling","gravidated","glacious","gargantuan","grating","glossology","gneissose","gowl","gorgoneion","gorgonize","gizzard","homilist","hoarseness","hake","hydrolytic","haltingly","howdy","horseworm","homotypy","headway","hygieist","intext","isonandra","inthirst","inlay","itala","insurance","inferrible","inwit","incitation","ignitible","jehad","jingler","jaculate","jarvy","jetton","jansenism","jezebel","judahite","joggle","jumper","krait","knubs","khenna","kneadable","kame","knappish","knurled","kevin","kabob","kokama","logogram","lentor","lighthouse","looseness","lithoidal","liberate","lineally","lisper","lacwork","limpidity","mexicanize","meropodite","midday","moonset","myops","mendacious","monodelph","manualist","moonbeam","maltose","nitrosyl","nervosity","numerative","nephilim","neurility","newcome","norimon","nitranilic","nylgau","nicolaitan","outermost","opaque","oscines","ossuarium","omelet","outvie","ochraceous","ovotesttis","orthopedic","outblown","pettifog","piciform","packing","proatlas","product","pulverate","pontee","pung","purpure","patentable","quintuplet","quarreling","quiet","quob","quitrent","quantify","quindism","question","quartridge","quadrature","reviewal","refinement","refret","routinary","ridable","ralstonite","reame","rotalite","regarding","ripienist","sphacelus","sandglass","southernly","siliginose","soss","spirillum","spicous","scienter","spicery","slapjack","tinsel","thundering","tagnicate","turgent","theatric","tabulate","triviality","tyfoon","therewhile","trait","upcoil","underjoin","upbreed","unable","univalved","unrivet","urceole","uncertain","undock","umbrage","visual","vesiculous","vitriolic","vulpic","varsity","verminate","vertebrate","vadium","voluta","volunteer","whit","wrymouth","wireless","winterly","weber","walaway","workship","waur","wendish","welkin","xylitone","xylate","xystus","xylorcin","xylophagan","xyloidin","xeronic","xanthopous","xylylene","xeriff","yeman","ythrowe","ymaked","yautia","yearningly","youngthly","yestereve","yend","yakoots","yokelet","zephyr","zoophytic","zither","zooecyst","zoophite","zoonic","zibet","zymogen","zamindari","zeuzerian"];
  var WORDSET = {};
  WORDS.forEach(function (w) { WORDSET[w] = 1; });

  /* mechanical edit operations; each is exactly reversible for verification */
  var OPS = {
    transpose: {
      rule: 'transposed adjacent letters',
      valid: function (w) { return w.length >= 2; },
      apply: function (w, pos) {
        var i = pos % (w.length - 1);
        if (w[i] === w[i + 1]) i = (i + 1) % (w.length - 1);
        return { out: w.slice(0, i) + w[i + 1] + w[i] + w.slice(i + 2), pos: i };
      }
    },
    double: {
      rule: 'doubled a letter',
      valid: function (w) { return w.length >= 2 && w.length <= 9; },
      apply: function (w, pos) {
        var i = pos % w.length;
        return { out: w.slice(0, i + 1) + w[i] + w.slice(i + 1), pos: i };
      }
    },
    drop: {
      rule: 'dropped a letter',
      valid: function (w) { return w.length >= 5; },
      apply: function (w, pos) {
        var i = 1 + (pos % (w.length - 2));
        return { out: w.slice(0, i) + w.slice(i + 1), pos: i };
      }
    }
  };
  var OPNAMES = Object.keys(OPS);

  function generate(seed, opts, rnd) {
    opts = opts || {};
    var word = opts.word && WORDSET[opts.word] ? opts.word : pick(rnd, WORDS);
    var opName = opts.op && OPS[opts.op] && OPS[opts.op].valid(word) ? opts.op : pick(rnd, OPNAMES.filter(function (o) { return OPS[o].valid(word); }));
    var op = OPS[opName];
    var pos = ri(rnd, 0, 999);
    var r = op.apply(word, pos);
    var n = (opts.baseN || 0) + 1 + (opts.seq || 0);
    var rec = {
      id: ID_PREFIX + String(n).padStart(6, '0'),
      n: n,
      word: word,
      misspelling: r.out,
      op: opName,
      rule: op.rule,
      letter: word.charAt(0).toUpperCase()
    };
    var pub = {};
    ['id', 'n', 'word', 'misspelling', 'op', 'rule', 'letter'].forEach(function (k) { pub[k] = rec[k]; });
    pub._priv = { word: word, op: opName, pos: pos, ipos: r.pos, out: r.out };
    return pub;
  }

  /* independent re-verification: re-apply the op to the word from scratch */
  function verify(rec) {
    var errs = [];
    var p = rec._priv;
    if (!WORDSET[p.word]) errs.push('word is not in the archive word sample');
    if (p.word !== rec.word) errs.push('word mismatch');
    if (!OPS[p.op]) errs.push('unknown op ' + p.op);
    else {
      var r = OPS[p.op].apply(p.word, p.pos);
      if (r.out !== rec.misspelling) errs.push('misspelling does not match re-applied operation');
      if (r.pos !== p.ipos) errs.push('op position mismatch');
    }
    if (rec.misspelling === rec.word) errs.push('misspelling equals the word');
    if (rec.rule !== OPS[rec.op].rule) errs.push('rule text mismatch');
    if (rec.letter !== rec.word.charAt(0).toUpperCase()) errs.push('letter mismatch');
    return errs;
  }

  function validate(rec) {
    var errs = [];
    if (!rec || typeof rec !== 'object') return { ok: false, errors: ['not an object'] };
    ['id', 'word', 'misspelling', 'op', 'rule', 'letter'].forEach(function (k) {
      if (rec[k] === undefined || rec[k] === null || rec[k] === '') errs.push('missing field: ' + k);
    });
    if (rec.id && !/^JAH-SPELL-\d{6}$/.test(rec.id)) errs.push('bad id format');
    if (rec.op && OPNAMES.indexOf(rec.op) < 0) errs.push('bad op');
    if (rec._priv) errs = errs.concat(verify(rec));
    else errs.push('no private params — cannot independently verify');
    return { ok: errs.length === 0, errors: errs };
  }

  /* drift: a generated "misspelling" must not itself be a real archive word,
     and the pair must not repeat */
  function driftCheck(rec, archiveSample) {
    var errs = [];
    (archiveSample || []).forEach(function (a) {
      var w = typeof a === 'string' ? a : (a.word || a.w);
      if (w && String(w).toLowerCase() === String(rec.misspelling).toLowerCase())
        errs.push('misspelling is itself a real archive word: ' + rec.misspelling);
      if (a.word && a.misspelling && a.word === rec.word && a.misspelling === rec.misspelling)
        errs.push('duplicate spelling record');
    });
    return { ok: errs.length === 0, errors: errs };
  }

  function themedGenerate(seed, opts, rnd, themeSamples) {
    var rec = generate(seed, opts, rnd);
    if (themeSamples && themeSamples.length) {
      var t = themeSamples[Math.floor(rnd() * themeSamples.length)];
      var words = String(JSON.stringify(t)).match(/[A-Za-z]{4,10}/g);
      if (words && words.length) {
        var w = words[parseInt(words[0].length, 10) % words.length].toLowerCase();
        if (WORDSET[w]) {
          var rec2 = generate(seed, { baseN: opts.baseN, word: w }, JAHDB.prng(JAHDB.hashStr(String(seed) + w)));
          rec2.id = rec.id; rec2.n = rec.n;
          return rec2;
        }
      }
    }
    return rec;
  }

  JAHDB.registerGenerator('spelling', {
    version: VERSION,
    generate: generate,
    validate: validate,
    driftCheck: driftCheck,
    themedGenerate: themedGenerate,
    ops: OPNAMES
  });
})();
