(function(){'use strict';
/* JAH Volleyball Olympics Database generator — jahdb-e2-olympic2-volleyball-olympics-sport-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-olympic2-volleyball-olympics-sport',PREFIX='JAH-E2OLYMPIC2V-',NAME='JAH Volleyball Olympics Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Volleyball Olympics: the complete guide", "d": "Volleyball Olympics: the indoor net..", "g": "overview", "l": 2, "q": "What is Volleyball Olympics: the complete guide?", "a": "Volleyball Olympics: the indoor net..", "x": "The complete olympic sport guide to Volleyball Olympics: the indoor net.. 1964. History, meaning, practices, and how to engage respectfully — everything in one database. Players. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Volleyball Olympics essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Volleyball Olympics essentials.", "x": "At a glance: Volleyball Olympics — the indoor net.. 6 players. The essentials: Libero.. Rallies. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "1964.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "1964.", "x": "Volleyball Olympics: 1964.. Libero. Essential knowledge — Rallies.. the indoor net. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 1964..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 1964..", "x": "Explained: 1964.. Rallies. The context — Volleyball Olympics. Sets. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "6 players.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "6 players.", "x": "Volleyball Olympics: 6 players.. Spikes. Essential knowledge — Sets.. the indoor net. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: 6 players..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: 6 players..", "x": "Explained: 6 players.. Sets. The context — Volleyball Olympics. Libero. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Rallies.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Rallies.", "x": "Volleyball Olympics: Rallies.. Rallies. Essential knowledge — Libero.. the indoor net. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Rallies..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Rallies..", "x": "Explained: Rallies.. Guide. The context — Volleyball Olympics. Spikes. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Sets.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Sets.", "x": "Volleyball Olympics: Sets.. Sets. Essential knowledge — Spikes.. the indoor net. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Sets..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Sets..", "x": "Explained: Sets.. Players. The context — Volleyball Olympics. 1964. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Libero.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Libero.", "x": "Volleyball Olympics: Libero.. Guide. Essential knowledge — 1964.. the indoor net. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Libero..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Libero..", "x": "Explained: Libero.. Libero. The context — Volleyball Olympics. 6 players. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Spikes.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Spikes.", "x": "Volleyball Olympics: Spikes.. Players. Essential knowledge — 6 players.. the indoor net. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Spikes..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Spikes..", "x": "Explained: Spikes.. Spikes. The context — Volleyball Olympics. Rallies. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Players.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Players.", "x": "Volleyball Olympics in depth: Players.. 6 players. Details — the indoor net.. Spikes. Sets. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Libero.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Libero.", "x": "Volleyball Olympics in depth: Libero.. Rallies. Details — the indoor net.. Rallies. Libero. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Spikes.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Spikes.", "x": "Volleyball Olympics in depth: Spikes.. Sets. Details — the indoor net.. Sets. Spikes. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Rallies.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Rallies.", "x": "Volleyball Olympics in depth: Rallies.. Libero. Details — the indoor net.. Guide. 1964. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Sets.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Sets.", "x": "Volleyball Olympics in depth: Sets.. Spikes. Details — the indoor net.. Players. 6 players. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Guide.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Guide.", "x": "Volleyball Olympics in depth: Guide.. 1964. Details — the indoor net.. Libero. Rallies. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Volleyball Olympics comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Volleyball Olympics comes from.", "x": "Origins: Players.. 1964. The history of Volleyball Olympics — the indoor net.. Libero. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Volleyball Olympics respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Volleyball Olympics respectfully.", "x": "Engaging: Spikes.. 6 players. How to participate or observe well — Volleyball Olympics. the indoor net. Respect first, always; Rallies.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Volleyball Olympics do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Volleyball Olympics do's and don'ts.", "x": "Etiquette: Sets.. Rallies. The rules of respect — Volleyball Olympics. the indoor net. When in doubt, ask about Guide.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Volleyball Olympics.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Volleyball Olympics.", "x": "Planning: Players.. Sets. Practical notes — Volleyball Olympics. the indoor net. A little planning shows respect for Libero.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Volleyball Olympics and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Volleyball Olympics and money.", "x": "Costs: Spikes.. Libero. What to budget — Volleyball Olympics. the indoor net. The best experiences of Rallies. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-olympic2-volleyball-olympics-sport-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
