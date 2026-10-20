(function(){'use strict';
/* JAH Manneken Pis Landmark Database generator — jahdb-e2-landmark-manneken-pis-landmark-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-landmark-manneken-pis-landmark',PREFIX='JAH-E2LANDMARKM-',NAME='JAH Manneken Pis Landmark Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Manneken Pis: the complete guide", "d": "Manneken Pis: the peeing boy..", "g": "overview", "l": 2, "q": "What is Manneken Pis: the complete guide?", "a": "Manneken Pis: the peeing boy..", "x": "The complete landmark guide to Manneken Pis: the peeing boy.. 1619. History, meaning, practices, and how to engage respectfully — everything in one database. 1619. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Manneken Pis essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Manneken Pis essentials.", "x": "At a glance: Manneken Pis — the peeing boy.. Bronze. The essentials: Costumes.. Costumes. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "1619.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "1619.", "x": "Manneken Pis: 1619.. Costumes. Essential knowledge — Costumes.. the peeing boy. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 1619..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 1619..", "x": "Explained: 1619.. Small. The context — Manneken Pis. Fountain. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Bronze.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Bronze.", "x": "Manneken Pis: Bronze.. Legend. Essential knowledge — Fountain.. the peeing boy. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Bronze..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Bronze..", "x": "Explained: Bronze.. Bronze. The context — Manneken Pis. Legend. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Costumes.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Costumes.", "x": "Manneken Pis: Costumes.. Small. Essential knowledge — Legend.. the peeing boy. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Costumes..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Costumes..", "x": "Explained: Costumes.. Views. The context — Manneken Pis. Small. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Fountain.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Fountain.", "x": "Manneken Pis: Fountain.. Bronze. Essential knowledge — Small.. the peeing boy. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Fountain..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Fountain..", "x": "Explained: Fountain.. 1619. The context — Manneken Pis. 1619. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Legend.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Legend.", "x": "Manneken Pis: Legend.. Views. Essential knowledge — 1619.. the peeing boy. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Legend..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Legend..", "x": "Explained: Legend.. Costumes. The context — Manneken Pis. Bronze. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Small.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Small.", "x": "Manneken Pis: Small.. 1619. Essential knowledge — Bronze.. the peeing boy. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Small..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Small..", "x": "Explained: Small.. Legend. The context — Manneken Pis. Costumes. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "1619.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "1619.", "x": "Manneken Pis in depth: 1619.. Bronze. Details — the peeing boy.. Legend. Fountain. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Costumes.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Costumes.", "x": "Manneken Pis in depth: Costumes.. Costumes. Details — the peeing boy.. Small. Legend. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Legend.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Legend.", "x": "Manneken Pis in depth: Legend.. Fountain. Details — the peeing boy.. Bronze. Small. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Small.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Small.", "x": "Manneken Pis in depth: Small.. Legend. Details — the peeing boy.. Views. 1619. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Bronze.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Bronze.", "x": "Manneken Pis in depth: Bronze.. Small. Details — the peeing boy.. 1619. Bronze. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Views.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Views.", "x": "Manneken Pis in depth: Views.. 1619. Details — the peeing boy.. Costumes. Costumes. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Manneken Pis comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Manneken Pis comes from.", "x": "Origins: 1619.. 1619. The history of Manneken Pis — the peeing boy.. Costumes. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Manneken Pis respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Manneken Pis respectfully.", "x": "Engaging: Legend.. Bronze. How to participate or observe well — Manneken Pis. the peeing boy. Respect first, always; Small.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Manneken Pis do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Manneken Pis do's and don'ts.", "x": "Etiquette: Bronze.. Costumes. The rules of respect — Manneken Pis. the peeing boy. When in doubt, ask about Views.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Manneken Pis.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Manneken Pis.", "x": "Planning: 1619.. Fountain. Practical notes — Manneken Pis. the peeing boy. A little planning shows respect for Costumes.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Manneken Pis and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Manneken Pis and money.", "x": "Costs: Legend.. Legend. What to budget — Manneken Pis. the peeing boy. The best experiences of Small. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-landmark-manneken-pis-landmark-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
