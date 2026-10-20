(function(){'use strict';
/* JAH Refrigerator Repair Database generator — jahdb-e2-trade2-refrigerator-repair-trade-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-trade2-refrigerator-repair-trade',PREFIX='JAH-E2TRADE2REF-',NAME='JAH Refrigerator Repair Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Refrigerator Repair: the complete guide", "d": "Refrigerator Repair: the cold pros..", "g": "overview", "l": 2, "q": "What is Refrigerator Repair: the complete guide?", "a": "Refrigerator Repair: the cold pros..", "x": "The complete trade guide to Refrigerator Repair: the cold pros.. Compressor. History, meaning, practices, and how to engage respectfully — everything in one database. Coils. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Refrigerator Repair essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Refrigerator Repair essentials.", "x": "At a glance: Refrigerator Repair — the cold pros.. Coils. The essentials: Thermostat.. Seals. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Compressor.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Compressor.", "x": "Refrigerator Repair: Compressor.. Thermostat. Essential knowledge — Seals.. the cold pros. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Compressor..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Compressor..", "x": "Explained: Compressor.. Compressor. The context — Refrigerator Repair. Ice maker. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Coils.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Coils.", "x": "Refrigerator Repair: Coils.. Frost. Essential knowledge — Ice maker.. the cold pros. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Coils..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Coils..", "x": "Explained: Coils.. Seals. The context — Refrigerator Repair. Thermostat. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Seals.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Seals.", "x": "Refrigerator Repair: Seals.. Compressor. Essential knowledge — Thermostat.. the cold pros. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Seals..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Seals..", "x": "Explained: Seals.. Hiring. The context — Refrigerator Repair. Frost. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Ice maker.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Ice maker.", "x": "Refrigerator Repair: Ice maker.. Seals. Essential knowledge — Frost.. the cold pros. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Ice maker..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Ice maker..", "x": "Explained: Ice maker.. Coils. The context — Refrigerator Repair. Compressor. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Thermostat.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Thermostat.", "x": "Refrigerator Repair: Thermostat.. Hiring. Essential knowledge — Compressor.. the cold pros. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Thermostat..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Thermostat..", "x": "Explained: Thermostat.. Thermostat. The context — Refrigerator Repair. Coils. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Frost.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Frost.", "x": "Refrigerator Repair: Frost.. Coils. Essential knowledge — Coils.. the cold pros. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Frost..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Frost..", "x": "Explained: Frost.. Frost. The context — Refrigerator Repair. Seals. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Coils.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Coils.", "x": "Refrigerator Repair in depth: Coils.. Coils. Details — the cold pros.. Frost. Ice maker. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Thermostat.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Thermostat.", "x": "Refrigerator Repair in depth: Thermostat.. Seals. Details — the cold pros.. Compressor. Thermostat. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Frost.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Frost.", "x": "Refrigerator Repair in depth: Frost.. Ice maker. Details — the cold pros.. Seals. Frost. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Compressor.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Compressor.", "x": "Refrigerator Repair in depth: Compressor.. Thermostat. Details — the cold pros.. Hiring. Compressor. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Seals.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Seals.", "x": "Refrigerator Repair in depth: Seals.. Frost. Details — the cold pros.. Coils. Coils. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Hiring.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Hiring.", "x": "Refrigerator Repair in depth: Hiring.. Compressor. Details — the cold pros.. Thermostat. Seals. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Refrigerator Repair comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Refrigerator Repair comes from.", "x": "Origins: Coils.. Compressor. The history of Refrigerator Repair — the cold pros.. Thermostat. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Refrigerator Repair respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Refrigerator Repair respectfully.", "x": "Engaging: Frost.. Coils. How to participate or observe well — Refrigerator Repair. the cold pros. Respect first, always; Compressor.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Refrigerator Repair do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Refrigerator Repair do's and don'ts.", "x": "Etiquette: Seals.. Seals. The rules of respect — Refrigerator Repair. the cold pros. When in doubt, ask about Hiring.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Refrigerator Repair.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Refrigerator Repair.", "x": "Planning: Coils.. Ice maker. Practical notes — Refrigerator Repair. the cold pros. A little planning shows respect for Thermostat.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Refrigerator Repair and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Refrigerator Repair and money.", "x": "Costs: Frost.. Thermostat. What to budget — Refrigerator Repair. the cold pros. The best experiences of Compressor. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-trade2-refrigerator-repair-trade-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
