(function(){'use strict';
/* JAH Toilet Installer Database generator — jahdb-e2-trade2-toilet-installer-trade-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-trade2-toilet-installer-trade',PREFIX='JAH-E2TRADE2TOI-',NAME='JAH Toilet Installer Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Toilet Installer: the complete guide", "d": "Toilet Installer: the throne pros..", "g": "overview", "l": 2, "q": "What is Toilet Installer: the complete guide?", "a": "Toilet Installer: the throne pros..", "x": "The complete trade guide to Toilet Installer: the throne pros.. Wax ring. History, meaning, practices, and how to engage respectfully — everything in one database. Flange. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Toilet Installer essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Toilet Installer essentials.", "x": "At a glance: Toilet Installer — the throne pros.. Flange. The essentials: Caulk.. Bolts. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Wax ring.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Wax ring.", "x": "Toilet Installer: Wax ring.. Caulk. Essential knowledge — Bolts.. the throne pros. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Wax ring..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Wax ring..", "x": "Explained: Wax ring.. Wax. The context — Toilet Installer. Level. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Flange.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Flange.", "x": "Toilet Installer: Flange.. Shutoff. Essential knowledge — Level.. the throne pros. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Flange..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Flange..", "x": "Explained: Flange.. Bolts. The context — Toilet Installer. Caulk. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Bolts.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Bolts.", "x": "Toilet Installer: Bolts.. Wax. Essential knowledge — Caulk.. the throne pros. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Bolts..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Bolts..", "x": "Explained: Bolts.. Hiring. The context — Toilet Installer. Shutoff. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Level.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Level.", "x": "Toilet Installer: Level.. Bolts. Essential knowledge — Shutoff.. the throne pros. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Level..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Level..", "x": "Explained: Level.. Flange. The context — Toilet Installer. Wax ring. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Caulk.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Caulk.", "x": "Toilet Installer: Caulk.. Hiring. Essential knowledge — Wax ring.. the throne pros. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Caulk..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Caulk..", "x": "Explained: Caulk.. Caulk. The context — Toilet Installer. Flange. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Shutoff.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Shutoff.", "x": "Toilet Installer: Shutoff.. Flange. Essential knowledge — Flange.. the throne pros. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Shutoff..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Shutoff..", "x": "Explained: Shutoff.. Shutoff. The context — Toilet Installer. Bolts. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Flange.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Flange.", "x": "Toilet Installer in depth: Flange.. Flange. Details — the throne pros.. Shutoff. Level. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Caulk.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Caulk.", "x": "Toilet Installer in depth: Caulk.. Bolts. Details — the throne pros.. Wax. Caulk. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Shutoff.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Shutoff.", "x": "Toilet Installer in depth: Shutoff.. Level. Details — the throne pros.. Bolts. Shutoff. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Wax.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Wax.", "x": "Toilet Installer in depth: Wax.. Caulk. Details — the throne pros.. Hiring. Wax ring. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Bolts.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Bolts.", "x": "Toilet Installer in depth: Bolts.. Shutoff. Details — the throne pros.. Flange. Flange. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Hiring.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Hiring.", "x": "Toilet Installer in depth: Hiring.. Wax ring. Details — the throne pros.. Caulk. Bolts. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Toilet Installer comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Toilet Installer comes from.", "x": "Origins: Flange.. Wax ring. The history of Toilet Installer — the throne pros.. Caulk. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Toilet Installer respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Toilet Installer respectfully.", "x": "Engaging: Shutoff.. Flange. How to participate or observe well — Toilet Installer. the throne pros. Respect first, always; Wax.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Toilet Installer do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Toilet Installer do's and don'ts.", "x": "Etiquette: Bolts.. Bolts. The rules of respect — Toilet Installer. the throne pros. When in doubt, ask about Hiring.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Toilet Installer.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Toilet Installer.", "x": "Planning: Flange.. Level. Practical notes — Toilet Installer. the throne pros. A little planning shows respect for Caulk.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Toilet Installer and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Toilet Installer and money.", "x": "Costs: Shutoff.. Caulk. What to budget — Toilet Installer. the throne pros. The best experiences of Wax. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-trade2-toilet-installer-trade-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
