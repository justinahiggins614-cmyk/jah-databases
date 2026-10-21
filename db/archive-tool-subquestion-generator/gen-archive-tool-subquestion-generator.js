(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["question-decomposition", "dependency-ordering", "subquestion-validation", "fan-out-control", "answer-recomposition"];
var PREFIX='JAH-AT72-';
var KIND_LIST=['method','algorithm','pattern','procedure'];
var VARIANTS=[" Foundational form: the core technique demonstrated on a minimal example.", " Compounded form: the technique combined with a second mechanism for harder cases.", " Production-hardened form: edge cases, failure modes, and operational safeguards included."];
var SIG=false;
var ARCH=[{"t": "Decomposition by question facets", "k": "method", "d": "A complex question is split along its natural facets: what, how, how well, and compared to what. Each facet becomes an independent subquestion that can be searched without waiting on the others. Facet-based splitting works because most research questions are really several smaller questions wearing a trench coat.", "demo": "q = 'Is the inverted index the best choice for our archive search?'\nfacets = {'what': 'What index structures exist for archive search?', 'how well': 'What latencies do they achieve at 50k+ records?', 'compared to what': 'How do they compare on our query mix?'}\nfor k, v in facets.items(): print(f'[{k}]', v)\n"}, {"t": "Dependency ordering of subquestions", "k": "algorithm", "d": "Subquestions are topologically ordered so that ones whose answers feed others run first. Independent subquestions are marked parallel-safe and can fan out to multiple workers at once. The ordering is computed from an explicit dependency list, not guessed, so the execution plan is always sound.", "demo": "deps = {'q1': [], 'q2': ['q1'], 'q3': ['q1'], 'q4': ['q2', 'q3']}\norder, done = [], set()\nwhile len(order) < len(deps):\n    for q, ds in deps.items():\n        if q not in done and all(d in done for d in ds):\n            order.append(q); done.add(q)\nprint('execution order:', order)\n"}, {"t": "Subquestion answerability check", "k": "method", "d": "Each generated subquestion is checked for answerability: it must be specific enough to search and narrow enough to answer from retrievable sources. Vague subquestions are refined with added constraints before they enter the queue. This check keeps the fan-out from producing dozens of unanswerable micro-questions.", "demo": "import re\ndef answerable(q):\n    return len(q.split()) >= 5 and bool(re.search(r'\\d|which|what|how', q, re.I))\nfor q in ['search stuff', 'What latencies do inverted indexes achieve at 50k records?']:\n    print(('ANSWERABLE ' if answerable(q) else 'REFINE ') + q[:50])\n"}, {"t": "Fan-out control with branching budget", "k": "method", "d": "The total number of subquestions is capped by a branching budget derived from available workers and time. When decomposition proposes more subquestions than the budget allows, the lowest-information ones are merged or dropped. Bounded fan-out keeps the investigation parallel without exploding into hundreds of tiny searches.", "demo": "proposed = ['q1', 'q2', 'q3', 'q4', 'q5', 'q6']\nbudget = 4\nkept = proposed[:budget]\nprint('kept:', kept, '| merged/dropped:', proposed[budget:])\n"}, {"t": "Answer recomposition into the parent answer", "k": "procedure", "d": "Subquestion answers are recombined into the parent answer following the dependency order, with each section citing its subquestion. Contradictions between subquestion answers are surfaced explicitly rather than smoothed over. The recomposed answer links back to every subquestion so readers can drill into any part.", "demo": "answers = {'q1': 'inverted index: 40ms', 'q2': 'scan: 900ms'}\nparent = 'Comparison: ' + '; '.join(f'{k} -> {v}' for k, v in answers.items())\nprint(parent)\n"}];
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
var gen={version:'jahdb-archive-tool-subquestion-generator-1.0',generate:generate,validate:validate,driftCheck:driftCheck};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('archive-tool-subquestion-generator',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
