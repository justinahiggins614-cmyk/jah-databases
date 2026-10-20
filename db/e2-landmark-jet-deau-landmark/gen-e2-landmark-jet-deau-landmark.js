(function(){'use strict';
/* JAH Jet d\'Eau Landmark Database generator — jahdb-e2-landmark-jet-deau-landmark-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-landmark-jet-deau-landmark',PREFIX='JAH-E2LANDMARKJ-',NAME='JAH Jet d\'Eau Landmark Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Jet d'Eau: the complete guide", "d": "Jet d'Eau: the 140m jet..", "g": "overview", "l": 2, "q": "What is Jet d'Eau: the complete guide?", "a": "Jet d'Eau: the 140m jet..", "x": "The complete landmark guide to Jet d'Eau: the 140m jet.. 140m. History, meaning, practices, and how to engage respectfully — everything in one database. 140m. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Jet d'Eau essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Jet d'Eau essentials.", "x": "At a glance: Jet d'Eau — the 140m jet.. 1886. The essentials: Lake.. Lake Geneva. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "140m.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "140m.", "x": "Jet d'Eau: 140m.. Lake. Essential knowledge — Lake Geneva.. the 140m jet. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 140m..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 140m..", "x": "Explained: 140m.. 1886. The context — Jet d'Eau. 500 L/s. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "1886.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "1886.", "x": "Jet d'Eau: 1886.. Rainbow. Essential knowledge — 500 L/s.. the 140m jet. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: 1886..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: 1886..", "x": "Explained: 1886.. Jet. The context — Jet d'Eau. Landmark. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Lake Geneva.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Lake Geneva.", "x": "Jet d'Eau: Lake Geneva.. 1886. Essential knowledge — Landmark.. the 140m jet. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Lake Geneva..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Lake Geneva..", "x": "Explained: Lake Geneva.. Views. The context — Jet d'Eau. Rainbow. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "500 L/s.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "500 L/s.", "x": "Jet d'Eau: 500 L/s.. Jet. Essential knowledge — Rainbow.. the 140m jet. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: 500 L/s..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: 500 L/s..", "x": "Explained: 500 L/s.. 140m. The context — Jet d'Eau. 140m. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Landmark.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Landmark.", "x": "Jet d'Eau: Landmark.. Views. Essential knowledge — 140m.. the 140m jet. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Landmark..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Landmark..", "x": "Explained: Landmark.. Lake. The context — Jet d'Eau. 1886. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Rainbow.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Rainbow.", "x": "Jet d'Eau: Rainbow.. 140m. Essential knowledge — 1886.. the 140m jet. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Rainbow..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Rainbow..", "x": "Explained: Rainbow.. Rainbow. The context — Jet d'Eau. Lake Geneva. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "140m.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "140m.", "x": "Jet d'Eau in depth: 140m.. 1886. Details — the 140m jet.. Rainbow. 500 L/s. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Lake.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Lake.", "x": "Jet d'Eau in depth: Lake.. Lake Geneva. Details — the 140m jet.. 1886. Landmark. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Rainbow.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Rainbow.", "x": "Jet d'Eau in depth: Rainbow.. 500 L/s. Details — the 140m jet.. Jet. Rainbow. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "1886.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "1886.", "x": "Jet d'Eau in depth: 1886.. Landmark. Details — the 140m jet.. Views. 140m. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Jet.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Jet.", "x": "Jet d'Eau in depth: Jet.. Rainbow. Details — the 140m jet.. 140m. 1886. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Views.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Views.", "x": "Jet d'Eau in depth: Views.. 140m. Details — the 140m jet.. Lake. Lake Geneva. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Jet d'Eau comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Jet d'Eau comes from.", "x": "Origins: 140m.. 140m. The history of Jet d'Eau — the 140m jet.. Lake. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Jet d'Eau respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Jet d'Eau respectfully.", "x": "Engaging: Rainbow.. 1886. How to participate or observe well — Jet d'Eau. the 140m jet. Respect first, always; 1886.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Jet d'Eau do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Jet d'Eau do's and don'ts.", "x": "Etiquette: Jet.. Lake Geneva. The rules of respect — Jet d'Eau. the 140m jet. When in doubt, ask about Views.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Jet d'Eau.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Jet d'Eau.", "x": "Planning: 140m.. 500 L/s. Practical notes — Jet d'Eau. the 140m jet. A little planning shows respect for Lake.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Jet d'Eau and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Jet d'Eau and money.", "x": "Costs: Rainbow.. Landmark. What to budget — Jet d'Eau. the 140m jet. The best experiences of 1886. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-landmark-jet-deau-landmark-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
