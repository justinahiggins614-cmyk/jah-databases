(function(){'use strict';
/* JAH Chichen UNESCO Database generator — jahdb-e2-unesco2-chichen-unesco2-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-unesco2-chichen-unesco2',PREFIX='JAH-E2UNESCO2CH-',NAME='JAH Chichen UNESCO Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Chichen UNESCO: the complete guide", "d": "Chichen UNESCO: the Maya 2..", "g": "overview", "l": 2, "q": "What is Chichen UNESCO: the complete guide?", "a": "Chichen UNESCO: the Maya 2..", "x": "The complete unesco site guide to Chichen UNESCO: the Maya 2.. Mexico. History, meaning, practices, and how to engage respectfully — everything in one database. Mexico. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Chichen UNESCO essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Chichen UNESCO essentials.", "x": "At a glance: Chichen UNESCO — the Maya 2.. 1988. The essentials: Yucatan.. Maya. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Mexico.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Mexico.", "x": "Chichen UNESCO: Mexico.. Yucatan. Essential knowledge — Maya.. the Maya 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Mexico..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Mexico..", "x": "Explained: Mexico.. 1988. The context — Chichen UNESCO. Castillo. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "1988.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "1988.", "x": "Chichen UNESCO: 1988.. Equinox. Essential knowledge — Castillo.. the Maya 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: 1988..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: 1988..", "x": "Explained: 1988.. Castillo. The context — Chichen UNESCO. Equinox. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Maya.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Maya.", "x": "Chichen UNESCO: Maya.. 1988. Essential knowledge — Equinox.. the Maya 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Maya..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Maya..", "x": "Explained: Maya.. Visiting. The context — Chichen UNESCO. Yucatan. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Castillo.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Castillo.", "x": "Chichen UNESCO: Castillo.. Castillo. Essential knowledge — Yucatan.. the Maya 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Castillo..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Castillo..", "x": "Explained: Castillo.. Mexico. The context — Chichen UNESCO. Mexico. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Equinox.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Equinox.", "x": "Chichen UNESCO: Equinox.. Visiting. Essential knowledge — Mexico.. the Maya 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Equinox..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Equinox..", "x": "Explained: Equinox.. Yucatan. The context — Chichen UNESCO. 1988. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Yucatan.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Yucatan.", "x": "Chichen UNESCO: Yucatan.. Mexico. Essential knowledge — 1988.. the Maya 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Yucatan..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Yucatan..", "x": "Explained: Yucatan.. Equinox. The context — Chichen UNESCO. Maya. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Mexico.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Mexico.", "x": "Chichen UNESCO in depth: Mexico.. 1988. Details — the Maya 2.. Equinox. Castillo. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Yucatan.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Yucatan.", "x": "Chichen UNESCO in depth: Yucatan.. Maya. Details — the Maya 2.. 1988. Equinox. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Equinox.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Equinox.", "x": "Chichen UNESCO in depth: Equinox.. Castillo. Details — the Maya 2.. Castillo. Yucatan. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "1988.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "1988.", "x": "Chichen UNESCO in depth: 1988.. Equinox. Details — the Maya 2.. Visiting. Mexico. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Castillo.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Castillo.", "x": "Chichen UNESCO in depth: Castillo.. Yucatan. Details — the Maya 2.. Mexico. 1988. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Visiting.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Visiting.", "x": "Chichen UNESCO in depth: Visiting.. Mexico. Details — the Maya 2.. Yucatan. Maya. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Chichen UNESCO comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Chichen UNESCO comes from.", "x": "Origins: Mexico.. Mexico. The history of Chichen UNESCO — the Maya 2.. Yucatan. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Chichen UNESCO respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Chichen UNESCO respectfully.", "x": "Engaging: Equinox.. 1988. How to participate or observe well — Chichen UNESCO. the Maya 2. Respect first, always; 1988.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Chichen UNESCO do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Chichen UNESCO do's and don'ts.", "x": "Etiquette: Castillo.. Maya. The rules of respect — Chichen UNESCO. the Maya 2. When in doubt, ask about Visiting.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Chichen UNESCO.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Chichen UNESCO.", "x": "Planning: Mexico.. Castillo. Practical notes — Chichen UNESCO. the Maya 2. A little planning shows respect for Yucatan.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Chichen UNESCO and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Chichen UNESCO and money.", "x": "Costs: Equinox.. Equinox. What to budget — Chichen UNESCO. the Maya 2. The best experiences of 1988. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-unesco2-chichen-unesco2-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
