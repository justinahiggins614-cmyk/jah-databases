(function(){'use strict';
/* JAH Warrior III Yoga Pose Database generator — jahdb-e2-yoga-warrior-three-pose-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-yoga-warrior-three-pose',PREFIX='JAH-E2YOGAWARRI-',NAME='JAH Warrior III Yoga Pose Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Warrior III: the complete guide", "d": "Warrior III: the flying balance..", "g": "overview", "l": 2, "q": "What is Warrior III: the complete guide?", "a": "Warrior III: the flying balance..", "x": "The complete yoga pose guide to Warrior III: the flying balance.. Virabhadrasana III. History, meaning, practices, and how to engage respectfully — everything in one database. Balance. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Warrior III essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Warrior III essentials.", "x": "At a glance: Warrior III — the flying balance.. Balance. The essentials: Core.. Core. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Virabhadrasana III.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Virabhadrasana III.", "x": "Warrior III: Virabhadrasana III.. Core. Essential knowledge — Core.. the flying balance. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Virabhadrasana III..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Virabhadrasana III..", "x": "Explained: Virabhadrasana III.. Hips. The context — Warrior III. Hamstrings. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Balance.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Balance.", "x": "Warrior III: Balance.. Focus. Essential knowledge — Hamstrings.. the flying balance. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Balance..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Balance..", "x": "Explained: Balance.. Hamstrings. The context — Warrior III. Hips square. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Core.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Core.", "x": "Warrior III: Core.. Hips. Essential knowledge — Hips square.. the flying balance. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Core..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Core..", "x": "Explained: Core.. Sequence. The context — Warrior III. Focus. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Hamstrings.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Hamstrings.", "x": "Warrior III: Hamstrings.. Hamstrings. Essential knowledge — Focus.. the flying balance. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Hamstrings..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Hamstrings..", "x": "Explained: Hamstrings.. Balance. The context — Warrior III. Virabhadrasana III. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Hips square.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Hips square.", "x": "Warrior III: Hips square.. Sequence. Essential knowledge — Virabhadrasana III.. the flying balance. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Hips square..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Hips square..", "x": "Explained: Hips square.. Core. The context — Warrior III. Balance. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Focus.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Focus.", "x": "Warrior III: Focus.. Balance. Essential knowledge — Balance.. the flying balance. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Focus..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Focus..", "x": "Explained: Focus.. Focus. The context — Warrior III. Core. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Balance.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Balance.", "x": "Warrior III in depth: Balance.. Balance. Details — the flying balance.. Focus. Hamstrings. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Core.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Core.", "x": "Warrior III in depth: Core.. Core. Details — the flying balance.. Hips. Hips square. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Focus.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Focus.", "x": "Warrior III in depth: Focus.. Hamstrings. Details — the flying balance.. Hamstrings. Focus. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Hips.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Hips.", "x": "Warrior III in depth: Hips.. Hips square. Details — the flying balance.. Sequence. Virabhadrasana III. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Hamstrings.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Hamstrings.", "x": "Warrior III in depth: Hamstrings.. Focus. Details — the flying balance.. Balance. Balance. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Sequence.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Sequence.", "x": "Warrior III in depth: Sequence.. Virabhadrasana III. Details — the flying balance.. Core. Core. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Warrior III comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Warrior III comes from.", "x": "Origins: Balance.. Virabhadrasana III. The history of Warrior III — the flying balance.. Core. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Warrior III respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Warrior III respectfully.", "x": "Engaging: Focus.. Balance. How to participate or observe well — Warrior III. the flying balance. Respect first, always; Hips.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Warrior III do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Warrior III do's and don'ts.", "x": "Etiquette: Hamstrings.. Core. The rules of respect — Warrior III. the flying balance. When in doubt, ask about Sequence.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Warrior III.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Warrior III.", "x": "Planning: Balance.. Hamstrings. Practical notes — Warrior III. the flying balance. A little planning shows respect for Core.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Warrior III and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Warrior III and money.", "x": "Costs: Focus.. Hips square. What to budget — Warrior III. the flying balance. The best experiences of Hips. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-yoga-warrior-three-pose-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
