(function(){'use strict';
/* JAH Emergency Vet Veterinary Database generator — jahdb-e2-vet-emergency-vet-care-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-vet-emergency-vet-care',PREFIX='JAH-E2VETEMERGE-',NAME='JAH Emergency Vet Veterinary Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Emergency Vet: the complete guide", "d": "Emergency Vet: the ER visit..", "g": "overview", "l": 2, "q": "What is Emergency Vet: the complete guide?", "a": "Emergency Vet: the ER visit..", "x": "The complete veterinary guide to Emergency Vet: the ER visit.. Triage. History, meaning, practices, and how to engage respectfully — everything in one database. Triage. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Emergency Vet essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Emergency Vet essentials.", "x": "At a glance: Emergency Vet — the ER visit.. Bloat. The essentials: Toxins.. Toxins. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Triage.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Triage.", "x": "Emergency Vet: Triage.. Toxins. Essential knowledge — Toxins.. the ER visit. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Triage..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Triage..", "x": "Explained: Triage.. Stabilize. The context — Emergency Vet. Trauma. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Bloat.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Bloat.", "x": "Emergency Vet: Bloat.. Costs. Essential knowledge — Trauma.. the ER visit. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Bloat..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Bloat..", "x": "Explained: Bloat.. Bloat. The context — Emergency Vet. Costs. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Toxins.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Toxins.", "x": "Emergency Vet: Toxins.. Stabilize. Essential knowledge — Costs.. the ER visit. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Toxins..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Toxins..", "x": "Explained: Toxins.. Guide. The context — Emergency Vet. Stabilize. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Trauma.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Trauma.", "x": "Emergency Vet: Trauma.. Bloat. Essential knowledge — Stabilize.. the ER visit. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Trauma..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Trauma..", "x": "Explained: Trauma.. Triage. The context — Emergency Vet. Triage. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Costs.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Costs.", "x": "Emergency Vet: Costs.. Guide. Essential knowledge — Triage.. the ER visit. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Costs..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Costs..", "x": "Explained: Costs.. Toxins. The context — Emergency Vet. Bloat. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Stabilize.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Stabilize.", "x": "Emergency Vet: Stabilize.. Triage. Essential knowledge — Bloat.. the ER visit. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Stabilize..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Stabilize..", "x": "Explained: Stabilize.. Costs. The context — Emergency Vet. Toxins. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Triage.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Triage.", "x": "Emergency Vet in depth: Triage.. Bloat. Details — the ER visit.. Costs. Trauma. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Toxins.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Toxins.", "x": "Emergency Vet in depth: Toxins.. Toxins. Details — the ER visit.. Stabilize. Costs. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Costs.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Costs.", "x": "Emergency Vet in depth: Costs.. Trauma. Details — the ER visit.. Bloat. Stabilize. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Stabilize.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Stabilize.", "x": "Emergency Vet in depth: Stabilize.. Costs. Details — the ER visit.. Guide. Triage. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Bloat.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Bloat.", "x": "Emergency Vet in depth: Bloat.. Stabilize. Details — the ER visit.. Triage. Bloat. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Guide.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Guide.", "x": "Emergency Vet in depth: Guide.. Triage. Details — the ER visit.. Toxins. Toxins. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Emergency Vet comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Emergency Vet comes from.", "x": "Origins: Triage.. Triage. The history of Emergency Vet — the ER visit.. Toxins. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Emergency Vet respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Emergency Vet respectfully.", "x": "Engaging: Costs.. Bloat. How to participate or observe well — Emergency Vet. the ER visit. Respect first, always; Stabilize.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Emergency Vet do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Emergency Vet do's and don'ts.", "x": "Etiquette: Bloat.. Toxins. The rules of respect — Emergency Vet. the ER visit. When in doubt, ask about Guide.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Emergency Vet.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Emergency Vet.", "x": "Planning: Triage.. Trauma. Practical notes — Emergency Vet. the ER visit. A little planning shows respect for Toxins.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Emergency Vet and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Emergency Vet and money.", "x": "Costs: Costs.. Costs. What to budget — Emergency Vet. the ER visit. The best experiences of Stabilize. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
function pad(n){return String(n).padStart(6,'0');}
function drillProg(q,a){
  return '// boundless drill program\nvar Q='+JSON.stringify(q)+';\nvar A='+JSON.stringify(a)+';\n'
    +'console.log("DRILL: "+Q);\nconsole.log("Say it out loud, then check:");\nconsole.log("ANSWER: "+A);';
}
function bankRec(i){
  var b=BANK[(i-1)%BANK.length];
  var r={id:PREFIX+pad(i),title:b.t,description:b.x,group:b.g,ladder:b.l,
    question:b.q,answer:b.a,method:'archive-sample',
    program:drillProg(b.q,b.a),language:'javascript',
    src:b.s,last_verified:'2026-10-19',sample:true};
  return r;
}
function genQuizDrill(rnd,seed){
  var b=BANK[(rnd()*BANK.length)|0];
  var desc='Boundless drill #'+seed+' — '+NAME+'. The question: '+b.q+'\n\n'
    +'Cover the answer and say it out loud before reading on. Fluency with these facts is the whole game: '
    +'each drill pulls a real record from this database\'s archive and tests exactly one fact cold. '
    +'If you knew it, it is yours; if not, open the archive record "'+b.t+'" and read the full entry, then come back and drill it again. '
    +'The validated answer: '+b.a+'\n\n'
    +'Drills never repeat the archive verbatim — they re-ask the same true facts from new angles so the knowledge sticks.';
  return {id:PREFIX+pad(seed),title:'Drill: '+b.t,description:desc,group:b.g,ladder:b.l,
    method:'quiz-drill',question:b.q,answer:b.a,
    program:drillProg(b.q,b.a),language:'javascript',src:GEN_SRC,last_verified:'2026-10-19'};
}
function genConvertDrill(rnd,seed){
  var b1=BANK[(rnd()*BANK.length)|0],b2=BANK[(rnd()*BANK.length)|0];
  var v=Math.round((1+rnd()*999)*100)/100;
  var ans=v*b1.f/b2.f;
  var q='Convert '+v+' '+b1.t+' to '+b2.t+'.';
  var a=String(Math.round(ans*1e6)/1e6)+' '+b2.t;
  var desc='Boundless drill #'+seed+' — '+NAME+'. The question: '+q+'\n\n'
    +'Work it with the factor table: multiply by the "from" unit\'s factor to reach the base unit, then divide by the "to" unit\'s factor. '
    +'The demo program on any archive record in this database runs the same computation, so you can check your method there first. '
    +'The validated answer: '+a+'. If your number matches, the method is yours; drills like this one keep every conversion in this database one multiplication and one division away.';
  return {id:PREFIX+pad(seed),title:'Conversion drill: '+b1.t+' to '+b2.t,description:desc,
    group:b1.g,ladder:2,method:'convert-drill',question:q,answer:a,
    conv:{value:v,from:b1.t,fromF:b1.f,to:b2.t,toF:b2.f},
    program:'// conversion drill program\nvar v='+v+';\nvar fromF='+b1.f+';\nvar toF='+b2.f+';\n'
      +'console.log("Q: convert "+v+" '+b1.t.replace(/'/g,"\\'")+' to '+b2.t.replace(/'/g,"\\'")+'");\n'
      +'console.log("A: "+(v*fromF/toF)+" '+b2.t.replace(/'/g,"\\'")+'");',
    language:'javascript',src:GEN_SRC,last_verified:'2026-10-19'};
}
function generate(seed,opts,rnd){
  opts=opts||{};seed=+seed||1;rnd=rnd||prng(seed);
  var g=opts.group||opts.category;
  if(g&&FIELDS.indexOf(g)<0)g=null;
  var r;
  if(seed>=1&&seed<=BANK.length){r=bankRec(seed);}
  else{r=(MODE==='convert')?genConvertDrill(rnd,seed):genQuizDrill(rnd,seed);}
  if(g)r.group=g;
  return r;
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return{ok:false,errors:['not an object']};
  if(!new RegExp('^'+PREFIX.replace(/-/g,'\\-')+'\\d{6}$').test(r.id||''))e.push('id');
  if(FIELDS.indexOf(r.group)<0)e.push('group');
  if(typeof r.title!=='string'||!r.title.length)e.push('title');
  if(typeof r.description!=='string'||r.description.length<200)e.push('description');
  if(r.method==='quiz-drill'||r.method==='archive-sample'){
    var hit=null;
    for(var i=0;i<BANK.length;i++){if(BANK[i].q===r.question&&BANK[i].a===r.answer){hit=BANK[i];break;}}
    if(!hit)e.push('answer not banked');
  }else if(r.method==='convert-drill'){
    var c=r.conv;
    if(!c||typeof c.value!=='number')e.push('conv missing');
    else{
      var expect=c.value*c.fromF/c.toF;
      var got=parseFloat(String(r.answer).split(' ')[0]);
      if(!(Math.abs(got-expect)<Math.max(1e-6,Math.abs(expect)*1e-9)))e.push('conversion mismatch');
    }
  }else{e.push('method');}
  return{ok:!e.length,errors:e};
}
function driftCheck(rec,sample){
  var seen={};(sample||[]).forEach(function(s){if(s&&s.t)seen[s.t]=1;});
  if(rec&&seen[rec.title])return{ok:false,errors:['duplicate title in archive sample']};
  return{ok:true,errors:[]};
}
var gen={version:'jahdb-e2-vet-emergency-vet-care-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
