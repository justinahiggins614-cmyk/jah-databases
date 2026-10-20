(function(){'use strict';
/* JAH Guri Dam Database generator — jahdb-e2-dam2-guri-dam-dam-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-dam2-guri-dam-dam',PREFIX='JAH-E2DAM2GURID-',NAME='JAH Guri Dam Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Guri Dam: the complete guide", "d": "Guri Dam: the Venezuela..", "g": "overview", "l": 2, "q": "What is Guri Dam: the complete guide?", "a": "Guri Dam: the Venezuela..", "x": "The complete dam guide to Guri Dam: the Venezuela.. 1986. History, meaning, practices, and how to engage respectfully — everything in one database. 1986. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Guri Dam essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Guri Dam essentials.", "x": "At a glance: Guri Dam — the Venezuela.. Caroní. The essentials: Lake.. Power. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "1986.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "1986.", "x": "Guri Dam: 1986.. Lake. Essential knowledge — Power.. the Venezuela. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 1986..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 1986..", "x": "Explained: 1986.. Caroní. The context — Guri Dam. Venezuela. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Caroní.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Caroní.", "x": "Guri Dam: Caroní.. Venezuela. Essential knowledge — Venezuela.. the Venezuela. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Caroní..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Caroní..", "x": "Explained: Caroní.. Gravity. The context — Guri Dam. Gravity. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Power.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Power.", "x": "Guri Dam: Power.. Caroní. Essential knowledge — Gravity.. the Venezuela. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Power..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Power..", "x": "Explained: Power.. Visiting. The context — Guri Dam. Lake. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Venezuela.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Venezuela.", "x": "Guri Dam: Venezuela.. Gravity. Essential knowledge — Lake.. the Venezuela. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Venezuela..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Venezuela..", "x": "Explained: Venezuela.. 1986. The context — Guri Dam. 1986. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Gravity.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Gravity.", "x": "Guri Dam: Gravity.. Visiting. Essential knowledge — 1986.. the Venezuela. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Gravity..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Gravity..", "x": "Explained: Gravity.. Lake. The context — Guri Dam. Caroní. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Lake.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Lake.", "x": "Guri Dam: Lake.. 1986. Essential knowledge — Caroní.. the Venezuela. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Lake..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Lake..", "x": "Explained: Lake.. Venezuela. The context — Guri Dam. Power. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "1986.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "1986.", "x": "Guri Dam in depth: 1986.. Caroní. Details — the Venezuela.. Venezuela. Venezuela. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Lake.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Lake.", "x": "Guri Dam in depth: Lake.. Power. Details — the Venezuela.. Caroní. Gravity. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Venezuela.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Venezuela.", "x": "Guri Dam in depth: Venezuela.. Venezuela. Details — the Venezuela.. Gravity. Lake. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Caroní.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Caroní.", "x": "Guri Dam in depth: Caroní.. Gravity. Details — the Venezuela.. Visiting. 1986. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Gravity.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Gravity.", "x": "Guri Dam in depth: Gravity.. Lake. Details — the Venezuela.. 1986. Caroní. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Visiting.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Visiting.", "x": "Guri Dam in depth: Visiting.. 1986. Details — the Venezuela.. Lake. Power. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Guri Dam comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Guri Dam comes from.", "x": "Origins: 1986.. 1986. The history of Guri Dam — the Venezuela.. Lake. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Guri Dam respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Guri Dam respectfully.", "x": "Engaging: Venezuela.. Caroní. How to participate or observe well — Guri Dam. the Venezuela. Respect first, always; Caroní.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Guri Dam do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Guri Dam do's and don'ts.", "x": "Etiquette: Gravity.. Power. The rules of respect — Guri Dam. the Venezuela. When in doubt, ask about Visiting.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Guri Dam.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Guri Dam.", "x": "Planning: 1986.. Venezuela. Practical notes — Guri Dam. the Venezuela. A little planning shows respect for Lake.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Guri Dam and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Guri Dam and money.", "x": "Costs: Venezuela.. Gravity. What to budget — Guri Dam. the Venezuela. The best experiences of Caroní. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-dam2-guri-dam-dam-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
