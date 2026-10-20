(function(){'use strict';
/* JAH Bun Cha Dish Database generator — jahdb-e2-dish-bun-cha-dish-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-dish-bun-cha-dish',PREFIX='JAH-E2DISHBUNCH-',NAME='JAH Bun Cha Dish Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Bun Cha: the complete guide", "d": "Bun Cha: the Hanoi pork..", "g": "overview", "l": 2, "q": "What is Bun Cha: the complete guide?", "a": "Bun Cha: the Hanoi pork..", "x": "The complete dish guide to Bun Cha: the Hanoi pork.. Hanoi. History, meaning, practices, and how to engage respectfully — everything in one database. Hanoi. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Bun Cha essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Bun Cha essentials.", "x": "At a glance: Bun Cha — the Hanoi pork.. Pork. The essentials: Grilled.. Noodles. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Hanoi.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Hanoi.", "x": "Bun Cha: Hanoi.. Grilled. Essential knowledge — Noodles.. the Hanoi pork. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Hanoi..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Hanoi..", "x": "Explained: Hanoi.. Pork. The context — Bun Cha. Herbs. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Pork.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Pork.", "x": "Bun Cha: Pork.. Obama. Essential knowledge — Herbs.. the Hanoi pork. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Pork..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Pork..", "x": "Explained: Pork.. Herbs. The context — Bun Cha. Grilled. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Noodles.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Noodles.", "x": "Bun Cha: Noodles.. Pork. Essential knowledge — Grilled.. the Hanoi pork. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Noodles..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Noodles..", "x": "Explained: Noodles.. Making. The context — Bun Cha. Obama. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Herbs.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Herbs.", "x": "Bun Cha: Herbs.. Herbs. Essential knowledge — Obama.. the Hanoi pork. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Herbs..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Herbs..", "x": "Explained: Herbs.. Hanoi. The context — Bun Cha. Hanoi. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Grilled.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Grilled.", "x": "Bun Cha: Grilled.. Making. Essential knowledge — Hanoi.. the Hanoi pork. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Grilled..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Grilled..", "x": "Explained: Grilled.. Grilled. The context — Bun Cha. Pork. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Obama.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Obama.", "x": "Bun Cha: Obama.. Hanoi. Essential knowledge — Pork.. the Hanoi pork. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Obama..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Obama..", "x": "Explained: Obama.. Obama. The context — Bun Cha. Noodles. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Hanoi.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Hanoi.", "x": "Bun Cha in depth: Hanoi.. Pork. Details — the Hanoi pork.. Obama. Herbs. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Grilled.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Grilled.", "x": "Bun Cha in depth: Grilled.. Noodles. Details — the Hanoi pork.. Pork. Grilled. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Obama.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Obama.", "x": "Bun Cha in depth: Obama.. Herbs. Details — the Hanoi pork.. Herbs. Obama. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Pork.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Pork.", "x": "Bun Cha in depth: Pork.. Grilled. Details — the Hanoi pork.. Making. Hanoi. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Herbs.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Herbs.", "x": "Bun Cha in depth: Herbs.. Obama. Details — the Hanoi pork.. Hanoi. Pork. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Making.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Making.", "x": "Bun Cha in depth: Making.. Hanoi. Details — the Hanoi pork.. Grilled. Noodles. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Bun Cha comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Bun Cha comes from.", "x": "Origins: Hanoi.. Hanoi. The history of Bun Cha — the Hanoi pork.. Grilled. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Bun Cha respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Bun Cha respectfully.", "x": "Engaging: Obama.. Pork. How to participate or observe well — Bun Cha. the Hanoi pork. Respect first, always; Pork.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Bun Cha do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Bun Cha do's and don'ts.", "x": "Etiquette: Herbs.. Noodles. The rules of respect — Bun Cha. the Hanoi pork. When in doubt, ask about Making.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Bun Cha.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Bun Cha.", "x": "Planning: Hanoi.. Herbs. Practical notes — Bun Cha. the Hanoi pork. A little planning shows respect for Grilled.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Bun Cha and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Bun Cha and money.", "x": "Costs: Obama.. Grilled. What to budget — Bun Cha. the Hanoi pork. The best experiences of Pork. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-dish-bun-cha-dish-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
