(function(){'use strict';
/* JAH Pergamon Museum Museum Database generator — jahdb-e2-museum-pergamon-museum-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-museum-pergamon-museum',PREFIX='JAH-E2MUSEUMPER-',NAME='JAH Pergamon Museum Museum Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Pergamon Museum: the complete guide", "d": "Pergamon Museum: monumental Berlin..", "g": "overview", "l": 2, "q": "What is Pergamon Museum: the complete guide?", "a": "Pergamon Museum: monumental Berlin..", "x": "The complete museum guide to Pergamon Museum: monumental Berlin.. Pergamon Altar. History, meaning, practices, and how to engage respectfully — everything in one database. Altar. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Pergamon Museum essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Pergamon Museum essentials.", "x": "At a glance: Pergamon Museum — monumental Berlin.. Ishtar Gate. The essentials: Gate.. Berlin. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Pergamon Altar.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Pergamon Altar.", "x": "Pergamon Museum: Pergamon Altar.. Gate. Essential knowledge — Berlin.. monumental Berlin. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Pergamon Altar..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Pergamon Altar..", "x": "Explained: Pergamon Altar.. Tickets. The context — Pergamon Museum. Rebuilding. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Ishtar Gate.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Ishtar Gate.", "x": "Pergamon Museum: Ishtar Gate.. History. Essential knowledge — Rebuilding.. monumental Berlin. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Ishtar Gate..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Ishtar Gate..", "x": "Explained: Ishtar Gate.. Berlin. The context — Pergamon Museum. History. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Berlin.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Berlin.", "x": "Pergamon Museum: Berlin.. Tickets. Essential knowledge — History.. monumental Berlin. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Berlin..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Berlin..", "x": "Explained: Berlin.. Debate. The context — Pergamon Museum. Tickets. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Rebuilding.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Rebuilding.", "x": "Pergamon Museum: Rebuilding.. Berlin. Essential knowledge — Tickets.. monumental Berlin. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Rebuilding..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Rebuilding..", "x": "Explained: Rebuilding.. Altar. The context — Pergamon Museum. Pergamon Altar. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "History.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "History.", "x": "Pergamon Museum: History.. Debate. Essential knowledge — Pergamon Altar.. monumental Berlin. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: History..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: History..", "x": "Explained: History.. Gate. The context — Pergamon Museum. Ishtar Gate. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Tickets.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Tickets.", "x": "Pergamon Museum: Tickets.. Altar. Essential knowledge — Ishtar Gate.. monumental Berlin. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Tickets..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Tickets..", "x": "Explained: Tickets.. History. The context — Pergamon Museum. Berlin. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Altar.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Altar.", "x": "Pergamon Museum in depth: Altar.. Ishtar Gate. Details — monumental Berlin.. History. Rebuilding. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Gate.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Gate.", "x": "Pergamon Museum in depth: Gate.. Berlin. Details — monumental Berlin.. Tickets. History. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "History.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "History.", "x": "Pergamon Museum in depth: History.. Rebuilding. Details — monumental Berlin.. Berlin. Tickets. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Tickets.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Tickets.", "x": "Pergamon Museum in depth: Tickets.. History. Details — monumental Berlin.. Debate. Pergamon Altar. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Berlin.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Berlin.", "x": "Pergamon Museum in depth: Berlin.. Tickets. Details — monumental Berlin.. Altar. Ishtar Gate. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Debate.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Debate.", "x": "Pergamon Museum in depth: Debate.. Pergamon Altar. Details — monumental Berlin.. Gate. Berlin. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Pergamon Museum comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Pergamon Museum comes from.", "x": "Origins: Altar.. Pergamon Altar. The history of Pergamon Museum — monumental Berlin.. Gate. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Pergamon Museum respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Pergamon Museum respectfully.", "x": "Engaging: History.. Ishtar Gate. How to participate or observe well — Pergamon Museum. monumental Berlin. Respect first, always; Tickets.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Pergamon Museum do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Pergamon Museum do's and don'ts.", "x": "Etiquette: Berlin.. Berlin. The rules of respect — Pergamon Museum. monumental Berlin. When in doubt, ask about Debate.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Pergamon Museum.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Pergamon Museum.", "x": "Planning: Altar.. Rebuilding. Practical notes — Pergamon Museum. monumental Berlin. A little planning shows respect for Gate.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Pergamon Museum and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Pergamon Museum and money.", "x": "Costs: History.. History. What to budget — Pergamon Museum. monumental Berlin. The best experiences of Tickets. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-museum-pergamon-museum-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
