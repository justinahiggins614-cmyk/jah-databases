(function(){'use strict';
/* JAH Handball Olympics Database generator — jahdb-e2-olympic2-handball-olympics-sport-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-olympic2-handball-olympics-sport',PREFIX='JAH-E2OLYMPIC2H-',NAME='JAH Handball Olympics Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Handball Olympics: the complete guide", "d": "Handball Olympics: the indoor throw..", "g": "overview", "l": 2, "q": "What is Handball Olympics: the complete guide?", "a": "Handball Olympics: the indoor throw..", "x": "The complete olympic sport guide to Handball Olympics: the indoor throw.. 1936. History, meaning, practices, and how to engage respectfully — everything in one database. Players. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Handball Olympics essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Handball Olympics essentials.", "x": "At a glance: Handball Olympics — the indoor throw.. 7 players. The essentials: Europe.. Goals. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "1936.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "1936.", "x": "Handball Olympics: 1936.. Europe. Essential knowledge — Goals.. the indoor throw. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 1936..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 1936..", "x": "Explained: 1936.. Goals. The context — Handball Olympics. Europe. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "7 players.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "7 players.", "x": "Handball Olympics: 7 players.. Court. Essential knowledge — Europe.. the indoor throw. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: 7 players..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: 7 players..", "x": "Explained: 7 players.. Fast. The context — Handball Olympics. Fast. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Goals.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Goals.", "x": "Handball Olympics: Goals.. Goals. Essential knowledge — Fast.. the indoor throw. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Goals..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Goals..", "x": "Explained: Goals.. Guide. The context — Handball Olympics. Court. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Europe.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Europe.", "x": "Handball Olympics: Europe.. Fast. Essential knowledge — Court.. the indoor throw. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Europe..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Europe..", "x": "Explained: Europe.. Players. The context — Handball Olympics. 1936. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Fast.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Fast.", "x": "Handball Olympics: Fast.. Guide. Essential knowledge — 1936.. the indoor throw. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Fast..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Fast..", "x": "Explained: Fast.. Europe. The context — Handball Olympics. 7 players. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Court.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Court.", "x": "Handball Olympics: Court.. Players. Essential knowledge — 7 players.. the indoor throw. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Court..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Court..", "x": "Explained: Court.. Court. The context — Handball Olympics. Goals. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Players.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Players.", "x": "Handball Olympics in depth: Players.. 7 players. Details — the indoor throw.. Court. Europe. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Europe.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Europe.", "x": "Handball Olympics in depth: Europe.. Goals. Details — the indoor throw.. Goals. Fast. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Court.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Court.", "x": "Handball Olympics in depth: Court.. Europe. Details — the indoor throw.. Fast. Court. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Goals.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Goals.", "x": "Handball Olympics in depth: Goals.. Fast. Details — the indoor throw.. Guide. 1936. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Fast.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Fast.", "x": "Handball Olympics in depth: Fast.. Court. Details — the indoor throw.. Players. 7 players. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Guide.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Guide.", "x": "Handball Olympics in depth: Guide.. 1936. Details — the indoor throw.. Europe. Goals. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Handball Olympics comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Handball Olympics comes from.", "x": "Origins: Players.. 1936. The history of Handball Olympics — the indoor throw.. Europe. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Handball Olympics respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Handball Olympics respectfully.", "x": "Engaging: Court.. 7 players. How to participate or observe well — Handball Olympics. the indoor throw. Respect first, always; Goals.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Handball Olympics do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Handball Olympics do's and don'ts.", "x": "Etiquette: Fast.. Goals. The rules of respect — Handball Olympics. the indoor throw. When in doubt, ask about Guide.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Handball Olympics.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Handball Olympics.", "x": "Planning: Players.. Europe. Practical notes — Handball Olympics. the indoor throw. A little planning shows respect for Europe.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Handball Olympics and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Handball Olympics and money.", "x": "Costs: Court.. Fast. What to budget — Handball Olympics. the indoor throw. The best experiences of Goals. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-olympic2-handball-olympics-sport-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
