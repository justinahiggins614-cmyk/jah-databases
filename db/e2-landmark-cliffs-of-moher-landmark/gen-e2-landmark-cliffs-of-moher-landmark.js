(function(){'use strict';
/* JAH Cliffs of Moher Landmark Database generator — jahdb-e2-landmark-cliffs-of-moher-landmark-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-landmark-cliffs-of-moher-landmark',PREFIX='JAH-E2LANDMARKC-',NAME='JAH Cliffs of Moher Landmark Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Cliffs of Moher: the complete guide", "d": "Cliffs of Moher: the 214m cliffs..", "g": "overview", "l": 2, "q": "What is Cliffs of Moher: the complete guide?", "a": "Cliffs of Moher: the 214m cliffs..", "x": "The complete landmark guide to Cliffs of Moher: the 214m cliffs.. 214m. History, meaning, practices, and how to engage respectfully — everything in one database. 214m. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Cliffs of Moher essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Cliffs of Moher essentials.", "x": "At a glance: Cliffs of Moher — the 214m cliffs.. 8 km. The essentials: Puffins.. Puffins. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "214m.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "214m.", "x": "Cliffs of Moher: 214m.. Puffins. Essential knowledge — Puffins.. the 214m cliffs. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 214m..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 214m..", "x": "Explained: 214m.. Atlantic. The context — Cliffs of Moher. Atlantic. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "8 km.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "8 km.", "x": "Cliffs of Moher: 8 km.. Views. Essential knowledge — Atlantic.. the 214m cliffs. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: 8 km..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: 8 km..", "x": "Explained: 8 km.. O'Brien's. The context — Cliffs of Moher. O'Brien's. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Puffins.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Puffins.", "x": "Cliffs of Moher: Puffins.. Atlantic. Essential knowledge — O'Brien's.. the 214m cliffs. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Puffins..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Puffins..", "x": "Explained: Puffins.. Walking. The context — Cliffs of Moher. Views. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Atlantic.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Atlantic.", "x": "Cliffs of Moher: Atlantic.. O'Brien's. Essential knowledge — Views.. the 214m cliffs. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Atlantic..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Atlantic..", "x": "Explained: Atlantic.. 214m. The context — Cliffs of Moher. 214m. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "O'Brien's.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "O'Brien's.", "x": "Cliffs of Moher: O'Brien's.. Walking. Essential knowledge — 214m.. the 214m cliffs. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: O'Brien's..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: O'Brien's..", "x": "Explained: O'Brien's.. Puffins. The context — Cliffs of Moher. 8 km. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Views.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Views.", "x": "Cliffs of Moher: Views.. 214m. Essential knowledge — 8 km.. the 214m cliffs. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Views..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Views..", "x": "Explained: Views.. Views. The context — Cliffs of Moher. Puffins. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "214m.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "214m.", "x": "Cliffs of Moher in depth: 214m.. 8 km. Details — the 214m cliffs.. Views. Atlantic. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Puffins.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Puffins.", "x": "Cliffs of Moher in depth: Puffins.. Puffins. Details — the 214m cliffs.. Atlantic. O'Brien's. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Views.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Views.", "x": "Cliffs of Moher in depth: Views.. Atlantic. Details — the 214m cliffs.. O'Brien's. Views. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Atlantic.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Atlantic.", "x": "Cliffs of Moher in depth: Atlantic.. O'Brien's. Details — the 214m cliffs.. Walking. 214m. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "O'Brien's.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "O'Brien's.", "x": "Cliffs of Moher in depth: O'Brien's.. Views. Details — the 214m cliffs.. 214m. 8 km. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Walking.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Walking.", "x": "Cliffs of Moher in depth: Walking.. 214m. Details — the 214m cliffs.. Puffins. Puffins. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Cliffs of Moher comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Cliffs of Moher comes from.", "x": "Origins: 214m.. 214m. The history of Cliffs of Moher — the 214m cliffs.. Puffins. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Cliffs of Moher respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Cliffs of Moher respectfully.", "x": "Engaging: Views.. 8 km. How to participate or observe well — Cliffs of Moher. the 214m cliffs. Respect first, always; Atlantic.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Cliffs of Moher do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Cliffs of Moher do's and don'ts.", "x": "Etiquette: O'Brien's.. Puffins. The rules of respect — Cliffs of Moher. the 214m cliffs. When in doubt, ask about Walking.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Cliffs of Moher.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Cliffs of Moher.", "x": "Planning: 214m.. Atlantic. Practical notes — Cliffs of Moher. the 214m cliffs. A little planning shows respect for Puffins.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Cliffs of Moher and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Cliffs of Moher and money.", "x": "Costs: Views.. O'Brien's. What to budget — Cliffs of Moher. the 214m cliffs. The best experiences of Atlantic. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-landmark-cliffs-of-moher-landmark-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
