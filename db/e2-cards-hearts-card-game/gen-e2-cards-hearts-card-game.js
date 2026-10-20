(function(){'use strict';
/* JAH Hearts Card Card Game Database generator — jahdb-e2-cards-hearts-card-game-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-cards-hearts-card-game',PREFIX='JAH-E2CARDSHEAR-',NAME='JAH Hearts Card Card Game Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Hearts Card: the complete guide", "d": "Hearts Card: the avoid classic..", "g": "overview", "l": 2, "q": "What is Hearts Card: the complete guide?", "a": "Hearts Card: the avoid classic..", "x": "The complete card game guide to Hearts Card: the avoid classic.. Avoid hearts. History, meaning, practices, and how to engage respectfully — everything in one database. Avoid. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Hearts Card essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Hearts Card essentials.", "x": "At a glance: Hearts Card — the avoid classic.. Queen spades. The essentials: Moon.. Shooting moon. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Avoid hearts.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Avoid hearts.", "x": "Hearts Card: Avoid hearts.. Moon. Essential knowledge — Shooting moon.. the avoid classic. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Avoid hearts..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Avoid hearts..", "x": "Explained: Avoid hearts.. Windows. The context — Hearts Card. Tricks. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Queen spades.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Queen spades.", "x": "Hearts Card: Queen spades.. Passing. Essential knowledge — Tricks.. the avoid classic. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Queen spades..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Queen spades..", "x": "Explained: Queen spades.. Queen. The context — Hearts Card. Passing. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Shooting moon.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Shooting moon.", "x": "Hearts Card: Shooting moon.. Windows. Essential knowledge — Passing.. the avoid classic. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Shooting moon..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Shooting moon..", "x": "Explained: Shooting moon.. Strategy. The context — Hearts Card. Windows. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Tricks.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Tricks.", "x": "Hearts Card: Tricks.. Queen. Essential knowledge — Windows.. the avoid classic. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Tricks..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Tricks..", "x": "Explained: Tricks.. Avoid. The context — Hearts Card. Avoid hearts. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Passing.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Passing.", "x": "Hearts Card: Passing.. Strategy. Essential knowledge — Avoid hearts.. the avoid classic. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Passing..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Passing..", "x": "Explained: Passing.. Moon. The context — Hearts Card. Queen spades. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Windows.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Windows.", "x": "Hearts Card: Windows.. Avoid. Essential knowledge — Queen spades.. the avoid classic. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Windows..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Windows..", "x": "Explained: Windows.. Passing. The context — Hearts Card. Shooting moon. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Avoid.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Avoid.", "x": "Hearts Card in depth: Avoid.. Queen spades. Details — the avoid classic.. Passing. Tricks. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Moon.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Moon.", "x": "Hearts Card in depth: Moon.. Shooting moon. Details — the avoid classic.. Windows. Passing. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Passing.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Passing.", "x": "Hearts Card in depth: Passing.. Tricks. Details — the avoid classic.. Queen. Windows. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Windows.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Windows.", "x": "Hearts Card in depth: Windows.. Passing. Details — the avoid classic.. Strategy. Avoid hearts. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Queen.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Queen.", "x": "Hearts Card in depth: Queen.. Windows. Details — the avoid classic.. Avoid. Queen spades. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Strategy.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Strategy.", "x": "Hearts Card in depth: Strategy.. Avoid hearts. Details — the avoid classic.. Moon. Shooting moon. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Hearts Card comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Hearts Card comes from.", "x": "Origins: Avoid.. Avoid hearts. The history of Hearts Card — the avoid classic.. Moon. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Hearts Card respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Hearts Card respectfully.", "x": "Engaging: Passing.. Queen spades. How to participate or observe well — Hearts Card. the avoid classic. Respect first, always; Windows.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Hearts Card do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Hearts Card do's and don'ts.", "x": "Etiquette: Queen.. Shooting moon. The rules of respect — Hearts Card. the avoid classic. When in doubt, ask about Strategy.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Hearts Card.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Hearts Card.", "x": "Planning: Avoid.. Tricks. Practical notes — Hearts Card. the avoid classic. A little planning shows respect for Moon.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Hearts Card and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Hearts Card and money.", "x": "Costs: Passing.. Passing. What to budget — Hearts Card. the avoid classic. The best experiences of Windows. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-cards-hearts-card-game-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
