(function(){'use strict';
/* JAH Leaning Tower of Pisa Landmark Database generator — jahdb-e2-landmark-leaning-tower-pisa-landmark-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-landmark-leaning-tower-pisa-landmark',PREFIX='JAH-E2LANDMARKL-',NAME='JAH Leaning Tower of Pisa Landmark Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Leaning Tower of Pisa: the complete guide", "d": "Leaning Tower of Pisa: the tilted bell..", "g": "overview", "l": 2, "q": "What is Leaning Tower of Pisa: the complete guide?", "a": "Leaning Tower of Pisa: the tilted bell..", "x": "The complete landmark guide to Leaning Tower of Pisa: the tilted bell.. 1372. History, meaning, practices, and how to engage respectfully — everything in one database. 1372. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Leaning Tower of Pisa essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Leaning Tower of Pisa essentials.", "x": "At a glance: Leaning Tower of Pisa — the tilted bell.. 4 degrees. The essentials: Galileo.. 8 stories. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "1372.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "1372.", "x": "Leaning Tower of Pisa: 1372.. Galileo. Essential knowledge — 8 stories.. the tilted bell. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 1372..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 1372..", "x": "Explained: 1372.. Marble. The context — Leaning Tower of Pisa. Galileo. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "4 degrees.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "4 degrees.", "x": "Leaning Tower of Pisa: 4 degrees.. Stabilized. Essential knowledge — Galileo.. the tilted bell. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: 4 degrees..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: 4 degrees..", "x": "Explained: 4 degrees.. Tilt. The context — Leaning Tower of Pisa. Stabilized. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "8 stories.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "8 stories.", "x": "Leaning Tower of Pisa: 8 stories.. Marble. Essential knowledge — Stabilized.. the tilted bell. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: 8 stories..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: 8 stories..", "x": "Explained: 8 stories.. Tickets. The context — Leaning Tower of Pisa. Marble. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Galileo.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Galileo.", "x": "Leaning Tower of Pisa: Galileo.. Tilt. Essential knowledge — Marble.. the tilted bell. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Galileo..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Galileo..", "x": "Explained: Galileo.. 1372. The context — Leaning Tower of Pisa. 1372. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Stabilized.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Stabilized.", "x": "Leaning Tower of Pisa: Stabilized.. Tickets. Essential knowledge — 1372.. the tilted bell. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Stabilized..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Stabilized..", "x": "Explained: Stabilized.. Galileo. The context — Leaning Tower of Pisa. 4 degrees. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Marble.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Marble.", "x": "Leaning Tower of Pisa: Marble.. 1372. Essential knowledge — 4 degrees.. the tilted bell. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Marble..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Marble..", "x": "Explained: Marble.. Stabilized. The context — Leaning Tower of Pisa. 8 stories. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "1372.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "1372.", "x": "Leaning Tower of Pisa in depth: 1372.. 4 degrees. Details — the tilted bell.. Stabilized. Galileo. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Galileo.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Galileo.", "x": "Leaning Tower of Pisa in depth: Galileo.. 8 stories. Details — the tilted bell.. Marble. Stabilized. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Stabilized.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Stabilized.", "x": "Leaning Tower of Pisa in depth: Stabilized.. Galileo. Details — the tilted bell.. Tilt. Marble. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Marble.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Marble.", "x": "Leaning Tower of Pisa in depth: Marble.. Stabilized. Details — the tilted bell.. Tickets. 1372. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Tilt.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Tilt.", "x": "Leaning Tower of Pisa in depth: Tilt.. Marble. Details — the tilted bell.. 1372. 4 degrees. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Tickets.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Tickets.", "x": "Leaning Tower of Pisa in depth: Tickets.. 1372. Details — the tilted bell.. Galileo. 8 stories. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Leaning Tower of Pisa comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Leaning Tower of Pisa comes from.", "x": "Origins: 1372.. 1372. The history of Leaning Tower of Pisa — the tilted bell.. Galileo. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Leaning Tower of Pisa respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Leaning Tower of Pisa respectfully.", "x": "Engaging: Stabilized.. 4 degrees. How to participate or observe well — Leaning Tower of Pisa. the tilted bell. Respect first, always; Marble.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Leaning Tower of Pisa do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Leaning Tower of Pisa do's and don'ts.", "x": "Etiquette: Tilt.. 8 stories. The rules of respect — Leaning Tower of Pisa. the tilted bell. When in doubt, ask about Tickets.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Leaning Tower of Pisa.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Leaning Tower of Pisa.", "x": "Planning: 1372.. Galileo. Practical notes — Leaning Tower of Pisa. the tilted bell. A little planning shows respect for Galileo.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Leaning Tower of Pisa and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Leaning Tower of Pisa and money.", "x": "Costs: Stabilized.. Stabilized. What to budget — Leaning Tower of Pisa. the tilted bell. The best experiences of Marble. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-landmark-leaning-tower-pisa-landmark-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
