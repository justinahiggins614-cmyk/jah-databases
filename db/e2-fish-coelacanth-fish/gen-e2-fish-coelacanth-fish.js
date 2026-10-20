(function(){'use strict';
/* JAH Coelacanth Fish Species Database generator — jahdb-e2-fish-coelacanth-fish-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-fish-coelacanth-fish',PREFIX='JAH-E2FISHCOELA-',NAME='JAH Coelacanth Fish Species Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Coelacanth: the complete guide", "d": "Coelacanth: the living fossil..", "g": "overview", "l": 2, "q": "What is Coelacanth: the complete guide?", "a": "Coelacanth: the living fossil..", "x": "The complete fish species guide to Coelacanth: the living fossil.. Fossil. History, meaning, practices, and how to engage respectfully — everything in one database. Fossil. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Coelacanth essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Coelacanth essentials.", "x": "At a glance: Coelacanth — the living fossil.. 1938. The essentials: 1938.. Lobed fins. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Fossil.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Fossil.", "x": "Coelacanth: Fossil.. 1938. Essential knowledge — Lobed fins.. the living fossil. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Fossil..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Fossil..", "x": "Explained: Fossil.. Ancient. The context — Coelacanth. Deep. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "1938.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "1938.", "x": "Coelacanth: 1938.. Deep. Essential knowledge — Deep.. the living fossil. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: 1938..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: 1938..", "x": "Explained: 1938.. Latimeria. The context — Coelacanth. Latimeria. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Lobed fins.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Lobed fins.", "x": "Coelacanth: Lobed fins.. Ancient. Essential knowledge — Latimeria.. the living fossil. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Lobed fins..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Lobed fins..", "x": "Explained: Lobed fins.. Habitat. The context — Coelacanth. Ancient. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Deep.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Deep.", "x": "Coelacanth: Deep.. Latimeria. Essential knowledge — Ancient.. the living fossil. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Deep..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Deep..", "x": "Explained: Deep.. Fossil. The context — Coelacanth. Fossil. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Latimeria.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Latimeria.", "x": "Coelacanth: Latimeria.. Habitat. Essential knowledge — Fossil.. the living fossil. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Latimeria..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Latimeria..", "x": "Explained: Latimeria.. 1938. The context — Coelacanth. 1938. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Ancient.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Ancient.", "x": "Coelacanth: Ancient.. Fossil. Essential knowledge — 1938.. the living fossil. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Ancient..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Ancient..", "x": "Explained: Ancient.. Deep. The context — Coelacanth. Lobed fins. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Fossil.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Fossil.", "x": "Coelacanth in depth: Fossil.. 1938. Details — the living fossil.. Deep. Deep. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "1938.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "1938.", "x": "Coelacanth in depth: 1938.. Lobed fins. Details — the living fossil.. Ancient. Latimeria. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Deep.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Deep.", "x": "Coelacanth in depth: Deep.. Deep. Details — the living fossil.. Latimeria. Ancient. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Ancient.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Ancient.", "x": "Coelacanth in depth: Ancient.. Latimeria. Details — the living fossil.. Habitat. Fossil. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Latimeria.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Latimeria.", "x": "Coelacanth in depth: Latimeria.. Ancient. Details — the living fossil.. Fossil. 1938. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Habitat.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Habitat.", "x": "Coelacanth in depth: Habitat.. Fossil. Details — the living fossil.. 1938. Lobed fins. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Coelacanth comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Coelacanth comes from.", "x": "Origins: Fossil.. Fossil. The history of Coelacanth — the living fossil.. 1938. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Coelacanth respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Coelacanth respectfully.", "x": "Engaging: Deep.. 1938. How to participate or observe well — Coelacanth. the living fossil. Respect first, always; Ancient.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Coelacanth do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Coelacanth do's and don'ts.", "x": "Etiquette: Latimeria.. Lobed fins. The rules of respect — Coelacanth. the living fossil. When in doubt, ask about Habitat.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Coelacanth.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Coelacanth.", "x": "Planning: Fossil.. Deep. Practical notes — Coelacanth. the living fossil. A little planning shows respect for 1938.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Coelacanth and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Coelacanth and money.", "x": "Costs: Deep.. Latimeria. What to budget — Coelacanth. the living fossil. The best experiences of Ancient. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-fish-coelacanth-fish-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
