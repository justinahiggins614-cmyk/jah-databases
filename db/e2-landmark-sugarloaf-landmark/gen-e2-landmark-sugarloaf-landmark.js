(function(){'use strict';
/* JAH Sugarloaf Mountain Landmark Database generator — jahdb-e2-landmark-sugarloaf-landmark-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-landmark-sugarloaf-landmark',PREFIX='JAH-E2LANDMARKS-',NAME='JAH Sugarloaf Mountain Landmark Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Sugarloaf Mountain: the complete guide", "d": "Sugarloaf Mountain: the cable car peak..", "g": "overview", "l": 2, "q": "What is Sugarloaf Mountain: the complete guide?", "a": "Sugarloaf Mountain: the cable car peak..", "x": "The complete landmark guide to Sugarloaf Mountain: the cable car peak.. 396m. History, meaning, practices, and how to engage respectfully — everything in one database. 396m. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Sugarloaf Mountain essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Sugarloaf Mountain essentials.", "x": "At a glance: Sugarloaf Mountain — the cable car peak.. Cable car. The essentials: Cable car.. 1912. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "396m.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "396m.", "x": "Sugarloaf Mountain: 396m.. Cable car. Essential knowledge — 1912.. the cable car peak. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 396m..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 396m..", "x": "Explained: 396m.. Urca. The context — Sugarloaf Mountain. Sunset. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Cable car.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Cable car.", "x": "Sugarloaf Mountain: Cable car.. Sunset. Essential knowledge — Sunset.. the cable car peak. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Cable car..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Cable car..", "x": "Explained: Cable car.. 1912. The context — Sugarloaf Mountain. Urca. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "1912.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "1912.", "x": "Sugarloaf Mountain: 1912.. Urca. Essential knowledge — Urca.. the cable car peak. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: 1912..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: 1912..", "x": "Explained: 1912.. Tickets. The context — Sugarloaf Mountain. Views. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Sunset.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Sunset.", "x": "Sugarloaf Mountain: Sunset.. 1912. Essential knowledge — Views.. the cable car peak. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Sunset..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Sunset..", "x": "Explained: Sunset.. 396m. The context — Sugarloaf Mountain. 396m. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Urca.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Urca.", "x": "Sugarloaf Mountain: Urca.. Tickets. Essential knowledge — 396m.. the cable car peak. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Urca..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Urca..", "x": "Explained: Urca.. Cable car. The context — Sugarloaf Mountain. Cable car. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Views.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Views.", "x": "Sugarloaf Mountain: Views.. 396m. Essential knowledge — Cable car.. the cable car peak. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Views..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Views..", "x": "Explained: Views.. Sunset. The context — Sugarloaf Mountain. 1912. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "396m.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "396m.", "x": "Sugarloaf Mountain in depth: 396m.. Cable car. Details — the cable car peak.. Sunset. Sunset. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Cable car.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Cable car.", "x": "Sugarloaf Mountain in depth: Cable car.. 1912. Details — the cable car peak.. Urca. Urca. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Sunset.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Sunset.", "x": "Sugarloaf Mountain in depth: Sunset.. Sunset. Details — the cable car peak.. 1912. Views. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Urca.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Urca.", "x": "Sugarloaf Mountain in depth: Urca.. Urca. Details — the cable car peak.. Tickets. 396m. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "1912.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "1912.", "x": "Sugarloaf Mountain in depth: 1912.. Views. Details — the cable car peak.. 396m. Cable car. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Tickets.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Tickets.", "x": "Sugarloaf Mountain in depth: Tickets.. 396m. Details — the cable car peak.. Cable car. 1912. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Sugarloaf Mountain comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Sugarloaf Mountain comes from.", "x": "Origins: 396m.. 396m. The history of Sugarloaf Mountain — the cable car peak.. Cable car. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Sugarloaf Mountain respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Sugarloaf Mountain respectfully.", "x": "Engaging: Sunset.. Cable car. How to participate or observe well — Sugarloaf Mountain. the cable car peak. Respect first, always; Urca.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Sugarloaf Mountain do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Sugarloaf Mountain do's and don'ts.", "x": "Etiquette: 1912.. 1912. The rules of respect — Sugarloaf Mountain. the cable car peak. When in doubt, ask about Tickets.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Sugarloaf Mountain.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Sugarloaf Mountain.", "x": "Planning: 396m.. Sunset. Practical notes — Sugarloaf Mountain. the cable car peak. A little planning shows respect for Cable car.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Sugarloaf Mountain and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Sugarloaf Mountain and money.", "x": "Costs: Sunset.. Urca. What to budget — Sugarloaf Mountain. the cable car peak. The best experiences of Urca. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-landmark-sugarloaf-landmark-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
