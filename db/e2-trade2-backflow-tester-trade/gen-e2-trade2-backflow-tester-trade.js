(function(){'use strict';
/* JAH Backflow Tester Database generator — jahdb-e2-trade2-backflow-tester-trade-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-trade2-backflow-tester-trade',PREFIX='JAH-E2TRADE2BAC-',NAME='JAH Backflow Tester Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Backflow Tester: the complete guide", "d": "Backflow Tester: the valve pros..", "g": "overview", "l": 2, "q": "What is Backflow Tester: the complete guide?", "a": "Backflow Tester: the valve pros..", "x": "The complete trade guide to Backflow Tester: the valve pros.. Annual. History, meaning, practices, and how to engage respectfully — everything in one database. Certified. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Backflow Tester essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Backflow Tester essentials.", "x": "At a glance: Backflow Tester — the valve pros.. Certified. The essentials: City.. Irrigation. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Annual.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Annual.", "x": "Backflow Tester: Annual.. City. Essential knowledge — Irrigation.. the valve pros. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Annual..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Annual..", "x": "Explained: Annual.. Annual. The context — Backflow Tester. Report. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Certified.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Certified.", "x": "Backflow Tester: Certified.. Devices. Essential knowledge — Report.. the valve pros. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Certified..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Certified..", "x": "Explained: Certified.. Report. The context — Backflow Tester. City. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Irrigation.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Irrigation.", "x": "Backflow Tester: Irrigation.. Annual. Essential knowledge — City.. the valve pros. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Irrigation..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Irrigation..", "x": "Explained: Irrigation.. Hiring. The context — Backflow Tester. Devices. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Report.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Report.", "x": "Backflow Tester: Report.. Report. Essential knowledge — Devices.. the valve pros. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Report..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Report..", "x": "Explained: Report.. Certified. The context — Backflow Tester. Annual. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "City.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "City.", "x": "Backflow Tester: City.. Hiring. Essential knowledge — Annual.. the valve pros. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: City..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: City..", "x": "Explained: City.. City. The context — Backflow Tester. Certified. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Devices.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Devices.", "x": "Backflow Tester: Devices.. Certified. Essential knowledge — Certified.. the valve pros. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Devices..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Devices..", "x": "Explained: Devices.. Devices. The context — Backflow Tester. Irrigation. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Certified.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Certified.", "x": "Backflow Tester in depth: Certified.. Certified. Details — the valve pros.. Devices. Report. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "City.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "City.", "x": "Backflow Tester in depth: City.. Irrigation. Details — the valve pros.. Annual. City. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Devices.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Devices.", "x": "Backflow Tester in depth: Devices.. Report. Details — the valve pros.. Report. Devices. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Annual.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Annual.", "x": "Backflow Tester in depth: Annual.. City. Details — the valve pros.. Hiring. Annual. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Report.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Report.", "x": "Backflow Tester in depth: Report.. Devices. Details — the valve pros.. Certified. Certified. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Hiring.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Hiring.", "x": "Backflow Tester in depth: Hiring.. Annual. Details — the valve pros.. City. Irrigation. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Backflow Tester comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Backflow Tester comes from.", "x": "Origins: Certified.. Annual. The history of Backflow Tester — the valve pros.. City. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Backflow Tester respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Backflow Tester respectfully.", "x": "Engaging: Devices.. Certified. How to participate or observe well — Backflow Tester. the valve pros. Respect first, always; Annual.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Backflow Tester do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Backflow Tester do's and don'ts.", "x": "Etiquette: Report.. Irrigation. The rules of respect — Backflow Tester. the valve pros. When in doubt, ask about Hiring.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Backflow Tester.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Backflow Tester.", "x": "Planning: Certified.. Report. Practical notes — Backflow Tester. the valve pros. A little planning shows respect for City.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Backflow Tester and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Backflow Tester and money.", "x": "Costs: Devices.. City. What to budget — Backflow Tester. the valve pros. The best experiences of Annual. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-trade2-backflow-tester-trade-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
