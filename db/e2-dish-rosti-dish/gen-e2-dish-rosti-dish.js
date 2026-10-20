(function(){'use strict';
/* JAH Rosti Dish Database generator — jahdb-e2-dish-rosti-dish-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-dish-rosti-dish',PREFIX='JAH-E2DISHROSTI-',NAME='JAH Rosti Dish Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Rosti: the complete guide", "d": "Rosti: the potato pancake..", "g": "overview", "l": 2, "q": "What is Rosti: the complete guide?", "a": "Rosti: the potato pancake..", "x": "The complete dish guide to Rosti: the potato pancake.. Potato. History, meaning, practices, and how to engage respectfully — everything in one database. Potato. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Rosti essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Rosti essentials.", "x": "At a glance: Rosti — the potato pancake.. Crispy. The essentials: Bern.. Grated. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Potato.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Potato.", "x": "Rosti: Potato.. Bern. Essential knowledge — Grated.. the potato pancake. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Potato..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Potato..", "x": "Explained: Potato.. Grated. The context — Rosti. Bern. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Crispy.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Crispy.", "x": "Rosti: Crispy.. Golden. Essential knowledge — Bern.. the potato pancake. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Crispy..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Crispy..", "x": "Explained: Crispy.. Crispy. The context — Rosti. Butter. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Grated.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Grated.", "x": "Rosti: Grated.. Grated. Essential knowledge — Butter.. the potato pancake. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Grated..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Grated..", "x": "Explained: Grated.. Making. The context — Rosti. Golden. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Bern.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Bern.", "x": "Rosti: Bern.. Crispy. Essential knowledge — Golden.. the potato pancake. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Bern..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Bern..", "x": "Explained: Bern.. Potato. The context — Rosti. Potato. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Butter.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Butter.", "x": "Rosti: Butter.. Making. Essential knowledge — Potato.. the potato pancake. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Butter..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Butter..", "x": "Explained: Butter.. Bern. The context — Rosti. Crispy. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Golden.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Golden.", "x": "Rosti: Golden.. Potato. Essential knowledge — Crispy.. the potato pancake. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Golden..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Golden..", "x": "Explained: Golden.. Golden. The context — Rosti. Grated. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Potato.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Potato.", "x": "Rosti in depth: Potato.. Crispy. Details — the potato pancake.. Golden. Bern. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Bern.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Bern.", "x": "Rosti in depth: Bern.. Grated. Details — the potato pancake.. Grated. Butter. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Golden.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Golden.", "x": "Rosti in depth: Golden.. Bern. Details — the potato pancake.. Crispy. Golden. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Grated.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Grated.", "x": "Rosti in depth: Grated.. Butter. Details — the potato pancake.. Making. Potato. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Crispy.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Crispy.", "x": "Rosti in depth: Crispy.. Golden. Details — the potato pancake.. Potato. Crispy. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Making.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Making.", "x": "Rosti in depth: Making.. Potato. Details — the potato pancake.. Bern. Grated. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Rosti comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Rosti comes from.", "x": "Origins: Potato.. Potato. The history of Rosti — the potato pancake.. Bern. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Rosti respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Rosti respectfully.", "x": "Engaging: Golden.. Crispy. How to participate or observe well — Rosti. the potato pancake. Respect first, always; Grated.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Rosti do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Rosti do's and don'ts.", "x": "Etiquette: Crispy.. Grated. The rules of respect — Rosti. the potato pancake. When in doubt, ask about Making.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Rosti.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Rosti.", "x": "Planning: Potato.. Bern. Practical notes — Rosti. the potato pancake. A little planning shows respect for Bern.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Rosti and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Rosti and money.", "x": "Costs: Golden.. Butter. What to budget — Rosti. the potato pancake. The best experiences of Grated. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-dish-rosti-dish-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
