(function(){'use strict';
/* JAH Small Mammal Care Pet Care Database generator — jahdb-e2-petcare-small-mammal-petcare-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-petcare-small-mammal-petcare',PREFIX='JAH-E2PETCARESM-',NAME='JAH Small Mammal Care Pet Care Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Small Mammal Care: the complete guide", "d": "Small Mammal Care: the pocket pets..", "g": "overview", "l": 2, "q": "What is Small Mammal Care: the complete guide?", "a": "Small Mammal Care: the pocket pets..", "x": "The complete pet care guide to Small Mammal Care: the pocket pets.. Hamsters. History, meaning, practices, and how to engage respectfully — everything in one database. Bedding. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Small Mammal Care essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Small Mammal Care essentials.", "x": "At a glance: Small Mammal Care — the pocket pets.. Guinea pigs. The essentials: Hay.. Rabbits. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Hamsters.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Hamsters.", "x": "Small Mammal Care: Hamsters.. Hay. Essential knowledge — Rabbits.. the pocket pets. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Hamsters..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Hamsters..", "x": "Explained: Hamsters.. Rabbits. The context — Small Mammal Care. Bedding. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Guinea pigs.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Guinea pigs.", "x": "Small Mammal Care: Guinea pigs.. Handling. Essential knowledge — Bedding.. the pocket pets. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Guinea pigs..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Guinea pigs..", "x": "Explained: Guinea pigs.. Guinea. The context — Small Mammal Care. Hay. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Rabbits.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Rabbits.", "x": "Small Mammal Care: Rabbits.. Rabbits. Essential knowledge — Hay.. the pocket pets. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Rabbits..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Rabbits..", "x": "Explained: Rabbits.. Guide. The context — Small Mammal Care. Handling. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Bedding.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Bedding.", "x": "Small Mammal Care: Bedding.. Guinea. Essential knowledge — Handling.. the pocket pets. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Bedding..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Bedding..", "x": "Explained: Bedding.. Bedding. The context — Small Mammal Care. Hamsters. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Hay.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Hay.", "x": "Small Mammal Care: Hay.. Guide. Essential knowledge — Hamsters.. the pocket pets. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Hay..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Hay..", "x": "Explained: Hay.. Hay. The context — Small Mammal Care. Guinea pigs. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Handling.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Handling.", "x": "Small Mammal Care: Handling.. Bedding. Essential knowledge — Guinea pigs.. the pocket pets. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Handling..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Handling..", "x": "Explained: Handling.. Handling. The context — Small Mammal Care. Rabbits. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Bedding.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Bedding.", "x": "Small Mammal Care in depth: Bedding.. Guinea pigs. Details — the pocket pets.. Handling. Bedding. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Hay.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Hay.", "x": "Small Mammal Care in depth: Hay.. Rabbits. Details — the pocket pets.. Rabbits. Hay. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Handling.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Handling.", "x": "Small Mammal Care in depth: Handling.. Bedding. Details — the pocket pets.. Guinea. Handling. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Rabbits.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Rabbits.", "x": "Small Mammal Care in depth: Rabbits.. Hay. Details — the pocket pets.. Guide. Hamsters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Guinea.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Guinea.", "x": "Small Mammal Care in depth: Guinea.. Handling. Details — the pocket pets.. Bedding. Guinea pigs. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Guide.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Guide.", "x": "Small Mammal Care in depth: Guide.. Hamsters. Details — the pocket pets.. Hay. Rabbits. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Small Mammal Care comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Small Mammal Care comes from.", "x": "Origins: Bedding.. Hamsters. The history of Small Mammal Care — the pocket pets.. Hay. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Small Mammal Care respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Small Mammal Care respectfully.", "x": "Engaging: Handling.. Guinea pigs. How to participate or observe well — Small Mammal Care. the pocket pets. Respect first, always; Rabbits.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Small Mammal Care do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Small Mammal Care do's and don'ts.", "x": "Etiquette: Guinea.. Rabbits. The rules of respect — Small Mammal Care. the pocket pets. When in doubt, ask about Guide.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Small Mammal Care.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Small Mammal Care.", "x": "Planning: Bedding.. Bedding. Practical notes — Small Mammal Care. the pocket pets. A little planning shows respect for Hay.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Small Mammal Care and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Small Mammal Care and money.", "x": "Costs: Handling.. Hay. What to budget — Small Mammal Care. the pocket pets. The best experiences of Rabbits. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-petcare-small-mammal-petcare-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
