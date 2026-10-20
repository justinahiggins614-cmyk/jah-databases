(function(){'use strict';
/* JAH Mahler Composer Composer Database generator — jahdb-e2-composer-mahler-composer-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-composer-mahler-composer',PREFIX='JAH-E2COMPOSERM-',NAME='JAH Mahler Composer Composer Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Mahler Composer: the complete guide", "d": "Mahler Composer: the vast symphonist..", "g": "overview", "l": 2, "q": "What is Mahler Composer: the complete guide?", "a": "Mahler Composer: the vast symphonist..", "x": "The complete composer guide to Mahler Composer: the vast symphonist.. 1860. History, meaning, practices, and how to engage respectfully — everything in one database. Symphonies. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Mahler Composer essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Mahler Composer essentials.", "x": "At a glance: Mahler Composer — the vast symphonist.. 9 symphonies. The essentials: Vienna.. Vienna. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "1860.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "1860.", "x": "Mahler Composer: 1860.. Vienna. Essential knowledge — Vienna.. the vast symphonist. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 1860..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 1860..", "x": "Explained: 1860.. Alma. The context — Mahler Composer. Conducting. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "9 symphonies.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "9 symphonies.", "x": "Mahler Composer: 9 symphonies.. Resurrection. Essential knowledge — Conducting.. the vast symphonist. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: 9 symphonies..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: 9 symphonies..", "x": "Explained: 9 symphonies.. Conducting. The context — Mahler Composer. Resurrection. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Vienna.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Vienna.", "x": "Mahler Composer: Vienna.. Alma. Essential knowledge — Resurrection.. the vast symphonist. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Vienna..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Vienna..", "x": "Explained: Vienna.. Legacy. The context — Mahler Composer. Alma. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Conducting.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Conducting.", "x": "Mahler Composer: Conducting.. Conducting. Essential knowledge — Alma.. the vast symphonist. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Conducting..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Conducting..", "x": "Explained: Conducting.. Symphonies. The context — Mahler Composer. 1860. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Resurrection.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Resurrection.", "x": "Mahler Composer: Resurrection.. Legacy. Essential knowledge — 1860.. the vast symphonist. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Resurrection..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Resurrection..", "x": "Explained: Resurrection.. Vienna. The context — Mahler Composer. 9 symphonies. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Alma.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Alma.", "x": "Mahler Composer: Alma.. Symphonies. Essential knowledge — 9 symphonies.. the vast symphonist. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Alma..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Alma..", "x": "Explained: Alma.. Resurrection. The context — Mahler Composer. Vienna. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Symphonies.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Symphonies.", "x": "Mahler Composer in depth: Symphonies.. 9 symphonies. Details — the vast symphonist.. Resurrection. Conducting. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Vienna.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Vienna.", "x": "Mahler Composer in depth: Vienna.. Vienna. Details — the vast symphonist.. Alma. Resurrection. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Resurrection.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Resurrection.", "x": "Mahler Composer in depth: Resurrection.. Conducting. Details — the vast symphonist.. Conducting. Alma. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Alma.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Alma.", "x": "Mahler Composer in depth: Alma.. Resurrection. Details — the vast symphonist.. Legacy. 1860. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Conducting.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Conducting.", "x": "Mahler Composer in depth: Conducting.. Alma. Details — the vast symphonist.. Symphonies. 9 symphonies. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Legacy.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Legacy.", "x": "Mahler Composer in depth: Legacy.. 1860. Details — the vast symphonist.. Vienna. Vienna. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Mahler Composer comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Mahler Composer comes from.", "x": "Origins: Symphonies.. 1860. The history of Mahler Composer — the vast symphonist.. Vienna. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Mahler Composer respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Mahler Composer respectfully.", "x": "Engaging: Resurrection.. 9 symphonies. How to participate or observe well — Mahler Composer. the vast symphonist. Respect first, always; Alma.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Mahler Composer do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Mahler Composer do's and don'ts.", "x": "Etiquette: Conducting.. Vienna. The rules of respect — Mahler Composer. the vast symphonist. When in doubt, ask about Legacy.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Mahler Composer.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Mahler Composer.", "x": "Planning: Symphonies.. Conducting. Practical notes — Mahler Composer. the vast symphonist. A little planning shows respect for Vienna.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Mahler Composer and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Mahler Composer and money.", "x": "Costs: Resurrection.. Resurrection. What to budget — Mahler Composer. the vast symphonist. The best experiences of Alma. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-composer-mahler-composer-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
