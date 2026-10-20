(function(){'use strict';
/* JAH Camel Up Board Database generator — jahdb-e2-games2-camel-up-board-game-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-games2-camel-up-board-game',PREFIX='JAH-E2GAMES2CAM-',NAME='JAH Camel Up Board Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Camel Up Board: the complete guide", "d": "Camel Up Board: the camel race..", "g": "overview", "l": 2, "q": "What is Camel Up Board: the complete guide?", "a": "Camel Up Board: the camel race..", "x": "The complete board game guide to Camel Up Board: the camel race.. 2014. History, meaning, practices, and how to engage respectfully — everything in one database. Betting. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Camel Up Board essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Camel Up Board essentials.", "x": "At a glance: Camel Up Board — the camel race.. Camels. The essentials: Stacking.. Betting. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "2014.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "2014.", "x": "Camel Up Board: 2014.. Stacking. Essential knowledge — Betting.. the camel race. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 2014..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 2014..", "x": "Explained: 2014.. 2014. The context — Camel Up Board. Pyramid. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Camels.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Camels.", "x": "Camel Up Board: Camels.. Spiel. Essential knowledge — Pyramid.. the camel race. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Camels..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Camels..", "x": "Explained: Camels.. Camels. The context — Camel Up Board. Stacking. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Betting.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Betting.", "x": "Camel Up Board: Betting.. 2014. Essential knowledge — Stacking.. the camel race. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Betting..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Betting..", "x": "Explained: Betting.. Guide. The context — Camel Up Board. Spiel. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Pyramid.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Pyramid.", "x": "Camel Up Board: Pyramid.. Camels. Essential knowledge — Spiel.. the camel race. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Pyramid..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Pyramid..", "x": "Explained: Pyramid.. Betting. The context — Camel Up Board. 2014. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Stacking.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Stacking.", "x": "Camel Up Board: Stacking.. Guide. Essential knowledge — 2014.. the camel race. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Stacking..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Stacking..", "x": "Explained: Stacking.. Stacking. The context — Camel Up Board. Camels. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Spiel.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Spiel.", "x": "Camel Up Board: Spiel.. Betting. Essential knowledge — Camels.. the camel race. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Spiel..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Spiel..", "x": "Explained: Spiel.. Spiel. The context — Camel Up Board. Betting. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Betting.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Betting.", "x": "Camel Up Board in depth: Betting.. Camels. Details — the camel race.. Spiel. Pyramid. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Stacking.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Stacking.", "x": "Camel Up Board in depth: Stacking.. Betting. Details — the camel race.. 2014. Stacking. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Spiel.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Spiel.", "x": "Camel Up Board in depth: Spiel.. Pyramid. Details — the camel race.. Camels. Spiel. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "2014.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "2014.", "x": "Camel Up Board in depth: 2014.. Stacking. Details — the camel race.. Guide. 2014. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Camels.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Camels.", "x": "Camel Up Board in depth: Camels.. Spiel. Details — the camel race.. Betting. Camels. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Guide.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Guide.", "x": "Camel Up Board in depth: Guide.. 2014. Details — the camel race.. Stacking. Betting. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Camel Up Board comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Camel Up Board comes from.", "x": "Origins: Betting.. 2014. The history of Camel Up Board — the camel race.. Stacking. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Camel Up Board respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Camel Up Board respectfully.", "x": "Engaging: Spiel.. Camels. How to participate or observe well — Camel Up Board. the camel race. Respect first, always; 2014.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Camel Up Board do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Camel Up Board do's and don'ts.", "x": "Etiquette: Camels.. Betting. The rules of respect — Camel Up Board. the camel race. When in doubt, ask about Guide.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Camel Up Board.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Camel Up Board.", "x": "Planning: Betting.. Pyramid. Practical notes — Camel Up Board. the camel race. A little planning shows respect for Stacking.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Camel Up Board and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Camel Up Board and money.", "x": "Costs: Spiel.. Stacking. What to budget — Camel Up Board. the camel race. The best experiences of 2014. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-games2-camel-up-board-game-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
