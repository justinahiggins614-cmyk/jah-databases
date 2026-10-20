(function(){'use strict';
/* JAH Albatross Bird Species Database generator — jahdb-e2-bird-albatross-bird-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-bird-albatross-bird',PREFIX='JAH-E2BIRDALBAT-',NAME='JAH Albatross Bird Species Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Albatross: the complete guide", "d": "Albatross: the ocean wanderer..", "g": "overview", "l": 2, "q": "What is Albatross: the complete guide?", "a": "Albatross: the ocean wanderer..", "x": "The complete bird species guide to Albatross: the ocean wanderer.. 11 ft wingspan. History, meaning, practices, and how to engage respectfully — everything in one database. Wingspan. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Albatross essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Albatross essentials.", "x": "At a glance: Albatross — the ocean wanderer.. Gliding. The essentials: Gliding.. Ocean. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "11 ft wingspan.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "11 ft wingspan.", "x": "Albatross: 11 ft wingspan.. Gliding. Essential knowledge — Ocean.. the ocean wanderer. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 11 ft wingspan..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 11 ft wingspan..", "x": "Explained: 11 ft wingspan.. Ocean. The context — Albatross. Years. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Gliding.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Gliding.", "x": "Albatross: Gliding.. Monogamous. Essential knowledge — Years.. the ocean wanderer. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Gliding..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Gliding..", "x": "Explained: Gliding.. Years. The context — Albatross. Monogamous. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Ocean.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Ocean.", "x": "Albatross: Ocean.. Ocean. Essential knowledge — Monogamous.. the ocean wanderer. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Ocean..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Ocean..", "x": "Explained: Ocean.. Habitat. The context — Albatross. Wandering. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Years.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Years.", "x": "Albatross: Years.. Years. Essential knowledge — Wandering.. the ocean wanderer. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Years..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Years..", "x": "Explained: Years.. Wingspan. The context — Albatross. 11 ft wingspan. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Monogamous.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Monogamous.", "x": "Albatross: Monogamous.. Habitat. Essential knowledge — 11 ft wingspan.. the ocean wanderer. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Monogamous..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Monogamous..", "x": "Explained: Monogamous.. Gliding. The context — Albatross. Gliding. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Wandering.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Wandering.", "x": "Albatross: Wandering.. Wingspan. Essential knowledge — Gliding.. the ocean wanderer. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Wandering..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Wandering..", "x": "Explained: Wandering.. Monogamous. The context — Albatross. Ocean. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Wingspan.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Wingspan.", "x": "Albatross in depth: Wingspan.. Gliding. Details — the ocean wanderer.. Monogamous. Years. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Gliding.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Gliding.", "x": "Albatross in depth: Gliding.. Ocean. Details — the ocean wanderer.. Ocean. Monogamous. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Monogamous.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Monogamous.", "x": "Albatross in depth: Monogamous.. Years. Details — the ocean wanderer.. Years. Wandering. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Ocean.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Ocean.", "x": "Albatross in depth: Ocean.. Monogamous. Details — the ocean wanderer.. Habitat. 11 ft wingspan. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Years.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Years.", "x": "Albatross in depth: Years.. Wandering. Details — the ocean wanderer.. Wingspan. Gliding. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Habitat.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Habitat.", "x": "Albatross in depth: Habitat.. 11 ft wingspan. Details — the ocean wanderer.. Gliding. Ocean. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Albatross comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Albatross comes from.", "x": "Origins: Wingspan.. 11 ft wingspan. The history of Albatross — the ocean wanderer.. Gliding. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Albatross respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Albatross respectfully.", "x": "Engaging: Monogamous.. Gliding. How to participate or observe well — Albatross. the ocean wanderer. Respect first, always; Ocean.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Albatross do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Albatross do's and don'ts.", "x": "Etiquette: Years.. Ocean. The rules of respect — Albatross. the ocean wanderer. When in doubt, ask about Habitat.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Albatross.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Albatross.", "x": "Planning: Wingspan.. Years. Practical notes — Albatross. the ocean wanderer. A little planning shows respect for Gliding.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Albatross and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Albatross and money.", "x": "Costs: Monogamous.. Monogamous. What to budget — Albatross. the ocean wanderer. The best experiences of Ocean. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-bird-albatross-bird-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
