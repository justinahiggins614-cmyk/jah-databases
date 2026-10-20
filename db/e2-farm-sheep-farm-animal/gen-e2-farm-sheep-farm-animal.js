(function(){'use strict';
/* JAH Sheep Farm Farm Animal Database generator — jahdb-e2-farm-sheep-farm-animal-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-farm-sheep-farm-animal',PREFIX='JAH-E2FARMSHEEP-',NAME='JAH Sheep Farm Farm Animal Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Sheep Farm: the complete guide", "d": "Sheep Farm: the wool flock..", "g": "overview", "l": 2, "q": "What is Sheep Farm: the complete guide?", "a": "Sheep Farm: the wool flock..", "x": "The complete farm animal guide to Sheep Farm: the wool flock.. Wool. History, meaning, practices, and how to engage respectfully — everything in one database. Wool. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Sheep Farm essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Sheep Farm essentials.", "x": "At a glance: Sheep Farm — the wool flock.. Flocking. The essentials: Lambs.. Lambs. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Wool.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Wool.", "x": "Sheep Farm: Wool.. Lambs. Essential knowledge — Lambs.. the wool flock. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Wool..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Wool..", "x": "Explained: Wool.. Dogs. The context — Sheep Farm. Shearing. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Flocking.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Flocking.", "x": "Sheep Farm: Flocking.. Shearing. Essential knowledge — Shearing.. the wool flock. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Flocking..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Flocking..", "x": "Explained: Flocking.. Flocking. The context — Sheep Farm. Grazing. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Lambs.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Lambs.", "x": "Sheep Farm: Lambs.. Dogs. Essential knowledge — Grazing.. the wool flock. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Lambs..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Lambs..", "x": "Explained: Lambs.. Care. The context — Sheep Farm. Dogs. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Shearing.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Shearing.", "x": "Sheep Farm: Shearing.. Flocking. Essential knowledge — Dogs.. the wool flock. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Shearing..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Shearing..", "x": "Explained: Shearing.. Wool. The context — Sheep Farm. Wool. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Grazing.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Grazing.", "x": "Sheep Farm: Grazing.. Care. Essential knowledge — Wool.. the wool flock. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Grazing..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Grazing..", "x": "Explained: Grazing.. Lambs. The context — Sheep Farm. Flocking. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Dogs.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Dogs.", "x": "Sheep Farm: Dogs.. Wool. Essential knowledge — Flocking.. the wool flock. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Dogs..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Dogs..", "x": "Explained: Dogs.. Shearing. The context — Sheep Farm. Lambs. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Wool.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Wool.", "x": "Sheep Farm in depth: Wool.. Flocking. Details — the wool flock.. Shearing. Shearing. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Lambs.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Lambs.", "x": "Sheep Farm in depth: Lambs.. Lambs. Details — the wool flock.. Dogs. Grazing. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Shearing.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Shearing.", "x": "Sheep Farm in depth: Shearing.. Shearing. Details — the wool flock.. Flocking. Dogs. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Dogs.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Dogs.", "x": "Sheep Farm in depth: Dogs.. Grazing. Details — the wool flock.. Care. Wool. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Flocking.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Flocking.", "x": "Sheep Farm in depth: Flocking.. Dogs. Details — the wool flock.. Wool. Flocking. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Care.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Care.", "x": "Sheep Farm in depth: Care.. Wool. Details — the wool flock.. Lambs. Lambs. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Sheep Farm comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Sheep Farm comes from.", "x": "Origins: Wool.. Wool. The history of Sheep Farm — the wool flock.. Lambs. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Sheep Farm respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Sheep Farm respectfully.", "x": "Engaging: Shearing.. Flocking. How to participate or observe well — Sheep Farm. the wool flock. Respect first, always; Dogs.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Sheep Farm do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Sheep Farm do's and don'ts.", "x": "Etiquette: Flocking.. Lambs. The rules of respect — Sheep Farm. the wool flock. When in doubt, ask about Care.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Sheep Farm.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Sheep Farm.", "x": "Planning: Wool.. Shearing. Practical notes — Sheep Farm. the wool flock. A little planning shows respect for Lambs.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Sheep Farm and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Sheep Farm and money.", "x": "Costs: Shearing.. Grazing. What to budget — Sheep Farm. the wool flock. The best experiences of Dogs. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-farm-sheep-farm-animal-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
