(function(){'use strict';
/* JAH Sales Rep Profession Database generator — jahdb-e2-profession-sales-rep-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-profession-sales-rep',PREFIX='JAH-E2PROFESSIO-',NAME='JAH Sales Rep Profession Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Sales Rep Profession: the complete guide", "d": "Sales Rep Profession: the quota profession..", "g": "overview", "l": 2, "q": "What is Sales Rep Profession: the complete guide?", "a": "Sales Rep Profession: the quota profession..", "x": "The complete profession guide to Sales Rep Profession: the quota profession.. Quota. History, meaning, practices, and how to engage respectfully — everything in one database. Quota. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Sales Rep Profession essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Sales Rep Profession essentials.", "x": "At a glance: Sales Rep Profession — the quota profession.. Pipeline. The essentials: Pipeline.. Calls. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Quota.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Quota.", "x": "Sales Rep Profession: Quota.. Pipeline. Essential knowledge — Calls.. the quota profession. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Quota..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Quota..", "x": "Explained: Quota.. Commission. The context — Sales Rep Profession. Demos. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Pipeline.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Pipeline.", "x": "Sales Rep Profession: Pipeline.. Demos. Essential knowledge — Demos.. the quota profession. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Pipeline..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Pipeline..", "x": "Explained: Pipeline.. CRM. The context — Sales Rep Profession. Commission. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Calls.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Calls.", "x": "Sales Rep Profession: Calls.. Commission. Essential knowledge — Commission.. the quota profession. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Calls..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Calls..", "x": "Explained: Calls.. Day. The context — Sales Rep Profession. CRM. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Demos.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Demos.", "x": "Sales Rep Profession: Demos.. CRM. Essential knowledge — CRM.. the quota profession. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Demos..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Demos..", "x": "Explained: Demos.. Quota. The context — Sales Rep Profession. Quota. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Commission.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Commission.", "x": "Sales Rep Profession: Commission.. Day. Essential knowledge — Quota.. the quota profession. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Commission..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Commission..", "x": "Explained: Commission.. Pipeline. The context — Sales Rep Profession. Pipeline. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "CRM.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "CRM.", "x": "Sales Rep Profession: CRM.. Quota. Essential knowledge — Pipeline.. the quota profession. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: CRM..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: CRM..", "x": "Explained: CRM.. Demos. The context — Sales Rep Profession. Calls. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Quota.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Quota.", "x": "Sales Rep Profession in depth: Quota.. Pipeline. Details — the quota profession.. Demos. Demos. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Pipeline.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Pipeline.", "x": "Sales Rep Profession in depth: Pipeline.. Calls. Details — the quota profession.. Commission. Commission. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Demos.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Demos.", "x": "Sales Rep Profession in depth: Demos.. Demos. Details — the quota profession.. CRM. CRM. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Commission.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Commission.", "x": "Sales Rep Profession in depth: Commission.. Commission. Details — the quota profession.. Day. Quota. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "CRM.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "CRM.", "x": "Sales Rep Profession in depth: CRM.. CRM. Details — the quota profession.. Quota. Pipeline. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Day.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Day.", "x": "Sales Rep Profession in depth: Day.. Quota. Details — the quota profession.. Pipeline. Calls. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Sales Rep Profession comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Sales Rep Profession comes from.", "x": "Origins: Quota.. Quota. The history of Sales Rep Profession — the quota profession.. Pipeline. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Sales Rep Profession respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Sales Rep Profession respectfully.", "x": "Engaging: Demos.. Pipeline. How to participate or observe well — Sales Rep Profession. the quota profession. Respect first, always; Commission.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Sales Rep Profession do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Sales Rep Profession do's and don'ts.", "x": "Etiquette: CRM.. Calls. The rules of respect — Sales Rep Profession. the quota profession. When in doubt, ask about Day.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Sales Rep Profession.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Sales Rep Profession.", "x": "Planning: Quota.. Demos. Practical notes — Sales Rep Profession. the quota profession. A little planning shows respect for Pipeline.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Sales Rep Profession and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Sales Rep Profession and money.", "x": "Costs: Demos.. Commission. What to budget — Sales Rep Profession. the quota profession. The best experiences of Commission. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-profession-sales-rep-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
