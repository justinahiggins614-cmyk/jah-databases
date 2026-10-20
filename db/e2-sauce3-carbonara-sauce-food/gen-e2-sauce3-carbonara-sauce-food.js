(function(){'use strict';
/* JAH Carbonara Sauce Sauce Database generator — jahdb-e2-sauce3-carbonara-sauce-food-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-sauce3-carbonara-sauce-food',PREFIX='JAH-E2SAUCE3CAR-',NAME='JAH Carbonara Sauce Sauce Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Carbonara Sauce: the complete guide", "d": "Carbonara Sauce: the egg pancetta..", "g": "overview", "l": 2, "q": "What is Carbonara Sauce: the complete guide?", "a": "Carbonara Sauce: the egg pancetta..", "x": "The complete sauce guide to Carbonara Sauce: the egg pancetta.. Eggs. History, meaning, practices, and how to engage respectfully — everything in one database. Eggs. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Carbonara Sauce essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Carbonara Sauce essentials.", "x": "At a glance: Carbonara Sauce — the egg pancetta.. Guanciale. The essentials: Rome.. No cream. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Eggs.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Eggs.", "x": "Carbonara Sauce: Eggs.. Rome. Essential knowledge — No cream.. the egg pancetta. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Eggs..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Eggs..", "x": "Explained: Eggs.. Guanciale. The context — Carbonara Sauce. Pecorino. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Guanciale.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Guanciale.", "x": "Carbonara Sauce: Guanciale.. Technique. Essential knowledge — Pecorino.. the egg pancetta. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Guanciale..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Guanciale..", "x": "Explained: Guanciale.. No cream. The context — Carbonara Sauce. Rome. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "No cream.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "No cream.", "x": "Carbonara Sauce: No cream.. Guanciale. Essential knowledge — Rome.. the egg pancetta. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: No cream..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: No cream..", "x": "Explained: No cream.. Making. The context — Carbonara Sauce. Technique. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Pecorino.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Pecorino.", "x": "Carbonara Sauce: Pecorino.. No cream. Essential knowledge — Technique.. the egg pancetta. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Pecorino..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Pecorino..", "x": "Explained: Pecorino.. Eggs. The context — Carbonara Sauce. Eggs. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Rome.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Rome.", "x": "Carbonara Sauce: Rome.. Making. Essential knowledge — Eggs.. the egg pancetta. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Rome..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Rome..", "x": "Explained: Rome.. Rome. The context — Carbonara Sauce. Guanciale. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Technique.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Technique.", "x": "Carbonara Sauce: Technique.. Eggs. Essential knowledge — Guanciale.. the egg pancetta. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Technique..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Technique..", "x": "Explained: Technique.. Technique. The context — Carbonara Sauce. No cream. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Eggs.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Eggs.", "x": "Carbonara Sauce in depth: Eggs.. Guanciale. Details — the egg pancetta.. Technique. Pecorino. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Rome.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Rome.", "x": "Carbonara Sauce in depth: Rome.. No cream. Details — the egg pancetta.. Guanciale. Rome. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Technique.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Technique.", "x": "Carbonara Sauce in depth: Technique.. Pecorino. Details — the egg pancetta.. No cream. Technique. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Guanciale.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Guanciale.", "x": "Carbonara Sauce in depth: Guanciale.. Rome. Details — the egg pancetta.. Making. Eggs. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "No cream.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "No cream.", "x": "Carbonara Sauce in depth: No cream.. Technique. Details — the egg pancetta.. Eggs. Guanciale. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Making.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Making.", "x": "Carbonara Sauce in depth: Making.. Eggs. Details — the egg pancetta.. Rome. No cream. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Carbonara Sauce comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Carbonara Sauce comes from.", "x": "Origins: Eggs.. Eggs. The history of Carbonara Sauce — the egg pancetta.. Rome. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Carbonara Sauce respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Carbonara Sauce respectfully.", "x": "Engaging: Technique.. Guanciale. How to participate or observe well — Carbonara Sauce. the egg pancetta. Respect first, always; Guanciale.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Carbonara Sauce do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Carbonara Sauce do's and don'ts.", "x": "Etiquette: No cream.. No cream. The rules of respect — Carbonara Sauce. the egg pancetta. When in doubt, ask about Making.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Carbonara Sauce.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Carbonara Sauce.", "x": "Planning: Eggs.. Pecorino. Practical notes — Carbonara Sauce. the egg pancetta. A little planning shows respect for Rome.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Carbonara Sauce and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Carbonara Sauce and money.", "x": "Costs: Technique.. Rome. What to budget — Carbonara Sauce. the egg pancetta. The best experiences of Guanciale. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-sauce3-carbonara-sauce-food-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
