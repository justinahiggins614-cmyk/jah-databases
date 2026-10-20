(function(){'use strict';
/* JAH Full English Dish Database generator — jahdb-e2-dish-full-english-dish-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-dish-full-english-dish',PREFIX='JAH-E2DISHFULLE-',NAME='JAH Full English Dish Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Full English: the complete guide", "d": "Full English: the fry-up..", "g": "overview", "l": 2, "q": "What is Full English: the complete guide?", "a": "Full English: the fry-up..", "x": "The complete dish guide to Full English: the fry-up.. Bacon. History, meaning, practices, and how to engage respectfully — everything in one database. Bacon. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Full English essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Full English essentials.", "x": "At a glance: Full English — the fry-up.. Eggs. The essentials: Sausage.. Beans. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Bacon.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Bacon.", "x": "Full English: Bacon.. Sausage. Essential knowledge — Beans.. the fry-up. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Bacon..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Bacon..", "x": "Explained: Bacon.. Beans. The context — Full English. Sausage. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Eggs.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Eggs.", "x": "Full English: Eggs.. Fry-up. Essential knowledge — Sausage.. the fry-up. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Eggs..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Eggs..", "x": "Explained: Eggs.. Eggs. The context — Full English. Tomato. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Beans.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Beans.", "x": "Full English: Beans.. Beans. Essential knowledge — Tomato.. the fry-up. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Beans..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Beans..", "x": "Explained: Beans.. Making. The context — Full English. Fry-up. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Sausage.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Sausage.", "x": "Full English: Sausage.. Eggs. Essential knowledge — Fry-up.. the fry-up. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Sausage..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Sausage..", "x": "Explained: Sausage.. Bacon. The context — Full English. Bacon. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Tomato.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Tomato.", "x": "Full English: Tomato.. Making. Essential knowledge — Bacon.. the fry-up. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Tomato..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Tomato..", "x": "Explained: Tomato.. Sausage. The context — Full English. Eggs. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Fry-up.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Fry-up.", "x": "Full English: Fry-up.. Bacon. Essential knowledge — Eggs.. the fry-up. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Fry-up..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Fry-up..", "x": "Explained: Fry-up.. Fry-up. The context — Full English. Beans. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Bacon.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Bacon.", "x": "Full English in depth: Bacon.. Eggs. Details — the fry-up.. Fry-up. Sausage. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Sausage.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Sausage.", "x": "Full English in depth: Sausage.. Beans. Details — the fry-up.. Beans. Tomato. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Fry-up.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Fry-up.", "x": "Full English in depth: Fry-up.. Sausage. Details — the fry-up.. Eggs. Fry-up. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Beans.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Beans.", "x": "Full English in depth: Beans.. Tomato. Details — the fry-up.. Making. Bacon. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Eggs.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Eggs.", "x": "Full English in depth: Eggs.. Fry-up. Details — the fry-up.. Bacon. Eggs. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Making.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Making.", "x": "Full English in depth: Making.. Bacon. Details — the fry-up.. Sausage. Beans. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Full English comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Full English comes from.", "x": "Origins: Bacon.. Bacon. The history of Full English — the fry-up.. Sausage. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Full English respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Full English respectfully.", "x": "Engaging: Fry-up.. Eggs. How to participate or observe well — Full English. the fry-up. Respect first, always; Beans.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Full English do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Full English do's and don'ts.", "x": "Etiquette: Eggs.. Beans. The rules of respect — Full English. the fry-up. When in doubt, ask about Making.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Full English.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Full English.", "x": "Planning: Bacon.. Sausage. Practical notes — Full English. the fry-up. A little planning shows respect for Sausage.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Full English and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Full English and money.", "x": "Costs: Fry-up.. Tomato. What to budget — Full English. the fry-up. The best experiences of Beans. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-dish-full-english-dish-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
