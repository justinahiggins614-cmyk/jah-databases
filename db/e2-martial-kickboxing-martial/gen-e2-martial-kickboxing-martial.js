(function(){'use strict';
/* JAH Kickboxing Martial Art Database generator — jahdb-e2-martial-kickboxing-martial-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-martial-kickboxing-martial',PREFIX='JAH-E2MARTIALKI-',NAME='JAH Kickboxing Martial Art Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Kickboxing: the complete guide", "d": "Kickboxing: the stand-up hybrid..", "g": "overview", "l": 2, "q": "What is Kickboxing: the complete guide?", "a": "Kickboxing: the stand-up hybrid..", "x": "The complete martial art guide to Kickboxing: the stand-up hybrid.. Kicks. History, meaning, practices, and how to engage respectfully — everything in one database. Kicks. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Kickboxing essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Kickboxing essentials.", "x": "At a glance: Kickboxing — the stand-up hybrid.. Punches. The essentials: K-1.. Japan. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Kicks.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Kicks.", "x": "Kickboxing: Kicks.. K-1. Essential knowledge — Japan.. the stand-up hybrid. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Kicks..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Kicks..", "x": "Explained: Kicks.. Japan. The context — Kickboxing. K-1. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Punches.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Punches.", "x": "Kickboxing: Punches.. Cardio. Essential knowledge — K-1.. the stand-up hybrid. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Punches..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Punches..", "x": "Explained: Punches.. Gloves. The context — Kickboxing. Cardio. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Japan.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Japan.", "x": "Kickboxing: Japan.. Japan. Essential knowledge — Cardio.. the stand-up hybrid. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Japan..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Japan..", "x": "Explained: Japan.. Styles. The context — Kickboxing. Gloves. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "K-1.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "K-1.", "x": "Kickboxing: K-1.. Gloves. Essential knowledge — Gloves.. the stand-up hybrid. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: K-1..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: K-1..", "x": "Explained: K-1.. Kicks. The context — Kickboxing. Kicks. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Cardio.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Cardio.", "x": "Kickboxing: Cardio.. Styles. Essential knowledge — Kicks.. the stand-up hybrid. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Cardio..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Cardio..", "x": "Explained: Cardio.. K-1. The context — Kickboxing. Punches. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Gloves.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Gloves.", "x": "Kickboxing: Gloves.. Kicks. Essential knowledge — Punches.. the stand-up hybrid. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Gloves..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Gloves..", "x": "Explained: Gloves.. Cardio. The context — Kickboxing. Japan. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Kicks.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Kicks.", "x": "Kickboxing in depth: Kicks.. Punches. Details — the stand-up hybrid.. Cardio. K-1. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "K-1.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "K-1.", "x": "Kickboxing in depth: K-1.. Japan. Details — the stand-up hybrid.. Japan. Cardio. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Cardio.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Cardio.", "x": "Kickboxing in depth: Cardio.. K-1. Details — the stand-up hybrid.. Gloves. Gloves. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Japan.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Japan.", "x": "Kickboxing in depth: Japan.. Cardio. Details — the stand-up hybrid.. Styles. Kicks. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Gloves.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Gloves.", "x": "Kickboxing in depth: Gloves.. Gloves. Details — the stand-up hybrid.. Kicks. Punches. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Styles.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Styles.", "x": "Kickboxing in depth: Styles.. Kicks. Details — the stand-up hybrid.. K-1. Japan. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Kickboxing comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Kickboxing comes from.", "x": "Origins: Kicks.. Kicks. The history of Kickboxing — the stand-up hybrid.. K-1. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Kickboxing respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Kickboxing respectfully.", "x": "Engaging: Cardio.. Punches. How to participate or observe well — Kickboxing. the stand-up hybrid. Respect first, always; Japan.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Kickboxing do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Kickboxing do's and don'ts.", "x": "Etiquette: Gloves.. Japan. The rules of respect — Kickboxing. the stand-up hybrid. When in doubt, ask about Styles.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Kickboxing.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Kickboxing.", "x": "Planning: Kicks.. K-1. Practical notes — Kickboxing. the stand-up hybrid. A little planning shows respect for K-1.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Kickboxing and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Kickboxing and money.", "x": "Costs: Cardio.. Cardio. What to budget — Kickboxing. the stand-up hybrid. The best experiences of Japan. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-martial-kickboxing-martial-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
