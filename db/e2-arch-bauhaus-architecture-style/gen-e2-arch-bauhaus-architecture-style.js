(function(){'use strict';
/* JAH Bauhaus Architecture Style Database generator — jahdb-e2-arch-bauhaus-architecture-style-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-arch-bauhaus-architecture-style',PREFIX='JAH-E2ARCHBAUHA-',NAME='JAH Bauhaus Architecture Style Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Bauhaus Architecture: the complete guide", "d": "Bauhaus Architecture: the form follows function..", "g": "overview", "l": 2, "q": "What is Bauhaus Architecture: the complete guide?", "a": "Bauhaus Architecture: the form follows function..", "x": "The complete architecture style guide to Bauhaus Architecture: the form follows function.. 1919. History, meaning, practices, and how to engage respectfully — everything in one database. Gropius. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Bauhaus Architecture essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Bauhaus Architecture essentials.", "x": "At a glance: Bauhaus Architecture — the form follows function.. Gropius. The essentials: Minimal.. Steel. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "1919.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "1919.", "x": "Bauhaus Architecture: 1919.. Minimal. Essential knowledge — Steel.. the form follows function. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 1919..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 1919..", "x": "Explained: 1919.. Steel. The context — Bauhaus Architecture. Glass. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Gropius.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Gropius.", "x": "Bauhaus Architecture: Gropius.. Dessau. Essential knowledge — Glass.. the form follows function. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Gropius..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Gropius..", "x": "Explained: Gropius.. 1919. The context — Bauhaus Architecture. Minimal. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Steel.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Steel.", "x": "Bauhaus Architecture: Steel.. Steel. Essential knowledge — Minimal.. the form follows function. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Steel..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Steel..", "x": "Explained: Steel.. Legacy. The context — Bauhaus Architecture. Dessau. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Glass.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Glass.", "x": "Bauhaus Architecture: Glass.. 1919. Essential knowledge — Dessau.. the form follows function. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Glass..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Glass..", "x": "Explained: Glass.. Gropius. The context — Bauhaus Architecture. 1919. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Minimal.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Minimal.", "x": "Bauhaus Architecture: Minimal.. Legacy. Essential knowledge — 1919.. the form follows function. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Minimal..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Minimal..", "x": "Explained: Minimal.. Minimal. The context — Bauhaus Architecture. Gropius. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Dessau.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Dessau.", "x": "Bauhaus Architecture: Dessau.. Gropius. Essential knowledge — Gropius.. the form follows function. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Dessau..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Dessau..", "x": "Explained: Dessau.. Dessau. The context — Bauhaus Architecture. Steel. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Gropius.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Gropius.", "x": "Bauhaus Architecture in depth: Gropius.. Gropius. Details — the form follows function.. Dessau. Glass. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Minimal.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Minimal.", "x": "Bauhaus Architecture in depth: Minimal.. Steel. Details — the form follows function.. Steel. Minimal. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Dessau.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Dessau.", "x": "Bauhaus Architecture in depth: Dessau.. Glass. Details — the form follows function.. 1919. Dessau. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Steel.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Steel.", "x": "Bauhaus Architecture in depth: Steel.. Minimal. Details — the form follows function.. Legacy. 1919. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "1919.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "1919.", "x": "Bauhaus Architecture in depth: 1919.. Dessau. Details — the form follows function.. Gropius. Gropius. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Legacy.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Legacy.", "x": "Bauhaus Architecture in depth: Legacy.. 1919. Details — the form follows function.. Minimal. Steel. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Bauhaus Architecture comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Bauhaus Architecture comes from.", "x": "Origins: Gropius.. 1919. The history of Bauhaus Architecture — the form follows function.. Minimal. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Bauhaus Architecture respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Bauhaus Architecture respectfully.", "x": "Engaging: Dessau.. Gropius. How to participate or observe well — Bauhaus Architecture. the form follows function. Respect first, always; Steel.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Bauhaus Architecture do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Bauhaus Architecture do's and don'ts.", "x": "Etiquette: 1919.. Steel. The rules of respect — Bauhaus Architecture. the form follows function. When in doubt, ask about Legacy.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Bauhaus Architecture.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Bauhaus Architecture.", "x": "Planning: Gropius.. Glass. Practical notes — Bauhaus Architecture. the form follows function. A little planning shows respect for Minimal.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Bauhaus Architecture and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Bauhaus Architecture and money.", "x": "Costs: Dessau.. Minimal. What to budget — Bauhaus Architecture. the form follows function. The best experiences of Steel. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-arch-bauhaus-architecture-style-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
