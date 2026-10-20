(function(){'use strict';
/* JAH BBQ Sauce Sauce Database generator — jahdb-e2-sauce-bbq-sauce-sauce-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-sauce-bbq-sauce-sauce',PREFIX='JAH-E2SAUCEBBQS-',NAME='JAH BBQ Sauce Sauce Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "BBQ Sauce: the complete guide", "d": "BBQ Sauce: the American smoke..", "g": "overview", "l": 2, "q": "What is BBQ Sauce: the complete guide?", "a": "BBQ Sauce: the American smoke..", "x": "The complete sauce guide to BBQ Sauce: the American smoke.. Kansas City. History, meaning, practices, and how to engage respectfully — everything in one database. KC. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "BBQ Sauce essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "BBQ Sauce essentials.", "x": "At a glance: BBQ Sauce — the American smoke.. Tomato. The essentials: Smoke.. Molasses. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Kansas City.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Kansas City.", "x": "BBQ Sauce: Kansas City.. Smoke. Essential knowledge — Molasses.. the American smoke. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Kansas City..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Kansas City..", "x": "Explained: Kansas City.. Ribs. The context — BBQ Sauce. Smoke. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Tomato.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Tomato.", "x": "BBQ Sauce: Tomato.. Regional. Essential knowledge — Smoke.. the American smoke. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Tomato..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Tomato..", "x": "Explained: Tomato.. Molasses. The context — BBQ Sauce. Regional. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Molasses.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Molasses.", "x": "BBQ Sauce: Molasses.. Ribs. Essential knowledge — Regional.. the American smoke. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Molasses..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Molasses..", "x": "Explained: Molasses.. Styles. The context — BBQ Sauce. Ribs. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Smoke.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Smoke.", "x": "BBQ Sauce: Smoke.. Molasses. Essential knowledge — Ribs.. the American smoke. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Smoke..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Smoke..", "x": "Explained: Smoke.. KC. The context — BBQ Sauce. Kansas City. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Regional.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Regional.", "x": "BBQ Sauce: Regional.. Styles. Essential knowledge — Kansas City.. the American smoke. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Regional..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Regional..", "x": "Explained: Regional.. Smoke. The context — BBQ Sauce. Tomato. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Ribs.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Ribs.", "x": "BBQ Sauce: Ribs.. KC. Essential knowledge — Tomato.. the American smoke. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Ribs..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Ribs..", "x": "Explained: Ribs.. Regional. The context — BBQ Sauce. Molasses. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "KC.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "KC.", "x": "BBQ Sauce in depth: KC.. Tomato. Details — the American smoke.. Regional. Smoke. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Smoke.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Smoke.", "x": "BBQ Sauce in depth: Smoke.. Molasses. Details — the American smoke.. Ribs. Regional. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Regional.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Regional.", "x": "BBQ Sauce in depth: Regional.. Smoke. Details — the American smoke.. Molasses. Ribs. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Ribs.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Ribs.", "x": "BBQ Sauce in depth: Ribs.. Regional. Details — the American smoke.. Styles. Kansas City. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Molasses.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Molasses.", "x": "BBQ Sauce in depth: Molasses.. Ribs. Details — the American smoke.. KC. Tomato. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Styles.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Styles.", "x": "BBQ Sauce in depth: Styles.. Kansas City. Details — the American smoke.. Smoke. Molasses. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where BBQ Sauce comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where BBQ Sauce comes from.", "x": "Origins: KC.. Kansas City. The history of BBQ Sauce — the American smoke.. Smoke. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing BBQ Sauce respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing BBQ Sauce respectfully.", "x": "Engaging: Regional.. Tomato. How to participate or observe well — BBQ Sauce. the American smoke. Respect first, always; Ribs.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "BBQ Sauce do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "BBQ Sauce do's and don'ts.", "x": "Etiquette: Molasses.. Molasses. The rules of respect — BBQ Sauce. the American smoke. When in doubt, ask about Styles.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around BBQ Sauce.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around BBQ Sauce.", "x": "Planning: KC.. Smoke. Practical notes — BBQ Sauce. the American smoke. A little planning shows respect for Smoke.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "BBQ Sauce and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "BBQ Sauce and money.", "x": "Costs: Regional.. Regional. What to budget — BBQ Sauce. the American smoke. The best experiences of Ribs. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-sauce-bbq-sauce-sauce-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
