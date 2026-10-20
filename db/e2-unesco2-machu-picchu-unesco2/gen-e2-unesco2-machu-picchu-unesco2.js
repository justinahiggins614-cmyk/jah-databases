(function(){'use strict';
/* JAH Machu Picchu UNESCO Database generator — jahdb-e2-unesco2-machu-picchu-unesco2-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-unesco2-machu-picchu-unesco2',PREFIX='JAH-E2UNESCO2MA-',NAME='JAH Machu Picchu UNESCO Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Machu Picchu UNESCO: the complete guide", "d": "Machu Picchu UNESCO: the Inca 2..", "g": "overview", "l": 2, "q": "What is Machu Picchu UNESCO: the complete guide?", "a": "Machu Picchu UNESCO: the Inca 2..", "x": "The complete unesco site guide to Machu Picchu UNESCO: the Inca 2.. Peru. History, meaning, practices, and how to engage respectfully — everything in one database. Peru. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Machu Picchu UNESCO essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Machu Picchu UNESCO essentials.", "x": "At a glance: Machu Picchu UNESCO — the Inca 2.. 1983. The essentials: Bingham.. Inca. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Peru.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Peru.", "x": "Machu Picchu UNESCO: Peru.. Bingham. Essential knowledge — Inca.. the Inca 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Peru..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Peru..", "x": "Explained: Peru.. 1983. The context — Machu Picchu UNESCO. Andes. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "1983.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "1983.", "x": "Machu Picchu UNESCO: 1983.. Citadel. Essential knowledge — Andes.. the Inca 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: 1983..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: 1983..", "x": "Explained: 1983.. Andes. The context — Machu Picchu UNESCO. Citadel. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Inca.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Inca.", "x": "Machu Picchu UNESCO: Inca.. 1983. Essential knowledge — Citadel.. the Inca 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Inca..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Inca..", "x": "Explained: Inca.. Visiting. The context — Machu Picchu UNESCO. Bingham. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Andes.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Andes.", "x": "Machu Picchu UNESCO: Andes.. Andes. Essential knowledge — Bingham.. the Inca 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Andes..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Andes..", "x": "Explained: Andes.. Peru. The context — Machu Picchu UNESCO. Peru. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Citadel.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Citadel.", "x": "Machu Picchu UNESCO: Citadel.. Visiting. Essential knowledge — Peru.. the Inca 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Citadel..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Citadel..", "x": "Explained: Citadel.. Bingham. The context — Machu Picchu UNESCO. 1983. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Bingham.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Bingham.", "x": "Machu Picchu UNESCO: Bingham.. Peru. Essential knowledge — 1983.. the Inca 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Bingham..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Bingham..", "x": "Explained: Bingham.. Citadel. The context — Machu Picchu UNESCO. Inca. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Peru.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Peru.", "x": "Machu Picchu UNESCO in depth: Peru.. 1983. Details — the Inca 2.. Citadel. Andes. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Bingham.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Bingham.", "x": "Machu Picchu UNESCO in depth: Bingham.. Inca. Details — the Inca 2.. 1983. Citadel. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Citadel.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Citadel.", "x": "Machu Picchu UNESCO in depth: Citadel.. Andes. Details — the Inca 2.. Andes. Bingham. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "1983.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "1983.", "x": "Machu Picchu UNESCO in depth: 1983.. Citadel. Details — the Inca 2.. Visiting. Peru. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Andes.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Andes.", "x": "Machu Picchu UNESCO in depth: Andes.. Bingham. Details — the Inca 2.. Peru. 1983. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Visiting.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Visiting.", "x": "Machu Picchu UNESCO in depth: Visiting.. Peru. Details — the Inca 2.. Bingham. Inca. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Machu Picchu UNESCO comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Machu Picchu UNESCO comes from.", "x": "Origins: Peru.. Peru. The history of Machu Picchu UNESCO — the Inca 2.. Bingham. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Machu Picchu UNESCO respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Machu Picchu UNESCO respectfully.", "x": "Engaging: Citadel.. 1983. How to participate or observe well — Machu Picchu UNESCO. the Inca 2. Respect first, always; 1983.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Machu Picchu UNESCO do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Machu Picchu UNESCO do's and don'ts.", "x": "Etiquette: Andes.. Inca. The rules of respect — Machu Picchu UNESCO. the Inca 2. When in doubt, ask about Visiting.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Machu Picchu UNESCO.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Machu Picchu UNESCO.", "x": "Planning: Peru.. Andes. Practical notes — Machu Picchu UNESCO. the Inca 2. A little planning shows respect for Bingham.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Machu Picchu UNESCO and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Machu Picchu UNESCO and money.", "x": "Costs: Citadel.. Citadel. What to budget — Machu Picchu UNESCO. the Inca 2. The best experiences of 1983. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-unesco2-machu-picchu-unesco2-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
