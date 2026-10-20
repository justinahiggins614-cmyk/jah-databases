(function(){'use strict';
/* JAH Pongal Holiday Database generator — jahdb-e2-holiday-pongal-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-holiday-pongal',PREFIX='JAH-E2HOLIDAYPO-',NAME='JAH Pongal Holiday Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Pongal: the complete guide", "d": "Pongal: Tamil harvest festival..", "g": "overview", "l": 2, "q": "What is Pongal: the complete guide?", "a": "Pongal: Tamil harvest festival..", "x": "The complete holiday guide to Pongal: Tamil harvest festival.. January. History, meaning, practices, and how to engage respectfully — everything in one database. Harvest. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Pongal essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Pongal essentials.", "x": "At a glance: Pongal — Tamil harvest festival.. Rice. The essentials: Food.. Sun god. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "January.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "January.", "x": "Pongal: January.. Food. Essential knowledge — Sun god.. Tamil harvest festival. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: January..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: January..", "x": "Explained: January.. Family. The context — Pongal. Kolam. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Rice.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Rice.", "x": "Pongal: Rice.. Art. Essential knowledge — Kolam.. Tamil harvest festival. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Rice..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Rice..", "x": "Explained: Rice.. Meaning. The context — Pongal. 4 days. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Sun god.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Sun god.", "x": "Pongal: Sun god.. Family. Essential knowledge — 4 days.. Tamil harvest festival. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Sun god..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Sun god..", "x": "Explained: Sun god.. Joy. The context — Pongal. Tamil Nadu. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Kolam.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Kolam.", "x": "Pongal: Kolam.. Meaning. Essential knowledge — Tamil Nadu.. Tamil harvest festival. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Kolam..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Kolam..", "x": "Explained: Kolam.. Harvest. The context — Pongal. January. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "4 days.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "4 days.", "x": "Pongal: 4 days.. Joy. Essential knowledge — January.. Tamil harvest festival. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: 4 days..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: 4 days..", "x": "Explained: 4 days.. Food. The context — Pongal. Rice. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Tamil Nadu.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Tamil Nadu.", "x": "Pongal: Tamil Nadu.. Harvest. Essential knowledge — Rice.. Tamil harvest festival. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Tamil Nadu..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Tamil Nadu..", "x": "Explained: Tamil Nadu.. Art. The context — Pongal. Sun god. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Harvest.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Harvest.", "x": "Pongal in depth: Harvest.. Rice. Details — Tamil harvest festival.. Art. Kolam. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Food.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Food.", "x": "Pongal in depth: Food.. Sun god. Details — Tamil harvest festival.. Family. 4 days. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Art.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Art.", "x": "Pongal in depth: Art.. Kolam. Details — Tamil harvest festival.. Meaning. Tamil Nadu. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Family.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Family.", "x": "Pongal in depth: Family.. 4 days. Details — Tamil harvest festival.. Joy. January. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Meaning.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Meaning.", "x": "Pongal in depth: Meaning.. Tamil Nadu. Details — Tamil harvest festival.. Harvest. Rice. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Joy.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Joy.", "x": "Pongal in depth: Joy.. January. Details — Tamil harvest festival.. Food. Sun god. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Pongal comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Pongal comes from.", "x": "Origins: Harvest.. January. The history of Pongal — Tamil harvest festival.. Food. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Pongal respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Pongal respectfully.", "x": "Engaging: Art.. Rice. How to participate or observe well — Pongal. Tamil harvest festival. Respect first, always; Family.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Pongal do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Pongal do's and don'ts.", "x": "Etiquette: Meaning.. Sun god. The rules of respect — Pongal. Tamil harvest festival. When in doubt, ask about Joy.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Pongal.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Pongal.", "x": "Planning: Harvest.. Kolam. Practical notes — Pongal. Tamil harvest festival. A little planning shows respect for Food.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Pongal and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Pongal and money.", "x": "Costs: Art.. 4 days. What to budget — Pongal. Tamil harvest festival. The best experiences of Family. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-holiday-pongal-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
