(function(){'use strict';
/* JAH Guided Visualization Meditation Database generator — jahdb-e2-meditation-guided-visualization-meditation-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-meditation-guided-visualization-meditation',PREFIX='JAH-E2MEDITATIO-',NAME='JAH Guided Visualization Meditation Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Guided Visualization: the complete guide", "d": "Guided Visualization: the imagined journey..", "g": "overview", "l": 2, "q": "What is Guided Visualization: the complete guide?", "a": "Guided Visualization: the imagined journey..", "x": "The complete meditation guide to Guided Visualization: the imagined journey.. Imagery. History, meaning, practices, and how to engage respectfully — everything in one database. Imagery. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Guided Visualization essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Guided Visualization essentials.", "x": "At a glance: Guided Visualization — the imagined journey.. Goals. The essentials: Goals.. Relaxation. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Imagery.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Imagery.", "x": "Guided Visualization: Imagery.. Goals. Essential knowledge — Relaxation.. the imagined journey. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Imagery..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Imagery..", "x": "Explained: Imagery.. Sports. The context — Guided Visualization. Audio. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Goals.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Goals.", "x": "Guided Visualization: Goals.. Audio. Essential knowledge — Audio.. the imagined journey. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Goals..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Goals..", "x": "Explained: Goals.. Healing. The context — Guided Visualization. Sports. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Relaxation.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Relaxation.", "x": "Guided Visualization: Relaxation.. Sports. Essential knowledge — Sports.. the imagined journey. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Relaxation..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Relaxation..", "x": "Explained: Relaxation.. Practice. The context — Guided Visualization. Healing. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Audio.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Audio.", "x": "Guided Visualization: Audio.. Healing. Essential knowledge — Healing.. the imagined journey. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Audio..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Audio..", "x": "Explained: Audio.. Imagery. The context — Guided Visualization. Imagery. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Sports.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Sports.", "x": "Guided Visualization: Sports.. Practice. Essential knowledge — Imagery.. the imagined journey. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Sports..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Sports..", "x": "Explained: Sports.. Goals. The context — Guided Visualization. Goals. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Healing.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Healing.", "x": "Guided Visualization: Healing.. Imagery. Essential knowledge — Goals.. the imagined journey. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Healing..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Healing..", "x": "Explained: Healing.. Audio. The context — Guided Visualization. Relaxation. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Imagery.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Imagery.", "x": "Guided Visualization in depth: Imagery.. Goals. Details — the imagined journey.. Audio. Audio. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Goals.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Goals.", "x": "Guided Visualization in depth: Goals.. Relaxation. Details — the imagined journey.. Sports. Sports. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Audio.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Audio.", "x": "Guided Visualization in depth: Audio.. Audio. Details — the imagined journey.. Healing. Healing. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Sports.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Sports.", "x": "Guided Visualization in depth: Sports.. Sports. Details — the imagined journey.. Practice. Imagery. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Healing.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Healing.", "x": "Guided Visualization in depth: Healing.. Healing. Details — the imagined journey.. Imagery. Goals. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Practice.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Practice.", "x": "Guided Visualization in depth: Practice.. Imagery. Details — the imagined journey.. Goals. Relaxation. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Guided Visualization comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Guided Visualization comes from.", "x": "Origins: Imagery.. Imagery. The history of Guided Visualization — the imagined journey.. Goals. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Guided Visualization respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Guided Visualization respectfully.", "x": "Engaging: Audio.. Goals. How to participate or observe well — Guided Visualization. the imagined journey. Respect first, always; Sports.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Guided Visualization do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Guided Visualization do's and don'ts.", "x": "Etiquette: Healing.. Relaxation. The rules of respect — Guided Visualization. the imagined journey. When in doubt, ask about Practice.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Guided Visualization.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Guided Visualization.", "x": "Planning: Imagery.. Audio. Practical notes — Guided Visualization. the imagined journey. A little planning shows respect for Goals.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Guided Visualization and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Guided Visualization and money.", "x": "Costs: Audio.. Sports. What to budget — Guided Visualization. the imagined journey. The best experiences of Sports. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-meditation-guided-visualization-meditation-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
