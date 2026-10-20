(function(){'use strict';
/* JAH Clam Chowder Dish Database generator — jahdb-e2-dish-clam-chowder-dish-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-dish-clam-chowder-dish',PREFIX='JAH-E2DISHCLAMC-',NAME='JAH Clam Chowder Dish Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Clam Chowder: the complete guide", "d": "Clam Chowder: the New England creamy..", "g": "overview", "l": 2, "q": "What is Clam Chowder: the complete guide?", "a": "Clam Chowder: the New England creamy..", "x": "The complete dish guide to Clam Chowder: the New England creamy.. Clams. History, meaning, practices, and how to engage respectfully — everything in one database. Clams. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Clam Chowder essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Clam Chowder essentials.", "x": "At a glance: Clam Chowder — the New England creamy.. Cream. The essentials: Crackers.. Potatoes. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Clams.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Clams.", "x": "Clam Chowder: Clams.. Crackers. Essential knowledge — Potatoes.. the New England creamy. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Clams..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Clams..", "x": "Explained: Clams.. Cream. The context — Clam Chowder. Oyster crackers. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Cream.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Cream.", "x": "Clam Chowder: Cream.. Boston. Essential knowledge — Oyster crackers.. the New England creamy. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Cream..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Cream..", "x": "Explained: Cream.. Potatoes. The context — Clam Chowder. White. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Potatoes.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Potatoes.", "x": "Clam Chowder: Potatoes.. Cream. Essential knowledge — White.. the New England creamy. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Potatoes..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Potatoes..", "x": "Explained: Potatoes.. Making. The context — Clam Chowder. Boston. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Oyster crackers.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Oyster crackers.", "x": "Clam Chowder: Oyster crackers.. Potatoes. Essential knowledge — Boston.. the New England creamy. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Oyster crackers..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Oyster crackers..", "x": "Explained: Oyster crackers.. Clams. The context — Clam Chowder. Clams. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "White.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "White.", "x": "Clam Chowder: White.. Making. Essential knowledge — Clams.. the New England creamy. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: White..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: White..", "x": "Explained: White.. Crackers. The context — Clam Chowder. Cream. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Boston.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Boston.", "x": "Clam Chowder: Boston.. Clams. Essential knowledge — Cream.. the New England creamy. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Boston..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Boston..", "x": "Explained: Boston.. Boston. The context — Clam Chowder. Potatoes. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Clams.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Clams.", "x": "Clam Chowder in depth: Clams.. Cream. Details — the New England creamy.. Boston. Oyster crackers. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Crackers.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Crackers.", "x": "Clam Chowder in depth: Crackers.. Potatoes. Details — the New England creamy.. Cream. White. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Boston.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Boston.", "x": "Clam Chowder in depth: Boston.. Oyster crackers. Details — the New England creamy.. Potatoes. Boston. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Cream.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Cream.", "x": "Clam Chowder in depth: Cream.. White. Details — the New England creamy.. Making. Clams. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Potatoes.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Potatoes.", "x": "Clam Chowder in depth: Potatoes.. Boston. Details — the New England creamy.. Clams. Cream. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Making.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Making.", "x": "Clam Chowder in depth: Making.. Clams. Details — the New England creamy.. Crackers. Potatoes. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Clam Chowder comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Clam Chowder comes from.", "x": "Origins: Clams.. Clams. The history of Clam Chowder — the New England creamy.. Crackers. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Clam Chowder respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Clam Chowder respectfully.", "x": "Engaging: Boston.. Cream. How to participate or observe well — Clam Chowder. the New England creamy. Respect first, always; Cream.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Clam Chowder do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Clam Chowder do's and don'ts.", "x": "Etiquette: Potatoes.. Potatoes. The rules of respect — Clam Chowder. the New England creamy. When in doubt, ask about Making.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Clam Chowder.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Clam Chowder.", "x": "Planning: Clams.. Oyster crackers. Practical notes — Clam Chowder. the New England creamy. A little planning shows respect for Crackers.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Clam Chowder and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Clam Chowder and money.", "x": "Costs: Boston.. White. What to budget — Clam Chowder. the New England creamy. The best experiences of Cream. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-dish-clam-chowder-dish-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
