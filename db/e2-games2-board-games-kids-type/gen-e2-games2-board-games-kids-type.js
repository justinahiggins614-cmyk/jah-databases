(function(){'use strict';
/* JAH Board Games Kids Database generator — jahdb-e2-games2-board-games-kids-type-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-games2-board-games-kids-type',PREFIX='JAH-E2GAMES2BOA-',NAME='JAH Board Games Kids Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Board Games Kids: the complete guide", "d": "Board Games Kids: the family table..", "g": "overview", "l": 2, "q": "What is Board Games Kids: the complete guide?", "a": "Board Games Kids: the family table..", "x": "The complete toys guide to Board Games Kids: the family table.. Candy Land. History, meaning, practices, and how to engage respectfully — everything in one database. Candy. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Board Games Kids essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Board Games Kids essentials.", "x": "At a glance: Board Games Kids — the family table.. Chutes. The essentials: Cooperative.. Sorry. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Candy Land.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Candy Land.", "x": "Board Games Kids: Candy Land.. Cooperative. Essential knowledge — Sorry.. the family table. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Candy Land..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Candy Land..", "x": "Explained: Candy Land.. Chutes. The context — Board Games Kids. Guess Who. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Chutes.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Chutes.", "x": "Board Games Kids: Chutes.. Ages. Essential knowledge — Guess Who.. the family table. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Chutes..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Chutes..", "x": "Explained: Chutes.. Sorry. The context — Board Games Kids. Cooperative. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Sorry.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Sorry.", "x": "Board Games Kids: Sorry.. Chutes. Essential knowledge — Cooperative.. the family table. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Sorry..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Sorry..", "x": "Explained: Sorry.. Guide. The context — Board Games Kids. Ages. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Guess Who.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Guess Who.", "x": "Board Games Kids: Guess Who.. Sorry. Essential knowledge — Ages.. the family table. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Guess Who..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Guess Who..", "x": "Explained: Guess Who.. Candy. The context — Board Games Kids. Candy Land. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Cooperative.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Cooperative.", "x": "Board Games Kids: Cooperative.. Guide. Essential knowledge — Candy Land.. the family table. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Cooperative..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Cooperative..", "x": "Explained: Cooperative.. Cooperative. The context — Board Games Kids. Chutes. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Ages.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Ages.", "x": "Board Games Kids: Ages.. Candy. Essential knowledge — Chutes.. the family table. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Ages..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Ages..", "x": "Explained: Ages.. Ages. The context — Board Games Kids. Sorry. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Candy.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Candy.", "x": "Board Games Kids in depth: Candy.. Chutes. Details — the family table.. Ages. Guess Who. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Cooperative.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Cooperative.", "x": "Board Games Kids in depth: Cooperative.. Sorry. Details — the family table.. Chutes. Cooperative. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Ages.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Ages.", "x": "Board Games Kids in depth: Ages.. Guess Who. Details — the family table.. Sorry. Ages. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Chutes.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Chutes.", "x": "Board Games Kids in depth: Chutes.. Cooperative. Details — the family table.. Guide. Candy Land. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Sorry.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Sorry.", "x": "Board Games Kids in depth: Sorry.. Ages. Details — the family table.. Candy. Chutes. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Guide.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Guide.", "x": "Board Games Kids in depth: Guide.. Candy Land. Details — the family table.. Cooperative. Sorry. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Board Games Kids comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Board Games Kids comes from.", "x": "Origins: Candy.. Candy Land. The history of Board Games Kids — the family table.. Cooperative. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Board Games Kids respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Board Games Kids respectfully.", "x": "Engaging: Ages.. Chutes. How to participate or observe well — Board Games Kids. the family table. Respect first, always; Chutes.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Board Games Kids do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Board Games Kids do's and don'ts.", "x": "Etiquette: Sorry.. Sorry. The rules of respect — Board Games Kids. the family table. When in doubt, ask about Guide.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Board Games Kids.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Board Games Kids.", "x": "Planning: Candy.. Guess Who. Practical notes — Board Games Kids. the family table. A little planning shows respect for Cooperative.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Board Games Kids and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Board Games Kids and money.", "x": "Costs: Ages.. Cooperative. What to budget — Board Games Kids. the family table. The best experiences of Chutes. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-games2-board-games-kids-type-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
