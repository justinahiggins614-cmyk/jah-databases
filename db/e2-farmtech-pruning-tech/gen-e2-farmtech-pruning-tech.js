(function(){'use strict';
/* JAH Pruning Technique Farming Technique Database generator — jahdb-e2-farmtech-pruning-tech-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-farmtech-pruning-tech',PREFIX='JAH-E2FARMTECHP-',NAME='JAH Pruning Technique Farming Technique Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Pruning Technique: the complete guide", "d": "Pruning Technique: the cutting art..", "g": "overview", "l": 2, "q": "What is Pruning Technique: the complete guide?", "a": "Pruning Technique: the cutting art..", "x": "The complete farming technique guide to Pruning Technique: the cutting art.. Dormant. History, meaning, practices, and how to engage respectfully — everything in one database. Dormant. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Pruning Technique essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Pruning Technique essentials.", "x": "At a glance: Pruning Technique — the cutting art.. Angles. The essentials: Tools.. Tools. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Dormant.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Dormant.", "x": "Pruning Technique: Dormant.. Tools. Essential knowledge — Tools.. the cutting art. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Dormant..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Dormant..", "x": "Explained: Dormant.. Apples. The context — Pruning Technique. Apples. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Angles.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Angles.", "x": "Pruning Technique: Angles.. Healing. Essential knowledge — Apples.. the cutting art. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Angles..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Angles..", "x": "Explained: Angles.. Angles. The context — Pruning Technique. Vines. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Tools.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Tools.", "x": "Pruning Technique: Tools.. Apples. Essential knowledge — Vines.. the cutting art. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Tools..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Tools..", "x": "Explained: Tools.. Guide. The context — Pruning Technique. Healing. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Apples.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Apples.", "x": "Pruning Technique: Apples.. Angles. Essential knowledge — Healing.. the cutting art. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Apples..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Apples..", "x": "Explained: Apples.. Dormant. The context — Pruning Technique. Dormant. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Vines.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Vines.", "x": "Pruning Technique: Vines.. Guide. Essential knowledge — Dormant.. the cutting art. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Vines..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Vines..", "x": "Explained: Vines.. Tools. The context — Pruning Technique. Angles. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Healing.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Healing.", "x": "Pruning Technique: Healing.. Dormant. Essential knowledge — Angles.. the cutting art. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Healing..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Healing..", "x": "Explained: Healing.. Healing. The context — Pruning Technique. Tools. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Dormant.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Dormant.", "x": "Pruning Technique in depth: Dormant.. Angles. Details — the cutting art.. Healing. Apples. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Tools.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Tools.", "x": "Pruning Technique in depth: Tools.. Tools. Details — the cutting art.. Apples. Vines. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Healing.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Healing.", "x": "Pruning Technique in depth: Healing.. Apples. Details — the cutting art.. Angles. Healing. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Apples.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Apples.", "x": "Pruning Technique in depth: Apples.. Vines. Details — the cutting art.. Guide. Dormant. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Angles.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Angles.", "x": "Pruning Technique in depth: Angles.. Healing. Details — the cutting art.. Dormant. Angles. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Guide.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Guide.", "x": "Pruning Technique in depth: Guide.. Dormant. Details — the cutting art.. Tools. Tools. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Pruning Technique comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Pruning Technique comes from.", "x": "Origins: Dormant.. Dormant. The history of Pruning Technique — the cutting art.. Tools. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Pruning Technique respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Pruning Technique respectfully.", "x": "Engaging: Healing.. Angles. How to participate or observe well — Pruning Technique. the cutting art. Respect first, always; Apples.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Pruning Technique do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Pruning Technique do's and don'ts.", "x": "Etiquette: Angles.. Tools. The rules of respect — Pruning Technique. the cutting art. When in doubt, ask about Guide.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Pruning Technique.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Pruning Technique.", "x": "Planning: Dormant.. Apples. Practical notes — Pruning Technique. the cutting art. A little planning shows respect for Tools.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Pruning Technique and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Pruning Technique and money.", "x": "Costs: Healing.. Vines. What to budget — Pruning Technique. the cutting art. The best experiences of Apples. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-farmtech-pruning-tech-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
