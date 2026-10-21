(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["extractive-summary", "key-detail-preservation", "redundancy-removal", "budget-packing", "fidelity-check"];
var PREFIX='JAH-AT62S-';
var KIND_LIST=['method','algorithm','pattern','procedure'];
var VARIANTS=[" Foundational form: the core technique demonstrated on a minimal example.", " Compounded form: the technique combined with a second mechanism for harder cases.", " Production-hardened form: edge cases, failure modes, and operational safeguards included."];
var SIG=true;
var ARCH=[{"t": "Extractive summarization by term weight", "k": "algorithm", "d": "Signature original: Sentences are scored by the sum of their terms' frequencies across the whole input, a classic TF-based extractive method. The top-scoring sentences are kept in original order, which preserves narrative flow without any generation step. Extractive summaries never invent facts because every word comes verbatim from the source.", "demo": "from collections import Counter\ntext = 'The index is fast. The index uses posting lists. Posting lists map terms to documents. The scan is slow.'\nsents = text.split('. ')\ntf = Counter(text.lower().split())\nranked = sorted(sents, key=lambda s: sum(tf[w] for w in s.lower().split()), reverse=True)\nprint('kept:', ranked[0])\nprint('dropped:', ranked[-1])\n"}, {"t": "Critical-detail preservation list", "k": "method", "d": "Signature original: Before compression, a preservation list is built: numbers, dates, names, and identifiers found by pattern matching. Any sentence containing a preserved detail is protected from removal regardless of its term-weight score. This guarantees that the compressed context keeps the exact figures and names downstream reasoning depends on.", "demo": "import re\nsents = ['The archive is large.', 'It holds 52,268 databases as of 2026-10-21.', 'Growth is steady.']\nkeep = [s for s in sents if re.search(r'\\d[\\d,]*|\\d{4}-\\d{2}-\\d{2}', s)]\nprint('protected sentences:', keep)\n"}, {"t": "Redundancy removal via near-duplicate filter", "k": "algorithm", "d": "Signature original: Candidate sentences are compared pairwise with Jaccard similarity over word sets, and near-duplicates above 0.8 similarity are collapsed to the single highest-scoring one. Redundancy removal runs before budget packing so the token budget is spent on distinct information. The 0.8 threshold is tunable per database.", "demo": "def jacc(a, b):\n    A, B = set(a.split()), set(b.split())\n    return len(A & B) / len(A | B)\ns1 = 'the index uses posting lists for fast lookup'\ns2 = 'the index uses posting lists for quick lookup'\nprint('similarity:', round(jacc(s1, s2), 2), '-> collapse' if jacc(s1, s2) > 0.8 else '-> keep both')\n"}, {"t": "Budget packing under a token limit", "k": "algorithm", "d": "Signature original: Sentences are packed greedily by score-per-token until the token budget is exhausted, which is a knapsack-style selection that maximizes information per token. Protected critical-detail sentences are packed first, then the best remaining by efficiency. The result is the densest faithful context that fits the limit.", "demo": "sents = [('protected: 52,268 databases', 10, True), ('index is fast', 5, False), ('scan is slow', 4, False), ('posting lists map terms', 6, False)]\nbudget, out = 12, []\nfor text, tokens, prot in sorted(sents, key=lambda x: (x[2], x[1]), reverse=True):\n    if tokens <= budget: out.append(text); budget -= tokens\nprint('packed:', out, '| tokens left:', budget)\n"}, {"t": "Fidelity check of the compressed output", "k": "method", "d": "Signature original: After compression, fidelity is checked two ways: every preserved detail must appear verbatim in the output, and no sentence may appear that was not in the input. These two checks catch the two failure modes of compression, dropped facts and invented ones. A failed fidelity check falls back to a shorter extractive pass rather than shipping a lossy summary.", "demo": "src = ['holds 52,268 databases', 'index is fast', 'scan is slow']\nout = ['holds 52,268 databases', 'index is fast']\npreserved = ['52,268']\nprint('details kept:', all(any(p in s for s in out) for p in preserved))\nprint('no inventions:', all(any(o in s for s in src) for o in out))\n"}];
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
var gen={version:'jahdb-archive-tool-context-compression-engine-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('archive-tool-context-compression-engine-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
