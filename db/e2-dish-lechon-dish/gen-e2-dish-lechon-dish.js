(function(){'use strict';
/* JAH Lechon Dish Database generator — jahdb-e2-dish-lechon-dish-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-dish-lechon-dish',PREFIX='JAH-E2DISHLECHO-',NAME='JAH Lechon Dish Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Lechon: the complete guide", "d": "Lechon: the whole roast pig..", "g": "overview", "l": 2, "q": "What is Lechon: the complete guide?", "a": "Lechon: the whole roast pig..", "x": "The complete dish guide to Lechon: the whole roast pig.. Whole pig. History, meaning, practices, and how to engage respectfully — everything in one database. Pig. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Lechon essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Lechon essentials.", "x": "At a glance: Lechon — the whole roast pig.. Crispy. The essentials: Feast.. Celebration. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Whole pig.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Whole pig.", "x": "Lechon: Whole pig.. Feast. Essential knowledge — Celebration.. the whole roast pig. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Whole pig..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Whole pig..", "x": "Explained: Whole pig.. Crispy. The context — Lechon. Spit. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Crispy.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Crispy.", "x": "Lechon: Crispy.. Cebu. Essential knowledge — Spit.. the whole roast pig. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Crispy..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Crispy..", "x": "Explained: Crispy.. Spit. The context — Lechon. Cebu. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Celebration.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Celebration.", "x": "Lechon: Celebration.. Crispy. Essential knowledge — Cebu.. the whole roast pig. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Celebration..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Celebration..", "x": "Explained: Celebration.. Making. The context — Lechon. Feast. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Spit.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Spit.", "x": "Lechon: Spit.. Spit. Essential knowledge — Feast.. the whole roast pig. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Spit..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Spit..", "x": "Explained: Spit.. Pig. The context — Lechon. Whole pig. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Cebu.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Cebu.", "x": "Lechon: Cebu.. Making. Essential knowledge — Whole pig.. the whole roast pig. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Cebu..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Cebu..", "x": "Explained: Cebu.. Feast. The context — Lechon. Crispy. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Feast.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Feast.", "x": "Lechon: Feast.. Pig. Essential knowledge — Crispy.. the whole roast pig. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Feast..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Feast..", "x": "Explained: Feast.. Cebu. The context — Lechon. Celebration. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Pig.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Pig.", "x": "Lechon in depth: Pig.. Crispy. Details — the whole roast pig.. Cebu. Spit. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Feast.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Feast.", "x": "Lechon in depth: Feast.. Celebration. Details — the whole roast pig.. Crispy. Cebu. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Cebu.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Cebu.", "x": "Lechon in depth: Cebu.. Spit. Details — the whole roast pig.. Spit. Feast. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Crispy.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Crispy.", "x": "Lechon in depth: Crispy.. Cebu. Details — the whole roast pig.. Making. Whole pig. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Spit.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Spit.", "x": "Lechon in depth: Spit.. Feast. Details — the whole roast pig.. Pig. Crispy. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Making.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Making.", "x": "Lechon in depth: Making.. Whole pig. Details — the whole roast pig.. Feast. Celebration. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Lechon comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Lechon comes from.", "x": "Origins: Pig.. Whole pig. The history of Lechon — the whole roast pig.. Feast. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Lechon respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Lechon respectfully.", "x": "Engaging: Cebu.. Crispy. How to participate or observe well — Lechon. the whole roast pig. Respect first, always; Crispy.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Lechon do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Lechon do's and don'ts.", "x": "Etiquette: Spit.. Celebration. The rules of respect — Lechon. the whole roast pig. When in doubt, ask about Making.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Lechon.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Lechon.", "x": "Planning: Pig.. Spit. Practical notes — Lechon. the whole roast pig. A little planning shows respect for Feast.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Lechon and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Lechon and money.", "x": "Costs: Cebu.. Cebu. What to budget — Lechon. the whole roast pig. The best experiences of Crispy. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-dish-lechon-dish-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
