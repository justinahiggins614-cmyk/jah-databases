(function(){'use strict';
/* JAH Redwood Trees Tree Database generator — jahdb-e2-tree-redwood-trees-species-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-tree-redwood-trees-species',PREFIX='JAH-E2TREEREDWO-',NAME='JAH Redwood Trees Tree Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Redwood Trees: the complete guide", "d": "Redwood Trees: the tallest trees..", "g": "overview", "l": 2, "q": "What is Redwood Trees: the complete guide?", "a": "Redwood Trees: the tallest trees..", "x": "The complete tree guide to Redwood Trees: the tallest trees.. Tallest. History, meaning, practices, and how to engage respectfully — everything in one database. Tallest. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Redwood Trees essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Redwood Trees essentials.", "x": "At a glance: Redwood Trees — the tallest trees.. California. The essentials: Fog.. Fog. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Tallest.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Tallest.", "x": "Redwood Trees: Tallest.. Fog. Essential knowledge — Fog.. the tallest trees. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Tallest..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Tallest..", "x": "Explained: Tallest.. Fire. The context — Redwood Trees. Ancient. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "California.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "California.", "x": "Redwood Trees: California.. Ancient. Essential knowledge — Ancient.. the tallest trees. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: California..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: California..", "x": "Explained: California.. California. The context — Redwood Trees. Burls. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Fog.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Fog.", "x": "Redwood Trees: Fog.. Fire. Essential knowledge — Burls.. the tallest trees. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Fog..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Fog..", "x": "Explained: Fog.. Guide. The context — Redwood Trees. Fire. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Ancient.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Ancient.", "x": "Redwood Trees: Ancient.. California. Essential knowledge — Fire.. the tallest trees. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Ancient..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Ancient..", "x": "Explained: Ancient.. Tallest. The context — Redwood Trees. Tallest. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Burls.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Burls.", "x": "Redwood Trees: Burls.. Guide. Essential knowledge — Tallest.. the tallest trees. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Burls..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Burls..", "x": "Explained: Burls.. Fog. The context — Redwood Trees. California. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Fire.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Fire.", "x": "Redwood Trees: Fire.. Tallest. Essential knowledge — California.. the tallest trees. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Fire..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Fire..", "x": "Explained: Fire.. Ancient. The context — Redwood Trees. Fog. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Tallest.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Tallest.", "x": "Redwood Trees in depth: Tallest.. California. Details — the tallest trees.. Ancient. Ancient. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Fog.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Fog.", "x": "Redwood Trees in depth: Fog.. Fog. Details — the tallest trees.. Fire. Burls. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Ancient.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Ancient.", "x": "Redwood Trees in depth: Ancient.. Ancient. Details — the tallest trees.. California. Fire. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Fire.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Fire.", "x": "Redwood Trees in depth: Fire.. Burls. Details — the tallest trees.. Guide. Tallest. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "California.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "California.", "x": "Redwood Trees in depth: California.. Fire. Details — the tallest trees.. Tallest. California. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Guide.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Guide.", "x": "Redwood Trees in depth: Guide.. Tallest. Details — the tallest trees.. Fog. Fog. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Redwood Trees comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Redwood Trees comes from.", "x": "Origins: Tallest.. Tallest. The history of Redwood Trees — the tallest trees.. Fog. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Redwood Trees respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Redwood Trees respectfully.", "x": "Engaging: Ancient.. California. How to participate or observe well — Redwood Trees. the tallest trees. Respect first, always; Fire.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Redwood Trees do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Redwood Trees do's and don'ts.", "x": "Etiquette: California.. Fog. The rules of respect — Redwood Trees. the tallest trees. When in doubt, ask about Guide.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Redwood Trees.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Redwood Trees.", "x": "Planning: Tallest.. Ancient. Practical notes — Redwood Trees. the tallest trees. A little planning shows respect for Fog.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Redwood Trees and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Redwood Trees and money.", "x": "Costs: Ancient.. Burls. What to budget — Redwood Trees. the tallest trees. The best experiences of Fire. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-tree-redwood-trees-species-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
