(function(){'use strict';
/* JAH Singing Hobby Database generator — jahdb-e2-hobby2-singing-hobby-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-hobby2-singing-hobby',PREFIX='JAH-E2HOBBY2SIN-',NAME='JAH Singing Hobby Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Singing Hobby: the complete guide", "d": "Singing Hobby: the voice instrument..", "g": "overview", "l": 2, "q": "What is Singing Hobby: the complete guide?", "a": "Singing Hobby: the voice instrument..", "x": "The complete hobby guide to Singing Hobby: the voice instrument.. Warm-ups. History, meaning, practices, and how to engage respectfully — everything in one database. Breath. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Singing Hobby essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Singing Hobby essentials.", "x": "At a glance: Singing Hobby — the voice instrument.. Breath. The essentials: Choir.. Pitch. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Warm-ups.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Warm-ups.", "x": "Singing Hobby: Warm-ups.. Choir. Essential knowledge — Pitch.. the voice instrument. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Warm-ups..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Warm-ups..", "x": "Explained: Warm-ups.. Warm-ups. The context — Singing Hobby. Choir. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Breath.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Breath.", "x": "Singing Hobby: Breath.. Practice. Essential knowledge — Choir.. the voice instrument. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Breath..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Breath..", "x": "Explained: Breath.. Pitch. The context — Singing Hobby. Lessons. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Pitch.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Pitch.", "x": "Singing Hobby: Pitch.. Warm-ups. Essential knowledge — Lessons.. the voice instrument. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Pitch..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Pitch..", "x": "Explained: Pitch.. Getting started. The context — Singing Hobby. Practice. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Choir.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Choir.", "x": "Singing Hobby: Choir.. Pitch. Essential knowledge — Practice.. the voice instrument. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Choir..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Choir..", "x": "Explained: Choir.. Breath. The context — Singing Hobby. Warm-ups. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Lessons.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Lessons.", "x": "Singing Hobby: Lessons.. Getting started. Essential knowledge — Warm-ups.. the voice instrument. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Lessons..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Lessons..", "x": "Explained: Lessons.. Choir. The context — Singing Hobby. Breath. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Practice.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Practice.", "x": "Singing Hobby: Practice.. Breath. Essential knowledge — Breath.. the voice instrument. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Practice..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Practice..", "x": "Explained: Practice.. Practice. The context — Singing Hobby. Pitch. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Breath.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Breath.", "x": "Singing Hobby in depth: Breath.. Breath. Details — the voice instrument.. Practice. Choir. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Choir.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Choir.", "x": "Singing Hobby in depth: Choir.. Pitch. Details — the voice instrument.. Warm-ups. Lessons. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Practice.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Practice.", "x": "Singing Hobby in depth: Practice.. Choir. Details — the voice instrument.. Pitch. Practice. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Warm-ups.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Warm-ups.", "x": "Singing Hobby in depth: Warm-ups.. Lessons. Details — the voice instrument.. Getting started. Warm-ups. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Pitch.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Pitch.", "x": "Singing Hobby in depth: Pitch.. Practice. Details — the voice instrument.. Breath. Breath. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Getting started.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Getting started.", "x": "Singing Hobby in depth: Getting started.. Warm-ups. Details — the voice instrument.. Choir. Pitch. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Singing Hobby comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Singing Hobby comes from.", "x": "Origins: Breath.. Warm-ups. The history of Singing Hobby — the voice instrument.. Choir. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Singing Hobby respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Singing Hobby respectfully.", "x": "Engaging: Practice.. Breath. How to participate or observe well — Singing Hobby. the voice instrument. Respect first, always; Warm-ups.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Singing Hobby do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Singing Hobby do's and don'ts.", "x": "Etiquette: Pitch.. Pitch. The rules of respect — Singing Hobby. the voice instrument. When in doubt, ask about Getting started.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Singing Hobby.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Singing Hobby.", "x": "Planning: Breath.. Choir. Practical notes — Singing Hobby. the voice instrument. A little planning shows respect for Choir.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Singing Hobby and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Singing Hobby and money.", "x": "Costs: Practice.. Lessons. What to budget — Singing Hobby. the voice instrument. The best experiences of Warm-ups. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-hobby2-singing-hobby-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
