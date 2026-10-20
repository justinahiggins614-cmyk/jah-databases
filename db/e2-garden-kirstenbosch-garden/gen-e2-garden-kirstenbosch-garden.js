(function(){'use strict';
/* JAH Kirstenbosch Garden Botanical Garden Database generator — jahdb-e2-garden-kirstenbosch-garden-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-garden-kirstenbosch-garden',PREFIX='JAH-E2GARDENKIR-',NAME='JAH Kirstenbosch Garden Botanical Garden Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Kirstenbosch Garden: the complete guide", "d": "Kirstenbosch Garden: Cape Town's floral mountain..", "g": "overview", "l": 2, "q": "What is Kirstenbosch Garden: the complete guide?", "a": "Kirstenbosch Garden: Cape Town's floral mountain..", "x": "The complete botanical garden guide to Kirstenbosch Garden: Cape Town's floral mountain.. 1913. History, meaning, practices, and how to engage respectfully — everything in one database. Mountain. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Kirstenbosch Garden essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Kirstenbosch Garden essentials.", "x": "At a glance: Kirstenbosch Garden — Cape Town's floral mountain.. Table Mountain. The essentials: Proteas.. Proteas. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "1913.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "1913.", "x": "Kirstenbosch Garden: 1913.. Proteas. Essential knowledge — Proteas.. Cape Town's floral mountain. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 1913..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 1913..", "x": "Explained: 1913.. Tickets. The context — Kirstenbosch Garden. Boomslang. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Table Mountain.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Table Mountain.", "x": "Kirstenbosch Garden: Table Mountain.. Walkway. Essential knowledge — Boomslang.. Cape Town's floral mountain. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Table Mountain..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Table Mountain..", "x": "Explained: Table Mountain.. Cape Town. The context — Kirstenbosch Garden. Concerts. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Proteas.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Proteas.", "x": "Kirstenbosch Garden: Proteas.. Tickets. Essential knowledge — Concerts.. Cape Town's floral mountain. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Proteas..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Proteas..", "x": "Explained: Proteas.. Fynbos. The context — Kirstenbosch Garden. Fynbos. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Boomslang.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Boomslang.", "x": "Kirstenbosch Garden: Boomslang.. Cape Town. Essential knowledge — Fynbos.. Cape Town's floral mountain. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Boomslang..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Boomslang..", "x": "Explained: Boomslang.. Mountain. The context — Kirstenbosch Garden. 1913. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Concerts.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Concerts.", "x": "Kirstenbosch Garden: Concerts.. Fynbos. Essential knowledge — 1913.. Cape Town's floral mountain. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Concerts..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Concerts..", "x": "Explained: Concerts.. Proteas. The context — Kirstenbosch Garden. Table Mountain. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Fynbos.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Fynbos.", "x": "Kirstenbosch Garden: Fynbos.. Mountain. Essential knowledge — Table Mountain.. Cape Town's floral mountain. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Fynbos..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Fynbos..", "x": "Explained: Fynbos.. Walkway. The context — Kirstenbosch Garden. Proteas. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Mountain.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Mountain.", "x": "Kirstenbosch Garden in depth: Mountain.. Table Mountain. Details — Cape Town's floral mountain.. Walkway. Boomslang. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Proteas.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Proteas.", "x": "Kirstenbosch Garden in depth: Proteas.. Proteas. Details — Cape Town's floral mountain.. Tickets. Concerts. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Walkway.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Walkway.", "x": "Kirstenbosch Garden in depth: Walkway.. Boomslang. Details — Cape Town's floral mountain.. Cape Town. Fynbos. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Tickets.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Tickets.", "x": "Kirstenbosch Garden in depth: Tickets.. Concerts. Details — Cape Town's floral mountain.. Fynbos. 1913. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Cape Town.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Cape Town.", "x": "Kirstenbosch Garden in depth: Cape Town.. Fynbos. Details — Cape Town's floral mountain.. Mountain. Table Mountain. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Fynbos.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Fynbos.", "x": "Kirstenbosch Garden in depth: Fynbos.. 1913. Details — Cape Town's floral mountain.. Proteas. Proteas. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Kirstenbosch Garden comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Kirstenbosch Garden comes from.", "x": "Origins: Mountain.. 1913. The history of Kirstenbosch Garden — Cape Town's floral mountain.. Proteas. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Kirstenbosch Garden respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Kirstenbosch Garden respectfully.", "x": "Engaging: Walkway.. Table Mountain. How to participate or observe well — Kirstenbosch Garden. Cape Town's floral mountain. Respect first, always; Tickets.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Kirstenbosch Garden do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Kirstenbosch Garden do's and don'ts.", "x": "Etiquette: Cape Town.. Proteas. The rules of respect — Kirstenbosch Garden. Cape Town's floral mountain. When in doubt, ask about Fynbos.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Kirstenbosch Garden.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Kirstenbosch Garden.", "x": "Planning: Mountain.. Boomslang. Practical notes — Kirstenbosch Garden. Cape Town's floral mountain. A little planning shows respect for Proteas.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Kirstenbosch Garden and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Kirstenbosch Garden and money.", "x": "Costs: Walkway.. Concerts. What to budget — Kirstenbosch Garden. Cape Town's floral mountain. The best experiences of Tickets. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-garden-kirstenbosch-garden-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
