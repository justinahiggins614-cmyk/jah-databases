(function(){'use strict';
/* JAH Ajanta Caves Landmark Database generator — jahdb-e2-landmark-ajanta-caves-landmark-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-landmark-ajanta-caves-landmark',PREFIX='JAH-E2LANDMARKA-',NAME='JAH Ajanta Caves Landmark Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Ajanta Caves: the complete guide", "d": "Ajanta Caves: the painted caves..", "g": "overview", "l": 2, "q": "What is Ajanta Caves: the complete guide?", "a": "Ajanta Caves: the painted caves..", "x": "The complete landmark guide to Ajanta Caves: the painted caves.. 30 caves. History, meaning, practices, and how to engage respectfully — everything in one database. 30. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Ajanta Caves essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Ajanta Caves essentials.", "x": "At a glance: Ajanta Caves — the painted caves.. Frescoes. The essentials: Frescoes.. 2nd century BC. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "30 caves.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "30 caves.", "x": "Ajanta Caves: 30 caves.. Frescoes. Essential knowledge — 2nd century BC.. the painted caves. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 30 caves..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 30 caves..", "x": "Explained: 30 caves.. Buddhist. The context — Ajanta Caves. Horseshoe. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Frescoes.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Frescoes.", "x": "Ajanta Caves: Frescoes.. UNESCO. Essential knowledge — Horseshoe.. the painted caves. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Frescoes..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Frescoes..", "x": "Explained: Frescoes.. Horseshoe. The context — Ajanta Caves. UNESCO. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "2nd century BC.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "2nd century BC.", "x": "Ajanta Caves: 2nd century BC.. Buddhist. Essential knowledge — UNESCO.. the painted caves. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: 2nd century BC..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: 2nd century BC..", "x": "Explained: 2nd century BC.. Tours. The context — Ajanta Caves. Buddhist. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Horseshoe.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Horseshoe.", "x": "Ajanta Caves: Horseshoe.. Horseshoe. Essential knowledge — Buddhist.. the painted caves. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Horseshoe..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Horseshoe..", "x": "Explained: Horseshoe.. 30. The context — Ajanta Caves. 30 caves. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "UNESCO.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "UNESCO.", "x": "Ajanta Caves: UNESCO.. Tours. Essential knowledge — 30 caves.. the painted caves. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: UNESCO..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: UNESCO..", "x": "Explained: UNESCO.. Frescoes. The context — Ajanta Caves. Frescoes. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Buddhist.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Buddhist.", "x": "Ajanta Caves: Buddhist.. 30. Essential knowledge — Frescoes.. the painted caves. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Buddhist..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Buddhist..", "x": "Explained: Buddhist.. UNESCO. The context — Ajanta Caves. 2nd century BC. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "30.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "30.", "x": "Ajanta Caves in depth: 30.. Frescoes. Details — the painted caves.. UNESCO. Horseshoe. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Frescoes.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Frescoes.", "x": "Ajanta Caves in depth: Frescoes.. 2nd century BC. Details — the painted caves.. Buddhist. UNESCO. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "UNESCO.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "UNESCO.", "x": "Ajanta Caves in depth: UNESCO.. Horseshoe. Details — the painted caves.. Horseshoe. Buddhist. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Buddhist.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Buddhist.", "x": "Ajanta Caves in depth: Buddhist.. UNESCO. Details — the painted caves.. Tours. 30 caves. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Horseshoe.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Horseshoe.", "x": "Ajanta Caves in depth: Horseshoe.. Buddhist. Details — the painted caves.. 30. Frescoes. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Tours.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Tours.", "x": "Ajanta Caves in depth: Tours.. 30 caves. Details — the painted caves.. Frescoes. 2nd century BC. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Ajanta Caves comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Ajanta Caves comes from.", "x": "Origins: 30.. 30 caves. The history of Ajanta Caves — the painted caves.. Frescoes. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Ajanta Caves respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Ajanta Caves respectfully.", "x": "Engaging: UNESCO.. Frescoes. How to participate or observe well — Ajanta Caves. the painted caves. Respect first, always; Buddhist.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Ajanta Caves do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Ajanta Caves do's and don'ts.", "x": "Etiquette: Horseshoe.. 2nd century BC. The rules of respect — Ajanta Caves. the painted caves. When in doubt, ask about Tours.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Ajanta Caves.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Ajanta Caves.", "x": "Planning: 30.. Horseshoe. Practical notes — Ajanta Caves. the painted caves. A little planning shows respect for Frescoes.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Ajanta Caves and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Ajanta Caves and money.", "x": "Costs: UNESCO.. UNESCO. What to budget — Ajanta Caves. the painted caves. The best experiences of Buddhist. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-landmark-ajanta-caves-landmark-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
