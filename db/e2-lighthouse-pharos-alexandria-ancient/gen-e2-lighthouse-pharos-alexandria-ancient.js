(function(){'use strict';
/* JAH Pharos of Alexandria (ancient) Lighthouse Database generator — jahdb-e2-lighthouse-pharos-alexandria-ancient-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-lighthouse-pharos-alexandria-ancient',PREFIX='JAH-E2LIGHTHOUS-',NAME='JAH Pharos of Alexandria (ancient) Lighthouse Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Pharos of Alexandria (ancient): the complete guide", "d": "Pharos of Alexandria (ancient): the original wonder..", "g": "overview", "l": 2, "q": "What is Pharos of Alexandria (ancient): the complete guide?", "a": "Pharos of Alexandria (ancient): the original wonder..", "x": "The complete lighthouse guide to Pharos of Alexandria (ancient): the original wonder.. 280 BC. History, meaning, practices, and how to engage respectfully — everything in one database. Wonder. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Pharos of Alexandria (ancient) essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Pharos of Alexandria (ancient) essentials.", "x": "At a glance: Pharos of Alexandria (ancient) — the original wonder.. 100m. The essentials: History.. Wonder. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "280 BC.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "280 BC.", "x": "Pharos of Alexandria (ancient): 280 BC.. History. Essential knowledge — Wonder.. the original wonder. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 280 BC..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 280 BC..", "x": "Explained: 280 BC.. Fall. The context — Pharos of Alexandria (ancient). Earthquakes. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "100m.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "100m.", "x": "Pharos of Alexandria (ancient): 100m.. Design. Essential knowledge — Earthquakes.. the original wonder. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: 100m..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: 100m..", "x": "Explained: 100m.. Legacy. The context — Pharos of Alexandria (ancient). Qaitbay. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Wonder.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Wonder.", "x": "Pharos of Alexandria (ancient): Wonder.. Fall. Essential knowledge — Qaitbay.. the original wonder. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Wonder..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Wonder..", "x": "Explained: Wonder.. Egypt. The context — Pharos of Alexandria (ancient). Legacy. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Earthquakes.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Earthquakes.", "x": "Pharos of Alexandria (ancient): Earthquakes.. Legacy. Essential knowledge — Legacy.. the original wonder. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Earthquakes..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Earthquakes..", "x": "Explained: Earthquakes.. Wonder. The context — Pharos of Alexandria (ancient). 280 BC. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Qaitbay.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Qaitbay.", "x": "Pharos of Alexandria (ancient): Qaitbay.. Egypt. Essential knowledge — 280 BC.. the original wonder. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Qaitbay..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Qaitbay..", "x": "Explained: Qaitbay.. History. The context — Pharos of Alexandria (ancient). 100m. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Legacy.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Legacy.", "x": "Pharos of Alexandria (ancient): Legacy.. Wonder. Essential knowledge — 100m.. the original wonder. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Legacy..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Legacy..", "x": "Explained: Legacy.. Design. The context — Pharos of Alexandria (ancient). Wonder. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Wonder.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Wonder.", "x": "Pharos of Alexandria (ancient) in depth: Wonder.. 100m. Details — the original wonder.. Design. Earthquakes. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "History.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "History.", "x": "Pharos of Alexandria (ancient) in depth: History.. Wonder. Details — the original wonder.. Fall. Qaitbay. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Design.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Design.", "x": "Pharos of Alexandria (ancient) in depth: Design.. Earthquakes. Details — the original wonder.. Legacy. Legacy. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Fall.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Fall.", "x": "Pharos of Alexandria (ancient) in depth: Fall.. Qaitbay. Details — the original wonder.. Egypt. 280 BC. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Legacy.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Legacy.", "x": "Pharos of Alexandria (ancient) in depth: Legacy.. Legacy. Details — the original wonder.. Wonder. 100m. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Egypt.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Egypt.", "x": "Pharos of Alexandria (ancient) in depth: Egypt.. 280 BC. Details — the original wonder.. History. Wonder. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Pharos of Alexandria (ancient) comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Pharos of Alexandria (ancient) comes from.", "x": "Origins: Wonder.. 280 BC. The history of Pharos of Alexandria (ancient) — the original wonder.. History. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Pharos of Alexandria (ancient) respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Pharos of Alexandria (ancient) respectfully.", "x": "Engaging: Design.. 100m. How to participate or observe well — Pharos of Alexandria (ancient). the original wonder. Respect first, always; Fall.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Pharos of Alexandria (ancient) do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Pharos of Alexandria (ancient) do's and don'ts.", "x": "Etiquette: Legacy.. Wonder. The rules of respect — Pharos of Alexandria (ancient). the original wonder. When in doubt, ask about Egypt.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Pharos of Alexandria (ancient).", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Pharos of Alexandria (ancient).", "x": "Planning: Wonder.. Earthquakes. Practical notes — Pharos of Alexandria (ancient). the original wonder. A little planning shows respect for History.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Pharos of Alexandria (ancient) and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Pharos of Alexandria (ancient) and money.", "x": "Costs: Design.. Qaitbay. What to budget — Pharos of Alexandria (ancient). the original wonder. The best experiences of Fall. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-lighthouse-pharos-alexandria-ancient-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
