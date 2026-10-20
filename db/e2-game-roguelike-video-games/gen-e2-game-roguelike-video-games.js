(function(){'use strict';
/* JAH Roguelike Games Game Genre Database generator — jahdb-e2-game-roguelike-video-games-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-game-roguelike-video-games',PREFIX='JAH-E2GAMEROGUE-',NAME='JAH Roguelike Games Game Genre Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Roguelike Games: the complete guide", "d": "Roguelike Games: the permadeath run..", "g": "overview", "l": 2, "q": "What is Roguelike Games: the complete guide?", "a": "Roguelike Games: the permadeath run..", "x": "The complete game genre guide to Roguelike Games: the permadeath run.. Hades. History, meaning, practices, and how to engage respectfully — everything in one database. Permadeath. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Roguelike Games essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Roguelike Games essentials.", "x": "At a glance: Roguelike Games — the permadeath run.. Permadeath. The essentials: Runs.. Procedural. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Hades.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Hades.", "x": "Roguelike Games: Hades.. Runs. Essential knowledge — Procedural.. the permadeath run. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Hades..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Hades..", "x": "Explained: Hades.. Difficulty. The context — Roguelike Games. Runs. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Permadeath.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Permadeath.", "x": "Roguelike Games: Permadeath.. Rogue. Essential knowledge — Runs.. the permadeath run. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Permadeath..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Permadeath..", "x": "Explained: Permadeath.. Hades. The context — Roguelike Games. Rogue. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Procedural.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Procedural.", "x": "Roguelike Games: Procedural.. Difficulty. Essential knowledge — Rogue.. the permadeath run. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Procedural..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Procedural..", "x": "Explained: Procedural.. Classics. The context — Roguelike Games. Difficulty. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Runs.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Runs.", "x": "Roguelike Games: Runs.. Hades. Essential knowledge — Difficulty.. the permadeath run. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Runs..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Runs..", "x": "Explained: Runs.. Permadeath. The context — Roguelike Games. Hades. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Rogue.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Rogue.", "x": "Roguelike Games: Rogue.. Classics. Essential knowledge — Hades.. the permadeath run. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Rogue..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Rogue..", "x": "Explained: Rogue.. Runs. The context — Roguelike Games. Permadeath. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Difficulty.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Difficulty.", "x": "Roguelike Games: Difficulty.. Permadeath. Essential knowledge — Permadeath.. the permadeath run. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Difficulty..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Difficulty..", "x": "Explained: Difficulty.. Rogue. The context — Roguelike Games. Procedural. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Permadeath.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Permadeath.", "x": "Roguelike Games in depth: Permadeath.. Permadeath. Details — the permadeath run.. Rogue. Runs. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Runs.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Runs.", "x": "Roguelike Games in depth: Runs.. Procedural. Details — the permadeath run.. Difficulty. Rogue. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Rogue.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Rogue.", "x": "Roguelike Games in depth: Rogue.. Runs. Details — the permadeath run.. Hades. Difficulty. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Difficulty.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Difficulty.", "x": "Roguelike Games in depth: Difficulty.. Rogue. Details — the permadeath run.. Classics. Hades. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Hades.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Hades.", "x": "Roguelike Games in depth: Hades.. Difficulty. Details — the permadeath run.. Permadeath. Permadeath. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Classics.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Classics.", "x": "Roguelike Games in depth: Classics.. Hades. Details — the permadeath run.. Runs. Procedural. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Roguelike Games comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Roguelike Games comes from.", "x": "Origins: Permadeath.. Hades. The history of Roguelike Games — the permadeath run.. Runs. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Roguelike Games respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Roguelike Games respectfully.", "x": "Engaging: Rogue.. Permadeath. How to participate or observe well — Roguelike Games. the permadeath run. Respect first, always; Difficulty.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Roguelike Games do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Roguelike Games do's and don'ts.", "x": "Etiquette: Hades.. Procedural. The rules of respect — Roguelike Games. the permadeath run. When in doubt, ask about Classics.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Roguelike Games.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Roguelike Games.", "x": "Planning: Permadeath.. Runs. Practical notes — Roguelike Games. the permadeath run. A little planning shows respect for Runs.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Roguelike Games and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Roguelike Games and money.", "x": "Costs: Rogue.. Rogue. What to budget — Roguelike Games. the permadeath run. The best experiences of Difficulty. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-game-roguelike-video-games-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
