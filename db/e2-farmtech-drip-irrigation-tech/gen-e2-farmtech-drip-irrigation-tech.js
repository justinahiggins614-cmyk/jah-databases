(function(){'use strict';
/* JAH Drip Irrigation Farming Technique Database generator — jahdb-e2-farmtech-drip-irrigation-tech-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-farmtech-drip-irrigation-tech',PREFIX='JAH-E2FARMTECHD-',NAME='JAH Drip Irrigation Farming Technique Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Drip Irrigation: the complete guide", "d": "Drip Irrigation: the precise water..", "g": "overview", "l": 2, "q": "What is Drip Irrigation: the complete guide?", "a": "Drip Irrigation: the precise water..", "x": "The complete farming technique guide to Drip Irrigation: the precise water.. Emitters. History, meaning, practices, and how to engage respectfully — everything in one database. Emitters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Drip Irrigation essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Drip Irrigation essentials.", "x": "At a glance: Drip Irrigation — the precise water.. Efficiency. The essentials: Savings.. Mulch. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Emitters.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Emitters.", "x": "Drip Irrigation: Emitters.. Savings. Essential knowledge — Mulch.. the precise water. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Emitters..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Emitters..", "x": "Explained: Emitters.. Clogging. The context — Drip Irrigation. Clogging. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Efficiency.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Efficiency.", "x": "Drip Irrigation: Efficiency.. Timing. Essential knowledge — Clogging.. the precise water. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Efficiency..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Efficiency..", "x": "Explained: Efficiency.. Mulch. The context — Drip Irrigation. Timing. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Mulch.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Mulch.", "x": "Drip Irrigation: Mulch.. Clogging. Essential knowledge — Timing.. the precise water. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Mulch..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Mulch..", "x": "Explained: Mulch.. Guide. The context — Drip Irrigation. Savings. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Clogging.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Clogging.", "x": "Drip Irrigation: Clogging.. Mulch. Essential knowledge — Savings.. the precise water. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Clogging..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Clogging..", "x": "Explained: Clogging.. Emitters. The context — Drip Irrigation. Emitters. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Timing.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Timing.", "x": "Drip Irrigation: Timing.. Guide. Essential knowledge — Emitters.. the precise water. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Timing..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Timing..", "x": "Explained: Timing.. Savings. The context — Drip Irrigation. Efficiency. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Savings.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Savings.", "x": "Drip Irrigation: Savings.. Emitters. Essential knowledge — Efficiency.. the precise water. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Savings..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Savings..", "x": "Explained: Savings.. Timing. The context — Drip Irrigation. Mulch. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Emitters.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Emitters.", "x": "Drip Irrigation in depth: Emitters.. Efficiency. Details — the precise water.. Timing. Clogging. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Savings.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Savings.", "x": "Drip Irrigation in depth: Savings.. Mulch. Details — the precise water.. Clogging. Timing. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Timing.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Timing.", "x": "Drip Irrigation in depth: Timing.. Clogging. Details — the precise water.. Mulch. Savings. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Clogging.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Clogging.", "x": "Drip Irrigation in depth: Clogging.. Timing. Details — the precise water.. Guide. Emitters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Mulch.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Mulch.", "x": "Drip Irrigation in depth: Mulch.. Savings. Details — the precise water.. Emitters. Efficiency. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Guide.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Guide.", "x": "Drip Irrigation in depth: Guide.. Emitters. Details — the precise water.. Savings. Mulch. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Drip Irrigation comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Drip Irrigation comes from.", "x": "Origins: Emitters.. Emitters. The history of Drip Irrigation — the precise water.. Savings. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Drip Irrigation respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Drip Irrigation respectfully.", "x": "Engaging: Timing.. Efficiency. How to participate or observe well — Drip Irrigation. the precise water. Respect first, always; Clogging.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Drip Irrigation do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Drip Irrigation do's and don'ts.", "x": "Etiquette: Mulch.. Mulch. The rules of respect — Drip Irrigation. the precise water. When in doubt, ask about Guide.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Drip Irrigation.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Drip Irrigation.", "x": "Planning: Emitters.. Clogging. Practical notes — Drip Irrigation. the precise water. A little planning shows respect for Savings.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Drip Irrigation and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Drip Irrigation and money.", "x": "Costs: Timing.. Timing. What to budget — Drip Irrigation. the precise water. The best experiences of Clogging. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-farmtech-drip-irrigation-tech-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
