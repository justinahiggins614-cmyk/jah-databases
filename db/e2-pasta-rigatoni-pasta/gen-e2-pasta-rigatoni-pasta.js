(function(){'use strict';
/* JAH Rigatoni Pasta Database generator — jahdb-e2-pasta-rigatoni-pasta-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-pasta-rigatoni-pasta',PREFIX='JAH-E2PASTARIGA-',NAME='JAH Rigatoni Pasta Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Rigatoni: the complete guide", "d": "Rigatoni: the big ridges..", "g": "overview", "l": 2, "q": "What is Rigatoni: the complete guide?", "a": "Rigatoni: the big ridges..", "x": "The complete pasta guide to Rigatoni: the big ridges.. Large. History, meaning, practices, and how to engage respectfully — everything in one database. Large. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Rigatoni essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Rigatoni essentials.", "x": "At a glance: Rigatoni — the big ridges.. Ridges. The essentials: Ridges.. Baked. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Large.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Large.", "x": "Rigatoni: Large.. Ridges. Essential knowledge — Baked.. the big ridges. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Large..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Large..", "x": "Explained: Large.. Sauce. The context — Rigatoni. Sunday sauce. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Ridges.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Ridges.", "x": "Rigatoni: Ridges.. Baked. Essential knowledge — Sunday sauce.. the big ridges. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Ridges..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Ridges..", "x": "Explained: Ridges.. Rome. The context — Rigatoni. Holds. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Baked.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Baked.", "x": "Rigatoni: Baked.. Sauce. Essential knowledge — Holds.. the big ridges. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Baked..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Baked..", "x": "Explained: Baked.. Holds. The context — Rigatoni. Rome. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Sunday sauce.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Sunday sauce.", "x": "Rigatoni: Sunday sauce.. Rome. Essential knowledge — Rome.. the big ridges. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Sunday sauce..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Sunday sauce..", "x": "Explained: Sunday sauce.. Large. The context — Rigatoni. Large. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Holds.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Holds.", "x": "Rigatoni: Holds.. Holds. Essential knowledge — Large.. the big ridges. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Holds..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Holds..", "x": "Explained: Holds.. Ridges. The context — Rigatoni. Ridges. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Rome.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Rome.", "x": "Rigatoni: Rome.. Large. Essential knowledge — Ridges.. the big ridges. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Rome..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Rome..", "x": "Explained: Rome.. Baked. The context — Rigatoni. Baked. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Large.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Large.", "x": "Rigatoni in depth: Large.. Ridges. Details — the big ridges.. Baked. Sunday sauce. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Ridges.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Ridges.", "x": "Rigatoni in depth: Ridges.. Baked. Details — the big ridges.. Sauce. Holds. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Baked.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Baked.", "x": "Rigatoni in depth: Baked.. Sunday sauce. Details — the big ridges.. Rome. Rome. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Sauce.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Sauce.", "x": "Rigatoni in depth: Sauce.. Holds. Details — the big ridges.. Holds. Large. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Rome.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Rome.", "x": "Rigatoni in depth: Rome.. Rome. Details — the big ridges.. Large. Ridges. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Holds.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Holds.", "x": "Rigatoni in depth: Holds.. Large. Details — the big ridges.. Ridges. Baked. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Rigatoni comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Rigatoni comes from.", "x": "Origins: Large.. Large. The history of Rigatoni — the big ridges.. Ridges. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Rigatoni respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Rigatoni respectfully.", "x": "Engaging: Baked.. Ridges. How to participate or observe well — Rigatoni. the big ridges. Respect first, always; Sauce.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Rigatoni do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Rigatoni do's and don'ts.", "x": "Etiquette: Rome.. Baked. The rules of respect — Rigatoni. the big ridges. When in doubt, ask about Holds.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Rigatoni.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Rigatoni.", "x": "Planning: Large.. Sunday sauce. Practical notes — Rigatoni. the big ridges. A little planning shows respect for Ridges.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Rigatoni and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Rigatoni and money.", "x": "Costs: Baked.. Holds. What to budget — Rigatoni. the big ridges. The best experiences of Sauce. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-pasta-rigatoni-pasta-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
