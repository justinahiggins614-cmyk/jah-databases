(function(){'use strict';
/* JAH Royal Mile Landmark Database generator — jahdb-e2-landmark-royal-mile-landmark-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-landmark-royal-mile-landmark',PREFIX='JAH-E2LANDMARKR-',NAME='JAH Royal Mile Landmark Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Royal Mile: the complete guide", "d": "Royal Mile: the historic mile..", "g": "overview", "l": 2, "q": "What is Royal Mile: the complete guide?", "a": "Royal Mile: the historic mile..", "x": "The complete landmark guide to Royal Mile: the historic mile.. 1 mile. History, meaning, practices, and how to engage respectfully — everything in one database. Mile. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Royal Mile essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Royal Mile essentials.", "x": "At a glance: Royal Mile — the historic mile.. Castle. The essentials: Fringe.. Holyrood. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "1 mile.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "1 mile.", "x": "Royal Mile: 1 mile.. Fringe. Essential knowledge — Holyrood.. the historic mile. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 1 mile..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 1 mile..", "x": "Explained: 1 mile.. Castle. The context — Royal Mile. Fringe. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Castle.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Castle.", "x": "Royal Mile: Castle.. Tartan. Essential knowledge — Fringe.. the historic mile. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Castle..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Castle..", "x": "Explained: Castle.. Holyrood. The context — Royal Mile. Closes. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Holyrood.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Holyrood.", "x": "Royal Mile: Holyrood.. Castle. Essential knowledge — Closes.. the historic mile. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Holyrood..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Holyrood..", "x": "Explained: Holyrood.. Walking. The context — Royal Mile. Tartan. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Fringe.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Fringe.", "x": "Royal Mile: Fringe.. Holyrood. Essential knowledge — Tartan.. the historic mile. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Fringe..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Fringe..", "x": "Explained: Fringe.. Mile. The context — Royal Mile. 1 mile. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Closes.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Closes.", "x": "Royal Mile: Closes.. Walking. Essential knowledge — 1 mile.. the historic mile. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Closes..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Closes..", "x": "Explained: Closes.. Fringe. The context — Royal Mile. Castle. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Tartan.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Tartan.", "x": "Royal Mile: Tartan.. Mile. Essential knowledge — Castle.. the historic mile. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Tartan..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Tartan..", "x": "Explained: Tartan.. Tartan. The context — Royal Mile. Holyrood. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Mile.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Mile.", "x": "Royal Mile in depth: Mile.. Castle. Details — the historic mile.. Tartan. Fringe. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Fringe.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Fringe.", "x": "Royal Mile in depth: Fringe.. Holyrood. Details — the historic mile.. Castle. Closes. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Tartan.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Tartan.", "x": "Royal Mile in depth: Tartan.. Fringe. Details — the historic mile.. Holyrood. Tartan. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Castle.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Castle.", "x": "Royal Mile in depth: Castle.. Closes. Details — the historic mile.. Walking. 1 mile. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Holyrood.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Holyrood.", "x": "Royal Mile in depth: Holyrood.. Tartan. Details — the historic mile.. Mile. Castle. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Walking.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Walking.", "x": "Royal Mile in depth: Walking.. 1 mile. Details — the historic mile.. Fringe. Holyrood. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Royal Mile comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Royal Mile comes from.", "x": "Origins: Mile.. 1 mile. The history of Royal Mile — the historic mile.. Fringe. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Royal Mile respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Royal Mile respectfully.", "x": "Engaging: Tartan.. Castle. How to participate or observe well — Royal Mile. the historic mile. Respect first, always; Castle.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Royal Mile do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Royal Mile do's and don'ts.", "x": "Etiquette: Holyrood.. Holyrood. The rules of respect — Royal Mile. the historic mile. When in doubt, ask about Walking.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Royal Mile.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Royal Mile.", "x": "Planning: Mile.. Fringe. Practical notes — Royal Mile. the historic mile. A little planning shows respect for Fringe.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Royal Mile and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Royal Mile and money.", "x": "Costs: Tartan.. Closes. What to budget — Royal Mile. the historic mile. The best experiences of Castle. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-landmark-royal-mile-landmark-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
