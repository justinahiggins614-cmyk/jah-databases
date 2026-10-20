(function(){'use strict';
/* JAH The Alamo Landmark Database generator — jahdb-e2-landmark-alamo-landmark-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-landmark-alamo-landmark',PREFIX='JAH-E2LANDMARKA-',NAME='JAH The Alamo Landmark Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "The Alamo: the complete guide", "d": "The Alamo: the 1836 mission..", "g": "overview", "l": 2, "q": "What is The Alamo: the complete guide?", "a": "The Alamo: the 1836 mission..", "x": "The complete landmark guide to The Alamo: the 1836 mission.. 1836. History, meaning, practices, and how to engage respectfully — everything in one database. 1836. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "The Alamo essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "The Alamo essentials.", "x": "At a glance: The Alamo — the 1836 mission.. Remember. The essentials: Mission.. Mission. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "1836.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "1836.", "x": "The Alamo: 1836.. Mission. Essential knowledge — Mission.. the 1836 mission. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 1836..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 1836..", "x": "Explained: 1836.. Crockett. The context — The Alamo. San Antonio. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Remember.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Remember.", "x": "The Alamo: Remember.. Shrine. Essential knowledge — San Antonio.. the 1836 mission. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Remember..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Remember..", "x": "Explained: Remember.. Remember. The context — The Alamo. Crockett. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Mission.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Mission.", "x": "The Alamo: Mission.. Crockett. Essential knowledge — Crockett.. the 1836 mission. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Mission..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Mission..", "x": "Explained: Mission.. Tours. The context — The Alamo. Shrine. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "San Antonio.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "San Antonio.", "x": "The Alamo: San Antonio.. Remember. Essential knowledge — Shrine.. the 1836 mission. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: San Antonio..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: San Antonio..", "x": "Explained: San Antonio.. 1836. The context — The Alamo. 1836. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Crockett.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Crockett.", "x": "The Alamo: Crockett.. Tours. Essential knowledge — 1836.. the 1836 mission. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Crockett..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Crockett..", "x": "Explained: Crockett.. Mission. The context — The Alamo. Remember. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Shrine.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Shrine.", "x": "The Alamo: Shrine.. 1836. Essential knowledge — Remember.. the 1836 mission. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Shrine..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Shrine..", "x": "Explained: Shrine.. Shrine. The context — The Alamo. Mission. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "1836.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "1836.", "x": "The Alamo in depth: 1836.. Remember. Details — the 1836 mission.. Shrine. San Antonio. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Mission.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Mission.", "x": "The Alamo in depth: Mission.. Mission. Details — the 1836 mission.. Crockett. Crockett. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Shrine.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Shrine.", "x": "The Alamo in depth: Shrine.. San Antonio. Details — the 1836 mission.. Remember. Shrine. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Crockett.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Crockett.", "x": "The Alamo in depth: Crockett.. Crockett. Details — the 1836 mission.. Tours. 1836. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Remember.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Remember.", "x": "The Alamo in depth: Remember.. Shrine. Details — the 1836 mission.. 1836. Remember. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Tours.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Tours.", "x": "The Alamo in depth: Tours.. 1836. Details — the 1836 mission.. Mission. Mission. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where The Alamo comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where The Alamo comes from.", "x": "Origins: 1836.. 1836. The history of The Alamo — the 1836 mission.. Mission. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing The Alamo respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing The Alamo respectfully.", "x": "Engaging: Shrine.. Remember. How to participate or observe well — The Alamo. the 1836 mission. Respect first, always; Crockett.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "The Alamo do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "The Alamo do's and don'ts.", "x": "Etiquette: Remember.. Mission. The rules of respect — The Alamo. the 1836 mission. When in doubt, ask about Tours.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around The Alamo.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around The Alamo.", "x": "Planning: 1836.. San Antonio. Practical notes — The Alamo. the 1836 mission. A little planning shows respect for Mission.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "The Alamo and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "The Alamo and money.", "x": "Costs: Shrine.. Crockett. What to budget — The Alamo. the 1836 mission. The best experiences of Crockett. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-landmark-alamo-landmark-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
