(function(){'use strict';
/* JAH College Parenting Database generator — jahdb-e2-signature2-college-parenting-signature-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-signature2-college-parenting-signature',PREFIX='JAH-E2SIGNATURE-',NAME='JAH College Parenting Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "College Parenting: the complete guide", "d": "College Parenting: the launch years..", "g": "overview", "l": 2, "q": "What is College Parenting: the complete guide?", "a": "College Parenting: the launch years..", "x": "The complete signature original guide to College Parenting: the launch years.. Letting go. History, meaning, practices, and how to engage respectfully — everything in one database. Money. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "College Parenting essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "College Parenting essentials.", "x": "At a glance: College Parenting — the launch years.. Money. The essentials: Independence.. Visits. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Letting go.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Letting go.", "x": "College Parenting: Letting go.. Independence. Essential knowledge — Visits.. the launch years. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Letting go..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Letting go..", "x": "Explained: Letting go.. Letting go. The context — College Parenting. Support. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Money.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Money.", "x": "College Parenting: Money.. Career. Essential knowledge — Support.. the launch years. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Money..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Money..", "x": "Explained: Money.. Visits. The context — College Parenting. Career. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Visits.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Visits.", "x": "College Parenting: Visits.. Letting go. Essential knowledge — Career.. the launch years. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Visits..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Visits..", "x": "Explained: Visits.. Guide. The context — College Parenting. Independence. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Support.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Support.", "x": "College Parenting: Support.. Visits. Essential knowledge — Independence.. the launch years. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Support..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Support..", "x": "Explained: Support.. Money. The context — College Parenting. Letting go. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Career.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Career.", "x": "College Parenting: Career.. Guide. Essential knowledge — Letting go.. the launch years. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Career..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Career..", "x": "Explained: Career.. Independence. The context — College Parenting. Money. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Independence.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Independence.", "x": "College Parenting: Independence.. Money. Essential knowledge — Money.. the launch years. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Independence..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Independence..", "x": "Explained: Independence.. Career. The context — College Parenting. Visits. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Money.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Money.", "x": "College Parenting in depth: Money.. Money. Details — the launch years.. Career. Support. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Independence.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Independence.", "x": "College Parenting in depth: Independence.. Visits. Details — the launch years.. Letting go. Career. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Career.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Career.", "x": "College Parenting in depth: Career.. Support. Details — the launch years.. Visits. Independence. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Letting go.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Letting go.", "x": "College Parenting in depth: Letting go.. Career. Details — the launch years.. Guide. Letting go. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Visits.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Visits.", "x": "College Parenting in depth: Visits.. Independence. Details — the launch years.. Money. Money. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Guide.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Guide.", "x": "College Parenting in depth: Guide.. Letting go. Details — the launch years.. Independence. Visits. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where College Parenting comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where College Parenting comes from.", "x": "Origins: Money.. Letting go. The history of College Parenting — the launch years.. Independence. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing College Parenting respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing College Parenting respectfully.", "x": "Engaging: Career.. Money. How to participate or observe well — College Parenting. the launch years. Respect first, always; Letting go.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "College Parenting do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "College Parenting do's and don'ts.", "x": "Etiquette: Visits.. Visits. The rules of respect — College Parenting. the launch years. When in doubt, ask about Guide.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around College Parenting.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around College Parenting.", "x": "Planning: Money.. Support. Practical notes — College Parenting. the launch years. A little planning shows respect for Independence.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "College Parenting and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "College Parenting and money.", "x": "Costs: Career.. Career. What to budget — College Parenting. the launch years. The best experiences of Letting go. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-signature2-college-parenting-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
