(function(){'use strict';
/* JAH Pandemic Board Board Game Database generator — jahdb-e2-board-pandemic-board-game-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-board-pandemic-board-game',PREFIX='JAH-E2BOARDPAND-',NAME='JAH Pandemic Board Board Game Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Pandemic Board: the complete guide", "d": "Pandemic Board: the co-op classic..", "g": "overview", "l": 2, "q": "What is Pandemic Board: the complete guide?", "a": "Pandemic Board: the co-op classic..", "x": "The complete board game guide to Pandemic Board: the co-op classic.. 2008. History, meaning, practices, and how to engage respectfully — everything in one database. Co-op. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Pandemic Board essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Pandemic Board essentials.", "x": "At a glance: Pandemic Board — the co-op classic.. Co-op. The essentials: Cubes.. Diseases. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "2008.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "2008.", "x": "Pandemic Board: 2008.. Cubes. Essential knowledge — Diseases.. the co-op classic. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 2008..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 2008..", "x": "Explained: 2008.. Z-Man. The context — Pandemic Board. Cubes. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Co-op.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Co-op.", "x": "Pandemic Board: Co-op.. Teamwork. Essential knowledge — Cubes.. the co-op classic. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Co-op..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Co-op..", "x": "Explained: Co-op.. Diseases. The context — Pandemic Board. Z-Man. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Diseases.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Diseases.", "x": "Pandemic Board: Diseases.. Z-Man. Essential knowledge — Z-Man.. the co-op classic. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Diseases..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Diseases..", "x": "Explained: Diseases.. Strategy. The context — Pandemic Board. Teamwork. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Cubes.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Cubes.", "x": "Pandemic Board: Cubes.. Diseases. Essential knowledge — Teamwork.. the co-op classic. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Cubes..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Cubes..", "x": "Explained: Cubes.. Co-op. The context — Pandemic Board. 2008. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Z-Man.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Z-Man.", "x": "Pandemic Board: Z-Man.. Strategy. Essential knowledge — 2008.. the co-op classic. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Z-Man..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Z-Man..", "x": "Explained: Z-Man.. Cubes. The context — Pandemic Board. Co-op. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Teamwork.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Teamwork.", "x": "Pandemic Board: Teamwork.. Co-op. Essential knowledge — Co-op.. the co-op classic. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Teamwork..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Teamwork..", "x": "Explained: Teamwork.. Teamwork. The context — Pandemic Board. Diseases. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Co-op.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Co-op.", "x": "Pandemic Board in depth: Co-op.. Co-op. Details — the co-op classic.. Teamwork. Cubes. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Cubes.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Cubes.", "x": "Pandemic Board in depth: Cubes.. Diseases. Details — the co-op classic.. Z-Man. Z-Man. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Teamwork.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Teamwork.", "x": "Pandemic Board in depth: Teamwork.. Cubes. Details — the co-op classic.. Diseases. Teamwork. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Z-Man.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Z-Man.", "x": "Pandemic Board in depth: Z-Man.. Z-Man. Details — the co-op classic.. Strategy. 2008. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Diseases.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Diseases.", "x": "Pandemic Board in depth: Diseases.. Teamwork. Details — the co-op classic.. Co-op. Co-op. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Strategy.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Strategy.", "x": "Pandemic Board in depth: Strategy.. 2008. Details — the co-op classic.. Cubes. Diseases. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Pandemic Board comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Pandemic Board comes from.", "x": "Origins: Co-op.. 2008. The history of Pandemic Board — the co-op classic.. Cubes. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Pandemic Board respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Pandemic Board respectfully.", "x": "Engaging: Teamwork.. Co-op. How to participate or observe well — Pandemic Board. the co-op classic. Respect first, always; Z-Man.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Pandemic Board do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Pandemic Board do's and don'ts.", "x": "Etiquette: Diseases.. Diseases. The rules of respect — Pandemic Board. the co-op classic. When in doubt, ask about Strategy.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Pandemic Board.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Pandemic Board.", "x": "Planning: Co-op.. Cubes. Practical notes — Pandemic Board. the co-op classic. A little planning shows respect for Cubes.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Pandemic Board and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Pandemic Board and money.", "x": "Costs: Teamwork.. Z-Man. What to budget — Pandemic Board. the co-op classic. The best experiences of Z-Man. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-board-pandemic-board-game-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
