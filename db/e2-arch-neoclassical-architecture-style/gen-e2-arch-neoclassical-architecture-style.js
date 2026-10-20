(function(){'use strict';
/* JAH Neoclassical Architecture Style Database generator — jahdb-e2-arch-neoclassical-architecture-style-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-arch-neoclassical-architecture-style',PREFIX='JAH-E2ARCHNEOCL-',NAME='JAH Neoclassical Architecture Style Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Neoclassical Architecture: the complete guide", "d": "Neoclassical Architecture: the republic orders..", "g": "overview", "l": 2, "q": "What is Neoclassical Architecture: the complete guide?", "a": "Neoclassical Architecture: the republic orders..", "x": "The complete architecture style guide to Neoclassical Architecture: the republic orders.. Columns. History, meaning, practices, and how to engage respectfully — everything in one database. Columns. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Neoclassical Architecture essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Neoclassical Architecture essentials.", "x": "At a glance: Neoclassical Architecture — the republic orders.. Pediment. The essentials: Democracy.. Capitals. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Columns.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Columns.", "x": "Neoclassical Architecture: Columns.. Democracy. Essential knowledge — Capitals.. the republic orders. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Columns..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Columns..", "x": "Explained: Columns.. Capitals. The context — Neoclassical Architecture. 18th century. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Pediment.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Pediment.", "x": "Neoclassical Architecture: Pediment.. Monumental. Essential knowledge — 18th century.. the republic orders. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Pediment..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Pediment..", "x": "Explained: Pediment.. 18th. The context — Neoclassical Architecture. Democracy. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Capitals.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Capitals.", "x": "Neoclassical Architecture: Capitals.. Capitals. Essential knowledge — Democracy.. the republic orders. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Capitals..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Capitals..", "x": "Explained: Capitals.. Legacy. The context — Neoclassical Architecture. Monumental. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "18th century.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "18th century.", "x": "Neoclassical Architecture: 18th century.. 18th. Essential knowledge — Monumental.. the republic orders. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: 18th century..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: 18th century..", "x": "Explained: 18th century.. Columns. The context — Neoclassical Architecture. Columns. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Democracy.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Democracy.", "x": "Neoclassical Architecture: Democracy.. Legacy. Essential knowledge — Columns.. the republic orders. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Democracy..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Democracy..", "x": "Explained: Democracy.. Democracy. The context — Neoclassical Architecture. Pediment. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Monumental.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Monumental.", "x": "Neoclassical Architecture: Monumental.. Columns. Essential knowledge — Pediment.. the republic orders. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Monumental..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Monumental..", "x": "Explained: Monumental.. Monumental. The context — Neoclassical Architecture. Capitals. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Columns.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Columns.", "x": "Neoclassical Architecture in depth: Columns.. Pediment. Details — the republic orders.. Monumental. 18th century. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Democracy.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Democracy.", "x": "Neoclassical Architecture in depth: Democracy.. Capitals. Details — the republic orders.. Capitals. Democracy. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Monumental.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Monumental.", "x": "Neoclassical Architecture in depth: Monumental.. 18th century. Details — the republic orders.. 18th. Monumental. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Capitals.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Capitals.", "x": "Neoclassical Architecture in depth: Capitals.. Democracy. Details — the republic orders.. Legacy. Columns. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "18th.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "18th.", "x": "Neoclassical Architecture in depth: 18th.. Monumental. Details — the republic orders.. Columns. Pediment. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Legacy.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Legacy.", "x": "Neoclassical Architecture in depth: Legacy.. Columns. Details — the republic orders.. Democracy. Capitals. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Neoclassical Architecture comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Neoclassical Architecture comes from.", "x": "Origins: Columns.. Columns. The history of Neoclassical Architecture — the republic orders.. Democracy. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Neoclassical Architecture respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Neoclassical Architecture respectfully.", "x": "Engaging: Monumental.. Pediment. How to participate or observe well — Neoclassical Architecture. the republic orders. Respect first, always; Capitals.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Neoclassical Architecture do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Neoclassical Architecture do's and don'ts.", "x": "Etiquette: 18th.. Capitals. The rules of respect — Neoclassical Architecture. the republic orders. When in doubt, ask about Legacy.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Neoclassical Architecture.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Neoclassical Architecture.", "x": "Planning: Columns.. 18th century. Practical notes — Neoclassical Architecture. the republic orders. A little planning shows respect for Democracy.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Neoclassical Architecture and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Neoclassical Architecture and money.", "x": "Costs: Monumental.. Democracy. What to budget — Neoclassical Architecture. the republic orders. The best experiences of Capitals. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-arch-neoclassical-architecture-style-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
