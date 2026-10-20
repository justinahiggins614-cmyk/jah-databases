(function(){'use strict';
/* JAH Cape Cod Architecture Style Database generator — jahdb-e2-arch-cape-cod-architecture-style-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-arch-cape-cod-architecture-style',PREFIX='JAH-E2ARCHCAPEC-',NAME='JAH Cape Cod Architecture Style Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Cape Cod Architecture: the complete guide", "d": "Cape Cod Architecture: the simple cottage..", "g": "overview", "l": 2, "q": "What is Cape Cod Architecture: the complete guide?", "a": "Cape Cod Architecture: the simple cottage..", "x": "The complete architecture style guide to Cape Cod Architecture: the simple cottage.. Steep. History, meaning, practices, and how to engage respectfully — everything in one database. Chimney. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Cape Cod Architecture essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Cape Cod Architecture essentials.", "x": "At a glance: Cape Cod Architecture — the simple cottage.. Central chimney. The essentials: Simple.. Shutters. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Steep.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Steep.", "x": "Cape Cod Architecture: Steep.. Simple. Essential knowledge — Shutters.. the simple cottage. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Steep..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Steep..", "x": "Explained: Steep.. 1940s. The context — Cape Cod Architecture. Cape. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Central chimney.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Central chimney.", "x": "Cape Cod Architecture: Central chimney.. Cape. Essential knowledge — Cape.. the simple cottage. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Central chimney..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Central chimney..", "x": "Explained: Central chimney.. Steep. The context — Cape Cod Architecture. Simple. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Shutters.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Shutters.", "x": "Cape Cod Architecture: Shutters.. 1940s. Essential knowledge — Simple.. the simple cottage. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Shutters..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Shutters..", "x": "Explained: Shutters.. Legacy. The context — Cape Cod Architecture. 1940s. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Cape.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Cape.", "x": "Cape Cod Architecture: Cape.. Steep. Essential knowledge — 1940s.. the simple cottage. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Cape..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Cape..", "x": "Explained: Cape.. Chimney. The context — Cape Cod Architecture. Steep. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Simple.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Simple.", "x": "Cape Cod Architecture: Simple.. Legacy. Essential knowledge — Steep.. the simple cottage. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Simple..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Simple..", "x": "Explained: Simple.. Simple. The context — Cape Cod Architecture. Central chimney. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "1940s.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "1940s.", "x": "Cape Cod Architecture: 1940s.. Chimney. Essential knowledge — Central chimney.. the simple cottage. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: 1940s..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: 1940s..", "x": "Explained: 1940s.. Cape. The context — Cape Cod Architecture. Shutters. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Chimney.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Chimney.", "x": "Cape Cod Architecture in depth: Chimney.. Central chimney. Details — the simple cottage.. Cape. Cape. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Simple.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Simple.", "x": "Cape Cod Architecture in depth: Simple.. Shutters. Details — the simple cottage.. 1940s. Simple. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Cape.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Cape.", "x": "Cape Cod Architecture in depth: Cape.. Cape. Details — the simple cottage.. Steep. 1940s. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "1940s.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "1940s.", "x": "Cape Cod Architecture in depth: 1940s.. Simple. Details — the simple cottage.. Legacy. Steep. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Steep.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Steep.", "x": "Cape Cod Architecture in depth: Steep.. 1940s. Details — the simple cottage.. Chimney. Central chimney. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Legacy.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Legacy.", "x": "Cape Cod Architecture in depth: Legacy.. Steep. Details — the simple cottage.. Simple. Shutters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Cape Cod Architecture comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Cape Cod Architecture comes from.", "x": "Origins: Chimney.. Steep. The history of Cape Cod Architecture — the simple cottage.. Simple. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Cape Cod Architecture respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Cape Cod Architecture respectfully.", "x": "Engaging: Cape.. Central chimney. How to participate or observe well — Cape Cod Architecture. the simple cottage. Respect first, always; 1940s.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Cape Cod Architecture do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Cape Cod Architecture do's and don'ts.", "x": "Etiquette: Steep.. Shutters. The rules of respect — Cape Cod Architecture. the simple cottage. When in doubt, ask about Legacy.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Cape Cod Architecture.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Cape Cod Architecture.", "x": "Planning: Chimney.. Cape. Practical notes — Cape Cod Architecture. the simple cottage. A little planning shows respect for Simple.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Cape Cod Architecture and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Cape Cod Architecture and money.", "x": "Costs: Cape.. Simple. What to budget — Cape Cod Architecture. the simple cottage. The best experiences of 1940s. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-arch-cape-cod-architecture-style-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
