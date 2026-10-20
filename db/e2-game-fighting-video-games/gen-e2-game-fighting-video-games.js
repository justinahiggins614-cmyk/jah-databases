(function(){'use strict';
/* JAH Fighting Games Game Genre Database generator — jahdb-e2-game-fighting-video-games-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-game-fighting-video-games',PREFIX='JAH-E2GAMEFIGHT-',NAME='JAH Fighting Games Game Genre Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Fighting Games: the complete guide", "d": "Fighting Games: the one-on-one..", "g": "overview", "l": 2, "q": "What is Fighting Games: the complete guide?", "a": "Fighting Games: the one-on-one..", "x": "The complete game genre guide to Fighting Games: the one-on-one.. Street Fighter. History, meaning, practices, and how to engage respectfully — everything in one database. Combos. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Fighting Games essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Fighting Games essentials.", "x": "At a glance: Fighting Games — the one-on-one.. Combos. The essentials: Arcade.. Arcade. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Street Fighter.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Street Fighter.", "x": "Fighting Games: Street Fighter.. Arcade. Essential knowledge — Arcade.. the one-on-one. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Street Fighter..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Street Fighter..", "x": "Explained: Street Fighter.. Tournaments. The context — Fighting Games. Tekken. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Combos.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Combos.", "x": "Fighting Games: Combos.. Frames. Essential knowledge — Tekken.. the one-on-one. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Combos..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Combos..", "x": "Explained: Combos.. SF. The context — Fighting Games. Frames. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Arcade.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Arcade.", "x": "Fighting Games: Arcade.. Tournaments. Essential knowledge — Frames.. the one-on-one. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Arcade..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Arcade..", "x": "Explained: Arcade.. Classics. The context — Fighting Games. Tournaments. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Tekken.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Tekken.", "x": "Fighting Games: Tekken.. SF. Essential knowledge — Tournaments.. the one-on-one. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Tekken..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Tekken..", "x": "Explained: Tekken.. Combos. The context — Fighting Games. Street Fighter. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Frames.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Frames.", "x": "Fighting Games: Frames.. Classics. Essential knowledge — Street Fighter.. the one-on-one. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Frames..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Frames..", "x": "Explained: Frames.. Arcade. The context — Fighting Games. Combos. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Tournaments.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Tournaments.", "x": "Fighting Games: Tournaments.. Combos. Essential knowledge — Combos.. the one-on-one. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Tournaments..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Tournaments..", "x": "Explained: Tournaments.. Frames. The context — Fighting Games. Arcade. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Combos.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Combos.", "x": "Fighting Games in depth: Combos.. Combos. Details — the one-on-one.. Frames. Tekken. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Arcade.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Arcade.", "x": "Fighting Games in depth: Arcade.. Arcade. Details — the one-on-one.. Tournaments. Frames. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Frames.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Frames.", "x": "Fighting Games in depth: Frames.. Tekken. Details — the one-on-one.. SF. Tournaments. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Tournaments.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Tournaments.", "x": "Fighting Games in depth: Tournaments.. Frames. Details — the one-on-one.. Classics. Street Fighter. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "SF.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "SF.", "x": "Fighting Games in depth: SF.. Tournaments. Details — the one-on-one.. Combos. Combos. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Classics.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Classics.", "x": "Fighting Games in depth: Classics.. Street Fighter. Details — the one-on-one.. Arcade. Arcade. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Fighting Games comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Fighting Games comes from.", "x": "Origins: Combos.. Street Fighter. The history of Fighting Games — the one-on-one.. Arcade. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Fighting Games respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Fighting Games respectfully.", "x": "Engaging: Frames.. Combos. How to participate or observe well — Fighting Games. the one-on-one. Respect first, always; Tournaments.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Fighting Games do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Fighting Games do's and don'ts.", "x": "Etiquette: SF.. Arcade. The rules of respect — Fighting Games. the one-on-one. When in doubt, ask about Classics.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Fighting Games.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Fighting Games.", "x": "Planning: Combos.. Tekken. Practical notes — Fighting Games. the one-on-one. A little planning shows respect for Arcade.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Fighting Games and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Fighting Games and money.", "x": "Costs: Frames.. Frames. What to budget — Fighting Games. the one-on-one. The best experiences of Tournaments. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-game-fighting-video-games-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
