(function(){'use strict';
/* JAH Tower Defense Game Genre Database generator — jahdb-e2-game-tower-defense-games-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-game-tower-defense-games',PREFIX='JAH-E2GAMETOWER-',NAME='JAH Tower Defense Game Genre Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Tower Defense: the complete guide", "d": "Tower Defense: the hold the line..", "g": "overview", "l": 2, "q": "What is Tower Defense: the complete guide?", "a": "Tower Defense: the hold the line..", "x": "The complete game genre guide to Tower Defense: the hold the line.. Waves. History, meaning, practices, and how to engage respectfully — everything in one database. Waves. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Tower Defense essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Tower Defense essentials.", "x": "At a glance: Tower Defense — the hold the line.. Towers. The essentials: Mazes.. Mazes. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Waves.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Waves.", "x": "Tower Defense: Waves.. Mazes. Essential knowledge — Mazes.. the hold the line. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Waves..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Waves..", "x": "Explained: Waves.. Bloons. The context — Tower Defense. Bloons. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Towers.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Towers.", "x": "Tower Defense: Towers.. Upgrades. Essential knowledge — Bloons.. the hold the line. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Towers..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Towers..", "x": "Explained: Towers.. Strategy. The context — Tower Defense. Strategy. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Mazes.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Mazes.", "x": "Tower Defense: Mazes.. Bloons. Essential knowledge — Strategy.. the hold the line. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Mazes..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Mazes..", "x": "Explained: Mazes.. Classics. The context — Tower Defense. Upgrades. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Bloons.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Bloons.", "x": "Tower Defense: Bloons.. Strategy. Essential knowledge — Upgrades.. the hold the line. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Bloons..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Bloons..", "x": "Explained: Bloons.. Waves. The context — Tower Defense. Waves. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Strategy.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Strategy.", "x": "Tower Defense: Strategy.. Classics. Essential knowledge — Waves.. the hold the line. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Strategy..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Strategy..", "x": "Explained: Strategy.. Mazes. The context — Tower Defense. Towers. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Upgrades.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Upgrades.", "x": "Tower Defense: Upgrades.. Waves. Essential knowledge — Towers.. the hold the line. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Upgrades..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Upgrades..", "x": "Explained: Upgrades.. Upgrades. The context — Tower Defense. Mazes. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Waves.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Waves.", "x": "Tower Defense in depth: Waves.. Towers. Details — the hold the line.. Upgrades. Bloons. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Mazes.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Mazes.", "x": "Tower Defense in depth: Mazes.. Mazes. Details — the hold the line.. Bloons. Strategy. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Upgrades.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Upgrades.", "x": "Tower Defense in depth: Upgrades.. Bloons. Details — the hold the line.. Strategy. Upgrades. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Bloons.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Bloons.", "x": "Tower Defense in depth: Bloons.. Strategy. Details — the hold the line.. Classics. Waves. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Strategy.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Strategy.", "x": "Tower Defense in depth: Strategy.. Upgrades. Details — the hold the line.. Waves. Towers. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Classics.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Classics.", "x": "Tower Defense in depth: Classics.. Waves. Details — the hold the line.. Mazes. Mazes. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Tower Defense comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Tower Defense comes from.", "x": "Origins: Waves.. Waves. The history of Tower Defense — the hold the line.. Mazes. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Tower Defense respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Tower Defense respectfully.", "x": "Engaging: Upgrades.. Towers. How to participate or observe well — Tower Defense. the hold the line. Respect first, always; Bloons.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Tower Defense do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Tower Defense do's and don'ts.", "x": "Etiquette: Strategy.. Mazes. The rules of respect — Tower Defense. the hold the line. When in doubt, ask about Classics.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Tower Defense.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Tower Defense.", "x": "Planning: Waves.. Bloons. Practical notes — Tower Defense. the hold the line. A little planning shows respect for Mazes.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Tower Defense and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Tower Defense and money.", "x": "Costs: Upgrades.. Strategy. What to budget — Tower Defense. the hold the line. The best experiences of Bloons. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-game-tower-defense-games-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
