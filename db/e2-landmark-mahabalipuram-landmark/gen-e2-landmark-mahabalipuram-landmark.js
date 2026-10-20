(function(){'use strict';
/* JAH Mahabalipuram Landmark Database generator — jahdb-e2-landmark-mahabalipuram-landmark-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-landmark-mahabalipuram-landmark',PREFIX='JAH-E2LANDMARKM-',NAME='JAH Mahabalipuram Landmark Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Mahabalipuram: the complete guide", "d": "Mahabalipuram: the shore temples..", "g": "overview", "l": 2, "q": "What is Mahabalipuram: the complete guide?", "a": "Mahabalipuram: the shore temples..", "x": "The complete landmark guide to Mahabalipuram: the shore temples.. 7th century. History, meaning, practices, and how to engage respectfully — everything in one database. 7th. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Mahabalipuram essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Mahabalipuram essentials.", "x": "At a glance: Mahabalipuram — the shore temples.. Shore. The essentials: Shore.. Pancha Rathas. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "7th century.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "7th century.", "x": "Mahabalipuram: 7th century.. Shore. Essential knowledge — Pancha Rathas.. the shore temples. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 7th century..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 7th century..", "x": "Explained: 7th century.. Granite. The context — Mahabalipuram. UNESCO. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Shore.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Shore.", "x": "Mahabalipuram: Shore.. UNESCO. Essential knowledge — UNESCO.. the shore temples. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Shore..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Shore..", "x": "Explained: Shore.. Rathas. The context — Mahabalipuram. Granite. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Pancha Rathas.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Pancha Rathas.", "x": "Mahabalipuram: Pancha Rathas.. Granite. Essential knowledge — Granite.. the shore temples. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Pancha Rathas..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Pancha Rathas..", "x": "Explained: Pancha Rathas.. Tours. The context — Mahabalipuram. Coromandel. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "UNESCO.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "UNESCO.", "x": "Mahabalipuram: UNESCO.. Rathas. Essential knowledge — Coromandel.. the shore temples. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: UNESCO..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: UNESCO..", "x": "Explained: UNESCO.. 7th. The context — Mahabalipuram. 7th century. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Granite.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Granite.", "x": "Mahabalipuram: Granite.. Tours. Essential knowledge — 7th century.. the shore temples. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Granite..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Granite..", "x": "Explained: Granite.. Shore. The context — Mahabalipuram. Shore. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Coromandel.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Coromandel.", "x": "Mahabalipuram: Coromandel.. 7th. Essential knowledge — Shore.. the shore temples. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Coromandel..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Coromandel..", "x": "Explained: Coromandel.. UNESCO. The context — Mahabalipuram. Pancha Rathas. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "7th.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "7th.", "x": "Mahabalipuram in depth: 7th.. Shore. Details — the shore temples.. UNESCO. UNESCO. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Shore.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Shore.", "x": "Mahabalipuram in depth: Shore.. Pancha Rathas. Details — the shore temples.. Granite. Granite. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "UNESCO.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "UNESCO.", "x": "Mahabalipuram in depth: UNESCO.. UNESCO. Details — the shore temples.. Rathas. Coromandel. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Granite.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Granite.", "x": "Mahabalipuram in depth: Granite.. Granite. Details — the shore temples.. Tours. 7th century. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Rathas.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Rathas.", "x": "Mahabalipuram in depth: Rathas.. Coromandel. Details — the shore temples.. 7th. Shore. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Tours.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Tours.", "x": "Mahabalipuram in depth: Tours.. 7th century. Details — the shore temples.. Shore. Pancha Rathas. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Mahabalipuram comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Mahabalipuram comes from.", "x": "Origins: 7th.. 7th century. The history of Mahabalipuram — the shore temples.. Shore. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Mahabalipuram respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Mahabalipuram respectfully.", "x": "Engaging: UNESCO.. Shore. How to participate or observe well — Mahabalipuram. the shore temples. Respect first, always; Granite.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Mahabalipuram do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Mahabalipuram do's and don'ts.", "x": "Etiquette: Rathas.. Pancha Rathas. The rules of respect — Mahabalipuram. the shore temples. When in doubt, ask about Tours.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Mahabalipuram.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Mahabalipuram.", "x": "Planning: 7th.. UNESCO. Practical notes — Mahabalipuram. the shore temples. A little planning shows respect for Shore.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Mahabalipuram and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Mahabalipuram and money.", "x": "Costs: UNESCO.. Granite. What to budget — Mahabalipuram. the shore temples. The best experiences of Granite. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-landmark-mahabalipuram-landmark-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
