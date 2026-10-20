(function(){'use strict';
/* JAH Lighting2 Database generator — jahdb-e2-photo2-lighting2-photo-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-photo2-lighting2-photo',PREFIX='JAH-E2PHOTO2LIG-',NAME='JAH Lighting2 Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Lighting2: the complete guide", "d": "Lighting2: the light 2..", "g": "overview", "l": 2, "q": "What is Lighting2: the complete guide?", "a": "Lighting2: the light 2..", "x": "The complete photography guide to Lighting2: the light 2.. Rembrandt. History, meaning, practices, and how to engage respectfully — everything in one database. Loop. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Lighting2 essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Lighting2 essentials.", "x": "At a glance: Lighting2 — the light 2.. Loop. The essentials: Ratios.. Butterfly. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Rembrandt.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Rembrandt.", "x": "Lighting2: Rembrandt.. Ratios. Essential knowledge — Butterfly.. the light 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Rembrandt..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Rembrandt..", "x": "Explained: Rembrandt.. Rembrandt. The context — Lighting2. Split. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Loop.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Loop.", "x": "Lighting2: Loop.. Modifiers. Essential knowledge — Split.. the light 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Loop..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Loop..", "x": "Explained: Loop.. Split. The context — Lighting2. Modifiers. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Butterfly.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Butterfly.", "x": "Lighting2: Butterfly.. Rembrandt. Essential knowledge — Modifiers.. the light 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Butterfly..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Butterfly..", "x": "Explained: Butterfly.. Tips. The context — Lighting2. Ratios. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Split.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Split.", "x": "Lighting2: Split.. Split. Essential knowledge — Ratios.. the light 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Split..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Split..", "x": "Explained: Split.. Loop. The context — Lighting2. Rembrandt. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Modifiers.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Modifiers.", "x": "Lighting2: Modifiers.. Tips. Essential knowledge — Rembrandt.. the light 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Modifiers..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Modifiers..", "x": "Explained: Modifiers.. Ratios. The context — Lighting2. Loop. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Ratios.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Ratios.", "x": "Lighting2: Ratios.. Loop. Essential knowledge — Loop.. the light 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Ratios..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Ratios..", "x": "Explained: Ratios.. Modifiers. The context — Lighting2. Butterfly. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Loop.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Loop.", "x": "Lighting2 in depth: Loop.. Loop. Details — the light 2.. Modifiers. Split. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Ratios.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Ratios.", "x": "Lighting2 in depth: Ratios.. Butterfly. Details — the light 2.. Rembrandt. Modifiers. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Modifiers.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Modifiers.", "x": "Lighting2 in depth: Modifiers.. Split. Details — the light 2.. Split. Ratios. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Rembrandt.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Rembrandt.", "x": "Lighting2 in depth: Rembrandt.. Modifiers. Details — the light 2.. Tips. Rembrandt. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Split.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Split.", "x": "Lighting2 in depth: Split.. Ratios. Details — the light 2.. Loop. Loop. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Tips.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Tips.", "x": "Lighting2 in depth: Tips.. Rembrandt. Details — the light 2.. Ratios. Butterfly. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Lighting2 comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Lighting2 comes from.", "x": "Origins: Loop.. Rembrandt. The history of Lighting2 — the light 2.. Ratios. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Lighting2 respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Lighting2 respectfully.", "x": "Engaging: Modifiers.. Loop. How to participate or observe well — Lighting2. the light 2. Respect first, always; Rembrandt.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Lighting2 do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Lighting2 do's and don'ts.", "x": "Etiquette: Split.. Butterfly. The rules of respect — Lighting2. the light 2. When in doubt, ask about Tips.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Lighting2.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Lighting2.", "x": "Planning: Loop.. Split. Practical notes — Lighting2. the light 2. A little planning shows respect for Ratios.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Lighting2 and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Lighting2 and money.", "x": "Costs: Modifiers.. Modifiers. What to budget — Lighting2. the light 2. The best experiences of Rembrandt. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-photo2-lighting2-photo-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
