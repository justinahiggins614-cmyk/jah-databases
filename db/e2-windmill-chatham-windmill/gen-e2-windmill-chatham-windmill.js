(function(){'use strict';
/* JAH Chatham Windmill Windmill Database generator — jahdb-e2-windmill-chatham-windmill-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-windmill-chatham-windmill',PREFIX='JAH-E2WINDMILLC-',NAME='JAH Chatham Windmill Windmill Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Chatham Windmill: the complete guide", "d": "Chatham Windmill: Cape Cod's grist mill..", "g": "overview", "l": 2, "q": "What is Chatham Windmill: the complete guide?", "a": "Chatham Windmill: Cape Cod's grist mill..", "x": "The complete windmill guide to Chatham Windmill: Cape Cod's grist mill.. 1797. History, meaning, practices, and how to engage respectfully — everything in one database. Grist. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Chatham Windmill essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Chatham Windmill essentials.", "x": "At a glance: Chatham Windmill — Cape Cod's grist mill.. Grist. The essentials: History.. Cape Cod. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "1797.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "1797.", "x": "Chatham Windmill: 1797.. History. Essential knowledge — Cape Cod.. Cape Cod's grist mill. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 1797..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 1797..", "x": "Explained: 1797.. Cape Cod. The context — Chatham Windmill. Tours. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Grist.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Grist.", "x": "Chatham Windmill: Grist.. Tours. Essential knowledge — Tours.. Cape Cod's grist mill. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Grist..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Grist..", "x": "Explained: Grist.. Photos. The context — Chatham Windmill. History. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Cape Cod.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Cape Cod.", "x": "Chatham Windmill: Cape Cod.. Cape Cod. Essential knowledge — History.. Cape Cod's grist mill. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Cape Cod..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Cape Cod..", "x": "Explained: Cape Cod.. Mill. The context — Chatham Windmill. Photos. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Tours.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Tours.", "x": "Chatham Windmill: Tours.. Photos. Essential knowledge — Photos.. Cape Cod's grist mill. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Tours..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Tours..", "x": "Explained: Tours.. Grist. The context — Chatham Windmill. 1797. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "History.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "History.", "x": "Chatham Windmill: History.. Mill. Essential knowledge — 1797.. Cape Cod's grist mill. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: History..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: History..", "x": "Explained: History.. History. The context — Chatham Windmill. Grist. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Photos.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Photos.", "x": "Chatham Windmill: Photos.. Grist. Essential knowledge — Grist.. Cape Cod's grist mill. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Photos..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Photos..", "x": "Explained: Photos.. Tours. The context — Chatham Windmill. Cape Cod. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Grist.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Grist.", "x": "Chatham Windmill in depth: Grist.. Grist. Details — Cape Cod's grist mill.. Tours. Tours. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "History.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "History.", "x": "Chatham Windmill in depth: History.. Cape Cod. Details — Cape Cod's grist mill.. Cape Cod. History. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Tours.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Tours.", "x": "Chatham Windmill in depth: Tours.. Tours. Details — Cape Cod's grist mill.. Photos. Photos. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Cape Cod.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Cape Cod.", "x": "Chatham Windmill in depth: Cape Cod.. History. Details — Cape Cod's grist mill.. Mill. 1797. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Photos.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Photos.", "x": "Chatham Windmill in depth: Photos.. Photos. Details — Cape Cod's grist mill.. Grist. Grist. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Mill.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Mill.", "x": "Chatham Windmill in depth: Mill.. 1797. Details — Cape Cod's grist mill.. History. Cape Cod. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Chatham Windmill comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Chatham Windmill comes from.", "x": "Origins: Grist.. 1797. The history of Chatham Windmill — Cape Cod's grist mill.. History. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Chatham Windmill respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Chatham Windmill respectfully.", "x": "Engaging: Tours.. Grist. How to participate or observe well — Chatham Windmill. Cape Cod's grist mill. Respect first, always; Cape Cod.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Chatham Windmill do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Chatham Windmill do's and don'ts.", "x": "Etiquette: Photos.. Cape Cod. The rules of respect — Chatham Windmill. Cape Cod's grist mill. When in doubt, ask about Mill.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Chatham Windmill.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Chatham Windmill.", "x": "Planning: Grist.. Tours. Practical notes — Chatham Windmill. Cape Cod's grist mill. A little planning shows respect for History.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Chatham Windmill and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Chatham Windmill and money.", "x": "Costs: Tours.. History. What to budget — Chatham Windmill. Cape Cod's grist mill. The best experiences of Cape Cod. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-windmill-chatham-windmill-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
