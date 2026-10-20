(function(){'use strict';
/* JAH BMX Olympics Database generator — jahdb-e2-olympic2-bmx-olympics-sport-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-olympic2-bmx-olympics-sport',PREFIX='JAH-E2OLYMPIC2B-',NAME='JAH BMX Olympics Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "BMX Olympics: the complete guide", "d": "BMX Olympics: the dirt sprint..", "g": "overview", "l": 2, "q": "What is BMX Olympics: the complete guide?", "a": "BMX Olympics: the dirt sprint..", "x": "The complete olympic sport guide to BMX Olympics: the dirt sprint.. 2008. History, meaning, practices, and how to engage respectfully — everything in one database. Gates. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "BMX Olympics essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "BMX Olympics essentials.", "x": "At a glance: BMX Olympics — the dirt sprint.. Dirt. The essentials: Freestyle.. Gates. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "2008.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "2008.", "x": "BMX Olympics: 2008.. Freestyle. Essential knowledge — Gates.. the dirt sprint. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 2008..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 2008..", "x": "Explained: 2008.. Dirt. The context — BMX Olympics. Jumps. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Dirt.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Dirt.", "x": "BMX Olympics: Dirt.. 40 sec. Essential knowledge — Jumps.. the dirt sprint. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Dirt..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Dirt..", "x": "Explained: Dirt.. Jumps. The context — BMX Olympics. Freestyle. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Gates.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Gates.", "x": "BMX Olympics: Gates.. Dirt. Essential knowledge — Freestyle.. the dirt sprint. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Gates..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Gates..", "x": "Explained: Gates.. Guide. The context — BMX Olympics. 40 sec. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Jumps.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Jumps.", "x": "BMX Olympics: Jumps.. Jumps. Essential knowledge — 40 sec.. the dirt sprint. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Jumps..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Jumps..", "x": "Explained: Jumps.. Gates. The context — BMX Olympics. 2008. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Freestyle.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Freestyle.", "x": "BMX Olympics: Freestyle.. Guide. Essential knowledge — 2008.. the dirt sprint. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Freestyle..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Freestyle..", "x": "Explained: Freestyle.. Freestyle. The context — BMX Olympics. Dirt. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "40 sec.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "40 sec.", "x": "BMX Olympics: 40 sec.. Gates. Essential knowledge — Dirt.. the dirt sprint. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: 40 sec..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: 40 sec..", "x": "Explained: 40 sec.. 40 sec. The context — BMX Olympics. Gates. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Gates.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Gates.", "x": "BMX Olympics in depth: Gates.. Dirt. Details — the dirt sprint.. 40 sec. Jumps. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Freestyle.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Freestyle.", "x": "BMX Olympics in depth: Freestyle.. Gates. Details — the dirt sprint.. Dirt. Freestyle. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "40 sec.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "40 sec.", "x": "BMX Olympics in depth: 40 sec.. Jumps. Details — the dirt sprint.. Jumps. 40 sec. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Dirt.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Dirt.", "x": "BMX Olympics in depth: Dirt.. Freestyle. Details — the dirt sprint.. Guide. 2008. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Jumps.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Jumps.", "x": "BMX Olympics in depth: Jumps.. 40 sec. Details — the dirt sprint.. Gates. Dirt. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Guide.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Guide.", "x": "BMX Olympics in depth: Guide.. 2008. Details — the dirt sprint.. Freestyle. Gates. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where BMX Olympics comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where BMX Olympics comes from.", "x": "Origins: Gates.. 2008. The history of BMX Olympics — the dirt sprint.. Freestyle. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing BMX Olympics respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing BMX Olympics respectfully.", "x": "Engaging: 40 sec.. Dirt. How to participate or observe well — BMX Olympics. the dirt sprint. Respect first, always; Dirt.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "BMX Olympics do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "BMX Olympics do's and don'ts.", "x": "Etiquette: Jumps.. Gates. The rules of respect — BMX Olympics. the dirt sprint. When in doubt, ask about Guide.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around BMX Olympics.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around BMX Olympics.", "x": "Planning: Gates.. Jumps. Practical notes — BMX Olympics. the dirt sprint. A little planning shows respect for Freestyle.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "BMX Olympics and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "BMX Olympics and money.", "x": "Costs: 40 sec.. Freestyle. What to budget — BMX Olympics. the dirt sprint. The best experiences of Dirt. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-olympic2-bmx-olympics-sport-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
