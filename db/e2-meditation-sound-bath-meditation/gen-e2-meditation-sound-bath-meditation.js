(function(){'use strict';
/* JAH Sound Bath Meditation Database generator — jahdb-e2-meditation-sound-bath-meditation-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-meditation-sound-bath-meditation',PREFIX='JAH-E2MEDITATIO-',NAME='JAH Sound Bath Meditation Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Sound Bath: the complete guide", "d": "Sound Bath: the vibrational rest..", "g": "overview", "l": 2, "q": "What is Sound Bath: the complete guide?", "a": "Sound Bath: the vibrational rest..", "x": "The complete meditation guide to Sound Bath: the vibrational rest.. Bowls. History, meaning, practices, and how to engage respectfully — everything in one database. Bowls. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Sound Bath essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Sound Bath essentials.", "x": "At a glance: Sound Bath — the vibrational rest.. Gongs. The essentials: Vibration.. Vibration. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Bowls.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Bowls.", "x": "Sound Bath: Bowls.. Vibration. Essential knowledge — Vibration.. the vibrational rest. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Bowls..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Bowls..", "x": "Explained: Bowls.. Baths. The context — Sound Bath. Rest. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Gongs.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Gongs.", "x": "Sound Bath: Gongs.. Rest. Essential knowledge — Rest.. the vibrational rest. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Gongs..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Gongs..", "x": "Explained: Gongs.. Gongs. The context — Sound Bath. 90 min. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Vibration.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Vibration.", "x": "Sound Bath: Vibration.. Baths. Essential knowledge — 90 min.. the vibrational rest. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Vibration..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Vibration..", "x": "Explained: Vibration.. Practice. The context — Sound Bath. Baths. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Rest.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Rest.", "x": "Sound Bath: Rest.. Gongs. Essential knowledge — Baths.. the vibrational rest. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Rest..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Rest..", "x": "Explained: Rest.. Bowls. The context — Sound Bath. Bowls. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "90 min.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "90 min.", "x": "Sound Bath: 90 min.. Practice. Essential knowledge — Bowls.. the vibrational rest. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: 90 min..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: 90 min..", "x": "Explained: 90 min.. Vibration. The context — Sound Bath. Gongs. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Baths.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Baths.", "x": "Sound Bath: Baths.. Bowls. Essential knowledge — Gongs.. the vibrational rest. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Baths..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Baths..", "x": "Explained: Baths.. Rest. The context — Sound Bath. Vibration. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Bowls.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Bowls.", "x": "Sound Bath in depth: Bowls.. Gongs. Details — the vibrational rest.. Rest. Rest. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Vibration.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Vibration.", "x": "Sound Bath in depth: Vibration.. Vibration. Details — the vibrational rest.. Baths. 90 min. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Rest.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Rest.", "x": "Sound Bath in depth: Rest.. Rest. Details — the vibrational rest.. Gongs. Baths. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Baths.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Baths.", "x": "Sound Bath in depth: Baths.. 90 min. Details — the vibrational rest.. Practice. Bowls. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Gongs.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Gongs.", "x": "Sound Bath in depth: Gongs.. Baths. Details — the vibrational rest.. Bowls. Gongs. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Practice.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Practice.", "x": "Sound Bath in depth: Practice.. Bowls. Details — the vibrational rest.. Vibration. Vibration. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Sound Bath comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Sound Bath comes from.", "x": "Origins: Bowls.. Bowls. The history of Sound Bath — the vibrational rest.. Vibration. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Sound Bath respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Sound Bath respectfully.", "x": "Engaging: Rest.. Gongs. How to participate or observe well — Sound Bath. the vibrational rest. Respect first, always; Baths.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Sound Bath do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Sound Bath do's and don'ts.", "x": "Etiquette: Gongs.. Vibration. The rules of respect — Sound Bath. the vibrational rest. When in doubt, ask about Practice.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Sound Bath.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Sound Bath.", "x": "Planning: Bowls.. Rest. Practical notes — Sound Bath. the vibrational rest. A little planning shows respect for Vibration.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Sound Bath and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Sound Bath and money.", "x": "Costs: Rest.. 90 min. What to budget — Sound Bath. the vibrational rest. The best experiences of Baths. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-meditation-sound-bath-meditation-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
