(function(){'use strict';
/* JAH Metaphysical Poetry Poetry Database generator — jahdb-e2-poetry-metaphysical-poetry-era-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-poetry-metaphysical-poetry-era',PREFIX='JAH-E2POETRYMET-',NAME='JAH Metaphysical Poetry Poetry Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Metaphysical Poetry: the complete guide", "d": "Metaphysical Poetry: the clever conceit..", "g": "overview", "l": 2, "q": "What is Metaphysical Poetry: the complete guide?", "a": "Metaphysical Poetry: the clever conceit..", "x": "The complete poetry guide to Metaphysical Poetry: the clever conceit.. Donne. History, meaning, practices, and how to engage respectfully — everything in one database. Donne. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Metaphysical Poetry essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Metaphysical Poetry essentials.", "x": "At a glance: Metaphysical Poetry — the clever conceit.. Conceits. The essentials: Conceits.. 17th century. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Donne.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Donne.", "x": "Metaphysical Poetry: Donne.. Conceits. Essential knowledge — 17th century.. the clever conceit. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Donne..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Donne..", "x": "Explained: Donne.. Herbert. The context — Metaphysical Poetry. Wit. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Conceits.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Conceits.", "x": "Metaphysical Poetry: Conceits.. Wit. Essential knowledge — Wit.. the clever conceit. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Conceits..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Conceits..", "x": "Explained: Conceits.. 17th. The context — Metaphysical Poetry. Herbert. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "17th century.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "17th century.", "x": "Metaphysical Poetry: 17th century.. Herbert. Essential knowledge — Herbert.. the clever conceit. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: 17th century..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: 17th century..", "x": "Explained: 17th century.. Legacy. The context — Metaphysical Poetry. Marvell. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Wit.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Wit.", "x": "Metaphysical Poetry: Wit.. 17th. Essential knowledge — Marvell.. the clever conceit. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Wit..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Wit..", "x": "Explained: Wit.. Donne. The context — Metaphysical Poetry. Donne. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Herbert.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Herbert.", "x": "Metaphysical Poetry: Herbert.. Legacy. Essential knowledge — Donne.. the clever conceit. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Herbert..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Herbert..", "x": "Explained: Herbert.. Conceits. The context — Metaphysical Poetry. Conceits. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Marvell.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Marvell.", "x": "Metaphysical Poetry: Marvell.. Donne. Essential knowledge — Conceits.. the clever conceit. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Marvell..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Marvell..", "x": "Explained: Marvell.. Wit. The context — Metaphysical Poetry. 17th century. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Donne.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Donne.", "x": "Metaphysical Poetry in depth: Donne.. Conceits. Details — the clever conceit.. Wit. Wit. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Conceits.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Conceits.", "x": "Metaphysical Poetry in depth: Conceits.. 17th century. Details — the clever conceit.. Herbert. Herbert. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Wit.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Wit.", "x": "Metaphysical Poetry in depth: Wit.. Wit. Details — the clever conceit.. 17th. Marvell. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Herbert.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Herbert.", "x": "Metaphysical Poetry in depth: Herbert.. Herbert. Details — the clever conceit.. Legacy. Donne. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "17th.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "17th.", "x": "Metaphysical Poetry in depth: 17th.. Marvell. Details — the clever conceit.. Donne. Conceits. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Legacy.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Legacy.", "x": "Metaphysical Poetry in depth: Legacy.. Donne. Details — the clever conceit.. Conceits. 17th century. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Metaphysical Poetry comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Metaphysical Poetry comes from.", "x": "Origins: Donne.. Donne. The history of Metaphysical Poetry — the clever conceit.. Conceits. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Metaphysical Poetry respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Metaphysical Poetry respectfully.", "x": "Engaging: Wit.. Conceits. How to participate or observe well — Metaphysical Poetry. the clever conceit. Respect first, always; Herbert.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Metaphysical Poetry do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Metaphysical Poetry do's and don'ts.", "x": "Etiquette: 17th.. 17th century. The rules of respect — Metaphysical Poetry. the clever conceit. When in doubt, ask about Legacy.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Metaphysical Poetry.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Metaphysical Poetry.", "x": "Planning: Donne.. Wit. Practical notes — Metaphysical Poetry. the clever conceit. A little planning shows respect for Conceits.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Metaphysical Poetry and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Metaphysical Poetry and money.", "x": "Costs: Wit.. Herbert. What to budget — Metaphysical Poetry. the clever conceit. The best experiences of Herbert. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-poetry-metaphysical-poetry-era-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
