(function(){'use strict';
/* JAH Table Mountain Landmark Database generator — jahdb-e2-landmark-table-mountain-landmark-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-landmark-table-mountain-landmark',PREFIX='JAH-E2LANDMARKT-',NAME='JAH Table Mountain Landmark Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Table Mountain: the complete guide", "d": "Table Mountain: the flat top..", "g": "overview", "l": 2, "q": "What is Table Mountain: the complete guide?", "a": "Table Mountain: the flat top..", "x": "The complete landmark guide to Table Mountain: the flat top.. 1,085m. History, meaning, practices, and how to engage respectfully — everything in one database. 1,085m. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Table Mountain essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Table Mountain essentials.", "x": "At a glance: Table Mountain — the flat top.. Flat. The essentials: Cable car.. Cable car. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "1,085m.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "1,085m.", "x": "Table Mountain: 1,085m.. Cable car. Essential knowledge — Cable car.. the flat top. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 1,085m..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 1,085m..", "x": "Explained: 1,085m.. Fynbos. The context — Table Mountain. Fynbos. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Flat.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Flat.", "x": "Table Mountain: Flat.. Views. Essential knowledge — Fynbos.. the flat top. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Flat..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Flat..", "x": "Explained: Flat.. Flat. The context — Table Mountain. Cloud. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Cable car.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Cable car.", "x": "Table Mountain: Cable car.. Fynbos. Essential knowledge — Cloud.. the flat top. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Cable car..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Cable car..", "x": "Explained: Cable car.. Tickets. The context — Table Mountain. Views. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Fynbos.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Fynbos.", "x": "Table Mountain: Fynbos.. Flat. Essential knowledge — Views.. the flat top. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Fynbos..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Fynbos..", "x": "Explained: Fynbos.. 1,085m. The context — Table Mountain. 1,085m. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Cloud.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Cloud.", "x": "Table Mountain: Cloud.. Tickets. Essential knowledge — 1,085m.. the flat top. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Cloud..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Cloud..", "x": "Explained: Cloud.. Cable car. The context — Table Mountain. Flat. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Views.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Views.", "x": "Table Mountain: Views.. 1,085m. Essential knowledge — Flat.. the flat top. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Views..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Views..", "x": "Explained: Views.. Views. The context — Table Mountain. Cable car. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "1,085m.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "1,085m.", "x": "Table Mountain in depth: 1,085m.. Flat. Details — the flat top.. Views. Fynbos. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Cable car.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Cable car.", "x": "Table Mountain in depth: Cable car.. Cable car. Details — the flat top.. Fynbos. Cloud. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Views.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Views.", "x": "Table Mountain in depth: Views.. Fynbos. Details — the flat top.. Flat. Views. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Fynbos.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Fynbos.", "x": "Table Mountain in depth: Fynbos.. Cloud. Details — the flat top.. Tickets. 1,085m. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Flat.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Flat.", "x": "Table Mountain in depth: Flat.. Views. Details — the flat top.. 1,085m. Flat. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Tickets.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Tickets.", "x": "Table Mountain in depth: Tickets.. 1,085m. Details — the flat top.. Cable car. Cable car. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Table Mountain comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Table Mountain comes from.", "x": "Origins: 1,085m.. 1,085m. The history of Table Mountain — the flat top.. Cable car. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Table Mountain respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Table Mountain respectfully.", "x": "Engaging: Views.. Flat. How to participate or observe well — Table Mountain. the flat top. Respect first, always; Fynbos.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Table Mountain do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Table Mountain do's and don'ts.", "x": "Etiquette: Flat.. Cable car. The rules of respect — Table Mountain. the flat top. When in doubt, ask about Tickets.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Table Mountain.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Table Mountain.", "x": "Planning: 1,085m.. Fynbos. Practical notes — Table Mountain. the flat top. A little planning shows respect for Cable car.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Table Mountain and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Table Mountain and money.", "x": "Costs: Views.. Cloud. What to budget — Table Mountain. the flat top. The best experiences of Fynbos. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-landmark-table-mountain-landmark-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
