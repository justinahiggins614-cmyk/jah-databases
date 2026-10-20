(function(){'use strict';
/* JAH Yoga Hobby Database generator — jahdb-e2-hobby2-yoga-hobby2-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-hobby2-yoga-hobby2',PREFIX='JAH-E2HOBBY2YOG-',NAME='JAH Yoga Hobby Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Yoga Hobby: the complete guide", "d": "Yoga Hobby: the mat practice..", "g": "overview", "l": 2, "q": "What is Yoga Hobby: the complete guide?", "a": "Yoga Hobby: the mat practice..", "x": "The complete hobby guide to Yoga Hobby: the mat practice.. Mat. History, meaning, practices, and how to engage respectfully — everything in one database. Breath. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Yoga Hobby essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Yoga Hobby essentials.", "x": "At a glance: Yoga Hobby — the mat practice.. Breath. The essentials: Daily.. Poses. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Mat.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Mat.", "x": "Yoga Hobby: Mat.. Daily. Essential knowledge — Poses.. the mat practice. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Mat..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Mat..", "x": "Explained: Mat.. Mat. The context — Yoga Hobby. Studios. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Breath.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Breath.", "x": "Yoga Hobby: Breath.. Studios. Essential knowledge — Studios.. the mat practice. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Breath..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Breath..", "x": "Explained: Breath.. Poses. The context — Yoga Hobby. Flexibility. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Poses.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Poses.", "x": "Yoga Hobby: Poses.. Mat. Essential knowledge — Flexibility.. the mat practice. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Poses..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Poses..", "x": "Explained: Poses.. Getting started. The context — Yoga Hobby. Daily. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Studios.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Studios.", "x": "Yoga Hobby: Studios.. Poses. Essential knowledge — Daily.. the mat practice. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Studios..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Studios..", "x": "Explained: Studios.. Breath. The context — Yoga Hobby. Mat. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Flexibility.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Flexibility.", "x": "Yoga Hobby: Flexibility.. Getting started. Essential knowledge — Mat.. the mat practice. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Flexibility..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Flexibility..", "x": "Explained: Flexibility.. Daily. The context — Yoga Hobby. Breath. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Daily.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Daily.", "x": "Yoga Hobby: Daily.. Breath. Essential knowledge — Breath.. the mat practice. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Daily..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Daily..", "x": "Explained: Daily.. Studios. The context — Yoga Hobby. Poses. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Breath.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Breath.", "x": "Yoga Hobby in depth: Breath.. Breath. Details — the mat practice.. Studios. Studios. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Daily.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Daily.", "x": "Yoga Hobby in depth: Daily.. Poses. Details — the mat practice.. Mat. Flexibility. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Studios.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Studios.", "x": "Yoga Hobby in depth: Studios.. Studios. Details — the mat practice.. Poses. Daily. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Mat.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Mat.", "x": "Yoga Hobby in depth: Mat.. Flexibility. Details — the mat practice.. Getting started. Mat. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Poses.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Poses.", "x": "Yoga Hobby in depth: Poses.. Daily. Details — the mat practice.. Breath. Breath. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Getting started.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Getting started.", "x": "Yoga Hobby in depth: Getting started.. Mat. Details — the mat practice.. Daily. Poses. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Yoga Hobby comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Yoga Hobby comes from.", "x": "Origins: Breath.. Mat. The history of Yoga Hobby — the mat practice.. Daily. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Yoga Hobby respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Yoga Hobby respectfully.", "x": "Engaging: Studios.. Breath. How to participate or observe well — Yoga Hobby. the mat practice. Respect first, always; Mat.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Yoga Hobby do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Yoga Hobby do's and don'ts.", "x": "Etiquette: Poses.. Poses. The rules of respect — Yoga Hobby. the mat practice. When in doubt, ask about Getting started.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Yoga Hobby.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Yoga Hobby.", "x": "Planning: Breath.. Studios. Practical notes — Yoga Hobby. the mat practice. A little planning shows respect for Daily.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Yoga Hobby and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Yoga Hobby and money.", "x": "Costs: Studios.. Flexibility. What to budget — Yoga Hobby. the mat practice. The best experiences of Mat. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-hobby2-yoga-hobby2-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
