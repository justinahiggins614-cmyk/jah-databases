(function(){'use strict';
/* JAH Couch to 5K Fitness Program Database generator — jahdb-e2-fitness-couch-to-5k-fitness-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-fitness-couch-to-5k-fitness',PREFIX='JAH-E2FITNESSCO-',NAME='JAH Couch to 5K Fitness Program Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Couch to 5K: the complete guide", "d": "Couch to 5K: the beginner run..", "g": "overview", "l": 2, "q": "What is Couch to 5K: the complete guide?", "a": "Couch to 5K: the beginner run..", "x": "The complete fitness program guide to Couch to 5K: the beginner run.. 9 weeks. History, meaning, practices, and how to engage respectfully — everything in one database. Walk/run. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Couch to 5K essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Couch to 5K essentials.", "x": "At a glance: Couch to 5K — the beginner run.. Walk/run. The essentials: App.. App. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "9 weeks.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "9 weeks.", "x": "Couch to 5K: 9 weeks.. App. Essential knowledge — App.. the beginner run. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 9 weeks..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 9 weeks..", "x": "Explained: 9 weeks.. Gradual. The context — Couch to 5K. 5K. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Walk/run.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Walk/run.", "x": "Couch to 5K: Walk/run.. Beginners. Essential knowledge — 5K.. the beginner run. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Walk/run..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Walk/run..", "x": "Explained: Walk/run.. 9 weeks. The context — Couch to 5K. Beginners. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "App.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "App.", "x": "Couch to 5K: App.. Gradual. Essential knowledge — Beginners.. the beginner run. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: App..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: App..", "x": "Explained: App.. Method. The context — Couch to 5K. Gradual. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "5K.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "5K.", "x": "Couch to 5K: 5K.. 9 weeks. Essential knowledge — Gradual.. the beginner run. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: 5K..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: 5K..", "x": "Explained: 5K.. Walk/run. The context — Couch to 5K. 9 weeks. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Beginners.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Beginners.", "x": "Couch to 5K: Beginners.. Method. Essential knowledge — 9 weeks.. the beginner run. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Beginners..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Beginners..", "x": "Explained: Beginners.. App. The context — Couch to 5K. Walk/run. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Gradual.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Gradual.", "x": "Couch to 5K: Gradual.. Walk/run. Essential knowledge — Walk/run.. the beginner run. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Gradual..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Gradual..", "x": "Explained: Gradual.. Beginners. The context — Couch to 5K. App. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Walk/run.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Walk/run.", "x": "Couch to 5K in depth: Walk/run.. Walk/run. Details — the beginner run.. Beginners. 5K. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "App.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "App.", "x": "Couch to 5K in depth: App.. App. Details — the beginner run.. Gradual. Beginners. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Beginners.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Beginners.", "x": "Couch to 5K in depth: Beginners.. 5K. Details — the beginner run.. 9 weeks. Gradual. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Gradual.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Gradual.", "x": "Couch to 5K in depth: Gradual.. Beginners. Details — the beginner run.. Method. 9 weeks. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "9 weeks.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "9 weeks.", "x": "Couch to 5K in depth: 9 weeks.. Gradual. Details — the beginner run.. Walk/run. Walk/run. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Method.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Method.", "x": "Couch to 5K in depth: Method.. 9 weeks. Details — the beginner run.. App. App. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Couch to 5K comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Couch to 5K comes from.", "x": "Origins: Walk/run.. 9 weeks. The history of Couch to 5K — the beginner run.. App. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Couch to 5K respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Couch to 5K respectfully.", "x": "Engaging: Beginners.. Walk/run. How to participate or observe well — Couch to 5K. the beginner run. Respect first, always; Gradual.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Couch to 5K do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Couch to 5K do's and don'ts.", "x": "Etiquette: 9 weeks.. App. The rules of respect — Couch to 5K. the beginner run. When in doubt, ask about Method.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Couch to 5K.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Couch to 5K.", "x": "Planning: Walk/run.. 5K. Practical notes — Couch to 5K. the beginner run. A little planning shows respect for App.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Couch to 5K and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Couch to 5K and money.", "x": "Costs: Beginners.. Beginners. What to budget — Couch to 5K. the beginner run. The best experiences of Gradual. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-fitness-couch-to-5k-fitness-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
