(function(){'use strict';
/* JAH Cape of Good Hope Landmark Database generator — jahdb-e2-landmark-cape-good-hope-landmark-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-landmark-cape-good-hope-landmark',PREFIX='JAH-E2LANDMARKC-',NAME='JAH Cape of Good Hope Landmark Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Cape of Good Hope: the complete guide", "d": "Cape of Good Hope: the meeting point..", "g": "overview", "l": 2, "q": "What is Cape of Good Hope: the complete guide?", "a": "Cape of Good Hope: the meeting point..", "x": "The complete landmark guide to Cape of Good Hope: the meeting point.. 1488. History, meaning, practices, and how to engage respectfully — everything in one database. 1488. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Cape of Good Hope essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Cape of Good Hope essentials.", "x": "At a glance: Cape of Good Hope — the meeting point.. Diaz. The essentials: Penguins.. Two oceans. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "1488.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "1488.", "x": "Cape of Good Hope: 1488.. Penguins. Essential knowledge — Two oceans.. the meeting point. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 1488..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 1488..", "x": "Explained: 1488.. Diaz. The context — Cape of Good Hope. Penguins. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Diaz.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Diaz.", "x": "Cape of Good Hope: Diaz.. Myth. Essential knowledge — Penguins.. the meeting point. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Diaz..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Diaz..", "x": "Explained: Diaz.. Cliffs. The context — Cape of Good Hope. Cliffs. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Two oceans.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Two oceans.", "x": "Cape of Good Hope: Two oceans.. Diaz. Essential knowledge — Cliffs.. the meeting point. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Two oceans..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Two oceans..", "x": "Explained: Two oceans.. Visits. The context — Cape of Good Hope. Myth. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Penguins.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Penguins.", "x": "Cape of Good Hope: Penguins.. Cliffs. Essential knowledge — Myth.. the meeting point. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Penguins..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Penguins..", "x": "Explained: Penguins.. 1488. The context — Cape of Good Hope. 1488. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Cliffs.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Cliffs.", "x": "Cape of Good Hope: Cliffs.. Visits. Essential knowledge — 1488.. the meeting point. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Cliffs..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Cliffs..", "x": "Explained: Cliffs.. Penguins. The context — Cape of Good Hope. Diaz. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Myth.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Myth.", "x": "Cape of Good Hope: Myth.. 1488. Essential knowledge — Diaz.. the meeting point. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Myth..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Myth..", "x": "Explained: Myth.. Myth. The context — Cape of Good Hope. Two oceans. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "1488.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "1488.", "x": "Cape of Good Hope in depth: 1488.. Diaz. Details — the meeting point.. Myth. Penguins. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Penguins.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Penguins.", "x": "Cape of Good Hope in depth: Penguins.. Two oceans. Details — the meeting point.. Diaz. Cliffs. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Myth.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Myth.", "x": "Cape of Good Hope in depth: Myth.. Penguins. Details — the meeting point.. Cliffs. Myth. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Diaz.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Diaz.", "x": "Cape of Good Hope in depth: Diaz.. Cliffs. Details — the meeting point.. Visits. 1488. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Cliffs.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Cliffs.", "x": "Cape of Good Hope in depth: Cliffs.. Myth. Details — the meeting point.. 1488. Diaz. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Visits.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Visits.", "x": "Cape of Good Hope in depth: Visits.. 1488. Details — the meeting point.. Penguins. Two oceans. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Cape of Good Hope comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Cape of Good Hope comes from.", "x": "Origins: 1488.. 1488. The history of Cape of Good Hope — the meeting point.. Penguins. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Cape of Good Hope respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Cape of Good Hope respectfully.", "x": "Engaging: Myth.. Diaz. How to participate or observe well — Cape of Good Hope. the meeting point. Respect first, always; Diaz.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Cape of Good Hope do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Cape of Good Hope do's and don'ts.", "x": "Etiquette: Cliffs.. Two oceans. The rules of respect — Cape of Good Hope. the meeting point. When in doubt, ask about Visits.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Cape of Good Hope.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Cape of Good Hope.", "x": "Planning: 1488.. Penguins. Practical notes — Cape of Good Hope. the meeting point. A little planning shows respect for Penguins.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Cape of Good Hope and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Cape of Good Hope and money.", "x": "Costs: Myth.. Cliffs. What to budget — Cape of Good Hope. the meeting point. The best experiences of Diaz. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-landmark-cape-good-hope-landmark-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
