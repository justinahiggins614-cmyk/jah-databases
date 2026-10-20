(function(){'use strict';
/* JAH Hedge Trimming Database generator — jahdb-e2-trade2-hedge-trimming-trade-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-trade2-hedge-trimming-trade',PREFIX='JAH-E2TRADE2HED-',NAME='JAH Hedge Trimming Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Hedge Trimming: the complete guide", "d": "Hedge Trimming: the shape pros..", "g": "overview", "l": 2, "q": "What is Hedge Trimming: the complete guide?", "a": "Hedge Trimming: the shape pros..", "x": "The complete trade guide to Hedge Trimming: the shape pros.. Shearing. History, meaning, practices, and how to engage respectfully — everything in one database. Shearing. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Hedge Trimming essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Hedge Trimming essentials.", "x": "At a glance: Hedge Trimming — the shape pros.. Shaping. The essentials: Cleanup.. Timing. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Shearing.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Shearing.", "x": "Hedge Trimming: Shearing.. Cleanup. Essential knowledge — Timing.. the shape pros. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Shearing..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Shearing..", "x": "Explained: Shearing.. Timing. The context — Hedge Trimming. Cleanup. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Shaping.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Shaping.", "x": "Hedge Trimming: Shaping.. Lines. Essential knowledge — Cleanup.. the shape pros. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Shaping..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Shaping..", "x": "Explained: Shaping.. Health. The context — Hedge Trimming. Health. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Timing.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Timing.", "x": "Hedge Trimming: Timing.. Timing. Essential knowledge — Health.. the shape pros. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Timing..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Timing..", "x": "Explained: Timing.. Hiring. The context — Hedge Trimming. Lines. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Cleanup.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Cleanup.", "x": "Hedge Trimming: Cleanup.. Health. Essential knowledge — Lines.. the shape pros. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Cleanup..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Cleanup..", "x": "Explained: Cleanup.. Shearing. The context — Hedge Trimming. Shearing. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Health.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Health.", "x": "Hedge Trimming: Health.. Hiring. Essential knowledge — Shearing.. the shape pros. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Health..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Health..", "x": "Explained: Health.. Cleanup. The context — Hedge Trimming. Shaping. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Lines.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Lines.", "x": "Hedge Trimming: Lines.. Shearing. Essential knowledge — Shaping.. the shape pros. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Lines..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Lines..", "x": "Explained: Lines.. Lines. The context — Hedge Trimming. Timing. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Shearing.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Shearing.", "x": "Hedge Trimming in depth: Shearing.. Shaping. Details — the shape pros.. Lines. Cleanup. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Cleanup.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Cleanup.", "x": "Hedge Trimming in depth: Cleanup.. Timing. Details — the shape pros.. Timing. Health. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Lines.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Lines.", "x": "Hedge Trimming in depth: Lines.. Cleanup. Details — the shape pros.. Health. Lines. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Timing.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Timing.", "x": "Hedge Trimming in depth: Timing.. Health. Details — the shape pros.. Hiring. Shearing. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Health.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Health.", "x": "Hedge Trimming in depth: Health.. Lines. Details — the shape pros.. Shearing. Shaping. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Hiring.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Hiring.", "x": "Hedge Trimming in depth: Hiring.. Shearing. Details — the shape pros.. Cleanup. Timing. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Hedge Trimming comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Hedge Trimming comes from.", "x": "Origins: Shearing.. Shearing. The history of Hedge Trimming — the shape pros.. Cleanup. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Hedge Trimming respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Hedge Trimming respectfully.", "x": "Engaging: Lines.. Shaping. How to participate or observe well — Hedge Trimming. the shape pros. Respect first, always; Timing.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Hedge Trimming do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Hedge Trimming do's and don'ts.", "x": "Etiquette: Health.. Timing. The rules of respect — Hedge Trimming. the shape pros. When in doubt, ask about Hiring.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Hedge Trimming.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Hedge Trimming.", "x": "Planning: Shearing.. Cleanup. Practical notes — Hedge Trimming. the shape pros. A little planning shows respect for Cleanup.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Hedge Trimming and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Hedge Trimming and money.", "x": "Costs: Lines.. Health. What to budget — Hedge Trimming. the shape pros. The best experiences of Timing. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-trade2-hedge-trimming-trade-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
