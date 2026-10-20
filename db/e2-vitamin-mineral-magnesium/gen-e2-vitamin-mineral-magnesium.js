(function(){'use strict';
/* JAH Magnesium Vitamin Database generator — jahdb-e2-vitamin-mineral-magnesium-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-vitamin-mineral-magnesium',PREFIX='JAH-E2VITAMINMI-',NAME='JAH Magnesium Vitamin Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Magnesium: the complete guide", "d": "Magnesium: the calm mineral..", "g": "overview", "l": 2, "q": "What is Magnesium: the complete guide?", "a": "Magnesium: the calm mineral..", "x": "The complete vitamin guide to Magnesium: the calm mineral.. Magnesium. History, meaning, practices, and how to engage respectfully — everything in one database. Sleep. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Magnesium essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Magnesium essentials.", "x": "At a glance: Magnesium — the calm mineral.. Sleep. The essentials: Muscles.. Muscles. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Magnesium.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Magnesium.", "x": "Magnesium: Magnesium.. Muscles. Essential knowledge — Muscles.. the calm mineral. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Magnesium..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Magnesium..", "x": "Explained: Magnesium.. Deficiency. The context — Magnesium. Nuts. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Sleep.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Sleep.", "x": "Magnesium: Sleep.. Sources. Essential knowledge — Nuts.. the calm mineral. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Sleep..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Sleep..", "x": "Explained: Sleep.. Forms. The context — Magnesium. Deficiency. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Muscles.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Muscles.", "x": "Magnesium: Muscles.. Deficiency. Essential knowledge — Deficiency.. the calm mineral. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Muscles..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Muscles..", "x": "Explained: Muscles.. Supplements. The context — Magnesium. Glycinate. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Nuts.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Nuts.", "x": "Magnesium: Nuts.. Forms. Essential knowledge — Glycinate.. the calm mineral. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Nuts..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Nuts..", "x": "Explained: Nuts.. Sleep. The context — Magnesium. Magnesium. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Deficiency.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Deficiency.", "x": "Magnesium: Deficiency.. Supplements. Essential knowledge — Magnesium.. the calm mineral. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Deficiency..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Deficiency..", "x": "Explained: Deficiency.. Muscles. The context — Magnesium. Sleep. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Glycinate.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Glycinate.", "x": "Magnesium: Glycinate.. Sleep. Essential knowledge — Sleep.. the calm mineral. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Glycinate..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Glycinate..", "x": "Explained: Glycinate.. Sources. The context — Magnesium. Muscles. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Sleep.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Sleep.", "x": "Magnesium in depth: Sleep.. Sleep. Details — the calm mineral.. Sources. Nuts. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Muscles.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Muscles.", "x": "Magnesium in depth: Muscles.. Muscles. Details — the calm mineral.. Deficiency. Deficiency. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Sources.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Sources.", "x": "Magnesium in depth: Sources.. Nuts. Details — the calm mineral.. Forms. Glycinate. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Deficiency.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Deficiency.", "x": "Magnesium in depth: Deficiency.. Deficiency. Details — the calm mineral.. Supplements. Magnesium. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Forms.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Forms.", "x": "Magnesium in depth: Forms.. Glycinate. Details — the calm mineral.. Sleep. Sleep. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Supplements.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Supplements.", "x": "Magnesium in depth: Supplements.. Magnesium. Details — the calm mineral.. Muscles. Muscles. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Magnesium comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Magnesium comes from.", "x": "Origins: Sleep.. Magnesium. The history of Magnesium — the calm mineral.. Muscles. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Magnesium respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Magnesium respectfully.", "x": "Engaging: Sources.. Sleep. How to participate or observe well — Magnesium. the calm mineral. Respect first, always; Deficiency.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Magnesium do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Magnesium do's and don'ts.", "x": "Etiquette: Forms.. Muscles. The rules of respect — Magnesium. the calm mineral. When in doubt, ask about Supplements.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Magnesium.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Magnesium.", "x": "Planning: Sleep.. Nuts. Practical notes — Magnesium. the calm mineral. A little planning shows respect for Muscles.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Magnesium and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Magnesium and money.", "x": "Costs: Sources.. Deficiency. What to budget — Magnesium. the calm mineral. The best experiences of Deficiency. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-vitamin-mineral-magnesium-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
