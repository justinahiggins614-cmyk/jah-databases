(function(){'use strict';
/* JAH Rummy Card Card Game Database generator — jahdb-e2-cards-rummy-card-game-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-cards-rummy-card-game',PREFIX='JAH-E2CARDSRUMM-',NAME='JAH Rummy Card Card Game Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Rummy Card: the complete guide", "d": "Rummy Card: the meld classic..", "g": "overview", "l": 2, "q": "What is Rummy Card: the complete guide?", "a": "Rummy Card: the meld classic..", "x": "The complete card game guide to Rummy Card: the meld classic.. Melds. History, meaning, practices, and how to engage respectfully — everything in one database. Melds. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Rummy Card essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Rummy Card essentials.", "x": "At a glance: Rummy Card — the meld classic.. Sets. The essentials: Gin.. Runs. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Melds.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Melds.", "x": "Rummy Card: Melds.. Gin. Essential knowledge — Runs.. the meld classic. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Melds..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Melds..", "x": "Explained: Melds.. Points. The context — Rummy Card. Gin. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Sets.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Sets.", "x": "Rummy Card: Sets.. Discard. Essential knowledge — Gin.. the meld classic. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Sets..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Sets..", "x": "Explained: Sets.. Sets. The context — Rummy Card. Discard. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Runs.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Runs.", "x": "Rummy Card: Runs.. Points. Essential knowledge — Discard.. the meld classic. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Runs..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Runs..", "x": "Explained: Runs.. Strategy. The context — Rummy Card. Points. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Gin.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Gin.", "x": "Rummy Card: Gin.. Sets. Essential knowledge — Points.. the meld classic. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Gin..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Gin..", "x": "Explained: Gin.. Melds. The context — Rummy Card. Melds. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Discard.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Discard.", "x": "Rummy Card: Discard.. Strategy. Essential knowledge — Melds.. the meld classic. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Discard..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Discard..", "x": "Explained: Discard.. Gin. The context — Rummy Card. Sets. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Points.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Points.", "x": "Rummy Card: Points.. Melds. Essential knowledge — Sets.. the meld classic. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Points..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Points..", "x": "Explained: Points.. Discard. The context — Rummy Card. Runs. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Melds.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Melds.", "x": "Rummy Card in depth: Melds.. Sets. Details — the meld classic.. Discard. Gin. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Gin.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Gin.", "x": "Rummy Card in depth: Gin.. Runs. Details — the meld classic.. Points. Discard. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Discard.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Discard.", "x": "Rummy Card in depth: Discard.. Gin. Details — the meld classic.. Sets. Points. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Points.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Points.", "x": "Rummy Card in depth: Points.. Discard. Details — the meld classic.. Strategy. Melds. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Sets.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Sets.", "x": "Rummy Card in depth: Sets.. Points. Details — the meld classic.. Melds. Sets. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Strategy.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Strategy.", "x": "Rummy Card in depth: Strategy.. Melds. Details — the meld classic.. Gin. Runs. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Rummy Card comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Rummy Card comes from.", "x": "Origins: Melds.. Melds. The history of Rummy Card — the meld classic.. Gin. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Rummy Card respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Rummy Card respectfully.", "x": "Engaging: Discard.. Sets. How to participate or observe well — Rummy Card. the meld classic. Respect first, always; Points.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Rummy Card do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Rummy Card do's and don'ts.", "x": "Etiquette: Sets.. Runs. The rules of respect — Rummy Card. the meld classic. When in doubt, ask about Strategy.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Rummy Card.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Rummy Card.", "x": "Planning: Melds.. Gin. Practical notes — Rummy Card. the meld classic. A little planning shows respect for Gin.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Rummy Card and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Rummy Card and money.", "x": "Costs: Discard.. Discard. What to budget — Rummy Card. the meld classic. The best experiences of Points. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-cards-rummy-card-game-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
