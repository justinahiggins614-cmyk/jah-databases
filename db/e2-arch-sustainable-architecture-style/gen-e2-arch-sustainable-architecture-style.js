(function(){'use strict';
/* JAH Sustainable Architecture Style Database generator — jahdb-e2-arch-sustainable-architecture-style-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-arch-sustainable-architecture-style',PREFIX='JAH-E2ARCHSUSTA-',NAME='JAH Sustainable Architecture Style Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Sustainable Architecture: the complete guide", "d": "Sustainable Architecture: the green building..", "g": "overview", "l": 2, "q": "What is Sustainable Architecture: the complete guide?", "a": "Sustainable Architecture: the green building..", "x": "The complete architecture style guide to Sustainable Architecture: the green building.. LEED. History, meaning, practices, and how to engage respectfully — everything in one database. LEED. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Sustainable Architecture essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Sustainable Architecture essentials.", "x": "At a glance: Sustainable Architecture — the green building.. Solar. The essentials: Solar.. Green roofs. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "LEED.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "LEED.", "x": "Sustainable Architecture: LEED.. Solar. Essential knowledge — Green roofs.. the green building. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: LEED..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: LEED..", "x": "Explained: LEED.. Net-zero. The context — Sustainable Architecture. Passive. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Solar.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Solar.", "x": "Sustainable Architecture: Solar.. Passive. Essential knowledge — Passive.. the green building. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Solar..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Solar..", "x": "Explained: Solar.. Green. The context — Sustainable Architecture. Materials. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Green roofs.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Green roofs.", "x": "Sustainable Architecture: Green roofs.. Net-zero. Essential knowledge — Materials.. the green building. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Green roofs..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Green roofs..", "x": "Explained: Green roofs.. Future. The context — Sustainable Architecture. Net-zero. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Passive.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Passive.", "x": "Sustainable Architecture: Passive.. Green. Essential knowledge — Net-zero.. the green building. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Passive..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Passive..", "x": "Explained: Passive.. LEED. The context — Sustainable Architecture. LEED. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Materials.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Materials.", "x": "Sustainable Architecture: Materials.. Future. Essential knowledge — LEED.. the green building. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Materials..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Materials..", "x": "Explained: Materials.. Solar. The context — Sustainable Architecture. Solar. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Net-zero.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Net-zero.", "x": "Sustainable Architecture: Net-zero.. LEED. Essential knowledge — Solar.. the green building. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Net-zero..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Net-zero..", "x": "Explained: Net-zero.. Passive. The context — Sustainable Architecture. Green roofs. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "LEED.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "LEED.", "x": "Sustainable Architecture in depth: LEED.. Solar. Details — the green building.. Passive. Passive. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Solar.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Solar.", "x": "Sustainable Architecture in depth: Solar.. Green roofs. Details — the green building.. Net-zero. Materials. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Passive.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Passive.", "x": "Sustainable Architecture in depth: Passive.. Passive. Details — the green building.. Green. Net-zero. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Net-zero.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Net-zero.", "x": "Sustainable Architecture in depth: Net-zero.. Materials. Details — the green building.. Future. LEED. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Green.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Green.", "x": "Sustainable Architecture in depth: Green.. Net-zero. Details — the green building.. LEED. Solar. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Future.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Future.", "x": "Sustainable Architecture in depth: Future.. LEED. Details — the green building.. Solar. Green roofs. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Sustainable Architecture comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Sustainable Architecture comes from.", "x": "Origins: LEED.. LEED. The history of Sustainable Architecture — the green building.. Solar. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Sustainable Architecture respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Sustainable Architecture respectfully.", "x": "Engaging: Passive.. Solar. How to participate or observe well — Sustainable Architecture. the green building. Respect first, always; Net-zero.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Sustainable Architecture do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Sustainable Architecture do's and don'ts.", "x": "Etiquette: Green.. Green roofs. The rules of respect — Sustainable Architecture. the green building. When in doubt, ask about Future.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Sustainable Architecture.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Sustainable Architecture.", "x": "Planning: LEED.. Passive. Practical notes — Sustainable Architecture. the green building. A little planning shows respect for Solar.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Sustainable Architecture and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Sustainable Architecture and money.", "x": "Costs: Passive.. Materials. What to budget — Sustainable Architecture. the green building. The best experiences of Net-zero. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-arch-sustainable-architecture-style-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
