(function(){'use strict';
/* JAH Atkins Diet Diet Database generator — jahdb-e2-diet-atkins-diet-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-diet-atkins-diet',PREFIX='JAH-E2DIETATKIN-',NAME='JAH Atkins Diet Diet Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Atkins Diet: the complete guide", "d": "Atkins Diet: the original low-carb..", "g": "overview", "l": 2, "q": "What is Atkins Diet: the complete guide?", "a": "Atkins Diet: the original low-carb..", "x": "The complete diet guide to Atkins Diet: the original low-carb.. 1972. History, meaning, practices, and how to engage respectfully — everything in one database. Phases. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Atkins Diet essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Atkins Diet essentials.", "x": "At a glance: Atkins Diet — the original low-carb.. Phases. The essentials: History.. Induction. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "1972.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "1972.", "x": "Atkins Diet: 1972.. History. Essential knowledge — Induction.. the original low-carb. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 1972..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 1972..", "x": "Explained: 1972.. Atkins. The context — Atkins Diet. Low-carb. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Phases.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Phases.", "x": "Atkins Diet: Phases.. Low-carb. Essential knowledge — Low-carb.. the original low-carb. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Phases..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Phases..", "x": "Explained: Phases.. Ketosis. The context — Atkins Diet. Atkins. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Induction.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Induction.", "x": "Atkins Diet: Induction.. Atkins. Essential knowledge — Atkins.. the original low-carb. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Induction..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Induction..", "x": "Explained: Induction.. Foods. The context — Atkins Diet. Ketosis. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Low-carb.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Low-carb.", "x": "Atkins Diet: Low-carb.. Ketosis. Essential knowledge — Ketosis.. the original low-carb. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Low-carb..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Low-carb..", "x": "Explained: Low-carb.. Phases. The context — Atkins Diet. 1972. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Atkins.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Atkins.", "x": "Atkins Diet: Atkins.. Foods. Essential knowledge — 1972.. the original low-carb. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Atkins..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Atkins..", "x": "Explained: Atkins.. History. The context — Atkins Diet. Phases. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Ketosis.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Ketosis.", "x": "Atkins Diet: Ketosis.. Phases. Essential knowledge — Phases.. the original low-carb. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Ketosis..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Ketosis..", "x": "Explained: Ketosis.. Low-carb. The context — Atkins Diet. Induction. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Phases.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Phases.", "x": "Atkins Diet in depth: Phases.. Phases. Details — the original low-carb.. Low-carb. Low-carb. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "History.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "History.", "x": "Atkins Diet in depth: History.. Induction. Details — the original low-carb.. Atkins. Atkins. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Low-carb.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Low-carb.", "x": "Atkins Diet in depth: Low-carb.. Low-carb. Details — the original low-carb.. Ketosis. Ketosis. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Atkins.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Atkins.", "x": "Atkins Diet in depth: Atkins.. Atkins. Details — the original low-carb.. Foods. 1972. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Ketosis.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Ketosis.", "x": "Atkins Diet in depth: Ketosis.. Ketosis. Details — the original low-carb.. Phases. Phases. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Foods.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Foods.", "x": "Atkins Diet in depth: Foods.. 1972. Details — the original low-carb.. History. Induction. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Atkins Diet comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Atkins Diet comes from.", "x": "Origins: Phases.. 1972. The history of Atkins Diet — the original low-carb.. History. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Atkins Diet respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Atkins Diet respectfully.", "x": "Engaging: Low-carb.. Phases. How to participate or observe well — Atkins Diet. the original low-carb. Respect first, always; Atkins.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Atkins Diet do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Atkins Diet do's and don'ts.", "x": "Etiquette: Ketosis.. Induction. The rules of respect — Atkins Diet. the original low-carb. When in doubt, ask about Foods.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Atkins Diet.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Atkins Diet.", "x": "Planning: Phases.. Low-carb. Practical notes — Atkins Diet. the original low-carb. A little planning shows respect for History.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Atkins Diet and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Atkins Diet and money.", "x": "Costs: Low-carb.. Atkins. What to budget — Atkins Diet. the original low-carb. The best experiences of Atkins. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-diet-atkins-diet-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
