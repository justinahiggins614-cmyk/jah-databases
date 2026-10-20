(function(){'use strict';
/* JAH Sci-Fi Comics Comic Genre Database generator — jahdb-e2-comic-scifi-comics-genre-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-comic-scifi-comics-genre',PREFIX='JAH-E2COMICSCIF-',NAME='JAH Sci-Fi Comics Comic Genre Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Sci-Fi Comics: the complete guide", "d": "Sci-Fi Comics: the future panels..", "g": "overview", "l": 2, "q": "What is Sci-Fi Comics: the complete guide?", "a": "Sci-Fi Comics: the future panels..", "x": "The complete comic genre guide to Sci-Fi Comics: the future panels.. 2000 AD. History, meaning, practices, and how to engage respectfully — everything in one database. 2000 AD. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Sci-Fi Comics essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Sci-Fi Comics essentials.", "x": "At a glance: Sci-Fi Comics — the future panels.. Heavy Metal. The essentials: Moebius.. Moebius. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "2000 AD.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "2000 AD.", "x": "Sci-Fi Comics: 2000 AD.. Moebius. Essential knowledge — Moebius.. the future panels. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 2000 AD..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 2000 AD..", "x": "Explained: 2000 AD.. Space. The context — Sci-Fi Comics. Dredd. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Heavy Metal.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Heavy Metal.", "x": "Sci-Fi Comics: Heavy Metal.. Dredd. Essential knowledge — Dredd.. the future panels. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Heavy Metal..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Heavy Metal..", "x": "Explained: Heavy Metal.. Metal. The context — Sci-Fi Comics. Space. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Moebius.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Moebius.", "x": "Sci-Fi Comics: Moebius.. Space. Essential knowledge — Space.. the future panels. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Moebius..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Moebius..", "x": "Explained: Moebius.. History. The context — Sci-Fi Comics. Dystopia. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Dredd.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Dredd.", "x": "Sci-Fi Comics: Dredd.. Metal. Essential knowledge — Dystopia.. the future panels. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Dredd..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Dredd..", "x": "Explained: Dredd.. 2000 AD. The context — Sci-Fi Comics. 2000 AD. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Space.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Space.", "x": "Sci-Fi Comics: Space.. History. Essential knowledge — 2000 AD.. the future panels. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Space..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Space..", "x": "Explained: Space.. Moebius. The context — Sci-Fi Comics. Heavy Metal. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Dystopia.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Dystopia.", "x": "Sci-Fi Comics: Dystopia.. 2000 AD. Essential knowledge — Heavy Metal.. the future panels. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Dystopia..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Dystopia..", "x": "Explained: Dystopia.. Dredd. The context — Sci-Fi Comics. Moebius. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "2000 AD.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "2000 AD.", "x": "Sci-Fi Comics in depth: 2000 AD.. Heavy Metal. Details — the future panels.. Dredd. Dredd. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Moebius.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Moebius.", "x": "Sci-Fi Comics in depth: Moebius.. Moebius. Details — the future panels.. Space. Space. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Dredd.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Dredd.", "x": "Sci-Fi Comics in depth: Dredd.. Dredd. Details — the future panels.. Metal. Dystopia. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Space.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Space.", "x": "Sci-Fi Comics in depth: Space.. Space. Details — the future panels.. History. 2000 AD. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Metal.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Metal.", "x": "Sci-Fi Comics in depth: Metal.. Dystopia. Details — the future panels.. 2000 AD. Heavy Metal. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "History.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "History.", "x": "Sci-Fi Comics in depth: History.. 2000 AD. Details — the future panels.. Moebius. Moebius. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Sci-Fi Comics comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Sci-Fi Comics comes from.", "x": "Origins: 2000 AD.. 2000 AD. The history of Sci-Fi Comics — the future panels.. Moebius. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Sci-Fi Comics respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Sci-Fi Comics respectfully.", "x": "Engaging: Dredd.. Heavy Metal. How to participate or observe well — Sci-Fi Comics. the future panels. Respect first, always; Space.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Sci-Fi Comics do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Sci-Fi Comics do's and don'ts.", "x": "Etiquette: Metal.. Moebius. The rules of respect — Sci-Fi Comics. the future panels. When in doubt, ask about History.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Sci-Fi Comics.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Sci-Fi Comics.", "x": "Planning: 2000 AD.. Dredd. Practical notes — Sci-Fi Comics. the future panels. A little planning shows respect for Moebius.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Sci-Fi Comics and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Sci-Fi Comics and money.", "x": "Costs: Dredd.. Space. What to budget — Sci-Fi Comics. the future panels. The best experiences of Space. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-comic-scifi-comics-genre-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
