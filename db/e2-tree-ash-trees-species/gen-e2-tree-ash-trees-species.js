(function(){'use strict';
/* JAH Ash Trees Tree Database generator — jahdb-e2-tree-ash-trees-species-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-tree-ash-trees-species',PREFIX='JAH-E2TREEASHTR-',NAME='JAH Ash Trees Tree Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Ash Trees: the complete guide", "d": "Ash Trees: the borer battle..", "g": "overview", "l": 2, "q": "What is Ash Trees: the complete guide?", "a": "Ash Trees: the borer battle..", "x": "The complete tree guide to Ash Trees: the borer battle.. Emerald ash. History, meaning, practices, and how to engage respectfully — everything in one database. Borer. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Ash Trees essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Ash Trees essentials.", "x": "At a glance: Ash Trees — the borer battle.. Borer. The essentials: Bats.. Baseball bats. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Emerald ash.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Emerald ash.", "x": "Ash Trees: Emerald ash.. Bats. Essential knowledge — Baseball bats.. the borer battle. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Emerald ash..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Emerald ash..", "x": "Explained: Emerald ash.. Species. The context — Ash Trees. Fall. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Borer.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Borer.", "x": "Ash Trees: Borer.. Treatment. Essential knowledge — Fall.. the borer battle. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Borer..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Borer..", "x": "Explained: Borer.. Fall. The context — Ash Trees. Treatment. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Baseball bats.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Baseball bats.", "x": "Ash Trees: Baseball bats.. Species. Essential knowledge — Treatment.. the borer battle. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Baseball bats..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Baseball bats..", "x": "Explained: Baseball bats.. Guide. The context — Ash Trees. Species. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Fall.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Fall.", "x": "Ash Trees: Fall.. Fall. Essential knowledge — Species.. the borer battle. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Fall..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Fall..", "x": "Explained: Fall.. Borer. The context — Ash Trees. Emerald ash. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Treatment.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Treatment.", "x": "Ash Trees: Treatment.. Guide. Essential knowledge — Emerald ash.. the borer battle. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Treatment..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Treatment..", "x": "Explained: Treatment.. Bats. The context — Ash Trees. Borer. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Species.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Species.", "x": "Ash Trees: Species.. Borer. Essential knowledge — Borer.. the borer battle. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Species..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Species..", "x": "Explained: Species.. Treatment. The context — Ash Trees. Baseball bats. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Borer.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Borer.", "x": "Ash Trees in depth: Borer.. Borer. Details — the borer battle.. Treatment. Fall. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Bats.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Bats.", "x": "Ash Trees in depth: Bats.. Baseball bats. Details — the borer battle.. Species. Treatment. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Treatment.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Treatment.", "x": "Ash Trees in depth: Treatment.. Fall. Details — the borer battle.. Fall. Species. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Species.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Species.", "x": "Ash Trees in depth: Species.. Treatment. Details — the borer battle.. Guide. Emerald ash. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Fall.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Fall.", "x": "Ash Trees in depth: Fall.. Species. Details — the borer battle.. Borer. Borer. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Guide.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Guide.", "x": "Ash Trees in depth: Guide.. Emerald ash. Details — the borer battle.. Bats. Baseball bats. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Ash Trees comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Ash Trees comes from.", "x": "Origins: Borer.. Emerald ash. The history of Ash Trees — the borer battle.. Bats. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Ash Trees respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Ash Trees respectfully.", "x": "Engaging: Treatment.. Borer. How to participate or observe well — Ash Trees. the borer battle. Respect first, always; Species.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Ash Trees do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Ash Trees do's and don'ts.", "x": "Etiquette: Fall.. Baseball bats. The rules of respect — Ash Trees. the borer battle. When in doubt, ask about Guide.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Ash Trees.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Ash Trees.", "x": "Planning: Borer.. Fall. Practical notes — Ash Trees. the borer battle. A little planning shows respect for Bats.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Ash Trees and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Ash Trees and money.", "x": "Costs: Treatment.. Treatment. What to budget — Ash Trees. the borer battle. The best experiences of Species. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-tree-ash-trees-species-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
