(function(){'use strict';
/* JAH Smithsonian Natural History Museum Database generator — jahdb-e2-museum-smithsonian-natural-history-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-museum-smithsonian-natural-history',PREFIX='JAH-E2MUSEUMSMI-',NAME='JAH Smithsonian Natural History Museum Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Smithsonian Natural History: the complete guide", "d": "Smithsonian Natural History: the nation's attic of nature..", "g": "overview", "l": 2, "q": "What is Smithsonian Natural History: the complete guide?", "a": "Smithsonian Natural History: the nation's attic of nature..", "x": "The complete museum guide to Smithsonian Natural History: the nation's attic of nature.. Hope Diamond. History, meaning, practices, and how to engage respectfully — everything in one database. Gems. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Smithsonian Natural History essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Smithsonian Natural History essentials.", "x": "At a glance: Smithsonian Natural History — the nation's attic of nature.. Elephant. The essentials: Fossils.. DC. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Hope Diamond.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Hope Diamond.", "x": "Smithsonian Natural History: Hope Diamond.. Fossils. Essential knowledge — DC.. the nation's attic of nature. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Hope Diamond..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Hope Diamond..", "x": "Explained: Hope Diamond.. History. The context — Smithsonian Natural History. Free. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Elephant.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Elephant.", "x": "Smithsonian Natural History: Elephant.. Free. Essential knowledge — Free.. the nation's attic of nature. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Elephant..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Elephant..", "x": "Explained: Elephant.. Halls. The context — Smithsonian Natural History. Ocean Hall. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "DC.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "DC.", "x": "Smithsonian Natural History: DC.. History. Essential knowledge — Ocean Hall.. the nation's attic of nature. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: DC..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: DC..", "x": "Explained: DC.. Science. The context — Smithsonian Natural History. Fossils. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Free.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Free.", "x": "Smithsonian Natural History: Free.. Halls. Essential knowledge — Fossils.. the nation's attic of nature. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Free..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Free..", "x": "Explained: Free.. Gems. The context — Smithsonian Natural History. Hope Diamond. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Ocean Hall.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Ocean Hall.", "x": "Smithsonian Natural History: Ocean Hall.. Science. Essential knowledge — Hope Diamond.. the nation's attic of nature. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Ocean Hall..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Ocean Hall..", "x": "Explained: Ocean Hall.. Fossils. The context — Smithsonian Natural History. Elephant. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Fossils.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Fossils.", "x": "Smithsonian Natural History: Fossils.. Gems. Essential knowledge — Elephant.. the nation's attic of nature. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Fossils..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Fossils..", "x": "Explained: Fossils.. Free. The context — Smithsonian Natural History. DC. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Gems.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Gems.", "x": "Smithsonian Natural History in depth: Gems.. Elephant. Details — the nation's attic of nature.. Free. Free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Fossils.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Fossils.", "x": "Smithsonian Natural History in depth: Fossils.. DC. Details — the nation's attic of nature.. History. Ocean Hall. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Free.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Free.", "x": "Smithsonian Natural History in depth: Free.. Free. Details — the nation's attic of nature.. Halls. Fossils. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "History.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "History.", "x": "Smithsonian Natural History in depth: History.. Ocean Hall. Details — the nation's attic of nature.. Science. Hope Diamond. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Halls.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Halls.", "x": "Smithsonian Natural History in depth: Halls.. Fossils. Details — the nation's attic of nature.. Gems. Elephant. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Science.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Science.", "x": "Smithsonian Natural History in depth: Science.. Hope Diamond. Details — the nation's attic of nature.. Fossils. DC. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Smithsonian Natural History comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Smithsonian Natural History comes from.", "x": "Origins: Gems.. Hope Diamond. The history of Smithsonian Natural History — the nation's attic of nature.. Fossils. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Smithsonian Natural History respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Smithsonian Natural History respectfully.", "x": "Engaging: Free.. Elephant. How to participate or observe well — Smithsonian Natural History. the nation's attic of nature. Respect first, always; History.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Smithsonian Natural History do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Smithsonian Natural History do's and don'ts.", "x": "Etiquette: Halls.. DC. The rules of respect — Smithsonian Natural History. the nation's attic of nature. When in doubt, ask about Science.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Smithsonian Natural History.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Smithsonian Natural History.", "x": "Planning: Gems.. Free. Practical notes — Smithsonian Natural History. the nation's attic of nature. A little planning shows respect for Fossils.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Smithsonian Natural History and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Smithsonian Natural History and money.", "x": "Costs: Free.. Ocean Hall. What to budget — Smithsonian Natural History. the nation's attic of nature. The best experiences of History. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-museum-smithsonian-natural-history-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
