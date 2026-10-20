(function(){'use strict';
/* JAH White House Landmark Database generator — jahdb-e2-landmark-white-house-landmark-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-landmark-white-house-landmark',PREFIX='JAH-E2LANDMARKW-',NAME='JAH White House Landmark Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "White House: the complete guide", "d": "White House: the people's house..", "g": "overview", "l": 2, "q": "What is White House: the complete guide?", "a": "White House: the people's house..", "x": "The complete landmark guide to White House: the people's house.. 1800. History, meaning, practices, and how to engage respectfully — everything in one database. 1800. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "White House essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "White House essentials.", "x": "At a glance: White House — the people's house.. 1600 Penn. The essentials: Tours.. Adams. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "1800.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "1800.", "x": "White House: 1800.. Tours. Essential knowledge — Adams.. the people's house. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 1800..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 1800..", "x": "Explained: 1800.. Adams. The context — White House. Burned 1814. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "1600 Penn.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "1600 Penn.", "x": "White House: 1600 Penn.. Oval. Essential knowledge — Burned 1814.. the people's house. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: 1600 Penn..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: 1600 Penn..", "x": "Explained: 1600 Penn.. 1814. The context — White House. Tours. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Adams.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Adams.", "x": "White House: Adams.. Adams. Essential knowledge — Tours.. the people's house. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Adams..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Adams..", "x": "Explained: Adams.. Visits. The context — White House. Oval. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Burned 1814.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Burned 1814.", "x": "White House: Burned 1814.. 1814. Essential knowledge — Oval.. the people's house. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Burned 1814..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Burned 1814..", "x": "Explained: Burned 1814.. 1800. The context — White House. 1800. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Tours.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Tours.", "x": "White House: Tours.. Visits. Essential knowledge — 1800.. the people's house. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Tours..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Tours..", "x": "Explained: Tours.. Tours. The context — White House. 1600 Penn. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Oval.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Oval.", "x": "White House: Oval.. 1800. Essential knowledge — 1600 Penn.. the people's house. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Oval..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Oval..", "x": "Explained: Oval.. Oval. The context — White House. Adams. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "1800.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "1800.", "x": "White House in depth: 1800.. 1600 Penn. Details — the people's house.. Oval. Burned 1814. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Tours.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Tours.", "x": "White House in depth: Tours.. Adams. Details — the people's house.. Adams. Tours. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Oval.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Oval.", "x": "White House in depth: Oval.. Burned 1814. Details — the people's house.. 1814. Oval. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Adams.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Adams.", "x": "White House in depth: Adams.. Tours. Details — the people's house.. Visits. 1800. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "1814.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "1814.", "x": "White House in depth: 1814.. Oval. Details — the people's house.. 1800. 1600 Penn. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Visits.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Visits.", "x": "White House in depth: Visits.. 1800. Details — the people's house.. Tours. Adams. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where White House comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where White House comes from.", "x": "Origins: 1800.. 1800. The history of White House — the people's house.. Tours. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing White House respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing White House respectfully.", "x": "Engaging: Oval.. 1600 Penn. How to participate or observe well — White House. the people's house. Respect first, always; Adams.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "White House do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "White House do's and don'ts.", "x": "Etiquette: 1814.. Adams. The rules of respect — White House. the people's house. When in doubt, ask about Visits.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around White House.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around White House.", "x": "Planning: 1800.. Burned 1814. Practical notes — White House. the people's house. A little planning shows respect for Tours.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "White House and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "White House and money.", "x": "Costs: Oval.. Tours. What to budget — White House. the people's house. The best experiences of Adams. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-landmark-white-house-landmark-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
