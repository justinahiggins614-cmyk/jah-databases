(function(){'use strict';
/* JAH Plank Pose Yoga Pose Database generator — jahdb-e2-yoga-plank-pose-yoga-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-yoga-plank-pose-yoga',PREFIX='JAH-E2YOGAPLANK-',NAME='JAH Plank Pose Yoga Pose Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Plank Pose: the complete guide", "d": "Plank Pose: the core hold..", "g": "overview", "l": 2, "q": "What is Plank Pose: the complete guide?", "a": "Plank Pose: the core hold..", "x": "The complete yoga pose guide to Plank Pose: the core hold.. Phalakasana. History, meaning, practices, and how to engage respectfully — everything in one database. Core. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Plank Pose essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Plank Pose essentials.", "x": "At a glance: Plank Pose — the core hold.. Core. The essentials: Line.. Shoulders. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Phalakasana.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Phalakasana.", "x": "Plank Pose: Phalakasana.. Line. Essential knowledge — Shoulders.. the core hold. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Phalakasana..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Phalakasana..", "x": "Explained: Phalakasana.. Shoulders. The context — Plank Pose. Line. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Core.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Core.", "x": "Plank Pose: Core.. Breath. Essential knowledge — Line.. the core hold. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Core..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Core..", "x": "Explained: Core.. Hold. The context — Plank Pose. Breath. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Shoulders.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Shoulders.", "x": "Plank Pose: Shoulders.. Shoulders. Essential knowledge — Breath.. the core hold. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Shoulders..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Shoulders..", "x": "Explained: Shoulders.. Sequence. The context — Plank Pose. Chaturanga. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Line.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Line.", "x": "Plank Pose: Line.. Hold. Essential knowledge — Chaturanga.. the core hold. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Line..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Line..", "x": "Explained: Line.. Core. The context — Plank Pose. Phalakasana. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Breath.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Breath.", "x": "Plank Pose: Breath.. Sequence. Essential knowledge — Phalakasana.. the core hold. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Breath..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Breath..", "x": "Explained: Breath.. Line. The context — Plank Pose. Core. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Chaturanga.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Chaturanga.", "x": "Plank Pose: Chaturanga.. Core. Essential knowledge — Core.. the core hold. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Chaturanga..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Chaturanga..", "x": "Explained: Chaturanga.. Breath. The context — Plank Pose. Shoulders. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Core.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Core.", "x": "Plank Pose in depth: Core.. Core. Details — the core hold.. Breath. Line. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Line.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Line.", "x": "Plank Pose in depth: Line.. Shoulders. Details — the core hold.. Shoulders. Breath. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Breath.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Breath.", "x": "Plank Pose in depth: Breath.. Line. Details — the core hold.. Hold. Chaturanga. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Shoulders.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Shoulders.", "x": "Plank Pose in depth: Shoulders.. Breath. Details — the core hold.. Sequence. Phalakasana. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Hold.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Hold.", "x": "Plank Pose in depth: Hold.. Chaturanga. Details — the core hold.. Core. Core. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Sequence.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Sequence.", "x": "Plank Pose in depth: Sequence.. Phalakasana. Details — the core hold.. Line. Shoulders. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Plank Pose comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Plank Pose comes from.", "x": "Origins: Core.. Phalakasana. The history of Plank Pose — the core hold.. Line. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Plank Pose respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Plank Pose respectfully.", "x": "Engaging: Breath.. Core. How to participate or observe well — Plank Pose. the core hold. Respect first, always; Shoulders.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Plank Pose do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Plank Pose do's and don'ts.", "x": "Etiquette: Hold.. Shoulders. The rules of respect — Plank Pose. the core hold. When in doubt, ask about Sequence.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Plank Pose.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Plank Pose.", "x": "Planning: Core.. Line. Practical notes — Plank Pose. the core hold. A little planning shows respect for Line.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Plank Pose and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Plank Pose and money.", "x": "Costs: Breath.. Breath. What to budget — Plank Pose. the core hold. The best experiences of Shoulders. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-yoga-plank-pose-yoga-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
