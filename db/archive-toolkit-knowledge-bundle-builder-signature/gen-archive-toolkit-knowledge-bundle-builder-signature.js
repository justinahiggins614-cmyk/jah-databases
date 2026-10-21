(function(){'use strict';
var PREFIX="JAH-ATK217S-";
var METHODS=[["Seed-based collection", "Start from seed documents and expand along citation, dependency, and 'see also' edges to a bounded depth."], ["Reading-order curation", "Order the bundle foundations-first so a newcomer meets prerequisites before advanced material."], ["Dependency inclusion", "Pull in every dependency of every included item so the bundle is self-sufficient offline."], ["Evidence grading", "Label each item as primary evidence, supporting material, or background so readers weight them correctly."], ["Glossary generation", "Extract key terms across the bundle into a unified glossary with per-term definitions."], ["Contradiction flagging", "When bundled sources disagree, surface the disagreement explicitly instead of hiding it."], ["Runnable example inclusion", "Attach runnable demos for procedural items so the bundle teaches by doing."], ["Bundle completeness check", "Verify every internal reference resolves inside the bundle; report dangling links."], ["Audience tailoring", "Generate beginner, practitioner, and expert variants from the same collection by filtering depth."], ["Update subscriptions", "Let readers subscribe to a bundle topic and receive curated additions as the archive grows."], ["Bundle diffing", "Show what changed between bundle versions so returning readers catch up fast."], ["Licensing clearance", "Check every item's license for redistribution and exclude or summarize what cannot ship."], ["Multilingual bundles", "Include translations or summaries so the bundle serves readers across languages."], ["Assessment inclusion", "Add self-test questions per section so readers verify understanding as they go."], ["Bundle metrics", "Track completion and quiz scores to measure whether bundles actually teach."]];
var CATS=["bundling", "curation", "packaging"];
var DEMO="# Knowledge Bundle Builder demo: seed expansion with reading order + completeness check.\nGRAPH={\"intro\":[\"basics\"],\"basics\":[\"advanced\",\"glossary\"],\"advanced\":[],\"glossary\":[]}\nDEPTH={\"intro\":0,\"basics\":1,\"advanced\":2,\"glossary\":2}\ndef collect(seed,max_depth=2):\n    seen={}; stack=[(seed,0)]\n    while stack:\n        n,d=stack.pop()\n        if n in seen or d>max_depth: continue\n        seen[n]=d; stack.extend((m,d+1) for m in GRAPH.get(n,[]))\n    return sorted(seen,key=lambda n:(seen[n],n))\nbundle=collect(\"intro\")\nprint(\"bundle reading order:\",bundle)\ndangling=[m for n in bundle for m in GRAPH.get(n,[]) if m not in bundle]\nprint(\"dangling references:\",dangling or \"none - bundle complete\")\n";
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function generate(seed,opts){
  opts=opts||{};var rnd=prng(seed);
  var idx=(seed-1)%METHODS.length;var m=METHODS[idx];
  var cat=opts.category||CATS[(rnd()*CATS.length)|0];
  var id=PREFIX+String(1000+((seed-1)%9000));
  var title=m[0]+' \u2014 '+"Knowledge Bundle Builder (Signature)";
  return {id:id,t:title,title:title,description:"Signature edition. The knowledge bundle builder assembles everything a human or agent needs to truly understand a topic: the core documents, their dependencies, cited references, supporting evidence, glossaries, and runnable examples \u2014 in one package with a guided reading order. Where the snapshot packager freezes a moment, the bundle builder curates a subject. It is the difference between handing someone a box of p",
    kind:"delivery tool",category:cat,ladder_rank:1+((seed-1)%3),demo:DEMO,
    provenance:"Signature-generated-completion",last_verified:'2026-10-21',src:"signature-generated-completion",_seed:seed};
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(typeof r.id!=='string'||r.id.indexOf(PREFIX)!==0)e.push('id');
  if(typeof r.title!=='string'||!r.title.length)e.push('title');
  if(typeof r.description!=='string'||r.description.length<100)e.push('description');
  if(CATS.indexOf(r.category)<0)e.push('category');
  if(!(r.ladder_rank>=1&&r.ladder_rank<=3))e.push('ladder_rank');
  if(typeof r.demo!=='string'||r.demo.indexOf('print(')<0)e.push('demo');
  if(r.src!=="signature-generated-completion")e.push('src');
  return {ok:!e.length,errors:e};
}
var gen={version:"jahdb-archive-toolkit-knowledge-bundle-builder-signature-1.0",generate:generate,validate:validate};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("archive-toolkit-knowledge-bundle-builder-signature",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();