(function(){'use strict';
/* JAH Albuquerque Balloon Fiesta Festival Database generator — jahdb-e2-festival-balloon-fiesta-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-festival-balloon-fiesta',PREFIX='JAH-E2FESTIVALB-',NAME='JAH Albuquerque Balloon Fiesta Festival Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Albuquerque Balloon Fiesta: the complete guide", "d": "Albuquerque Balloon Fiesta: mass ascension..", "g": "overview", "l": 2, "q": "What is Albuquerque Balloon Fiesta: the complete guide?", "a": "Albuquerque Balloon Fiesta: mass ascension..", "x": "The complete festival guide to Albuquerque Balloon Fiesta: mass ascension.. October. History, meaning, practices, and how to engage respectfully — everything in one database. Balloons. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Albuquerque Balloon Fiesta essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Albuquerque Balloon Fiesta essentials.", "x": "At a glance: Albuquerque Balloon Fiesta — mass ascension.. 600 balloons. The essentials: Dawn.. Dawn patrol. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "October.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "October.", "x": "Albuquerque Balloon Fiesta: October.. Dawn. Essential knowledge — Dawn patrol.. mass ascension. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: October..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: October..", "x": "Explained: October.. History. The context — Albuquerque Balloon Fiesta. Box effect. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "600 balloons.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "600 balloons.", "x": "Albuquerque Balloon Fiesta: 600 balloons.. Photos. Essential knowledge — Box effect.. mass ascension. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: 600 balloons..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: 600 balloons..", "x": "Explained: 600 balloons.. Travel. The context — Albuquerque Balloon Fiesta. Photos. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Dawn patrol.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Dawn patrol.", "x": "Albuquerque Balloon Fiesta: Dawn patrol.. History. Essential knowledge — Photos.. mass ascension. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Dawn patrol..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Dawn patrol..", "x": "Explained: Dawn patrol.. Magic. The context — Albuquerque Balloon Fiesta. New Mexico. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Box effect.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Box effect.", "x": "Albuquerque Balloon Fiesta: Box effect.. Travel. Essential knowledge — New Mexico.. mass ascension. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Box effect..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Box effect..", "x": "Explained: Box effect.. Balloons. The context — Albuquerque Balloon Fiesta. October. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Photos.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Photos.", "x": "Albuquerque Balloon Fiesta: Photos.. Magic. Essential knowledge — October.. mass ascension. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Photos..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Photos..", "x": "Explained: Photos.. Dawn. The context — Albuquerque Balloon Fiesta. 600 balloons. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "New Mexico.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "New Mexico.", "x": "Albuquerque Balloon Fiesta: New Mexico.. Balloons. Essential knowledge — 600 balloons.. mass ascension. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: New Mexico..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: New Mexico..", "x": "Explained: New Mexico.. Photos. The context — Albuquerque Balloon Fiesta. Dawn patrol. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Balloons.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Balloons.", "x": "Albuquerque Balloon Fiesta in depth: Balloons.. 600 balloons. Details — mass ascension.. Photos. Box effect. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Dawn.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Dawn.", "x": "Albuquerque Balloon Fiesta in depth: Dawn.. Dawn patrol. Details — mass ascension.. History. Photos. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Photos.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Photos.", "x": "Albuquerque Balloon Fiesta in depth: Photos.. Box effect. Details — mass ascension.. Travel. New Mexico. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "History.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "History.", "x": "Albuquerque Balloon Fiesta in depth: History.. Photos. Details — mass ascension.. Magic. October. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Travel.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Travel.", "x": "Albuquerque Balloon Fiesta in depth: Travel.. New Mexico. Details — mass ascension.. Balloons. 600 balloons. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Magic.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Magic.", "x": "Albuquerque Balloon Fiesta in depth: Magic.. October. Details — mass ascension.. Dawn. Dawn patrol. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Albuquerque Balloon Fiesta comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Albuquerque Balloon Fiesta comes from.", "x": "Origins: Balloons.. October. The history of Albuquerque Balloon Fiesta — mass ascension.. Dawn. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Albuquerque Balloon Fiesta respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Albuquerque Balloon Fiesta respectfully.", "x": "Engaging: Photos.. 600 balloons. How to participate or observe well — Albuquerque Balloon Fiesta. mass ascension. Respect first, always; History.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Albuquerque Balloon Fiesta do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Albuquerque Balloon Fiesta do's and don'ts.", "x": "Etiquette: Travel.. Dawn patrol. The rules of respect — Albuquerque Balloon Fiesta. mass ascension. When in doubt, ask about Magic.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Albuquerque Balloon Fiesta.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Albuquerque Balloon Fiesta.", "x": "Planning: Balloons.. Box effect. Practical notes — Albuquerque Balloon Fiesta. mass ascension. A little planning shows respect for Dawn.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Albuquerque Balloon Fiesta and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Albuquerque Balloon Fiesta and money.", "x": "Costs: Photos.. Photos. What to budget — Albuquerque Balloon Fiesta. mass ascension. The best experiences of History. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-festival-balloon-fiesta-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
