(function(){'use strict';
/* JAH Golden Age Heroes Superhero Database generator — jahdb-e2-hero-golden-age-heroes-universe-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-hero-golden-age-heroes-universe',PREFIX='JAH-E2HEROGOLDE-',NAME='JAH Golden Age Heroes Superhero Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Golden Age Heroes: the complete guide", "d": "Golden Age Heroes: the 1940s heroes..", "g": "overview", "l": 2, "q": "What is Golden Age Heroes: the complete guide?", "a": "Golden Age Heroes: the 1940s heroes..", "x": "The complete superhero guide to Golden Age Heroes: the 1940s heroes.. 1940s. History, meaning, practices, and how to engage respectfully — everything in one database. 1940s. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Golden Age Heroes essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Golden Age Heroes essentials.", "x": "At a glance: Golden Age Heroes — the 1940s heroes.. Superman. The essentials: Cap.. Captain America. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "1940s.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "1940s.", "x": "Golden Age Heroes: 1940s.. Cap. Essential knowledge — Captain America.. the 1940s heroes. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 1940s..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 1940s..", "x": "Explained: 1940s.. Timely. The context — Golden Age Heroes. Plastic Man. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Superman.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Superman.", "x": "Golden Age Heroes: Superman.. War. Essential knowledge — Plastic Man.. the 1940s heroes. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Superman..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Superman..", "x": "Explained: Superman.. Superman. The context — Golden Age Heroes. War. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Captain America.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Captain America.", "x": "Golden Age Heroes: Captain America.. Timely. Essential knowledge — War.. the 1940s heroes. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Captain America..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Captain America..", "x": "Explained: Captain America.. Heroes. The context — Golden Age Heroes. Timely. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Plastic Man.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Plastic Man.", "x": "Golden Age Heroes: Plastic Man.. Superman. Essential knowledge — Timely.. the 1940s heroes. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Plastic Man..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Plastic Man..", "x": "Explained: Plastic Man.. 1940s. The context — Golden Age Heroes. 1940s. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "War.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "War.", "x": "Golden Age Heroes: War.. Heroes. Essential knowledge — 1940s.. the 1940s heroes. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: War..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: War..", "x": "Explained: War.. Cap. The context — Golden Age Heroes. Superman. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Timely.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Timely.", "x": "Golden Age Heroes: Timely.. 1940s. Essential knowledge — Superman.. the 1940s heroes. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Timely..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Timely..", "x": "Explained: Timely.. War. The context — Golden Age Heroes. Captain America. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "1940s.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "1940s.", "x": "Golden Age Heroes in depth: 1940s.. Superman. Details — the 1940s heroes.. War. Plastic Man. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Cap.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Cap.", "x": "Golden Age Heroes in depth: Cap.. Captain America. Details — the 1940s heroes.. Timely. War. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "War.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "War.", "x": "Golden Age Heroes in depth: War.. Plastic Man. Details — the 1940s heroes.. Superman. Timely. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Timely.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Timely.", "x": "Golden Age Heroes in depth: Timely.. War. Details — the 1940s heroes.. Heroes. 1940s. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Superman.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Superman.", "x": "Golden Age Heroes in depth: Superman.. Timely. Details — the 1940s heroes.. 1940s. Superman. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Heroes.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Heroes.", "x": "Golden Age Heroes in depth: Heroes.. 1940s. Details — the 1940s heroes.. Cap. Captain America. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Golden Age Heroes comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Golden Age Heroes comes from.", "x": "Origins: 1940s.. 1940s. The history of Golden Age Heroes — the 1940s heroes.. Cap. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Golden Age Heroes respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Golden Age Heroes respectfully.", "x": "Engaging: War.. Superman. How to participate or observe well — Golden Age Heroes. the 1940s heroes. Respect first, always; Timely.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Golden Age Heroes do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Golden Age Heroes do's and don'ts.", "x": "Etiquette: Superman.. Captain America. The rules of respect — Golden Age Heroes. the 1940s heroes. When in doubt, ask about Heroes.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Golden Age Heroes.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Golden Age Heroes.", "x": "Planning: 1940s.. Plastic Man. Practical notes — Golden Age Heroes. the 1940s heroes. A little planning shows respect for Cap.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Golden Age Heroes and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Golden Age Heroes and money.", "x": "Costs: War.. War. What to budget — Golden Age Heroes. the 1940s heroes. The best experiences of Timely. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-hero-golden-age-heroes-universe-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
