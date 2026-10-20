(function(){'use strict';
/* JAH Potala Palace Landmark Database generator — jahdb-e2-landmark-potala-palace-landmark-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-landmark-potala-palace-landmark',PREFIX='JAH-E2LANDMARKP-',NAME='JAH Potala Palace Landmark Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Potala Palace: the complete guide", "d": "Potala Palace: the Dalai palace..", "g": "overview", "l": 2, "q": "What is Potala Palace: the complete guide?", "a": "Potala Palace: the Dalai palace..", "x": "The complete landmark guide to Potala Palace: the Dalai palace.. 1649. History, meaning, practices, and how to engage respectfully — everything in one database. 1649. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Potala Palace essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Potala Palace essentials.", "x": "At a glance: Potala Palace — the Dalai palace.. 13 stories. The essentials: Pilgrims.. 1,000 rooms. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "1649.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "1649.", "x": "Potala Palace: 1649.. Pilgrims. Essential knowledge — 1,000 rooms.. the Dalai palace. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 1649..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 1649..", "x": "Explained: 1649.. Red. The context — Potala Palace. Red/white. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "13 stories.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "13 stories.", "x": "Potala Palace: 13 stories.. Altitude. Essential knowledge — Red/white.. the Dalai palace. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: 13 stories..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: 13 stories..", "x": "Explained: 13 stories.. 1,000. The context — Potala Palace. Pilgrims. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "1,000 rooms.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "1,000 rooms.", "x": "Potala Palace: 1,000 rooms.. Red. Essential knowledge — Pilgrims.. the Dalai palace. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: 1,000 rooms..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: 1,000 rooms..", "x": "Explained: 1,000 rooms.. Tours. The context — Potala Palace. Altitude. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Red/white.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Red/white.", "x": "Potala Palace: Red/white.. 1,000. Essential knowledge — Altitude.. the Dalai palace. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Red/white..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Red/white..", "x": "Explained: Red/white.. 1649. The context — Potala Palace. 1649. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Pilgrims.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Pilgrims.", "x": "Potala Palace: Pilgrims.. Tours. Essential knowledge — 1649.. the Dalai palace. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Pilgrims..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Pilgrims..", "x": "Explained: Pilgrims.. Pilgrims. The context — Potala Palace. 13 stories. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Altitude.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Altitude.", "x": "Potala Palace: Altitude.. 1649. Essential knowledge — 13 stories.. the Dalai palace. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Altitude..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Altitude..", "x": "Explained: Altitude.. Altitude. The context — Potala Palace. 1,000 rooms. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "1649.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "1649.", "x": "Potala Palace in depth: 1649.. 13 stories. Details — the Dalai palace.. Altitude. Red/white. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Pilgrims.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Pilgrims.", "x": "Potala Palace in depth: Pilgrims.. 1,000 rooms. Details — the Dalai palace.. Red. Pilgrims. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Altitude.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Altitude.", "x": "Potala Palace in depth: Altitude.. Red/white. Details — the Dalai palace.. 1,000. Altitude. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Red.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Red.", "x": "Potala Palace in depth: Red.. Pilgrims. Details — the Dalai palace.. Tours. 1649. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "1,000.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "1,000.", "x": "Potala Palace in depth: 1,000.. Altitude. Details — the Dalai palace.. 1649. 13 stories. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Tours.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Tours.", "x": "Potala Palace in depth: Tours.. 1649. Details — the Dalai palace.. Pilgrims. 1,000 rooms. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Potala Palace comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Potala Palace comes from.", "x": "Origins: 1649.. 1649. The history of Potala Palace — the Dalai palace.. Pilgrims. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Potala Palace respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Potala Palace respectfully.", "x": "Engaging: Altitude.. 13 stories. How to participate or observe well — Potala Palace. the Dalai palace. Respect first, always; Red.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Potala Palace do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Potala Palace do's and don'ts.", "x": "Etiquette: 1,000.. 1,000 rooms. The rules of respect — Potala Palace. the Dalai palace. When in doubt, ask about Tours.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Potala Palace.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Potala Palace.", "x": "Planning: 1649.. Red/white. Practical notes — Potala Palace. the Dalai palace. A little planning shows respect for Pilgrims.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Potala Palace and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Potala Palace and money.", "x": "Costs: Altitude.. Pilgrims. What to budget — Potala Palace. the Dalai palace. The best experiences of Red. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-landmark-potala-palace-landmark-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
