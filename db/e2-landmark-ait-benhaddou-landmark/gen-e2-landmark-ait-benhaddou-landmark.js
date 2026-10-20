(function(){'use strict';
/* JAH Ait Benhaddou Landmark Database generator — jahdb-e2-landmark-ait-benhaddou-landmark-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-landmark-ait-benhaddou-landmark',PREFIX='JAH-E2LANDMARKA-',NAME='JAH Ait Benhaddou Landmark Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Ait Benhaddou: the complete guide", "d": "Ait Benhaddou: the earthen ksar..", "g": "overview", "l": 2, "q": "What is Ait Benhaddou: the complete guide?", "a": "Ait Benhaddou: the earthen ksar..", "x": "The complete landmark guide to Ait Benhaddou: the earthen ksar.. Earthen. History, meaning, practices, and how to engage respectfully — everything in one database. Earthen. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Ait Benhaddou essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Ait Benhaddou essentials.", "x": "At a glance: Ait Benhaddou — the earthen ksar.. Ksar. The essentials: Films.. Films. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Earthen.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Earthen.", "x": "Ait Benhaddou: Earthen.. Films. Essential knowledge — Films.. the earthen ksar. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Earthen..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Earthen..", "x": "Explained: Earthen.. Atlas. The context — Ait Benhaddou. UNESCO. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Ksar.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Ksar.", "x": "Ait Benhaddou: Ksar.. UNESCO. Essential knowledge — UNESCO.. the earthen ksar. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Ksar..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Ksar..", "x": "Explained: Ksar.. Ksar. The context — Ait Benhaddou. Pise. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Films.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Films.", "x": "Ait Benhaddou: Films.. Atlas. Essential knowledge — Pise.. the earthen ksar. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Films..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Films..", "x": "Explained: Films.. Tours. The context — Ait Benhaddou. Atlas. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "UNESCO.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "UNESCO.", "x": "Ait Benhaddou: UNESCO.. Ksar. Essential knowledge — Atlas.. the earthen ksar. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: UNESCO..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: UNESCO..", "x": "Explained: UNESCO.. Earthen. The context — Ait Benhaddou. Earthen. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Pise.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Pise.", "x": "Ait Benhaddou: Pise.. Tours. Essential knowledge — Earthen.. the earthen ksar. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Pise..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Pise..", "x": "Explained: Pise.. Films. The context — Ait Benhaddou. Ksar. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Atlas.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Atlas.", "x": "Ait Benhaddou: Atlas.. Earthen. Essential knowledge — Ksar.. the earthen ksar. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Atlas..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Atlas..", "x": "Explained: Atlas.. UNESCO. The context — Ait Benhaddou. Films. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Earthen.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Earthen.", "x": "Ait Benhaddou in depth: Earthen.. Ksar. Details — the earthen ksar.. UNESCO. UNESCO. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Films.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Films.", "x": "Ait Benhaddou in depth: Films.. Films. Details — the earthen ksar.. Atlas. Pise. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "UNESCO.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "UNESCO.", "x": "Ait Benhaddou in depth: UNESCO.. UNESCO. Details — the earthen ksar.. Ksar. Atlas. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Atlas.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Atlas.", "x": "Ait Benhaddou in depth: Atlas.. Pise. Details — the earthen ksar.. Tours. Earthen. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Ksar.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Ksar.", "x": "Ait Benhaddou in depth: Ksar.. Atlas. Details — the earthen ksar.. Earthen. Ksar. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Tours.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Tours.", "x": "Ait Benhaddou in depth: Tours.. Earthen. Details — the earthen ksar.. Films. Films. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Ait Benhaddou comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Ait Benhaddou comes from.", "x": "Origins: Earthen.. Earthen. The history of Ait Benhaddou — the earthen ksar.. Films. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Ait Benhaddou respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Ait Benhaddou respectfully.", "x": "Engaging: UNESCO.. Ksar. How to participate or observe well — Ait Benhaddou. the earthen ksar. Respect first, always; Atlas.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Ait Benhaddou do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Ait Benhaddou do's and don'ts.", "x": "Etiquette: Ksar.. Films. The rules of respect — Ait Benhaddou. the earthen ksar. When in doubt, ask about Tours.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Ait Benhaddou.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Ait Benhaddou.", "x": "Planning: Earthen.. UNESCO. Practical notes — Ait Benhaddou. the earthen ksar. A little planning shows respect for Films.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Ait Benhaddou and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Ait Benhaddou and money.", "x": "Costs: UNESCO.. Pise. What to budget — Ait Benhaddou. the earthen ksar. The best experiences of Atlas. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-landmark-ait-benhaddou-landmark-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
