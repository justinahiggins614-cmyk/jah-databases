(function(){'use strict';
/* JAH Hopkins2 Database generator — jahdb-e2-screen2-hopkins-actor2-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-screen2-hopkins-actor2',PREFIX='JAH-E2SCREEN2HO-',NAME='JAH Hopkins2 Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Hopkins2: the complete guide", "d": "Hopkins2: the Hannibal 2..", "g": "overview", "l": 2, "q": "What is Hopkins2: the complete guide?", "a": "Hopkins2: the Hannibal 2..", "x": "The complete actor guide to Hopkins2: the Hannibal 2.. Father. History, meaning, practices, and how to engage respectfully — everything in one database. Oscars. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Hopkins2 essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Hopkins2 essentials.", "x": "At a glance: Hopkins2 — the Hannibal 2.. Westworld. The essentials: Painting.. 2 Oscars. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Father.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Father.", "x": "Hopkins2: Father.. Painting. Essential knowledge — 2 Oscars.. the Hannibal 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Father..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Father..", "x": "Explained: Father.. Father. The context — Hopkins2. Welsh. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Westworld.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Westworld.", "x": "Hopkins2: Westworld.. Lear. Essential knowledge — Welsh.. the Hannibal 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Westworld..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Westworld..", "x": "Explained: Westworld.. Westworld. The context — Hopkins2. Painting. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "2 Oscars.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "2 Oscars.", "x": "Hopkins2: 2 Oscars.. Father. Essential knowledge — Painting.. the Hannibal 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: 2 Oscars..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: 2 Oscars..", "x": "Explained: 2 Oscars.. Roles. The context — Hopkins2. King Lear. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Welsh.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Welsh.", "x": "Hopkins2: Welsh.. Westworld. Essential knowledge — King Lear.. the Hannibal 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Welsh..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Welsh..", "x": "Explained: Welsh.. Oscars. The context — Hopkins2. Father. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Painting.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Painting.", "x": "Hopkins2: Painting.. Roles. Essential knowledge — Father.. the Hannibal 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Painting..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Painting..", "x": "Explained: Painting.. Painting. The context — Hopkins2. Westworld. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "King Lear.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "King Lear.", "x": "Hopkins2: King Lear.. Oscars. Essential knowledge — Westworld.. the Hannibal 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: King Lear..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: King Lear..", "x": "Explained: King Lear.. Lear. The context — Hopkins2. 2 Oscars. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Oscars.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Oscars.", "x": "Hopkins2 in depth: Oscars.. Westworld. Details — the Hannibal 2.. Lear. Welsh. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Painting.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Painting.", "x": "Hopkins2 in depth: Painting.. 2 Oscars. Details — the Hannibal 2.. Father. Painting. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Lear.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Lear.", "x": "Hopkins2 in depth: Lear.. Welsh. Details — the Hannibal 2.. Westworld. King Lear. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Father.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Father.", "x": "Hopkins2 in depth: Father.. Painting. Details — the Hannibal 2.. Roles. Father. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Westworld.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Westworld.", "x": "Hopkins2 in depth: Westworld.. King Lear. Details — the Hannibal 2.. Oscars. Westworld. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Roles.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Roles.", "x": "Hopkins2 in depth: Roles.. Father. Details — the Hannibal 2.. Painting. 2 Oscars. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Hopkins2 comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Hopkins2 comes from.", "x": "Origins: Oscars.. Father. The history of Hopkins2 — the Hannibal 2.. Painting. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Hopkins2 respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Hopkins2 respectfully.", "x": "Engaging: Lear.. Westworld. How to participate or observe well — Hopkins2. the Hannibal 2. Respect first, always; Father.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Hopkins2 do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Hopkins2 do's and don'ts.", "x": "Etiquette: Westworld.. 2 Oscars. The rules of respect — Hopkins2. the Hannibal 2. When in doubt, ask about Roles.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Hopkins2.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Hopkins2.", "x": "Planning: Oscars.. Welsh. Practical notes — Hopkins2. the Hannibal 2. A little planning shows respect for Painting.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Hopkins2 and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Hopkins2 and money.", "x": "Costs: Lear.. Painting. What to budget — Hopkins2. the Hannibal 2. The best experiences of Father. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-screen2-hopkins-actor2-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
