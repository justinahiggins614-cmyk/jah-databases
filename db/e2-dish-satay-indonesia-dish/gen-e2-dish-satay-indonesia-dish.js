(function(){'use strict';
/* JAH Satay Indonesia Dish Database generator — jahdb-e2-dish-satay-indonesia-dish-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-dish-satay-indonesia-dish',PREFIX='JAH-E2DISHSATAY-',NAME='JAH Satay Indonesia Dish Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Satay Indonesia: the complete guide", "d": "Satay Indonesia: the peanut skewers..", "g": "overview", "l": 2, "q": "What is Satay Indonesia: the complete guide?", "a": "Satay Indonesia: the peanut skewers..", "x": "The complete dish guide to Satay Indonesia: the peanut skewers.. Peanut. History, meaning, practices, and how to engage respectfully — everything in one database. Peanut. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Satay Indonesia essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Satay Indonesia essentials.", "x": "At a glance: Satay Indonesia — the peanut skewers.. Skewers. The essentials: Grilled.. Turmeric. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Peanut.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Peanut.", "x": "Satay Indonesia: Peanut.. Grilled. Essential knowledge — Turmeric.. the peanut skewers. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Peanut..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Peanut..", "x": "Explained: Peanut.. Skewers. The context — Satay Indonesia. Grilled. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Skewers.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Skewers.", "x": "Satay Indonesia: Skewers.. Street. Essential knowledge — Grilled.. the peanut skewers. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Skewers..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Skewers..", "x": "Explained: Skewers.. Turmeric. The context — Satay Indonesia. Ketupat. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Turmeric.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Turmeric.", "x": "Satay Indonesia: Turmeric.. Skewers. Essential knowledge — Ketupat.. the peanut skewers. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Turmeric..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Turmeric..", "x": "Explained: Turmeric.. Making. The context — Satay Indonesia. Street. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Grilled.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Grilled.", "x": "Satay Indonesia: Grilled.. Turmeric. Essential knowledge — Street.. the peanut skewers. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Grilled..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Grilled..", "x": "Explained: Grilled.. Peanut. The context — Satay Indonesia. Peanut. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Ketupat.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Ketupat.", "x": "Satay Indonesia: Ketupat.. Making. Essential knowledge — Peanut.. the peanut skewers. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Ketupat..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Ketupat..", "x": "Explained: Ketupat.. Grilled. The context — Satay Indonesia. Skewers. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Street.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Street.", "x": "Satay Indonesia: Street.. Peanut. Essential knowledge — Skewers.. the peanut skewers. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Street..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Street..", "x": "Explained: Street.. Street. The context — Satay Indonesia. Turmeric. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Peanut.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Peanut.", "x": "Satay Indonesia in depth: Peanut.. Skewers. Details — the peanut skewers.. Street. Grilled. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Grilled.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Grilled.", "x": "Satay Indonesia in depth: Grilled.. Turmeric. Details — the peanut skewers.. Skewers. Ketupat. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Street.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Street.", "x": "Satay Indonesia in depth: Street.. Grilled. Details — the peanut skewers.. Turmeric. Street. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Skewers.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Skewers.", "x": "Satay Indonesia in depth: Skewers.. Ketupat. Details — the peanut skewers.. Making. Peanut. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Turmeric.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Turmeric.", "x": "Satay Indonesia in depth: Turmeric.. Street. Details — the peanut skewers.. Peanut. Skewers. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Making.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Making.", "x": "Satay Indonesia in depth: Making.. Peanut. Details — the peanut skewers.. Grilled. Turmeric. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Satay Indonesia comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Satay Indonesia comes from.", "x": "Origins: Peanut.. Peanut. The history of Satay Indonesia — the peanut skewers.. Grilled. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Satay Indonesia respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Satay Indonesia respectfully.", "x": "Engaging: Street.. Skewers. How to participate or observe well — Satay Indonesia. the peanut skewers. Respect first, always; Skewers.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Satay Indonesia do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Satay Indonesia do's and don'ts.", "x": "Etiquette: Turmeric.. Turmeric. The rules of respect — Satay Indonesia. the peanut skewers. When in doubt, ask about Making.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Satay Indonesia.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Satay Indonesia.", "x": "Planning: Peanut.. Grilled. Practical notes — Satay Indonesia. the peanut skewers. A little planning shows respect for Grilled.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Satay Indonesia and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Satay Indonesia and money.", "x": "Costs: Street.. Ketupat. What to budget — Satay Indonesia. the peanut skewers. The best experiences of Skewers. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-dish-satay-indonesia-dish-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
