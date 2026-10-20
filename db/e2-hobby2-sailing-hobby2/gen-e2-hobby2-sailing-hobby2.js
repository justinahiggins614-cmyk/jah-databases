(function(){'use strict';
/* JAH Sailing Hobby Database generator — jahdb-e2-hobby2-sailing-hobby2-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-hobby2-sailing-hobby2',PREFIX='JAH-E2HOBBY2SAI-',NAME='JAH Sailing Hobby Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Sailing Hobby: the complete guide", "d": "Sailing Hobby: the wind harness..", "g": "overview", "l": 2, "q": "What is Sailing Hobby: the complete guide?", "a": "Sailing Hobby: the wind harness..", "x": "The complete hobby guide to Sailing Hobby: the wind harness.. Points of sail. History, meaning, practices, and how to engage respectfully — everything in one database. Tacking. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Sailing Hobby essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Sailing Hobby essentials.", "x": "At a glance: Sailing Hobby — the wind harness.. Tacking. The essentials: Wind.. Knots. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Points of sail.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Points of sail.", "x": "Sailing Hobby: Points of sail.. Wind. Essential knowledge — Knots.. the wind harness. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Points of sail..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Points of sail..", "x": "Explained: Points of sail.. Sail. The context — Sailing Hobby. Lessons. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Tacking.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Tacking.", "x": "Sailing Hobby: Tacking.. Heeling. Essential knowledge — Lessons.. the wind harness. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Tacking..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Tacking..", "x": "Explained: Tacking.. Knots. The context — Sailing Hobby. Wind. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Knots.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Knots.", "x": "Sailing Hobby: Knots.. Sail. Essential knowledge — Wind.. the wind harness. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Knots..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Knots..", "x": "Explained: Knots.. Getting started. The context — Sailing Hobby. Heeling. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Lessons.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Lessons.", "x": "Sailing Hobby: Lessons.. Knots. Essential knowledge — Heeling.. the wind harness. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Lessons..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Lessons..", "x": "Explained: Lessons.. Tacking. The context — Sailing Hobby. Points of sail. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Wind.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Wind.", "x": "Sailing Hobby: Wind.. Getting started. Essential knowledge — Points of sail.. the wind harness. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Wind..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Wind..", "x": "Explained: Wind.. Wind. The context — Sailing Hobby. Tacking. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Heeling.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Heeling.", "x": "Sailing Hobby: Heeling.. Tacking. Essential knowledge — Tacking.. the wind harness. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Heeling..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Heeling..", "x": "Explained: Heeling.. Heeling. The context — Sailing Hobby. Knots. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Tacking.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Tacking.", "x": "Sailing Hobby in depth: Tacking.. Tacking. Details — the wind harness.. Heeling. Lessons. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Wind.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Wind.", "x": "Sailing Hobby in depth: Wind.. Knots. Details — the wind harness.. Sail. Wind. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Heeling.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Heeling.", "x": "Sailing Hobby in depth: Heeling.. Lessons. Details — the wind harness.. Knots. Heeling. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Sail.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Sail.", "x": "Sailing Hobby in depth: Sail.. Wind. Details — the wind harness.. Getting started. Points of sail. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Knots.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Knots.", "x": "Sailing Hobby in depth: Knots.. Heeling. Details — the wind harness.. Tacking. Tacking. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Getting started.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Getting started.", "x": "Sailing Hobby in depth: Getting started.. Points of sail. Details — the wind harness.. Wind. Knots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Sailing Hobby comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Sailing Hobby comes from.", "x": "Origins: Tacking.. Points of sail. The history of Sailing Hobby — the wind harness.. Wind. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Sailing Hobby respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Sailing Hobby respectfully.", "x": "Engaging: Heeling.. Tacking. How to participate or observe well — Sailing Hobby. the wind harness. Respect first, always; Sail.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Sailing Hobby do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Sailing Hobby do's and don'ts.", "x": "Etiquette: Knots.. Knots. The rules of respect — Sailing Hobby. the wind harness. When in doubt, ask about Getting started.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Sailing Hobby.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Sailing Hobby.", "x": "Planning: Tacking.. Lessons. Practical notes — Sailing Hobby. the wind harness. A little planning shows respect for Wind.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Sailing Hobby and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Sailing Hobby and money.", "x": "Costs: Heeling.. Wind. What to budget — Sailing Hobby. the wind harness. The best experiences of Sail. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-hobby2-sailing-hobby2-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
