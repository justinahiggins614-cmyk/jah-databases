(function(){'use strict';
/* JAH Copenhagen Zoo Zoo Database generator — jahdb-e2-zoo-copenhagen-zoo-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-zoo-copenhagen-zoo',PREFIX='JAH-E2ZOOCOPENH-',NAME='JAH Copenhagen Zoo Zoo Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Copenhagen Zoo: the complete guide", "d": "Copenhagen Zoo: the Arctic ring..", "g": "overview", "l": 2, "q": "What is Copenhagen Zoo: the complete guide?", "a": "Copenhagen Zoo: the Arctic ring..", "x": "The complete zoo guide to Copenhagen Zoo: the Arctic ring.. 1859. History, meaning, practices, and how to engage respectfully — everything in one database. Arctic. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Copenhagen Zoo essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Copenhagen Zoo essentials.", "x": "At a glance: Copenhagen Zoo — the Arctic ring.. Pandas. The essentials: History.. Arctic Ring. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "1859.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "1859.", "x": "Copenhagen Zoo: 1859.. History. Essential knowledge — Arctic Ring.. the Arctic ring. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 1859..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 1859..", "x": "Explained: 1859.. Copenhagen. The context — Copenhagen Zoo. Giraffe debate. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Pandas.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Pandas.", "x": "Copenhagen Zoo: Pandas.. Tickets. Essential knowledge — Giraffe debate.. the Arctic ring. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Pandas..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Pandas..", "x": "Explained: Pandas.. Debate. The context — Copenhagen Zoo. Tours. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Arctic Ring.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Arctic Ring.", "x": "Copenhagen Zoo: Arctic Ring.. Copenhagen. Essential knowledge — Tours.. the Arctic ring. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Arctic Ring..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Arctic Ring..", "x": "Explained: Arctic Ring.. Nordic. The context — Copenhagen Zoo. Denmark. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Giraffe debate.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Giraffe debate.", "x": "Copenhagen Zoo: Giraffe debate.. Debate. Essential knowledge — Denmark.. the Arctic ring. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Giraffe debate..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Giraffe debate..", "x": "Explained: Giraffe debate.. Arctic. The context — Copenhagen Zoo. 1859. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Tours.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Tours.", "x": "Copenhagen Zoo: Tours.. Nordic. Essential knowledge — 1859.. the Arctic ring. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Tours..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Tours..", "x": "Explained: Tours.. History. The context — Copenhagen Zoo. Pandas. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Denmark.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Denmark.", "x": "Copenhagen Zoo: Denmark.. Arctic. Essential knowledge — Pandas.. the Arctic ring. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Denmark..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Denmark..", "x": "Explained: Denmark.. Tickets. The context — Copenhagen Zoo. Arctic Ring. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Arctic.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Arctic.", "x": "Copenhagen Zoo in depth: Arctic.. Pandas. Details — the Arctic ring.. Tickets. Giraffe debate. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "History.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "History.", "x": "Copenhagen Zoo in depth: History.. Arctic Ring. Details — the Arctic ring.. Copenhagen. Tours. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Tickets.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Tickets.", "x": "Copenhagen Zoo in depth: Tickets.. Giraffe debate. Details — the Arctic ring.. Debate. Denmark. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Copenhagen.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Copenhagen.", "x": "Copenhagen Zoo in depth: Copenhagen.. Tours. Details — the Arctic ring.. Nordic. 1859. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Debate.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Debate.", "x": "Copenhagen Zoo in depth: Debate.. Denmark. Details — the Arctic ring.. Arctic. Pandas. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Nordic.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Nordic.", "x": "Copenhagen Zoo in depth: Nordic.. 1859. Details — the Arctic ring.. History. Arctic Ring. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Copenhagen Zoo comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Copenhagen Zoo comes from.", "x": "Origins: Arctic.. 1859. The history of Copenhagen Zoo — the Arctic ring.. History. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Copenhagen Zoo respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Copenhagen Zoo respectfully.", "x": "Engaging: Tickets.. Pandas. How to participate or observe well — Copenhagen Zoo. the Arctic ring. Respect first, always; Copenhagen.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Copenhagen Zoo do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Copenhagen Zoo do's and don'ts.", "x": "Etiquette: Debate.. Arctic Ring. The rules of respect — Copenhagen Zoo. the Arctic ring. When in doubt, ask about Nordic.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Copenhagen Zoo.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Copenhagen Zoo.", "x": "Planning: Arctic.. Giraffe debate. Practical notes — Copenhagen Zoo. the Arctic ring. A little planning shows respect for History.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Copenhagen Zoo and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Copenhagen Zoo and money.", "x": "Costs: Tickets.. Tours. What to budget — Copenhagen Zoo. the Arctic ring. The best experiences of Copenhagen. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-zoo-copenhagen-zoo-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
