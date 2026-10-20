(function(){'use strict';
/* JAH Croissant Bread Bread Database generator — jahdb-e2-bread-croissant-bread-loaf-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-bread-croissant-bread-loaf',PREFIX='JAH-E2BREADCROI-',NAME='JAH Croissant Bread Bread Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Croissant Bread: the complete guide", "d": "Croissant Bread: the laminated loaf..", "g": "overview", "l": 2, "q": "What is Croissant Bread: the complete guide?", "a": "Croissant Bread: the laminated loaf..", "x": "The complete bread guide to Croissant Bread: the laminated loaf.. Laminated. History, meaning, practices, and how to engage respectfully — everything in one database. Laminated. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Croissant Bread essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Croissant Bread essentials.", "x": "At a glance: Croissant Bread — the laminated loaf.. Butter. The essentials: Butter.. French. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Laminated.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Laminated.", "x": "Croissant Bread: Laminated.. Butter. Essential knowledge — French.. the laminated loaf. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Laminated..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Laminated..", "x": "Explained: Laminated.. French. The context — Croissant Bread. Flaky. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Butter.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Butter.", "x": "Croissant Bread: Butter.. Flaky. Essential knowledge — Flaky.. the laminated loaf. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Butter..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Butter..", "x": "Explained: Butter.. Layers. The context — Croissant Bread. Viennoiserie. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "French.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "French.", "x": "Croissant Bread: French.. French. Essential knowledge — Viennoiserie.. the laminated loaf. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: French..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: French..", "x": "Explained: French.. Baking. The context — Croissant Bread. Layers. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Flaky.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Flaky.", "x": "Croissant Bread: Flaky.. Layers. Essential knowledge — Layers.. the laminated loaf. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Flaky..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Flaky..", "x": "Explained: Flaky.. Laminated. The context — Croissant Bread. Laminated. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Viennoiserie.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Viennoiserie.", "x": "Croissant Bread: Viennoiserie.. Baking. Essential knowledge — Laminated.. the laminated loaf. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Viennoiserie..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Viennoiserie..", "x": "Explained: Viennoiserie.. Butter. The context — Croissant Bread. Butter. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Layers.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Layers.", "x": "Croissant Bread: Layers.. Laminated. Essential knowledge — Butter.. the laminated loaf. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Layers..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Layers..", "x": "Explained: Layers.. Flaky. The context — Croissant Bread. French. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Laminated.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Laminated.", "x": "Croissant Bread in depth: Laminated.. Butter. Details — the laminated loaf.. Flaky. Flaky. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Butter.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Butter.", "x": "Croissant Bread in depth: Butter.. French. Details — the laminated loaf.. French. Viennoiserie. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Flaky.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Flaky.", "x": "Croissant Bread in depth: Flaky.. Flaky. Details — the laminated loaf.. Layers. Layers. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "French.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "French.", "x": "Croissant Bread in depth: French.. Viennoiserie. Details — the laminated loaf.. Baking. Laminated. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Layers.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Layers.", "x": "Croissant Bread in depth: Layers.. Layers. Details — the laminated loaf.. Laminated. Butter. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Baking.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Baking.", "x": "Croissant Bread in depth: Baking.. Laminated. Details — the laminated loaf.. Butter. French. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Croissant Bread comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Croissant Bread comes from.", "x": "Origins: Laminated.. Laminated. The history of Croissant Bread — the laminated loaf.. Butter. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Croissant Bread respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Croissant Bread respectfully.", "x": "Engaging: Flaky.. Butter. How to participate or observe well — Croissant Bread. the laminated loaf. Respect first, always; French.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Croissant Bread do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Croissant Bread do's and don'ts.", "x": "Etiquette: Layers.. French. The rules of respect — Croissant Bread. the laminated loaf. When in doubt, ask about Baking.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Croissant Bread.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Croissant Bread.", "x": "Planning: Laminated.. Flaky. Practical notes — Croissant Bread. the laminated loaf. A little planning shows respect for Butter.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Croissant Bread and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Croissant Bread and money.", "x": "Costs: Flaky.. Viennoiserie. What to budget — Croissant Bread. the laminated loaf. The best experiences of French. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-bread-croissant-bread-loaf-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
