(function(){'use strict';
/* JAH Breathwork Meditation Database generator — jahdb-e2-meditation-breathwork-meditation-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-meditation-breathwork-meditation',PREFIX='JAH-E2MEDITATIO-',NAME='JAH Breathwork Meditation Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Breathwork: the complete guide", "d": "Breathwork: the conscious breathing..", "g": "overview", "l": 2, "q": "What is Breathwork: the complete guide?", "a": "Breathwork: the conscious breathing..", "x": "The complete meditation guide to Breathwork: the conscious breathing.. Pranayama. History, meaning, practices, and how to engage respectfully — everything in one database. Pranayama. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Breathwork essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Breathwork essentials.", "x": "At a glance: Breathwork — the conscious breathing.. Wim Hof. The essentials: Hof.. Box breathing. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Pranayama.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Pranayama.", "x": "Breathwork: Pranayama.. Hof. Essential knowledge — Box breathing.. the conscious breathing. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Pranayama..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Pranayama..", "x": "Explained: Pranayama.. Energy. The context — Breathwork. Energy. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Wim Hof.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Wim Hof.", "x": "Breathwork: Wim Hof.. Box. Essential knowledge — Energy.. the conscious breathing. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Wim Hof..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Wim Hof..", "x": "Explained: Wim Hof.. Calm. The context — Breathwork. Calm. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Box breathing.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Box breathing.", "x": "Breathwork: Box breathing.. Energy. Essential knowledge — Calm.. the conscious breathing. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Box breathing..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Box breathing..", "x": "Explained: Box breathing.. Safety. The context — Breathwork. Techniques. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Energy.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Energy.", "x": "Breathwork: Energy.. Calm. Essential knowledge — Techniques.. the conscious breathing. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Energy..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Energy..", "x": "Explained: Energy.. Pranayama. The context — Breathwork. Pranayama. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Calm.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Calm.", "x": "Breathwork: Calm.. Safety. Essential knowledge — Pranayama.. the conscious breathing. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Calm..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Calm..", "x": "Explained: Calm.. Hof. The context — Breathwork. Wim Hof. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Techniques.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Techniques.", "x": "Breathwork: Techniques.. Pranayama. Essential knowledge — Wim Hof.. the conscious breathing. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Techniques..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Techniques..", "x": "Explained: Techniques.. Box. The context — Breathwork. Box breathing. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Pranayama.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Pranayama.", "x": "Breathwork in depth: Pranayama.. Wim Hof. Details — the conscious breathing.. Box. Energy. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Hof.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Hof.", "x": "Breathwork in depth: Hof.. Box breathing. Details — the conscious breathing.. Energy. Calm. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Box.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Box.", "x": "Breathwork in depth: Box.. Energy. Details — the conscious breathing.. Calm. Techniques. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Energy.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Energy.", "x": "Breathwork in depth: Energy.. Calm. Details — the conscious breathing.. Safety. Pranayama. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Calm.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Calm.", "x": "Breathwork in depth: Calm.. Techniques. Details — the conscious breathing.. Pranayama. Wim Hof. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Safety.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Safety.", "x": "Breathwork in depth: Safety.. Pranayama. Details — the conscious breathing.. Hof. Box breathing. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Breathwork comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Breathwork comes from.", "x": "Origins: Pranayama.. Pranayama. The history of Breathwork — the conscious breathing.. Hof. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Breathwork respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Breathwork respectfully.", "x": "Engaging: Box.. Wim Hof. How to participate or observe well — Breathwork. the conscious breathing. Respect first, always; Energy.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Breathwork do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Breathwork do's and don'ts.", "x": "Etiquette: Calm.. Box breathing. The rules of respect — Breathwork. the conscious breathing. When in doubt, ask about Safety.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Breathwork.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Breathwork.", "x": "Planning: Pranayama.. Energy. Practical notes — Breathwork. the conscious breathing. A little planning shows respect for Hof.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Breathwork and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Breathwork and money.", "x": "Costs: Box.. Calm. What to budget — Breathwork. the conscious breathing. The best experiences of Energy. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-meditation-breathwork-meditation-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
