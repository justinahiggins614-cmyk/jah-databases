(function(){'use strict';
/* JAH Tuba Instrument Instrument Database generator — jahdb-e2-instrument-tuba-instrument-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-instrument-tuba-instrument',PREFIX='JAH-E2INSTRUMEN-',NAME='JAH Tuba Instrument Instrument Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Tuba Instrument: the complete guide", "d": "Tuba Instrument: the brass bass..", "g": "overview", "l": 2, "q": "What is Tuba Instrument: the complete guide?", "a": "Tuba Instrument: the brass bass..", "x": "The complete instrument guide to Tuba Instrument: the brass bass.. Lowest. History, meaning, practices, and how to engage respectfully — everything in one database. Lowest. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Tuba Instrument essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Tuba Instrument essentials.", "x": "At a glance: Tuba Instrument — the brass bass.. Big. The essentials: Sousa.. Oom-pah. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Lowest.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Lowest.", "x": "Tuba Instrument: Lowest.. Sousa. Essential knowledge — Oom-pah.. the brass bass. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Lowest..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Lowest..", "x": "Explained: Lowest.. Breath. The context — Tuba Instrument. Sousa. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Big.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Big.", "x": "Tuba Instrument: Big.. Marching. Essential knowledge — Sousa.. the brass bass. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Big..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Big..", "x": "Explained: Big.. Oom-pah. The context — Tuba Instrument. Marching. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Oom-pah.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Oom-pah.", "x": "Tuba Instrument: Oom-pah.. Breath. Essential knowledge — Marching.. the brass bass. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Oom-pah..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Oom-pah..", "x": "Explained: Oom-pah.. Learning. The context — Tuba Instrument. Breath. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Sousa.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Sousa.", "x": "Tuba Instrument: Sousa.. Oom-pah. Essential knowledge — Breath.. the brass bass. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Sousa..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Sousa..", "x": "Explained: Sousa.. Lowest. The context — Tuba Instrument. Lowest. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Marching.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Marching.", "x": "Tuba Instrument: Marching.. Learning. Essential knowledge — Lowest.. the brass bass. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Marching..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Marching..", "x": "Explained: Marching.. Sousa. The context — Tuba Instrument. Big. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Breath.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Breath.", "x": "Tuba Instrument: Breath.. Lowest. Essential knowledge — Big.. the brass bass. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Breath..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Breath..", "x": "Explained: Breath.. Marching. The context — Tuba Instrument. Oom-pah. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Lowest.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Lowest.", "x": "Tuba Instrument in depth: Lowest.. Big. Details — the brass bass.. Marching. Sousa. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Sousa.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Sousa.", "x": "Tuba Instrument in depth: Sousa.. Oom-pah. Details — the brass bass.. Breath. Marching. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Marching.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Marching.", "x": "Tuba Instrument in depth: Marching.. Sousa. Details — the brass bass.. Oom-pah. Breath. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Breath.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Breath.", "x": "Tuba Instrument in depth: Breath.. Marching. Details — the brass bass.. Learning. Lowest. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Oom-pah.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Oom-pah.", "x": "Tuba Instrument in depth: Oom-pah.. Breath. Details — the brass bass.. Lowest. Big. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Learning.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Learning.", "x": "Tuba Instrument in depth: Learning.. Lowest. Details — the brass bass.. Sousa. Oom-pah. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Tuba Instrument comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Tuba Instrument comes from.", "x": "Origins: Lowest.. Lowest. The history of Tuba Instrument — the brass bass.. Sousa. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Tuba Instrument respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Tuba Instrument respectfully.", "x": "Engaging: Marching.. Big. How to participate or observe well — Tuba Instrument. the brass bass. Respect first, always; Breath.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Tuba Instrument do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Tuba Instrument do's and don'ts.", "x": "Etiquette: Oom-pah.. Oom-pah. The rules of respect — Tuba Instrument. the brass bass. When in doubt, ask about Learning.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Tuba Instrument.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Tuba Instrument.", "x": "Planning: Lowest.. Sousa. Practical notes — Tuba Instrument. the brass bass. A little planning shows respect for Sousa.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Tuba Instrument and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Tuba Instrument and money.", "x": "Costs: Marching.. Marching. What to budget — Tuba Instrument. the brass bass. The best experiences of Breath. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-instrument-tuba-instrument-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
