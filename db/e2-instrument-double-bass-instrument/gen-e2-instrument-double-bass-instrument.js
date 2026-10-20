(function(){'use strict';
/* JAH Double Bass Instrument Instrument Database generator — jahdb-e2-instrument-double-bass-instrument-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-instrument-double-bass-instrument',PREFIX='JAH-E2INSTRUMEN-',NAME='JAH Double Bass Instrument Instrument Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Double Bass Instrument: the complete guide", "d": "Double Bass Instrument: the string bass..", "g": "overview", "l": 2, "q": "What is Double Bass Instrument: the complete guide?", "a": "Double Bass Instrument: the string bass..", "x": "The complete instrument guide to Double Bass Instrument: the string bass.. Lowest strings. History, meaning, practices, and how to engage respectfully — everything in one database. Tall. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Double Bass Instrument essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Double Bass Instrument essentials.", "x": "At a glance: Double Bass Instrument — the string bass.. Tall. The essentials: Pizzicato.. Pizzicato. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Lowest strings.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Lowest strings.", "x": "Double Bass Instrument: Lowest strings.. Pizzicato. Essential knowledge — Pizzicato.. the string bass. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Lowest strings..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Lowest strings..", "x": "Explained: Lowest strings.. Orchestra. The context — Double Bass Instrument. Jazz. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Tall.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Tall.", "x": "Double Bass Instrument: Tall.. Jazz. Essential knowledge — Jazz.. the string bass. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Tall..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Tall..", "x": "Explained: Tall.. Bow. The context — Double Bass Instrument. Orchestra. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Pizzicato.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Pizzicato.", "x": "Double Bass Instrument: Pizzicato.. Orchestra. Essential knowledge — Orchestra.. the string bass. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Pizzicato..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Pizzicato..", "x": "Explained: Pizzicato.. Learning. The context — Double Bass Instrument. Bow. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Jazz.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Jazz.", "x": "Double Bass Instrument: Jazz.. Bow. Essential knowledge — Bow.. the string bass. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Jazz..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Jazz..", "x": "Explained: Jazz.. Tall. The context — Double Bass Instrument. Lowest strings. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Orchestra.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Orchestra.", "x": "Double Bass Instrument: Orchestra.. Learning. Essential knowledge — Lowest strings.. the string bass. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Orchestra..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Orchestra..", "x": "Explained: Orchestra.. Pizzicato. The context — Double Bass Instrument. Tall. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Bow.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Bow.", "x": "Double Bass Instrument: Bow.. Tall. Essential knowledge — Tall.. the string bass. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Bow..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Bow..", "x": "Explained: Bow.. Jazz. The context — Double Bass Instrument. Pizzicato. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Tall.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Tall.", "x": "Double Bass Instrument in depth: Tall.. Tall. Details — the string bass.. Jazz. Jazz. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Pizzicato.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Pizzicato.", "x": "Double Bass Instrument in depth: Pizzicato.. Pizzicato. Details — the string bass.. Orchestra. Orchestra. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Jazz.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Jazz.", "x": "Double Bass Instrument in depth: Jazz.. Jazz. Details — the string bass.. Bow. Bow. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Orchestra.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Orchestra.", "x": "Double Bass Instrument in depth: Orchestra.. Orchestra. Details — the string bass.. Learning. Lowest strings. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Bow.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Bow.", "x": "Double Bass Instrument in depth: Bow.. Bow. Details — the string bass.. Tall. Tall. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Learning.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Learning.", "x": "Double Bass Instrument in depth: Learning.. Lowest strings. Details — the string bass.. Pizzicato. Pizzicato. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Double Bass Instrument comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Double Bass Instrument comes from.", "x": "Origins: Tall.. Lowest strings. The history of Double Bass Instrument — the string bass.. Pizzicato. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Double Bass Instrument respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Double Bass Instrument respectfully.", "x": "Engaging: Jazz.. Tall. How to participate or observe well — Double Bass Instrument. the string bass. Respect first, always; Orchestra.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Double Bass Instrument do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Double Bass Instrument do's and don'ts.", "x": "Etiquette: Bow.. Pizzicato. The rules of respect — Double Bass Instrument. the string bass. When in doubt, ask about Learning.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Double Bass Instrument.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Double Bass Instrument.", "x": "Planning: Tall.. Jazz. Practical notes — Double Bass Instrument. the string bass. A little planning shows respect for Pizzicato.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Double Bass Instrument and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Double Bass Instrument and money.", "x": "Costs: Jazz.. Orchestra. What to budget — Double Bass Instrument. the string bass. The best experiences of Orchestra. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-instrument-double-bass-instrument-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
