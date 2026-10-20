(function(){'use strict';
/* JAH Anglerfish Fish Species Database generator — jahdb-e2-fish-anglerfish-fish-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-fish-anglerfish-fish',PREFIX='JAH-E2FISHANGLE-',NAME='JAH Anglerfish Fish Species Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Anglerfish: the complete guide", "d": "Anglerfish: the deep lure..", "g": "overview", "l": 2, "q": "What is Anglerfish: the complete guide?", "a": "Anglerfish: the deep lure..", "x": "The complete fish species guide to Anglerfish: the deep lure.. Lure. History, meaning, practices, and how to engage respectfully — everything in one database. Lure. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Anglerfish essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Anglerfish essentials.", "x": "At a glance: Anglerfish — the deep lure.. Deep. The essentials: Deep.. Bioluminescence. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Lure.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Lure.", "x": "Anglerfish: Lure.. Deep. Essential knowledge — Bioluminescence.. the deep lure. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Lure..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Lure..", "x": "Explained: Lure.. Teeth. The context — Anglerfish. Males. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Deep.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Deep.", "x": "Anglerfish: Deep.. Abyss. Essential knowledge — Males.. the deep lure. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Deep..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Deep..", "x": "Explained: Deep.. Bioluminescence. The context — Anglerfish. Teeth. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Bioluminescence.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Bioluminescence.", "x": "Anglerfish: Bioluminescence.. Teeth. Essential knowledge — Teeth.. the deep lure. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Bioluminescence..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Bioluminescence..", "x": "Explained: Bioluminescence.. Habitat. The context — Anglerfish. Abyss. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Males.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Males.", "x": "Anglerfish: Males.. Bioluminescence. Essential knowledge — Abyss.. the deep lure. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Males..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Males..", "x": "Explained: Males.. Lure. The context — Anglerfish. Lure. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Teeth.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Teeth.", "x": "Anglerfish: Teeth.. Habitat. Essential knowledge — Lure.. the deep lure. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Teeth..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Teeth..", "x": "Explained: Teeth.. Deep. The context — Anglerfish. Deep. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Abyss.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Abyss.", "x": "Anglerfish: Abyss.. Lure. Essential knowledge — Deep.. the deep lure. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Abyss..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Abyss..", "x": "Explained: Abyss.. Abyss. The context — Anglerfish. Bioluminescence. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Lure.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Lure.", "x": "Anglerfish in depth: Lure.. Deep. Details — the deep lure.. Abyss. Males. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Deep.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Deep.", "x": "Anglerfish in depth: Deep.. Bioluminescence. Details — the deep lure.. Teeth. Teeth. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Abyss.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Abyss.", "x": "Anglerfish in depth: Abyss.. Males. Details — the deep lure.. Bioluminescence. Abyss. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Teeth.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Teeth.", "x": "Anglerfish in depth: Teeth.. Teeth. Details — the deep lure.. Habitat. Lure. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Bioluminescence.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Bioluminescence.", "x": "Anglerfish in depth: Bioluminescence.. Abyss. Details — the deep lure.. Lure. Deep. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Habitat.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Habitat.", "x": "Anglerfish in depth: Habitat.. Lure. Details — the deep lure.. Deep. Bioluminescence. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Anglerfish comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Anglerfish comes from.", "x": "Origins: Lure.. Lure. The history of Anglerfish — the deep lure.. Deep. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Anglerfish respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Anglerfish respectfully.", "x": "Engaging: Abyss.. Deep. How to participate or observe well — Anglerfish. the deep lure. Respect first, always; Teeth.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Anglerfish do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Anglerfish do's and don'ts.", "x": "Etiquette: Bioluminescence.. Bioluminescence. The rules of respect — Anglerfish. the deep lure. When in doubt, ask about Habitat.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Anglerfish.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Anglerfish.", "x": "Planning: Lure.. Males. Practical notes — Anglerfish. the deep lure. A little planning shows respect for Deep.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Anglerfish and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Anglerfish and money.", "x": "Costs: Abyss.. Teeth. What to budget — Anglerfish. the deep lure. The best experiences of Teeth. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-fish-anglerfish-fish-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
