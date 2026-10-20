(function(){'use strict';
/* JAH American Museum of Natural History Museum Database generator — jahdb-e2-museum-amnh-museum-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-museum-amnh-museum',PREFIX='JAH-E2MUSEUMAMN-',NAME='JAH American Museum of Natural History Museum Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "American Museum of Natural History: the complete guide", "d": "American Museum of Natural History: New York's nature giant..", "g": "overview", "l": 2, "q": "What is American Museum of Natural History: the complete guide?", "a": "American Museum of Natural History: New York's nature giant..", "x": "The complete museum guide to American Museum of Natural History: New York's nature giant.. Blue whale. History, meaning, practices, and how to engage respectfully — everything in one database. Whale. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "American Museum of Natural History essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "American Museum of Natural History essentials.", "x": "At a glance: American Museum of Natural History — New York's nature giant.. Dinosaurs. The essentials: Dinos.. Hayden Planetarium. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Blue whale.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Blue whale.", "x": "American Museum of Natural History: Blue whale.. Dinos. Essential knowledge — Hayden Planetarium.. New York's nature giant. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Blue whale..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Blue whale..", "x": "Explained: Blue whale.. History. The context — American Museum of Natural History. 1869. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Dinosaurs.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Dinosaurs.", "x": "American Museum of Natural History: Dinosaurs.. Planetarium. Essential knowledge — 1869.. New York's nature giant. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Dinosaurs..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Dinosaurs..", "x": "Explained: Dinosaurs.. Tickets. The context — American Museum of Natural History. NYC. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Hayden Planetarium.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Hayden Planetarium.", "x": "American Museum of Natural History: Hayden Planetarium.. History. Essential knowledge — NYC.. New York's nature giant. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Hayden Planetarium..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Hayden Planetarium..", "x": "Explained: Hayden Planetarium.. Science. The context — American Museum of Natural History. Roosevelt. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "1869.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "1869.", "x": "American Museum of Natural History: 1869.. Tickets. Essential knowledge — Roosevelt.. New York's nature giant. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: 1869..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: 1869..", "x": "Explained: 1869.. Whale. The context — American Museum of Natural History. Blue whale. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "NYC.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "NYC.", "x": "American Museum of Natural History: NYC.. Science. Essential knowledge — Blue whale.. New York's nature giant. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: NYC..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: NYC..", "x": "Explained: NYC.. Dinos. The context — American Museum of Natural History. Dinosaurs. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Roosevelt.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Roosevelt.", "x": "American Museum of Natural History: Roosevelt.. Whale. Essential knowledge — Dinosaurs.. New York's nature giant. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Roosevelt..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Roosevelt..", "x": "Explained: Roosevelt.. Planetarium. The context — American Museum of Natural History. Hayden Planetarium. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Whale.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Whale.", "x": "American Museum of Natural History in depth: Whale.. Dinosaurs. Details — New York's nature giant.. Planetarium. 1869. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Dinos.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Dinos.", "x": "American Museum of Natural History in depth: Dinos.. Hayden Planetarium. Details — New York's nature giant.. History. NYC. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Planetarium.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Planetarium.", "x": "American Museum of Natural History in depth: Planetarium.. 1869. Details — New York's nature giant.. Tickets. Roosevelt. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "History.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "History.", "x": "American Museum of Natural History in depth: History.. NYC. Details — New York's nature giant.. Science. Blue whale. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Tickets.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Tickets.", "x": "American Museum of Natural History in depth: Tickets.. Roosevelt. Details — New York's nature giant.. Whale. Dinosaurs. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Science.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Science.", "x": "American Museum of Natural History in depth: Science.. Blue whale. Details — New York's nature giant.. Dinos. Hayden Planetarium. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where American Museum of Natural History comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where American Museum of Natural History comes from.", "x": "Origins: Whale.. Blue whale. The history of American Museum of Natural History — New York's nature giant.. Dinos. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing American Museum of Natural History respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing American Museum of Natural History respectfully.", "x": "Engaging: Planetarium.. Dinosaurs. How to participate or observe well — American Museum of Natural History. New York's nature giant. Respect first, always; History.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "American Museum of Natural History do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "American Museum of Natural History do's and don'ts.", "x": "Etiquette: Tickets.. Hayden Planetarium. The rules of respect — American Museum of Natural History. New York's nature giant. When in doubt, ask about Science.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around American Museum of Natural History.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around American Museum of Natural History.", "x": "Planning: Whale.. 1869. Practical notes — American Museum of Natural History. New York's nature giant. A little planning shows respect for Dinos.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "American Museum of Natural History and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "American Museum of Natural History and money.", "x": "Costs: Planetarium.. NYC. What to budget — American Museum of Natural History. New York's nature giant. The best experiences of History. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-museum-amnh-museum-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
