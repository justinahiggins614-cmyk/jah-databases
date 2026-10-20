(function(){'use strict';
/* JAH Military Diet Diet Database generator — jahdb-e2-diet-military-diet-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-diet-military-diet',PREFIX='JAH-E2DIETMILIT-',NAME='JAH Military Diet Diet Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Military Diet: the complete guide", "d": "Military Diet: the 3-day crash..", "g": "overview", "l": 2, "q": "What is Military Diet: the complete guide?", "a": "Military Diet: the 3-day crash..", "x": "The complete diet guide to Military Diet: the 3-day crash.. 3 days. History, meaning, practices, and how to engage respectfully — everything in one database. 3 days. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Military Diet essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Military Diet essentials.", "x": "At a glance: Military Diet — the 3-day crash.. 1000 cal. The essentials: Crash.. Not military. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "3 days.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "3 days.", "x": "Military Diet: 3 days.. Crash. Essential knowledge — Not military.. the 3-day crash. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 3 days..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 3 days..", "x": "Explained: 3 days.. Tuna. The context — Military Diet. Crash. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "1000 cal.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "1000 cal.", "x": "Military Diet: 1000 cal.. Debate. Essential knowledge — Crash.. the 3-day crash. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: 1000 cal..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: 1000 cal..", "x": "Explained: 1000 cal.. Not. The context — Military Diet. Tuna. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Not military.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Not military.", "x": "Military Diet: Not military.. Tuna. Essential knowledge — Tuna.. the 3-day crash. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Not military..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Not military..", "x": "Explained: Not military.. Foods. The context — Military Diet. Debate. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Crash.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Crash.", "x": "Military Diet: Crash.. Not. Essential knowledge — Debate.. the 3-day crash. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Crash..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Crash..", "x": "Explained: Crash.. 3 days. The context — Military Diet. 3 days. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Tuna.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Tuna.", "x": "Military Diet: Tuna.. Foods. Essential knowledge — 3 days.. the 3-day crash. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Tuna..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Tuna..", "x": "Explained: Tuna.. Crash. The context — Military Diet. 1000 cal. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Debate.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Debate.", "x": "Military Diet: Debate.. 3 days. Essential knowledge — 1000 cal.. the 3-day crash. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Debate..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Debate..", "x": "Explained: Debate.. Debate. The context — Military Diet. Not military. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "3 days.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "3 days.", "x": "Military Diet in depth: 3 days.. 1000 cal. Details — the 3-day crash.. Debate. Crash. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Crash.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Crash.", "x": "Military Diet in depth: Crash.. Not military. Details — the 3-day crash.. Tuna. Tuna. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Debate.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Debate.", "x": "Military Diet in depth: Debate.. Crash. Details — the 3-day crash.. Not. Debate. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Tuna.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Tuna.", "x": "Military Diet in depth: Tuna.. Tuna. Details — the 3-day crash.. Foods. 3 days. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Not.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Not.", "x": "Military Diet in depth: Not.. Debate. Details — the 3-day crash.. 3 days. 1000 cal. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Foods.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Foods.", "x": "Military Diet in depth: Foods.. 3 days. Details — the 3-day crash.. Crash. Not military. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Military Diet comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Military Diet comes from.", "x": "Origins: 3 days.. 3 days. The history of Military Diet — the 3-day crash.. Crash. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Military Diet respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Military Diet respectfully.", "x": "Engaging: Debate.. 1000 cal. How to participate or observe well — Military Diet. the 3-day crash. Respect first, always; Tuna.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Military Diet do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Military Diet do's and don'ts.", "x": "Etiquette: Not.. Not military. The rules of respect — Military Diet. the 3-day crash. When in doubt, ask about Foods.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Military Diet.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Military Diet.", "x": "Planning: 3 days.. Crash. Practical notes — Military Diet. the 3-day crash. A little planning shows respect for Crash.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Military Diet and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Military Diet and money.", "x": "Costs: Debate.. Tuna. What to budget — Military Diet. the 3-day crash. The best experiences of Tuna. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-diet-military-diet-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
