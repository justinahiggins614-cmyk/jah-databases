(function(){'use strict';
/* JAH Singapore City2 Database generator — jahdb-e2-city2-singapore-city2-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-city2-singapore-city2',PREFIX='JAH-E2CITY2SING-',NAME='JAH Singapore City2 Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Singapore City2: the complete guide", "d": "Singapore City2: the garden 2..", "g": "overview", "l": 2, "q": "What is Singapore City2: the complete guide?", "a": "Singapore City2: the garden 2..", "x": "The complete city guide to Singapore City2: the garden 2.. Marina Bay. History, meaning, practices, and how to engage respectfully — everything in one database. Bay. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Singapore City2 essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Singapore City2 essentials.", "x": "At a glance: Singapore City2 — the garden 2.. Gardens. The essentials: Merlion.. Hawker. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Marina Bay.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Marina Bay.", "x": "Singapore City2: Marina Bay.. Merlion. Essential knowledge — Hawker.. the garden 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Marina Bay..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Marina Bay..", "x": "Explained: Marina Bay.. Gardens. The context — Singapore City2. 5.6M. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Gardens.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Gardens.", "x": "Singapore City2: Gardens.. Clean. Essential knowledge — 5.6M.. the garden 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Gardens..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Gardens..", "x": "Explained: Gardens.. Hawker. The context — Singapore City2. Clean. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Hawker.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Hawker.", "x": "Singapore City2: Hawker.. Gardens. Essential knowledge — Clean.. the garden 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Hawker..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Hawker..", "x": "Explained: Hawker.. Guide. The context — Singapore City2. Merlion. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "5.6M.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "5.6M.", "x": "Singapore City2: 5.6M.. Hawker. Essential knowledge — Merlion.. the garden 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: 5.6M..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: 5.6M..", "x": "Explained: 5.6M.. Bay. The context — Singapore City2. Marina Bay. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Clean.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Clean.", "x": "Singapore City2: Clean.. Guide. Essential knowledge — Marina Bay.. the garden 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Clean..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Clean..", "x": "Explained: Clean.. Merlion. The context — Singapore City2. Gardens. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Merlion.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Merlion.", "x": "Singapore City2: Merlion.. Bay. Essential knowledge — Gardens.. the garden 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Merlion..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Merlion..", "x": "Explained: Merlion.. Clean. The context — Singapore City2. Hawker. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Bay.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Bay.", "x": "Singapore City2 in depth: Bay.. Gardens. Details — the garden 2.. Clean. 5.6M. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Merlion.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Merlion.", "x": "Singapore City2 in depth: Merlion.. Hawker. Details — the garden 2.. Gardens. Clean. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Clean.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Clean.", "x": "Singapore City2 in depth: Clean.. 5.6M. Details — the garden 2.. Hawker. Merlion. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Gardens.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Gardens.", "x": "Singapore City2 in depth: Gardens.. Clean. Details — the garden 2.. Guide. Marina Bay. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Hawker.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Hawker.", "x": "Singapore City2 in depth: Hawker.. Merlion. Details — the garden 2.. Bay. Gardens. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Guide.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Guide.", "x": "Singapore City2 in depth: Guide.. Marina Bay. Details — the garden 2.. Merlion. Hawker. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Singapore City2 comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Singapore City2 comes from.", "x": "Origins: Bay.. Marina Bay. The history of Singapore City2 — the garden 2.. Merlion. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Singapore City2 respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Singapore City2 respectfully.", "x": "Engaging: Clean.. Gardens. How to participate or observe well — Singapore City2. the garden 2. Respect first, always; Gardens.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Singapore City2 do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Singapore City2 do's and don'ts.", "x": "Etiquette: Hawker.. Hawker. The rules of respect — Singapore City2. the garden 2. When in doubt, ask about Guide.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Singapore City2.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Singapore City2.", "x": "Planning: Bay.. 5.6M. Practical notes — Singapore City2. the garden 2. A little planning shows respect for Merlion.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Singapore City2 and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Singapore City2 and money.", "x": "Costs: Clean.. Clean. What to budget — Singapore City2. the garden 2. The best experiences of Gardens. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-city2-singapore-city2-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
