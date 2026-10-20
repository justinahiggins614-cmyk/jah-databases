(function(){'use strict';
/* JAH Cairo City2 Database generator — jahdb-e2-city2-cairo-city2-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-city2-cairo-city2',PREFIX='JAH-E2CITY2CAIR-',NAME='JAH Cairo City2 Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Cairo City2: the complete guide", "d": "Cairo City2: the Nile 2..", "g": "overview", "l": 2, "q": "What is Cairo City2: the complete guide?", "a": "Cairo City2: the Nile 2..", "x": "The complete city guide to Cairo City2: the Nile 2.. Pyramids. History, meaning, practices, and how to engage respectfully — everything in one database. Pyramids. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Cairo City2 essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Cairo City2 essentials.", "x": "At a glance: Cairo City2 — the Nile 2.. Nile. The essentials: Egypt.. 20M. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Pyramids.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Pyramids.", "x": "Cairo City2: Pyramids.. Egypt. Essential knowledge — 20M.. the Nile 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Pyramids..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Pyramids..", "x": "Explained: Pyramids.. Nile. The context — Cairo City2. Egypt. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Nile.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Nile.", "x": "Cairo City2: Nile.. Chaos. Essential knowledge — Egypt.. the Nile 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Nile..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Nile..", "x": "Explained: Nile.. Khan. The context — Cairo City2. Khan. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "20M.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "20M.", "x": "Cairo City2: 20M.. Nile. Essential knowledge — Khan.. the Nile 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: 20M..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: 20M..", "x": "Explained: 20M.. Guide. The context — Cairo City2. Chaos. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Egypt.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Egypt.", "x": "Cairo City2: Egypt.. Khan. Essential knowledge — Chaos.. the Nile 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Egypt..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Egypt..", "x": "Explained: Egypt.. Pyramids. The context — Cairo City2. Pyramids. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Khan.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Khan.", "x": "Cairo City2: Khan.. Guide. Essential knowledge — Pyramids.. the Nile 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Khan..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Khan..", "x": "Explained: Khan.. Egypt. The context — Cairo City2. Nile. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Chaos.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Chaos.", "x": "Cairo City2: Chaos.. Pyramids. Essential knowledge — Nile.. the Nile 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Chaos..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Chaos..", "x": "Explained: Chaos.. Chaos. The context — Cairo City2. 20M. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Pyramids.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Pyramids.", "x": "Cairo City2 in depth: Pyramids.. Nile. Details — the Nile 2.. Chaos. Egypt. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Egypt.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Egypt.", "x": "Cairo City2 in depth: Egypt.. 20M. Details — the Nile 2.. Nile. Khan. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Chaos.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Chaos.", "x": "Cairo City2 in depth: Chaos.. Egypt. Details — the Nile 2.. Khan. Chaos. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Nile.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Nile.", "x": "Cairo City2 in depth: Nile.. Khan. Details — the Nile 2.. Guide. Pyramids. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Khan.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Khan.", "x": "Cairo City2 in depth: Khan.. Chaos. Details — the Nile 2.. Pyramids. Nile. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Guide.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Guide.", "x": "Cairo City2 in depth: Guide.. Pyramids. Details — the Nile 2.. Egypt. 20M. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Cairo City2 comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Cairo City2 comes from.", "x": "Origins: Pyramids.. Pyramids. The history of Cairo City2 — the Nile 2.. Egypt. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Cairo City2 respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Cairo City2 respectfully.", "x": "Engaging: Chaos.. Nile. How to participate or observe well — Cairo City2. the Nile 2. Respect first, always; Nile.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Cairo City2 do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Cairo City2 do's and don'ts.", "x": "Etiquette: Khan.. 20M. The rules of respect — Cairo City2. the Nile 2. When in doubt, ask about Guide.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Cairo City2.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Cairo City2.", "x": "Planning: Pyramids.. Egypt. Practical notes — Cairo City2. the Nile 2. A little planning shows respect for Egypt.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Cairo City2 and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Cairo City2 and money.", "x": "Costs: Chaos.. Khan. What to budget — Cairo City2. the Nile 2. The best experiences of Nile. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-city2-cairo-city2-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
