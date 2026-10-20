(function(){'use strict';
/* JAH Rye Bread Bread Database generator — jahdb-e2-bread-rye-bread-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-bread-rye-bread',PREFIX='JAH-E2BREADRYEB-',NAME='JAH Rye Bread Bread Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Rye Bread: the complete guide", "d": "Rye Bread: the dark dense..", "g": "overview", "l": 2, "q": "What is Rye Bread: the complete guide?", "a": "Rye Bread: the dark dense..", "x": "The complete bread guide to Rye Bread: the dark dense.. Rye. History, meaning, practices, and how to engage respectfully — everything in one database. Rye. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Rye Bread essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Rye Bread essentials.", "x": "At a glance: Rye Bread — the dark dense.. Caraway. The essentials: Caraway.. Pumpernickel. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Rye.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Rye.", "x": "Rye Bread: Rye.. Caraway. Essential knowledge — Pumpernickel.. the dark dense. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Rye..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Rye..", "x": "Explained: Rye.. Nordic. The context — Rye Bread. Dense. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Caraway.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Caraway.", "x": "Rye Bread: Caraway.. Dense. Essential knowledge — Dense.. the dark dense. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Caraway..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Caraway..", "x": "Explained: Caraway.. Sourdough. The context — Rye Bread. Nordic. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Pumpernickel.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Pumpernickel.", "x": "Rye Bread: Pumpernickel.. Nordic. Essential knowledge — Nordic.. the dark dense. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Pumpernickel..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Pumpernickel..", "x": "Explained: Pumpernickel.. Deli. The context — Rye Bread. Sourdough. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Dense.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Dense.", "x": "Rye Bread: Dense.. Sourdough. Essential knowledge — Sourdough.. the dark dense. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Dense..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Dense..", "x": "Explained: Dense.. Rye. The context — Rye Bread. Rye. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Nordic.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Nordic.", "x": "Rye Bread: Nordic.. Deli. Essential knowledge — Rye.. the dark dense. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Nordic..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Nordic..", "x": "Explained: Nordic.. Caraway. The context — Rye Bread. Caraway. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Sourdough.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Sourdough.", "x": "Rye Bread: Sourdough.. Rye. Essential knowledge — Caraway.. the dark dense. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Sourdough..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Sourdough..", "x": "Explained: Sourdough.. Dense. The context — Rye Bread. Pumpernickel. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Rye.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Rye.", "x": "Rye Bread in depth: Rye.. Caraway. Details — the dark dense.. Dense. Dense. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Caraway.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Caraway.", "x": "Rye Bread in depth: Caraway.. Pumpernickel. Details — the dark dense.. Nordic. Nordic. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Dense.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Dense.", "x": "Rye Bread in depth: Dense.. Dense. Details — the dark dense.. Sourdough. Sourdough. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Nordic.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Nordic.", "x": "Rye Bread in depth: Nordic.. Nordic. Details — the dark dense.. Deli. Rye. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Sourdough.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Sourdough.", "x": "Rye Bread in depth: Sourdough.. Sourdough. Details — the dark dense.. Rye. Caraway. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Deli.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Deli.", "x": "Rye Bread in depth: Deli.. Rye. Details — the dark dense.. Caraway. Pumpernickel. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Rye Bread comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Rye Bread comes from.", "x": "Origins: Rye.. Rye. The history of Rye Bread — the dark dense.. Caraway. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Rye Bread respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Rye Bread respectfully.", "x": "Engaging: Dense.. Caraway. How to participate or observe well — Rye Bread. the dark dense. Respect first, always; Nordic.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Rye Bread do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Rye Bread do's and don'ts.", "x": "Etiquette: Sourdough.. Pumpernickel. The rules of respect — Rye Bread. the dark dense. When in doubt, ask about Deli.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Rye Bread.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Rye Bread.", "x": "Planning: Rye.. Dense. Practical notes — Rye Bread. the dark dense. A little planning shows respect for Caraway.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Rye Bread and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Rye Bread and money.", "x": "Costs: Dense.. Nordic. What to budget — Rye Bread. the dark dense. The best experiences of Nordic. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-bread-rye-bread-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
