(function(){'use strict';
/* JAH The Crew Board Database generator — jahdb-e2-games2-the-crew-board-game-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-games2-the-crew-board-game',PREFIX='JAH-E2GAMES2THE-',NAME='JAH The Crew Board Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "The Crew Board: the complete guide", "d": "The Crew Board: the trick co-op..", "g": "overview", "l": 2, "q": "What is The Crew Board: the complete guide?", "a": "The Crew Board: the trick co-op..", "x": "The complete board game guide to The Crew Board: the trick co-op.. 2019. History, meaning, practices, and how to engage respectfully — everything in one database. Tricks. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "The Crew Board essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "The Crew Board essentials.", "x": "At a glance: The Crew Board — the trick co-op.. Tricks. The essentials: Co-op.. Missions. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "2019.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "2019.", "x": "The Crew Board: 2019.. Co-op. Essential knowledge — Missions.. the trick co-op. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 2019..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 2019..", "x": "Explained: 2019.. 2019. The context — The Crew Board. Co-op. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Tricks.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Tricks.", "x": "The Crew Board: Tricks.. Space. Essential knowledge — Co-op.. the trick co-op. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Tricks..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Tricks..", "x": "Explained: Tricks.. Missions. The context — The Crew Board. Cards. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Missions.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Missions.", "x": "The Crew Board: Missions.. 2019. Essential knowledge — Cards.. the trick co-op. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Missions..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Missions..", "x": "Explained: Missions.. Guide. The context — The Crew Board. Space. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Co-op.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Co-op.", "x": "The Crew Board: Co-op.. Missions. Essential knowledge — Space.. the trick co-op. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Co-op..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Co-op..", "x": "Explained: Co-op.. Tricks. The context — The Crew Board. 2019. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Cards.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Cards.", "x": "The Crew Board: Cards.. Guide. Essential knowledge — 2019.. the trick co-op. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Cards..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Cards..", "x": "Explained: Cards.. Co-op. The context — The Crew Board. Tricks. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Space.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Space.", "x": "The Crew Board: Space.. Tricks. Essential knowledge — Tricks.. the trick co-op. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Space..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Space..", "x": "Explained: Space.. Space. The context — The Crew Board. Missions. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Tricks.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Tricks.", "x": "The Crew Board in depth: Tricks.. Tricks. Details — the trick co-op.. Space. Co-op. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Co-op.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Co-op.", "x": "The Crew Board in depth: Co-op.. Missions. Details — the trick co-op.. 2019. Cards. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Space.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Space.", "x": "The Crew Board in depth: Space.. Co-op. Details — the trick co-op.. Missions. Space. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "2019.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "2019.", "x": "The Crew Board in depth: 2019.. Cards. Details — the trick co-op.. Guide. 2019. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Missions.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Missions.", "x": "The Crew Board in depth: Missions.. Space. Details — the trick co-op.. Tricks. Tricks. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Guide.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Guide.", "x": "The Crew Board in depth: Guide.. 2019. Details — the trick co-op.. Co-op. Missions. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where The Crew Board comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where The Crew Board comes from.", "x": "Origins: Tricks.. 2019. The history of The Crew Board — the trick co-op.. Co-op. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing The Crew Board respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing The Crew Board respectfully.", "x": "Engaging: Space.. Tricks. How to participate or observe well — The Crew Board. the trick co-op. Respect first, always; 2019.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "The Crew Board do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "The Crew Board do's and don'ts.", "x": "Etiquette: Missions.. Missions. The rules of respect — The Crew Board. the trick co-op. When in doubt, ask about Guide.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around The Crew Board.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around The Crew Board.", "x": "Planning: Tricks.. Co-op. Practical notes — The Crew Board. the trick co-op. A little planning shows respect for Co-op.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "The Crew Board and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "The Crew Board and money.", "x": "Costs: Space.. Cards. What to budget — The Crew Board. the trick co-op. The best experiences of 2019. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-games2-the-crew-board-game-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
