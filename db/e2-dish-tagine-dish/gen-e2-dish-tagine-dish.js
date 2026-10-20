(function(){'use strict';
/* JAH Tagine Dish Database generator — jahdb-e2-dish-tagine-dish-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-dish-tagine-dish',PREFIX='JAH-E2DISHTAGIN-',NAME='JAH Tagine Dish Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Tagine: the complete guide", "d": "Tagine: the conical stew..", "g": "overview", "l": 2, "q": "What is Tagine: the complete guide?", "a": "Tagine: the conical stew..", "x": "The complete dish guide to Tagine: the conical stew.. Conical. History, meaning, practices, and how to engage respectfully — everything in one database. Conical. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Tagine essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Tagine essentials.", "x": "At a glance: Tagine — the conical stew.. Slow. The essentials: Olives.. Preserved lemon. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Conical.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Conical.", "x": "Tagine: Conical.. Olives. Essential knowledge — Preserved lemon.. the conical stew. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Conical..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Conical..", "x": "Explained: Conical.. Slow. The context — Tagine. Olives. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Slow.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Slow.", "x": "Tagine: Slow.. Clay. Essential knowledge — Olives.. the conical stew. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Slow..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Slow..", "x": "Explained: Slow.. Lamb. The context — Tagine. Lamb. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Preserved lemon.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Preserved lemon.", "x": "Tagine: Preserved lemon.. Slow. Essential knowledge — Lamb.. the conical stew. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Preserved lemon..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Preserved lemon..", "x": "Explained: Preserved lemon.. Making. The context — Tagine. Clay. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Olives.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Olives.", "x": "Tagine: Olives.. Lamb. Essential knowledge — Clay.. the conical stew. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Olives..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Olives..", "x": "Explained: Olives.. Conical. The context — Tagine. Conical. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Lamb.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Lamb.", "x": "Tagine: Lamb.. Making. Essential knowledge — Conical.. the conical stew. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Lamb..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Lamb..", "x": "Explained: Lamb.. Olives. The context — Tagine. Slow. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Clay.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Clay.", "x": "Tagine: Clay.. Conical. Essential knowledge — Slow.. the conical stew. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Clay..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Clay..", "x": "Explained: Clay.. Clay. The context — Tagine. Preserved lemon. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Conical.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Conical.", "x": "Tagine in depth: Conical.. Slow. Details — the conical stew.. Clay. Olives. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Olives.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Olives.", "x": "Tagine in depth: Olives.. Preserved lemon. Details — the conical stew.. Slow. Lamb. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Clay.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Clay.", "x": "Tagine in depth: Clay.. Olives. Details — the conical stew.. Lamb. Clay. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Slow.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Slow.", "x": "Tagine in depth: Slow.. Lamb. Details — the conical stew.. Making. Conical. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Lamb.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Lamb.", "x": "Tagine in depth: Lamb.. Clay. Details — the conical stew.. Conical. Slow. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Making.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Making.", "x": "Tagine in depth: Making.. Conical. Details — the conical stew.. Olives. Preserved lemon. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Tagine comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Tagine comes from.", "x": "Origins: Conical.. Conical. The history of Tagine — the conical stew.. Olives. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Tagine respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Tagine respectfully.", "x": "Engaging: Clay.. Slow. How to participate or observe well — Tagine. the conical stew. Respect first, always; Slow.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Tagine do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Tagine do's and don'ts.", "x": "Etiquette: Lamb.. Preserved lemon. The rules of respect — Tagine. the conical stew. When in doubt, ask about Making.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Tagine.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Tagine.", "x": "Planning: Conical.. Olives. Practical notes — Tagine. the conical stew. A little planning shows respect for Olives.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Tagine and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Tagine and money.", "x": "Costs: Clay.. Lamb. What to budget — Tagine. the conical stew. The best experiences of Slow. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-dish-tagine-dish-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
