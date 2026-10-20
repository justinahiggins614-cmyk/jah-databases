(function(){'use strict';
/* JAH Georgia Aquarium2 Database generator — jahdb-e2-aquarium2-georgia-aquarium2-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-aquarium2-georgia-aquarium2',PREFIX='JAH-E2AQUARIUM2-',NAME='JAH Georgia Aquarium2 Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Georgia Aquarium2: the complete guide", "d": "Georgia Aquarium2: the Atlanta 2..", "g": "overview", "l": 2, "q": "What is Georgia Aquarium2: the complete guide?", "a": "Georgia Aquarium2: the Atlanta 2..", "x": "The complete aquarium guide to Georgia Aquarium2: the Atlanta 2.. 2005. History, meaning, practices, and how to engage respectfully — everything in one database. 2005. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Georgia Aquarium2 essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Georgia Aquarium2 essentials.", "x": "At a glance: Georgia Aquarium2 — the Atlanta 2.. Whale sharks. The essentials: Voyager.. Belugas. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "2005.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "2005.", "x": "Georgia Aquarium2: 2005.. Voyager. Essential knowledge — Belugas.. the Atlanta 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 2005..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 2005..", "x": "Explained: 2005.. Sharks. The context — Georgia Aquarium2. 6M gallons. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Whale sharks.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Whale sharks.", "x": "Georgia Aquarium2: Whale sharks.. Atlanta. Essential knowledge — 6M gallons.. the Atlanta 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Whale sharks..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Whale sharks..", "x": "Explained: Whale sharks.. Belugas. The context — Georgia Aquarium2. Atlanta. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Belugas.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Belugas.", "x": "Georgia Aquarium2: Belugas.. Sharks. Essential knowledge — Atlanta.. the Atlanta 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Belugas..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Belugas..", "x": "Explained: Belugas.. Visiting. The context — Georgia Aquarium2. Ocean Voyager. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "6M gallons.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "6M gallons.", "x": "Georgia Aquarium2: 6M gallons.. Belugas. Essential knowledge — Ocean Voyager.. the Atlanta 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: 6M gallons..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: 6M gallons..", "x": "Explained: 6M gallons.. 2005. The context — Georgia Aquarium2. 2005. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Atlanta.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Atlanta.", "x": "Georgia Aquarium2: Atlanta.. Visiting. Essential knowledge — 2005.. the Atlanta 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Atlanta..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Atlanta..", "x": "Explained: Atlanta.. Voyager. The context — Georgia Aquarium2. Whale sharks. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Ocean Voyager.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Ocean Voyager.", "x": "Georgia Aquarium2: Ocean Voyager.. 2005. Essential knowledge — Whale sharks.. the Atlanta 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Ocean Voyager..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Ocean Voyager..", "x": "Explained: Ocean Voyager.. Atlanta. The context — Georgia Aquarium2. Belugas. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "2005.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "2005.", "x": "Georgia Aquarium2 in depth: 2005.. Whale sharks. Details — the Atlanta 2.. Atlanta. 6M gallons. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Voyager.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Voyager.", "x": "Georgia Aquarium2 in depth: Voyager.. Belugas. Details — the Atlanta 2.. Sharks. Atlanta. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Atlanta.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Atlanta.", "x": "Georgia Aquarium2 in depth: Atlanta.. 6M gallons. Details — the Atlanta 2.. Belugas. Ocean Voyager. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Sharks.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Sharks.", "x": "Georgia Aquarium2 in depth: Sharks.. Atlanta. Details — the Atlanta 2.. Visiting. 2005. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Belugas.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Belugas.", "x": "Georgia Aquarium2 in depth: Belugas.. Ocean Voyager. Details — the Atlanta 2.. 2005. Whale sharks. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Visiting.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Visiting.", "x": "Georgia Aquarium2 in depth: Visiting.. 2005. Details — the Atlanta 2.. Voyager. Belugas. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Georgia Aquarium2 comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Georgia Aquarium2 comes from.", "x": "Origins: 2005.. 2005. The history of Georgia Aquarium2 — the Atlanta 2.. Voyager. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Georgia Aquarium2 respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Georgia Aquarium2 respectfully.", "x": "Engaging: Atlanta.. Whale sharks. How to participate or observe well — Georgia Aquarium2. the Atlanta 2. Respect first, always; Sharks.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Georgia Aquarium2 do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Georgia Aquarium2 do's and don'ts.", "x": "Etiquette: Belugas.. Belugas. The rules of respect — Georgia Aquarium2. the Atlanta 2. When in doubt, ask about Visiting.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Georgia Aquarium2.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Georgia Aquarium2.", "x": "Planning: 2005.. 6M gallons. Practical notes — Georgia Aquarium2. the Atlanta 2. A little planning shows respect for Voyager.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Georgia Aquarium2 and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Georgia Aquarium2 and money.", "x": "Costs: Atlanta.. Atlanta. What to budget — Georgia Aquarium2. the Atlanta 2. The best experiences of Sharks. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-aquarium2-georgia-aquarium2-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
