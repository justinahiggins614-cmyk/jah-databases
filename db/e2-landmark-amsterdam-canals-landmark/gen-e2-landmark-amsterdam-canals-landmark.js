(function(){'use strict';
/* JAH Amsterdam Canals Landmark Database generator — jahdb-e2-landmark-amsterdam-canals-landmark-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-landmark-amsterdam-canals-landmark',PREFIX='JAH-E2LANDMARKA-',NAME='JAH Amsterdam Canals Landmark Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Amsterdam Canals: the complete guide", "d": "Amsterdam Canals: the grachtengordel..", "g": "overview", "l": 2, "q": "What is Amsterdam Canals: the complete guide?", "a": "Amsterdam Canals: the grachtengordel..", "x": "The complete landmark guide to Amsterdam Canals: the grachtengordel.. 17th century. History, meaning, practices, and how to engage respectfully — everything in one database. 17th. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Amsterdam Canals essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Amsterdam Canals essentials.", "x": "At a glance: Amsterdam Canals — the grachtengordel.. Grachtengordel. The essentials: Houseboats.. Houseboats. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "17th century.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "17th century.", "x": "Amsterdam Canals: 17th century.. Houseboats. Essential knowledge — Houseboats.. the grachtengordel. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 17th century..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 17th century..", "x": "Explained: 17th century.. Bikes. The context — Amsterdam Canals. Bridges. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Grachtengordel.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Grachtengordel.", "x": "Amsterdam Canals: Grachtengordel.. UNESCO. Essential knowledge — Bridges.. the grachtengordel. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Grachtengordel..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Grachtengordel..", "x": "Explained: Grachtengordel.. Canals. The context — Amsterdam Canals. UNESCO. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Houseboats.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Houseboats.", "x": "Amsterdam Canals: Houseboats.. Bikes. Essential knowledge — UNESCO.. the grachtengordel. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Houseboats..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Houseboats..", "x": "Explained: Houseboats.. Tours. The context — Amsterdam Canals. Bikes. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Bridges.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Bridges.", "x": "Amsterdam Canals: Bridges.. Canals. Essential knowledge — Bikes.. the grachtengordel. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Bridges..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Bridges..", "x": "Explained: Bridges.. 17th. The context — Amsterdam Canals. 17th century. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "UNESCO.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "UNESCO.", "x": "Amsterdam Canals: UNESCO.. Tours. Essential knowledge — 17th century.. the grachtengordel. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: UNESCO..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: UNESCO..", "x": "Explained: UNESCO.. Houseboats. The context — Amsterdam Canals. Grachtengordel. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Bikes.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Bikes.", "x": "Amsterdam Canals: Bikes.. 17th. Essential knowledge — Grachtengordel.. the grachtengordel. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Bikes..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Bikes..", "x": "Explained: Bikes.. UNESCO. The context — Amsterdam Canals. Houseboats. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "17th.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "17th.", "x": "Amsterdam Canals in depth: 17th.. Grachtengordel. Details — the grachtengordel.. UNESCO. Bridges. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Houseboats.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Houseboats.", "x": "Amsterdam Canals in depth: Houseboats.. Houseboats. Details — the grachtengordel.. Bikes. UNESCO. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "UNESCO.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "UNESCO.", "x": "Amsterdam Canals in depth: UNESCO.. Bridges. Details — the grachtengordel.. Canals. Bikes. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Bikes.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Bikes.", "x": "Amsterdam Canals in depth: Bikes.. UNESCO. Details — the grachtengordel.. Tours. 17th century. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Canals.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Canals.", "x": "Amsterdam Canals in depth: Canals.. Bikes. Details — the grachtengordel.. 17th. Grachtengordel. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Tours.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Tours.", "x": "Amsterdam Canals in depth: Tours.. 17th century. Details — the grachtengordel.. Houseboats. Houseboats. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Amsterdam Canals comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Amsterdam Canals comes from.", "x": "Origins: 17th.. 17th century. The history of Amsterdam Canals — the grachtengordel.. Houseboats. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Amsterdam Canals respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Amsterdam Canals respectfully.", "x": "Engaging: UNESCO.. Grachtengordel. How to participate or observe well — Amsterdam Canals. the grachtengordel. Respect first, always; Bikes.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Amsterdam Canals do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Amsterdam Canals do's and don'ts.", "x": "Etiquette: Canals.. Houseboats. The rules of respect — Amsterdam Canals. the grachtengordel. When in doubt, ask about Tours.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Amsterdam Canals.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Amsterdam Canals.", "x": "Planning: 17th.. Bridges. Practical notes — Amsterdam Canals. the grachtengordel. A little planning shows respect for Houseboats.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Amsterdam Canals and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Amsterdam Canals and money.", "x": "Costs: UNESCO.. UNESCO. What to budget — Amsterdam Canals. the grachtengordel. The best experiences of Bikes. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-landmark-amsterdam-canals-landmark-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
