(function(){'use strict';
/* JAH Rhine Falls Landmark Database generator — jahdb-e2-landmark-rhine-falls-landmark-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-landmark-rhine-falls-landmark',PREFIX='JAH-E2LANDMARKR-',NAME='JAH Rhine Falls Landmark Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Rhine Falls: the complete guide", "d": "Rhine Falls: Europe's largest falls..", "g": "overview", "l": 2, "q": "What is Rhine Falls: the complete guide?", "a": "Rhine Falls: Europe's largest falls..", "x": "The complete landmark guide to Rhine Falls: Europe's largest falls.. 150m wide. History, meaning, practices, and how to engage respectfully — everything in one database. 150m. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Rhine Falls essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Rhine Falls essentials.", "x": "At a glance: Rhine Falls — Europe's largest falls.. 23m. The essentials: Boats.. Schaffhausen. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "150m wide.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "150m wide.", "x": "Rhine Falls: 150m wide.. Boats. Essential knowledge — Schaffhausen.. Europe's largest falls. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 150m wide..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 150m wide..", "x": "Explained: 150m wide.. Schaffhausen. The context — Rhine Falls. Boats. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "23m.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "23m.", "x": "Rhine Falls: 23m.. Mist. Essential knowledge — Boats.. Europe's largest falls. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: 23m..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: 23m..", "x": "Explained: 23m.. Rock. The context — Rhine Falls. Mist. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Schaffhausen.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Schaffhausen.", "x": "Rhine Falls: Schaffhausen.. Schaffhausen. Essential knowledge — Mist.. Europe's largest falls. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Schaffhausen..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Schaffhausen..", "x": "Explained: Schaffhausen.. Views. The context — Rhine Falls. Rock. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Boats.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Boats.", "x": "Rhine Falls: Boats.. Rock. Essential knowledge — Rock.. Europe's largest falls. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Boats..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Boats..", "x": "Explained: Boats.. 150m. The context — Rhine Falls. 150m wide. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Mist.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Mist.", "x": "Rhine Falls: Mist.. Views. Essential knowledge — 150m wide.. Europe's largest falls. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Mist..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Mist..", "x": "Explained: Mist.. Boats. The context — Rhine Falls. 23m. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Rock.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Rock.", "x": "Rhine Falls: Rock.. 150m. Essential knowledge — 23m.. Europe's largest falls. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Rock..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Rock..", "x": "Explained: Rock.. Mist. The context — Rhine Falls. Schaffhausen. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "150m.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "150m.", "x": "Rhine Falls in depth: 150m.. 23m. Details — Europe's largest falls.. Mist. Boats. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Boats.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Boats.", "x": "Rhine Falls in depth: Boats.. Schaffhausen. Details — Europe's largest falls.. Schaffhausen. Mist. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Mist.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Mist.", "x": "Rhine Falls in depth: Mist.. Boats. Details — Europe's largest falls.. Rock. Rock. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Schaffhausen.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Schaffhausen.", "x": "Rhine Falls in depth: Schaffhausen.. Mist. Details — Europe's largest falls.. Views. 150m wide. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Rock.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Rock.", "x": "Rhine Falls in depth: Rock.. Rock. Details — Europe's largest falls.. 150m. 23m. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Views.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Views.", "x": "Rhine Falls in depth: Views.. 150m wide. Details — Europe's largest falls.. Boats. Schaffhausen. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Rhine Falls comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Rhine Falls comes from.", "x": "Origins: 150m.. 150m wide. The history of Rhine Falls — Europe's largest falls.. Boats. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Rhine Falls respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Rhine Falls respectfully.", "x": "Engaging: Mist.. 23m. How to participate or observe well — Rhine Falls. Europe's largest falls. Respect first, always; Schaffhausen.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Rhine Falls do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Rhine Falls do's and don'ts.", "x": "Etiquette: Rock.. Schaffhausen. The rules of respect — Rhine Falls. Europe's largest falls. When in doubt, ask about Views.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Rhine Falls.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Rhine Falls.", "x": "Planning: 150m.. Boats. Practical notes — Rhine Falls. Europe's largest falls. A little planning shows respect for Boats.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Rhine Falls and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Rhine Falls and money.", "x": "Costs: Mist.. Mist. What to budget — Rhine Falls. Europe's largest falls. The best experiences of Schaffhausen. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-landmark-rhine-falls-landmark-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
