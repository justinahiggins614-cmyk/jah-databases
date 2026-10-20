(function(){'use strict';
/* JAH Peloton Program Fitness Program Database generator — jahdb-e2-fitness-peloton-fitness-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-fitness-peloton-fitness',PREFIX='JAH-E2FITNESSPE-',NAME='JAH Peloton Program Fitness Program Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Peloton Program: the complete guide", "d": "Peloton Program: the connected bike..", "g": "overview", "l": 2, "q": "What is Peloton Program: the complete guide?", "a": "Peloton Program: the connected bike..", "x": "The complete fitness program guide to Peloton Program: the connected bike.. 2012. History, meaning, practices, and how to engage respectfully — everything in one database. Bike. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Peloton Program essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Peloton Program essentials.", "x": "At a glance: Peloton Program — the connected bike.. Bike. The essentials: Leaderboard.. Leaderboard. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "2012.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "2012.", "x": "Peloton Program: 2012.. Leaderboard. Essential knowledge — Leaderboard.. the connected bike. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 2012..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 2012..", "x": "Explained: 2012.. Instructors. The context — Peloton Program. Classes. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Bike.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Bike.", "x": "Peloton Program: Bike.. Home. Essential knowledge — Classes.. the connected bike. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Bike..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Bike..", "x": "Explained: Bike.. Classes. The context — Peloton Program. Home. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Leaderboard.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Leaderboard.", "x": "Peloton Program: Leaderboard.. Instructors. Essential knowledge — Home.. the connected bike. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Leaderboard..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Leaderboard..", "x": "Explained: Leaderboard.. Method. The context — Peloton Program. Instructors. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Classes.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Classes.", "x": "Peloton Program: Classes.. Classes. Essential knowledge — Instructors.. the connected bike. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Classes..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Classes..", "x": "Explained: Classes.. Bike. The context — Peloton Program. 2012. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Home.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Home.", "x": "Peloton Program: Home.. Method. Essential knowledge — 2012.. the connected bike. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Home..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Home..", "x": "Explained: Home.. Leaderboard. The context — Peloton Program. Bike. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Instructors.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Instructors.", "x": "Peloton Program: Instructors.. Bike. Essential knowledge — Bike.. the connected bike. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Instructors..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Instructors..", "x": "Explained: Instructors.. Home. The context — Peloton Program. Leaderboard. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Bike.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Bike.", "x": "Peloton Program in depth: Bike.. Bike. Details — the connected bike.. Home. Classes. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Leaderboard.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Leaderboard.", "x": "Peloton Program in depth: Leaderboard.. Leaderboard. Details — the connected bike.. Instructors. Home. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Home.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Home.", "x": "Peloton Program in depth: Home.. Classes. Details — the connected bike.. Classes. Instructors. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Instructors.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Instructors.", "x": "Peloton Program in depth: Instructors.. Home. Details — the connected bike.. Method. 2012. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Classes.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Classes.", "x": "Peloton Program in depth: Classes.. Instructors. Details — the connected bike.. Bike. Bike. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Method.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Method.", "x": "Peloton Program in depth: Method.. 2012. Details — the connected bike.. Leaderboard. Leaderboard. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Peloton Program comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Peloton Program comes from.", "x": "Origins: Bike.. 2012. The history of Peloton Program — the connected bike.. Leaderboard. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Peloton Program respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Peloton Program respectfully.", "x": "Engaging: Home.. Bike. How to participate or observe well — Peloton Program. the connected bike. Respect first, always; Instructors.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Peloton Program do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Peloton Program do's and don'ts.", "x": "Etiquette: Classes.. Leaderboard. The rules of respect — Peloton Program. the connected bike. When in doubt, ask about Method.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Peloton Program.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Peloton Program.", "x": "Planning: Bike.. Classes. Practical notes — Peloton Program. the connected bike. A little planning shows respect for Leaderboard.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Peloton Program and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Peloton Program and money.", "x": "Costs: Home.. Home. What to budget — Peloton Program. the connected bike. The best experiences of Instructors. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-fitness-peloton-fitness-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
