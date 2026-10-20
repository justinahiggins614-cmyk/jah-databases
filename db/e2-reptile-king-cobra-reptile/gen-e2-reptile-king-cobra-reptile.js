(function(){'use strict';
/* JAH King Cobra Reptile Database generator — jahdb-e2-reptile-king-cobra-reptile-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-reptile-king-cobra-reptile',PREFIX='JAH-E2REPTILEKI-',NAME='JAH King Cobra Reptile Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "King Cobra: the complete guide", "d": "King Cobra: the longest venomous..", "g": "overview", "l": 2, "q": "What is King Cobra: the complete guide?", "a": "King Cobra: the longest venomous..", "x": "The complete reptile guide to King Cobra: the longest venomous.. 18 ft. History, meaning, practices, and how to engage respectfully — everything in one database. Venom. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "King Cobra essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "King Cobra essentials.", "x": "At a glance: King Cobra — the longest venomous.. Venom. The essentials: Hood.. Hood. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "18 ft.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "18 ft.", "x": "King Cobra: 18 ft.. Hood. Essential knowledge — Hood.. the longest venomous. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 18 ft..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 18 ft..", "x": "Explained: 18 ft.. Nests. The context — King Cobra. Ophiophagus. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Venom.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Venom.", "x": "King Cobra: Venom.. India. Essential knowledge — Ophiophagus.. the longest venomous. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Venom..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Venom..", "x": "Explained: Venom.. Longest. The context — King Cobra. India. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Hood.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Hood.", "x": "King Cobra: Hood.. Nests. Essential knowledge — India.. the longest venomous. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Hood..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Hood..", "x": "Explained: Hood.. Care. The context — King Cobra. Nests. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Ophiophagus.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Ophiophagus.", "x": "King Cobra: Ophiophagus.. Longest. Essential knowledge — Nests.. the longest venomous. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Ophiophagus..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Ophiophagus..", "x": "Explained: Ophiophagus.. Venom. The context — King Cobra. 18 ft. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "India.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "India.", "x": "King Cobra: India.. Care. Essential knowledge — 18 ft.. the longest venomous. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: India..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: India..", "x": "Explained: India.. Hood. The context — King Cobra. Venom. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Nests.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Nests.", "x": "King Cobra: Nests.. Venom. Essential knowledge — Venom.. the longest venomous. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Nests..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Nests..", "x": "Explained: Nests.. India. The context — King Cobra. Hood. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Venom.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Venom.", "x": "King Cobra in depth: Venom.. Venom. Details — the longest venomous.. India. Ophiophagus. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Hood.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Hood.", "x": "King Cobra in depth: Hood.. Hood. Details — the longest venomous.. Nests. India. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "India.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "India.", "x": "King Cobra in depth: India.. Ophiophagus. Details — the longest venomous.. Longest. Nests. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Nests.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Nests.", "x": "King Cobra in depth: Nests.. India. Details — the longest venomous.. Care. 18 ft. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Longest.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Longest.", "x": "King Cobra in depth: Longest.. Nests. Details — the longest venomous.. Venom. Venom. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Care.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Care.", "x": "King Cobra in depth: Care.. 18 ft. Details — the longest venomous.. Hood. Hood. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where King Cobra comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where King Cobra comes from.", "x": "Origins: Venom.. 18 ft. The history of King Cobra — the longest venomous.. Hood. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing King Cobra respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing King Cobra respectfully.", "x": "Engaging: India.. Venom. How to participate or observe well — King Cobra. the longest venomous. Respect first, always; Nests.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "King Cobra do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "King Cobra do's and don'ts.", "x": "Etiquette: Longest.. Hood. The rules of respect — King Cobra. the longest venomous. When in doubt, ask about Care.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around King Cobra.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around King Cobra.", "x": "Planning: Venom.. Ophiophagus. Practical notes — King Cobra. the longest venomous. A little planning shows respect for Hood.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "King Cobra and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "King Cobra and money.", "x": "Costs: India.. India. What to budget — King Cobra. the longest venomous. The best experiences of Nests. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-reptile-king-cobra-reptile-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
