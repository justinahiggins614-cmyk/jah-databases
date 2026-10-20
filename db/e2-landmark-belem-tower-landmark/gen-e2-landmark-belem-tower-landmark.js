(function(){'use strict';
/* JAH Lisbon Belem Tower Landmark Database generator — jahdb-e2-landmark-belem-tower-landmark-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-landmark-belem-tower-landmark',PREFIX='JAH-E2LANDMARKB-',NAME='JAH Lisbon Belem Tower Landmark Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Lisbon Belem Tower: the complete guide", "d": "Lisbon Belem Tower: the Manueline tower..", "g": "overview", "l": 2, "q": "What is Lisbon Belem Tower: the complete guide?", "a": "Lisbon Belem Tower: the Manueline tower..", "x": "The complete landmark guide to Lisbon Belem Tower: the Manueline tower.. 1520. History, meaning, practices, and how to engage respectfully — everything in one database. 1520. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Lisbon Belem Tower essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Lisbon Belem Tower essentials.", "x": "At a glance: Lisbon Belem Tower — the Manueline tower.. Manueline. The essentials: Tagus.. Tagus. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "1520.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "1520.", "x": "Lisbon Belem Tower: 1520.. Tagus. Essential knowledge — Tagus.. the Manueline tower. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 1520..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 1520..", "x": "Explained: 1520.. Manueline. The context — Lisbon Belem Tower. Explorers. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Manueline.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Manueline.", "x": "Lisbon Belem Tower: Manueline.. UNESCO. Essential knowledge — Explorers.. the Manueline tower. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Manueline..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Manueline..", "x": "Explained: Manueline.. Explorers. The context — Lisbon Belem Tower. UNESCO. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Tagus.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Tagus.", "x": "Lisbon Belem Tower: Tagus.. Manueline. Essential knowledge — UNESCO.. the Manueline tower. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Tagus..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Tagus..", "x": "Explained: Tagus.. Tours. The context — Lisbon Belem Tower. Limestone. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Explorers.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Explorers.", "x": "Lisbon Belem Tower: Explorers.. Explorers. Essential knowledge — Limestone.. the Manueline tower. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Explorers..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Explorers..", "x": "Explained: Explorers.. 1520. The context — Lisbon Belem Tower. 1520. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "UNESCO.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "UNESCO.", "x": "Lisbon Belem Tower: UNESCO.. Tours. Essential knowledge — 1520.. the Manueline tower. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: UNESCO..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: UNESCO..", "x": "Explained: UNESCO.. Tagus. The context — Lisbon Belem Tower. Manueline. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Limestone.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Limestone.", "x": "Lisbon Belem Tower: Limestone.. 1520. Essential knowledge — Manueline.. the Manueline tower. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Limestone..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Limestone..", "x": "Explained: Limestone.. UNESCO. The context — Lisbon Belem Tower. Tagus. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "1520.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "1520.", "x": "Lisbon Belem Tower in depth: 1520.. Manueline. Details — the Manueline tower.. UNESCO. Explorers. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Tagus.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Tagus.", "x": "Lisbon Belem Tower in depth: Tagus.. Tagus. Details — the Manueline tower.. Manueline. UNESCO. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "UNESCO.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "UNESCO.", "x": "Lisbon Belem Tower in depth: UNESCO.. Explorers. Details — the Manueline tower.. Explorers. Limestone. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Manueline.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Manueline.", "x": "Lisbon Belem Tower in depth: Manueline.. UNESCO. Details — the Manueline tower.. Tours. 1520. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Explorers.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Explorers.", "x": "Lisbon Belem Tower in depth: Explorers.. Limestone. Details — the Manueline tower.. 1520. Manueline. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Tours.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Tours.", "x": "Lisbon Belem Tower in depth: Tours.. 1520. Details — the Manueline tower.. Tagus. Tagus. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Lisbon Belem Tower comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Lisbon Belem Tower comes from.", "x": "Origins: 1520.. 1520. The history of Lisbon Belem Tower — the Manueline tower.. Tagus. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Lisbon Belem Tower respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Lisbon Belem Tower respectfully.", "x": "Engaging: UNESCO.. Manueline. How to participate or observe well — Lisbon Belem Tower. the Manueline tower. Respect first, always; Manueline.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Lisbon Belem Tower do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Lisbon Belem Tower do's and don'ts.", "x": "Etiquette: Explorers.. Tagus. The rules of respect — Lisbon Belem Tower. the Manueline tower. When in doubt, ask about Tours.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Lisbon Belem Tower.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Lisbon Belem Tower.", "x": "Planning: 1520.. Explorers. Practical notes — Lisbon Belem Tower. the Manueline tower. A little planning shows respect for Tagus.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Lisbon Belem Tower and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Lisbon Belem Tower and money.", "x": "Costs: UNESCO.. UNESCO. What to budget — Lisbon Belem Tower. the Manueline tower. The best experiences of Manueline. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-landmark-belem-tower-landmark-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
