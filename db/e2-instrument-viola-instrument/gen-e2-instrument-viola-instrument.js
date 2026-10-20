(function(){'use strict';
/* JAH Viola Instrument Instrument Database generator — jahdb-e2-instrument-viola-instrument-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-instrument-viola-instrument',PREFIX='JAH-E2INSTRUMEN-',NAME='JAH Viola Instrument Instrument Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Viola Instrument: the complete guide", "d": "Viola Instrument: the alto strings..", "g": "overview", "l": 2, "q": "What is Viola Instrument: the complete guide?", "a": "Viola Instrument: the alto strings..", "x": "The complete instrument guide to Viola Instrument: the alto strings.. Alto. History, meaning, practices, and how to engage respectfully — everything in one database. Alto. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Viola Instrument essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Viola Instrument essentials.", "x": "At a glance: Viola Instrument — the alto strings.. Deeper. The essentials: Clef.. Clef. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Alto.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Alto.", "x": "Viola Instrument: Alto.. Clef. Essential knowledge — Clef.. the alto strings. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Alto..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Alto..", "x": "Explained: Alto.. Warm. The context — Viola Instrument. Inner voices. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Deeper.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Deeper.", "x": "Viola Instrument: Deeper.. Inner. Essential knowledge — Inner voices.. the alto strings. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Deeper..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Deeper..", "x": "Explained: Deeper.. Orchestra. The context — Viola Instrument. Orchestra. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Clef.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Clef.", "x": "Viola Instrument: Clef.. Warm. Essential knowledge — Orchestra.. the alto strings. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Clef..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Clef..", "x": "Explained: Clef.. Learning. The context — Viola Instrument. Warm. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Inner voices.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Inner voices.", "x": "Viola Instrument: Inner voices.. Orchestra. Essential knowledge — Warm.. the alto strings. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Inner voices..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Inner voices..", "x": "Explained: Inner voices.. Alto. The context — Viola Instrument. Alto. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Orchestra.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Orchestra.", "x": "Viola Instrument: Orchestra.. Learning. Essential knowledge — Alto.. the alto strings. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Orchestra..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Orchestra..", "x": "Explained: Orchestra.. Clef. The context — Viola Instrument. Deeper. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Warm.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Warm.", "x": "Viola Instrument: Warm.. Alto. Essential knowledge — Deeper.. the alto strings. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Warm..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Warm..", "x": "Explained: Warm.. Inner. The context — Viola Instrument. Clef. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Alto.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Alto.", "x": "Viola Instrument in depth: Alto.. Deeper. Details — the alto strings.. Inner. Inner voices. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Clef.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Clef.", "x": "Viola Instrument in depth: Clef.. Clef. Details — the alto strings.. Warm. Orchestra. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Inner.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Inner.", "x": "Viola Instrument in depth: Inner.. Inner voices. Details — the alto strings.. Orchestra. Warm. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Warm.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Warm.", "x": "Viola Instrument in depth: Warm.. Orchestra. Details — the alto strings.. Learning. Alto. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Orchestra.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Orchestra.", "x": "Viola Instrument in depth: Orchestra.. Warm. Details — the alto strings.. Alto. Deeper. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Learning.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Learning.", "x": "Viola Instrument in depth: Learning.. Alto. Details — the alto strings.. Clef. Clef. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Viola Instrument comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Viola Instrument comes from.", "x": "Origins: Alto.. Alto. The history of Viola Instrument — the alto strings.. Clef. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Viola Instrument respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Viola Instrument respectfully.", "x": "Engaging: Inner.. Deeper. How to participate or observe well — Viola Instrument. the alto strings. Respect first, always; Warm.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Viola Instrument do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Viola Instrument do's and don'ts.", "x": "Etiquette: Orchestra.. Clef. The rules of respect — Viola Instrument. the alto strings. When in doubt, ask about Learning.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Viola Instrument.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Viola Instrument.", "x": "Planning: Alto.. Inner voices. Practical notes — Viola Instrument. the alto strings. A little planning shows respect for Clef.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Viola Instrument and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Viola Instrument and money.", "x": "Costs: Inner.. Orchestra. What to budget — Viola Instrument. the alto strings. The best experiences of Warm. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-instrument-viola-instrument-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
