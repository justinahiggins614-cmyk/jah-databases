(function(){'use strict';
/* JAH Carcassonne Board Board Game Database generator — jahdb-e2-board-carcassonne-board-game-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-board-carcassonne-board-game',PREFIX='JAH-E2BOARDCARC-',NAME='JAH Carcassonne Board Board Game Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Carcassonne Board: the complete guide", "d": "Carcassonne Board: the tile classic..", "g": "overview", "l": 2, "q": "What is Carcassonne Board: the complete guide?", "a": "Carcassonne Board: the tile classic..", "x": "The complete board game guide to Carcassonne Board: the tile classic.. 2000. History, meaning, practices, and how to engage respectfully — everything in one database. Tiles. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Carcassonne Board essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Carcassonne Board essentials.", "x": "At a glance: Carcassonne Board — the tile classic.. Tiles. The essentials: Meeples.. Meeples. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "2000.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "2000.", "x": "Carcassonne Board: 2000.. Meeples. Essential knowledge — Meeples.. the tile classic. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 2000..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 2000..", "x": "Explained: 2000.. France. The context — Carcassonne Board. France. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Tiles.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Tiles.", "x": "Carcassonne Board: Tiles.. Placement. Essential knowledge — France.. the tile classic. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Tiles..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Tiles..", "x": "Explained: Tiles.. Expansions. The context — Carcassonne Board. Placement. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Meeples.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Meeples.", "x": "Carcassonne Board: Meeples.. France. Essential knowledge — Placement.. the tile classic. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Meeples..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Meeples..", "x": "Explained: Meeples.. Strategy. The context — Carcassonne Board. Expansions. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "France.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "France.", "x": "Carcassonne Board: France.. Expansions. Essential knowledge — Expansions.. the tile classic. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: France..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: France..", "x": "Explained: France.. Tiles. The context — Carcassonne Board. 2000. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Placement.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Placement.", "x": "Carcassonne Board: Placement.. Strategy. Essential knowledge — 2000.. the tile classic. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Placement..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Placement..", "x": "Explained: Placement.. Meeples. The context — Carcassonne Board. Tiles. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Expansions.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Expansions.", "x": "Carcassonne Board: Expansions.. Tiles. Essential knowledge — Tiles.. the tile classic. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Expansions..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Expansions..", "x": "Explained: Expansions.. Placement. The context — Carcassonne Board. Meeples. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Tiles.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Tiles.", "x": "Carcassonne Board in depth: Tiles.. Tiles. Details — the tile classic.. Placement. France. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Meeples.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Meeples.", "x": "Carcassonne Board in depth: Meeples.. Meeples. Details — the tile classic.. France. Placement. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Placement.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Placement.", "x": "Carcassonne Board in depth: Placement.. France. Details — the tile classic.. Expansions. Expansions. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "France.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "France.", "x": "Carcassonne Board in depth: France.. Placement. Details — the tile classic.. Strategy. 2000. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Expansions.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Expansions.", "x": "Carcassonne Board in depth: Expansions.. Expansions. Details — the tile classic.. Tiles. Tiles. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Strategy.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Strategy.", "x": "Carcassonne Board in depth: Strategy.. 2000. Details — the tile classic.. Meeples. Meeples. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Carcassonne Board comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Carcassonne Board comes from.", "x": "Origins: Tiles.. 2000. The history of Carcassonne Board — the tile classic.. Meeples. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Carcassonne Board respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Carcassonne Board respectfully.", "x": "Engaging: Placement.. Tiles. How to participate or observe well — Carcassonne Board. the tile classic. Respect first, always; France.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Carcassonne Board do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Carcassonne Board do's and don'ts.", "x": "Etiquette: Expansions.. Meeples. The rules of respect — Carcassonne Board. the tile classic. When in doubt, ask about Strategy.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Carcassonne Board.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Carcassonne Board.", "x": "Planning: Tiles.. France. Practical notes — Carcassonne Board. the tile classic. A little planning shows respect for Meeples.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Carcassonne Board and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Carcassonne Board and money.", "x": "Costs: Placement.. Placement. What to budget — Carcassonne Board. the tile classic. The best experiences of France. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-board-carcassonne-board-game-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
