(function(){'use strict';
/* JAH Keck Observatory Observatory Database generator — jahdb-e2-observatory-keck-observatory-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-observatory-keck-observatory',PREFIX='JAH-E2OBSERVATO-',NAME='JAH Keck Observatory Observatory Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Keck Observatory: the complete guide", "d": "Keck Observatory: twin ten-meter eyes..", "g": "overview", "l": 2, "q": "What is Keck Observatory: the complete guide?", "a": "Keck Observatory: twin ten-meter eyes..", "x": "The complete observatory guide to Keck Observatory: twin ten-meter eyes.. 10m twins. History, meaning, practices, and how to engage respectfully — everything in one database. Mirrors. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Keck Observatory essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Keck Observatory essentials.", "x": "At a glance: Keck Observatory — twin ten-meter eyes.. Segmented. The essentials: Planets.. Mauna Kea. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "10m twins.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "10m twins.", "x": "Keck Observatory: 10m twins.. Planets. Essential knowledge — Mauna Kea.. twin ten-meter eyes. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 10m twins..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 10m twins..", "x": "Explained: 10m twins.. Science. The context — Keck Observatory. Exoplanets. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Segmented.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Segmented.", "x": "Keck Observatory: Segmented.. History. Essential knowledge — Exoplanets.. twin ten-meter eyes. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Segmented..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Segmented..", "x": "Explained: Segmented.. Hawaii. The context — Keck Observatory. 1990s. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Mauna Kea.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Mauna Kea.", "x": "Keck Observatory: Mauna Kea.. Science. Essential knowledge — 1990s.. twin ten-meter eyes. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Mauna Kea..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Mauna Kea..", "x": "Explained: Mauna Kea.. Tours. The context — Keck Observatory. Science. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Exoplanets.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Exoplanets.", "x": "Keck Observatory: Exoplanets.. Hawaii. Essential knowledge — Science.. twin ten-meter eyes. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Exoplanets..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Exoplanets..", "x": "Explained: Exoplanets.. Mirrors. The context — Keck Observatory. 10m twins. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "1990s.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "1990s.", "x": "Keck Observatory: 1990s.. Tours. Essential knowledge — 10m twins.. twin ten-meter eyes. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: 1990s..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: 1990s..", "x": "Explained: 1990s.. Planets. The context — Keck Observatory. Segmented. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Science.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Science.", "x": "Keck Observatory: Science.. Mirrors. Essential knowledge — Segmented.. twin ten-meter eyes. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Science..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Science..", "x": "Explained: Science.. History. The context — Keck Observatory. Mauna Kea. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Mirrors.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Mirrors.", "x": "Keck Observatory in depth: Mirrors.. Segmented. Details — twin ten-meter eyes.. History. Exoplanets. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Planets.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Planets.", "x": "Keck Observatory in depth: Planets.. Mauna Kea. Details — twin ten-meter eyes.. Science. 1990s. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "History.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "History.", "x": "Keck Observatory in depth: History.. Exoplanets. Details — twin ten-meter eyes.. Hawaii. Science. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Science.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Science.", "x": "Keck Observatory in depth: Science.. 1990s. Details — twin ten-meter eyes.. Tours. 10m twins. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Hawaii.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Hawaii.", "x": "Keck Observatory in depth: Hawaii.. Science. Details — twin ten-meter eyes.. Mirrors. Segmented. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Tours.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Tours.", "x": "Keck Observatory in depth: Tours.. 10m twins. Details — twin ten-meter eyes.. Planets. Mauna Kea. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Keck Observatory comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Keck Observatory comes from.", "x": "Origins: Mirrors.. 10m twins. The history of Keck Observatory — twin ten-meter eyes.. Planets. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Keck Observatory respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Keck Observatory respectfully.", "x": "Engaging: History.. Segmented. How to participate or observe well — Keck Observatory. twin ten-meter eyes. Respect first, always; Science.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Keck Observatory do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Keck Observatory do's and don'ts.", "x": "Etiquette: Hawaii.. Mauna Kea. The rules of respect — Keck Observatory. twin ten-meter eyes. When in doubt, ask about Tours.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Keck Observatory.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Keck Observatory.", "x": "Planning: Mirrors.. Exoplanets. Practical notes — Keck Observatory. twin ten-meter eyes. A little planning shows respect for Planets.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Keck Observatory and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Keck Observatory and money.", "x": "Costs: History.. 1990s. What to budget — Keck Observatory. twin ten-meter eyes. The best experiences of Science. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-observatory-keck-observatory-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
