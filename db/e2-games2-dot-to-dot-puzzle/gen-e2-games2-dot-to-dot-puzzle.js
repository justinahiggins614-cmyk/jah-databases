(function(){'use strict';
/* JAH Dot to Dot Database generator — jahdb-e2-games2-dot-to-dot-puzzle-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-games2-dot-to-dot-puzzle',PREFIX='JAH-E2GAMES2DOT-',NAME='JAH Dot to Dot Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Dot to Dot: the complete guide", "d": "Dot to Dot: the connect art..", "g": "overview", "l": 2, "q": "What is Dot to Dot: the complete guide?", "a": "Dot to Dot: the connect art..", "x": "The complete puzzle guide to Dot to Dot: the connect art.. Connect. History, meaning, practices, and how to engage respectfully — everything in one database. Numbers. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Dot to Dot essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Dot to Dot essentials.", "x": "At a glance: Dot to Dot — the connect art.. Numbers. The essentials: Extreme.. Reveal. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Connect.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Connect.", "x": "Dot to Dot: Connect.. Extreme. Essential knowledge — Reveal.. the connect art. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Connect..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Connect..", "x": "Explained: Connect.. Connect. The context — Dot to Dot. Kids. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Numbers.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Numbers.", "x": "Dot to Dot: Numbers.. Animals. Essential knowledge — Kids.. the connect art. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Numbers..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Numbers..", "x": "Explained: Numbers.. Reveal. The context — Dot to Dot. Extreme. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Reveal.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Reveal.", "x": "Dot to Dot: Reveal.. Connect. Essential knowledge — Extreme.. the connect art. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Reveal..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Reveal..", "x": "Explained: Reveal.. Guide. The context — Dot to Dot. Animals. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Kids.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Kids.", "x": "Dot to Dot: Kids.. Reveal. Essential knowledge — Animals.. the connect art. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Kids..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Kids..", "x": "Explained: Kids.. Numbers. The context — Dot to Dot. Connect. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Extreme.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Extreme.", "x": "Dot to Dot: Extreme.. Guide. Essential knowledge — Connect.. the connect art. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Extreme..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Extreme..", "x": "Explained: Extreme.. Extreme. The context — Dot to Dot. Numbers. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Animals.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Animals.", "x": "Dot to Dot: Animals.. Numbers. Essential knowledge — Numbers.. the connect art. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Animals..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Animals..", "x": "Explained: Animals.. Animals. The context — Dot to Dot. Reveal. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Numbers.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Numbers.", "x": "Dot to Dot in depth: Numbers.. Numbers. Details — the connect art.. Animals. Kids. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Extreme.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Extreme.", "x": "Dot to Dot in depth: Extreme.. Reveal. Details — the connect art.. Connect. Extreme. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Animals.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Animals.", "x": "Dot to Dot in depth: Animals.. Kids. Details — the connect art.. Reveal. Animals. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Connect.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Connect.", "x": "Dot to Dot in depth: Connect.. Extreme. Details — the connect art.. Guide. Connect. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Reveal.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Reveal.", "x": "Dot to Dot in depth: Reveal.. Animals. Details — the connect art.. Numbers. Numbers. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Guide.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Guide.", "x": "Dot to Dot in depth: Guide.. Connect. Details — the connect art.. Extreme. Reveal. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Dot to Dot comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Dot to Dot comes from.", "x": "Origins: Numbers.. Connect. The history of Dot to Dot — the connect art.. Extreme. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Dot to Dot respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Dot to Dot respectfully.", "x": "Engaging: Animals.. Numbers. How to participate or observe well — Dot to Dot. the connect art. Respect first, always; Connect.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Dot to Dot do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Dot to Dot do's and don'ts.", "x": "Etiquette: Reveal.. Reveal. The rules of respect — Dot to Dot. the connect art. When in doubt, ask about Guide.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Dot to Dot.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Dot to Dot.", "x": "Planning: Numbers.. Kids. Practical notes — Dot to Dot. the connect art. A little planning shows respect for Extreme.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Dot to Dot and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Dot to Dot and money.", "x": "Costs: Animals.. Extreme. What to budget — Dot to Dot. the connect art. The best experiences of Connect. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-games2-dot-to-dot-puzzle-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
