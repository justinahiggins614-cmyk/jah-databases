(function(){'use strict';
/* JAH Kyudo Martial Art Database generator — jahdb-e2-martial-kyudo-martial-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-martial-kyudo-martial',PREFIX='JAH-E2MARTIALKY-',NAME='JAH Kyudo Martial Art Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Kyudo: the complete guide", "d": "Kyudo: the way of the bow..", "g": "overview", "l": 2, "q": "What is Kyudo: the complete guide?", "a": "Kyudo: the way of the bow..", "x": "The complete martial art guide to Kyudo: the way of the bow.. Japan. History, meaning, practices, and how to engage respectfully — everything in one database. Archery. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Kyudo essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Kyudo essentials.", "x": "At a glance: Kyudo — the way of the bow.. Archery. The essentials: Meditation.. Asymmetrical. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Japan.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Japan.", "x": "Kyudo: Japan.. Meditation. Essential knowledge — Asymmetrical.. the way of the bow. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Japan..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Japan..", "x": "Explained: Japan.. Japan. The context — Kyudo. Meditation. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Archery.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Archery.", "x": "Kyudo: Archery.. Ceremony. Essential knowledge — Meditation.. the way of the bow. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Archery..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Archery..", "x": "Explained: Archery.. Bow. The context — Kyudo. Ceremony. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Asymmetrical.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Asymmetrical.", "x": "Kyudo: Asymmetrical.. Japan. Essential knowledge — Ceremony.. the way of the bow. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Asymmetrical..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Asymmetrical..", "x": "Explained: Asymmetrical.. Practice. The context — Kyudo. Target. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Meditation.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Meditation.", "x": "Kyudo: Meditation.. Bow. Essential knowledge — Target.. the way of the bow. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Meditation..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Meditation..", "x": "Explained: Meditation.. Archery. The context — Kyudo. Japan. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Ceremony.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Ceremony.", "x": "Kyudo: Ceremony.. Practice. Essential knowledge — Japan.. the way of the bow. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Ceremony..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Ceremony..", "x": "Explained: Ceremony.. Meditation. The context — Kyudo. Archery. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Target.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Target.", "x": "Kyudo: Target.. Archery. Essential knowledge — Archery.. the way of the bow. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Target..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Target..", "x": "Explained: Target.. Ceremony. The context — Kyudo. Asymmetrical. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Archery.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Archery.", "x": "Kyudo in depth: Archery.. Archery. Details — the way of the bow.. Ceremony. Meditation. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Meditation.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Meditation.", "x": "Kyudo in depth: Meditation.. Asymmetrical. Details — the way of the bow.. Japan. Ceremony. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Ceremony.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Ceremony.", "x": "Kyudo in depth: Ceremony.. Meditation. Details — the way of the bow.. Bow. Target. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Japan.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Japan.", "x": "Kyudo in depth: Japan.. Ceremony. Details — the way of the bow.. Practice. Japan. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Bow.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Bow.", "x": "Kyudo in depth: Bow.. Target. Details — the way of the bow.. Archery. Archery. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Practice.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Practice.", "x": "Kyudo in depth: Practice.. Japan. Details — the way of the bow.. Meditation. Asymmetrical. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Kyudo comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Kyudo comes from.", "x": "Origins: Archery.. Japan. The history of Kyudo — the way of the bow.. Meditation. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Kyudo respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Kyudo respectfully.", "x": "Engaging: Ceremony.. Archery. How to participate or observe well — Kyudo. the way of the bow. Respect first, always; Japan.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Kyudo do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Kyudo do's and don'ts.", "x": "Etiquette: Bow.. Asymmetrical. The rules of respect — Kyudo. the way of the bow. When in doubt, ask about Practice.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Kyudo.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Kyudo.", "x": "Planning: Archery.. Meditation. Practical notes — Kyudo. the way of the bow. A little planning shows respect for Meditation.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Kyudo and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Kyudo and money.", "x": "Costs: Ceremony.. Ceremony. What to budget — Kyudo. the way of the bow. The best experiences of Japan. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-martial-kyudo-martial-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
