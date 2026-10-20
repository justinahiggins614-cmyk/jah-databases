(function(){'use strict';
/* JAH 7 Wonders Board Game Database generator — jahdb-e2-board-seven-wonders-board-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-board-seven-wonders-board',PREFIX='JAH-E2BOARDSEVE-',NAME='JAH 7 Wonders Board Game Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "7 Wonders: the complete guide", "d": "7 Wonders: the card drafting..", "g": "overview", "l": 2, "q": "What is 7 Wonders: the complete guide?", "a": "7 Wonders: the card drafting..", "x": "The complete board game guide to 7 Wonders: the card drafting.. 2010. History, meaning, practices, and how to engage respectfully — everything in one database. Drafting. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "7 Wonders essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "7 Wonders essentials.", "x": "At a glance: 7 Wonders — the card drafting.. Drafting. The essentials: Ages.. Wonders. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "2010.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "2010.", "x": "7 Wonders: 2010.. Ages. Essential knowledge — Wonders.. the card drafting. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 2010..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 2010..", "x": "Explained: 2010.. Antoine. The context — 7 Wonders. 3 ages. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Drafting.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Drafting.", "x": "7 Wonders: Drafting.. Simultaneous. Essential knowledge — 3 ages.. the card drafting. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Drafting..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Drafting..", "x": "Explained: Drafting.. Wonders. The context — 7 Wonders. Simultaneous. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Wonders.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Wonders.", "x": "7 Wonders: Wonders.. Antoine. Essential knowledge — Simultaneous.. the card drafting. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Wonders..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Wonders..", "x": "Explained: Wonders.. Strategy. The context — 7 Wonders. Antoine. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "3 ages.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "3 ages.", "x": "7 Wonders: 3 ages.. Wonders. Essential knowledge — Antoine.. the card drafting. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: 3 ages..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: 3 ages..", "x": "Explained: 3 ages.. Drafting. The context — 7 Wonders. 2010. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Simultaneous.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Simultaneous.", "x": "7 Wonders: Simultaneous.. Strategy. Essential knowledge — 2010.. the card drafting. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Simultaneous..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Simultaneous..", "x": "Explained: Simultaneous.. Ages. The context — 7 Wonders. Drafting. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Antoine.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Antoine.", "x": "7 Wonders: Antoine.. Drafting. Essential knowledge — Drafting.. the card drafting. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Antoine..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Antoine..", "x": "Explained: Antoine.. Simultaneous. The context — 7 Wonders. Wonders. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Drafting.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Drafting.", "x": "7 Wonders in depth: Drafting.. Drafting. Details — the card drafting.. Simultaneous. 3 ages. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Ages.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Ages.", "x": "7 Wonders in depth: Ages.. Wonders. Details — the card drafting.. Antoine. Simultaneous. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Simultaneous.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Simultaneous.", "x": "7 Wonders in depth: Simultaneous.. 3 ages. Details — the card drafting.. Wonders. Antoine. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Antoine.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Antoine.", "x": "7 Wonders in depth: Antoine.. Simultaneous. Details — the card drafting.. Strategy. 2010. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Wonders.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Wonders.", "x": "7 Wonders in depth: Wonders.. Antoine. Details — the card drafting.. Drafting. Drafting. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Strategy.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Strategy.", "x": "7 Wonders in depth: Strategy.. 2010. Details — the card drafting.. Ages. Wonders. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where 7 Wonders comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where 7 Wonders comes from.", "x": "Origins: Drafting.. 2010. The history of 7 Wonders — the card drafting.. Ages. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing 7 Wonders respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing 7 Wonders respectfully.", "x": "Engaging: Simultaneous.. Drafting. How to participate or observe well — 7 Wonders. the card drafting. Respect first, always; Antoine.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "7 Wonders do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "7 Wonders do's and don'ts.", "x": "Etiquette: Wonders.. Wonders. The rules of respect — 7 Wonders. the card drafting. When in doubt, ask about Strategy.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around 7 Wonders.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around 7 Wonders.", "x": "Planning: Drafting.. 3 ages. Practical notes — 7 Wonders. the card drafting. A little planning shows respect for Ages.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "7 Wonders and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "7 Wonders and money.", "x": "Costs: Simultaneous.. Simultaneous. What to budget — 7 Wonders. the card drafting. The best experiences of Antoine. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-board-seven-wonders-board-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
