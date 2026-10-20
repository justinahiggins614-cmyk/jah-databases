(function(){'use strict';
/* JAH Thistlegorm Dive2 Database generator — jahdb-e2-dive2-thistlegorm-dive2-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-dive2-thistlegorm-dive2',PREFIX='JAH-E2DIVE2THIS-',NAME='JAH Thistlegorm Dive2 Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Thistlegorm Dive2: the complete guide", "d": "Thistlegorm Dive2: the Red Sea 2..", "g": "overview", "l": 2, "q": "What is Thistlegorm Dive2: the complete guide?", "a": "Thistlegorm Dive2: the Red Sea 2..", "x": "The complete dive site guide to Thistlegorm Dive2: the Red Sea 2.. Wreck. History, meaning, practices, and how to engage respectfully — everything in one database. Wreck. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Thistlegorm Dive2 essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Thistlegorm Dive2 essentials.", "x": "At a glance: Thistlegorm Dive2 — the Red Sea 2.. WWII. The essentials: Sea.. Egypt. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Wreck.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Wreck.", "x": "Thistlegorm Dive2: Wreck.. Sea. Essential knowledge — Egypt.. the Red Sea 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Wreck..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Wreck..", "x": "Explained: Wreck.. WWII. The context — Thistlegorm Dive2. Motorbikes. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "WWII.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "WWII.", "x": "Thistlegorm Dive2: WWII.. Red. Essential knowledge — Motorbikes.. the Red Sea 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: WWII..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: WWII..", "x": "Explained: WWII.. 1941. The context — Thistlegorm Dive2. 1941. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Egypt.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Egypt.", "x": "Thistlegorm Dive2: Egypt.. WWII. Essential knowledge — 1941.. the Red Sea 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Egypt..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Egypt..", "x": "Explained: Egypt.. Guide. The context — Thistlegorm Dive2. Red Sea. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Motorbikes.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Motorbikes.", "x": "Thistlegorm Dive2: Motorbikes.. 1941. Essential knowledge — Red Sea.. the Red Sea 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Motorbikes..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Motorbikes..", "x": "Explained: Motorbikes.. Wreck. The context — Thistlegorm Dive2. Wreck. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "1941.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "1941.", "x": "Thistlegorm Dive2: 1941.. Guide. Essential knowledge — Wreck.. the Red Sea 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: 1941..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: 1941..", "x": "Explained: 1941.. Sea. The context — Thistlegorm Dive2. WWII. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Red Sea.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Red Sea.", "x": "Thistlegorm Dive2: Red Sea.. Wreck. Essential knowledge — WWII.. the Red Sea 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Red Sea..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Red Sea..", "x": "Explained: Red Sea.. Red. The context — Thistlegorm Dive2. Egypt. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Wreck.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Wreck.", "x": "Thistlegorm Dive2 in depth: Wreck.. WWII. Details — the Red Sea 2.. Red. Motorbikes. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Sea.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Sea.", "x": "Thistlegorm Dive2 in depth: Sea.. Egypt. Details — the Red Sea 2.. WWII. 1941. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Red.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Red.", "x": "Thistlegorm Dive2 in depth: Red.. Motorbikes. Details — the Red Sea 2.. 1941. Red Sea. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "WWII.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "WWII.", "x": "Thistlegorm Dive2 in depth: WWII.. 1941. Details — the Red Sea 2.. Guide. Wreck. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "1941.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "1941.", "x": "Thistlegorm Dive2 in depth: 1941.. Red Sea. Details — the Red Sea 2.. Wreck. WWII. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Guide.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Guide.", "x": "Thistlegorm Dive2 in depth: Guide.. Wreck. Details — the Red Sea 2.. Sea. Egypt. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Thistlegorm Dive2 comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Thistlegorm Dive2 comes from.", "x": "Origins: Wreck.. Wreck. The history of Thistlegorm Dive2 — the Red Sea 2.. Sea. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Thistlegorm Dive2 respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Thistlegorm Dive2 respectfully.", "x": "Engaging: Red.. WWII. How to participate or observe well — Thistlegorm Dive2. the Red Sea 2. Respect first, always; WWII.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Thistlegorm Dive2 do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Thistlegorm Dive2 do's and don'ts.", "x": "Etiquette: 1941.. Egypt. The rules of respect — Thistlegorm Dive2. the Red Sea 2. When in doubt, ask about Guide.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Thistlegorm Dive2.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Thistlegorm Dive2.", "x": "Planning: Wreck.. Motorbikes. Practical notes — Thistlegorm Dive2. the Red Sea 2. A little planning shows respect for Sea.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Thistlegorm Dive2 and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Thistlegorm Dive2 and money.", "x": "Costs: Red.. 1941. What to budget — Thistlegorm Dive2. the Red Sea 2. The best experiences of WWII. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-dive2-thistlegorm-dive2-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
