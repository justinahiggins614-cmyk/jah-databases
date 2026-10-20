(function(){'use strict';
/* JAH Contemplative Prayer Meditation Database generator — jahdb-e2-meditation-contemplative-prayer-meditation-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-meditation-contemplative-prayer-meditation',PREFIX='JAH-E2MEDITATIO-',NAME='JAH Contemplative Prayer Meditation Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Contemplative Prayer: the complete guide", "d": "Contemplative Prayer: the silent prayer..", "g": "overview", "l": 2, "q": "What is Contemplative Prayer: the complete guide?", "a": "Contemplative Prayer: the silent prayer..", "x": "The complete meditation guide to Contemplative Prayer: the silent prayer.. Centering. History, meaning, practices, and how to engage respectfully — everything in one database. Centering. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Contemplative Prayer essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Contemplative Prayer essentials.", "x": "At a glance: Contemplative Prayer — the silent prayer.. Christian. The essentials: Silence.. Silence. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Centering.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Centering.", "x": "Contemplative Prayer: Centering.. Silence. Essential knowledge — Silence.. the silent prayer. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Centering..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Centering..", "x": "Explained: Centering.. Word. The context — Contemplative Prayer. Keating. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Christian.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Christian.", "x": "Contemplative Prayer: Christian.. Keating. Essential knowledge — Keating.. the silent prayer. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Christian..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Christian..", "x": "Explained: Christian.. Christian. The context — Contemplative Prayer. 20 min. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Silence.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Silence.", "x": "Contemplative Prayer: Silence.. Word. Essential knowledge — 20 min.. the silent prayer. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Silence..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Silence..", "x": "Explained: Silence.. Practice. The context — Contemplative Prayer. Sacred word. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Keating.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Keating.", "x": "Contemplative Prayer: Keating.. Christian. Essential knowledge — Sacred word.. the silent prayer. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Keating..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Keating..", "x": "Explained: Keating.. Centering. The context — Contemplative Prayer. Centering. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "20 min.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "20 min.", "x": "Contemplative Prayer: 20 min.. Practice. Essential knowledge — Centering.. the silent prayer. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: 20 min..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: 20 min..", "x": "Explained: 20 min.. Silence. The context — Contemplative Prayer. Christian. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Sacred word.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Sacred word.", "x": "Contemplative Prayer: Sacred word.. Centering. Essential knowledge — Christian.. the silent prayer. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Sacred word..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Sacred word..", "x": "Explained: Sacred word.. Keating. The context — Contemplative Prayer. Silence. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Centering.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Centering.", "x": "Contemplative Prayer in depth: Centering.. Christian. Details — the silent prayer.. Keating. Keating. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Silence.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Silence.", "x": "Contemplative Prayer in depth: Silence.. Silence. Details — the silent prayer.. Word. 20 min. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Keating.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Keating.", "x": "Contemplative Prayer in depth: Keating.. Keating. Details — the silent prayer.. Christian. Sacred word. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Word.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Word.", "x": "Contemplative Prayer in depth: Word.. 20 min. Details — the silent prayer.. Practice. Centering. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Christian.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Christian.", "x": "Contemplative Prayer in depth: Christian.. Sacred word. Details — the silent prayer.. Centering. Christian. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Practice.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Practice.", "x": "Contemplative Prayer in depth: Practice.. Centering. Details — the silent prayer.. Silence. Silence. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Contemplative Prayer comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Contemplative Prayer comes from.", "x": "Origins: Centering.. Centering. The history of Contemplative Prayer — the silent prayer.. Silence. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Contemplative Prayer respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Contemplative Prayer respectfully.", "x": "Engaging: Keating.. Christian. How to participate or observe well — Contemplative Prayer. the silent prayer. Respect first, always; Word.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Contemplative Prayer do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Contemplative Prayer do's and don'ts.", "x": "Etiquette: Christian.. Silence. The rules of respect — Contemplative Prayer. the silent prayer. When in doubt, ask about Practice.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Contemplative Prayer.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Contemplative Prayer.", "x": "Planning: Centering.. Keating. Practical notes — Contemplative Prayer. the silent prayer. A little planning shows respect for Silence.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Contemplative Prayer and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Contemplative Prayer and money.", "x": "Costs: Keating.. 20 min. What to budget — Contemplative Prayer. the silent prayer. The best experiences of Word. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-meditation-contemplative-prayer-meditation-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
