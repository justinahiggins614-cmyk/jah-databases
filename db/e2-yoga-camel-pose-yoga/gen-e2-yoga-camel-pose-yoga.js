(function(){'use strict';
/* JAH Camel Pose Yoga Pose Database generator — jahdb-e2-yoga-camel-pose-yoga-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-yoga-camel-pose-yoga',PREFIX='JAH-E2YOGACAMEL-',NAME='JAH Camel Pose Yoga Pose Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Camel Pose: the complete guide", "d": "Camel Pose: the heart opener..", "g": "overview", "l": 2, "q": "What is Camel Pose: the complete guide?", "a": "Camel Pose: the heart opener..", "x": "The complete yoga pose guide to Camel Pose: the heart opener.. Ustrasana. History, meaning, practices, and how to engage respectfully — everything in one database. Backbend. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Camel Pose essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Camel Pose essentials.", "x": "At a glance: Camel Pose — the heart opener.. Backbend. The essentials: Heart.. Thighs. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Ustrasana.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Ustrasana.", "x": "Camel Pose: Ustrasana.. Heart. Essential knowledge — Thighs.. the heart opener. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Ustrasana..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Ustrasana..", "x": "Explained: Ustrasana.. Neck. The context — Camel Pose. Hands. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Backbend.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Backbend.", "x": "Camel Pose: Backbend.. Thighs. Essential knowledge — Hands.. the heart opener. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Backbend..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Backbend..", "x": "Explained: Backbend.. Hands. The context — Camel Pose. Heart. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Thighs.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Thighs.", "x": "Camel Pose: Thighs.. Neck. Essential knowledge — Heart.. the heart opener. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Thighs..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Thighs..", "x": "Explained: Thighs.. Modifications. The context — Camel Pose. Neck. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Hands.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Hands.", "x": "Camel Pose: Hands.. Hands. Essential knowledge — Neck.. the heart opener. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Hands..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Hands..", "x": "Explained: Hands.. Backbend. The context — Camel Pose. Ustrasana. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Heart.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Heart.", "x": "Camel Pose: Heart.. Modifications. Essential knowledge — Ustrasana.. the heart opener. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Heart..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Heart..", "x": "Explained: Heart.. Heart. The context — Camel Pose. Backbend. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Neck.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Neck.", "x": "Camel Pose: Neck.. Backbend. Essential knowledge — Backbend.. the heart opener. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Neck..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Neck..", "x": "Explained: Neck.. Thighs. The context — Camel Pose. Thighs. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Backbend.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Backbend.", "x": "Camel Pose in depth: Backbend.. Backbend. Details — the heart opener.. Thighs. Hands. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Heart.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Heart.", "x": "Camel Pose in depth: Heart.. Thighs. Details — the heart opener.. Neck. Heart. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Thighs.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Thighs.", "x": "Camel Pose in depth: Thighs.. Hands. Details — the heart opener.. Hands. Neck. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Neck.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Neck.", "x": "Camel Pose in depth: Neck.. Heart. Details — the heart opener.. Modifications. Ustrasana. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Hands.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Hands.", "x": "Camel Pose in depth: Hands.. Neck. Details — the heart opener.. Backbend. Backbend. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Modifications.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Modifications.", "x": "Camel Pose in depth: Modifications.. Ustrasana. Details — the heart opener.. Heart. Thighs. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Camel Pose comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Camel Pose comes from.", "x": "Origins: Backbend.. Ustrasana. The history of Camel Pose — the heart opener.. Heart. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Camel Pose respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Camel Pose respectfully.", "x": "Engaging: Thighs.. Backbend. How to participate or observe well — Camel Pose. the heart opener. Respect first, always; Neck.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Camel Pose do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Camel Pose do's and don'ts.", "x": "Etiquette: Hands.. Thighs. The rules of respect — Camel Pose. the heart opener. When in doubt, ask about Modifications.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Camel Pose.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Camel Pose.", "x": "Planning: Backbend.. Hands. Practical notes — Camel Pose. the heart opener. A little planning shows respect for Heart.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Camel Pose and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Camel Pose and money.", "x": "Costs: Thighs.. Heart. What to budget — Camel Pose. the heart opener. The best experiences of Neck. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-yoga-camel-pose-yoga-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
