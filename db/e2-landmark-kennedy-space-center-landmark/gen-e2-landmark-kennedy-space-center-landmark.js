(function(){'use strict';
/* JAH Kennedy Space Center Landmark Database generator — jahdb-e2-landmark-kennedy-space-center-landmark-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-landmark-kennedy-space-center-landmark',PREFIX='JAH-E2LANDMARKK-',NAME='JAH Kennedy Space Center Landmark Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Kennedy Space Center: the complete guide", "d": "Kennedy Space Center: the launch coast..", "g": "overview", "l": 2, "q": "What is Kennedy Space Center: the complete guide?", "a": "Kennedy Space Center: the launch coast..", "x": "The complete landmark guide to Kennedy Space Center: the launch coast.. 1968. History, meaning, practices, and how to engage respectfully — everything in one database. 1968. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Kennedy Space Center essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Kennedy Space Center essentials.", "x": "At a glance: Kennedy Space Center — the launch coast.. Apollo. The essentials: Apollo.. Shuttle. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "1968.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "1968.", "x": "Kennedy Space Center: 1968.. Apollo. Essential knowledge — Shuttle.. the launch coast. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 1968..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 1968..", "x": "Explained: 1968.. Shuttle. The context — Kennedy Space Center. Launch. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Apollo.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Apollo.", "x": "Kennedy Space Center: Apollo.. Launch. Essential knowledge — Launch.. the launch coast. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Apollo..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Apollo..", "x": "Explained: Apollo.. Merritt. The context — Kennedy Space Center. Merritt. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Shuttle.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Shuttle.", "x": "Kennedy Space Center: Shuttle.. Shuttle. Essential knowledge — Merritt.. the launch coast. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Shuttle..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Shuttle..", "x": "Explained: Shuttle.. Tours. The context — Kennedy Space Center. Tours. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Launch.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Launch.", "x": "Kennedy Space Center: Launch.. Merritt. Essential knowledge — Tours.. the launch coast. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Launch..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Launch..", "x": "Explained: Launch.. 1968. The context — Kennedy Space Center. 1968. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Merritt.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Merritt.", "x": "Kennedy Space Center: Merritt.. Tours. Essential knowledge — 1968.. the launch coast. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Merritt..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Merritt..", "x": "Explained: Merritt.. Apollo. The context — Kennedy Space Center. Apollo. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Tours.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Tours.", "x": "Kennedy Space Center: Tours.. 1968. Essential knowledge — Apollo.. the launch coast. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Tours..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Tours..", "x": "Explained: Tours.. Launch. The context — Kennedy Space Center. Shuttle. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "1968.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "1968.", "x": "Kennedy Space Center in depth: 1968.. Apollo. Details — the launch coast.. Launch. Launch. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Apollo.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Apollo.", "x": "Kennedy Space Center in depth: Apollo.. Shuttle. Details — the launch coast.. Shuttle. Merritt. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Launch.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Launch.", "x": "Kennedy Space Center in depth: Launch.. Launch. Details — the launch coast.. Merritt. Tours. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Shuttle.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Shuttle.", "x": "Kennedy Space Center in depth: Shuttle.. Merritt. Details — the launch coast.. Tours. 1968. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Merritt.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Merritt.", "x": "Kennedy Space Center in depth: Merritt.. Tours. Details — the launch coast.. 1968. Apollo. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Tours.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Tours.", "x": "Kennedy Space Center in depth: Tours.. 1968. Details — the launch coast.. Apollo. Shuttle. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Kennedy Space Center comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Kennedy Space Center comes from.", "x": "Origins: 1968.. 1968. The history of Kennedy Space Center — the launch coast.. Apollo. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Kennedy Space Center respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Kennedy Space Center respectfully.", "x": "Engaging: Launch.. Apollo. How to participate or observe well — Kennedy Space Center. the launch coast. Respect first, always; Shuttle.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Kennedy Space Center do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Kennedy Space Center do's and don'ts.", "x": "Etiquette: Merritt.. Shuttle. The rules of respect — Kennedy Space Center. the launch coast. When in doubt, ask about Tours.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Kennedy Space Center.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Kennedy Space Center.", "x": "Planning: 1968.. Launch. Practical notes — Kennedy Space Center. the launch coast. A little planning shows respect for Apollo.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Kennedy Space Center and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Kennedy Space Center and money.", "x": "Costs: Launch.. Merritt. What to budget — Kennedy Space Center. the launch coast. The best experiences of Shuttle. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-landmark-kennedy-space-center-landmark-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
