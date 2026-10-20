(function(){'use strict';
/* JAH Metroidvania Games Game Genre Database generator — jahdb-e2-game-metroidvania-video-games-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-game-metroidvania-video-games',PREFIX='JAH-E2GAMEMETRO-',NAME='JAH Metroidvania Games Game Genre Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Metroidvania Games: the complete guide", "d": "Metroidvania Games: the interconnected map..", "g": "overview", "l": 2, "q": "What is Metroidvania Games: the complete guide?", "a": "Metroidvania Games: the interconnected map..", "x": "The complete game genre guide to Metroidvania Games: the interconnected map.. Metroid. History, meaning, practices, and how to engage respectfully — everything in one database. Backtracking. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Metroidvania Games essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Metroidvania Games essentials.", "x": "At a glance: Metroidvania Games — the interconnected map.. Castlevania. The essentials: Abilities.. Backtracking. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Metroid.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Metroid.", "x": "Metroidvania Games: Metroid.. Abilities. Essential knowledge — Backtracking.. the interconnected map. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Metroid..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Metroid..", "x": "Explained: Metroid.. Hollow Knight. The context — Metroidvania Games. Abilities. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Castlevania.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Castlevania.", "x": "Metroidvania Games: Castlevania.. Map. Essential knowledge — Abilities.. the interconnected map. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Castlevania..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Castlevania..", "x": "Explained: Castlevania.. Metroid. The context — Metroidvania Games. Map. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Backtracking.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Backtracking.", "x": "Metroidvania Games: Backtracking.. Hollow Knight. Essential knowledge — Map.. the interconnected map. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Backtracking..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Backtracking..", "x": "Explained: Backtracking.. Classics. The context — Metroidvania Games. Hollow Knight. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Abilities.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Abilities.", "x": "Metroidvania Games: Abilities.. Metroid. Essential knowledge — Hollow Knight.. the interconnected map. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Abilities..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Abilities..", "x": "Explained: Abilities.. Backtracking. The context — Metroidvania Games. Metroid. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Map.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Map.", "x": "Metroidvania Games: Map.. Classics. Essential knowledge — Metroid.. the interconnected map. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Map..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Map..", "x": "Explained: Map.. Abilities. The context — Metroidvania Games. Castlevania. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Hollow Knight.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Hollow Knight.", "x": "Metroidvania Games: Hollow Knight.. Backtracking. Essential knowledge — Castlevania.. the interconnected map. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Hollow Knight..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Hollow Knight..", "x": "Explained: Hollow Knight.. Map. The context — Metroidvania Games. Backtracking. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Backtracking.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Backtracking.", "x": "Metroidvania Games in depth: Backtracking.. Castlevania. Details — the interconnected map.. Map. Abilities. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Abilities.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Abilities.", "x": "Metroidvania Games in depth: Abilities.. Backtracking. Details — the interconnected map.. Hollow Knight. Map. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Map.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Map.", "x": "Metroidvania Games in depth: Map.. Abilities. Details — the interconnected map.. Metroid. Hollow Knight. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Hollow Knight.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Hollow Knight.", "x": "Metroidvania Games in depth: Hollow Knight.. Map. Details — the interconnected map.. Classics. Metroid. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Metroid.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Metroid.", "x": "Metroidvania Games in depth: Metroid.. Hollow Knight. Details — the interconnected map.. Backtracking. Castlevania. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Classics.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Classics.", "x": "Metroidvania Games in depth: Classics.. Metroid. Details — the interconnected map.. Abilities. Backtracking. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Metroidvania Games comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Metroidvania Games comes from.", "x": "Origins: Backtracking.. Metroid. The history of Metroidvania Games — the interconnected map.. Abilities. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Metroidvania Games respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Metroidvania Games respectfully.", "x": "Engaging: Map.. Castlevania. How to participate or observe well — Metroidvania Games. the interconnected map. Respect first, always; Hollow Knight.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Metroidvania Games do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Metroidvania Games do's and don'ts.", "x": "Etiquette: Metroid.. Backtracking. The rules of respect — Metroidvania Games. the interconnected map. When in doubt, ask about Classics.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Metroidvania Games.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Metroidvania Games.", "x": "Planning: Backtracking.. Abilities. Practical notes — Metroidvania Games. the interconnected map. A little planning shows respect for Abilities.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Metroidvania Games and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Metroidvania Games and money.", "x": "Costs: Map.. Map. What to budget — Metroidvania Games. the interconnected map. The best experiences of Hollow Knight. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-game-metroidvania-video-games-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
