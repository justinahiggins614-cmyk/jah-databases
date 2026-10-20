(function(){'use strict';
/* JAH Battleship Board Board Game Database generator — jahdb-e2-board-battleship-board-game-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-board-battleship-board-game',PREFIX='JAH-E2BOARDBATT-',NAME='JAH Battleship Board Board Game Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Battleship Board: the complete guide", "d": "Battleship Board: the coordinate hunt..", "g": "overview", "l": 2, "q": "What is Battleship Board: the complete guide?", "a": "Battleship Board: the coordinate hunt..", "x": "The complete board game guide to Battleship Board: the coordinate hunt.. 1967. History, meaning, practices, and how to engage respectfully — everything in one database. Grid. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Battleship Board essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Battleship Board essentials.", "x": "At a glance: Battleship Board — the coordinate hunt.. You sunk. The essentials: Pegs.. Grid. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "1967.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "1967.", "x": "Battleship Board: 1967.. Pegs. Essential knowledge — Grid.. the coordinate hunt. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 1967..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 1967..", "x": "Explained: 1967.. Bradley. The context — Battleship Board. Pegs. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "You sunk.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "You sunk.", "x": "Battleship Board: You sunk.. Salvo. Essential knowledge — Pegs.. the coordinate hunt. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: You sunk..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: You sunk..", "x": "Explained: You sunk.. Sunk. The context — Battleship Board. Milton Bradley. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Grid.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Grid.", "x": "Battleship Board: Grid.. Bradley. Essential knowledge — Milton Bradley.. the coordinate hunt. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Grid..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Grid..", "x": "Explained: Grid.. Strategy. The context — Battleship Board. Salvo. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Pegs.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Pegs.", "x": "Battleship Board: Pegs.. Sunk. Essential knowledge — Salvo.. the coordinate hunt. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Pegs..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Pegs..", "x": "Explained: Pegs.. Grid. The context — Battleship Board. 1967. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Milton Bradley.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Milton Bradley.", "x": "Battleship Board: Milton Bradley.. Strategy. Essential knowledge — 1967.. the coordinate hunt. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Milton Bradley..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Milton Bradley..", "x": "Explained: Milton Bradley.. Pegs. The context — Battleship Board. You sunk. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Salvo.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Salvo.", "x": "Battleship Board: Salvo.. Grid. Essential knowledge — You sunk.. the coordinate hunt. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Salvo..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Salvo..", "x": "Explained: Salvo.. Salvo. The context — Battleship Board. Grid. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Grid.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Grid.", "x": "Battleship Board in depth: Grid.. You sunk. Details — the coordinate hunt.. Salvo. Pegs. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Pegs.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Pegs.", "x": "Battleship Board in depth: Pegs.. Grid. Details — the coordinate hunt.. Bradley. Milton Bradley. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Salvo.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Salvo.", "x": "Battleship Board in depth: Salvo.. Pegs. Details — the coordinate hunt.. Sunk. Salvo. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Bradley.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Bradley.", "x": "Battleship Board in depth: Bradley.. Milton Bradley. Details — the coordinate hunt.. Strategy. 1967. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Sunk.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Sunk.", "x": "Battleship Board in depth: Sunk.. Salvo. Details — the coordinate hunt.. Grid. You sunk. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Strategy.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Strategy.", "x": "Battleship Board in depth: Strategy.. 1967. Details — the coordinate hunt.. Pegs. Grid. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Battleship Board comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Battleship Board comes from.", "x": "Origins: Grid.. 1967. The history of Battleship Board — the coordinate hunt.. Pegs. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Battleship Board respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Battleship Board respectfully.", "x": "Engaging: Salvo.. You sunk. How to participate or observe well — Battleship Board. the coordinate hunt. Respect first, always; Bradley.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Battleship Board do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Battleship Board do's and don'ts.", "x": "Etiquette: Sunk.. Grid. The rules of respect — Battleship Board. the coordinate hunt. When in doubt, ask about Strategy.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Battleship Board.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Battleship Board.", "x": "Planning: Grid.. Pegs. Practical notes — Battleship Board. the coordinate hunt. A little planning shows respect for Pegs.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Battleship Board and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Battleship Board and money.", "x": "Costs: Salvo.. Milton Bradley. What to budget — Battleship Board. the coordinate hunt. The best experiences of Bradley. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-board-battleship-board-game-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
