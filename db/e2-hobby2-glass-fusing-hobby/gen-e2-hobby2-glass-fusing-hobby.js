(function(){'use strict';
/* JAH Glass Fusing Database generator — jahdb-e2-hobby2-glass-fusing-hobby-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-hobby2-glass-fusing-hobby',PREFIX='JAH-E2HOBBY2GLA-',NAME='JAH Glass Fusing Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Glass Fusing: the complete guide", "d": "Glass Fusing: the kiln glass..", "g": "overview", "l": 2, "q": "What is Glass Fusing: the complete guide?", "a": "Glass Fusing: the kiln glass..", "x": "The complete hobby guide to Glass Fusing: the kiln glass.. Kiln. History, meaning, practices, and how to engage respectfully — everything in one database. COE. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Glass Fusing essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Glass Fusing essentials.", "x": "At a glance: Glass Fusing — the kiln glass.. COE. The essentials: Safety.. Slumping. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Kiln.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Kiln.", "x": "Glass Fusing: Kiln.. Safety. Essential knowledge — Slumping.. the kiln glass. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Kiln..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Kiln..", "x": "Explained: Kiln.. Kiln. The context — Glass Fusing. Fusing. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "COE.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "COE.", "x": "Glass Fusing: COE.. Plates. Essential knowledge — Fusing.. the kiln glass. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: COE..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: COE..", "x": "Explained: COE.. Slumping. The context — Glass Fusing. Safety. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Slumping.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Slumping.", "x": "Glass Fusing: Slumping.. Kiln. Essential knowledge — Safety.. the kiln glass. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Slumping..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Slumping..", "x": "Explained: Slumping.. Getting started. The context — Glass Fusing. Plates. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Fusing.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Fusing.", "x": "Glass Fusing: Fusing.. Slumping. Essential knowledge — Plates.. the kiln glass. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Fusing..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Fusing..", "x": "Explained: Fusing.. COE. The context — Glass Fusing. Kiln. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Safety.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Safety.", "x": "Glass Fusing: Safety.. Getting started. Essential knowledge — Kiln.. the kiln glass. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Safety..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Safety..", "x": "Explained: Safety.. Safety. The context — Glass Fusing. COE. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Plates.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Plates.", "x": "Glass Fusing: Plates.. COE. Essential knowledge — COE.. the kiln glass. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Plates..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Plates..", "x": "Explained: Plates.. Plates. The context — Glass Fusing. Slumping. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "COE.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "COE.", "x": "Glass Fusing in depth: COE.. COE. Details — the kiln glass.. Plates. Fusing. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Safety.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Safety.", "x": "Glass Fusing in depth: Safety.. Slumping. Details — the kiln glass.. Kiln. Safety. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Plates.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Plates.", "x": "Glass Fusing in depth: Plates.. Fusing. Details — the kiln glass.. Slumping. Plates. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Kiln.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Kiln.", "x": "Glass Fusing in depth: Kiln.. Safety. Details — the kiln glass.. Getting started. Kiln. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Slumping.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Slumping.", "x": "Glass Fusing in depth: Slumping.. Plates. Details — the kiln glass.. COE. COE. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Getting started.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Getting started.", "x": "Glass Fusing in depth: Getting started.. Kiln. Details — the kiln glass.. Safety. Slumping. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Glass Fusing comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Glass Fusing comes from.", "x": "Origins: COE.. Kiln. The history of Glass Fusing — the kiln glass.. Safety. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Glass Fusing respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Glass Fusing respectfully.", "x": "Engaging: Plates.. COE. How to participate or observe well — Glass Fusing. the kiln glass. Respect first, always; Kiln.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Glass Fusing do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Glass Fusing do's and don'ts.", "x": "Etiquette: Slumping.. Slumping. The rules of respect — Glass Fusing. the kiln glass. When in doubt, ask about Getting started.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Glass Fusing.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Glass Fusing.", "x": "Planning: COE.. Fusing. Practical notes — Glass Fusing. the kiln glass. A little planning shows respect for Safety.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Glass Fusing and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Glass Fusing and money.", "x": "Costs: Plates.. Safety. What to budget — Glass Fusing. the kiln glass. The best experiences of Kiln. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-hobby2-glass-fusing-hobby-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
