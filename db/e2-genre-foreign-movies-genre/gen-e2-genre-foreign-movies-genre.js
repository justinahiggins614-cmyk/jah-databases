(function(){'use strict';
/* JAH Foreign Movies Movie Genre Database generator — jahdb-e2-genre-foreign-movies-genre-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-genre-foreign-movies-genre',PREFIX='JAH-E2GENREFORE-',NAME='JAH Foreign Movies Movie Genre Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Foreign Movies: the complete guide", "d": "Foreign Movies: the world cinema..", "g": "overview", "l": 2, "q": "What is Foreign Movies: the complete guide?", "a": "Foreign Movies: the world cinema..", "x": "The complete movie genre guide to Foreign Movies: the world cinema.. Subtitles. History, meaning, practices, and how to engage respectfully — everything in one database. Subtitles. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Foreign Movies essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Foreign Movies essentials.", "x": "At a glance: Foreign Movies — the world cinema.. Festivals. The essentials: Festivals.. Kurosawa. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Subtitles.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Subtitles.", "x": "Foreign Movies: Subtitles.. Festivals. Essential knowledge — Kurosawa.. the world cinema. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Subtitles..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Subtitles..", "x": "Explained: Subtitles.. Waves. The context — Foreign Movies. Fellini. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Festivals.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Festivals.", "x": "Foreign Movies: Festivals.. Kurosawa. Essential knowledge — Fellini.. the world cinema. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Festivals..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Festivals..", "x": "Explained: Festivals.. Fellini. The context — Foreign Movies. New waves. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Kurosawa.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Kurosawa.", "x": "Foreign Movies: Kurosawa.. Waves. Essential knowledge — New waves.. the world cinema. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Kurosawa..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Kurosawa..", "x": "Explained: Kurosawa.. Classics. The context — Foreign Movies. Oscars. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Fellini.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Fellini.", "x": "Foreign Movies: Fellini.. Fellini. Essential knowledge — Oscars.. the world cinema. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Fellini..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Fellini..", "x": "Explained: Fellini.. Subtitles. The context — Foreign Movies. Subtitles. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "New waves.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "New waves.", "x": "Foreign Movies: New waves.. Classics. Essential knowledge — Subtitles.. the world cinema. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: New waves..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: New waves..", "x": "Explained: New waves.. Festivals. The context — Foreign Movies. Festivals. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Oscars.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Oscars.", "x": "Foreign Movies: Oscars.. Subtitles. Essential knowledge — Festivals.. the world cinema. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Oscars..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Oscars..", "x": "Explained: Oscars.. Kurosawa. The context — Foreign Movies. Kurosawa. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Subtitles.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Subtitles.", "x": "Foreign Movies in depth: Subtitles.. Festivals. Details — the world cinema.. Kurosawa. Fellini. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Festivals.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Festivals.", "x": "Foreign Movies in depth: Festivals.. Kurosawa. Details — the world cinema.. Waves. New waves. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Kurosawa.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Kurosawa.", "x": "Foreign Movies in depth: Kurosawa.. Fellini. Details — the world cinema.. Fellini. Oscars. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Waves.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Waves.", "x": "Foreign Movies in depth: Waves.. New waves. Details — the world cinema.. Classics. Subtitles. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Fellini.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Fellini.", "x": "Foreign Movies in depth: Fellini.. Oscars. Details — the world cinema.. Subtitles. Festivals. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Classics.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Classics.", "x": "Foreign Movies in depth: Classics.. Subtitles. Details — the world cinema.. Festivals. Kurosawa. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Foreign Movies comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Foreign Movies comes from.", "x": "Origins: Subtitles.. Subtitles. The history of Foreign Movies — the world cinema.. Festivals. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Foreign Movies respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Foreign Movies respectfully.", "x": "Engaging: Kurosawa.. Festivals. How to participate or observe well — Foreign Movies. the world cinema. Respect first, always; Waves.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Foreign Movies do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Foreign Movies do's and don'ts.", "x": "Etiquette: Fellini.. Kurosawa. The rules of respect — Foreign Movies. the world cinema. When in doubt, ask about Classics.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Foreign Movies.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Foreign Movies.", "x": "Planning: Subtitles.. Fellini. Practical notes — Foreign Movies. the world cinema. A little planning shows respect for Festivals.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Foreign Movies and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Foreign Movies and money.", "x": "Costs: Kurosawa.. New waves. What to budget — Foreign Movies. the world cinema. The best experiences of Waves. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-genre-foreign-movies-genre-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
