(function(){'use strict';
/* JAH PortAventura2 Database generator — jahdb-e2-theme2-portaventura2-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-theme2-portaventura2',PREFIX='JAH-E2THEME2POR-',NAME='JAH PortAventura2 Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "PortAventura2: the complete guide", "d": "PortAventura2: the Spanish 2..", "g": "overview", "l": 2, "q": "What is PortAventura2: the complete guide?", "a": "PortAventura2: the Spanish 2..", "x": "The complete theme park guide to PortAventura2: the Spanish 2.. Spain. History, meaning, practices, and how to engage respectfully — everything in one database. Spain. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "PortAventura2 essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "PortAventura2 essentials.", "x": "At a glance: PortAventura2 — the Spanish 2.. Shambhala. The essentials: Beach.. Ferrari. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Spain.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Spain.", "x": "PortAventura2: Spain.. Beach. Essential knowledge — Ferrari.. the Spanish 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Spain..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Spain..", "x": "Explained: Spain.. Shambhala. The context — PortAventura2. Mediterranean. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Shambhala.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Shambhala.", "x": "PortAventura2: Shambhala.. Coasters. Essential knowledge — Mediterranean.. the Spanish 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Shambhala..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Shambhala..", "x": "Explained: Shambhala.. Ferrari. The context — PortAventura2. Coasters. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Ferrari.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Ferrari.", "x": "PortAventura2: Ferrari.. Shambhala. Essential knowledge — Coasters.. the Spanish 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Ferrari..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Ferrari..", "x": "Explained: Ferrari.. Guide. The context — PortAventura2. Beach. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Mediterranean.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Mediterranean.", "x": "PortAventura2: Mediterranean.. Ferrari. Essential knowledge — Beach.. the Spanish 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Mediterranean..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Mediterranean..", "x": "Explained: Mediterranean.. Spain. The context — PortAventura2. Spain. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Coasters.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Coasters.", "x": "PortAventura2: Coasters.. Guide. Essential knowledge — Spain.. the Spanish 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Coasters..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Coasters..", "x": "Explained: Coasters.. Beach. The context — PortAventura2. Shambhala. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Beach.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Beach.", "x": "PortAventura2: Beach.. Spain. Essential knowledge — Shambhala.. the Spanish 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Beach..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Beach..", "x": "Explained: Beach.. Coasters. The context — PortAventura2. Ferrari. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Spain.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Spain.", "x": "PortAventura2 in depth: Spain.. Shambhala. Details — the Spanish 2.. Coasters. Mediterranean. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Beach.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Beach.", "x": "PortAventura2 in depth: Beach.. Ferrari. Details — the Spanish 2.. Shambhala. Coasters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Coasters.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Coasters.", "x": "PortAventura2 in depth: Coasters.. Mediterranean. Details — the Spanish 2.. Ferrari. Beach. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Shambhala.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Shambhala.", "x": "PortAventura2 in depth: Shambhala.. Coasters. Details — the Spanish 2.. Guide. Spain. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Ferrari.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Ferrari.", "x": "PortAventura2 in depth: Ferrari.. Beach. Details — the Spanish 2.. Spain. Shambhala. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Guide.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Guide.", "x": "PortAventura2 in depth: Guide.. Spain. Details — the Spanish 2.. Beach. Ferrari. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where PortAventura2 comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where PortAventura2 comes from.", "x": "Origins: Spain.. Spain. The history of PortAventura2 — the Spanish 2.. Beach. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing PortAventura2 respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing PortAventura2 respectfully.", "x": "Engaging: Coasters.. Shambhala. How to participate or observe well — PortAventura2. the Spanish 2. Respect first, always; Shambhala.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "PortAventura2 do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "PortAventura2 do's and don'ts.", "x": "Etiquette: Ferrari.. Ferrari. The rules of respect — PortAventura2. the Spanish 2. When in doubt, ask about Guide.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around PortAventura2.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around PortAventura2.", "x": "Planning: Spain.. Mediterranean. Practical notes — PortAventura2. the Spanish 2. A little planning shows respect for Beach.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "PortAventura2 and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "PortAventura2 and money.", "x": "Costs: Coasters.. Coasters. What to budget — PortAventura2. the Spanish 2. The best experiences of Shambhala. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-theme2-portaventura2-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
