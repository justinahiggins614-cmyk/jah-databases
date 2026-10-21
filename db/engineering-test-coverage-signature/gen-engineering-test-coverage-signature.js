(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["code", "requirements", "faults", "integration", "system"];
var PREFIX='JAH-ETC-S-';
var USE="Used by test engineers and safety assessors to argue that testing was sufficient.";
var FLD=[["metric", "Metric"], ["measures", "Measures"], ["target", "Target"]];
var DEMO="# {title} - coverage check (python3)\ncovered={d1}\ntotal={d2}\ntarget={d3}\npct=100.0*covered/total\nprint(\"coverage: %.1f%% (%d/%d)\" % (pct, covered, total))\nprint(\"TARGET MET\" if pct >= target else \"MORE TESTS NEEDED\")\n";
var SIG=true;
var SRC="signature-generated-completion";
var B=[["code", "Line Coverage", "Fraction of executable lines run at least once by the test suite.", "Line Coverage", "lines executed", "80%", "820", "1000", "80.0"], ["requirements", "Branch Coverage", "Fraction of branch outcomes (true/false) exercised.", "Branch Coverage", "decisions", "75%", "150", "200", "75.0"], ["faults", "Function Coverage", "Fraction of functions or methods called at least once.", "Function Coverage", "functions", "90%", "270", "300", "90.0"], ["integration", "Statement Coverage", "Fraction of statements executed; the weakest useful metric.", "Statement Coverage", "statements", "80%", "1600", "2000", "80.0"], ["system", "MC/DC", "Modified condition/decision coverage: each condition shown to independently affect the outcome.", "MC/DC", "logic", "100% (avionics)", "45", "45", "100.0"], ["code", "Condition Coverage", "Each boolean sub-condition evaluated both true and false.", "Condition Coverage", "conditions", "100%", "120", "120", "100.0"], ["requirements", "Path Coverage", "Distinct execution paths through the code; complete coverage is usually infeasible.", "Path Coverage", "paths", "critical paths", "38", "50", "70.0"], ["faults", "Requirement Coverage", "Fraction of requirements with at least one linked passing test.", "Requirement Coverage", "requirements", "100%", "210", "210", "100.0"], ["integration", "Mutation Score", "Fraction of seeded faults (mutants) the tests catch.", "Mutation Score", "test strength", "85%", "170", "200", "85.0"], ["system", "Boundary Coverage", "Tests at and around input boundaries where bugs cluster.", "Boundary Coverage", "edges", "100% of boundaries", "96", "96", "100.0"], ["code", "Equivalence Partition", "One representative test per input class instead of exhaustive values.", "Equivalence Partition", "classes", "all partitions", "60", "60", "100.0"], ["requirements", "State Coverage", "States of state machines visited during testing.", "State Coverage", "states", "100%", "24", "24", "100.0"], ["faults", "Transition Coverage", "State transitions exercised, including illegal ones that must be rejected.", "Transition Coverage", "transitions", "100%", "58", "58", "100.0"], ["integration", "API Coverage", "Endpoints and methods exercised with valid and invalid inputs.", "API Coverage", "API surface", "95%", "190", "200", "95.0"], ["system", "Integration Coverage", "Interfaces between components tested in combination.", "Integration Coverage", "interfaces", "90%", "45", "50", "90.0"], ["code", "Fault Coverage", "Injected faults detected or handled correctly.", "Fault Coverage", "dependability", "90%", "135", "150", "90.0"], ["requirements", "Timing Coverage", "Worst-case execution paths measured under load.", "Timing Coverage", "deadlines", "100% critical", "30", "30", "100.0"], ["faults", "Resource Coverage", "Peak memory, handles, and connections exercised.", "Resource Coverage", "resources", "no leaks", "48", "50", "95.0"], ["integration", "Concurrency Coverage", "Thread interleavings and race windows explored.", "Concurrency Coverage", "races", "known races", "22", "25", "85.0"], ["system", "Negative-test Coverage", "Invalid, malformed, and hostile inputs tested for safe rejection.", "Negative-test Coverage", "robustness", "all abuse cases", "140", "150", "90.0"]];
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
var gen={version:'jahdb-engineering-test-coverage-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('engineering-test-coverage-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
