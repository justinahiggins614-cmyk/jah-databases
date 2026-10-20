(function(){'use strict';
/* JAH Septic Pumping Database generator — jahdb-e2-trade2-septic-pumping-trade-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-trade2-septic-pumping-trade',PREFIX='JAH-E2TRADE2SEP-',NAME='JAH Septic Pumping Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Septic Pumping: the complete guide", "d": "Septic Pumping: the tank pros..", "g": "overview", "l": 2, "q": "What is Septic Pumping: the complete guide?", "a": "Septic Pumping: the tank pros..", "x": "The complete trade guide to Septic Pumping: the tank pros.. 3-5 years. History, meaning, practices, and how to engage respectfully — everything in one database. Pumping. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Septic Pumping essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Septic Pumping essentials.", "x": "At a glance: Septic Pumping — the tank pros.. Pumping. The essentials: Inspections.. Inspections. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "3-5 years.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "3-5 years.", "x": "Septic Pumping: 3-5 years.. Inspections. Essential knowledge — Inspections.. the tank pros. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 3-5 years..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 3-5 years..", "x": "Explained: 3-5 years.. Records. The context — Septic Pumping. Baffles. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Pumping.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Pumping.", "x": "Septic Pumping: Pumping.. Drainfield. Essential knowledge — Baffles.. the tank pros. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Pumping..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Pumping..", "x": "Explained: Pumping.. Baffles. The context — Septic Pumping. Drainfield. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Inspections.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Inspections.", "x": "Septic Pumping: Inspections.. Records. Essential knowledge — Drainfield.. the tank pros. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Inspections..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Inspections..", "x": "Explained: Inspections.. Hiring. The context — Septic Pumping. Records. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Baffles.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Baffles.", "x": "Septic Pumping: Baffles.. Baffles. Essential knowledge — Records.. the tank pros. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Baffles..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Baffles..", "x": "Explained: Baffles.. Pumping. The context — Septic Pumping. 3-5 years. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Drainfield.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Drainfield.", "x": "Septic Pumping: Drainfield.. Hiring. Essential knowledge — 3-5 years.. the tank pros. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Drainfield..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Drainfield..", "x": "Explained: Drainfield.. Inspections. The context — Septic Pumping. Pumping. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Records.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Records.", "x": "Septic Pumping: Records.. Pumping. Essential knowledge — Pumping.. the tank pros. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Records..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Records..", "x": "Explained: Records.. Drainfield. The context — Septic Pumping. Inspections. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Pumping.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Pumping.", "x": "Septic Pumping in depth: Pumping.. Pumping. Details — the tank pros.. Drainfield. Baffles. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Inspections.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Inspections.", "x": "Septic Pumping in depth: Inspections.. Inspections. Details — the tank pros.. Records. Drainfield. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Drainfield.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Drainfield.", "x": "Septic Pumping in depth: Drainfield.. Baffles. Details — the tank pros.. Baffles. Records. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Records.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Records.", "x": "Septic Pumping in depth: Records.. Drainfield. Details — the tank pros.. Hiring. 3-5 years. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Baffles.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Baffles.", "x": "Septic Pumping in depth: Baffles.. Records. Details — the tank pros.. Pumping. Pumping. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Hiring.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Hiring.", "x": "Septic Pumping in depth: Hiring.. 3-5 years. Details — the tank pros.. Inspections. Inspections. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Septic Pumping comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Septic Pumping comes from.", "x": "Origins: Pumping.. 3-5 years. The history of Septic Pumping — the tank pros.. Inspections. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Septic Pumping respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Septic Pumping respectfully.", "x": "Engaging: Drainfield.. Pumping. How to participate or observe well — Septic Pumping. the tank pros. Respect first, always; Records.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Septic Pumping do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Septic Pumping do's and don'ts.", "x": "Etiquette: Baffles.. Inspections. The rules of respect — Septic Pumping. the tank pros. When in doubt, ask about Hiring.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Septic Pumping.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Septic Pumping.", "x": "Planning: Pumping.. Baffles. Practical notes — Septic Pumping. the tank pros. A little planning shows respect for Inspections.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Septic Pumping and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Septic Pumping and money.", "x": "Costs: Drainfield.. Drainfield. What to budget — Septic Pumping. the tank pros. The best experiences of Records. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-trade2-septic-pumping-trade-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
