(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["exact", "heuristic", "statistical", "differential", "human"];
var PREFIX='JAH-AATO-S-';
var USE="Used by QA automation teams to get trustworthy verdicts without manual checking.";
var FLD=[["oracle", "Oracle"], ["decides", "Decides"], ["strength", "Strength"]];
var DEMO="# {title} - verdict (python3)\npassed_={d1}\ntotal={d2}\nthresh={d3}\npct=100.0*passed_/total\nprint(\"pass rate: %.1f%%\" % pct)\nprint(\"ACCEPT\" if pct >= thresh else \"REJECT\")\n";
var SIG=true;
var SRC="signature-generated-completion";
var B=[["exact", "True Oracle", "Compares against a known-correct implementation; the gold standard when available.", "True Oracle", "correctness", "definitive", "95", "100", "90.0"], ["heuristic", "Human Oracle", "A person judges the output, used for subjective quality like design.", "Human Oracle", "taste", "authoritative", "18", "20", "85.0"], ["statistical", "Heuristic Oracle", "Applies rules of thumb (no NaNs, ranges sane) that catch obvious failures cheaply.", "Heuristic Oracle", "sanity", "cheap", "180", "200", "85.0"], ["differential", "Metamorphic Relation", "Checks that known input transformations produce predictable output changes.", "Metamorphic Relation", "consistency", "no oracle needed", "140", "150", "90.0"], ["human", "Statistical Oracle", "Accepts outputs within learned distributions instead of exact matches.", "Statistical Oracle", "plausibility", "tolerant", "880", "1000", "85.0"], ["exact", "Differential Oracle", "Compares two implementations of the same spec and flags disagreements.", "Differential Oracle", "equivalence", "finds subtle bugs", "96", "100", "95.0"], ["heuristic", "Model-based Oracle", "Derives expected behavior from a formal or executable model.", "Model-based Oracle", "spec conformance", "rigorous", "190", "200", "95.0"], ["statistical", "Invariant Checker", "Asserts properties that must always hold (sorted output, conserved totals).", "Invariant Checker", "invariants", "always on", "495", "500", "99.0"], ["differential", "Property-based Oracle", "Generates random inputs and checks universal properties hold.", "Property-based Oracle", "generality", "broad", "920", "1000", "90.0"], ["human", "Regression Golden", "Compares against recorded golden outputs from a known-good version.", "Regression Golden", "no regression", "sensitive", "1180", "1200", "98.0"], ["exact", "Threshold Oracle", "Passes when a metric crosses a tuned threshold.", "Threshold Oracle", "good enough", "simple", "85", "100", "80.0"], ["heuristic", "Consensus Oracle", "Takes the majority verdict of several independent oracles.", "Consensus Oracle", "robustness", "fault tolerant", "97", "100", "95.0"], ["statistical", "Simulation Oracle", "Compares the real system against a high-fidelity simulator.", "Simulation Oracle", "fidelity", "grounded", "180", "200", "90.0"], ["differential", "Sampling Oracle", "Checks a random sample deeply instead of everything shallowly.", "Sampling Oracle", "efficiency", "scalable", "190", "200", "95.0"], ["human", "Partial Oracle", "Verifies checkable aspects and explicitly marks the rest unverified.", "Partial Oracle", "honesty", "no false confidence", "150", "200", "70.0"], ["exact", "Implicit Oracle", "Treats crashes, hangs, and exceptions as failures with no expected output needed.", "Implicit Oracle", "robustness", "zero setup", "990", "1000", "99.0"], ["heuristic", "Performance Oracle", "Fails when latency or throughput regress beyond the budget.", "Performance Oracle", "speed", "guards SLAs", "92", "100", "90.0"], ["statistical", "Visual Diff Oracle", "Compares rendered screenshots pixel-wise with tolerance masks.", "Visual Diff Oracle", "UI correctness", "catches visual bugs", "470", "500", "94.0"], ["differential", "LLM-judge Oracle", "Uses a language model with a rubric to grade open-ended outputs.", "LLM-judge Oracle", "quality", "scalable judgment", "82", "100", "80.0"], ["human", "Formal Specification Oracle", "Checks outputs against machine-checked specifications.", "Formal Specification Oracle", "correctness", "strongest", "99", "100", "99.0"]];
function buildTitle(b){ return SIG?('Signature '+b[1]):b[1]; }
function buildDesc(b){
  var d=b[2]+' Recorded facts \u2014 '+FLD[0][1]+': '+b[3]+'; '+FLD[1][1]+': '+b[4]+'; '+FLD[2][1]+': '+b[5]+'. '+USE;
  if(SIG) d='Signature-original: '+d+' Built as a Signature-authored original for the JAH network; clearly labeled Signature and never presented as a public record.';
  return d;
}
function buildDemo(b){
  return DEMO.split('{title}').join(b[1]).split('{d1}').join(b[6]).split('{d2}').join(b[7]).split('{d3}').join(b[8]);
}
function generate(seed,opts){
  opts=opts||{}; var rnd=prng(seed);
  var cat=opts.category||pick(CATS,rnd);
  var pool=B.filter(function(b){return b[0]===cat;});
  var b=pick(pool.length?pool:B,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  var title=buildTitle(b);
  var fields={}; fields[FLD[0][0]]=b[3]; fields[FLD[1][0]]=b[4]; fields[FLD[2][0]]=b[5];
  if(SIG) fields['signature_label']='Signature-authored original';
  return {id:id,title:title,description:buildDesc(b),category:cat,fields:fields,
    ladder_rank:1+(seed%3),
    demo:'# '+title+' \u2014 runnable demo (python3)\n'+buildDemo(b),
    provenance:'JAH Databases \u00b7 lane N3 build',last_verified:'2026-10-21',src:SRC,_seed:seed};
}
function driftCheck(rec,sample){
  sample=sample||[];
  for(var i=0;i<sample.length;i++){
    if(sample[i]&&sample[i].title===rec.title&&sample[i].category===rec.category)
      return {ok:false,errors:['duplicate of archive record '+sample[i].id]};
  }
  return {ok:true,errors:[]};
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  var idre=new RegExp('^'+PREFIX.replace(/[.*+?^${}()|[\]\\]/g,'\\$&')+'\\d{6}$');
  if(!idre.test(r.id||''))e.push('id');
  if(typeof r.title!=='string'||!r.title.length)e.push('title');
  if(typeof r.description!=='string'||r.description.length<40)e.push('description');
  if(CATS.indexOf(r.category)<0)e.push('category');
  if(!(r.ladder_rank>=1&&r.ladder_rank<=3))e.push('ladder_rank');
  if(typeof r.demo!=='string'||r.demo.indexOf('print(')<0)e.push('demo');
  if(['public-harvest','signature-generated-completion'].indexOf(r.src)<0)e.push('src');
  if(r.last_verified!=='2026-10-21')e.push('last_verified');
  return {ok:!e.length,errors:e};
}
var gen={version:'jahdb-automated-acceptance-test-oracle-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('automated-acceptance-test-oracle-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
