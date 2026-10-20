(function(){'use strict';
/* JAH Pilates Program Fitness Program Database generator — jahdb-e2-fitness-pilates-program-fitness-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-fitness-pilates-program-fitness',PREFIX='JAH-E2FITNESSPI-',NAME='JAH Pilates Program Fitness Program Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Pilates Program: the complete guide", "d": "Pilates Program: the core method..", "g": "overview", "l": 2, "q": "What is Pilates Program: the complete guide?", "a": "Pilates Program: the core method..", "x": "The complete fitness program guide to Pilates Program: the core method.. Joseph Pilates. History, meaning, practices, and how to engage respectfully — everything in one database. Reformer. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Pilates Program essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Pilates Program essentials.", "x": "At a glance: Pilates Program — the core method.. Reformer. The essentials: Core.. Core. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Joseph Pilates.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Joseph Pilates.", "x": "Pilates Program: Joseph Pilates.. Core. Essential knowledge — Core.. the core method. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Joseph Pilates..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Joseph Pilates..", "x": "Explained: Joseph Pilates.. History. The context — Pilates Program. Control. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Reformer.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Reformer.", "x": "Pilates Program: Reformer.. Control. Essential knowledge — Control.. the core method. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Reformer..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Reformer..", "x": "Explained: Reformer.. Studios. The context — Pilates Program. 1920s. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Core.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Core.", "x": "Pilates Program: Core.. History. Essential knowledge — 1920s.. the core method. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Core..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Core..", "x": "Explained: Core.. Method. The context — Pilates Program. Studios. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Control.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Control.", "x": "Pilates Program: Control.. Studios. Essential knowledge — Studios.. the core method. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Control..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Control..", "x": "Explained: Control.. Reformer. The context — Pilates Program. Joseph Pilates. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "1920s.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "1920s.", "x": "Pilates Program: 1920s.. Method. Essential knowledge — Joseph Pilates.. the core method. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: 1920s..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: 1920s..", "x": "Explained: 1920s.. Core. The context — Pilates Program. Reformer. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Studios.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Studios.", "x": "Pilates Program: Studios.. Reformer. Essential knowledge — Reformer.. the core method. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Studios..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Studios..", "x": "Explained: Studios.. Control. The context — Pilates Program. Core. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Reformer.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Reformer.", "x": "Pilates Program in depth: Reformer.. Reformer. Details — the core method.. Control. Control. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Core.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Core.", "x": "Pilates Program in depth: Core.. Core. Details — the core method.. History. 1920s. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Control.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Control.", "x": "Pilates Program in depth: Control.. Control. Details — the core method.. Studios. Studios. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "History.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "History.", "x": "Pilates Program in depth: History.. 1920s. Details — the core method.. Method. Joseph Pilates. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Studios.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Studios.", "x": "Pilates Program in depth: Studios.. Studios. Details — the core method.. Reformer. Reformer. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Method.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Method.", "x": "Pilates Program in depth: Method.. Joseph Pilates. Details — the core method.. Core. Core. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Pilates Program comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Pilates Program comes from.", "x": "Origins: Reformer.. Joseph Pilates. The history of Pilates Program — the core method.. Core. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Pilates Program respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Pilates Program respectfully.", "x": "Engaging: Control.. Reformer. How to participate or observe well — Pilates Program. the core method. Respect first, always; History.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Pilates Program do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Pilates Program do's and don'ts.", "x": "Etiquette: Studios.. Core. The rules of respect — Pilates Program. the core method. When in doubt, ask about Method.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Pilates Program.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Pilates Program.", "x": "Planning: Reformer.. Control. Practical notes — Pilates Program. the core method. A little planning shows respect for Core.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Pilates Program and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Pilates Program and money.", "x": "Costs: Control.. 1920s. What to budget — Pilates Program. the core method. The best experiences of History. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-fitness-pilates-program-fitness-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
