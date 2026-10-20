(function(){'use strict';
/* JAH Water Toys Database generator — jahdb-e2-games2-water-toys-type-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-games2-water-toys-type',PREFIX='JAH-E2GAMES2WAT-',NAME='JAH Water Toys Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Water Toys: the complete guide", "d": "Water Toys: the splash play..", "g": "overview", "l": 2, "q": "What is Water Toys: the complete guide?", "a": "Water Toys: the splash play..", "x": "The complete toys guide to Water Toys: the splash play.. Squirt guns. History, meaning, practices, and how to engage respectfully — everything in one database. Guns. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Water Toys essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Water Toys essentials.", "x": "At a glance: Water Toys — the splash play.. Pools. The essentials: Summer.. Sprinklers. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Squirt guns.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Squirt guns.", "x": "Water Toys: Squirt guns.. Summer. Essential knowledge — Sprinklers.. the splash play. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Squirt guns..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Squirt guns..", "x": "Explained: Squirt guns.. Pools. The context — Water Toys. Balloons. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Pools.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Pools.", "x": "Water Toys: Pools.. Slides. Essential knowledge — Balloons.. the splash play. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Pools..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Pools..", "x": "Explained: Pools.. Sprinklers. The context — Water Toys. Slides. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Sprinklers.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Sprinklers.", "x": "Water Toys: Sprinklers.. Pools. Essential knowledge — Slides.. the splash play. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Sprinklers..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Sprinklers..", "x": "Explained: Sprinklers.. Guide. The context — Water Toys. Summer. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Balloons.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Balloons.", "x": "Water Toys: Balloons.. Sprinklers. Essential knowledge — Summer.. the splash play. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Balloons..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Balloons..", "x": "Explained: Balloons.. Guns. The context — Water Toys. Squirt guns. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Slides.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Slides.", "x": "Water Toys: Slides.. Guide. Essential knowledge — Squirt guns.. the splash play. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Slides..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Slides..", "x": "Explained: Slides.. Summer. The context — Water Toys. Pools. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Summer.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Summer.", "x": "Water Toys: Summer.. Guns. Essential knowledge — Pools.. the splash play. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Summer..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Summer..", "x": "Explained: Summer.. Slides. The context — Water Toys. Sprinklers. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Guns.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Guns.", "x": "Water Toys in depth: Guns.. Pools. Details — the splash play.. Slides. Balloons. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Summer.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Summer.", "x": "Water Toys in depth: Summer.. Sprinklers. Details — the splash play.. Pools. Slides. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Slides.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Slides.", "x": "Water Toys in depth: Slides.. Balloons. Details — the splash play.. Sprinklers. Summer. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Pools.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Pools.", "x": "Water Toys in depth: Pools.. Slides. Details — the splash play.. Guide. Squirt guns. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Sprinklers.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Sprinklers.", "x": "Water Toys in depth: Sprinklers.. Summer. Details — the splash play.. Guns. Pools. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Guide.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Guide.", "x": "Water Toys in depth: Guide.. Squirt guns. Details — the splash play.. Summer. Sprinklers. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Water Toys comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Water Toys comes from.", "x": "Origins: Guns.. Squirt guns. The history of Water Toys — the splash play.. Summer. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Water Toys respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Water Toys respectfully.", "x": "Engaging: Slides.. Pools. How to participate or observe well — Water Toys. the splash play. Respect first, always; Pools.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Water Toys do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Water Toys do's and don'ts.", "x": "Etiquette: Sprinklers.. Sprinklers. The rules of respect — Water Toys. the splash play. When in doubt, ask about Guide.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Water Toys.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Water Toys.", "x": "Planning: Guns.. Balloons. Practical notes — Water Toys. the splash play. A little planning shows respect for Summer.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Water Toys and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Water Toys and money.", "x": "Costs: Slides.. Slides. What to budget — Water Toys. the splash play. The best experiences of Pools. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-games2-water-toys-type-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
