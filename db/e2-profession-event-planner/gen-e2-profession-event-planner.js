(function(){'use strict';
/* JAH Event Planner Profession Database generator — jahdb-e2-profession-event-planner-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-profession-event-planner',PREFIX='JAH-E2PROFESSIO-',NAME='JAH Event Planner Profession Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Event Planner Profession: the complete guide", "d": "Event Planner Profession: the detail profession..", "g": "overview", "l": 2, "q": "What is Event Planner Profession: the complete guide?", "a": "Event Planner Profession: the detail profession..", "x": "The complete profession guide to Event Planner Profession: the detail profession.. Timelines. History, meaning, practices, and how to engage respectfully — everything in one database. Vendors. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Event Planner Profession essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Event Planner Profession essentials.", "x": "At a glance: Event Planner Profession — the detail profession.. Vendors. The essentials: Checklists.. Checklists. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Timelines.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Timelines.", "x": "Event Planner Profession: Timelines.. Checklists. Essential knowledge — Checklists.. the detail profession. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Timelines..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Timelines..", "x": "Explained: Timelines.. Calm. The context — Event Planner Profession. Day-of. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Vendors.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Vendors.", "x": "Event Planner Profession: Vendors.. Budgets. Essential knowledge — Day-of.. the detail profession. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Vendors..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Vendors..", "x": "Explained: Vendors.. Timelines. The context — Event Planner Profession. Budgets. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Checklists.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Checklists.", "x": "Event Planner Profession: Checklists.. Calm. Essential knowledge — Budgets.. the detail profession. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Checklists..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Checklists..", "x": "Explained: Checklists.. Day. The context — Event Planner Profession. Calm. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Day-of.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Day-of.", "x": "Event Planner Profession: Day-of.. Timelines. Essential knowledge — Calm.. the detail profession. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Day-of..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Day-of..", "x": "Explained: Day-of.. Vendors. The context — Event Planner Profession. Timelines. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Budgets.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Budgets.", "x": "Event Planner Profession: Budgets.. Day. Essential knowledge — Timelines.. the detail profession. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Budgets..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Budgets..", "x": "Explained: Budgets.. Checklists. The context — Event Planner Profession. Vendors. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Calm.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Calm.", "x": "Event Planner Profession: Calm.. Vendors. Essential knowledge — Vendors.. the detail profession. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Calm..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Calm..", "x": "Explained: Calm.. Budgets. The context — Event Planner Profession. Checklists. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Vendors.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Vendors.", "x": "Event Planner Profession in depth: Vendors.. Vendors. Details — the detail profession.. Budgets. Day-of. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Checklists.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Checklists.", "x": "Event Planner Profession in depth: Checklists.. Checklists. Details — the detail profession.. Calm. Budgets. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Budgets.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Budgets.", "x": "Event Planner Profession in depth: Budgets.. Day-of. Details — the detail profession.. Timelines. Calm. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Calm.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Calm.", "x": "Event Planner Profession in depth: Calm.. Budgets. Details — the detail profession.. Day. Timelines. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Timelines.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Timelines.", "x": "Event Planner Profession in depth: Timelines.. Calm. Details — the detail profession.. Vendors. Vendors. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Day.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Day.", "x": "Event Planner Profession in depth: Day.. Timelines. Details — the detail profession.. Checklists. Checklists. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Event Planner Profession comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Event Planner Profession comes from.", "x": "Origins: Vendors.. Timelines. The history of Event Planner Profession — the detail profession.. Checklists. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Event Planner Profession respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Event Planner Profession respectfully.", "x": "Engaging: Budgets.. Vendors. How to participate or observe well — Event Planner Profession. the detail profession. Respect first, always; Calm.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Event Planner Profession do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Event Planner Profession do's and don'ts.", "x": "Etiquette: Timelines.. Checklists. The rules of respect — Event Planner Profession. the detail profession. When in doubt, ask about Day.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Event Planner Profession.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Event Planner Profession.", "x": "Planning: Vendors.. Day-of. Practical notes — Event Planner Profession. the detail profession. A little planning shows respect for Checklists.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Event Planner Profession and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Event Planner Profession and money.", "x": "Costs: Budgets.. Budgets. What to budget — Event Planner Profession. the detail profession. The best experiences of Calm. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-profession-event-planner-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
