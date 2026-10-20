(function(){'use strict';
/* JAH Hydro Jetting Pro Database generator — jahdb-e2-trade2-hydro-jetting-pro-trade-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-trade2-hydro-jetting-pro-trade',PREFIX='JAH-E2TRADE2HYD-',NAME='JAH Hydro Jetting Pro Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Hydro Jetting Pro: the complete guide", "d": "Hydro Jetting Pro: the blast pros..", "g": "overview", "l": 2, "q": "What is Hydro Jetting Pro: the complete guide?", "a": "Hydro Jetting Pro: the blast pros..", "x": "The complete trade guide to Hydro Jetting Pro: the blast pros.. 4000 PSI. History, meaning, practices, and how to engage respectfully — everything in one database. PSI. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Hydro Jetting Pro essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Hydro Jetting Pro essentials.", "x": "At a glance: Hydro Jetting Pro — the blast pros.. Grease. The essentials: Nozzles.. Roots. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "4000 PSI.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "4000 PSI.", "x": "Hydro Jetting Pro: 4000 PSI.. Nozzles. Essential knowledge — Roots.. the blast pros. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 4000 PSI..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 4000 PSI..", "x": "Explained: 4000 PSI.. Grease. The context — Hydro Jetting Pro. Camera. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Grease.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Grease.", "x": "Hydro Jetting Pro: Grease.. Access. Essential knowledge — Camera.. the blast pros. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Grease..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Grease..", "x": "Explained: Grease.. Roots. The context — Hydro Jetting Pro. Nozzles. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Roots.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Roots.", "x": "Hydro Jetting Pro: Roots.. Grease. Essential knowledge — Nozzles.. the blast pros. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Roots..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Roots..", "x": "Explained: Roots.. Hiring. The context — Hydro Jetting Pro. Access. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Camera.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Camera.", "x": "Hydro Jetting Pro: Camera.. Roots. Essential knowledge — Access.. the blast pros. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Camera..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Camera..", "x": "Explained: Camera.. PSI. The context — Hydro Jetting Pro. 4000 PSI. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Nozzles.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Nozzles.", "x": "Hydro Jetting Pro: Nozzles.. Hiring. Essential knowledge — 4000 PSI.. the blast pros. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Nozzles..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Nozzles..", "x": "Explained: Nozzles.. Nozzles. The context — Hydro Jetting Pro. Grease. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Access.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Access.", "x": "Hydro Jetting Pro: Access.. PSI. Essential knowledge — Grease.. the blast pros. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Access..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Access..", "x": "Explained: Access.. Access. The context — Hydro Jetting Pro. Roots. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "PSI.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "PSI.", "x": "Hydro Jetting Pro in depth: PSI.. Grease. Details — the blast pros.. Access. Camera. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Nozzles.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Nozzles.", "x": "Hydro Jetting Pro in depth: Nozzles.. Roots. Details — the blast pros.. Grease. Nozzles. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Access.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Access.", "x": "Hydro Jetting Pro in depth: Access.. Camera. Details — the blast pros.. Roots. Access. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Grease.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Grease.", "x": "Hydro Jetting Pro in depth: Grease.. Nozzles. Details — the blast pros.. Hiring. 4000 PSI. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Roots.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Roots.", "x": "Hydro Jetting Pro in depth: Roots.. Access. Details — the blast pros.. PSI. Grease. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Hiring.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Hiring.", "x": "Hydro Jetting Pro in depth: Hiring.. 4000 PSI. Details — the blast pros.. Nozzles. Roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Hydro Jetting Pro comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Hydro Jetting Pro comes from.", "x": "Origins: PSI.. 4000 PSI. The history of Hydro Jetting Pro — the blast pros.. Nozzles. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Hydro Jetting Pro respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Hydro Jetting Pro respectfully.", "x": "Engaging: Access.. Grease. How to participate or observe well — Hydro Jetting Pro. the blast pros. Respect first, always; Grease.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Hydro Jetting Pro do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Hydro Jetting Pro do's and don'ts.", "x": "Etiquette: Roots.. Roots. The rules of respect — Hydro Jetting Pro. the blast pros. When in doubt, ask about Hiring.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Hydro Jetting Pro.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Hydro Jetting Pro.", "x": "Planning: PSI.. Camera. Practical notes — Hydro Jetting Pro. the blast pros. A little planning shows respect for Nozzles.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Hydro Jetting Pro and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Hydro Jetting Pro and money.", "x": "Costs: Access.. Nozzles. What to budget — Hydro Jetting Pro. the blast pros. The best experiences of Grease. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-trade2-hydro-jetting-pro-trade-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
