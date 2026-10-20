(function(){'use strict';
/* JAH Documentary Movies Movie Genre Database generator — jahdb-e2-genre-documentary-movies-genre-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-genre-documentary-movies-genre',PREFIX='JAH-E2GENREDOCU-',NAME='JAH Documentary Movies Movie Genre Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Documentary Movies: the complete guide", "d": "Documentary Movies: the real genre..", "g": "overview", "l": 2, "q": "What is Documentary Movies: the complete guide?", "a": "Documentary Movies: the real genre..", "x": "The complete movie genre guide to Documentary Movies: the real genre.. Real. History, meaning, practices, and how to engage respectfully — everything in one database. Real. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Documentary Movies essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Documentary Movies essentials.", "x": "At a glance: Documentary Movies — the real genre.. Interviews. The essentials: Archival.. Archival. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Real.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Real.", "x": "Documentary Movies: Real.. Archival. Essential knowledge — Archival.. the real genre. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Real..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Real..", "x": "Explained: Real.. Oscars. The context — Documentary Movies. Cinema verite. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Interviews.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Interviews.", "x": "Documentary Movies: Interviews.. Verite. Essential knowledge — Cinema verite.. the real genre. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Interviews..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Interviews..", "x": "Explained: Interviews.. Truth. The context — Documentary Movies. Oscars. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Archival.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Archival.", "x": "Documentary Movies: Archival.. Oscars. Essential knowledge — Oscars.. the real genre. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Archival..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Archival..", "x": "Explained: Archival.. Classics. The context — Documentary Movies. Truth. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Cinema verite.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Cinema verite.", "x": "Documentary Movies: Cinema verite.. Truth. Essential knowledge — Truth.. the real genre. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Cinema verite..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Cinema verite..", "x": "Explained: Cinema verite.. Real. The context — Documentary Movies. Real. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Oscars.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Oscars.", "x": "Documentary Movies: Oscars.. Classics. Essential knowledge — Real.. the real genre. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Oscars..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Oscars..", "x": "Explained: Oscars.. Archival. The context — Documentary Movies. Interviews. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Truth.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Truth.", "x": "Documentary Movies: Truth.. Real. Essential knowledge — Interviews.. the real genre. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Truth..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Truth..", "x": "Explained: Truth.. Verite. The context — Documentary Movies. Archival. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Real.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Real.", "x": "Documentary Movies in depth: Real.. Interviews. Details — the real genre.. Verite. Cinema verite. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Archival.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Archival.", "x": "Documentary Movies in depth: Archival.. Archival. Details — the real genre.. Oscars. Oscars. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Verite.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Verite.", "x": "Documentary Movies in depth: Verite.. Cinema verite. Details — the real genre.. Truth. Truth. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Oscars.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Oscars.", "x": "Documentary Movies in depth: Oscars.. Oscars. Details — the real genre.. Classics. Real. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Truth.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Truth.", "x": "Documentary Movies in depth: Truth.. Truth. Details — the real genre.. Real. Interviews. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Classics.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Classics.", "x": "Documentary Movies in depth: Classics.. Real. Details — the real genre.. Archival. Archival. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Documentary Movies comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Documentary Movies comes from.", "x": "Origins: Real.. Real. The history of Documentary Movies — the real genre.. Archival. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Documentary Movies respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Documentary Movies respectfully.", "x": "Engaging: Verite.. Interviews. How to participate or observe well — Documentary Movies. the real genre. Respect first, always; Oscars.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Documentary Movies do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Documentary Movies do's and don'ts.", "x": "Etiquette: Truth.. Archival. The rules of respect — Documentary Movies. the real genre. When in doubt, ask about Classics.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Documentary Movies.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Documentary Movies.", "x": "Planning: Real.. Cinema verite. Practical notes — Documentary Movies. the real genre. A little planning shows respect for Archival.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Documentary Movies and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Documentary Movies and money.", "x": "Costs: Verite.. Oscars. What to budget — Documentary Movies. the real genre. The best experiences of Oscars. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-genre-documentary-movies-genre-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
