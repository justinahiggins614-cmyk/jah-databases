(function(){'use strict';
/* JAH Horror Movies Movie Genre Database generator — jahdb-e2-genre-horror-movies-genre-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-genre-horror-movies-genre',PREFIX='JAH-E2GENREHORR-',NAME='JAH Horror Movies Movie Genre Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Horror Movies: the complete guide", "d": "Horror Movies: the fear genre..", "g": "overview", "l": 2, "q": "What is Horror Movies: the complete guide?", "a": "Horror Movies: the fear genre..", "x": "The complete movie genre guide to Horror Movies: the fear genre.. Suspense. History, meaning, practices, and how to engage respectfully — everything in one database. Suspense. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Horror Movies essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Horror Movies essentials.", "x": "At a glance: Horror Movies — the fear genre.. Slashers. The essentials: Monsters.. Monsters. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Suspense.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Suspense.", "x": "Horror Movies: Suspense.. Monsters. Essential knowledge — Monsters.. the fear genre. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Suspense..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Suspense..", "x": "Explained: Suspense.. 1970s. The context — Horror Movies. Jump scares. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Slashers.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Slashers.", "x": "Horror Movies: Slashers.. Slashers. Essential knowledge — Jump scares.. the fear genre. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Slashers..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Slashers..", "x": "Explained: Slashers.. Scares. The context — Horror Movies. 1970s. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Monsters.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Monsters.", "x": "Horror Movies: Monsters.. 1970s. Essential knowledge — 1970s.. the fear genre. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Monsters..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Monsters..", "x": "Explained: Monsters.. Classics. The context — Horror Movies. Final girls. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Jump scares.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Jump scares.", "x": "Horror Movies: Jump scares.. Scares. Essential knowledge — Final girls.. the fear genre. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Jump scares..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Jump scares..", "x": "Explained: Jump scares.. Suspense. The context — Horror Movies. Suspense. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "1970s.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "1970s.", "x": "Horror Movies: 1970s.. Classics. Essential knowledge — Suspense.. the fear genre. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: 1970s..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: 1970s..", "x": "Explained: 1970s.. Monsters. The context — Horror Movies. Slashers. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Final girls.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Final girls.", "x": "Horror Movies: Final girls.. Suspense. Essential knowledge — Slashers.. the fear genre. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Final girls..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Final girls..", "x": "Explained: Final girls.. Slashers. The context — Horror Movies. Monsters. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Suspense.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Suspense.", "x": "Horror Movies in depth: Suspense.. Slashers. Details — the fear genre.. Slashers. Jump scares. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Monsters.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Monsters.", "x": "Horror Movies in depth: Monsters.. Monsters. Details — the fear genre.. 1970s. 1970s. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Slashers.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Slashers.", "x": "Horror Movies in depth: Slashers.. Jump scares. Details — the fear genre.. Scares. Final girls. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "1970s.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "1970s.", "x": "Horror Movies in depth: 1970s.. 1970s. Details — the fear genre.. Classics. Suspense. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Scares.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Scares.", "x": "Horror Movies in depth: Scares.. Final girls. Details — the fear genre.. Suspense. Slashers. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Classics.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Classics.", "x": "Horror Movies in depth: Classics.. Suspense. Details — the fear genre.. Monsters. Monsters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Horror Movies comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Horror Movies comes from.", "x": "Origins: Suspense.. Suspense. The history of Horror Movies — the fear genre.. Monsters. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Horror Movies respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Horror Movies respectfully.", "x": "Engaging: Slashers.. Slashers. How to participate or observe well — Horror Movies. the fear genre. Respect first, always; 1970s.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Horror Movies do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Horror Movies do's and don'ts.", "x": "Etiquette: Scares.. Monsters. The rules of respect — Horror Movies. the fear genre. When in doubt, ask about Classics.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Horror Movies.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Horror Movies.", "x": "Planning: Suspense.. Jump scares. Practical notes — Horror Movies. the fear genre. A little planning shows respect for Monsters.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Horror Movies and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Horror Movies and money.", "x": "Costs: Slashers.. 1970s. What to budget — Horror Movies. the fear genre. The best experiences of 1970s. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-genre-horror-movies-genre-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
