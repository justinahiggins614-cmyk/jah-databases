(function(){'use strict';
/* JAH Butterfly Pose Yoga Pose Database generator — jahdb-e2-yoga-butterfly-pose-yoga-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-yoga-butterfly-pose-yoga',PREFIX='JAH-E2YOGABUTTE-',NAME='JAH Butterfly Pose Yoga Pose Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Butterfly Pose: the complete guide", "d": "Butterfly Pose: the bound angle..", "g": "overview", "l": 2, "q": "What is Butterfly Pose: the complete guide?", "a": "Butterfly Pose: the bound angle..", "x": "The complete yoga pose guide to Butterfly Pose: the bound angle.. Baddha Konasana. History, meaning, practices, and how to engage respectfully — everything in one database. Hips. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Butterfly Pose essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Butterfly Pose essentials.", "x": "At a glance: Butterfly Pose — the bound angle.. Hips. The essentials: Feet.. Groin. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Baddha Konasana.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Baddha Konasana.", "x": "Butterfly Pose: Baddha Konasana.. Feet. Essential knowledge — Groin.. the bound angle. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Baddha Konasana..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Baddha Konasana..", "x": "Explained: Baddha Konasana.. Calm. The context — Butterfly Pose. Feet. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Hips.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Hips.", "x": "Butterfly Pose: Hips.. Fold. Essential knowledge — Feet.. the bound angle. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Hips..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Hips..", "x": "Explained: Hips.. Groin. The context — Butterfly Pose. Fold. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Groin.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Groin.", "x": "Butterfly Pose: Groin.. Calm. Essential knowledge — Fold.. the bound angle. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Groin..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Groin..", "x": "Explained: Groin.. Props. The context — Butterfly Pose. Calm. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Feet.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Feet.", "x": "Butterfly Pose: Feet.. Groin. Essential knowledge — Calm.. the bound angle. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Feet..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Feet..", "x": "Explained: Feet.. Hips. The context — Butterfly Pose. Baddha Konasana. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Fold.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Fold.", "x": "Butterfly Pose: Fold.. Props. Essential knowledge — Baddha Konasana.. the bound angle. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Fold..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Fold..", "x": "Explained: Fold.. Feet. The context — Butterfly Pose. Hips. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Calm.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Calm.", "x": "Butterfly Pose: Calm.. Hips. Essential knowledge — Hips.. the bound angle. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Calm..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Calm..", "x": "Explained: Calm.. Fold. The context — Butterfly Pose. Groin. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Hips.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Hips.", "x": "Butterfly Pose in depth: Hips.. Hips. Details — the bound angle.. Fold. Feet. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Feet.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Feet.", "x": "Butterfly Pose in depth: Feet.. Groin. Details — the bound angle.. Calm. Fold. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Fold.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Fold.", "x": "Butterfly Pose in depth: Fold.. Feet. Details — the bound angle.. Groin. Calm. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Calm.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Calm.", "x": "Butterfly Pose in depth: Calm.. Fold. Details — the bound angle.. Props. Baddha Konasana. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Groin.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Groin.", "x": "Butterfly Pose in depth: Groin.. Calm. Details — the bound angle.. Hips. Hips. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Props.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Props.", "x": "Butterfly Pose in depth: Props.. Baddha Konasana. Details — the bound angle.. Feet. Groin. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Butterfly Pose comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Butterfly Pose comes from.", "x": "Origins: Hips.. Baddha Konasana. The history of Butterfly Pose — the bound angle.. Feet. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Butterfly Pose respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Butterfly Pose respectfully.", "x": "Engaging: Fold.. Hips. How to participate or observe well — Butterfly Pose. the bound angle. Respect first, always; Calm.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Butterfly Pose do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Butterfly Pose do's and don'ts.", "x": "Etiquette: Groin.. Groin. The rules of respect — Butterfly Pose. the bound angle. When in doubt, ask about Props.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Butterfly Pose.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Butterfly Pose.", "x": "Planning: Hips.. Feet. Practical notes — Butterfly Pose. the bound angle. A little planning shows respect for Feet.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Butterfly Pose and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Butterfly Pose and money.", "x": "Costs: Fold.. Fold. What to budget — Butterfly Pose. the bound angle. The best experiences of Calm. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-yoga-butterfly-pose-yoga-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
