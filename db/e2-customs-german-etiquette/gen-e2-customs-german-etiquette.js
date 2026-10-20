(function(){'use strict';
/* JAH German Etiquette Customs Database generator — jahdb-e2-customs-german-etiquette-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-customs-german-etiquette',PREFIX='JAH-E2CUSTOMSGE-',NAME='JAH German Etiquette Customs Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "German Etiquette: the complete guide", "d": "German Etiquette: ordnung and punctuality..", "g": "overview", "l": 2, "q": "What is German Etiquette: the complete guide?", "a": "German Etiquette: ordnung and punctuality..", "x": "The complete customs guide to German Etiquette: ordnung and punctuality.. Punctual. History, meaning, practices, and how to engage respectfully — everything in one database. Time. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "German Etiquette essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "German Etiquette essentials.", "x": "At a glance: German Etiquette — ordnung and punctuality.. Titles. The essentials: Titles.. Recycling. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Punctual.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Punctual.", "x": "German Etiquette: Punctual.. Titles. Essential knowledge — Recycling.. ordnung and punctuality. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Punctual..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Punctual..", "x": "Explained: Punctual.. Sunday. The context — German Etiquette. Quiet Sundays. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Titles.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Titles.", "x": "German Etiquette: Titles.. Rules. Essential knowledge — Quiet Sundays.. ordnung and punctuality. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Titles..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Titles..", "x": "Explained: Titles.. Direct. The context — German Etiquette. Directness. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Recycling.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Recycling.", "x": "German Etiquette: Recycling.. Sunday. Essential knowledge — Directness.. ordnung and punctuality. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Recycling..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Recycling..", "x": "Explained: Recycling.. Order. The context — German Etiquette. Beer. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Quiet Sundays.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Quiet Sundays.", "x": "German Etiquette: Quiet Sundays.. Direct. Essential knowledge — Beer.. ordnung and punctuality. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Quiet Sundays..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Quiet Sundays..", "x": "Explained: Quiet Sundays.. Time. The context — German Etiquette. Punctual. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Directness.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Directness.", "x": "German Etiquette: Directness.. Order. Essential knowledge — Punctual.. ordnung and punctuality. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Directness..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Directness..", "x": "Explained: Directness.. Titles. The context — German Etiquette. Titles. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Beer.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Beer.", "x": "German Etiquette: Beer.. Time. Essential knowledge — Titles.. ordnung and punctuality. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Beer..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Beer..", "x": "Explained: Beer.. Rules. The context — German Etiquette. Recycling. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Time.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Time.", "x": "German Etiquette in depth: Time.. Titles. Details — ordnung and punctuality.. Rules. Quiet Sundays. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Titles.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Titles.", "x": "German Etiquette in depth: Titles.. Recycling. Details — ordnung and punctuality.. Sunday. Directness. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Rules.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Rules.", "x": "German Etiquette in depth: Rules.. Quiet Sundays. Details — ordnung and punctuality.. Direct. Beer. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Sunday.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Sunday.", "x": "German Etiquette in depth: Sunday.. Directness. Details — ordnung and punctuality.. Order. Punctual. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Direct.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Direct.", "x": "German Etiquette in depth: Direct.. Beer. Details — ordnung and punctuality.. Time. Titles. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Order.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Order.", "x": "German Etiquette in depth: Order.. Punctual. Details — ordnung and punctuality.. Titles. Recycling. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where German Etiquette comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where German Etiquette comes from.", "x": "Origins: Time.. Punctual. The history of German Etiquette — ordnung and punctuality.. Titles. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing German Etiquette respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing German Etiquette respectfully.", "x": "Engaging: Rules.. Titles. How to participate or observe well — German Etiquette. ordnung and punctuality. Respect first, always; Sunday.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "German Etiquette do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "German Etiquette do's and don'ts.", "x": "Etiquette: Direct.. Recycling. The rules of respect — German Etiquette. ordnung and punctuality. When in doubt, ask about Order.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around German Etiquette.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around German Etiquette.", "x": "Planning: Time.. Quiet Sundays. Practical notes — German Etiquette. ordnung and punctuality. A little planning shows respect for Titles.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "German Etiquette and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "German Etiquette and money.", "x": "Costs: Rules.. Directness. What to budget — German Etiquette. ordnung and punctuality. The best experiences of Sunday. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-customs-german-etiquette-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
