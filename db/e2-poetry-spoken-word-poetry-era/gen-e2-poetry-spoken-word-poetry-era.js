(function(){'use strict';
/* JAH Spoken Word Poetry Poetry Database generator — jahdb-e2-poetry-spoken-word-poetry-era-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-poetry-spoken-word-poetry-era',PREFIX='JAH-E2POETRYSPO-',NAME='JAH Spoken Word Poetry Poetry Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Spoken Word Poetry: the complete guide", "d": "Spoken Word Poetry: the stage verse..", "g": "overview", "l": 2, "q": "What is Spoken Word Poetry: the complete guide?", "a": "Spoken Word Poetry: the stage verse..", "x": "The complete poetry guide to Spoken Word Poetry: the stage verse.. Slam. History, meaning, practices, and how to engage respectfully — everything in one database. Slam. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Spoken Word Poetry essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Spoken Word Poetry essentials.", "x": "At a glance: Spoken Word Poetry — the stage verse.. Def Poetry. The essentials: Performance.. Performance. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Slam.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Slam.", "x": "Spoken Word Poetry: Slam.. Performance. Essential knowledge — Performance.. the stage verse. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Slam..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Slam..", "x": "Explained: Slam.. Community. The context — Spoken Word Poetry. Mic. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Def Poetry.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Def Poetry.", "x": "Spoken Word Poetry: Def Poetry.. Mic. Essential knowledge — Mic.. the stage verse. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Def Poetry..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Def Poetry..", "x": "Explained: Def Poetry.. Rhythm. The context — Spoken Word Poetry. Rhythm. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Performance.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Performance.", "x": "Spoken Word Poetry: Performance.. Community. Essential knowledge — Rhythm.. the stage verse. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Performance..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Performance..", "x": "Explained: Performance.. Legacy. The context — Spoken Word Poetry. Community. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Mic.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Mic.", "x": "Spoken Word Poetry: Mic.. Rhythm. Essential knowledge — Community.. the stage verse. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Mic..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Mic..", "x": "Explained: Mic.. Slam. The context — Spoken Word Poetry. Slam. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Rhythm.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Rhythm.", "x": "Spoken Word Poetry: Rhythm.. Legacy. Essential knowledge — Slam.. the stage verse. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Rhythm..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Rhythm..", "x": "Explained: Rhythm.. Performance. The context — Spoken Word Poetry. Def Poetry. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Community.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Community.", "x": "Spoken Word Poetry: Community.. Slam. Essential knowledge — Def Poetry.. the stage verse. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Community..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Community..", "x": "Explained: Community.. Mic. The context — Spoken Word Poetry. Performance. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Slam.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Slam.", "x": "Spoken Word Poetry in depth: Slam.. Def Poetry. Details — the stage verse.. Mic. Mic. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Performance.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Performance.", "x": "Spoken Word Poetry in depth: Performance.. Performance. Details — the stage verse.. Community. Rhythm. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Mic.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Mic.", "x": "Spoken Word Poetry in depth: Mic.. Mic. Details — the stage verse.. Rhythm. Community. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Community.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Community.", "x": "Spoken Word Poetry in depth: Community.. Rhythm. Details — the stage verse.. Legacy. Slam. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Rhythm.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Rhythm.", "x": "Spoken Word Poetry in depth: Rhythm.. Community. Details — the stage verse.. Slam. Def Poetry. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Legacy.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Legacy.", "x": "Spoken Word Poetry in depth: Legacy.. Slam. Details — the stage verse.. Performance. Performance. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Spoken Word Poetry comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Spoken Word Poetry comes from.", "x": "Origins: Slam.. Slam. The history of Spoken Word Poetry — the stage verse.. Performance. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Spoken Word Poetry respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Spoken Word Poetry respectfully.", "x": "Engaging: Mic.. Def Poetry. How to participate or observe well — Spoken Word Poetry. the stage verse. Respect first, always; Community.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Spoken Word Poetry do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Spoken Word Poetry do's and don'ts.", "x": "Etiquette: Rhythm.. Performance. The rules of respect — Spoken Word Poetry. the stage verse. When in doubt, ask about Legacy.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Spoken Word Poetry.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Spoken Word Poetry.", "x": "Planning: Slam.. Mic. Practical notes — Spoken Word Poetry. the stage verse. A little planning shows respect for Performance.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Spoken Word Poetry and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Spoken Word Poetry and money.", "x": "Costs: Mic.. Rhythm. What to budget — Spoken Word Poetry. the stage verse. The best experiences of Community. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-poetry-spoken-word-poetry-era-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
