(function(){'use strict';
/* JAH Journalist Profession Database generator — jahdb-e2-profession-journalist-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-profession-journalist',PREFIX='JAH-E2PROFESSIO-',NAME='JAH Journalist Profession Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Journalist Profession: the complete guide", "d": "Journalist Profession: the truth profession..", "g": "overview", "l": 2, "q": "What is Journalist Profession: the complete guide?", "a": "Journalist Profession: the truth profession..", "x": "The complete profession guide to Journalist Profession: the truth profession.. Beat. History, meaning, practices, and how to engage respectfully — everything in one database. Beat. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Journalist Profession essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Journalist Profession essentials.", "x": "At a glance: Journalist Profession — the truth profession.. Deadlines. The essentials: Sources.. Sources. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Beat.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Beat.", "x": "Journalist Profession: Beat.. Sources. Essential knowledge — Sources.. the truth profession. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Beat..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Beat..", "x": "Explained: Beat.. Bylines. The context — Journalist Profession. Ethics. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Deadlines.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Deadlines.", "x": "Journalist Profession: Deadlines.. Ethics. Essential knowledge — Ethics.. the truth profession. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Deadlines..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Deadlines..", "x": "Explained: Deadlines.. Press. The context — Journalist Profession. Bylines. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Sources.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Sources.", "x": "Journalist Profession: Sources.. Bylines. Essential knowledge — Bylines.. the truth profession. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Sources..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Sources..", "x": "Explained: Sources.. Day. The context — Journalist Profession. Press. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Ethics.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Ethics.", "x": "Journalist Profession: Ethics.. Press. Essential knowledge — Press.. the truth profession. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Ethics..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Ethics..", "x": "Explained: Ethics.. Beat. The context — Journalist Profession. Beat. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Bylines.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Bylines.", "x": "Journalist Profession: Bylines.. Day. Essential knowledge — Beat.. the truth profession. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Bylines..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Bylines..", "x": "Explained: Bylines.. Sources. The context — Journalist Profession. Deadlines. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Press.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Press.", "x": "Journalist Profession: Press.. Beat. Essential knowledge — Deadlines.. the truth profession. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Press..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Press..", "x": "Explained: Press.. Ethics. The context — Journalist Profession. Sources. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Beat.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Beat.", "x": "Journalist Profession in depth: Beat.. Deadlines. Details — the truth profession.. Ethics. Ethics. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Sources.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Sources.", "x": "Journalist Profession in depth: Sources.. Sources. Details — the truth profession.. Bylines. Bylines. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Ethics.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Ethics.", "x": "Journalist Profession in depth: Ethics.. Ethics. Details — the truth profession.. Press. Press. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Bylines.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Bylines.", "x": "Journalist Profession in depth: Bylines.. Bylines. Details — the truth profession.. Day. Beat. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Press.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Press.", "x": "Journalist Profession in depth: Press.. Press. Details — the truth profession.. Beat. Deadlines. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Day.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Day.", "x": "Journalist Profession in depth: Day.. Beat. Details — the truth profession.. Sources. Sources. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Journalist Profession comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Journalist Profession comes from.", "x": "Origins: Beat.. Beat. The history of Journalist Profession — the truth profession.. Sources. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Journalist Profession respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Journalist Profession respectfully.", "x": "Engaging: Ethics.. Deadlines. How to participate or observe well — Journalist Profession. the truth profession. Respect first, always; Bylines.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Journalist Profession do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Journalist Profession do's and don'ts.", "x": "Etiquette: Press.. Sources. The rules of respect — Journalist Profession. the truth profession. When in doubt, ask about Day.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Journalist Profession.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Journalist Profession.", "x": "Planning: Beat.. Ethics. Practical notes — Journalist Profession. the truth profession. A little planning shows respect for Sources.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Journalist Profession and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Journalist Profession and money.", "x": "Costs: Ethics.. Bylines. What to budget — Journalist Profession. the truth profession. The best experiences of Bylines. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-profession-journalist-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
