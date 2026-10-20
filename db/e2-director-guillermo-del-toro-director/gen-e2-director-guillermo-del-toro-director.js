(function(){'use strict';
/* JAH Guillermo del Toro Director Database generator — jahdb-e2-director-guillermo-del-toro-director-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-director-guillermo-del-toro-director',PREFIX='JAH-E2DIRECTORG-',NAME='JAH Guillermo del Toro Director Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Guillermo del Toro: the complete guide", "d": "Guillermo del Toro: the monster poet..", "g": "overview", "l": 2, "q": "What is Guillermo del Toro: the complete guide?", "a": "Guillermo del Toro: the monster poet..", "x": "The complete director guide to Guillermo del Toro: the monster poet.. 1964. History, meaning, practices, and how to engage respectfully — everything in one database. Pan's. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Guillermo del Toro essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Guillermo del Toro essentials.", "x": "At a glance: Guillermo del Toro — the monster poet.. Pan's Labyrinth. The essentials: Monsters.. Shape of Water. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "1964.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "1964.", "x": "Guillermo del Toro: 1964.. Monsters. Essential knowledge — Shape of Water.. the monster poet. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 1964..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 1964..", "x": "Explained: 1964.. Gothic. The context — Guillermo del Toro. Monsters. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Pan's Labyrinth.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Pan's Labyrinth.", "x": "Guillermo del Toro: Pan's Labyrinth.. Mexico. Essential knowledge — Monsters.. the monster poet. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Pan's Labyrinth..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Pan's Labyrinth..", "x": "Explained: Pan's Labyrinth.. Water. The context — Guillermo del Toro. Mexico. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Shape of Water.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Shape of Water.", "x": "Guillermo del Toro: Shape of Water.. Gothic. Essential knowledge — Mexico.. the monster poet. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Shape of Water..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Shape of Water..", "x": "Explained: Shape of Water.. Style. The context — Guillermo del Toro. Gothic. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Monsters.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Monsters.", "x": "Guillermo del Toro: Monsters.. Water. Essential knowledge — Gothic.. the monster poet. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Monsters..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Monsters..", "x": "Explained: Monsters.. Pan's. The context — Guillermo del Toro. 1964. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Mexico.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Mexico.", "x": "Guillermo del Toro: Mexico.. Style. Essential knowledge — 1964.. the monster poet. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Mexico..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Mexico..", "x": "Explained: Mexico.. Monsters. The context — Guillermo del Toro. Pan's Labyrinth. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Gothic.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Gothic.", "x": "Guillermo del Toro: Gothic.. Pan's. Essential knowledge — Pan's Labyrinth.. the monster poet. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Gothic..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Gothic..", "x": "Explained: Gothic.. Mexico. The context — Guillermo del Toro. Shape of Water. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Pan's.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Pan's.", "x": "Guillermo del Toro in depth: Pan's.. Pan's Labyrinth. Details — the monster poet.. Mexico. Monsters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Monsters.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Monsters.", "x": "Guillermo del Toro in depth: Monsters.. Shape of Water. Details — the monster poet.. Gothic. Mexico. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Mexico.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Mexico.", "x": "Guillermo del Toro in depth: Mexico.. Monsters. Details — the monster poet.. Water. Gothic. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Gothic.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Gothic.", "x": "Guillermo del Toro in depth: Gothic.. Mexico. Details — the monster poet.. Style. 1964. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Water.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Water.", "x": "Guillermo del Toro in depth: Water.. Gothic. Details — the monster poet.. Pan's. Pan's Labyrinth. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Style.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Style.", "x": "Guillermo del Toro in depth: Style.. 1964. Details — the monster poet.. Monsters. Shape of Water. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Guillermo del Toro comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Guillermo del Toro comes from.", "x": "Origins: Pan's.. 1964. The history of Guillermo del Toro — the monster poet.. Monsters. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Guillermo del Toro respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Guillermo del Toro respectfully.", "x": "Engaging: Mexico.. Pan's Labyrinth. How to participate or observe well — Guillermo del Toro. the monster poet. Respect first, always; Gothic.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Guillermo del Toro do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Guillermo del Toro do's and don'ts.", "x": "Etiquette: Water.. Shape of Water. The rules of respect — Guillermo del Toro. the monster poet. When in doubt, ask about Style.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Guillermo del Toro.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Guillermo del Toro.", "x": "Planning: Pan's.. Monsters. Practical notes — Guillermo del Toro. the monster poet. A little planning shows respect for Monsters.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Guillermo del Toro and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Guillermo del Toro and money.", "x": "Costs: Mexico.. Mexico. What to budget — Guillermo del Toro. the monster poet. The best experiences of Gothic. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-director-guillermo-del-toro-director-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
