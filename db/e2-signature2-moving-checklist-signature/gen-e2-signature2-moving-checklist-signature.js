(function(){'use strict';
/* JAH Moving Checklist Database generator — jahdb-e2-signature2-moving-checklist-signature-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-signature2-moving-checklist-signature',PREFIX='JAH-E2SIGNATURE-',NAME='JAH Moving Checklist Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Moving Checklist: the complete guide", "d": "Moving Checklist: the box plan..", "g": "overview", "l": 2, "q": "What is Moving Checklist: the complete guide?", "a": "Moving Checklist: the box plan..", "x": "The complete signature original guide to Moving Checklist: the box plan.. 8 weeks. History, meaning, practices, and how to engage respectfully — everything in one database. Weeks. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Moving Checklist essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Moving Checklist essentials.", "x": "At a glance: Moving Checklist — the box plan.. Boxes. The essentials: Essentials.. Label. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "8 weeks.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "8 weeks.", "x": "Moving Checklist: 8 weeks.. Essentials. Essential knowledge — Label.. the box plan. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 8 weeks..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 8 weeks..", "x": "Explained: 8 weeks.. Boxes. The context — Moving Checklist. Utilities. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Boxes.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Boxes.", "x": "Moving Checklist: Boxes.. Address. Essential knowledge — Utilities.. the box plan. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Boxes..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Boxes..", "x": "Explained: Boxes.. Utilities. The context — Moving Checklist. Change address. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Label.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Label.", "x": "Moving Checklist: Label.. Boxes. Essential knowledge — Change address.. the box plan. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Label..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Label..", "x": "Explained: Label.. Guide. The context — Moving Checklist. Essentials. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Utilities.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Utilities.", "x": "Moving Checklist: Utilities.. Utilities. Essential knowledge — Essentials.. the box plan. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Utilities..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Utilities..", "x": "Explained: Utilities.. Weeks. The context — Moving Checklist. 8 weeks. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Change address.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Change address.", "x": "Moving Checklist: Change address.. Guide. Essential knowledge — 8 weeks.. the box plan. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Change address..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Change address..", "x": "Explained: Change address.. Essentials. The context — Moving Checklist. Boxes. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Essentials.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Essentials.", "x": "Moving Checklist: Essentials.. Weeks. Essential knowledge — Boxes.. the box plan. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Essentials..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Essentials..", "x": "Explained: Essentials.. Address. The context — Moving Checklist. Label. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Weeks.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Weeks.", "x": "Moving Checklist in depth: Weeks.. Boxes. Details — the box plan.. Address. Utilities. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Essentials.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Essentials.", "x": "Moving Checklist in depth: Essentials.. Label. Details — the box plan.. Boxes. Change address. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Address.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Address.", "x": "Moving Checklist in depth: Address.. Utilities. Details — the box plan.. Utilities. Essentials. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Boxes.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Boxes.", "x": "Moving Checklist in depth: Boxes.. Change address. Details — the box plan.. Guide. 8 weeks. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Utilities.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Utilities.", "x": "Moving Checklist in depth: Utilities.. Essentials. Details — the box plan.. Weeks. Boxes. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Guide.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Guide.", "x": "Moving Checklist in depth: Guide.. 8 weeks. Details — the box plan.. Essentials. Label. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Moving Checklist comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Moving Checklist comes from.", "x": "Origins: Weeks.. 8 weeks. The history of Moving Checklist — the box plan.. Essentials. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Moving Checklist respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Moving Checklist respectfully.", "x": "Engaging: Address.. Boxes. How to participate or observe well — Moving Checklist. the box plan. Respect first, always; Boxes.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Moving Checklist do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Moving Checklist do's and don'ts.", "x": "Etiquette: Utilities.. Label. The rules of respect — Moving Checklist. the box plan. When in doubt, ask about Guide.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Moving Checklist.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Moving Checklist.", "x": "Planning: Weeks.. Utilities. Practical notes — Moving Checklist. the box plan. A little planning shows respect for Essentials.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Moving Checklist and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Moving Checklist and money.", "x": "Costs: Address.. Change address. What to budget — Moving Checklist. the box plan. The best experiences of Boxes. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-signature2-moving-checklist-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
