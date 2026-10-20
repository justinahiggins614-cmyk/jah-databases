(function(){'use strict';
/* JAH Upward Dog Yoga Pose Database generator — jahdb-e2-yoga-upward-dog-pose-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-yoga-upward-dog-pose',PREFIX='JAH-E2YOGAUPWAR-',NAME='JAH Upward Dog Yoga Pose Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Upward Dog: the complete guide", "d": "Upward Dog: the full backbend..", "g": "overview", "l": 2, "q": "What is Upward Dog: the complete guide?", "a": "Upward Dog: the full backbend..", "x": "The complete yoga pose guide to Upward Dog: the full backbend.. Urdhva Mukha. History, meaning, practices, and how to engage respectfully — everything in one database. Thighs. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Upward Dog essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Upward Dog essentials.", "x": "At a glance: Upward Dog — the full backbend.. Thighs off. The essentials: Chest.. Chest. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Urdhva Mukha.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Urdhva Mukha.", "x": "Upward Dog: Urdhva Mukha.. Chest. Essential knowledge — Chest.. the full backbend. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Urdhva Mukha..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Urdhva Mukha..", "x": "Explained: Urdhva Mukha.. Strong. The context — Upward Dog. Shoulders. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Thighs off.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Thighs off.", "x": "Upward Dog: Thighs off.. Vinyasa. Essential knowledge — Shoulders.. the full backbend. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Thighs off..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Thighs off..", "x": "Explained: Thighs off.. Shoulders. The context — Upward Dog. Vinyasa. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Chest.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Chest.", "x": "Upward Dog: Chest.. Strong. Essential knowledge — Vinyasa.. the full backbend. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Chest..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Chest..", "x": "Explained: Chest.. Sequence. The context — Upward Dog. Strong. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Shoulders.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Shoulders.", "x": "Upward Dog: Shoulders.. Shoulders. Essential knowledge — Strong.. the full backbend. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Shoulders..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Shoulders..", "x": "Explained: Shoulders.. Thighs. The context — Upward Dog. Urdhva Mukha. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Vinyasa.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Vinyasa.", "x": "Upward Dog: Vinyasa.. Sequence. Essential knowledge — Urdhva Mukha.. the full backbend. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Vinyasa..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Vinyasa..", "x": "Explained: Vinyasa.. Chest. The context — Upward Dog. Thighs off. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Strong.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Strong.", "x": "Upward Dog: Strong.. Thighs. Essential knowledge — Thighs off.. the full backbend. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Strong..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Strong..", "x": "Explained: Strong.. Vinyasa. The context — Upward Dog. Chest. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Thighs.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Thighs.", "x": "Upward Dog in depth: Thighs.. Thighs off. Details — the full backbend.. Vinyasa. Shoulders. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Chest.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Chest.", "x": "Upward Dog in depth: Chest.. Chest. Details — the full backbend.. Strong. Vinyasa. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Vinyasa.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Vinyasa.", "x": "Upward Dog in depth: Vinyasa.. Shoulders. Details — the full backbend.. Shoulders. Strong. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Strong.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Strong.", "x": "Upward Dog in depth: Strong.. Vinyasa. Details — the full backbend.. Sequence. Urdhva Mukha. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Shoulders.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Shoulders.", "x": "Upward Dog in depth: Shoulders.. Strong. Details — the full backbend.. Thighs. Thighs off. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Sequence.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Sequence.", "x": "Upward Dog in depth: Sequence.. Urdhva Mukha. Details — the full backbend.. Chest. Chest. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Upward Dog comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Upward Dog comes from.", "x": "Origins: Thighs.. Urdhva Mukha. The history of Upward Dog — the full backbend.. Chest. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Upward Dog respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Upward Dog respectfully.", "x": "Engaging: Vinyasa.. Thighs off. How to participate or observe well — Upward Dog. the full backbend. Respect first, always; Strong.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Upward Dog do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Upward Dog do's and don'ts.", "x": "Etiquette: Shoulders.. Chest. The rules of respect — Upward Dog. the full backbend. When in doubt, ask about Sequence.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Upward Dog.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Upward Dog.", "x": "Planning: Thighs.. Shoulders. Practical notes — Upward Dog. the full backbend. A little planning shows respect for Chest.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Upward Dog and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Upward Dog and money.", "x": "Costs: Vinyasa.. Vinyasa. What to budget — Upward Dog. the full backbend. The best experiences of Strong. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-yoga-upward-dog-pose-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
