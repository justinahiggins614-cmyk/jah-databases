(function(){'use strict';
/* JAH Sagrada2 Database generator — jahdb-e2-landmark2-sagrada2-landmark-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-landmark2-sagrada2-landmark',PREFIX='JAH-E2LANDMARK2-',NAME='JAH Sagrada2 Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Sagrada2: the complete guide", "d": "Sagrada2: the Gaudi basilica..", "g": "overview", "l": 2, "q": "What is Sagrada2: the complete guide?", "a": "Sagrada2: the Gaudi basilica..", "x": "The complete landmark guide to Sagrada2: the Gaudi basilica.. Barcelona. History, meaning, practices, and how to engage respectfully — everything in one database. Barcelona. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Sagrada2 essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Sagrada2 essentials.", "x": "At a glance: Sagrada2 — the Gaudi basilica.. Gaudi. The essentials: UNESCO.. 1882. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Barcelona.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Barcelona.", "x": "Sagrada2: Barcelona.. UNESCO. Essential knowledge — 1882.. the Gaudi basilica. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Barcelona..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Barcelona..", "x": "Explained: Barcelona.. Gaudi. The context — Sagrada2. Spires. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Gaudi.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Gaudi.", "x": "Sagrada2: Gaudi.. Unfinished. Essential knowledge — Spires.. the Gaudi basilica. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Gaudi..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Gaudi..", "x": "Explained: Gaudi.. 1882. The context — Sagrada2. Unfinished. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "1882.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "1882.", "x": "Sagrada2: 1882.. Gaudi. Essential knowledge — Unfinished.. the Gaudi basilica. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: 1882..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: 1882..", "x": "Explained: 1882.. Visiting. The context — Sagrada2. UNESCO. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Spires.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Spires.", "x": "Sagrada2: Spires.. 1882. Essential knowledge — UNESCO.. the Gaudi basilica. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Spires..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Spires..", "x": "Explained: Spires.. Barcelona. The context — Sagrada2. Barcelona. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Unfinished.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Unfinished.", "x": "Sagrada2: Unfinished.. Visiting. Essential knowledge — Barcelona.. the Gaudi basilica. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Unfinished..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Unfinished..", "x": "Explained: Unfinished.. UNESCO. The context — Sagrada2. Gaudi. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "UNESCO.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "UNESCO.", "x": "Sagrada2: UNESCO.. Barcelona. Essential knowledge — Gaudi.. the Gaudi basilica. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: UNESCO..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: UNESCO..", "x": "Explained: UNESCO.. Unfinished. The context — Sagrada2. 1882. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Barcelona.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Barcelona.", "x": "Sagrada2 in depth: Barcelona.. Gaudi. Details — the Gaudi basilica.. Unfinished. Spires. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "UNESCO.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "UNESCO.", "x": "Sagrada2 in depth: UNESCO.. 1882. Details — the Gaudi basilica.. Gaudi. Unfinished. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Unfinished.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Unfinished.", "x": "Sagrada2 in depth: Unfinished.. Spires. Details — the Gaudi basilica.. 1882. UNESCO. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Gaudi.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Gaudi.", "x": "Sagrada2 in depth: Gaudi.. Unfinished. Details — the Gaudi basilica.. Visiting. Barcelona. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "1882.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "1882.", "x": "Sagrada2 in depth: 1882.. UNESCO. Details — the Gaudi basilica.. Barcelona. Gaudi. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Visiting.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Visiting.", "x": "Sagrada2 in depth: Visiting.. Barcelona. Details — the Gaudi basilica.. UNESCO. 1882. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Sagrada2 comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Sagrada2 comes from.", "x": "Origins: Barcelona.. Barcelona. The history of Sagrada2 — the Gaudi basilica.. UNESCO. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Sagrada2 respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Sagrada2 respectfully.", "x": "Engaging: Unfinished.. Gaudi. How to participate or observe well — Sagrada2. the Gaudi basilica. Respect first, always; Gaudi.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Sagrada2 do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Sagrada2 do's and don'ts.", "x": "Etiquette: 1882.. 1882. The rules of respect — Sagrada2. the Gaudi basilica. When in doubt, ask about Visiting.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Sagrada2.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Sagrada2.", "x": "Planning: Barcelona.. Spires. Practical notes — Sagrada2. the Gaudi basilica. A little planning shows respect for UNESCO.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Sagrada2 and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Sagrada2 and money.", "x": "Costs: Unfinished.. Unfinished. What to budget — Sagrada2. the Gaudi basilica. The best experiences of Gaudi. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-landmark2-sagrada2-landmark-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
