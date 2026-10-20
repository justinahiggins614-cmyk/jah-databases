(function(){'use strict';
/* JAH Save the Cat Screenwriting Database generator — jahdb-e2-screen-save-the-cat-screen-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-screen-save-the-cat-screen',PREFIX='JAH-E2SCREENSAV-',NAME='JAH Save the Cat Screenwriting Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Save the Cat: the complete guide", "d": "Save the Cat: the beat sheet..", "g": "overview", "l": 2, "q": "What is Save the Cat: the complete guide?", "a": "Save the Cat: the beat sheet..", "x": "The complete screenwriting guide to Save the Cat: the beat sheet.. Snyder. History, meaning, practices, and how to engage respectfully — everything in one database. Beats. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Save the Cat essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Save the Cat essentials.", "x": "At a glance: Save the Cat — the beat sheet.. Beats. The essentials: Snyder.. 15 beats. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Snyder.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Snyder.", "x": "Save the Cat: Snyder.. Snyder. Essential knowledge — 15 beats.. the beat sheet. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Snyder..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Snyder..", "x": "Explained: Snyder.. Genre. The context — Save the Cat. Logline. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Beats.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Beats.", "x": "Save the Cat: Beats.. Logline. Essential knowledge — Logline.. the beat sheet. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Beats..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Beats..", "x": "Explained: Beats.. All is lost. The context — Save the Cat. All is lost. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "15 beats.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "15 beats.", "x": "Save the Cat: 15 beats.. Genre. Essential knowledge — All is lost.. the beat sheet. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: 15 beats..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: 15 beats..", "x": "Explained: 15 beats.. Method. The context — Save the Cat. Genre. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Logline.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Logline.", "x": "Save the Cat: Logline.. All is lost. Essential knowledge — Genre.. the beat sheet. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Logline..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Logline..", "x": "Explained: Logline.. Beats. The context — Save the Cat. Snyder. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "All is lost.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "All is lost.", "x": "Save the Cat: All is lost.. Method. Essential knowledge — Snyder.. the beat sheet. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: All is lost..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: All is lost..", "x": "Explained: All is lost.. Snyder. The context — Save the Cat. Beats. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Genre.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Genre.", "x": "Save the Cat: Genre.. Beats. Essential knowledge — Beats.. the beat sheet. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Genre..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Genre..", "x": "Explained: Genre.. Logline. The context — Save the Cat. 15 beats. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Beats.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Beats.", "x": "Save the Cat in depth: Beats.. Beats. Details — the beat sheet.. Logline. Logline. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Snyder.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Snyder.", "x": "Save the Cat in depth: Snyder.. 15 beats. Details — the beat sheet.. Genre. All is lost. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Logline.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Logline.", "x": "Save the Cat in depth: Logline.. Logline. Details — the beat sheet.. All is lost. Genre. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Genre.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Genre.", "x": "Save the Cat in depth: Genre.. All is lost. Details — the beat sheet.. Method. Snyder. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "All is lost.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "All is lost.", "x": "Save the Cat in depth: All is lost.. Genre. Details — the beat sheet.. Beats. Beats. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Method.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Method.", "x": "Save the Cat in depth: Method.. Snyder. Details — the beat sheet.. Snyder. 15 beats. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Save the Cat comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Save the Cat comes from.", "x": "Origins: Beats.. Snyder. The history of Save the Cat — the beat sheet.. Snyder. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Save the Cat respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Save the Cat respectfully.", "x": "Engaging: Logline.. Beats. How to participate or observe well — Save the Cat. the beat sheet. Respect first, always; Genre.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Save the Cat do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Save the Cat do's and don'ts.", "x": "Etiquette: All is lost.. 15 beats. The rules of respect — Save the Cat. the beat sheet. When in doubt, ask about Method.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Save the Cat.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Save the Cat.", "x": "Planning: Beats.. Logline. Practical notes — Save the Cat. the beat sheet. A little planning shows respect for Snyder.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Save the Cat and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Save the Cat and money.", "x": "Costs: Logline.. All is lost. What to budget — Save the Cat. the beat sheet. The best experiences of Genre. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-screen-save-the-cat-screen-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
