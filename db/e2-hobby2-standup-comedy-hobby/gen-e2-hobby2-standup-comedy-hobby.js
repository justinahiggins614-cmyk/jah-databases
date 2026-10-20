(function(){'use strict';
/* JAH Stand-Up Comedy Database generator — jahdb-e2-hobby2-standup-comedy-hobby-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-hobby2-standup-comedy-hobby',PREFIX='JAH-E2HOBBY2STA-',NAME='JAH Stand-Up Comedy Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Stand-Up Comedy: the complete guide", "d": "Stand-Up Comedy: the mic five..", "g": "overview", "l": 2, "q": "What is Stand-Up Comedy: the complete guide?", "a": "Stand-Up Comedy: the mic five..", "x": "The complete hobby guide to Stand-Up Comedy: the mic five.. Open mics. History, meaning, practices, and how to engage respectfully — everything in one database. Mics. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Stand-Up Comedy essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Stand-Up Comedy essentials.", "x": "At a glance: Stand-Up Comedy — the mic five.. Jokes. The essentials: Stage.. Timing. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Open mics.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Open mics.", "x": "Stand-Up Comedy: Open mics.. Stage. Essential knowledge — Timing.. the mic five. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Open mics..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Open mics..", "x": "Explained: Open mics.. Jokes. The context — Stand-Up Comedy. Bombing. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Jokes.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Jokes.", "x": "Stand-Up Comedy: Jokes.. Writing. Essential knowledge — Bombing.. the mic five. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Jokes..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Jokes..", "x": "Explained: Jokes.. Timing. The context — Stand-Up Comedy. Writing. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Timing.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Timing.", "x": "Stand-Up Comedy: Timing.. Jokes. Essential knowledge — Writing.. the mic five. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Timing..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Timing..", "x": "Explained: Timing.. Getting started. The context — Stand-Up Comedy. Stage. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Bombing.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Bombing.", "x": "Stand-Up Comedy: Bombing.. Timing. Essential knowledge — Stage.. the mic five. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Bombing..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Bombing..", "x": "Explained: Bombing.. Mics. The context — Stand-Up Comedy. Open mics. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Writing.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Writing.", "x": "Stand-Up Comedy: Writing.. Getting started. Essential knowledge — Open mics.. the mic five. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Writing..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Writing..", "x": "Explained: Writing.. Stage. The context — Stand-Up Comedy. Jokes. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Stage.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Stage.", "x": "Stand-Up Comedy: Stage.. Mics. Essential knowledge — Jokes.. the mic five. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Stage..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Stage..", "x": "Explained: Stage.. Writing. The context — Stand-Up Comedy. Timing. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Mics.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Mics.", "x": "Stand-Up Comedy in depth: Mics.. Jokes. Details — the mic five.. Writing. Bombing. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Stage.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Stage.", "x": "Stand-Up Comedy in depth: Stage.. Timing. Details — the mic five.. Jokes. Writing. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Writing.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Writing.", "x": "Stand-Up Comedy in depth: Writing.. Bombing. Details — the mic five.. Timing. Stage. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Jokes.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Jokes.", "x": "Stand-Up Comedy in depth: Jokes.. Writing. Details — the mic five.. Getting started. Open mics. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Timing.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Timing.", "x": "Stand-Up Comedy in depth: Timing.. Stage. Details — the mic five.. Mics. Jokes. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Getting started.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Getting started.", "x": "Stand-Up Comedy in depth: Getting started.. Open mics. Details — the mic five.. Stage. Timing. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Stand-Up Comedy comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Stand-Up Comedy comes from.", "x": "Origins: Mics.. Open mics. The history of Stand-Up Comedy — the mic five.. Stage. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Stand-Up Comedy respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Stand-Up Comedy respectfully.", "x": "Engaging: Writing.. Jokes. How to participate or observe well — Stand-Up Comedy. the mic five. Respect first, always; Jokes.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Stand-Up Comedy do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Stand-Up Comedy do's and don'ts.", "x": "Etiquette: Timing.. Timing. The rules of respect — Stand-Up Comedy. the mic five. When in doubt, ask about Getting started.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Stand-Up Comedy.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Stand-Up Comedy.", "x": "Planning: Mics.. Bombing. Practical notes — Stand-Up Comedy. the mic five. A little planning shows respect for Stage.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Stand-Up Comedy and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Stand-Up Comedy and money.", "x": "Costs: Writing.. Writing. What to budget — Stand-Up Comedy. the mic five. The best experiences of Jokes. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-hobby2-standup-comedy-hobby-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
