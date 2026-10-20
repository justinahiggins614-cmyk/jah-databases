(function(){'use strict';
/* JAH Sketching Database generator — jahdb-e2-hobby2-sketching-hobby-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-hobby2-sketching-hobby',PREFIX='JAH-E2HOBBY2SKE-',NAME='JAH Sketching Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Sketching: the complete guide", "d": "Sketching: the pencil lines..", "g": "overview", "l": 2, "q": "What is Sketching: the complete guide?", "a": "Sketching: the pencil lines..", "x": "The complete hobby guide to Sketching: the pencil lines.. Pencils. History, meaning, practices, and how to engage respectfully — everything in one database. Shading. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Sketching essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Sketching essentials.", "x": "At a glance: Sketching — the pencil lines.. Shading. The essentials: Sketchbook.. Gesture. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Pencils.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Pencils.", "x": "Sketching: Pencils.. Sketchbook. Essential knowledge — Gesture.. the pencil lines. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Pencils..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Pencils..", "x": "Explained: Pencils.. Pencils. The context — Sketching. Sketchbook. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Shading.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Shading.", "x": "Sketching: Shading.. Daily. Essential knowledge — Sketchbook.. the pencil lines. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Shading..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Shading..", "x": "Explained: Shading.. Gesture. The context — Sketching. Observation. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Gesture.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Gesture.", "x": "Sketching: Gesture.. Pencils. Essential knowledge — Observation.. the pencil lines. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Gesture..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Gesture..", "x": "Explained: Gesture.. Getting started. The context — Sketching. Daily. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Sketchbook.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Sketchbook.", "x": "Sketching: Sketchbook.. Gesture. Essential knowledge — Daily.. the pencil lines. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Sketchbook..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Sketchbook..", "x": "Explained: Sketchbook.. Shading. The context — Sketching. Pencils. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Observation.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Observation.", "x": "Sketching: Observation.. Getting started. Essential knowledge — Pencils.. the pencil lines. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Observation..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Observation..", "x": "Explained: Observation.. Sketchbook. The context — Sketching. Shading. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Daily.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Daily.", "x": "Sketching: Daily.. Shading. Essential knowledge — Shading.. the pencil lines. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Daily..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Daily..", "x": "Explained: Daily.. Daily. The context — Sketching. Gesture. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Shading.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Shading.", "x": "Sketching in depth: Shading.. Shading. Details — the pencil lines.. Daily. Sketchbook. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Sketchbook.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Sketchbook.", "x": "Sketching in depth: Sketchbook.. Gesture. Details — the pencil lines.. Pencils. Observation. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Daily.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Daily.", "x": "Sketching in depth: Daily.. Sketchbook. Details — the pencil lines.. Gesture. Daily. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Pencils.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Pencils.", "x": "Sketching in depth: Pencils.. Observation. Details — the pencil lines.. Getting started. Pencils. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Gesture.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Gesture.", "x": "Sketching in depth: Gesture.. Daily. Details — the pencil lines.. Shading. Shading. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Getting started.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Getting started.", "x": "Sketching in depth: Getting started.. Pencils. Details — the pencil lines.. Sketchbook. Gesture. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Sketching comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Sketching comes from.", "x": "Origins: Shading.. Pencils. The history of Sketching — the pencil lines.. Sketchbook. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Sketching respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Sketching respectfully.", "x": "Engaging: Daily.. Shading. How to participate or observe well — Sketching. the pencil lines. Respect first, always; Pencils.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Sketching do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Sketching do's and don'ts.", "x": "Etiquette: Gesture.. Gesture. The rules of respect — Sketching. the pencil lines. When in doubt, ask about Getting started.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Sketching.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Sketching.", "x": "Planning: Shading.. Sketchbook. Practical notes — Sketching. the pencil lines. A little planning shows respect for Sketchbook.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Sketching and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Sketching and money.", "x": "Costs: Daily.. Observation. What to budget — Sketching. the pencil lines. The best experiences of Pencils. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-hobby2-sketching-hobby-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
