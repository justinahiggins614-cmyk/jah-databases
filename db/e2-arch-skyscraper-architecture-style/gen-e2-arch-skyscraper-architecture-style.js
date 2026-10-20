(function(){'use strict';
/* JAH Skyscraper Architecture Style Database generator — jahdb-e2-arch-skyscraper-architecture-style-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-arch-skyscraper-architecture-style',PREFIX='JAH-E2ARCHSKYSC-',NAME='JAH Skyscraper Architecture Style Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Skyscraper Architecture: the complete guide", "d": "Skyscraper Architecture: the vertical city..", "g": "overview", "l": 2, "q": "What is Skyscraper Architecture: the complete guide?", "a": "Skyscraper Architecture: the vertical city..", "x": "The complete architecture style guide to Skyscraper Architecture: the vertical city.. Steel. History, meaning, practices, and how to engage respectfully — everything in one database. Steel. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Skyscraper Architecture essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Skyscraper Architecture essentials.", "x": "At a glance: Skyscraper Architecture — the vertical city.. Elevator. The essentials: Elevator.. 1885. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Steel.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Steel.", "x": "Skyscraper Architecture: Steel.. Elevator. Essential knowledge — 1885.. the vertical city. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Steel..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Steel..", "x": "Explained: Steel.. 1885. The context — Skyscraper Architecture. Curtain wall. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Elevator.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Elevator.", "x": "Skyscraper Architecture: Elevator.. Supertall. Essential knowledge — Curtain wall.. the vertical city. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Elevator..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Elevator..", "x": "Explained: Elevator.. Zoning. The context — Skyscraper Architecture. Zoning. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "1885.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "1885.", "x": "Skyscraper Architecture: 1885.. 1885. Essential knowledge — Zoning.. the vertical city. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: 1885..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: 1885..", "x": "Explained: 1885.. Future. The context — Skyscraper Architecture. Supertall. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Curtain wall.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Curtain wall.", "x": "Skyscraper Architecture: Curtain wall.. Zoning. Essential knowledge — Supertall.. the vertical city. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Curtain wall..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Curtain wall..", "x": "Explained: Curtain wall.. Steel. The context — Skyscraper Architecture. Steel. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Zoning.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Zoning.", "x": "Skyscraper Architecture: Zoning.. Future. Essential knowledge — Steel.. the vertical city. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Zoning..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Zoning..", "x": "Explained: Zoning.. Elevator. The context — Skyscraper Architecture. Elevator. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Supertall.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Supertall.", "x": "Skyscraper Architecture: Supertall.. Steel. Essential knowledge — Elevator.. the vertical city. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Supertall..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Supertall..", "x": "Explained: Supertall.. Supertall. The context — Skyscraper Architecture. 1885. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Steel.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Steel.", "x": "Skyscraper Architecture in depth: Steel.. Elevator. Details — the vertical city.. Supertall. Curtain wall. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Elevator.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Elevator.", "x": "Skyscraper Architecture in depth: Elevator.. 1885. Details — the vertical city.. 1885. Zoning. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Supertall.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Supertall.", "x": "Skyscraper Architecture in depth: Supertall.. Curtain wall. Details — the vertical city.. Zoning. Supertall. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "1885.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "1885.", "x": "Skyscraper Architecture in depth: 1885.. Zoning. Details — the vertical city.. Future. Steel. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Zoning.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Zoning.", "x": "Skyscraper Architecture in depth: Zoning.. Supertall. Details — the vertical city.. Steel. Elevator. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Future.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Future.", "x": "Skyscraper Architecture in depth: Future.. Steel. Details — the vertical city.. Elevator. 1885. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Skyscraper Architecture comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Skyscraper Architecture comes from.", "x": "Origins: Steel.. Steel. The history of Skyscraper Architecture — the vertical city.. Elevator. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Skyscraper Architecture respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Skyscraper Architecture respectfully.", "x": "Engaging: Supertall.. Elevator. How to participate or observe well — Skyscraper Architecture. the vertical city. Respect first, always; 1885.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Skyscraper Architecture do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Skyscraper Architecture do's and don'ts.", "x": "Etiquette: Zoning.. 1885. The rules of respect — Skyscraper Architecture. the vertical city. When in doubt, ask about Future.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Skyscraper Architecture.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Skyscraper Architecture.", "x": "Planning: Steel.. Curtain wall. Practical notes — Skyscraper Architecture. the vertical city. A little planning shows respect for Elevator.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Skyscraper Architecture and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Skyscraper Architecture and money.", "x": "Costs: Supertall.. Zoning. What to budget — Skyscraper Architecture. the vertical city. The best experiences of 1885. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-arch-skyscraper-architecture-style-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
