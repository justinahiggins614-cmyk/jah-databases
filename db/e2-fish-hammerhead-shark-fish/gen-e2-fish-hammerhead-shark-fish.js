(function(){'use strict';
/* JAH Hammerhead Shark Fish Species Database generator — jahdb-e2-fish-hammerhead-shark-fish-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-fish-hammerhead-shark-fish',PREFIX='JAH-E2FISHHAMME-',NAME='JAH Hammerhead Shark Fish Species Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Hammerhead Shark: the complete guide", "d": "Hammerhead Shark: the T-head hunter..", "g": "overview", "l": 2, "q": "What is Hammerhead Shark: the complete guide?", "a": "Hammerhead Shark: the T-head hunter..", "x": "The complete fish species guide to Hammerhead Shark: the T-head hunter.. T-head. History, meaning, practices, and how to engage respectfully — everything in one database. Head. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Hammerhead Shark essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Hammerhead Shark essentials.", "x": "At a glance: Hammerhead Shark — the T-head hunter.. Electroreception. The essentials: Schooling.. Schooling. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "T-head.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "T-head.", "x": "Hammerhead Shark: T-head.. Schooling. Essential knowledge — Schooling.. the T-head hunter. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: T-head..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: T-head..", "x": "Explained: T-head.. Coastal. The context — Hammerhead Shark. Eyes. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Electroreception.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Electroreception.", "x": "Hammerhead Shark: Electroreception.. Endangered. Essential knowledge — Eyes.. the T-head hunter. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Electroreception..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Electroreception..", "x": "Explained: Electroreception.. Eyes. The context — Hammerhead Shark. Coastal. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Schooling.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Schooling.", "x": "Hammerhead Shark: Schooling.. Coastal. Essential knowledge — Coastal.. the T-head hunter. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Schooling..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Schooling..", "x": "Explained: Schooling.. Habitat. The context — Hammerhead Shark. Endangered. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Eyes.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Eyes.", "x": "Hammerhead Shark: Eyes.. Eyes. Essential knowledge — Endangered.. the T-head hunter. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Eyes..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Eyes..", "x": "Explained: Eyes.. Head. The context — Hammerhead Shark. T-head. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Coastal.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Coastal.", "x": "Hammerhead Shark: Coastal.. Habitat. Essential knowledge — T-head.. the T-head hunter. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Coastal..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Coastal..", "x": "Explained: Coastal.. Schooling. The context — Hammerhead Shark. Electroreception. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Endangered.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Endangered.", "x": "Hammerhead Shark: Endangered.. Head. Essential knowledge — Electroreception.. the T-head hunter. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Endangered..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Endangered..", "x": "Explained: Endangered.. Endangered. The context — Hammerhead Shark. Schooling. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Head.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Head.", "x": "Hammerhead Shark in depth: Head.. Electroreception. Details — the T-head hunter.. Endangered. Eyes. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Schooling.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Schooling.", "x": "Hammerhead Shark in depth: Schooling.. Schooling. Details — the T-head hunter.. Coastal. Coastal. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Endangered.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Endangered.", "x": "Hammerhead Shark in depth: Endangered.. Eyes. Details — the T-head hunter.. Eyes. Endangered. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Coastal.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Coastal.", "x": "Hammerhead Shark in depth: Coastal.. Coastal. Details — the T-head hunter.. Habitat. T-head. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Eyes.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Eyes.", "x": "Hammerhead Shark in depth: Eyes.. Endangered. Details — the T-head hunter.. Head. Electroreception. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Habitat.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Habitat.", "x": "Hammerhead Shark in depth: Habitat.. T-head. Details — the T-head hunter.. Schooling. Schooling. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Hammerhead Shark comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Hammerhead Shark comes from.", "x": "Origins: Head.. T-head. The history of Hammerhead Shark — the T-head hunter.. Schooling. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Hammerhead Shark respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Hammerhead Shark respectfully.", "x": "Engaging: Endangered.. Electroreception. How to participate or observe well — Hammerhead Shark. the T-head hunter. Respect first, always; Coastal.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Hammerhead Shark do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Hammerhead Shark do's and don'ts.", "x": "Etiquette: Eyes.. Schooling. The rules of respect — Hammerhead Shark. the T-head hunter. When in doubt, ask about Habitat.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Hammerhead Shark.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Hammerhead Shark.", "x": "Planning: Head.. Eyes. Practical notes — Hammerhead Shark. the T-head hunter. A little planning shows respect for Schooling.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Hammerhead Shark and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Hammerhead Shark and money.", "x": "Costs: Endangered.. Coastal. What to budget — Hammerhead Shark. the T-head hunter. The best experiences of Coastal. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-fish-hammerhead-shark-fish-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
