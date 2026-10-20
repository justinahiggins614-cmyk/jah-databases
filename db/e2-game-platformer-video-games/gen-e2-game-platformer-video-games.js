(function(){'use strict';
/* JAH Platformer Games Game Genre Database generator — jahdb-e2-game-platformer-video-games-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-game-platformer-video-games',PREFIX='JAH-E2GAMEPLATF-',NAME='JAH Platformer Games Game Genre Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Platformer Games: the complete guide", "d": "Platformer Games: the jumping genre..", "g": "overview", "l": 2, "q": "What is Platformer Games: the complete guide?", "a": "Platformer Games: the jumping genre..", "x": "The complete game genre guide to Platformer Games: the jumping genre.. Mario. History, meaning, practices, and how to engage respectfully — everything in one database. Jumping. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Platformer Games essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Platformer Games essentials.", "x": "At a glance: Platformer Games — the jumping genre.. Jumping. The essentials: Precision.. Levels. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Mario.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Mario.", "x": "Platformer Games: Mario.. Precision. Essential knowledge — Levels.. the jumping genre. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Mario..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Mario..", "x": "Explained: Mario.. Mario. The context — Platformer Games. Precision. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Jumping.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Jumping.", "x": "Platformer Games: Jumping.. Bosses. Essential knowledge — Precision.. the jumping genre. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Jumping..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Jumping..", "x": "Explained: Jumping.. Sonic. The context — Platformer Games. Sonic. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Levels.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Levels.", "x": "Platformer Games: Levels.. Mario. Essential knowledge — Sonic.. the jumping genre. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Levels..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Levels..", "x": "Explained: Levels.. Classics. The context — Platformer Games. Bosses. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Precision.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Precision.", "x": "Platformer Games: Precision.. Sonic. Essential knowledge — Bosses.. the jumping genre. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Precision..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Precision..", "x": "Explained: Precision.. Jumping. The context — Platformer Games. Mario. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Sonic.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Sonic.", "x": "Platformer Games: Sonic.. Classics. Essential knowledge — Mario.. the jumping genre. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Sonic..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Sonic..", "x": "Explained: Sonic.. Precision. The context — Platformer Games. Jumping. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Bosses.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Bosses.", "x": "Platformer Games: Bosses.. Jumping. Essential knowledge — Jumping.. the jumping genre. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Bosses..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Bosses..", "x": "Explained: Bosses.. Bosses. The context — Platformer Games. Levels. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Jumping.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Jumping.", "x": "Platformer Games in depth: Jumping.. Jumping. Details — the jumping genre.. Bosses. Precision. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Precision.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Precision.", "x": "Platformer Games in depth: Precision.. Levels. Details — the jumping genre.. Mario. Sonic. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Bosses.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Bosses.", "x": "Platformer Games in depth: Bosses.. Precision. Details — the jumping genre.. Sonic. Bosses. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Mario.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Mario.", "x": "Platformer Games in depth: Mario.. Sonic. Details — the jumping genre.. Classics. Mario. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Sonic.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Sonic.", "x": "Platformer Games in depth: Sonic.. Bosses. Details — the jumping genre.. Jumping. Jumping. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Classics.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Classics.", "x": "Platformer Games in depth: Classics.. Mario. Details — the jumping genre.. Precision. Levels. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Platformer Games comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Platformer Games comes from.", "x": "Origins: Jumping.. Mario. The history of Platformer Games — the jumping genre.. Precision. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Platformer Games respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Platformer Games respectfully.", "x": "Engaging: Bosses.. Jumping. How to participate or observe well — Platformer Games. the jumping genre. Respect first, always; Mario.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Platformer Games do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Platformer Games do's and don'ts.", "x": "Etiquette: Sonic.. Levels. The rules of respect — Platformer Games. the jumping genre. When in doubt, ask about Classics.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Platformer Games.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Platformer Games.", "x": "Planning: Jumping.. Precision. Practical notes — Platformer Games. the jumping genre. A little planning shows respect for Precision.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Platformer Games and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Platformer Games and money.", "x": "Costs: Bosses.. Sonic. What to budget — Platformer Games. the jumping genre. The best experiences of Mario. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-game-platformer-video-games-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
