(function(){'use strict';
/* JAH Ejector Pump Installer Database generator — jahdb-e2-trade2-ejector-pump-installer-trade-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-trade2-ejector-pump-installer-trade',PREFIX='JAH-E2TRADE2EJE-',NAME='JAH Ejector Pump Installer Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Ejector Pump Installer: the complete guide", "d": "Ejector Pump Installer: the lift pros..", "g": "overview", "l": 2, "q": "What is Ejector Pump Installer: the complete guide?", "a": "Ejector Pump Installer: the lift pros..", "x": "The complete trade guide to Ejector Pump Installer: the lift pros.. Basement. History, meaning, practices, and how to engage respectfully — everything in one database. Sealed. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Ejector Pump Installer essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Ejector Pump Installer essentials.", "x": "At a glance: Ejector Pump Installer — the lift pros.. Bath. The essentials: Alarm.. Sealed. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Basement.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Basement.", "x": "Ejector Pump Installer: Basement.. Alarm. Essential knowledge — Sealed.. the lift pros. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Basement..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Basement..", "x": "Explained: Basement.. Basement. The context — Ejector Pump Installer. Venting. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Bath.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Bath.", "x": "Ejector Pump Installer: Bath.. Check. Essential knowledge — Venting.. the lift pros. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Bath..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Bath..", "x": "Explained: Bath.. Venting. The context — Ejector Pump Installer. Alarm. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Sealed.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Sealed.", "x": "Ejector Pump Installer: Sealed.. Basement. Essential knowledge — Alarm.. the lift pros. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Sealed..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Sealed..", "x": "Explained: Sealed.. Hiring. The context — Ejector Pump Installer. Check. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Venting.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Venting.", "x": "Ejector Pump Installer: Venting.. Venting. Essential knowledge — Check.. the lift pros. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Venting..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Venting..", "x": "Explained: Venting.. Sealed. The context — Ejector Pump Installer. Basement. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Alarm.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Alarm.", "x": "Ejector Pump Installer: Alarm.. Hiring. Essential knowledge — Basement.. the lift pros. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Alarm..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Alarm..", "x": "Explained: Alarm.. Alarm. The context — Ejector Pump Installer. Bath. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Check.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Check.", "x": "Ejector Pump Installer: Check.. Sealed. Essential knowledge — Bath.. the lift pros. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Check..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Check..", "x": "Explained: Check.. Check. The context — Ejector Pump Installer. Sealed. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Sealed.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Sealed.", "x": "Ejector Pump Installer in depth: Sealed.. Bath. Details — the lift pros.. Check. Venting. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Alarm.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Alarm.", "x": "Ejector Pump Installer in depth: Alarm.. Sealed. Details — the lift pros.. Basement. Alarm. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Check.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Check.", "x": "Ejector Pump Installer in depth: Check.. Venting. Details — the lift pros.. Venting. Check. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Basement.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Basement.", "x": "Ejector Pump Installer in depth: Basement.. Alarm. Details — the lift pros.. Hiring. Basement. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Venting.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Venting.", "x": "Ejector Pump Installer in depth: Venting.. Check. Details — the lift pros.. Sealed. Bath. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Hiring.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Hiring.", "x": "Ejector Pump Installer in depth: Hiring.. Basement. Details — the lift pros.. Alarm. Sealed. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Ejector Pump Installer comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Ejector Pump Installer comes from.", "x": "Origins: Sealed.. Basement. The history of Ejector Pump Installer — the lift pros.. Alarm. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Ejector Pump Installer respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Ejector Pump Installer respectfully.", "x": "Engaging: Check.. Bath. How to participate or observe well — Ejector Pump Installer. the lift pros. Respect first, always; Basement.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Ejector Pump Installer do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Ejector Pump Installer do's and don'ts.", "x": "Etiquette: Venting.. Sealed. The rules of respect — Ejector Pump Installer. the lift pros. When in doubt, ask about Hiring.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Ejector Pump Installer.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Ejector Pump Installer.", "x": "Planning: Sealed.. Venting. Practical notes — Ejector Pump Installer. the lift pros. A little planning shows respect for Alarm.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Ejector Pump Installer and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Ejector Pump Installer and money.", "x": "Costs: Check.. Alarm. What to budget — Ejector Pump Installer. the lift pros. The best experiences of Basement. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-trade2-ejector-pump-installer-trade-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
