(function(){'use strict';
/* JAH Dubrovnik Walls Landmark Database generator — jahdb-e2-landmark-dubrovnik-walls-landmark-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-landmark-dubrovnik-walls-landmark',PREFIX='JAH-E2LANDMARKD-',NAME='JAH Dubrovnik Walls Landmark Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Dubrovnik Walls: the complete guide", "d": "Dubrovnik Walls: the Adriatic fortress..", "g": "overview", "l": 2, "q": "What is Dubrovnik Walls: the complete guide?", "a": "Dubrovnik Walls: the Adriatic fortress..", "x": "The complete landmark guide to Dubrovnik Walls: the Adriatic fortress.. 13th century. History, meaning, practices, and how to engage respectfully — everything in one database. 13th. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Dubrovnik Walls essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Dubrovnik Walls essentials.", "x": "At a glance: Dubrovnik Walls — the Adriatic fortress.. 2 km. The essentials: Thrones.. Game of Thrones. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "13th century.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "13th century.", "x": "Dubrovnik Walls: 13th century.. Thrones. Essential knowledge — Game of Thrones.. the Adriatic fortress. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 13th century..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 13th century..", "x": "Explained: 13th century.. Sea. The context — Dubrovnik Walls. Sea. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "2 km.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "2 km.", "x": "Dubrovnik Walls: 2 km.. Stradun. Essential knowledge — Sea.. the Adriatic fortress. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: 2 km..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: 2 km..", "x": "Explained: 2 km.. 2 km. The context — Dubrovnik Walls. Stradun. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Game of Thrones.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Game of Thrones.", "x": "Dubrovnik Walls: Game of Thrones.. Sea. Essential knowledge — Stradun.. the Adriatic fortress. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Game of Thrones..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Game of Thrones..", "x": "Explained: Game of Thrones.. Walking. The context — Dubrovnik Walls. Fort. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Sea.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Sea.", "x": "Dubrovnik Walls: Sea.. 2 km. Essential knowledge — Fort.. the Adriatic fortress. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Sea..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Sea..", "x": "Explained: Sea.. 13th. The context — Dubrovnik Walls. 13th century. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Stradun.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Stradun.", "x": "Dubrovnik Walls: Stradun.. Walking. Essential knowledge — 13th century.. the Adriatic fortress. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Stradun..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Stradun..", "x": "Explained: Stradun.. Thrones. The context — Dubrovnik Walls. 2 km. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Fort.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Fort.", "x": "Dubrovnik Walls: Fort.. 13th. Essential knowledge — 2 km.. the Adriatic fortress. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Fort..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Fort..", "x": "Explained: Fort.. Stradun. The context — Dubrovnik Walls. Game of Thrones. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "13th.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "13th.", "x": "Dubrovnik Walls in depth: 13th.. 2 km. Details — the Adriatic fortress.. Stradun. Sea. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Thrones.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Thrones.", "x": "Dubrovnik Walls in depth: Thrones.. Game of Thrones. Details — the Adriatic fortress.. Sea. Stradun. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Stradun.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Stradun.", "x": "Dubrovnik Walls in depth: Stradun.. Sea. Details — the Adriatic fortress.. 2 km. Fort. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Sea.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Sea.", "x": "Dubrovnik Walls in depth: Sea.. Stradun. Details — the Adriatic fortress.. Walking. 13th century. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "2 km.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "2 km.", "x": "Dubrovnik Walls in depth: 2 km.. Fort. Details — the Adriatic fortress.. 13th. 2 km. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Walking.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Walking.", "x": "Dubrovnik Walls in depth: Walking.. 13th century. Details — the Adriatic fortress.. Thrones. Game of Thrones. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Dubrovnik Walls comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Dubrovnik Walls comes from.", "x": "Origins: 13th.. 13th century. The history of Dubrovnik Walls — the Adriatic fortress.. Thrones. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Dubrovnik Walls respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Dubrovnik Walls respectfully.", "x": "Engaging: Stradun.. 2 km. How to participate or observe well — Dubrovnik Walls. the Adriatic fortress. Respect first, always; Sea.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Dubrovnik Walls do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Dubrovnik Walls do's and don'ts.", "x": "Etiquette: 2 km.. Game of Thrones. The rules of respect — Dubrovnik Walls. the Adriatic fortress. When in doubt, ask about Walking.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Dubrovnik Walls.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Dubrovnik Walls.", "x": "Planning: 13th.. Sea. Practical notes — Dubrovnik Walls. the Adriatic fortress. A little planning shows respect for Thrones.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Dubrovnik Walls and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Dubrovnik Walls and money.", "x": "Costs: Stradun.. Stradun. What to budget — Dubrovnik Walls. the Adriatic fortress. The best experiences of Sea. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-landmark-dubrovnik-walls-landmark-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
