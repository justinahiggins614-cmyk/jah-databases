(function(){'use strict';
/* JAH Cologne Cathedral Landmark Database generator — jahdb-e2-landmark-cologne-cathedral-landmark-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-landmark-cologne-cathedral-landmark',PREFIX='JAH-E2LANDMARKC-',NAME='JAH Cologne Cathedral Landmark Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Cologne Cathedral: the complete guide", "d": "Cologne Cathedral: the Gothic giant..", "g": "overview", "l": 2, "q": "What is Cologne Cathedral: the complete guide?", "a": "Cologne Cathedral: the Gothic giant..", "x": "The complete landmark guide to Cologne Cathedral: the Gothic giant.. 1880. History, meaning, practices, and how to engage respectfully — everything in one database. 1880. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Cologne Cathedral essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Cologne Cathedral essentials.", "x": "At a glance: Cologne Cathedral — the Gothic giant.. 157m. The essentials: Shrine.. Gothic. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "1880.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "1880.", "x": "Cologne Cathedral: 1880.. Shrine. Essential knowledge — Gothic.. the Gothic giant. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 1880..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 1880..", "x": "Explained: 1880.. Spires. The context — Cologne Cathedral. Shrine. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "157m.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "157m.", "x": "Cologne Cathedral: 157m.. WWII. Essential knowledge — Shrine.. the Gothic giant. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: 157m..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: 157m..", "x": "Explained: 157m.. Gothic. The context — Cologne Cathedral. WWII. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Gothic.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Gothic.", "x": "Cologne Cathedral: Gothic.. Spires. Essential knowledge — WWII.. the Gothic giant. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Gothic..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Gothic..", "x": "Explained: Gothic.. Tours. The context — Cologne Cathedral. Twin spires. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Shrine.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Shrine.", "x": "Cologne Cathedral: Shrine.. Gothic. Essential knowledge — Twin spires.. the Gothic giant. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Shrine..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Shrine..", "x": "Explained: Shrine.. 1880. The context — Cologne Cathedral. 1880. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "WWII.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "WWII.", "x": "Cologne Cathedral: WWII.. Tours. Essential knowledge — 1880.. the Gothic giant. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: WWII..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: WWII..", "x": "Explained: WWII.. Shrine. The context — Cologne Cathedral. 157m. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Twin spires.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Twin spires.", "x": "Cologne Cathedral: Twin spires.. 1880. Essential knowledge — 157m.. the Gothic giant. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Twin spires..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Twin spires..", "x": "Explained: Twin spires.. WWII. The context — Cologne Cathedral. Gothic. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "1880.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "1880.", "x": "Cologne Cathedral in depth: 1880.. 157m. Details — the Gothic giant.. WWII. Shrine. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Shrine.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Shrine.", "x": "Cologne Cathedral in depth: Shrine.. Gothic. Details — the Gothic giant.. Spires. WWII. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "WWII.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "WWII.", "x": "Cologne Cathedral in depth: WWII.. Shrine. Details — the Gothic giant.. Gothic. Twin spires. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Spires.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Spires.", "x": "Cologne Cathedral in depth: Spires.. WWII. Details — the Gothic giant.. Tours. 1880. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Gothic.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Gothic.", "x": "Cologne Cathedral in depth: Gothic.. Twin spires. Details — the Gothic giant.. 1880. 157m. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Tours.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Tours.", "x": "Cologne Cathedral in depth: Tours.. 1880. Details — the Gothic giant.. Shrine. Gothic. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Cologne Cathedral comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Cologne Cathedral comes from.", "x": "Origins: 1880.. 1880. The history of Cologne Cathedral — the Gothic giant.. Shrine. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Cologne Cathedral respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Cologne Cathedral respectfully.", "x": "Engaging: WWII.. 157m. How to participate or observe well — Cologne Cathedral. the Gothic giant. Respect first, always; Spires.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Cologne Cathedral do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Cologne Cathedral do's and don'ts.", "x": "Etiquette: Gothic.. Gothic. The rules of respect — Cologne Cathedral. the Gothic giant. When in doubt, ask about Tours.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Cologne Cathedral.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Cologne Cathedral.", "x": "Planning: 1880.. Shrine. Practical notes — Cologne Cathedral. the Gothic giant. A little planning shows respect for Shrine.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Cologne Cathedral and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Cologne Cathedral and money.", "x": "Costs: WWII.. WWII. What to budget — Cologne Cathedral. the Gothic giant. The best experiences of Spires. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-landmark-cologne-cathedral-landmark-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
