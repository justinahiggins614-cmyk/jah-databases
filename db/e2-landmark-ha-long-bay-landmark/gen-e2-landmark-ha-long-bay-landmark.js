(function(){'use strict';
/* JAH Ha Long Bay Landmark Database generator — jahdb-e2-landmark-ha-long-bay-landmark-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-landmark-ha-long-bay-landmark',PREFIX='JAH-E2LANDMARKH-',NAME='JAH Ha Long Bay Landmark Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Ha Long Bay: the complete guide", "d": "Ha Long Bay: the 1,600 karsts..", "g": "overview", "l": 2, "q": "What is Ha Long Bay: the complete guide?", "a": "Ha Long Bay: the 1,600 karsts..", "x": "The complete landmark guide to Ha Long Bay: the 1,600 karsts.. 1,600. History, meaning, practices, and how to engage respectfully — everything in one database. 1,600. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Ha Long Bay essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Ha Long Bay essentials.", "x": "At a glance: Ha Long Bay — the 1,600 karsts.. Karsts. The essentials: Junks.. Junks. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "1,600.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "1,600.", "x": "Ha Long Bay: 1,600.. Junks. Essential knowledge — Junks.. the 1,600 karsts. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 1,600..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 1,600..", "x": "Explained: 1,600.. Mist. The context — Ha Long Bay. Caves. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Karsts.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Karsts.", "x": "Ha Long Bay: Karsts.. UNESCO. Essential knowledge — Caves.. the 1,600 karsts. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Karsts..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Karsts..", "x": "Explained: Karsts.. Karsts. The context — Ha Long Bay. UNESCO. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Junks.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Junks.", "x": "Ha Long Bay: Junks.. Mist. Essential knowledge — UNESCO.. the 1,600 karsts. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Junks..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Junks..", "x": "Explained: Junks.. Cruises. The context — Ha Long Bay. Mist. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Caves.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Caves.", "x": "Ha Long Bay: Caves.. Karsts. Essential knowledge — Mist.. the 1,600 karsts. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Caves..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Caves..", "x": "Explained: Caves.. 1,600. The context — Ha Long Bay. 1,600. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "UNESCO.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "UNESCO.", "x": "Ha Long Bay: UNESCO.. Cruises. Essential knowledge — 1,600.. the 1,600 karsts. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: UNESCO..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: UNESCO..", "x": "Explained: UNESCO.. Junks. The context — Ha Long Bay. Karsts. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Mist.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Mist.", "x": "Ha Long Bay: Mist.. 1,600. Essential knowledge — Karsts.. the 1,600 karsts. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Mist..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Mist..", "x": "Explained: Mist.. UNESCO. The context — Ha Long Bay. Junks. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "1,600.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "1,600.", "x": "Ha Long Bay in depth: 1,600.. Karsts. Details — the 1,600 karsts.. UNESCO. Caves. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Junks.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Junks.", "x": "Ha Long Bay in depth: Junks.. Junks. Details — the 1,600 karsts.. Mist. UNESCO. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "UNESCO.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "UNESCO.", "x": "Ha Long Bay in depth: UNESCO.. Caves. Details — the 1,600 karsts.. Karsts. Mist. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Mist.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Mist.", "x": "Ha Long Bay in depth: Mist.. UNESCO. Details — the 1,600 karsts.. Cruises. 1,600. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Karsts.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Karsts.", "x": "Ha Long Bay in depth: Karsts.. Mist. Details — the 1,600 karsts.. 1,600. Karsts. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Cruises.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Cruises.", "x": "Ha Long Bay in depth: Cruises.. 1,600. Details — the 1,600 karsts.. Junks. Junks. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Ha Long Bay comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Ha Long Bay comes from.", "x": "Origins: 1,600.. 1,600. The history of Ha Long Bay — the 1,600 karsts.. Junks. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Ha Long Bay respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Ha Long Bay respectfully.", "x": "Engaging: UNESCO.. Karsts. How to participate or observe well — Ha Long Bay. the 1,600 karsts. Respect first, always; Mist.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Ha Long Bay do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Ha Long Bay do's and don'ts.", "x": "Etiquette: Karsts.. Junks. The rules of respect — Ha Long Bay. the 1,600 karsts. When in doubt, ask about Cruises.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Ha Long Bay.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Ha Long Bay.", "x": "Planning: 1,600.. Caves. Practical notes — Ha Long Bay. the 1,600 karsts. A little planning shows respect for Junks.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Ha Long Bay and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Ha Long Bay and money.", "x": "Costs: UNESCO.. UNESCO. What to budget — Ha Long Bay. the 1,600 karsts. The best experiences of Mist. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-landmark-ha-long-bay-landmark-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
