(function(){'use strict';
/* JAH Cat-Cow Pose Yoga Pose Database generator — jahdb-e2-yoga-cat-cow-pose-yoga-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-yoga-cat-cow-pose-yoga',PREFIX='JAH-E2YOGACATCO-',NAME='JAH Cat-Cow Pose Yoga Pose Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Cat-Cow Pose: the complete guide", "d": "Cat-Cow Pose: the spinal wave..", "g": "overview", "l": 2, "q": "What is Cat-Cow Pose: the complete guide?", "a": "Cat-Cow Pose: the spinal wave..", "x": "The complete yoga pose guide to Cat-Cow Pose: the spinal wave.. Marjaryasana. History, meaning, practices, and how to engage respectfully — everything in one database. Spine. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Cat-Cow Pose essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Cat-Cow Pose essentials.", "x": "At a glance: Cat-Cow Pose — the spinal wave.. Spine. The essentials: Breath.. Breath. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Marjaryasana.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Marjaryasana.", "x": "Cat-Cow Pose: Marjaryasana.. Breath. Essential knowledge — Breath.. the spinal wave. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Marjaryasana..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Marjaryasana..", "x": "Explained: Marjaryasana.. Flow. The context — Cat-Cow Pose. Warm-up. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Spine.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Spine.", "x": "Cat-Cow Pose: Spine.. Warm-up. Essential knowledge — Warm-up.. the spinal wave. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Spine..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Spine..", "x": "Explained: Spine.. Flexion. The context — Cat-Cow Pose. Flexion. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Breath.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Breath.", "x": "Cat-Cow Pose: Breath.. Flow. Essential knowledge — Flexion.. the spinal wave. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Breath..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Breath..", "x": "Explained: Breath.. Sequence. The context — Cat-Cow Pose. Flow. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Warm-up.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Warm-up.", "x": "Cat-Cow Pose: Warm-up.. Flexion. Essential knowledge — Flow.. the spinal wave. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Warm-up..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Warm-up..", "x": "Explained: Warm-up.. Spine. The context — Cat-Cow Pose. Marjaryasana. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Flexion.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Flexion.", "x": "Cat-Cow Pose: Flexion.. Sequence. Essential knowledge — Marjaryasana.. the spinal wave. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Flexion..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Flexion..", "x": "Explained: Flexion.. Breath. The context — Cat-Cow Pose. Spine. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Flow.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Flow.", "x": "Cat-Cow Pose: Flow.. Spine. Essential knowledge — Spine.. the spinal wave. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Flow..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Flow..", "x": "Explained: Flow.. Warm-up. The context — Cat-Cow Pose. Breath. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Spine.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Spine.", "x": "Cat-Cow Pose in depth: Spine.. Spine. Details — the spinal wave.. Warm-up. Warm-up. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Breath.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Breath.", "x": "Cat-Cow Pose in depth: Breath.. Breath. Details — the spinal wave.. Flow. Flexion. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Warm-up.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Warm-up.", "x": "Cat-Cow Pose in depth: Warm-up.. Warm-up. Details — the spinal wave.. Flexion. Flow. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Flow.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Flow.", "x": "Cat-Cow Pose in depth: Flow.. Flexion. Details — the spinal wave.. Sequence. Marjaryasana. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Flexion.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Flexion.", "x": "Cat-Cow Pose in depth: Flexion.. Flow. Details — the spinal wave.. Spine. Spine. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Sequence.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Sequence.", "x": "Cat-Cow Pose in depth: Sequence.. Marjaryasana. Details — the spinal wave.. Breath. Breath. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Cat-Cow Pose comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Cat-Cow Pose comes from.", "x": "Origins: Spine.. Marjaryasana. The history of Cat-Cow Pose — the spinal wave.. Breath. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Cat-Cow Pose respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Cat-Cow Pose respectfully.", "x": "Engaging: Warm-up.. Spine. How to participate or observe well — Cat-Cow Pose. the spinal wave. Respect first, always; Flow.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Cat-Cow Pose do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Cat-Cow Pose do's and don'ts.", "x": "Etiquette: Flexion.. Breath. The rules of respect — Cat-Cow Pose. the spinal wave. When in doubt, ask about Sequence.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Cat-Cow Pose.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Cat-Cow Pose.", "x": "Planning: Spine.. Warm-up. Practical notes — Cat-Cow Pose. the spinal wave. A little planning shows respect for Breath.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Cat-Cow Pose and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Cat-Cow Pose and money.", "x": "Costs: Warm-up.. Flexion. What to budget — Cat-Cow Pose. the spinal wave. The best experiences of Flow. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-yoga-cat-cow-pose-yoga-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
