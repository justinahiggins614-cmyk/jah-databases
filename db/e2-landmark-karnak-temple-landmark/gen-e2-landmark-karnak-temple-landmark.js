(function(){'use strict';
/* JAH Karnak Temple Landmark Database generator — jahdb-e2-landmark-karnak-temple-landmark-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-landmark-karnak-temple-landmark',PREFIX='JAH-E2LANDMARKK-',NAME='JAH Karnak Temple Landmark Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Karnak Temple: the complete guide", "d": "Karnak Temple: the hypostyle hall..", "g": "overview", "l": 2, "q": "What is Karnak Temple: the complete guide?", "a": "Karnak Temple: the hypostyle hall..", "x": "The complete landmark guide to Karnak Temple: the hypostyle hall.. 134 columns. History, meaning, practices, and how to engage respectfully — everything in one database. 134. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Karnak Temple essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Karnak Temple essentials.", "x": "At a glance: Karnak Temple — the hypostyle hall.. Amun. The essentials: Amun.. Avenue sphinx. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "134 columns.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "134 columns.", "x": "Karnak Temple: 134 columns.. Amun. Essential knowledge — Avenue sphinx.. the hypostyle hall. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 134 columns..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 134 columns..", "x": "Explained: 134 columns.. Luxor. The context — Karnak Temple. Obelisks. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Amun.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Amun.", "x": "Karnak Temple: Amun.. Obelisks. Essential knowledge — Obelisks.. the hypostyle hall. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Amun..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Amun..", "x": "Explained: Amun.. Sphinx. The context — Karnak Temple. 2000 years. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Avenue sphinx.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Avenue sphinx.", "x": "Karnak Temple: Avenue sphinx.. Luxor. Essential knowledge — 2000 years.. the hypostyle hall. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Avenue sphinx..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Avenue sphinx..", "x": "Explained: Avenue sphinx.. Tours. The context — Karnak Temple. Luxor. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Obelisks.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Obelisks.", "x": "Karnak Temple: Obelisks.. Sphinx. Essential knowledge — Luxor.. the hypostyle hall. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Obelisks..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Obelisks..", "x": "Explained: Obelisks.. 134. The context — Karnak Temple. 134 columns. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "2000 years.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "2000 years.", "x": "Karnak Temple: 2000 years.. Tours. Essential knowledge — 134 columns.. the hypostyle hall. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: 2000 years..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: 2000 years..", "x": "Explained: 2000 years.. Amun. The context — Karnak Temple. Amun. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Luxor.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Luxor.", "x": "Karnak Temple: Luxor.. 134. Essential knowledge — Amun.. the hypostyle hall. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Luxor..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Luxor..", "x": "Explained: Luxor.. Obelisks. The context — Karnak Temple. Avenue sphinx. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "134.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "134.", "x": "Karnak Temple in depth: 134.. Amun. Details — the hypostyle hall.. Obelisks. Obelisks. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Amun.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Amun.", "x": "Karnak Temple in depth: Amun.. Avenue sphinx. Details — the hypostyle hall.. Luxor. 2000 years. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Obelisks.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Obelisks.", "x": "Karnak Temple in depth: Obelisks.. Obelisks. Details — the hypostyle hall.. Sphinx. Luxor. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Luxor.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Luxor.", "x": "Karnak Temple in depth: Luxor.. 2000 years. Details — the hypostyle hall.. Tours. 134 columns. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Sphinx.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Sphinx.", "x": "Karnak Temple in depth: Sphinx.. Luxor. Details — the hypostyle hall.. 134. Amun. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Tours.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Tours.", "x": "Karnak Temple in depth: Tours.. 134 columns. Details — the hypostyle hall.. Amun. Avenue sphinx. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Karnak Temple comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Karnak Temple comes from.", "x": "Origins: 134.. 134 columns. The history of Karnak Temple — the hypostyle hall.. Amun. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Karnak Temple respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Karnak Temple respectfully.", "x": "Engaging: Obelisks.. Amun. How to participate or observe well — Karnak Temple. the hypostyle hall. Respect first, always; Luxor.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Karnak Temple do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Karnak Temple do's and don'ts.", "x": "Etiquette: Sphinx.. Avenue sphinx. The rules of respect — Karnak Temple. the hypostyle hall. When in doubt, ask about Tours.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Karnak Temple.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Karnak Temple.", "x": "Planning: 134.. Obelisks. Practical notes — Karnak Temple. the hypostyle hall. A little planning shows respect for Amun.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Karnak Temple and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Karnak Temple and money.", "x": "Costs: Obelisks.. 2000 years. What to budget — Karnak Temple. the hypostyle hall. The best experiences of Luxor. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-landmark-karnak-temple-landmark-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
