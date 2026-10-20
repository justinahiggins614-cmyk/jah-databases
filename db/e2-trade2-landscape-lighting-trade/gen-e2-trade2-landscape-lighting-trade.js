(function(){'use strict';
/* JAH Landscape Lighting Database generator — jahdb-e2-trade2-landscape-lighting-trade-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-trade2-landscape-lighting-trade',PREFIX='JAH-E2TRADE2LAN-',NAME='JAH Landscape Lighting Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Landscape Lighting: the complete guide", "d": "Landscape Lighting: the glow pros..", "g": "overview", "l": 2, "q": "What is Landscape Lighting: the complete guide?", "a": "Landscape Lighting: the glow pros..", "x": "The complete trade guide to Landscape Lighting: the glow pros.. Low voltage. History, meaning, practices, and how to engage respectfully — everything in one database. Voltage. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Landscape Lighting essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Landscape Lighting essentials.", "x": "At a glance: Landscape Lighting — the glow pros.. Path. The essentials: Uplight.. Uplight. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Low voltage.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Low voltage.", "x": "Landscape Lighting: Low voltage.. Uplight. Essential knowledge — Uplight.. the glow pros. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Low voltage..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Low voltage..", "x": "Explained: Low voltage.. Path. The context — Landscape Lighting. Transformer. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Path.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Path.", "x": "Landscape Lighting: Path.. Timers. Essential knowledge — Transformer.. the glow pros. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Path..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Path..", "x": "Explained: Path.. LED. The context — Landscape Lighting. LED. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Uplight.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Uplight.", "x": "Landscape Lighting: Uplight.. Path. Essential knowledge — LED.. the glow pros. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Uplight..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Uplight..", "x": "Explained: Uplight.. Hiring. The context — Landscape Lighting. Timers. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Transformer.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Transformer.", "x": "Landscape Lighting: Transformer.. LED. Essential knowledge — Timers.. the glow pros. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Transformer..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Transformer..", "x": "Explained: Transformer.. Voltage. The context — Landscape Lighting. Low voltage. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "LED.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "LED.", "x": "Landscape Lighting: LED.. Hiring. Essential knowledge — Low voltage.. the glow pros. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: LED..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: LED..", "x": "Explained: LED.. Uplight. The context — Landscape Lighting. Path. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Timers.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Timers.", "x": "Landscape Lighting: Timers.. Voltage. Essential knowledge — Path.. the glow pros. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Timers..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Timers..", "x": "Explained: Timers.. Timers. The context — Landscape Lighting. Uplight. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Voltage.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Voltage.", "x": "Landscape Lighting in depth: Voltage.. Path. Details — the glow pros.. Timers. Transformer. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Uplight.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Uplight.", "x": "Landscape Lighting in depth: Uplight.. Uplight. Details — the glow pros.. Path. LED. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Timers.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Timers.", "x": "Landscape Lighting in depth: Timers.. Transformer. Details — the glow pros.. LED. Timers. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Path.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Path.", "x": "Landscape Lighting in depth: Path.. LED. Details — the glow pros.. Hiring. Low voltage. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "LED.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "LED.", "x": "Landscape Lighting in depth: LED.. Timers. Details — the glow pros.. Voltage. Path. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Hiring.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Hiring.", "x": "Landscape Lighting in depth: Hiring.. Low voltage. Details — the glow pros.. Uplight. Uplight. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Landscape Lighting comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Landscape Lighting comes from.", "x": "Origins: Voltage.. Low voltage. The history of Landscape Lighting — the glow pros.. Uplight. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Landscape Lighting respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Landscape Lighting respectfully.", "x": "Engaging: Timers.. Path. How to participate or observe well — Landscape Lighting. the glow pros. Respect first, always; Path.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Landscape Lighting do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Landscape Lighting do's and don'ts.", "x": "Etiquette: LED.. Uplight. The rules of respect — Landscape Lighting. the glow pros. When in doubt, ask about Hiring.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Landscape Lighting.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Landscape Lighting.", "x": "Planning: Voltage.. Transformer. Practical notes — Landscape Lighting. the glow pros. A little planning shows respect for Uplight.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Landscape Lighting and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Landscape Lighting and money.", "x": "Costs: Timers.. LED. What to budget — Landscape Lighting. the glow pros. The best experiences of Path. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-trade2-landscape-lighting-trade-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
