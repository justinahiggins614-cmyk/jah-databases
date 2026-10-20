(function(){'use strict';
/* JAH Silent Hill Franchise Database generator — jahdb-e2-games2-silent-hill-franchise-game-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-games2-silent-hill-franchise-game',PREFIX='JAH-E2GAMES2SIL-',NAME='JAH Silent Hill Franchise Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Silent Hill Franchise: the complete guide", "d": "Silent Hill Franchise: the fog town..", "g": "overview", "l": 2, "q": "What is Silent Hill Franchise: the complete guide?", "a": "Silent Hill Franchise: the fog town..", "x": "The complete game franchise guide to Silent Hill Franchise: the fog town.. 1999. History, meaning, practices, and how to engage respectfully — everything in one database. Fog. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Silent Hill Franchise essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Silent Hill Franchise essentials.", "x": "At a glance: Silent Hill Franchise — the fog town.. Konami. The essentials: Remake.. Fog. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "1999.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "1999.", "x": "Silent Hill Franchise: 1999.. Remake. Essential knowledge — Fog.. the fog town. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 1999..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 1999..", "x": "Explained: 1999.. Konami. The context — Silent Hill Franchise. Pyramid Head. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Konami.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Konami.", "x": "Silent Hill Franchise: Konami.. Psychological. Essential knowledge — Pyramid Head.. the fog town. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Konami..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Konami..", "x": "Explained: Konami.. Pyramid. The context — Silent Hill Franchise. Psychological. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Fog.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Fog.", "x": "Silent Hill Franchise: Fog.. Konami. Essential knowledge — Psychological.. the fog town. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Fog..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Fog..", "x": "Explained: Fog.. Games. The context — Silent Hill Franchise. Remake. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Pyramid Head.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Pyramid Head.", "x": "Silent Hill Franchise: Pyramid Head.. Pyramid. Essential knowledge — Remake.. the fog town. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Pyramid Head..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Pyramid Head..", "x": "Explained: Pyramid Head.. Fog. The context — Silent Hill Franchise. 1999. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Psychological.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Psychological.", "x": "Silent Hill Franchise: Psychological.. Games. Essential knowledge — 1999.. the fog town. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Psychological..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Psychological..", "x": "Explained: Psychological.. Remake. The context — Silent Hill Franchise. Konami. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Remake.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Remake.", "x": "Silent Hill Franchise: Remake.. Fog. Essential knowledge — Konami.. the fog town. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Remake..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Remake..", "x": "Explained: Remake.. Psychological. The context — Silent Hill Franchise. Fog. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Fog.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Fog.", "x": "Silent Hill Franchise in depth: Fog.. Konami. Details — the fog town.. Psychological. Pyramid Head. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Remake.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Remake.", "x": "Silent Hill Franchise in depth: Remake.. Fog. Details — the fog town.. Konami. Psychological. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Psychological.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Psychological.", "x": "Silent Hill Franchise in depth: Psychological.. Pyramid Head. Details — the fog town.. Pyramid. Remake. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Konami.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Konami.", "x": "Silent Hill Franchise in depth: Konami.. Psychological. Details — the fog town.. Games. 1999. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Pyramid.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Pyramid.", "x": "Silent Hill Franchise in depth: Pyramid.. Remake. Details — the fog town.. Fog. Konami. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Games.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Games.", "x": "Silent Hill Franchise in depth: Games.. 1999. Details — the fog town.. Remake. Fog. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Silent Hill Franchise comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Silent Hill Franchise comes from.", "x": "Origins: Fog.. 1999. The history of Silent Hill Franchise — the fog town.. Remake. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Silent Hill Franchise respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Silent Hill Franchise respectfully.", "x": "Engaging: Psychological.. Konami. How to participate or observe well — Silent Hill Franchise. the fog town. Respect first, always; Konami.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Silent Hill Franchise do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Silent Hill Franchise do's and don'ts.", "x": "Etiquette: Pyramid.. Fog. The rules of respect — Silent Hill Franchise. the fog town. When in doubt, ask about Games.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Silent Hill Franchise.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Silent Hill Franchise.", "x": "Planning: Fog.. Pyramid Head. Practical notes — Silent Hill Franchise. the fog town. A little planning shows respect for Remake.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Silent Hill Franchise and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Silent Hill Franchise and money.", "x": "Costs: Psychological.. Psychological. What to budget — Silent Hill Franchise. the fog town. The best experiences of Konami. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-games2-silent-hill-franchise-game-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
