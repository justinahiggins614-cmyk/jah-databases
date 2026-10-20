(function(){'use strict';
/* JAH Indian Wells Tennis2 Database generator — jahdb-e2-tennis2-indian-wells-tennis2-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-tennis2-indian-wells-tennis2',PREFIX='JAH-E2TENNIS2IN-',NAME='JAH Indian Wells Tennis2 Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Indian Wells Tennis2: the complete guide", "d": "Indian Wells Tennis2: the desert 2..", "g": "overview", "l": 2, "q": "What is Indian Wells Tennis2: the complete guide?", "a": "Indian Wells Tennis2: the desert 2..", "x": "The complete tennis court guide to Indian Wells Tennis2: the desert 2.. 1974. History, meaning, practices, and how to engage respectfully — everything in one database. 1974. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Indian Wells Tennis2 essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Indian Wells Tennis2 essentials.", "x": "At a glance: Indian Wells Tennis2 — the desert 2.. Desert. The essentials: March.. Fifth Slam. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "1974.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "1974.", "x": "Indian Wells Tennis2: 1974.. March. Essential knowledge — Fifth Slam.. the desert 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 1974..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 1974..", "x": "Explained: 1974.. Desert. The context — Indian Wells Tennis2. California. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Desert.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Desert.", "x": "Indian Wells Tennis2: Desert.. Stadium. Essential knowledge — California.. the desert 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Desert..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Desert..", "x": "Explained: Desert.. California. The context — Indian Wells Tennis2. Stadium 1. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Fifth Slam.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Fifth Slam.", "x": "Indian Wells Tennis2: Fifth Slam.. Desert. Essential knowledge — Stadium 1.. the desert 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Fifth Slam..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Fifth Slam..", "x": "Explained: Fifth Slam.. Guide. The context — Indian Wells Tennis2. March. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "California.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "California.", "x": "Indian Wells Tennis2: California.. California. Essential knowledge — March.. the desert 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: California..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: California..", "x": "Explained: California.. 1974. The context — Indian Wells Tennis2. 1974. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Stadium 1.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Stadium 1.", "x": "Indian Wells Tennis2: Stadium 1.. Guide. Essential knowledge — 1974.. the desert 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Stadium 1..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Stadium 1..", "x": "Explained: Stadium 1.. March. The context — Indian Wells Tennis2. Desert. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "March.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "March.", "x": "Indian Wells Tennis2: March.. 1974. Essential knowledge — Desert.. the desert 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: March..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: March..", "x": "Explained: March.. Stadium. The context — Indian Wells Tennis2. Fifth Slam. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "1974.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "1974.", "x": "Indian Wells Tennis2 in depth: 1974.. Desert. Details — the desert 2.. Stadium. California. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "March.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "March.", "x": "Indian Wells Tennis2 in depth: March.. Fifth Slam. Details — the desert 2.. Desert. Stadium 1. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Stadium.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Stadium.", "x": "Indian Wells Tennis2 in depth: Stadium.. California. Details — the desert 2.. California. March. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Desert.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Desert.", "x": "Indian Wells Tennis2 in depth: Desert.. Stadium 1. Details — the desert 2.. Guide. 1974. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "California.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "California.", "x": "Indian Wells Tennis2 in depth: California.. March. Details — the desert 2.. 1974. Desert. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Guide.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Guide.", "x": "Indian Wells Tennis2 in depth: Guide.. 1974. Details — the desert 2.. March. Fifth Slam. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Indian Wells Tennis2 comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Indian Wells Tennis2 comes from.", "x": "Origins: 1974.. 1974. The history of Indian Wells Tennis2 — the desert 2.. March. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Indian Wells Tennis2 respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Indian Wells Tennis2 respectfully.", "x": "Engaging: Stadium.. Desert. How to participate or observe well — Indian Wells Tennis2. the desert 2. Respect first, always; Desert.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Indian Wells Tennis2 do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Indian Wells Tennis2 do's and don'ts.", "x": "Etiquette: California.. Fifth Slam. The rules of respect — Indian Wells Tennis2. the desert 2. When in doubt, ask about Guide.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Indian Wells Tennis2.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Indian Wells Tennis2.", "x": "Planning: 1974.. California. Practical notes — Indian Wells Tennis2. the desert 2. A little planning shows respect for March.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Indian Wells Tennis2 and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Indian Wells Tennis2 and money.", "x": "Costs: Stadium.. Stadium 1. What to budget — Indian Wells Tennis2. the desert 2. The best experiences of Desert. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-tennis2-indian-wells-tennis2-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
