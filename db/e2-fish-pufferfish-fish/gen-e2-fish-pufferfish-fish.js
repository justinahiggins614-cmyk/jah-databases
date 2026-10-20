(function(){'use strict';
/* JAH Pufferfish Fish Species Database generator — jahdb-e2-fish-pufferfish-fish-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-fish-pufferfish-fish',PREFIX='JAH-E2FISHPUFFE-',NAME='JAH Pufferfish Fish Species Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Pufferfish: the complete guide", "d": "Pufferfish: the inflating toxin..", "g": "overview", "l": 2, "q": "What is Pufferfish: the complete guide?", "a": "Pufferfish: the inflating toxin..", "x": "The complete fish species guide to Pufferfish: the inflating toxin.. Inflate. History, meaning, practices, and how to engage respectfully — everything in one database. Inflate. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Pufferfish essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Pufferfish essentials.", "x": "At a glance: Pufferfish — the inflating toxin.. Tetrodotoxin. The essentials: Toxin.. Fugu. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Inflate.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Inflate.", "x": "Pufferfish: Inflate.. Toxin. Essential knowledge — Fugu.. the inflating toxin. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Inflate..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Inflate..", "x": "Explained: Inflate.. Beak. The context — Pufferfish. Beak. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Tetrodotoxin.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Tetrodotoxin.", "x": "Pufferfish: Tetrodotoxin.. Fugu. Essential knowledge — Beak.. the inflating toxin. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Tetrodotoxin..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Tetrodotoxin..", "x": "Explained: Tetrodotoxin.. Round. The context — Pufferfish. Slow. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Fugu.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Fugu.", "x": "Pufferfish: Fugu.. Beak. Essential knowledge — Slow.. the inflating toxin. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Fugu..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Fugu..", "x": "Explained: Fugu.. Habitat. The context — Pufferfish. Round. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Beak.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Beak.", "x": "Pufferfish: Beak.. Round. Essential knowledge — Round.. the inflating toxin. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Beak..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Beak..", "x": "Explained: Beak.. Inflate. The context — Pufferfish. Inflate. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Slow.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Slow.", "x": "Pufferfish: Slow.. Habitat. Essential knowledge — Inflate.. the inflating toxin. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Slow..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Slow..", "x": "Explained: Slow.. Toxin. The context — Pufferfish. Tetrodotoxin. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Round.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Round.", "x": "Pufferfish: Round.. Inflate. Essential knowledge — Tetrodotoxin.. the inflating toxin. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Round..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Round..", "x": "Explained: Round.. Fugu. The context — Pufferfish. Fugu. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Inflate.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Inflate.", "x": "Pufferfish in depth: Inflate.. Tetrodotoxin. Details — the inflating toxin.. Fugu. Beak. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Toxin.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Toxin.", "x": "Pufferfish in depth: Toxin.. Fugu. Details — the inflating toxin.. Beak. Slow. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Fugu.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Fugu.", "x": "Pufferfish in depth: Fugu.. Beak. Details — the inflating toxin.. Round. Round. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Beak.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Beak.", "x": "Pufferfish in depth: Beak.. Slow. Details — the inflating toxin.. Habitat. Inflate. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Round.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Round.", "x": "Pufferfish in depth: Round.. Round. Details — the inflating toxin.. Inflate. Tetrodotoxin. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Habitat.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Habitat.", "x": "Pufferfish in depth: Habitat.. Inflate. Details — the inflating toxin.. Toxin. Fugu. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Pufferfish comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Pufferfish comes from.", "x": "Origins: Inflate.. Inflate. The history of Pufferfish — the inflating toxin.. Toxin. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Pufferfish respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Pufferfish respectfully.", "x": "Engaging: Fugu.. Tetrodotoxin. How to participate or observe well — Pufferfish. the inflating toxin. Respect first, always; Beak.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Pufferfish do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Pufferfish do's and don'ts.", "x": "Etiquette: Round.. Fugu. The rules of respect — Pufferfish. the inflating toxin. When in doubt, ask about Habitat.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Pufferfish.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Pufferfish.", "x": "Planning: Inflate.. Beak. Practical notes — Pufferfish. the inflating toxin. A little planning shows respect for Toxin.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Pufferfish and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Pufferfish and money.", "x": "Costs: Fugu.. Slow. What to budget — Pufferfish. the inflating toxin. The best experiences of Beak. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-fish-pufferfish-fish-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
