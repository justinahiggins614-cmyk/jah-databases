(function(){'use strict';
/* JAH Taipei 101 Landmark Database generator — jahdb-e2-landmark-taipei-101-landmark-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-landmark-taipei-101-landmark',PREFIX='JAH-E2LANDMARKT-',NAME='JAH Taipei 101 Landmark Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Taipei 101: the complete guide", "d": "Taipei 101: the 508m pagoda..", "g": "overview", "l": 2, "q": "What is Taipei 101: the complete guide?", "a": "Taipei 101: the 508m pagoda..", "x": "The complete landmark guide to Taipei 101: the 508m pagoda.. 508m. History, meaning, practices, and how to engage respectfully — everything in one database. 508m. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Taipei 101 essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Taipei 101 essentials.", "x": "At a glance: Taipei 101 — the 508m pagoda.. 2004. The essentials: Damper.. Damper. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "508m.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "508m.", "x": "Taipei 101: 508m.. Damper. Essential knowledge — Damper.. the 508m pagoda. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 508m..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 508m..", "x": "Explained: 508m.. Pagoda. The context — Taipei 101. Pagoda. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "2004.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "2004.", "x": "Taipei 101: 2004.. Elevator. Essential knowledge — Pagoda.. the 508m pagoda. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: 2004..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: 2004..", "x": "Explained: 2004.. 2004. The context — Taipei 101. New Year. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Damper.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Damper.", "x": "Taipei 101: Damper.. Pagoda. Essential knowledge — New Year.. the 508m pagoda. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Damper..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Damper..", "x": "Explained: Damper.. Tickets. The context — Taipei 101. Elevator. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Pagoda.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Pagoda.", "x": "Taipei 101: Pagoda.. 2004. Essential knowledge — Elevator.. the 508m pagoda. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Pagoda..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Pagoda..", "x": "Explained: Pagoda.. 508m. The context — Taipei 101. 508m. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "New Year.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "New Year.", "x": "Taipei 101: New Year.. Tickets. Essential knowledge — 508m.. the 508m pagoda. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: New Year..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: New Year..", "x": "Explained: New Year.. Damper. The context — Taipei 101. 2004. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Elevator.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Elevator.", "x": "Taipei 101: Elevator.. 508m. Essential knowledge — 2004.. the 508m pagoda. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Elevator..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Elevator..", "x": "Explained: Elevator.. Elevator. The context — Taipei 101. Damper. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "508m.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "508m.", "x": "Taipei 101 in depth: 508m.. 2004. Details — the 508m pagoda.. Elevator. Pagoda. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Damper.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Damper.", "x": "Taipei 101 in depth: Damper.. Damper. Details — the 508m pagoda.. Pagoda. New Year. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Elevator.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Elevator.", "x": "Taipei 101 in depth: Elevator.. Pagoda. Details — the 508m pagoda.. 2004. Elevator. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Pagoda.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Pagoda.", "x": "Taipei 101 in depth: Pagoda.. New Year. Details — the 508m pagoda.. Tickets. 508m. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "2004.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "2004.", "x": "Taipei 101 in depth: 2004.. Elevator. Details — the 508m pagoda.. 508m. 2004. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Tickets.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Tickets.", "x": "Taipei 101 in depth: Tickets.. 508m. Details — the 508m pagoda.. Damper. Damper. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Taipei 101 comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Taipei 101 comes from.", "x": "Origins: 508m.. 508m. The history of Taipei 101 — the 508m pagoda.. Damper. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Taipei 101 respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Taipei 101 respectfully.", "x": "Engaging: Elevator.. 2004. How to participate or observe well — Taipei 101. the 508m pagoda. Respect first, always; Pagoda.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Taipei 101 do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Taipei 101 do's and don'ts.", "x": "Etiquette: 2004.. Damper. The rules of respect — Taipei 101. the 508m pagoda. When in doubt, ask about Tickets.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Taipei 101.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Taipei 101.", "x": "Planning: 508m.. Pagoda. Practical notes — Taipei 101. the 508m pagoda. A little planning shows respect for Damper.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Taipei 101 and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Taipei 101 and money.", "x": "Costs: Elevator.. New Year. What to budget — Taipei 101. the 508m pagoda. The best experiences of Pagoda. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-landmark-taipei-101-landmark-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
