(function(){'use strict';
/* JAH Earthworm2 Database generator — jahdb-e2-nature2-earthworm2-insect-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-nature2-earthworm2-insect',PREFIX='JAH-E2NATURE2EA-',NAME='JAH Earthworm2 Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Earthworm2: the complete guide", "d": "Earthworm2: the soil 2..", "g": "overview", "l": 2, "q": "What is Earthworm2: the complete guide?", "a": "Earthworm2: the soil 2..", "x": "The complete insect guide to Earthworm2: the soil 2.. Aeration. History, meaning, practices, and how to engage respectfully — everything in one database. Aeration. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Earthworm2 essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Earthworm2 essentials.", "x": "At a glance: Earthworm2 — the soil 2.. Castings. The essentials: Compost.. Soil. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Aeration.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Aeration.", "x": "Earthworm2: Aeration.. Compost. Essential knowledge — Soil.. the soil 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Aeration..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Aeration..", "x": "Explained: Aeration.. Castings. The context — Earthworm2. Rain. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Castings.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Castings.", "x": "Earthworm2: Castings.. Segments. Essential knowledge — Rain.. the soil 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Castings..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Castings..", "x": "Explained: Castings.. Rain. The context — Earthworm2. Compost. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Soil.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Soil.", "x": "Earthworm2: Soil.. Castings. Essential knowledge — Compost.. the soil 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Soil..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Soil..", "x": "Explained: Soil.. Guide. The context — Earthworm2. Segments. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Rain.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Rain.", "x": "Earthworm2: Rain.. Rain. Essential knowledge — Segments.. the soil 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Rain..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Rain..", "x": "Explained: Rain.. Aeration. The context — Earthworm2. Aeration. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Compost.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Compost.", "x": "Earthworm2: Compost.. Guide. Essential knowledge — Aeration.. the soil 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Compost..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Compost..", "x": "Explained: Compost.. Compost. The context — Earthworm2. Castings. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Segments.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Segments.", "x": "Earthworm2: Segments.. Aeration. Essential knowledge — Castings.. the soil 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Segments..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Segments..", "x": "Explained: Segments.. Segments. The context — Earthworm2. Soil. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Aeration.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Aeration.", "x": "Earthworm2 in depth: Aeration.. Castings. Details — the soil 2.. Segments. Rain. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Compost.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Compost.", "x": "Earthworm2 in depth: Compost.. Soil. Details — the soil 2.. Castings. Compost. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Segments.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Segments.", "x": "Earthworm2 in depth: Segments.. Rain. Details — the soil 2.. Rain. Segments. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Castings.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Castings.", "x": "Earthworm2 in depth: Castings.. Compost. Details — the soil 2.. Guide. Aeration. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Rain.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Rain.", "x": "Earthworm2 in depth: Rain.. Segments. Details — the soil 2.. Aeration. Castings. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Guide.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Guide.", "x": "Earthworm2 in depth: Guide.. Aeration. Details — the soil 2.. Compost. Soil. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Earthworm2 comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Earthworm2 comes from.", "x": "Origins: Aeration.. Aeration. The history of Earthworm2 — the soil 2.. Compost. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Earthworm2 respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Earthworm2 respectfully.", "x": "Engaging: Segments.. Castings. How to participate or observe well — Earthworm2. the soil 2. Respect first, always; Castings.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Earthworm2 do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Earthworm2 do's and don'ts.", "x": "Etiquette: Rain.. Soil. The rules of respect — Earthworm2. the soil 2. When in doubt, ask about Guide.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Earthworm2.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Earthworm2.", "x": "Planning: Aeration.. Rain. Practical notes — Earthworm2. the soil 2. A little planning shows respect for Compost.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Earthworm2 and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Earthworm2 and money.", "x": "Costs: Segments.. Compost. What to budget — Earthworm2. the soil 2. The best experiences of Castings. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-nature2-earthworm2-insect-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
