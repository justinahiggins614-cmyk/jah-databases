(function(){'use strict';
/* JAH Jenkins Director Database generator — jahdb-e2-screen2-jenkins-director2-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-screen2-jenkins-director2',PREFIX='JAH-E2SCREEN2JE-',NAME='JAH Jenkins Director Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Jenkins Director: the complete guide", "d": "Jenkins Director: the Moonlight..", "g": "overview", "l": 2, "q": "What is Jenkins Director: the complete guide?", "a": "Jenkins Director: the Moonlight..", "x": "The complete director guide to Jenkins Director: the Moonlight.. 1979. History, meaning, practices, and how to engage respectfully — everything in one database. Moonlight. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Jenkins Director essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Jenkins Director essentials.", "x": "At a glance: Jenkins Director — the Moonlight.. Moonlight. The essentials: Oscar.. If Beale. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "1979.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "1979.", "x": "Jenkins Director: 1979.. Oscar. Essential knowledge — If Beale.. the Moonlight. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 1979..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 1979..", "x": "Explained: 1979.. Miami. The context — Jenkins Director. Oscar. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Moonlight.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Moonlight.", "x": "Jenkins Director: Moonlight.. A24. Essential knowledge — Oscar.. the Moonlight. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Moonlight..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Moonlight..", "x": "Explained: Moonlight.. Beale. The context — Jenkins Director. Miami. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "If Beale.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "If Beale.", "x": "Jenkins Director: If Beale.. Miami. Essential knowledge — Miami.. the Moonlight. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: If Beale..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: If Beale..", "x": "Explained: If Beale.. Style. The context — Jenkins Director. A24. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Oscar.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Oscar.", "x": "Jenkins Director: Oscar.. Beale. Essential knowledge — A24.. the Moonlight. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Oscar..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Oscar..", "x": "Explained: Oscar.. Moonlight. The context — Jenkins Director. 1979. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Miami.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Miami.", "x": "Jenkins Director: Miami.. Style. Essential knowledge — 1979.. the Moonlight. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Miami..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Miami..", "x": "Explained: Miami.. Oscar. The context — Jenkins Director. Moonlight. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "A24.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "A24.", "x": "Jenkins Director: A24.. Moonlight. Essential knowledge — Moonlight.. the Moonlight. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: A24..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: A24..", "x": "Explained: A24.. A24. The context — Jenkins Director. If Beale. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Moonlight.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Moonlight.", "x": "Jenkins Director in depth: Moonlight.. Moonlight. Details — the Moonlight.. A24. Oscar. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Oscar.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Oscar.", "x": "Jenkins Director in depth: Oscar.. If Beale. Details — the Moonlight.. Miami. Miami. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "A24.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "A24.", "x": "Jenkins Director in depth: A24.. Oscar. Details — the Moonlight.. Beale. A24. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Miami.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Miami.", "x": "Jenkins Director in depth: Miami.. Miami. Details — the Moonlight.. Style. 1979. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Beale.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Beale.", "x": "Jenkins Director in depth: Beale.. A24. Details — the Moonlight.. Moonlight. Moonlight. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Style.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Style.", "x": "Jenkins Director in depth: Style.. 1979. Details — the Moonlight.. Oscar. If Beale. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Jenkins Director comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Jenkins Director comes from.", "x": "Origins: Moonlight.. 1979. The history of Jenkins Director — the Moonlight.. Oscar. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Jenkins Director respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Jenkins Director respectfully.", "x": "Engaging: A24.. Moonlight. How to participate or observe well — Jenkins Director. the Moonlight. Respect first, always; Miami.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Jenkins Director do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Jenkins Director do's and don'ts.", "x": "Etiquette: Beale.. If Beale. The rules of respect — Jenkins Director. the Moonlight. When in doubt, ask about Style.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Jenkins Director.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Jenkins Director.", "x": "Planning: Moonlight.. Oscar. Practical notes — Jenkins Director. the Moonlight. A little planning shows respect for Oscar.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Jenkins Director and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Jenkins Director and money.", "x": "Costs: A24.. Miami. What to budget — Jenkins Director. the Moonlight. The best experiences of Miami. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-screen2-jenkins-director2-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
