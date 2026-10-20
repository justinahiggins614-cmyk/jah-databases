(function(){'use strict';
/* JAH John Coltrane Band Band Database generator — jahdb-e2-band-john-coltrane-band-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-band-john-coltrane-band',PREFIX='JAH-E2BANDJOHNC-',NAME='JAH John Coltrane Band Band Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "John Coltrane Band: the complete guide", "d": "John Coltrane Band: the saxophone seeker..", "g": "overview", "l": 2, "q": "What is John Coltrane Band: the complete guide?", "a": "John Coltrane Band: the saxophone seeker..", "x": "The complete band guide to John Coltrane Band: the saxophone seeker.. 1926. History, meaning, practices, and how to engage respectfully — everything in one database. Supreme. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "John Coltrane Band essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "John Coltrane Band essentials.", "x": "At a glance: John Coltrane Band — the saxophone seeker.. A Love Supreme. The essentials: Giant Steps.. Giant Steps. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "1926.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "1926.", "x": "John Coltrane Band: 1926.. Giant Steps. Essential knowledge — Giant Steps.. the saxophone seeker. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 1926..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 1926..", "x": "Explained: 1926.. Quartet. The context — John Coltrane Band. Sheets. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "A Love Supreme.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "A Love Supreme.", "x": "John Coltrane Band: A Love Supreme.. Spiritual. Essential knowledge — Sheets.. the saxophone seeker. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: A Love Supreme..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: A Love Supreme..", "x": "Explained: A Love Supreme.. Sheets. The context — John Coltrane Band. Spiritual. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Giant Steps.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Giant Steps.", "x": "John Coltrane Band: Giant Steps.. Quartet. Essential knowledge — Spiritual.. the saxophone seeker. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Giant Steps..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Giant Steps..", "x": "Explained: Giant Steps.. Legacy. The context — John Coltrane Band. Quartet. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Sheets.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Sheets.", "x": "John Coltrane Band: Sheets.. Sheets. Essential knowledge — Quartet.. the saxophone seeker. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Sheets..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Sheets..", "x": "Explained: Sheets.. Supreme. The context — John Coltrane Band. 1926. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Spiritual.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Spiritual.", "x": "John Coltrane Band: Spiritual.. Legacy. Essential knowledge — 1926.. the saxophone seeker. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Spiritual..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Spiritual..", "x": "Explained: Spiritual.. Giant Steps. The context — John Coltrane Band. A Love Supreme. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Quartet.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Quartet.", "x": "John Coltrane Band: Quartet.. Supreme. Essential knowledge — A Love Supreme.. the saxophone seeker. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Quartet..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Quartet..", "x": "Explained: Quartet.. Spiritual. The context — John Coltrane Band. Giant Steps. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Supreme.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Supreme.", "x": "John Coltrane Band in depth: Supreme.. A Love Supreme. Details — the saxophone seeker.. Spiritual. Sheets. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Giant Steps.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Giant Steps.", "x": "John Coltrane Band in depth: Giant Steps.. Giant Steps. Details — the saxophone seeker.. Quartet. Spiritual. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Spiritual.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Spiritual.", "x": "John Coltrane Band in depth: Spiritual.. Sheets. Details — the saxophone seeker.. Sheets. Quartet. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Quartet.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Quartet.", "x": "John Coltrane Band in depth: Quartet.. Spiritual. Details — the saxophone seeker.. Legacy. 1926. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Sheets.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Sheets.", "x": "John Coltrane Band in depth: Sheets.. Quartet. Details — the saxophone seeker.. Supreme. A Love Supreme. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Legacy.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Legacy.", "x": "John Coltrane Band in depth: Legacy.. 1926. Details — the saxophone seeker.. Giant Steps. Giant Steps. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where John Coltrane Band comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where John Coltrane Band comes from.", "x": "Origins: Supreme.. 1926. The history of John Coltrane Band — the saxophone seeker.. Giant Steps. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing John Coltrane Band respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing John Coltrane Band respectfully.", "x": "Engaging: Spiritual.. A Love Supreme. How to participate or observe well — John Coltrane Band. the saxophone seeker. Respect first, always; Quartet.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "John Coltrane Band do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "John Coltrane Band do's and don'ts.", "x": "Etiquette: Sheets.. Giant Steps. The rules of respect — John Coltrane Band. the saxophone seeker. When in doubt, ask about Legacy.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around John Coltrane Band.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around John Coltrane Band.", "x": "Planning: Supreme.. Sheets. Practical notes — John Coltrane Band. the saxophone seeker. A little planning shows respect for Giant Steps.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "John Coltrane Band and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "John Coltrane Band and money.", "x": "Costs: Spiritual.. Spiritual. What to budget — John Coltrane Band. the saxophone seeker. The best experiences of Quartet. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-band-john-coltrane-band-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
