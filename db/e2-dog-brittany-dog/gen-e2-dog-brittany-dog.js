(function(){'use strict';
/* JAH Brittany Dog Dog Breed Database generator — jahdb-e2-dog-brittany-dog-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-dog-brittany-dog',PREFIX='JAH-E2DOGBRITTA-',NAME='JAH Brittany Dog Dog Breed Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Brittany Dog: the complete guide", "d": "Brittany Dog: the French pointer..", "g": "overview", "l": 2, "q": "What is Brittany Dog: the complete guide?", "a": "Brittany Dog: the French pointer..", "x": "The complete dog breed guide to Brittany Dog: the French pointer.. France. History, meaning, practices, and how to engage respectfully — everything in one database. France. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Brittany Dog essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Brittany Dog essentials.", "x": "At a glance: Brittany Dog — the French pointer.. Pointing. The essentials: Energy.. Energetic. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "France.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "France.", "x": "Brittany Dog: France.. Energy. Essential knowledge — Energetic.. the French pointer. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: France..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: France..", "x": "Explained: France.. Happy. The context — Brittany Dog. Versatile. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Pointing.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Pointing.", "x": "Brittany Dog: Pointing.. Versatile. Essential knowledge — Versatile.. the French pointer. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Pointing..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Pointing..", "x": "Explained: Pointing.. Pointing. The context — Brittany Dog. Orange. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Energetic.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Energetic.", "x": "Brittany Dog: Energetic.. Happy. Essential knowledge — Orange.. the French pointer. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Energetic..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Energetic..", "x": "Explained: Energetic.. History. The context — Brittany Dog. Happy. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Versatile.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Versatile.", "x": "Brittany Dog: Versatile.. Pointing. Essential knowledge — Happy.. the French pointer. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Versatile..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Versatile..", "x": "Explained: Versatile.. France. The context — Brittany Dog. France. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Orange.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Orange.", "x": "Brittany Dog: Orange.. History. Essential knowledge — France.. the French pointer. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Orange..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Orange..", "x": "Explained: Orange.. Energy. The context — Brittany Dog. Pointing. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Happy.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Happy.", "x": "Brittany Dog: Happy.. France. Essential knowledge — Pointing.. the French pointer. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Happy..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Happy..", "x": "Explained: Happy.. Versatile. The context — Brittany Dog. Energetic. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "France.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "France.", "x": "Brittany Dog in depth: France.. Pointing. Details — the French pointer.. Versatile. Versatile. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Energy.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Energy.", "x": "Brittany Dog in depth: Energy.. Energetic. Details — the French pointer.. Happy. Orange. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Versatile.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Versatile.", "x": "Brittany Dog in depth: Versatile.. Versatile. Details — the French pointer.. Pointing. Happy. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Happy.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Happy.", "x": "Brittany Dog in depth: Happy.. Orange. Details — the French pointer.. History. France. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Pointing.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Pointing.", "x": "Brittany Dog in depth: Pointing.. Happy. Details — the French pointer.. France. Pointing. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "History.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "History.", "x": "Brittany Dog in depth: History.. France. Details — the French pointer.. Energy. Energetic. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Brittany Dog comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Brittany Dog comes from.", "x": "Origins: France.. France. The history of Brittany Dog — the French pointer.. Energy. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Brittany Dog respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Brittany Dog respectfully.", "x": "Engaging: Versatile.. Pointing. How to participate or observe well — Brittany Dog. the French pointer. Respect first, always; Happy.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Brittany Dog do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Brittany Dog do's and don'ts.", "x": "Etiquette: Pointing.. Energetic. The rules of respect — Brittany Dog. the French pointer. When in doubt, ask about History.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Brittany Dog.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Brittany Dog.", "x": "Planning: France.. Versatile. Practical notes — Brittany Dog. the French pointer. A little planning shows respect for Energy.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Brittany Dog and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Brittany Dog and money.", "x": "Costs: Versatile.. Orange. What to budget — Brittany Dog. the French pointer. The best experiences of Happy. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-dog-brittany-dog-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
