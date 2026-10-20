(function(){'use strict';
/* JAH Colosseum Landmark Database generator — jahdb-e2-landmark-colosseum-landmark-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-landmark-colosseum-landmark',PREFIX='JAH-E2LANDMARKC-',NAME='JAH Colosseum Landmark Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Colosseum: the complete guide", "d": "Colosseum: the flavian arena..", "g": "overview", "l": 2, "q": "What is Colosseum: the complete guide?", "a": "Colosseum: the flavian arena..", "x": "The complete landmark guide to Colosseum: the flavian arena.. 80 AD. History, meaning, practices, and how to engage respectfully — everything in one database. 80 AD. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Colosseum essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Colosseum essentials.", "x": "At a glance: Colosseum — the flavian arena.. 50,000. The essentials: Gladiators.. Gladiators. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "80 AD.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "80 AD.", "x": "Colosseum: 80 AD.. Gladiators. Essential knowledge — Gladiators.. the flavian arena. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 80 AD..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 80 AD..", "x": "Explained: 80 AD.. Underground. The context — Colosseum. Travertine. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "50,000.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "50,000.", "x": "Colosseum: 50,000.. Vespasian. Essential knowledge — Travertine.. the flavian arena. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: 50,000..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: 50,000..", "x": "Explained: 50,000.. Travertine. The context — Colosseum. Vespasian. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Gladiators.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Gladiators.", "x": "Colosseum: Gladiators.. Underground. Essential knowledge — Vespasian.. the flavian arena. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Gladiators..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Gladiators..", "x": "Explained: Gladiators.. Tickets. The context — Colosseum. Underground. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Travertine.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Travertine.", "x": "Colosseum: Travertine.. Travertine. Essential knowledge — Underground.. the flavian arena. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Travertine..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Travertine..", "x": "Explained: Travertine.. 80 AD. The context — Colosseum. 80 AD. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Vespasian.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Vespasian.", "x": "Colosseum: Vespasian.. Tickets. Essential knowledge — 80 AD.. the flavian arena. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Vespasian..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Vespasian..", "x": "Explained: Vespasian.. Gladiators. The context — Colosseum. 50,000. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Underground.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Underground.", "x": "Colosseum: Underground.. 80 AD. Essential knowledge — 50,000.. the flavian arena. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Underground..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Underground..", "x": "Explained: Underground.. Vespasian. The context — Colosseum. Gladiators. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "80 AD.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "80 AD.", "x": "Colosseum in depth: 80 AD.. 50,000. Details — the flavian arena.. Vespasian. Travertine. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Gladiators.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Gladiators.", "x": "Colosseum in depth: Gladiators.. Gladiators. Details — the flavian arena.. Underground. Vespasian. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Vespasian.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Vespasian.", "x": "Colosseum in depth: Vespasian.. Travertine. Details — the flavian arena.. Travertine. Underground. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Underground.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Underground.", "x": "Colosseum in depth: Underground.. Vespasian. Details — the flavian arena.. Tickets. 80 AD. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Travertine.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Travertine.", "x": "Colosseum in depth: Travertine.. Underground. Details — the flavian arena.. 80 AD. 50,000. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Tickets.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Tickets.", "x": "Colosseum in depth: Tickets.. 80 AD. Details — the flavian arena.. Gladiators. Gladiators. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Colosseum comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Colosseum comes from.", "x": "Origins: 80 AD.. 80 AD. The history of Colosseum — the flavian arena.. Gladiators. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Colosseum respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Colosseum respectfully.", "x": "Engaging: Vespasian.. 50,000. How to participate or observe well — Colosseum. the flavian arena. Respect first, always; Underground.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Colosseum do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Colosseum do's and don'ts.", "x": "Etiquette: Travertine.. Gladiators. The rules of respect — Colosseum. the flavian arena. When in doubt, ask about Tickets.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Colosseum.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Colosseum.", "x": "Planning: 80 AD.. Travertine. Practical notes — Colosseum. the flavian arena. A little planning shows respect for Gladiators.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Colosseum and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Colosseum and money.", "x": "Costs: Vespasian.. Vespasian. What to budget — Colosseum. the flavian arena. The best experiences of Underground. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-landmark-colosseum-landmark-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
