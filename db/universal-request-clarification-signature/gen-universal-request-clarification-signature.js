(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["disambiguation", "slot-filling", "scoping", "confirmation", "budgeting"];
var PREFIX='JAH-URC-S-';
var USE="Used by conversational AI, support bots, and command interfaces to avoid acting on misunderstood requests.";
var FLD=[["strategy", "Strategy"], ["trigger", "Trigger"], ["outcome", "Outcome"]];
var DEMO="# {title} - slot completeness (python3)\nfilled={d1}\ntotal={d2}\nmin_ratio={d3}\nratio=filled/total\nprint(\"slots filled: %d/%d (%.0f%%)\" % (filled, total, ratio*100))\nprint(\"READY TO ACT\" if ratio >= min_ratio else \"ASK MORE\")\n";
var SIG=true;
var SRC="signature-generated-completion";
var B=[["disambiguation", "Slot Filling", "Asks for each missing required parameter in turn until the request is executable.", "Slot Filling", "missing parameters", "complete request", "4", "7", "0.8"], ["slot-filling", "Disambiguation Question", "Presents the top interpretations and asks the user to pick when confidence is split.", "Disambiguation Question", "multiple intents", "correct intent", "2", "2", "0.9"], ["scoping", "Example Offering", "Shows concrete examples of what the system can do to help the user phrase the request.", "Example Offering", "vague request", "grounded request", "1", "1", "1.0"], ["confirmation", "Scope Narrowing", "Asks whether the user means a subset (one file vs whole project) before a broad action.", "Scope Narrowing", "broad scope", "safe scope", "3", "4", "0.75"], ["budgeting", "Assumption Confirmation", "States the system's best-guess assumptions and asks for correction before acting.", "Assumption Confirmation", "risky action", "verified assumptions", "2", "3", "0.9"], ["disambiguation", "Multi-intent Splitting", "Detects two requests packed in one message and handles them as separate tasks.", "Multi-intent Splitting", "compound request", "both handled", "1", "2", "1.0"], ["slot-filling", "Preference Elicitation", "Asks about style, format, or depth preferences that change the answer shape.", "Preference Elicitation", "underspecified output", "tailored output", "2", "5", "0.6"], ["scoping", "Constraint Discovery", "Uncovers hidden constraints (budget, deadline, compatibility) that bound the solution.", "Constraint Discovery", "open-ended task", "feasible plan", "3", "6", "0.7"], ["confirmation", "Format Clarification", "Asks which output format the user wants when several are plausible.", "Format Clarification", "ambiguous format", "right format", "1", "3", "0.9"], ["budgeting", "Urgency Check", "Asks how urgent the request is to choose between fast approximate and slow thorough paths.", "Urgency Check", "time-sensitive", "right effort level", "1", "2", "1.0"], ["disambiguation", "Authority Verification", "Confirms the user is allowed to request the action before touching protected resources.", "Authority Verification", "protected resource", "authorized action", "2", "2", "1.0"], ["slot-filling", "Context Retrieval", "Pulls relevant history or files first, then asks only about what is still unclear.", "Context Retrieval", "partial context", "minimal questions", "3", "5", "0.8"], ["scoping", "Paraphrase Confirmation", "Restates the request in the system's own words and asks if it is right.", "Paraphrase Confirmation", "high stakes", "shared understanding", "1", "1", "1.0"], ["confirmation", "Partial Answer + Probe", "Answers the clear part immediately while asking about the unclear remainder.", "Partial Answer + Probe", "mixed clarity", "progress + clarity", "2", "4", "0.7"], ["budgeting", "Visual Reference Request", "Asks for a screenshot or photo when words cannot pin down the problem.", "Visual Reference Request", "visual problem", "see the issue", "1", "1", "1.0"], ["disambiguation", "Priority Ranking", "Asks the user to rank competing goals when they conflict.", "Priority Ranking", "conflicting goals", "clear priority", "2", "3", "0.9"], ["slot-filling", "Negative Clarification", "Asks what the user does NOT want, quickly ruling out whole solution families.", "Negative Clarification", "broad space", "narrowed space", "1", "4", "0.6"], ["scoping", "Time-boxed Clarification", "Limits clarifying questions to a budget (e.g. two) then proceeds with best guesses labeled.", "Time-boxed Clarification", "question fatigue", "bounded friction", "2", "2", "1.0"], ["confirmation", "Progressive Disclosure", "Asks one question at a time, using each answer to decide whether the next is needed.", "Progressive Disclosure", "complex forms", "low burden", "5", "8", "0.75"], ["budgeting", "Clarification Budget", "Tracks total questions asked and switches to assumptions-with-labels past the budget.", "Clarification Budget", "long sessions", "respectful flow", "6", "6", "1.0"]];
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
var gen={version:'jahdb-universal-request-clarification-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('universal-request-clarification-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
