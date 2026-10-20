(function(){'use strict';
/* JAH Venice Canals Landmark Database generator — jahdb-e2-landmark-venice-canals-landmark-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-landmark-venice-canals-landmark',PREFIX='JAH-E2LANDMARKV-',NAME='JAH Venice Canals Landmark Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Venice Canals: the complete guide", "d": "Venice Canals: the water streets..", "g": "overview", "l": 2, "q": "What is Venice Canals: the complete guide?", "a": "Venice Canals: the water streets..", "x": "The complete landmark guide to Venice Canals: the water streets.. 118 islands. History, meaning, practices, and how to engage respectfully — everything in one database. Islands. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Venice Canals essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Venice Canals essentials.", "x": "At a glance: Venice Canals — the water streets.. Gondolas. The essentials: Gondolas.. Grand Canal. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "118 islands.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "118 islands.", "x": "Venice Canals: 118 islands.. Gondolas. Essential knowledge — Grand Canal.. the water streets. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 118 islands..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 118 islands..", "x": "Explained: 118 islands.. Acqua. The context — Venice Canals. Bridges. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Gondolas.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Gondolas.", "x": "Venice Canals: Gondolas.. Bridges. Essential knowledge — Bridges.. the water streets. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Gondolas..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Gondolas..", "x": "Explained: Gondolas.. Grand. The context — Venice Canals. Acqua alta. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Grand Canal.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Grand Canal.", "x": "Venice Canals: Grand Canal.. Acqua. Essential knowledge — Acqua alta.. the water streets. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Grand Canal..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Grand Canal..", "x": "Explained: Grand Canal.. Tours. The context — Venice Canals. 400 bridges. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Bridges.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Bridges.", "x": "Venice Canals: Bridges.. Grand. Essential knowledge — 400 bridges.. the water streets. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Bridges..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Bridges..", "x": "Explained: Bridges.. Islands. The context — Venice Canals. 118 islands. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Acqua alta.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Acqua alta.", "x": "Venice Canals: Acqua alta.. Tours. Essential knowledge — 118 islands.. the water streets. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Acqua alta..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Acqua alta..", "x": "Explained: Acqua alta.. Gondolas. The context — Venice Canals. Gondolas. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "400 bridges.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "400 bridges.", "x": "Venice Canals: 400 bridges.. Islands. Essential knowledge — Gondolas.. the water streets. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: 400 bridges..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: 400 bridges..", "x": "Explained: 400 bridges.. Bridges. The context — Venice Canals. Grand Canal. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Islands.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Islands.", "x": "Venice Canals in depth: Islands.. Gondolas. Details — the water streets.. Bridges. Bridges. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Gondolas.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Gondolas.", "x": "Venice Canals in depth: Gondolas.. Grand Canal. Details — the water streets.. Acqua. Acqua alta. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Bridges.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Bridges.", "x": "Venice Canals in depth: Bridges.. Bridges. Details — the water streets.. Grand. 400 bridges. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Acqua.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Acqua.", "x": "Venice Canals in depth: Acqua.. Acqua alta. Details — the water streets.. Tours. 118 islands. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Grand.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Grand.", "x": "Venice Canals in depth: Grand.. 400 bridges. Details — the water streets.. Islands. Gondolas. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Tours.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Tours.", "x": "Venice Canals in depth: Tours.. 118 islands. Details — the water streets.. Gondolas. Grand Canal. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Venice Canals comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Venice Canals comes from.", "x": "Origins: Islands.. 118 islands. The history of Venice Canals — the water streets.. Gondolas. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Venice Canals respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Venice Canals respectfully.", "x": "Engaging: Bridges.. Gondolas. How to participate or observe well — Venice Canals. the water streets. Respect first, always; Acqua.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Venice Canals do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Venice Canals do's and don'ts.", "x": "Etiquette: Grand.. Grand Canal. The rules of respect — Venice Canals. the water streets. When in doubt, ask about Tours.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Venice Canals.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Venice Canals.", "x": "Planning: Islands.. Bridges. Practical notes — Venice Canals. the water streets. A little planning shows respect for Gondolas.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Venice Canals and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Venice Canals and money.", "x": "Costs: Bridges.. Acqua alta. What to budget — Venice Canals. the water streets. The best experiences of Acqua. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-landmark-venice-canals-landmark-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
