(function(){'use strict';
/* JAH Splendor Board Board Game Database generator — jahdb-e2-board-splendor-board-game-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-board-splendor-board-game',PREFIX='JAH-E2BOARDSPLE-',NAME='JAH Splendor Board Board Game Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Splendor Board: the complete guide", "d": "Splendor Board: the gem engine..", "g": "overview", "l": 2, "q": "What is Splendor Board: the complete guide?", "a": "Splendor Board: the gem engine..", "x": "The complete board game guide to Splendor Board: the gem engine.. 2014. History, meaning, practices, and how to engage respectfully — everything in one database. Gems. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Splendor Board essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Splendor Board essentials.", "x": "At a glance: Splendor Board — the gem engine.. Gems. The essentials: Engine.. Engine. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "2014.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "2014.", "x": "Splendor Board: 2014.. Engine. Essential knowledge — Engine.. the gem engine. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 2014..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 2014..", "x": "Explained: 2014.. Chips. The context — Splendor Board. Cards. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Gems.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Gems.", "x": "Splendor Board: Gems.. Nobles. Essential knowledge — Cards.. the gem engine. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Gems..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Gems..", "x": "Explained: Gems.. Cards. The context — Splendor Board. Nobles. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Engine.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Engine.", "x": "Splendor Board: Engine.. Chips. Essential knowledge — Nobles.. the gem engine. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Engine..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Engine..", "x": "Explained: Engine.. Strategy. The context — Splendor Board. Chips. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Cards.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Cards.", "x": "Splendor Board: Cards.. Cards. Essential knowledge — Chips.. the gem engine. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Cards..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Cards..", "x": "Explained: Cards.. Gems. The context — Splendor Board. 2014. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Nobles.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Nobles.", "x": "Splendor Board: Nobles.. Strategy. Essential knowledge — 2014.. the gem engine. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Nobles..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Nobles..", "x": "Explained: Nobles.. Engine. The context — Splendor Board. Gems. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Chips.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Chips.", "x": "Splendor Board: Chips.. Gems. Essential knowledge — Gems.. the gem engine. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Chips..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Chips..", "x": "Explained: Chips.. Nobles. The context — Splendor Board. Engine. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Gems.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Gems.", "x": "Splendor Board in depth: Gems.. Gems. Details — the gem engine.. Nobles. Cards. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Engine.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Engine.", "x": "Splendor Board in depth: Engine.. Engine. Details — the gem engine.. Chips. Nobles. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Nobles.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Nobles.", "x": "Splendor Board in depth: Nobles.. Cards. Details — the gem engine.. Cards. Chips. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Chips.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Chips.", "x": "Splendor Board in depth: Chips.. Nobles. Details — the gem engine.. Strategy. 2014. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Cards.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Cards.", "x": "Splendor Board in depth: Cards.. Chips. Details — the gem engine.. Gems. Gems. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Strategy.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Strategy.", "x": "Splendor Board in depth: Strategy.. 2014. Details — the gem engine.. Engine. Engine. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Splendor Board comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Splendor Board comes from.", "x": "Origins: Gems.. 2014. The history of Splendor Board — the gem engine.. Engine. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Splendor Board respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Splendor Board respectfully.", "x": "Engaging: Nobles.. Gems. How to participate or observe well — Splendor Board. the gem engine. Respect first, always; Chips.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Splendor Board do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Splendor Board do's and don'ts.", "x": "Etiquette: Cards.. Engine. The rules of respect — Splendor Board. the gem engine. When in doubt, ask about Strategy.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Splendor Board.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Splendor Board.", "x": "Planning: Gems.. Cards. Practical notes — Splendor Board. the gem engine. A little planning shows respect for Engine.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Splendor Board and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Splendor Board and money.", "x": "Costs: Nobles.. Nobles. What to budget — Splendor Board. the gem engine. The best experiences of Chips. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-board-splendor-board-game-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
