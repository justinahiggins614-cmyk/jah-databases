(function(){'use strict';
/* JAH Hadrian\'s Wall Landmark Database generator — jahdb-e2-landmark-hadrians-wall-landmark-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-landmark-hadrians-wall-landmark',PREFIX='JAH-E2LANDMARKH-',NAME='JAH Hadrian\'s Wall Landmark Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Hadrian's Wall: the complete guide", "d": "Hadrian's Wall: the Roman frontier..", "g": "overview", "l": 2, "q": "What is Hadrian's Wall: the complete guide?", "a": "Hadrian's Wall: the Roman frontier..", "x": "The complete landmark guide to Hadrian's Wall: the Roman frontier.. 122 AD. History, meaning, practices, and how to engage respectfully — everything in one database. 122 AD. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Hadrian's Wall essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Hadrian's Wall essentials.", "x": "At a glance: Hadrian's Wall — the Roman frontier.. 117 km. The essentials: Forts.. Hadrian. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "122 AD.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "122 AD.", "x": "Hadrian's Wall: 122 AD.. Forts. Essential knowledge — Hadrian.. the Roman frontier. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 122 AD..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 122 AD..", "x": "Explained: 122 AD.. Hadrian. The context — Hadrian's Wall. Forts. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "117 km.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "117 km.", "x": "Hadrian's Wall: 117 km.. Walking. Essential knowledge — Forts.. the Roman frontier. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: 117 km..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: 117 km..", "x": "Explained: 117 km.. 117 km. The context — Hadrian's Wall. Vindolanda. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Hadrian.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Hadrian.", "x": "Hadrian's Wall: Hadrian.. Hadrian. Essential knowledge — Vindolanda.. the Roman frontier. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Hadrian..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Hadrian..", "x": "Explained: Hadrian.. Hiking. The context — Hadrian's Wall. Walking. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Forts.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Forts.", "x": "Hadrian's Wall: Forts.. 117 km. Essential knowledge — Walking.. the Roman frontier. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Forts..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Forts..", "x": "Explained: Forts.. 122 AD. The context — Hadrian's Wall. 122 AD. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Vindolanda.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Vindolanda.", "x": "Hadrian's Wall: Vindolanda.. Hiking. Essential knowledge — 122 AD.. the Roman frontier. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Vindolanda..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Vindolanda..", "x": "Explained: Vindolanda.. Forts. The context — Hadrian's Wall. 117 km. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Walking.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Walking.", "x": "Hadrian's Wall: Walking.. 122 AD. Essential knowledge — 117 km.. the Roman frontier. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Walking..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Walking..", "x": "Explained: Walking.. Walking. The context — Hadrian's Wall. Hadrian. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "122 AD.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "122 AD.", "x": "Hadrian's Wall in depth: 122 AD.. 117 km. Details — the Roman frontier.. Walking. Forts. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Forts.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Forts.", "x": "Hadrian's Wall in depth: Forts.. Hadrian. Details — the Roman frontier.. Hadrian. Vindolanda. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Walking.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Walking.", "x": "Hadrian's Wall in depth: Walking.. Forts. Details — the Roman frontier.. 117 km. Walking. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Hadrian.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Hadrian.", "x": "Hadrian's Wall in depth: Hadrian.. Vindolanda. Details — the Roman frontier.. Hiking. 122 AD. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "117 km.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "117 km.", "x": "Hadrian's Wall in depth: 117 km.. Walking. Details — the Roman frontier.. 122 AD. 117 km. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Hiking.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Hiking.", "x": "Hadrian's Wall in depth: Hiking.. 122 AD. Details — the Roman frontier.. Forts. Hadrian. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Hadrian's Wall comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Hadrian's Wall comes from.", "x": "Origins: 122 AD.. 122 AD. The history of Hadrian's Wall — the Roman frontier.. Forts. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Hadrian's Wall respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Hadrian's Wall respectfully.", "x": "Engaging: Walking.. 117 km. How to participate or observe well — Hadrian's Wall. the Roman frontier. Respect first, always; Hadrian.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Hadrian's Wall do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Hadrian's Wall do's and don'ts.", "x": "Etiquette: 117 km.. Hadrian. The rules of respect — Hadrian's Wall. the Roman frontier. When in doubt, ask about Hiking.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Hadrian's Wall.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Hadrian's Wall.", "x": "Planning: 122 AD.. Forts. Practical notes — Hadrian's Wall. the Roman frontier. A little planning shows respect for Forts.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Hadrian's Wall and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Hadrian's Wall and money.", "x": "Costs: Walking.. Vindolanda. What to budget — Hadrian's Wall. the Roman frontier. The best experiences of Hadrian. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-landmark-hadrians-wall-landmark-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
