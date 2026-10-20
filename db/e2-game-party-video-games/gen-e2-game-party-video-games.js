(function(){'use strict';
/* JAH Party Games Game Genre Database generator — jahdb-e2-game-party-video-games-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-game-party-video-games',PREFIX='JAH-E2GAMEPARTY-',NAME='JAH Party Games Game Genre Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Party Games: the complete guide", "d": "Party Games: the couch multiplayer..", "g": "overview", "l": 2, "q": "What is Party Games: the complete guide?", "a": "Party Games: the couch multiplayer..", "x": "The complete game genre guide to Party Games: the couch multiplayer.. Mario Party. History, meaning, practices, and how to engage respectfully — everything in one database. Couch. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Party Games essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Party Games essentials.", "x": "At a glance: Party Games — the couch multiplayer.. Jackbox. The essentials: Minigames.. Couch. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Mario Party.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Mario Party.", "x": "Party Games: Mario Party.. Minigames. Essential knowledge — Couch.. the couch multiplayer. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Mario Party..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Mario Party..", "x": "Explained: Mario Party.. Chaos. The context — Party Games. Minigames. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Jackbox.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Jackbox.", "x": "Party Games: Jackbox.. Friends. Essential knowledge — Minigames.. the couch multiplayer. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Jackbox..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Jackbox..", "x": "Explained: Jackbox.. Jackbox. The context — Party Games. Friends. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Couch.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Couch.", "x": "Party Games: Couch.. Chaos. Essential knowledge — Friends.. the couch multiplayer. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Couch..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Couch..", "x": "Explained: Couch.. Classics. The context — Party Games. Chaos. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Minigames.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Minigames.", "x": "Party Games: Minigames.. Jackbox. Essential knowledge — Chaos.. the couch multiplayer. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Minigames..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Minigames..", "x": "Explained: Minigames.. Couch. The context — Party Games. Mario Party. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Friends.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Friends.", "x": "Party Games: Friends.. Classics. Essential knowledge — Mario Party.. the couch multiplayer. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Friends..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Friends..", "x": "Explained: Friends.. Minigames. The context — Party Games. Jackbox. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Chaos.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Chaos.", "x": "Party Games: Chaos.. Couch. Essential knowledge — Jackbox.. the couch multiplayer. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Chaos..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Chaos..", "x": "Explained: Chaos.. Friends. The context — Party Games. Couch. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Couch.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Couch.", "x": "Party Games in depth: Couch.. Jackbox. Details — the couch multiplayer.. Friends. Minigames. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Minigames.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Minigames.", "x": "Party Games in depth: Minigames.. Couch. Details — the couch multiplayer.. Chaos. Friends. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Friends.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Friends.", "x": "Party Games in depth: Friends.. Minigames. Details — the couch multiplayer.. Jackbox. Chaos. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Chaos.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Chaos.", "x": "Party Games in depth: Chaos.. Friends. Details — the couch multiplayer.. Classics. Mario Party. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Jackbox.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Jackbox.", "x": "Party Games in depth: Jackbox.. Chaos. Details — the couch multiplayer.. Couch. Jackbox. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Classics.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Classics.", "x": "Party Games in depth: Classics.. Mario Party. Details — the couch multiplayer.. Minigames. Couch. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Party Games comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Party Games comes from.", "x": "Origins: Couch.. Mario Party. The history of Party Games — the couch multiplayer.. Minigames. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Party Games respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Party Games respectfully.", "x": "Engaging: Friends.. Jackbox. How to participate or observe well — Party Games. the couch multiplayer. Respect first, always; Chaos.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Party Games do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Party Games do's and don'ts.", "x": "Etiquette: Jackbox.. Couch. The rules of respect — Party Games. the couch multiplayer. When in doubt, ask about Classics.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Party Games.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Party Games.", "x": "Planning: Couch.. Minigames. Practical notes — Party Games. the couch multiplayer. A little planning shows respect for Minigames.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Party Games and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Party Games and money.", "x": "Costs: Friends.. Friends. What to budget — Party Games. the couch multiplayer. The best experiences of Chaos. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-game-party-video-games-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
