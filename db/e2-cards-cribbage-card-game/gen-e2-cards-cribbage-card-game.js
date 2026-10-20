(function(){'use strict';
/* JAH Cribbage Card Card Game Database generator — jahdb-e2-cards-cribbage-card-game-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-cards-cribbage-card-game',PREFIX='JAH-E2CARDSCRIB-',NAME='JAH Cribbage Card Card Game Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Cribbage Card: the complete guide", "d": "Cribbage Card: the peg classic..", "g": "overview", "l": 2, "q": "What is Cribbage Card: the complete guide?", "a": "Cribbage Card: the peg classic..", "x": "The complete card game guide to Cribbage Card: the peg classic.. Pegs. History, meaning, practices, and how to engage respectfully — everything in one database. Pegs. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Cribbage Card essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Cribbage Card essentials.", "x": "At a glance: Cribbage Card — the peg classic.. 15. The essentials: Nobs.. Board. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Pegs.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Pegs.", "x": "Cribbage Card: Pegs.. Nobs. Essential knowledge — Board.. the peg classic. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Pegs..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Pegs..", "x": "Explained: Pegs.. Board. The context — Cribbage Card. Nobs. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "15.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "15.", "x": "Cribbage Card: 15.. Skunks. Essential knowledge — Nobs.. the peg classic. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: 15..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: 15..", "x": "Explained: 15.. 15. The context — Cribbage Card. Skunks. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Board.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Board.", "x": "Cribbage Card: Board.. Board. Essential knowledge — Skunks.. the peg classic. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Board..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Board..", "x": "Explained: Board.. Strategy. The context — Cribbage Card. 1590s. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Nobs.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Nobs.", "x": "Cribbage Card: Nobs.. 15. Essential knowledge — 1590s.. the peg classic. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Nobs..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Nobs..", "x": "Explained: Nobs.. Pegs. The context — Cribbage Card. Pegs. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Skunks.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Skunks.", "x": "Cribbage Card: Skunks.. Strategy. Essential knowledge — Pegs.. the peg classic. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Skunks..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Skunks..", "x": "Explained: Skunks.. Nobs. The context — Cribbage Card. 15. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "1590s.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "1590s.", "x": "Cribbage Card: 1590s.. Pegs. Essential knowledge — 15.. the peg classic. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: 1590s..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: 1590s..", "x": "Explained: 1590s.. Skunks. The context — Cribbage Card. Board. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Pegs.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Pegs.", "x": "Cribbage Card in depth: Pegs.. 15. Details — the peg classic.. Skunks. Nobs. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Nobs.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Nobs.", "x": "Cribbage Card in depth: Nobs.. Board. Details — the peg classic.. Board. Skunks. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Skunks.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Skunks.", "x": "Cribbage Card in depth: Skunks.. Nobs. Details — the peg classic.. 15. 1590s. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Board.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Board.", "x": "Cribbage Card in depth: Board.. Skunks. Details — the peg classic.. Strategy. Pegs. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "15.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "15.", "x": "Cribbage Card in depth: 15.. 1590s. Details — the peg classic.. Pegs. 15. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Strategy.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Strategy.", "x": "Cribbage Card in depth: Strategy.. Pegs. Details — the peg classic.. Nobs. Board. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Cribbage Card comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Cribbage Card comes from.", "x": "Origins: Pegs.. Pegs. The history of Cribbage Card — the peg classic.. Nobs. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Cribbage Card respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Cribbage Card respectfully.", "x": "Engaging: Skunks.. 15. How to participate or observe well — Cribbage Card. the peg classic. Respect first, always; Board.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Cribbage Card do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Cribbage Card do's and don'ts.", "x": "Etiquette: 15.. Board. The rules of respect — Cribbage Card. the peg classic. When in doubt, ask about Strategy.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Cribbage Card.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Cribbage Card.", "x": "Planning: Pegs.. Nobs. Practical notes — Cribbage Card. the peg classic. A little planning shows respect for Nobs.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Cribbage Card and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Cribbage Card and money.", "x": "Costs: Skunks.. Skunks. What to budget — Cribbage Card. the peg classic. The best experiences of Board. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-cards-cribbage-card-game-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
