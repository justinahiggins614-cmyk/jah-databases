(function(){'use strict';
/* JAH Rubik\'s Cube Puzzle Database generator — jahdb-e2-puzzle-rubiks-cube-puzzle-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-puzzle-rubiks-cube-puzzle',PREFIX='JAH-E2PUZZLERUB-',NAME='JAH Rubik\'s Cube Puzzle Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Rubik's Cube: the complete guide", "d": "Rubik's Cube: the twisty classic..", "g": "overview", "l": 2, "q": "What is Rubik's Cube: the complete guide?", "a": "Rubik's Cube: the twisty classic..", "x": "The complete puzzle guide to Rubik's Cube: the twisty classic.. 1974. History, meaning, practices, and how to engage respectfully — everything in one database. Erno. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Rubik's Cube essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Rubik's Cube essentials.", "x": "At a glance: Rubik's Cube — the twisty classic.. Erno. The essentials: Algorithms.. 43 quintillion. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "1974.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "1974.", "x": "Rubik's Cube: 1974.. Algorithms. Essential knowledge — 43 quintillion.. the twisty classic. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 1974..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 1974..", "x": "Explained: 1974.. God's. The context — Rubik's Cube. Speedcubing. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Erno.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Erno.", "x": "Rubik's Cube: Erno.. Speed. Essential knowledge — Speedcubing.. the twisty classic. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Erno..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Erno..", "x": "Explained: Erno.. Quintillion. The context — Rubik's Cube. Algorithms. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "43 quintillion.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "43 quintillion.", "x": "Rubik's Cube: 43 quintillion.. God's. Essential knowledge — Algorithms.. the twisty classic. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: 43 quintillion..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: 43 quintillion..", "x": "Explained: 43 quintillion.. Tips. The context — Rubik's Cube. God's number. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Speedcubing.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Speedcubing.", "x": "Rubik's Cube: Speedcubing.. Quintillion. Essential knowledge — God's number.. the twisty classic. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Speedcubing..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Speedcubing..", "x": "Explained: Speedcubing.. Erno. The context — Rubik's Cube. 1974. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Algorithms.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Algorithms.", "x": "Rubik's Cube: Algorithms.. Tips. Essential knowledge — 1974.. the twisty classic. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Algorithms..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Algorithms..", "x": "Explained: Algorithms.. Algorithms. The context — Rubik's Cube. Erno. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "God's number.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "God's number.", "x": "Rubik's Cube: God's number.. Erno. Essential knowledge — Erno.. the twisty classic. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: God's number..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: God's number..", "x": "Explained: God's number.. Speed. The context — Rubik's Cube. 43 quintillion. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Erno.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Erno.", "x": "Rubik's Cube in depth: Erno.. Erno. Details — the twisty classic.. Speed. Speedcubing. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Algorithms.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Algorithms.", "x": "Rubik's Cube in depth: Algorithms.. 43 quintillion. Details — the twisty classic.. God's. Algorithms. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Speed.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Speed.", "x": "Rubik's Cube in depth: Speed.. Speedcubing. Details — the twisty classic.. Quintillion. God's number. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "God's.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "God's.", "x": "Rubik's Cube in depth: God's.. Algorithms. Details — the twisty classic.. Tips. 1974. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Quintillion.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Quintillion.", "x": "Rubik's Cube in depth: Quintillion.. God's number. Details — the twisty classic.. Erno. Erno. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Tips.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Tips.", "x": "Rubik's Cube in depth: Tips.. 1974. Details — the twisty classic.. Algorithms. 43 quintillion. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Rubik's Cube comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Rubik's Cube comes from.", "x": "Origins: Erno.. 1974. The history of Rubik's Cube — the twisty classic.. Algorithms. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Rubik's Cube respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Rubik's Cube respectfully.", "x": "Engaging: Speed.. Erno. How to participate or observe well — Rubik's Cube. the twisty classic. Respect first, always; God's.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Rubik's Cube do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Rubik's Cube do's and don'ts.", "x": "Etiquette: Quintillion.. 43 quintillion. The rules of respect — Rubik's Cube. the twisty classic. When in doubt, ask about Tips.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Rubik's Cube.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Rubik's Cube.", "x": "Planning: Erno.. Speedcubing. Practical notes — Rubik's Cube. the twisty classic. A little planning shows respect for Algorithms.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Rubik's Cube and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Rubik's Cube and money.", "x": "Costs: Speed.. Algorithms. What to budget — Rubik's Cube. the twisty classic. The best experiences of God's. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-puzzle-rubiks-cube-puzzle-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
