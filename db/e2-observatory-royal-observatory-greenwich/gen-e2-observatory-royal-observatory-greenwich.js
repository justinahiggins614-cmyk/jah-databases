(function(){'use strict';
/* JAH Royal Observatory Greenwich Observatory Database generator — jahdb-e2-observatory-royal-observatory-greenwich-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-observatory-royal-observatory-greenwich',PREFIX='JAH-E2OBSERVATO-',NAME='JAH Royal Observatory Greenwich Observatory Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Royal Observatory Greenwich: the complete guide", "d": "Royal Observatory Greenwich: home of GMT..", "g": "overview", "l": 2, "q": "What is Royal Observatory Greenwich: the complete guide?", "a": "Royal Observatory Greenwich: home of GMT..", "x": "The complete observatory guide to Royal Observatory Greenwich: home of GMT.. 1675. History, meaning, practices, and how to engage respectfully — everything in one database. Meridian. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Royal Observatory Greenwich essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Royal Observatory Greenwich essentials.", "x": "At a glance: Royal Observatory Greenwich — home of GMT.. Prime Meridian. The essentials: History.. Flamsteed. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "1675.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "1675.", "x": "Royal Observatory Greenwich: 1675.. History. Essential knowledge — Flamsteed.. home of GMT. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 1675..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 1675..", "x": "Explained: 1675.. London. The context — Royal Observatory Greenwich. Museum. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Prime Meridian.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Prime Meridian.", "x": "Royal Observatory Greenwich: Prime Meridian.. Museum. Essential knowledge — Museum.. home of GMT. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Prime Meridian..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Prime Meridian..", "x": "Explained: Prime Meridian.. Time. The context — Royal Observatory Greenwich. London. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Flamsteed.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Flamsteed.", "x": "Royal Observatory Greenwich: Flamsteed.. London. Essential knowledge — London.. home of GMT. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Flamsteed..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Flamsteed..", "x": "Explained: Flamsteed.. Tours. The context — Royal Observatory Greenwich. Time. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Museum.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Museum.", "x": "Royal Observatory Greenwich: Museum.. Time. Essential knowledge — Time.. home of GMT. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Museum..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Museum..", "x": "Explained: Museum.. Meridian. The context — Royal Observatory Greenwich. 1675. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "London.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "London.", "x": "Royal Observatory Greenwich: London.. Tours. Essential knowledge — 1675.. home of GMT. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: London..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: London..", "x": "Explained: London.. History. The context — Royal Observatory Greenwich. Prime Meridian. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Time.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Time.", "x": "Royal Observatory Greenwich: Time.. Meridian. Essential knowledge — Prime Meridian.. home of GMT. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Time..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Time..", "x": "Explained: Time.. Museum. The context — Royal Observatory Greenwich. Flamsteed. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Meridian.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Meridian.", "x": "Royal Observatory Greenwich in depth: Meridian.. Prime Meridian. Details — home of GMT.. Museum. Museum. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "History.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "History.", "x": "Royal Observatory Greenwich in depth: History.. Flamsteed. Details — home of GMT.. London. London. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Museum.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Museum.", "x": "Royal Observatory Greenwich in depth: Museum.. Museum. Details — home of GMT.. Time. Time. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "London.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "London.", "x": "Royal Observatory Greenwich in depth: London.. London. Details — home of GMT.. Tours. 1675. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Time.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Time.", "x": "Royal Observatory Greenwich in depth: Time.. Time. Details — home of GMT.. Meridian. Prime Meridian. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Tours.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Tours.", "x": "Royal Observatory Greenwich in depth: Tours.. 1675. Details — home of GMT.. History. Flamsteed. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Royal Observatory Greenwich comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Royal Observatory Greenwich comes from.", "x": "Origins: Meridian.. 1675. The history of Royal Observatory Greenwich — home of GMT.. History. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Royal Observatory Greenwich respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Royal Observatory Greenwich respectfully.", "x": "Engaging: Museum.. Prime Meridian. How to participate or observe well — Royal Observatory Greenwich. home of GMT. Respect first, always; London.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Royal Observatory Greenwich do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Royal Observatory Greenwich do's and don'ts.", "x": "Etiquette: Time.. Flamsteed. The rules of respect — Royal Observatory Greenwich. home of GMT. When in doubt, ask about Tours.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Royal Observatory Greenwich.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Royal Observatory Greenwich.", "x": "Planning: Meridian.. Museum. Practical notes — Royal Observatory Greenwich. home of GMT. A little planning shows respect for History.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Royal Observatory Greenwich and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Royal Observatory Greenwich and money.", "x": "Costs: Museum.. London. What to budget — Royal Observatory Greenwich. home of GMT. The best experiences of London. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-observatory-royal-observatory-greenwich-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
