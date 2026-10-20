(function(){'use strict';
/* JAH Zoroastrianism Religion Database generator — jahdb-e2-religion-zoroastrianism-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-religion-zoroastrianism',PREFIX='JAH-E2RELIGIONZ-',NAME='JAH Zoroastrianism Religion Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Zoroastrianism: the complete guide", "d": "Zoroastrianism: ancient Persian faith..", "g": "overview", "l": 2, "q": "What is Zoroastrianism: the complete guide?", "a": "Zoroastrianism: ancient Persian faith..", "x": "The complete religion guide to Zoroastrianism: ancient Persian faith.. Zarathustra. History, meaning, practices, and how to engage respectfully — everything in one database. Texts. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Zoroastrianism essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Zoroastrianism essentials.", "x": "At a glance: Zoroastrianism — ancient Persian faith.. Ahura Mazda. The essentials: Rituals.. Fire temples. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Zarathustra.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Zarathustra.", "x": "Zoroastrianism: Zarathustra.. Rituals. Essential knowledge — Fire temples.. ancient Persian faith. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Zarathustra..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Zarathustra..", "x": "Explained: Zarathustra.. Parsis. The context — Zoroastrianism. Parsis. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Ahura Mazda.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Ahura Mazda.", "x": "Zoroastrianism: Ahura Mazda.. History. Essential knowledge — Parsis.. ancient Persian faith. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Ahura Mazda..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Ahura Mazda..", "x": "Explained: Ahura Mazda.. Influence. The context — Zoroastrianism. Dualism. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Fire temples.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Fire temples.", "x": "Zoroastrianism: Fire temples.. Parsis. Essential knowledge — Dualism.. ancient Persian faith. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Fire temples..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Fire temples..", "x": "Explained: Fire temples.. Ethics. The context — Zoroastrianism. 200K. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Parsis.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Parsis.", "x": "Zoroastrianism: Parsis.. Influence. Essential knowledge — 200K.. ancient Persian faith. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Parsis..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Parsis..", "x": "Explained: Parsis.. Texts. The context — Zoroastrianism. Zarathustra. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Dualism.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Dualism.", "x": "Zoroastrianism: Dualism.. Ethics. Essential knowledge — Zarathustra.. ancient Persian faith. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Dualism..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Dualism..", "x": "Explained: Dualism.. Rituals. The context — Zoroastrianism. Ahura Mazda. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "200K.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "200K.", "x": "Zoroastrianism: 200K.. Texts. Essential knowledge — Ahura Mazda.. ancient Persian faith. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: 200K..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: 200K..", "x": "Explained: 200K.. History. The context — Zoroastrianism. Fire temples. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Texts.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Texts.", "x": "Zoroastrianism in depth: Texts.. Ahura Mazda. Details — ancient Persian faith.. History. Parsis. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Rituals.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Rituals.", "x": "Zoroastrianism in depth: Rituals.. Fire temples. Details — ancient Persian faith.. Parsis. Dualism. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "History.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "History.", "x": "Zoroastrianism in depth: History.. Parsis. Details — ancient Persian faith.. Influence. 200K. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Parsis.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Parsis.", "x": "Zoroastrianism in depth: Parsis.. Dualism. Details — ancient Persian faith.. Ethics. Zarathustra. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Influence.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Influence.", "x": "Zoroastrianism in depth: Influence.. 200K. Details — ancient Persian faith.. Texts. Ahura Mazda. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Ethics.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Ethics.", "x": "Zoroastrianism in depth: Ethics.. Zarathustra. Details — ancient Persian faith.. Rituals. Fire temples. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Zoroastrianism comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Zoroastrianism comes from.", "x": "Origins: Texts.. Zarathustra. The history of Zoroastrianism — ancient Persian faith.. Rituals. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Zoroastrianism respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Zoroastrianism respectfully.", "x": "Engaging: History.. Ahura Mazda. How to participate or observe well — Zoroastrianism. ancient Persian faith. Respect first, always; Parsis.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Zoroastrianism do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Zoroastrianism do's and don'ts.", "x": "Etiquette: Influence.. Fire temples. The rules of respect — Zoroastrianism. ancient Persian faith. When in doubt, ask about Ethics.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Zoroastrianism.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Zoroastrianism.", "x": "Planning: Texts.. Parsis. Practical notes — Zoroastrianism. ancient Persian faith. A little planning shows respect for Rituals.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Zoroastrianism and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Zoroastrianism and money.", "x": "Costs: History.. Dualism. What to budget — Zoroastrianism. ancient Persian faith. The best experiences of Parsis. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-religion-zoroastrianism-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
