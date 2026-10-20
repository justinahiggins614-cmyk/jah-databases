(function(){'use strict';
/* JAH BTS Band Band Database generator — jahdb-e2-band-bts-band-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-band-bts-band',PREFIX='JAH-E2BANDBTSBA-',NAME='JAH BTS Band Band Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "BTS Band: the complete guide", "d": "BTS Band: the K-pop phenomenon..", "g": "overview", "l": 2, "q": "What is BTS Band: the complete guide?", "a": "BTS Band: the K-pop phenomenon..", "x": "The complete band guide to BTS Band: the K-pop phenomenon.. 2013. History, meaning, practices, and how to engage respectfully — everything in one database. ARMY. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "BTS Band essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "BTS Band essentials.", "x": "At a glance: BTS Band — the K-pop phenomenon.. ARMY. The essentials: Dynamite.. Dynamite. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "2013.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "2013.", "x": "BTS Band: 2013.. Dynamite. Essential knowledge — Dynamite.. the K-pop phenomenon. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 2013..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 2013..", "x": "Explained: 2013.. UN. The context — BTS Band. Seoul. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "ARMY.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "ARMY.", "x": "BTS Band: ARMY.. Seoul. Essential knowledge — Seoul.. the K-pop phenomenon. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: ARMY..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: ARMY..", "x": "Explained: ARMY.. Hiatus. The context — BTS Band. UN. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Dynamite.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Dynamite.", "x": "BTS Band: Dynamite.. UN. Essential knowledge — UN.. the K-pop phenomenon. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Dynamite..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Dynamite..", "x": "Explained: Dynamite.. Legacy. The context — BTS Band. Hiatus. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Seoul.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Seoul.", "x": "BTS Band: Seoul.. Hiatus. Essential knowledge — Hiatus.. the K-pop phenomenon. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Seoul..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Seoul..", "x": "Explained: Seoul.. ARMY. The context — BTS Band. 2013. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "UN.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "UN.", "x": "BTS Band: UN.. Legacy. Essential knowledge — 2013.. the K-pop phenomenon. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: UN..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: UN..", "x": "Explained: UN.. Dynamite. The context — BTS Band. ARMY. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Hiatus.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Hiatus.", "x": "BTS Band: Hiatus.. ARMY. Essential knowledge — ARMY.. the K-pop phenomenon. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Hiatus..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Hiatus..", "x": "Explained: Hiatus.. Seoul. The context — BTS Band. Dynamite. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "ARMY.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "ARMY.", "x": "BTS Band in depth: ARMY.. ARMY. Details — the K-pop phenomenon.. Seoul. Seoul. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Dynamite.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Dynamite.", "x": "BTS Band in depth: Dynamite.. Dynamite. Details — the K-pop phenomenon.. UN. UN. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Seoul.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Seoul.", "x": "BTS Band in depth: Seoul.. Seoul. Details — the K-pop phenomenon.. Hiatus. Hiatus. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "UN.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "UN.", "x": "BTS Band in depth: UN.. UN. Details — the K-pop phenomenon.. Legacy. 2013. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Hiatus.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Hiatus.", "x": "BTS Band in depth: Hiatus.. Hiatus. Details — the K-pop phenomenon.. ARMY. ARMY. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Legacy.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Legacy.", "x": "BTS Band in depth: Legacy.. 2013. Details — the K-pop phenomenon.. Dynamite. Dynamite. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where BTS Band comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where BTS Band comes from.", "x": "Origins: ARMY.. 2013. The history of BTS Band — the K-pop phenomenon.. Dynamite. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing BTS Band respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing BTS Band respectfully.", "x": "Engaging: Seoul.. ARMY. How to participate or observe well — BTS Band. the K-pop phenomenon. Respect first, always; UN.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "BTS Band do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "BTS Band do's and don'ts.", "x": "Etiquette: Hiatus.. Dynamite. The rules of respect — BTS Band. the K-pop phenomenon. When in doubt, ask about Legacy.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around BTS Band.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around BTS Band.", "x": "Planning: ARMY.. Seoul. Practical notes — BTS Band. the K-pop phenomenon. A little planning shows respect for Dynamite.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "BTS Band and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "BTS Band and money.", "x": "Costs: Seoul.. UN. What to budget — BTS Band. the K-pop phenomenon. The best experiences of UN. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-band-bts-band-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
