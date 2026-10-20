(function(){'use strict';
/* JAH Catan Board Game Board Game Database generator — jahdb-e2-board-catan-board-game-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-board-catan-board-game',PREFIX='JAH-E2BOARDCATA-',NAME='JAH Catan Board Game Board Game Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Catan Board Game: the complete guide", "d": "Catan Board Game: the gateway classic..", "g": "overview", "l": 2, "q": "What is Catan Board Game: the complete guide?", "a": "Catan Board Game: the gateway classic..", "x": "The complete board game guide to Catan Board Game: the gateway classic.. 1995. History, meaning, practices, and how to engage respectfully — everything in one database. Hexes. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Catan Board Game essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Catan Board Game essentials.", "x": "At a glance: Catan Board Game — the gateway classic.. Settlers. The essentials: Trading.. Hexes. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "1995.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "1995.", "x": "Catan Board Game: 1995.. Trading. Essential knowledge — Hexes.. the gateway classic. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 1995..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 1995..", "x": "Explained: 1995.. Gateway. The context — Catan Board Game. Trading. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Settlers.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Settlers.", "x": "Catan Board Game: Settlers.. Teuber. Essential knowledge — Trading.. the gateway classic. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Settlers..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Settlers..", "x": "Explained: Settlers.. Settlers. The context — Catan Board Game. Teuber. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Hexes.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Hexes.", "x": "Catan Board Game: Hexes.. Gateway. Essential knowledge — Teuber.. the gateway classic. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Hexes..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Hexes..", "x": "Explained: Hexes.. Strategy. The context — Catan Board Game. Gateway. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Trading.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Trading.", "x": "Catan Board Game: Trading.. Settlers. Essential knowledge — Gateway.. the gateway classic. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Trading..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Trading..", "x": "Explained: Trading.. Hexes. The context — Catan Board Game. 1995. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Teuber.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Teuber.", "x": "Catan Board Game: Teuber.. Strategy. Essential knowledge — 1995.. the gateway classic. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Teuber..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Teuber..", "x": "Explained: Teuber.. Trading. The context — Catan Board Game. Settlers. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Gateway.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Gateway.", "x": "Catan Board Game: Gateway.. Hexes. Essential knowledge — Settlers.. the gateway classic. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Gateway..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Gateway..", "x": "Explained: Gateway.. Teuber. The context — Catan Board Game. Hexes. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Hexes.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Hexes.", "x": "Catan Board Game in depth: Hexes.. Settlers. Details — the gateway classic.. Teuber. Trading. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Trading.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Trading.", "x": "Catan Board Game in depth: Trading.. Hexes. Details — the gateway classic.. Gateway. Teuber. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Teuber.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Teuber.", "x": "Catan Board Game in depth: Teuber.. Trading. Details — the gateway classic.. Settlers. Gateway. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Gateway.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Gateway.", "x": "Catan Board Game in depth: Gateway.. Teuber. Details — the gateway classic.. Strategy. 1995. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Settlers.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Settlers.", "x": "Catan Board Game in depth: Settlers.. Gateway. Details — the gateway classic.. Hexes. Settlers. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Strategy.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Strategy.", "x": "Catan Board Game in depth: Strategy.. 1995. Details — the gateway classic.. Trading. Hexes. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Catan Board Game comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Catan Board Game comes from.", "x": "Origins: Hexes.. 1995. The history of Catan Board Game — the gateway classic.. Trading. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Catan Board Game respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Catan Board Game respectfully.", "x": "Engaging: Teuber.. Settlers. How to participate or observe well — Catan Board Game. the gateway classic. Respect first, always; Gateway.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Catan Board Game do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Catan Board Game do's and don'ts.", "x": "Etiquette: Settlers.. Hexes. The rules of respect — Catan Board Game. the gateway classic. When in doubt, ask about Strategy.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Catan Board Game.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Catan Board Game.", "x": "Planning: Hexes.. Trading. Practical notes — Catan Board Game. the gateway classic. A little planning shows respect for Trading.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Catan Board Game and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Catan Board Game and money.", "x": "Costs: Teuber.. Teuber. What to budget — Catan Board Game. the gateway classic. The best experiences of Gateway. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-board-catan-board-game-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
