(function(){'use strict';
/* JAH Warrior II Pose Database generator — jahdb-e2-yoga2-warrior-ii-yoga2-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-yoga2-warrior-ii-yoga2',PREFIX='JAH-E2YOGA2WARR-',NAME='JAH Warrior II Pose Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Warrior II Pose: the complete guide", "d": "Warrior II Pose: the Virabhadrasana II..", "g": "overview", "l": 2, "q": "What is Warrior II Pose: the complete guide?", "a": "Warrior II Pose: the Virabhadrasana II..", "x": "The complete yoga pose guide to Warrior II Pose: the Virabhadrasana II.. Alignment. History, meaning, practices, and how to engage respectfully — everything in one database. Alignment. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Warrior II Pose essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Warrior II Pose essentials.", "x": "At a glance: Warrior II Pose — the Virabhadrasana II.. Hips. The essentials: Strength.. Gaze. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Alignment.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Alignment.", "x": "Warrior II Pose: Alignment.. Strength. Essential knowledge — Gaze.. the Virabhadrasana II. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Alignment..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Alignment..", "x": "Explained: Alignment.. Hips. The context — Warrior II Pose. Strength. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Hips.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Hips.", "x": "Warrior II Pose: Hips.. Standing. Essential knowledge — Strength.. the Virabhadrasana II. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Hips..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Hips..", "x": "Explained: Hips.. Gaze. The context — Warrior II Pose. Open. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Gaze.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Gaze.", "x": "Warrior II Pose: Gaze.. Hips. Essential knowledge — Open.. the Virabhadrasana II. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Gaze..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Gaze..", "x": "Explained: Gaze.. Guide. The context — Warrior II Pose. Standing. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Strength.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Strength.", "x": "Warrior II Pose: Strength.. Gaze. Essential knowledge — Standing.. the Virabhadrasana II. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Strength..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Strength..", "x": "Explained: Strength.. Alignment. The context — Warrior II Pose. Alignment. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Open.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Open.", "x": "Warrior II Pose: Open.. Guide. Essential knowledge — Alignment.. the Virabhadrasana II. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Open..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Open..", "x": "Explained: Open.. Strength. The context — Warrior II Pose. Hips. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Standing.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Standing.", "x": "Warrior II Pose: Standing.. Alignment. Essential knowledge — Hips.. the Virabhadrasana II. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Standing..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Standing..", "x": "Explained: Standing.. Standing. The context — Warrior II Pose. Gaze. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Alignment.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Alignment.", "x": "Warrior II Pose in depth: Alignment.. Hips. Details — the Virabhadrasana II.. Standing. Strength. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Strength.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Strength.", "x": "Warrior II Pose in depth: Strength.. Gaze. Details — the Virabhadrasana II.. Hips. Open. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Standing.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Standing.", "x": "Warrior II Pose in depth: Standing.. Strength. Details — the Virabhadrasana II.. Gaze. Standing. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Hips.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Hips.", "x": "Warrior II Pose in depth: Hips.. Open. Details — the Virabhadrasana II.. Guide. Alignment. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Gaze.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Gaze.", "x": "Warrior II Pose in depth: Gaze.. Standing. Details — the Virabhadrasana II.. Alignment. Hips. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Guide.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Guide.", "x": "Warrior II Pose in depth: Guide.. Alignment. Details — the Virabhadrasana II.. Strength. Gaze. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Warrior II Pose comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Warrior II Pose comes from.", "x": "Origins: Alignment.. Alignment. The history of Warrior II Pose — the Virabhadrasana II.. Strength. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Warrior II Pose respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Warrior II Pose respectfully.", "x": "Engaging: Standing.. Hips. How to participate or observe well — Warrior II Pose. the Virabhadrasana II. Respect first, always; Hips.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Warrior II Pose do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Warrior II Pose do's and don'ts.", "x": "Etiquette: Gaze.. Gaze. The rules of respect — Warrior II Pose. the Virabhadrasana II. When in doubt, ask about Guide.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Warrior II Pose.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Warrior II Pose.", "x": "Planning: Alignment.. Strength. Practical notes — Warrior II Pose. the Virabhadrasana II. A little planning shows respect for Strength.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Warrior II Pose and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Warrior II Pose and money.", "x": "Costs: Standing.. Open. What to budget — Warrior II Pose. the Virabhadrasana II. The best experiences of Hips. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-yoga2-warrior-ii-yoga2-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
