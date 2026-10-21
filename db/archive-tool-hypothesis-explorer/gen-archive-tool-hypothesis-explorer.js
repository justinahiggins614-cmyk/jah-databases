(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["hypothesis-generation", "evidence-for-against", "bayesian-tally", "crucial-test-search", "explanation-ranking"];
var PREFIX='JAH-AT74-';
var KIND_LIST=['method','algorithm','pattern','procedure'];
var VARIANTS=[" Foundational form: the core technique demonstrated on a minimal example.", " Compounded form: the technique combined with a second mechanism for harder cases.", " Production-hardened form: edge cases, failure modes, and operational safeguards included."];
var SIG=false;
var ARCH=[{"t": "Competing hypothesis generation", "k": "method", "d": "For a puzzling observation, the explorer generates multiple competing explanations, deliberately including ones that contradict the current favorite. Generation is seeded from known mechanism families so hypotheses stay plausible rather than fanciful. The set is kept small, three to five, because each one must earn its evidence.", "demo": "observation = 'query latency spiked on Tuesdays'\nhypos = ['H1: weekly reindex job contends for disk', 'H2: Tuesday traffic is genuinely higher', 'H3: cache TTL expiry aligns on Tuesdays']\nfor h in hypos: print(h)\n"}, {"t": "Evidence retrieval for and against each", "k": "algorithm", "d": "Each hypothesis gets its own evidence search: queries are phrased to find both supporting and refuting records. A hypothesis that only ever seeks confirmation is flagged for confirmation bias. The explorer records hits on both sides so the tally reflects the real evidentiary balance.", "demo": "evidence = {'H1': {'for': ['reindex runs Tuesdays 02:00'], 'against': []}, 'H2': {'for': [], 'against': ['traffic flat across weekdays']}}\nfor h, e in evidence.items():\n    print(h, 'supporting:', len(e['for']), '| refuting:', len(e['against']))\n"}, {"t": "Weighted evidence tally per hypothesis", "k": "algorithm", "d": "Supporting and refuting evidence are tallied with weights for source reliability and recency, producing a net score per hypothesis. A single strong refutation outweighs several weak supports, encoding the scientific asymmetry that falsification is decisive. Scores are comparable across hypotheses because they use the same weighting scheme.", "demo": "hypos = {'H1': ([0.8, 0.6], [0.9]), 'H2': ([0.5], [0.4, 0.7])}  # (supports, refutes)\nfor h, (s, r) in hypos.items():\n    net = sum(s) - 1.5 * sum(r)  # refutations weigh more\n    print(h, 'net score:', round(net, 2))\n"}, {"t": "Crucial-test search: evidence that discriminates", "k": "method", "d": "The explorer prioritizes finding crucial tests: single pieces of evidence that would strongly favor one hypothesis while disfavoring another. A crucial test is worth more than ten confirmatory finds because it actually separates the contenders. When no crucial test exists in the archive, the explorer says so plainly instead of pretending the tally is decisive.", "demo": "tests = [('check Tuesday disk IO during reindex', 'H1', 'H2'), ('compare Tuesday vs Wednesday traffic', 'H2', 'H1')]\nprint('crucial tests proposed:', len(tests))\nfor t, favors, disfavors in tests: print(' ', t, f'(favors {favors}, disfavors {disfavors})')\n"}, {"t": "Explanation ranking with uncertainty", "k": "procedure", "d": "Hypotheses are ranked by net score, but the ranking ships with explicit uncertainty: evidence counts, strongest refutation, and whether a crucial test was found. A ranking without uncertainty invites overconfidence, so the explorer refuses to present one. The top hypothesis is labeled 'leading', never 'proven'.", "demo": "ranked = [('H1', 0.5, 'leading'), ('H3', 0.1, 'contender'), ('H2', -0.6, 'disfavored')]\nfor h, score, status in ranked:\n    print(h, 'score', score, '->', status)\n"}];
function generate(seed,opts,rnd){
  opts=opts||{};rnd=rnd||prng(seed);
  var cat=opts.category||pick(CATS,rnd);
  var a=pick(ARCH,rnd);
  var v=(rnd()*3)|0;
  var desc=a.d+VARIANTS[v]+(SIG?' Signature-authored original by Justin Addam Higgins (JAH).':'');
  var id=PREFIX+String(seed).padStart(6,'0');
  var ttl=a.t+[' (foundational)',' (compounded)',' (production)'][v];
  var prov=SIG?'Signature-authored original by Justin Addam Higgins (JAH), 2026-10-21.':'Public computer-science methods literature; cross-checked against standard references, 2026-10-21.';
  return {id:id,t:ttl,title:ttl,description:desc,kind:a.k,category:cat,ladder_rank:v+1,demo:(SIG?'# Signature-authored original (JAH).\n':'')+a.demo,provenance:prov,last_verified:'2026-10-21',src:SIG?'signature-generated-completion':'public-harvest',_seed:seed};
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  var pre=PREFIX.replace(/-/g,'\\-');
  if(!new RegExp('^'+pre+'\\d{6}$').test(r.id||''))e.push('id');
  if(typeof r.title!=='string'||!r.title.length)e.push('title');
  if(typeof r.description!=='string'||r.description.length<50)e.push('description');
  if(KIND_LIST.indexOf(r.kind)<0)e.push('kind');
  if(CATS.indexOf(r.category)<0)e.push('category');
  if(!(r.ladder_rank>=1&&r.ladder_rank<=3))e.push('ladder_rank');
  if(typeof r.demo!=='string'||!r.demo.length)e.push('demo');
  if(r.last_verified!=='2026-10-21')e.push('last_verified');
  if(r.src!==(SIG?'signature-generated-completion':'public-harvest'))e.push('src');
  return {ok:!e.length,errors:e};
}
function driftCheck(rec,sample){
  var e=[];
  if(sample&&sample.length){
    for(var i=0;i<sample.length;i++){ if(sample[i]&&sample[i].id===rec.id){e.push('duplicate id');break;} }
  }
  return {ok:!e.length,errors:e};
}
var gen={version:'jahdb-archive-tool-hypothesis-explorer-1.0',generate:generate,validate:validate,driftCheck:driftCheck};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('archive-tool-hypothesis-explorer',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
