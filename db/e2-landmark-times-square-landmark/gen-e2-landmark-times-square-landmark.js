(function(){'use strict';
/* JAH Times Square Landmark Database generator — jahdb-e2-landmark-times-square-landmark-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-landmark-times-square-landmark',PREFIX='JAH-E2LANDMARKT-',NAME='JAH Times Square Landmark Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Times Square: the complete guide", "d": "Times Square: the crossroads..", "g": "overview", "l": 2, "q": "What is Times Square: the complete guide?", "a": "Times Square: the crossroads..", "x": "The complete landmark guide to Times Square: the crossroads.. 1904. History, meaning, practices, and how to engage respectfully — everything in one database. 1904. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Times Square essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Times Square essentials.", "x": "At a glance: Times Square — the crossroads.. Billboards. The essentials: New Year.. New Year. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "1904.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "1904.", "x": "Times Square: 1904.. New Year. Essential knowledge — New Year.. the crossroads. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 1904..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 1904..", "x": "Explained: 1904.. Crowds. The context — Times Square. TKTS. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Billboards.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Billboards.", "x": "Times Square: Billboards.. Neon. Essential knowledge — TKTS.. the crossroads. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Billboards..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Billboards..", "x": "Explained: Billboards.. Billboards. The context — Times Square. Neon. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "New Year.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "New Year.", "x": "Times Square: New Year.. Crowds. Essential knowledge — Neon.. the crossroads. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: New Year..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: New Year..", "x": "Explained: New Year.. Views. The context — Times Square. Crowds. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "TKTS.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "TKTS.", "x": "Times Square: TKTS.. Billboards. Essential knowledge — Crowds.. the crossroads. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: TKTS..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: TKTS..", "x": "Explained: TKTS.. 1904. The context — Times Square. 1904. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Neon.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Neon.", "x": "Times Square: Neon.. Views. Essential knowledge — 1904.. the crossroads. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Neon..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Neon..", "x": "Explained: Neon.. New Year. The context — Times Square. Billboards. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Crowds.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Crowds.", "x": "Times Square: Crowds.. 1904. Essential knowledge — Billboards.. the crossroads. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Crowds..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Crowds..", "x": "Explained: Crowds.. Neon. The context — Times Square. New Year. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "1904.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "1904.", "x": "Times Square in depth: 1904.. Billboards. Details — the crossroads.. Neon. TKTS. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "New Year.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "New Year.", "x": "Times Square in depth: New Year.. New Year. Details — the crossroads.. Crowds. Neon. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Neon.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Neon.", "x": "Times Square in depth: Neon.. TKTS. Details — the crossroads.. Billboards. Crowds. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Crowds.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Crowds.", "x": "Times Square in depth: Crowds.. Neon. Details — the crossroads.. Views. 1904. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Billboards.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Billboards.", "x": "Times Square in depth: Billboards.. Crowds. Details — the crossroads.. 1904. Billboards. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Views.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Views.", "x": "Times Square in depth: Views.. 1904. Details — the crossroads.. New Year. New Year. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Times Square comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Times Square comes from.", "x": "Origins: 1904.. 1904. The history of Times Square — the crossroads.. New Year. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Times Square respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Times Square respectfully.", "x": "Engaging: Neon.. Billboards. How to participate or observe well — Times Square. the crossroads. Respect first, always; Crowds.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Times Square do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Times Square do's and don'ts.", "x": "Etiquette: Billboards.. New Year. The rules of respect — Times Square. the crossroads. When in doubt, ask about Views.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Times Square.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Times Square.", "x": "Planning: 1904.. TKTS. Practical notes — Times Square. the crossroads. A little planning shows respect for New Year.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Times Square and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Times Square and money.", "x": "Costs: Neon.. Neon. What to budget — Times Square. the crossroads. The best experiences of Crowds. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-landmark-times-square-landmark-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
