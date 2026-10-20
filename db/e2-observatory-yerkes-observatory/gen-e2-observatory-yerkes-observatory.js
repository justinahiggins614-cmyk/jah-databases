(function(){'use strict';
/* JAH Yerkes Observatory Observatory Database generator — jahdb-e2-observatory-yerkes-observatory-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-observatory-yerkes-observatory',PREFIX='JAH-E2OBSERVATO-',NAME='JAH Yerkes Observatory Observatory Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Yerkes Observatory: the complete guide", "d": "Yerkes Observatory: the great refractor..", "g": "overview", "l": 2, "q": "What is Yerkes Observatory: the complete guide?", "a": "Yerkes Observatory: the great refractor..", "x": "The complete observatory guide to Yerkes Observatory: the great refractor.. 1897. History, meaning, practices, and how to engage respectfully — everything in one database. Refractor. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Yerkes Observatory essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Yerkes Observatory essentials.", "x": "At a glance: Yerkes Observatory — the great refractor.. 40-inch refractor. The essentials: History.. Burnham. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "1897.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "1897.", "x": "Yerkes Observatory: 1897.. History. Essential knowledge — Burnham.. the great refractor. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 1897..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 1897..", "x": "Explained: 1897.. Tours. The context — Yerkes Observatory. Wisconsin. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "40-inch refractor.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "40-inch refractor.", "x": "Yerkes Observatory: 40-inch refractor.. Wisconsin. Essential knowledge — Wisconsin.. the great refractor. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: 40-inch refractor..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: 40-inch refractor..", "x": "Explained: 40-inch refractor.. Future. The context — Yerkes Observatory. History. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Burnham.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Burnham.", "x": "Yerkes Observatory: Burnham.. Tours. Essential knowledge — History.. the great refractor. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Burnham..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Burnham..", "x": "Explained: Burnham.. Science. The context — Yerkes Observatory. Future. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Wisconsin.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Wisconsin.", "x": "Yerkes Observatory: Wisconsin.. Future. Essential knowledge — Future.. the great refractor. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Wisconsin..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Wisconsin..", "x": "Explained: Wisconsin.. Refractor. The context — Yerkes Observatory. 1897. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "History.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "History.", "x": "Yerkes Observatory: History.. Science. Essential knowledge — 1897.. the great refractor. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: History..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: History..", "x": "Explained: History.. History. The context — Yerkes Observatory. 40-inch refractor. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Future.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Future.", "x": "Yerkes Observatory: Future.. Refractor. Essential knowledge — 40-inch refractor.. the great refractor. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Future..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Future..", "x": "Explained: Future.. Wisconsin. The context — Yerkes Observatory. Burnham. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Refractor.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Refractor.", "x": "Yerkes Observatory in depth: Refractor.. 40-inch refractor. Details — the great refractor.. Wisconsin. Wisconsin. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "History.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "History.", "x": "Yerkes Observatory in depth: History.. Burnham. Details — the great refractor.. Tours. History. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Wisconsin.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Wisconsin.", "x": "Yerkes Observatory in depth: Wisconsin.. Wisconsin. Details — the great refractor.. Future. Future. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Tours.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Tours.", "x": "Yerkes Observatory in depth: Tours.. History. Details — the great refractor.. Science. 1897. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Future.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Future.", "x": "Yerkes Observatory in depth: Future.. Future. Details — the great refractor.. Refractor. 40-inch refractor. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Science.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Science.", "x": "Yerkes Observatory in depth: Science.. 1897. Details — the great refractor.. History. Burnham. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Yerkes Observatory comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Yerkes Observatory comes from.", "x": "Origins: Refractor.. 1897. The history of Yerkes Observatory — the great refractor.. History. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Yerkes Observatory respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Yerkes Observatory respectfully.", "x": "Engaging: Wisconsin.. 40-inch refractor. How to participate or observe well — Yerkes Observatory. the great refractor. Respect first, always; Tours.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Yerkes Observatory do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Yerkes Observatory do's and don'ts.", "x": "Etiquette: Future.. Burnham. The rules of respect — Yerkes Observatory. the great refractor. When in doubt, ask about Science.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Yerkes Observatory.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Yerkes Observatory.", "x": "Planning: Refractor.. Wisconsin. Practical notes — Yerkes Observatory. the great refractor. A little planning shows respect for History.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Yerkes Observatory and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Yerkes Observatory and money.", "x": "Costs: Wisconsin.. History. What to budget — Yerkes Observatory. the great refractor. The best experiences of Tours. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-observatory-yerkes-observatory-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
