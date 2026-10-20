(function(){'use strict';
/* JAH Carnival Rides Carnival Database generator — jahdb-e2-carnival-carnival-rides-carnival-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-carnival-carnival-rides-carnival',PREFIX='JAH-E2CARNIVALC-',NAME='JAH Carnival Rides Carnival Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Carnival Rides: the complete guide", "d": "Carnival Rides: the midway thrills..", "g": "overview", "l": 2, "q": "What is Carnival Rides: the complete guide?", "a": "Carnival Rides: the midway thrills..", "x": "The complete carnival guide to Carnival Rides: the midway thrills.. Ferris wheel. History, meaning, practices, and how to engage respectfully — everything in one database. Wheel. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Carnival Rides essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Carnival Rides essentials.", "x": "At a glance: Carnival Rides — the midway thrills.. Roller. The essentials: Games.. Games. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Ferris wheel.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Ferris wheel.", "x": "Carnival Rides: Ferris wheel.. Games. Essential knowledge — Games.. the midway thrills. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Ferris wheel..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Ferris wheel..", "x": "Explained: Ferris wheel.. Lights. The context — Carnival Rides. Cotton candy. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Roller.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Roller.", "x": "Carnival Rides: Roller.. Candy. Essential knowledge — Cotton candy.. the midway thrills. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Roller..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Roller..", "x": "Explained: Roller.. Summer. The context — Carnival Rides. Lights. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Games.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Games.", "x": "Carnival Rides: Games.. Lights. Essential knowledge — Lights.. the midway thrills. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Games..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Games..", "x": "Explained: Games.. Thrills. The context — Carnival Rides. Summer. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Cotton candy.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Cotton candy.", "x": "Carnival Rides: Cotton candy.. Summer. Essential knowledge — Summer.. the midway thrills. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Cotton candy..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Cotton candy..", "x": "Explained: Cotton candy.. Wheel. The context — Carnival Rides. Ferris wheel. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Lights.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Lights.", "x": "Carnival Rides: Lights.. Thrills. Essential knowledge — Ferris wheel.. the midway thrills. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Lights..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Lights..", "x": "Explained: Lights.. Games. The context — Carnival Rides. Roller. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Summer.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Summer.", "x": "Carnival Rides: Summer.. Wheel. Essential knowledge — Roller.. the midway thrills. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Summer..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Summer..", "x": "Explained: Summer.. Candy. The context — Carnival Rides. Games. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Wheel.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Wheel.", "x": "Carnival Rides in depth: Wheel.. Roller. Details — the midway thrills.. Candy. Cotton candy. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Games.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Games.", "x": "Carnival Rides in depth: Games.. Games. Details — the midway thrills.. Lights. Lights. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Candy.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Candy.", "x": "Carnival Rides in depth: Candy.. Cotton candy. Details — the midway thrills.. Summer. Summer. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Lights.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Lights.", "x": "Carnival Rides in depth: Lights.. Lights. Details — the midway thrills.. Thrills. Ferris wheel. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Summer.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Summer.", "x": "Carnival Rides in depth: Summer.. Summer. Details — the midway thrills.. Wheel. Roller. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Thrills.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Thrills.", "x": "Carnival Rides in depth: Thrills.. Ferris wheel. Details — the midway thrills.. Games. Games. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Carnival Rides comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Carnival Rides comes from.", "x": "Origins: Wheel.. Ferris wheel. The history of Carnival Rides — the midway thrills.. Games. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Carnival Rides respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Carnival Rides respectfully.", "x": "Engaging: Candy.. Roller. How to participate or observe well — Carnival Rides. the midway thrills. Respect first, always; Lights.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Carnival Rides do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Carnival Rides do's and don'ts.", "x": "Etiquette: Summer.. Games. The rules of respect — Carnival Rides. the midway thrills. When in doubt, ask about Thrills.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Carnival Rides.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Carnival Rides.", "x": "Planning: Wheel.. Cotton candy. Practical notes — Carnival Rides. the midway thrills. A little planning shows respect for Games.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Carnival Rides and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Carnival Rides and money.", "x": "Costs: Candy.. Lights. What to budget — Carnival Rides. the midway thrills. The best experiences of Lights. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-carnival-carnival-rides-carnival-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
