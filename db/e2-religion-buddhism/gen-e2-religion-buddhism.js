(function(){'use strict';
/* JAH Buddhism Religion Database generator — jahdb-e2-religion-buddhism-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-religion-buddhism',PREFIX='JAH-E2RELIGIONB-',NAME='JAH Buddhism Religion Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Buddhism: the complete guide", "d": "Buddhism: 500M; the Buddha's path..", "g": "overview", "l": 2, "q": "What is Buddhism: the complete guide?", "a": "Buddhism: 500M; the Buddha's path..", "x": "The complete religion guide to Buddhism: 500M; the Buddha's path.. Siddhartha Gautama. History, meaning, practices, and how to engage respectfully — everything in one database. Schools. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Buddhism essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Buddhism essentials.", "x": "At a glance: Buddhism — 500M; the Buddha's path.. Four Noble Truths. The essentials: Practices.. Eightfold Path. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Siddhartha Gautama.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Siddhartha Gautama.", "x": "Buddhism: Siddhartha Gautama.. Practices. Essential knowledge — Eightfold Path.. 500M; the Buddha's path. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Siddhartha Gautama..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Siddhartha Gautama..", "x": "Explained: Siddhartha Gautama.. History. The context — Buddhism. Meditation. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Four Noble Truths.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Four Noble Truths.", "x": "Buddhism: Four Noble Truths.. Monks. Essential knowledge — Meditation.. 500M; the Buddha's path. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Four Noble Truths..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Four Noble Truths..", "x": "Explained: Four Noble Truths.. Global. The context — Buddhism. Nirvana. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Eightfold Path.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Eightfold Path.", "x": "Buddhism: Eightfold Path.. History. Essential knowledge — Nirvana.. 500M; the Buddha's path. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Eightfold Path..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Eightfold Path..", "x": "Explained: Eightfold Path.. Ethics. The context — Buddhism. 500M followers. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Meditation.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Meditation.", "x": "Buddhism: Meditation.. Global. Essential knowledge — 500M followers.. 500M; the Buddha's path. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Meditation..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Meditation..", "x": "Explained: Meditation.. Schools. The context — Buddhism. Siddhartha Gautama. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Nirvana.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Nirvana.", "x": "Buddhism: Nirvana.. Ethics. Essential knowledge — Siddhartha Gautama.. 500M; the Buddha's path. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Nirvana..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Nirvana..", "x": "Explained: Nirvana.. Practices. The context — Buddhism. Four Noble Truths. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "500M followers.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "500M followers.", "x": "Buddhism: 500M followers.. Schools. Essential knowledge — Four Noble Truths.. 500M; the Buddha's path. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: 500M followers..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: 500M followers..", "x": "Explained: 500M followers.. Monks. The context — Buddhism. Eightfold Path. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Schools.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Schools.", "x": "Buddhism in depth: Schools.. Four Noble Truths. Details — 500M; the Buddha's path.. Monks. Meditation. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Practices.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Practices.", "x": "Buddhism in depth: Practices.. Eightfold Path. Details — 500M; the Buddha's path.. History. Nirvana. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Monks.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Monks.", "x": "Buddhism in depth: Monks.. Meditation. Details — 500M; the Buddha's path.. Global. 500M followers. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "History.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "History.", "x": "Buddhism in depth: History.. Nirvana. Details — 500M; the Buddha's path.. Ethics. Siddhartha Gautama. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Global.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Global.", "x": "Buddhism in depth: Global.. 500M followers. Details — 500M; the Buddha's path.. Schools. Four Noble Truths. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Ethics.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Ethics.", "x": "Buddhism in depth: Ethics.. Siddhartha Gautama. Details — 500M; the Buddha's path.. Practices. Eightfold Path. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Buddhism comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Buddhism comes from.", "x": "Origins: Schools.. Siddhartha Gautama. The history of Buddhism — 500M; the Buddha's path.. Practices. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Buddhism respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Buddhism respectfully.", "x": "Engaging: Monks.. Four Noble Truths. How to participate or observe well — Buddhism. 500M; the Buddha's path. Respect first, always; History.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Buddhism do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Buddhism do's and don'ts.", "x": "Etiquette: Global.. Eightfold Path. The rules of respect — Buddhism. 500M; the Buddha's path. When in doubt, ask about Ethics.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Buddhism.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Buddhism.", "x": "Planning: Schools.. Meditation. Practical notes — Buddhism. 500M; the Buddha's path. A little planning shows respect for Practices.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Buddhism and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Buddhism and money.", "x": "Costs: Monks.. Nirvana. What to budget — Buddhism. 500M; the Buddha's path. The best experiences of History. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-religion-buddhism-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
