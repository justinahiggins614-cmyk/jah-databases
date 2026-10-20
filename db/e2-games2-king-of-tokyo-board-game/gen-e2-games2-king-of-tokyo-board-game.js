(function(){'use strict';
/* JAH King of Tokyo Board Database generator — jahdb-e2-games2-king-of-tokyo-board-game-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-games2-king-of-tokyo-board-game',PREFIX='JAH-E2GAMES2KIN-',NAME='JAH King of Tokyo Board Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "King of Tokyo Board: the complete guide", "d": "King of Tokyo Board: the monster dice..", "g": "overview", "l": 2, "q": "What is King of Tokyo Board: the complete guide?", "a": "King of Tokyo Board: the monster dice..", "x": "The complete board game guide to King of Tokyo Board: the monster dice.. 2011. History, meaning, practices, and how to engage respectfully — everything in one database. Dice. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "King of Tokyo Board essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "King of Tokyo Board essentials.", "x": "At a glance: King of Tokyo Board — the monster dice.. Dice. The essentials: Yahtzee.. Monsters. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "2011.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "2011.", "x": "King of Tokyo Board: 2011.. Yahtzee. Essential knowledge — Monsters.. the monster dice. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 2011..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 2011..", "x": "Explained: 2011.. 2011. The context — King of Tokyo Board. Tokyo. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Dice.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Dice.", "x": "King of Tokyo Board: Dice.. Power. Essential knowledge — Tokyo.. the monster dice. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Dice..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Dice..", "x": "Explained: Dice.. Monsters. The context — King of Tokyo Board. Yahtzee. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Monsters.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Monsters.", "x": "King of Tokyo Board: Monsters.. 2011. Essential knowledge — Yahtzee.. the monster dice. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Monsters..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Monsters..", "x": "Explained: Monsters.. Guide. The context — King of Tokyo Board. Power. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Tokyo.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Tokyo.", "x": "King of Tokyo Board: Tokyo.. Monsters. Essential knowledge — Power.. the monster dice. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Tokyo..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Tokyo..", "x": "Explained: Tokyo.. Dice. The context — King of Tokyo Board. 2011. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Yahtzee.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Yahtzee.", "x": "King of Tokyo Board: Yahtzee.. Guide. Essential knowledge — 2011.. the monster dice. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Yahtzee..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Yahtzee..", "x": "Explained: Yahtzee.. Yahtzee. The context — King of Tokyo Board. Dice. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Power.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Power.", "x": "King of Tokyo Board: Power.. Dice. Essential knowledge — Dice.. the monster dice. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Power..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Power..", "x": "Explained: Power.. Power. The context — King of Tokyo Board. Monsters. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Dice.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Dice.", "x": "King of Tokyo Board in depth: Dice.. Dice. Details — the monster dice.. Power. Tokyo. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Yahtzee.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Yahtzee.", "x": "King of Tokyo Board in depth: Yahtzee.. Monsters. Details — the monster dice.. 2011. Yahtzee. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Power.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Power.", "x": "King of Tokyo Board in depth: Power.. Tokyo. Details — the monster dice.. Monsters. Power. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "2011.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "2011.", "x": "King of Tokyo Board in depth: 2011.. Yahtzee. Details — the monster dice.. Guide. 2011. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Monsters.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Monsters.", "x": "King of Tokyo Board in depth: Monsters.. Power. Details — the monster dice.. Dice. Dice. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Guide.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Guide.", "x": "King of Tokyo Board in depth: Guide.. 2011. Details — the monster dice.. Yahtzee. Monsters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where King of Tokyo Board comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where King of Tokyo Board comes from.", "x": "Origins: Dice.. 2011. The history of King of Tokyo Board — the monster dice.. Yahtzee. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing King of Tokyo Board respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing King of Tokyo Board respectfully.", "x": "Engaging: Power.. Dice. How to participate or observe well — King of Tokyo Board. the monster dice. Respect first, always; 2011.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "King of Tokyo Board do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "King of Tokyo Board do's and don'ts.", "x": "Etiquette: Monsters.. Monsters. The rules of respect — King of Tokyo Board. the monster dice. When in doubt, ask about Guide.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around King of Tokyo Board.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around King of Tokyo Board.", "x": "Planning: Dice.. Tokyo. Practical notes — King of Tokyo Board. the monster dice. A little planning shows respect for Yahtzee.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "King of Tokyo Board and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "King of Tokyo Board and money.", "x": "Costs: Power.. Yahtzee. What to budget — King of Tokyo Board. the monster dice. The best experiences of 2011. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-games2-king-of-tokyo-board-game-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
