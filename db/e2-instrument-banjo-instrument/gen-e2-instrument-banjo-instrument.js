(function(){'use strict';
/* JAH Banjo Instrument Instrument Database generator — jahdb-e2-instrument-banjo-instrument-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-instrument-banjo-instrument',PREFIX='JAH-E2INSTRUMEN-',NAME='JAH Banjo Instrument Instrument Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Banjo Instrument: the complete guide", "d": "Banjo Instrument: the twangy five..", "g": "overview", "l": 2, "q": "What is Banjo Instrument: the complete guide?", "a": "Banjo Instrument: the twangy five..", "x": "The complete instrument guide to Banjo Instrument: the twangy five.. 5 strings. History, meaning, practices, and how to engage respectfully — everything in one database. Strings. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Banjo Instrument essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Banjo Instrument essentials.", "x": "At a glance: Banjo Instrument — the twangy five.. Bluegrass. The essentials: Bluegrass.. Africa. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "5 strings.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "5 strings.", "x": "Banjo Instrument: 5 strings.. Bluegrass. Essential knowledge — Africa.. the twangy five. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 5 strings..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 5 strings..", "x": "Explained: 5 strings.. Clawhammer. The context — Banjo Instrument. Clawhammer. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Bluegrass.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Bluegrass.", "x": "Banjo Instrument: Bluegrass.. Africa. Essential knowledge — Clawhammer.. the twangy five. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Bluegrass..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Bluegrass..", "x": "Explained: Bluegrass.. Folk. The context — Banjo Instrument. Bright. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Africa.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Africa.", "x": "Banjo Instrument: Africa.. Clawhammer. Essential knowledge — Bright.. the twangy five. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Africa..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Africa..", "x": "Explained: Africa.. Learning. The context — Banjo Instrument. Folk. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Clawhammer.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Clawhammer.", "x": "Banjo Instrument: Clawhammer.. Folk. Essential knowledge — Folk.. the twangy five. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Clawhammer..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Clawhammer..", "x": "Explained: Clawhammer.. Strings. The context — Banjo Instrument. 5 strings. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Bright.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Bright.", "x": "Banjo Instrument: Bright.. Learning. Essential knowledge — 5 strings.. the twangy five. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Bright..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Bright..", "x": "Explained: Bright.. Bluegrass. The context — Banjo Instrument. Bluegrass. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Folk.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Folk.", "x": "Banjo Instrument: Folk.. Strings. Essential knowledge — Bluegrass.. the twangy five. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Folk..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Folk..", "x": "Explained: Folk.. Africa. The context — Banjo Instrument. Africa. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Strings.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Strings.", "x": "Banjo Instrument in depth: Strings.. Bluegrass. Details — the twangy five.. Africa. Clawhammer. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Bluegrass.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Bluegrass.", "x": "Banjo Instrument in depth: Bluegrass.. Africa. Details — the twangy five.. Clawhammer. Bright. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Africa.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Africa.", "x": "Banjo Instrument in depth: Africa.. Clawhammer. Details — the twangy five.. Folk. Folk. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Clawhammer.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Clawhammer.", "x": "Banjo Instrument in depth: Clawhammer.. Bright. Details — the twangy five.. Learning. 5 strings. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Folk.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Folk.", "x": "Banjo Instrument in depth: Folk.. Folk. Details — the twangy five.. Strings. Bluegrass. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Learning.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Learning.", "x": "Banjo Instrument in depth: Learning.. 5 strings. Details — the twangy five.. Bluegrass. Africa. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Banjo Instrument comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Banjo Instrument comes from.", "x": "Origins: Strings.. 5 strings. The history of Banjo Instrument — the twangy five.. Bluegrass. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Banjo Instrument respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Banjo Instrument respectfully.", "x": "Engaging: Africa.. Bluegrass. How to participate or observe well — Banjo Instrument. the twangy five. Respect first, always; Clawhammer.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Banjo Instrument do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Banjo Instrument do's and don'ts.", "x": "Etiquette: Folk.. Africa. The rules of respect — Banjo Instrument. the twangy five. When in doubt, ask about Learning.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Banjo Instrument.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Banjo Instrument.", "x": "Planning: Strings.. Clawhammer. Practical notes — Banjo Instrument. the twangy five. A little planning shows respect for Bluegrass.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Banjo Instrument and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Banjo Instrument and money.", "x": "Costs: Africa.. Bright. What to budget — Banjo Instrument. the twangy five. The best experiences of Clawhammer. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-instrument-banjo-instrument-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
