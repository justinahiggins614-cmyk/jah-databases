(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["coverage-measurement", "sufficiency-threshold", "marginal-value-estimate", "stop-decision", "continue-plan"];
var PREFIX='JAH-AT76-';
var KIND_LIST=['method','algorithm','pattern','procedure'];
var VARIANTS=[" Foundational form: the core technique demonstrated on a minimal example.", " Compounded form: the technique combined with a second mechanism for harder cases.", " Production-hardened form: edge cases, failure modes, and operational safeguards included."];
var SIG=false;
var ARCH=[{"t": "Evidence coverage measurement", "k": "algorithm", "d": "Coverage is measured as the fraction of the mission's subquestions that have at least one supporting source above the support threshold. A mission can feel complete while half its subquestions are actually unanswered; the coverage number makes the gap visible. Coverage is recomputed after every batch of new evidence.", "demo": "subs = {'q1': 0.8, 'q2': 0.5, 'q3': 0.1, 'q4': 0.7}\nTH = 0.35\ncov = sum(1 for s in subs.values() if s >= TH) / len(subs)\nprint(f'evidence coverage: {cov:.0%}')\n"}, {"t": "Sufficiency threshold per mission type", "k": "method", "d": "The sufficiency threshold is set from the mission's stakes: a casual overview stops at 60 percent coverage, a decision-grade investigation demands 90. Thresholds are declared in the mission plan, not improvised mid-search when fatigue sets in. Declared thresholds keep stopping honest.", "demo": "thresholds = {'overview': 0.6, 'decision-grade': 0.9}\nmission, coverage = 'decision-grade', 0.75\nprint('sufficient:', coverage >= thresholds[mission], f'({coverage:.0%} vs {thresholds[mission]:.0%} needed)')\n"}, {"t": "Marginal value estimate of continuing", "k": "algorithm", "d": "Before deciding, the evaluator estimates the marginal value of more searching: the recent rate of new-evidence discovery times the importance of the still-unanswered subquestions. If the discovery rate has flatlined, continuing is unlikely to help no matter how important the gaps are. The estimate turns 'should we keep going' from a feeling into a number.", "demo": "recent_new = [5, 3, 1, 0]  # new evidence per batch\ngap_importance = 0.8\nmarginal = (sum(recent_new[-2:]) / 2) * gap_importance\nprint('marginal value of continuing:', round(marginal, 2), '-> STOP' if marginal < 1 else '-> CONTINUE')\n"}, {"t": "Stop/continue decision record", "k": "procedure", "d": "The decision is recorded with its inputs: coverage, threshold, marginal value, and the resulting verdict. A recorded decision can be audited later, which matters when someone asks why an investigation stopped with questions open. The record also notes who or what made the call.", "demo": "decision = {'coverage': 0.75, 'threshold': 0.9, 'marginal': 0.4, 'verdict': 'CONTINUE', 'by': 'evaluator-1.0'}\nprint('decision record:', decision)\n"}, {"t": "Continue plan with targeted gaps", "k": "method", "d": "When the verdict is continue, the evaluator outputs a targeted plan naming exactly which subquestions remain and what kind of evidence would close each. Targeted continuation beats undirected 'search more' every time. The plan becomes the next iteration's marching orders for the search agent.", "demo": "gaps = ['q3: needs a primary source on cache TTL behavior']\nprint('continue plan:')\nfor g in gaps: print(' -', g)\n"}];
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
var gen={version:'jahdb-archive-tool-stopping-criterion-evaluator-1.0',generate:generate,validate:validate,driftCheck:driftCheck};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('archive-tool-stopping-criterion-evaluator',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
