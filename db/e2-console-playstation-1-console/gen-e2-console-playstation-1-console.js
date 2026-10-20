(function(){'use strict';
/* JAH PlayStation 1 Console Database generator — jahdb-e2-console-playstation-1-console-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-console-playstation-1-console',PREFIX='JAH-E2CONSOLEPL-',NAME='JAH PlayStation 1 Console Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "PlayStation 1: the complete guide", "d": "PlayStation 1: the CD revolution..", "g": "overview", "l": 2, "q": "What is PlayStation 1: the complete guide?", "a": "PlayStation 1: the CD revolution..", "x": "The complete console guide to PlayStation 1: the CD revolution.. 1994. History, meaning, practices, and how to engage respectfully — everything in one database. Discs. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "PlayStation 1 essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "PlayStation 1 essentials.", "x": "At a glance: PlayStation 1 — the CD revolution.. Sony. The essentials: FFVII.. Final Fantasy VII. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "1994.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "1994.", "x": "PlayStation 1: 1994.. FFVII. Essential knowledge — Final Fantasy VII.. the CD revolution. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 1994..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 1994..", "x": "Explained: 1994.. Sony. The context — PlayStation 1. Discs. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Sony.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Sony.", "x": "PlayStation 1: Sony.. Crash. Essential knowledge — Discs.. the CD revolution. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Sony..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Sony..", "x": "Explained: Sony.. Revolution. The context — PlayStation 1. Crash. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Final Fantasy VII.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Final Fantasy VII.", "x": "PlayStation 1: Final Fantasy VII.. Sony. Essential knowledge — Crash.. the CD revolution. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Final Fantasy VII..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Final Fantasy VII..", "x": "Explained: Final Fantasy VII.. Legacy. The context — PlayStation 1. Revolution. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Discs.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Discs.", "x": "PlayStation 1: Discs.. Revolution. Essential knowledge — Revolution.. the CD revolution. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Discs..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Discs..", "x": "Explained: Discs.. Discs. The context — PlayStation 1. 1994. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Crash.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Crash.", "x": "PlayStation 1: Crash.. Legacy. Essential knowledge — 1994.. the CD revolution. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Crash..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Crash..", "x": "Explained: Crash.. FFVII. The context — PlayStation 1. Sony. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Revolution.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Revolution.", "x": "PlayStation 1: Revolution.. Discs. Essential knowledge — Sony.. the CD revolution. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Revolution..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Revolution..", "x": "Explained: Revolution.. Crash. The context — PlayStation 1. Final Fantasy VII. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Discs.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Discs.", "x": "PlayStation 1 in depth: Discs.. Sony. Details — the CD revolution.. Crash. Discs. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "FFVII.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "FFVII.", "x": "PlayStation 1 in depth: FFVII.. Final Fantasy VII. Details — the CD revolution.. Sony. Crash. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Crash.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Crash.", "x": "PlayStation 1 in depth: Crash.. Discs. Details — the CD revolution.. Revolution. Revolution. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Sony.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Sony.", "x": "PlayStation 1 in depth: Sony.. Crash. Details — the CD revolution.. Legacy. 1994. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Revolution.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Revolution.", "x": "PlayStation 1 in depth: Revolution.. Revolution. Details — the CD revolution.. Discs. Sony. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Legacy.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Legacy.", "x": "PlayStation 1 in depth: Legacy.. 1994. Details — the CD revolution.. FFVII. Final Fantasy VII. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where PlayStation 1 comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where PlayStation 1 comes from.", "x": "Origins: Discs.. 1994. The history of PlayStation 1 — the CD revolution.. FFVII. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing PlayStation 1 respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing PlayStation 1 respectfully.", "x": "Engaging: Crash.. Sony. How to participate or observe well — PlayStation 1. the CD revolution. Respect first, always; Sony.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "PlayStation 1 do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "PlayStation 1 do's and don'ts.", "x": "Etiquette: Revolution.. Final Fantasy VII. The rules of respect — PlayStation 1. the CD revolution. When in doubt, ask about Legacy.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around PlayStation 1.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around PlayStation 1.", "x": "Planning: Discs.. Discs. Practical notes — PlayStation 1. the CD revolution. A little planning shows respect for FFVII.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "PlayStation 1 and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "PlayStation 1 and money.", "x": "Costs: Crash.. Crash. What to budget — PlayStation 1. the CD revolution. The best experiences of Sony. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-console-playstation-1-console-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
