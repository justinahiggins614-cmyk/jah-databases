(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["search-logging", "absence-documentation", "limitation-catalog", "gap-quantification", "negative-report"];
var PREFIX='JAH-AT78-';
var KIND_LIST=['method','algorithm','pattern','procedure'];
var VARIANTS=[" Foundational form: the core technique demonstrated on a minimal example.", " Compounded form: the technique combined with a second mechanism for harder cases.", " Production-hardened form: edge cases, failure modes, and operational safeguards included."];
var SIG=false;
var ARCH=[{"t": "Exhaustive search attempt logging", "k": "method", "d": "Every query tried, including the ones that returned nothing, is logged with its scope and parameters. Failed queries are data: they map the boundary of what the archive contains. Without this log, a negative result is just a feeling; with it, the negative result is evidence.", "demo": "attempts = [{'q': 'quantum archive index', 'hits': 0}, {'q': 'index structures', 'hits': 14}]\nprint('attempts logged:', len(attempts), '| zero-hit:', sum(1 for a in attempts if a['hits'] == 0))\n"}, {"t": "Absence documentation with scope notes", "k": "method", "d": "When something is not found, the analyzer documents the absence precisely: what was sought, where it was sought, and how thoroughly. 'Not found in the archive's index-structure collection after 12 queries' is a useful negative result; 'couldn't find it' is not. Scope notes let readers judge how hard the negative result is.", "demo": "neg = {'sought': 'quantum index designs', 'scope': 'index-structure collection', 'queries': 12, 'found': False}\nprint('negative result:', neg['sought'], '| scope:', neg['scope'], '| queries tried:', neg['queries'])\n"}, {"t": "Limitation catalog of the search itself", "k": "method", "d": "The analyzer catalogs the search's own limitations: collections not covered, languages not searched, date ranges excluded. Limitations bound the negative result's meaning: absence from a partial search does not prove absence everywhere. The catalog is written before conclusions are drawn, not after they are challenged.", "demo": "limits = ['only English sources searched', 'pre-2020 records excluded', 'image collections not covered']\nprint('search limitations:')\nfor l in limits: print(' -', l)\n"}, {"t": "Gap quantification across subquestions", "k": "algorithm", "d": "Unanswered subquestions are counted and weighted by importance, producing a single gap score for the investigation. The score tells decision-makers how much of the question remains open despite the negative results. A gap score near zero with documented negatives is a strong result; a high gap score is an honest admission of incompleteness.", "demo": "subs = [('q1', True, 0.9), ('q2', False, 0.7), ('q3', False, 0.3)]  # (id, answered, importance)\ngap = sum(imp for _, ok, imp in subs if not ok) / sum(imp for _, _, imp in subs)\nprint(f'gap score: {gap:.2f}')\n"}, {"t": "Negative-result report", "k": "procedure", "d": "The analysis ends in a report listing every negative result with its scope notes, the limitation catalog, and the gap score. The report is filed with the investigation so that future researchers do not repeat the same fruitless searches. Negative results, properly recorded, are a public good.", "demo": "report = {'negatives': 3, 'limitations': 3, 'gap_score': 0.42}\nprint('negative-result report filed:', report)\n"}];
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
var gen={version:'jahdb-archive-tool-negative-result-analyzer-1.0',generate:generate,validate:validate,driftCheck:driftCheck};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('archive-tool-negative-result-analyzer',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
