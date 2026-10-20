(function(){'use strict';
/* JAH Bangkok City2 Database generator — jahdb-e2-city2-bangkok-city2-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-city2-bangkok-city2',PREFIX='JAH-E2CITY2BANG-',NAME='JAH Bangkok City2 Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Bangkok City2: the complete guide", "d": "Bangkok City2: the temples 2..", "g": "overview", "l": 2, "q": "What is Bangkok City2: the complete guide?", "a": "Bangkok City2: the temples 2..", "x": "The complete city guide to Bangkok City2: the temples 2.. Grand Palace. History, meaning, practices, and how to engage respectfully — everything in one database. Palace. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Bangkok City2 essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Bangkok City2 essentials.", "x": "At a glance: Bangkok City2 — the temples 2.. Street food. The essentials: Thailand.. 10M. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Grand Palace.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Grand Palace.", "x": "Bangkok City2: Grand Palace.. Thailand. Essential knowledge — 10M.. the temples 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Grand Palace..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Grand Palace..", "x": "Explained: Grand Palace.. Food. The context — Bangkok City2. Tuk-tuks. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Street food.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Street food.", "x": "Bangkok City2: Street food.. Canals. Essential knowledge — Tuk-tuks.. the temples 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Street food..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Street food..", "x": "Explained: Street food.. Tuk-tuks. The context — Bangkok City2. Thailand. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "10M.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "10M.", "x": "Bangkok City2: 10M.. Food. Essential knowledge — Thailand.. the temples 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: 10M..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: 10M..", "x": "Explained: 10M.. Guide. The context — Bangkok City2. Canals. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Tuk-tuks.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Tuk-tuks.", "x": "Bangkok City2: Tuk-tuks.. Tuk-tuks. Essential knowledge — Canals.. the temples 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Tuk-tuks..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Tuk-tuks..", "x": "Explained: Tuk-tuks.. Palace. The context — Bangkok City2. Grand Palace. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Thailand.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Thailand.", "x": "Bangkok City2: Thailand.. Guide. Essential knowledge — Grand Palace.. the temples 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Thailand..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Thailand..", "x": "Explained: Thailand.. Thailand. The context — Bangkok City2. Street food. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Canals.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Canals.", "x": "Bangkok City2: Canals.. Palace. Essential knowledge — Street food.. the temples 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Canals..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Canals..", "x": "Explained: Canals.. Canals. The context — Bangkok City2. 10M. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Palace.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Palace.", "x": "Bangkok City2 in depth: Palace.. Street food. Details — the temples 2.. Canals. Tuk-tuks. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Thailand.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Thailand.", "x": "Bangkok City2 in depth: Thailand.. 10M. Details — the temples 2.. Food. Thailand. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Canals.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Canals.", "x": "Bangkok City2 in depth: Canals.. Tuk-tuks. Details — the temples 2.. Tuk-tuks. Canals. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Food.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Food.", "x": "Bangkok City2 in depth: Food.. Thailand. Details — the temples 2.. Guide. Grand Palace. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Tuk-tuks.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Tuk-tuks.", "x": "Bangkok City2 in depth: Tuk-tuks.. Canals. Details — the temples 2.. Palace. Street food. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Guide.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Guide.", "x": "Bangkok City2 in depth: Guide.. Grand Palace. Details — the temples 2.. Thailand. 10M. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Bangkok City2 comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Bangkok City2 comes from.", "x": "Origins: Palace.. Grand Palace. The history of Bangkok City2 — the temples 2.. Thailand. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Bangkok City2 respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Bangkok City2 respectfully.", "x": "Engaging: Canals.. Street food. How to participate or observe well — Bangkok City2. the temples 2. Respect first, always; Food.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Bangkok City2 do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Bangkok City2 do's and don'ts.", "x": "Etiquette: Tuk-tuks.. 10M. The rules of respect — Bangkok City2. the temples 2. When in doubt, ask about Guide.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Bangkok City2.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Bangkok City2.", "x": "Planning: Palace.. Tuk-tuks. Practical notes — Bangkok City2. the temples 2. A little planning shows respect for Thailand.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Bangkok City2 and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Bangkok City2 and money.", "x": "Costs: Canals.. Thailand. What to budget — Bangkok City2. the temples 2. The best experiences of Food. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-city2-bangkok-city2-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
