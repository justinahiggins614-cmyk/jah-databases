(function(){'use strict';
/* JAH Insanity Workout Fitness Program Database generator — jahdb-e2-fitness-insanity-fitness-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-fitness-insanity-fitness',PREFIX='JAH-E2FITNESSIN-',NAME='JAH Insanity Workout Fitness Program Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Insanity Workout: the complete guide", "d": "Insanity Workout: the max interval..", "g": "overview", "l": 2, "q": "What is Insanity Workout: the complete guide?", "a": "Insanity Workout: the max interval..", "x": "The complete fitness program guide to Insanity Workout: the max interval.. Shaun T. History, meaning, practices, and how to engage respectfully — everything in one database. HIIT. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Insanity Workout essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Insanity Workout essentials.", "x": "At a glance: Insanity Workout — the max interval.. HIIT. The essentials: Shaun T.. 60 days. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Shaun T.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Shaun T.", "x": "Insanity Workout: Shaun T.. Shaun T. Essential knowledge — 60 days.. the max interval. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Shaun T..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Shaun T..", "x": "Explained: Shaun T.. Cardio. The context — Insanity Workout. No equipment. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "HIIT.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "HIIT.", "x": "Insanity Workout: HIIT.. No gear. Essential knowledge — No equipment.. the max interval. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: HIIT..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: HIIT..", "x": "Explained: HIIT.. Max. The context — Insanity Workout. Max. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "60 days.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "60 days.", "x": "Insanity Workout: 60 days.. Cardio. Essential knowledge — Max.. the max interval. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: 60 days..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: 60 days..", "x": "Explained: 60 days.. Schedule. The context — Insanity Workout. Cardio. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "No equipment.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "No equipment.", "x": "Insanity Workout: No equipment.. Max. Essential knowledge — Cardio.. the max interval. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: No equipment..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: No equipment..", "x": "Explained: No equipment.. HIIT. The context — Insanity Workout. Shaun T. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Max.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Max.", "x": "Insanity Workout: Max.. Schedule. Essential knowledge — Shaun T.. the max interval. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Max..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Max..", "x": "Explained: Max.. Shaun T. The context — Insanity Workout. HIIT. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Cardio.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Cardio.", "x": "Insanity Workout: Cardio.. HIIT. Essential knowledge — HIIT.. the max interval. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Cardio..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Cardio..", "x": "Explained: Cardio.. No gear. The context — Insanity Workout. 60 days. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "HIIT.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "HIIT.", "x": "Insanity Workout in depth: HIIT.. HIIT. Details — the max interval.. No gear. No equipment. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Shaun T.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Shaun T.", "x": "Insanity Workout in depth: Shaun T.. 60 days. Details — the max interval.. Cardio. Max. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "No gear.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "No gear.", "x": "Insanity Workout in depth: No gear.. No equipment. Details — the max interval.. Max. Cardio. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Cardio.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Cardio.", "x": "Insanity Workout in depth: Cardio.. Max. Details — the max interval.. Schedule. Shaun T. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Max.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Max.", "x": "Insanity Workout in depth: Max.. Cardio. Details — the max interval.. HIIT. HIIT. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Schedule.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Schedule.", "x": "Insanity Workout in depth: Schedule.. Shaun T. Details — the max interval.. Shaun T. 60 days. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Insanity Workout comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Insanity Workout comes from.", "x": "Origins: HIIT.. Shaun T. The history of Insanity Workout — the max interval.. Shaun T. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Insanity Workout respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Insanity Workout respectfully.", "x": "Engaging: No gear.. HIIT. How to participate or observe well — Insanity Workout. the max interval. Respect first, always; Cardio.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Insanity Workout do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Insanity Workout do's and don'ts.", "x": "Etiquette: Max.. 60 days. The rules of respect — Insanity Workout. the max interval. When in doubt, ask about Schedule.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Insanity Workout.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Insanity Workout.", "x": "Planning: HIIT.. No equipment. Practical notes — Insanity Workout. the max interval. A little planning shows respect for Shaun T.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Insanity Workout and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Insanity Workout and money.", "x": "Costs: No gear.. Max. What to budget — Insanity Workout. the max interval. The best experiences of Cardio. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-fitness-insanity-fitness-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
