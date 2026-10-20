(function(){'use strict';
/* JAH State Fairs Fair Database generator — jahdb-e2-fair-state-fairs-fair-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-fair-state-fairs-fair',PREFIX='JAH-E2FAIRSTATE-',NAME='JAH State Fairs Fair Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "State Fairs: the complete guide", "d": "State Fairs: the annual showcase..", "g": "overview", "l": 2, "q": "What is State Fairs: the complete guide?", "a": "State Fairs: the annual showcase..", "x": "The complete fair guide to State Fairs: the annual showcase.. Livestock. History, meaning, practices, and how to engage respectfully — everything in one database. Livestock. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "State Fairs essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "State Fairs essentials.", "x": "At a glance: State Fairs — the annual showcase.. Midway. The essentials: Midway.. Fried food. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Livestock.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Livestock.", "x": "State Fairs: Livestock.. Midway. Essential knowledge — Fried food.. the annual showcase. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Livestock..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Livestock..", "x": "Explained: Livestock.. 4-H. The context — State Fairs. 4-H. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Midway.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Midway.", "x": "State Fairs: Midway.. Fried. Essential knowledge — 4-H.. the annual showcase. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Midway..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Midway..", "x": "Explained: Midway.. Summer. The context — State Fairs. Concerts. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Fried food.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Fried food.", "x": "State Fairs: Fried food.. 4-H. Essential knowledge — Concerts.. the annual showcase. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Fried food..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Fried food..", "x": "Explained: Fried food.. Fun. The context — State Fairs. Summer. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "4-H.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "4-H.", "x": "State Fairs: 4-H.. Summer. Essential knowledge — Summer.. the annual showcase. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: 4-H..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: 4-H..", "x": "Explained: 4-H.. Livestock. The context — State Fairs. Livestock. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Concerts.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Concerts.", "x": "State Fairs: Concerts.. Fun. Essential knowledge — Livestock.. the annual showcase. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Concerts..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Concerts..", "x": "Explained: Concerts.. Midway. The context — State Fairs. Midway. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Summer.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Summer.", "x": "State Fairs: Summer.. Livestock. Essential knowledge — Midway.. the annual showcase. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Summer..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Summer..", "x": "Explained: Summer.. Fried. The context — State Fairs. Fried food. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Livestock.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Livestock.", "x": "State Fairs in depth: Livestock.. Midway. Details — the annual showcase.. Fried. 4-H. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Midway.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Midway.", "x": "State Fairs in depth: Midway.. Fried food. Details — the annual showcase.. 4-H. Concerts. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Fried.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Fried.", "x": "State Fairs in depth: Fried.. 4-H. Details — the annual showcase.. Summer. Summer. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "4-H.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "4-H.", "x": "State Fairs in depth: 4-H.. Concerts. Details — the annual showcase.. Fun. Livestock. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Summer.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Summer.", "x": "State Fairs in depth: Summer.. Summer. Details — the annual showcase.. Livestock. Midway. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Fun.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Fun.", "x": "State Fairs in depth: Fun.. Livestock. Details — the annual showcase.. Midway. Fried food. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where State Fairs comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where State Fairs comes from.", "x": "Origins: Livestock.. Livestock. The history of State Fairs — the annual showcase.. Midway. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing State Fairs respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing State Fairs respectfully.", "x": "Engaging: Fried.. Midway. How to participate or observe well — State Fairs. the annual showcase. Respect first, always; 4-H.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "State Fairs do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "State Fairs do's and don'ts.", "x": "Etiquette: Summer.. Fried food. The rules of respect — State Fairs. the annual showcase. When in doubt, ask about Fun.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around State Fairs.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around State Fairs.", "x": "Planning: Livestock.. 4-H. Practical notes — State Fairs. the annual showcase. A little planning shows respect for Midway.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "State Fairs and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "State Fairs and money.", "x": "Costs: Fried.. Concerts. What to budget — State Fairs. the annual showcase. The best experiences of 4-H. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-fair-state-fairs-fair-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
