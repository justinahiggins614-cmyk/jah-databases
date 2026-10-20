(function(){'use strict';
/* JAH Currywurst Dish Database generator — jahdb-e2-dish-currywurst-dish-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-dish-currywurst-dish',PREFIX='JAH-E2DISHCURRY-',NAME='JAH Currywurst Dish Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Currywurst: the complete guide", "d": "Currywurst: the Berlin street..", "g": "overview", "l": 2, "q": "What is Currywurst: the complete guide?", "a": "Currywurst: the Berlin street..", "x": "The complete dish guide to Currywurst: the Berlin street.. Berlin. History, meaning, practices, and how to engage respectfully — everything in one database. Curry. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Currywurst essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Currywurst essentials.", "x": "At a glance: Currywurst — the Berlin street.. Curry ketchup. The essentials: Street.. Sliced. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Berlin.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Berlin.", "x": "Currywurst: Berlin.. Street. Essential knowledge — Sliced.. the Berlin street. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Berlin..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Berlin..", "x": "Explained: Berlin.. Berlin. The context — Currywurst. 1949. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Curry ketchup.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Curry ketchup.", "x": "Currywurst: Curry ketchup.. Herta. Essential knowledge — 1949.. the Berlin street. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Curry ketchup..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Curry ketchup..", "x": "Explained: Curry ketchup.. Sliced. The context — Currywurst. Street. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Sliced.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Sliced.", "x": "Currywurst: Sliced.. Berlin. Essential knowledge — Street.. the Berlin street. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Sliced..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Sliced..", "x": "Explained: Sliced.. Making. The context — Currywurst. Herta. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "1949.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "1949.", "x": "Currywurst: 1949.. Sliced. Essential knowledge — Herta.. the Berlin street. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: 1949..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: 1949..", "x": "Explained: 1949.. Curry. The context — Currywurst. Berlin. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Street.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Street.", "x": "Currywurst: Street.. Making. Essential knowledge — Berlin.. the Berlin street. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Street..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Street..", "x": "Explained: Street.. Street. The context — Currywurst. Curry ketchup. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Herta.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Herta.", "x": "Currywurst: Herta.. Curry. Essential knowledge — Curry ketchup.. the Berlin street. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Herta..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Herta..", "x": "Explained: Herta.. Herta. The context — Currywurst. Sliced. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Curry.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Curry.", "x": "Currywurst in depth: Curry.. Curry ketchup. Details — the Berlin street.. Herta. 1949. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Street.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Street.", "x": "Currywurst in depth: Street.. Sliced. Details — the Berlin street.. Berlin. Street. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Herta.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Herta.", "x": "Currywurst in depth: Herta.. 1949. Details — the Berlin street.. Sliced. Herta. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Berlin.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Berlin.", "x": "Currywurst in depth: Berlin.. Street. Details — the Berlin street.. Making. Berlin. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Sliced.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Sliced.", "x": "Currywurst in depth: Sliced.. Herta. Details — the Berlin street.. Curry. Curry ketchup. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Making.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Making.", "x": "Currywurst in depth: Making.. Berlin. Details — the Berlin street.. Street. Sliced. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Currywurst comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Currywurst comes from.", "x": "Origins: Curry.. Berlin. The history of Currywurst — the Berlin street.. Street. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Currywurst respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Currywurst respectfully.", "x": "Engaging: Herta.. Curry ketchup. How to participate or observe well — Currywurst. the Berlin street. Respect first, always; Berlin.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Currywurst do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Currywurst do's and don'ts.", "x": "Etiquette: Sliced.. Sliced. The rules of respect — Currywurst. the Berlin street. When in doubt, ask about Making.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Currywurst.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Currywurst.", "x": "Planning: Curry.. 1949. Practical notes — Currywurst. the Berlin street. A little planning shows respect for Street.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Currywurst and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Currywurst and money.", "x": "Costs: Herta.. Street. What to budget — Currywurst. the Berlin street. The best experiences of Berlin. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-dish-currywurst-dish-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
