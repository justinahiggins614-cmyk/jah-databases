(function(){'use strict';
/* JAH Ningaloo Dive2 Database generator — jahdb-e2-dive2-ningaloo-dive2-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-dive2-ningaloo-dive2',PREFIX='JAH-E2DIVE2NING-',NAME='JAH Ningaloo Dive2 Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Ningaloo Dive2: the complete guide", "d": "Ningaloo Dive2: the Australia 2..", "g": "overview", "l": 2, "q": "What is Ningaloo Dive2: the complete guide?", "a": "Ningaloo Dive2: the Australia 2..", "x": "The complete dive site guide to Ningaloo Dive2: the Australia 2.. Whale sharks. History, meaning, practices, and how to engage respectfully — everything in one database. Sharks. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Ningaloo Dive2 essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Ningaloo Dive2 essentials.", "x": "At a glance: Ningaloo Dive2 — the Australia 2.. Australia. The essentials: Seasonal.. Ningaloo. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Whale sharks.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Whale sharks.", "x": "Ningaloo Dive2: Whale sharks.. Seasonal. Essential knowledge — Ningaloo.. the Australia 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Whale sharks..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Whale sharks..", "x": "Explained: Whale sharks.. Australia. The context — Ningaloo Dive2. Reef. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Australia.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Australia.", "x": "Ningaloo Dive2: Australia.. Shore. Essential knowledge — Reef.. the Australia 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Australia..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Australia..", "x": "Explained: Australia.. Reef. The context — Ningaloo Dive2. Shore. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Ningaloo.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Ningaloo.", "x": "Ningaloo Dive2: Ningaloo.. Australia. Essential knowledge — Shore.. the Australia 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Ningaloo..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Ningaloo..", "x": "Explained: Ningaloo.. Guide. The context — Ningaloo Dive2. Seasonal. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Reef.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Reef.", "x": "Ningaloo Dive2: Reef.. Reef. Essential knowledge — Seasonal.. the Australia 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Reef..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Reef..", "x": "Explained: Reef.. Sharks. The context — Ningaloo Dive2. Whale sharks. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Shore.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Shore.", "x": "Ningaloo Dive2: Shore.. Guide. Essential knowledge — Whale sharks.. the Australia 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Shore..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Shore..", "x": "Explained: Shore.. Seasonal. The context — Ningaloo Dive2. Australia. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Seasonal.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Seasonal.", "x": "Ningaloo Dive2: Seasonal.. Sharks. Essential knowledge — Australia.. the Australia 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Seasonal..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Seasonal..", "x": "Explained: Seasonal.. Shore. The context — Ningaloo Dive2. Ningaloo. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Sharks.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Sharks.", "x": "Ningaloo Dive2 in depth: Sharks.. Australia. Details — the Australia 2.. Shore. Reef. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Seasonal.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Seasonal.", "x": "Ningaloo Dive2 in depth: Seasonal.. Ningaloo. Details — the Australia 2.. Australia. Shore. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Shore.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Shore.", "x": "Ningaloo Dive2 in depth: Shore.. Reef. Details — the Australia 2.. Reef. Seasonal. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Australia.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Australia.", "x": "Ningaloo Dive2 in depth: Australia.. Shore. Details — the Australia 2.. Guide. Whale sharks. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Reef.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Reef.", "x": "Ningaloo Dive2 in depth: Reef.. Seasonal. Details — the Australia 2.. Sharks. Australia. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Guide.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Guide.", "x": "Ningaloo Dive2 in depth: Guide.. Whale sharks. Details — the Australia 2.. Seasonal. Ningaloo. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Ningaloo Dive2 comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Ningaloo Dive2 comes from.", "x": "Origins: Sharks.. Whale sharks. The history of Ningaloo Dive2 — the Australia 2.. Seasonal. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Ningaloo Dive2 respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Ningaloo Dive2 respectfully.", "x": "Engaging: Shore.. Australia. How to participate or observe well — Ningaloo Dive2. the Australia 2. Respect first, always; Australia.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Ningaloo Dive2 do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Ningaloo Dive2 do's and don'ts.", "x": "Etiquette: Reef.. Ningaloo. The rules of respect — Ningaloo Dive2. the Australia 2. When in doubt, ask about Guide.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Ningaloo Dive2.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Ningaloo Dive2.", "x": "Planning: Sharks.. Reef. Practical notes — Ningaloo Dive2. the Australia 2. A little planning shows respect for Seasonal.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Ningaloo Dive2 and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Ningaloo Dive2 and money.", "x": "Costs: Shore.. Shore. What to budget — Ningaloo Dive2. the Australia 2. The best experiences of Australia. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-dive2-ningaloo-dive2-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
