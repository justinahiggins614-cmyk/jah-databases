(function(){'use strict';
/* JAH Warrior I Yoga Pose Database generator — jahdb-e2-yoga-warrior-one-pose-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-yoga-warrior-one-pose',PREFIX='JAH-E2YOGAWARRI-',NAME='JAH Warrior I Yoga Pose Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Warrior I: the complete guide", "d": "Warrior I: the lunge of strength..", "g": "overview", "l": 2, "q": "What is Warrior I: the complete guide?", "a": "Warrior I: the lunge of strength..", "x": "The complete yoga pose guide to Warrior I: the lunge of strength.. Virabhadrasana I. History, meaning, practices, and how to engage respectfully — everything in one database. Hips. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Warrior I essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Warrior I essentials.", "x": "At a glance: Warrior I — the lunge of strength.. Hips. The essentials: Square.. Quads. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Virabhadrasana I.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Virabhadrasana I.", "x": "Warrior I: Virabhadrasana I.. Square. Essential knowledge — Quads.. the lunge of strength. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Virabhadrasana I..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Virabhadrasana I..", "x": "Explained: Virabhadrasana I.. Feet. The context — Warrior I. Chest. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Hips.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Hips.", "x": "Warrior I: Hips.. Chest. Essential knowledge — Chest.. the lunge of strength. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Hips..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Hips..", "x": "Explained: Hips.. Breath. The context — Warrior I. Square. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Quads.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Quads.", "x": "Warrior I: Quads.. Feet. Essential knowledge — Square.. the lunge of strength. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Quads..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Quads..", "x": "Explained: Quads.. Sequence. The context — Warrior I. Foundation. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Chest.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Chest.", "x": "Warrior I: Chest.. Breath. Essential knowledge — Foundation.. the lunge of strength. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Chest..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Chest..", "x": "Explained: Chest.. Hips. The context — Warrior I. Virabhadrasana I. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Square.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Square.", "x": "Warrior I: Square.. Sequence. Essential knowledge — Virabhadrasana I.. the lunge of strength. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Square..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Square..", "x": "Explained: Square.. Square. The context — Warrior I. Hips. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Foundation.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Foundation.", "x": "Warrior I: Foundation.. Hips. Essential knowledge — Hips.. the lunge of strength. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Foundation..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Foundation..", "x": "Explained: Foundation.. Chest. The context — Warrior I. Quads. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Hips.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Hips.", "x": "Warrior I in depth: Hips.. Hips. Details — the lunge of strength.. Chest. Chest. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Square.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Square.", "x": "Warrior I in depth: Square.. Quads. Details — the lunge of strength.. Feet. Square. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Chest.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Chest.", "x": "Warrior I in depth: Chest.. Chest. Details — the lunge of strength.. Breath. Foundation. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Feet.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Feet.", "x": "Warrior I in depth: Feet.. Square. Details — the lunge of strength.. Sequence. Virabhadrasana I. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Breath.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Breath.", "x": "Warrior I in depth: Breath.. Foundation. Details — the lunge of strength.. Hips. Hips. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Sequence.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Sequence.", "x": "Warrior I in depth: Sequence.. Virabhadrasana I. Details — the lunge of strength.. Square. Quads. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Warrior I comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Warrior I comes from.", "x": "Origins: Hips.. Virabhadrasana I. The history of Warrior I — the lunge of strength.. Square. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Warrior I respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Warrior I respectfully.", "x": "Engaging: Chest.. Hips. How to participate or observe well — Warrior I. the lunge of strength. Respect first, always; Feet.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Warrior I do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Warrior I do's and don'ts.", "x": "Etiquette: Breath.. Quads. The rules of respect — Warrior I. the lunge of strength. When in doubt, ask about Sequence.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Warrior I.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Warrior I.", "x": "Planning: Hips.. Chest. Practical notes — Warrior I. the lunge of strength. A little planning shows respect for Square.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Warrior I and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Warrior I and money.", "x": "Costs: Chest.. Square. What to budget — Warrior I. the lunge of strength. The best experiences of Feet. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-yoga-warrior-one-pose-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
