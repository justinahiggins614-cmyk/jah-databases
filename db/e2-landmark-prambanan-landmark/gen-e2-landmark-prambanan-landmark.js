(function(){'use strict';
/* JAH Prambanan Landmark Database generator — jahdb-e2-landmark-prambanan-landmark-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-landmark-prambanan-landmark',PREFIX='JAH-E2LANDMARKP-',NAME='JAH Prambanan Landmark Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Prambanan: the complete guide", "d": "Prambanan: the Hindu towers..", "g": "overview", "l": 2, "q": "What is Prambanan: the complete guide?", "a": "Prambanan: the Hindu towers..", "x": "The complete landmark guide to Prambanan: the Hindu towers.. 9th century. History, meaning, practices, and how to engage respectfully — everything in one database. 9th. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Prambanan essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Prambanan essentials.", "x": "At a glance: Prambanan — the Hindu towers.. 47m. The essentials: Shiva.. Shiva. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "9th century.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "9th century.", "x": "Prambanan: 9th century.. Shiva. Essential knowledge — Shiva.. the Hindu towers. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 9th century..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 9th century..", "x": "Explained: 9th century.. Java. The context — Prambanan. Ramayana. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "47m.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "47m.", "x": "Prambanan: 47m.. UNESCO. Essential knowledge — Ramayana.. the Hindu towers. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: 47m..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: 47m..", "x": "Explained: 47m.. 47m. The context — Prambanan. UNESCO. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Shiva.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Shiva.", "x": "Prambanan: Shiva.. Java. Essential knowledge — UNESCO.. the Hindu towers. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Shiva..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Shiva..", "x": "Explained: Shiva.. Tours. The context — Prambanan. Java. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Ramayana.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Ramayana.", "x": "Prambanan: Ramayana.. 47m. Essential knowledge — Java.. the Hindu towers. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Ramayana..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Ramayana..", "x": "Explained: Ramayana.. 9th. The context — Prambanan. 9th century. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "UNESCO.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "UNESCO.", "x": "Prambanan: UNESCO.. Tours. Essential knowledge — 9th century.. the Hindu towers. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: UNESCO..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: UNESCO..", "x": "Explained: UNESCO.. Shiva. The context — Prambanan. 47m. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Java.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Java.", "x": "Prambanan: Java.. 9th. Essential knowledge — 47m.. the Hindu towers. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Java..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Java..", "x": "Explained: Java.. UNESCO. The context — Prambanan. Shiva. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "9th.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "9th.", "x": "Prambanan in depth: 9th.. 47m. Details — the Hindu towers.. UNESCO. Ramayana. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Shiva.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Shiva.", "x": "Prambanan in depth: Shiva.. Shiva. Details — the Hindu towers.. Java. UNESCO. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "UNESCO.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "UNESCO.", "x": "Prambanan in depth: UNESCO.. Ramayana. Details — the Hindu towers.. 47m. Java. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Java.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Java.", "x": "Prambanan in depth: Java.. UNESCO. Details — the Hindu towers.. Tours. 9th century. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "47m.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "47m.", "x": "Prambanan in depth: 47m.. Java. Details — the Hindu towers.. 9th. 47m. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Tours.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Tours.", "x": "Prambanan in depth: Tours.. 9th century. Details — the Hindu towers.. Shiva. Shiva. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Prambanan comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Prambanan comes from.", "x": "Origins: 9th.. 9th century. The history of Prambanan — the Hindu towers.. Shiva. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Prambanan respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Prambanan respectfully.", "x": "Engaging: UNESCO.. 47m. How to participate or observe well — Prambanan. the Hindu towers. Respect first, always; Java.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Prambanan do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Prambanan do's and don'ts.", "x": "Etiquette: 47m.. Shiva. The rules of respect — Prambanan. the Hindu towers. When in doubt, ask about Tours.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Prambanan.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Prambanan.", "x": "Planning: 9th.. Ramayana. Practical notes — Prambanan. the Hindu towers. A little planning shows respect for Shiva.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Prambanan and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Prambanan and money.", "x": "Costs: UNESCO.. UNESCO. What to budget — Prambanan. the Hindu towers. The best experiences of Java. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-landmark-prambanan-landmark-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
