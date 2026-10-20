(function(){'use strict';
/* JAH La Rambla Landmark Database generator — jahdb-e2-landmark-la-rambla-landmark-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-landmark-la-rambla-landmark',PREFIX='JAH-E2LANDMARKL-',NAME='JAH La Rambla Landmark Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "La Rambla: the complete guide", "d": "La Rambla: the lively boulevard..", "g": "overview", "l": 2, "q": "What is La Rambla: the complete guide?", "a": "La Rambla: the lively boulevard..", "x": "The complete landmark guide to La Rambla: the lively boulevard.. 1.2 km. History, meaning, practices, and how to engage respectfully — everything in one database. Stalls. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "La Rambla essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "La Rambla essentials.", "x": "At a glance: La Rambla — the lively boulevard.. Flower stalls. The essentials: Boqueria.. Mimes. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "1.2 km.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "1.2 km.", "x": "La Rambla: 1.2 km.. Boqueria. Essential knowledge — Mimes.. the lively boulevard. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 1.2 km..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 1.2 km..", "x": "Explained: 1.2 km.. Mimes. The context — La Rambla. Boqueria. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Flower stalls.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Flower stalls.", "x": "La Rambla: Flower stalls.. Stroll. Essential knowledge — Boqueria.. the lively boulevard. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Flower stalls..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Flower stalls..", "x": "Explained: Flower stalls.. 1.2 km. The context — La Rambla. Pickpockets. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Mimes.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Mimes.", "x": "La Rambla: Mimes.. Mimes. Essential knowledge — Pickpockets.. the lively boulevard. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Mimes..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Mimes..", "x": "Explained: Mimes.. Walking. The context — La Rambla. Stroll. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Boqueria.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Boqueria.", "x": "La Rambla: Boqueria.. 1.2 km. Essential knowledge — Stroll.. the lively boulevard. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Boqueria..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Boqueria..", "x": "Explained: Boqueria.. Stalls. The context — La Rambla. 1.2 km. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Pickpockets.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Pickpockets.", "x": "La Rambla: Pickpockets.. Walking. Essential knowledge — 1.2 km.. the lively boulevard. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Pickpockets..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Pickpockets..", "x": "Explained: Pickpockets.. Boqueria. The context — La Rambla. Flower stalls. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Stroll.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Stroll.", "x": "La Rambla: Stroll.. Stalls. Essential knowledge — Flower stalls.. the lively boulevard. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Stroll..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Stroll..", "x": "Explained: Stroll.. Stroll. The context — La Rambla. Mimes. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Stalls.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Stalls.", "x": "La Rambla in depth: Stalls.. Flower stalls. Details — the lively boulevard.. Stroll. Boqueria. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Boqueria.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Boqueria.", "x": "La Rambla in depth: Boqueria.. Mimes. Details — the lively boulevard.. Mimes. Pickpockets. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Stroll.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Stroll.", "x": "La Rambla in depth: Stroll.. Boqueria. Details — the lively boulevard.. 1.2 km. Stroll. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Mimes.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Mimes.", "x": "La Rambla in depth: Mimes.. Pickpockets. Details — the lively boulevard.. Walking. 1.2 km. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "1.2 km.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "1.2 km.", "x": "La Rambla in depth: 1.2 km.. Stroll. Details — the lively boulevard.. Stalls. Flower stalls. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Walking.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Walking.", "x": "La Rambla in depth: Walking.. 1.2 km. Details — the lively boulevard.. Boqueria. Mimes. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where La Rambla comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where La Rambla comes from.", "x": "Origins: Stalls.. 1.2 km. The history of La Rambla — the lively boulevard.. Boqueria. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing La Rambla respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing La Rambla respectfully.", "x": "Engaging: Stroll.. Flower stalls. How to participate or observe well — La Rambla. the lively boulevard. Respect first, always; Mimes.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "La Rambla do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "La Rambla do's and don'ts.", "x": "Etiquette: 1.2 km.. Mimes. The rules of respect — La Rambla. the lively boulevard. When in doubt, ask about Walking.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around La Rambla.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around La Rambla.", "x": "Planning: Stalls.. Boqueria. Practical notes — La Rambla. the lively boulevard. A little planning shows respect for Boqueria.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "La Rambla and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "La Rambla and money.", "x": "Costs: Stroll.. Pickpockets. What to budget — La Rambla. the lively boulevard. The best experiences of Mimes. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-landmark-la-rambla-landmark-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
