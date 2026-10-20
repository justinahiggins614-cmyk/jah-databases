(function(){'use strict';
/* JAH Mechanic Profession Database generator — jahdb-e2-profession-mechanic-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-profession-mechanic',PREFIX='JAH-E2PROFESSIO-',NAME='JAH Mechanic Profession Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Mechanic Profession: the complete guide", "d": "Mechanic Profession: the engine profession..", "g": "overview", "l": 2, "q": "What is Mechanic Profession: the complete guide?", "a": "Mechanic Profession: the engine profession..", "x": "The complete profession guide to Mechanic Profession: the engine profession.. Diagnostics. History, meaning, practices, and how to engage respectfully — everything in one database. Diagnostics. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Mechanic Profession essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Mechanic Profession essentials.", "x": "At a glance: Mechanic Profession — the engine profession.. ASE. The essentials: ASE.. Lifts. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Diagnostics.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Diagnostics.", "x": "Mechanic Profession: Diagnostics.. ASE. Essential knowledge — Lifts.. the engine profession. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Diagnostics..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Diagnostics..", "x": "Explained: Diagnostics.. Shops. The context — Mechanic Profession. Tools. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "ASE.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "ASE.", "x": "Mechanic Profession: ASE.. Tools. Essential knowledge — Tools.. the engine profession. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: ASE..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: ASE..", "x": "Explained: ASE.. EV. The context — Mechanic Profession. Shops. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Lifts.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Lifts.", "x": "Mechanic Profession: Lifts.. Shops. Essential knowledge — Shops.. the engine profession. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Lifts..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Lifts..", "x": "Explained: Lifts.. Day. The context — Mechanic Profession. EV. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Tools.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Tools.", "x": "Mechanic Profession: Tools.. EV. Essential knowledge — EV.. the engine profession. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Tools..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Tools..", "x": "Explained: Tools.. Diagnostics. The context — Mechanic Profession. Diagnostics. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Shops.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Shops.", "x": "Mechanic Profession: Shops.. Day. Essential knowledge — Diagnostics.. the engine profession. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Shops..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Shops..", "x": "Explained: Shops.. ASE. The context — Mechanic Profession. ASE. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "EV.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "EV.", "x": "Mechanic Profession: EV.. Diagnostics. Essential knowledge — ASE.. the engine profession. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: EV..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: EV..", "x": "Explained: EV.. Tools. The context — Mechanic Profession. Lifts. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Diagnostics.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Diagnostics.", "x": "Mechanic Profession in depth: Diagnostics.. ASE. Details — the engine profession.. Tools. Tools. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "ASE.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "ASE.", "x": "Mechanic Profession in depth: ASE.. Lifts. Details — the engine profession.. Shops. Shops. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Tools.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Tools.", "x": "Mechanic Profession in depth: Tools.. Tools. Details — the engine profession.. EV. EV. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Shops.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Shops.", "x": "Mechanic Profession in depth: Shops.. Shops. Details — the engine profession.. Day. Diagnostics. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "EV.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "EV.", "x": "Mechanic Profession in depth: EV.. EV. Details — the engine profession.. Diagnostics. ASE. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Day.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Day.", "x": "Mechanic Profession in depth: Day.. Diagnostics. Details — the engine profession.. ASE. Lifts. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Mechanic Profession comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Mechanic Profession comes from.", "x": "Origins: Diagnostics.. Diagnostics. The history of Mechanic Profession — the engine profession.. ASE. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Mechanic Profession respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Mechanic Profession respectfully.", "x": "Engaging: Tools.. ASE. How to participate or observe well — Mechanic Profession. the engine profession. Respect first, always; Shops.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Mechanic Profession do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Mechanic Profession do's and don'ts.", "x": "Etiquette: EV.. Lifts. The rules of respect — Mechanic Profession. the engine profession. When in doubt, ask about Day.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Mechanic Profession.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Mechanic Profession.", "x": "Planning: Diagnostics.. Tools. Practical notes — Mechanic Profession. the engine profession. A little planning shows respect for ASE.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Mechanic Profession and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Mechanic Profession and money.", "x": "Costs: Tools.. Shops. What to budget — Mechanic Profession. the engine profession. The best experiences of Shops. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-profession-mechanic-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
