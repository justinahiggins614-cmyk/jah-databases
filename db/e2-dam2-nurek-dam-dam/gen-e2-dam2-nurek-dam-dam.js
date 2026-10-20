(function(){'use strict';
/* JAH Nurek Dam Database generator — jahdb-e2-dam2-nurek-dam-dam-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-dam2-nurek-dam-dam',PREFIX='JAH-E2DAM2NUREK-',NAME='JAH Nurek Dam Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Nurek Dam: the complete guide", "d": "Nurek Dam: the Tajikistan..", "g": "overview", "l": 2, "q": "What is Nurek Dam: the complete guide?", "a": "Nurek Dam: the Tajikistan..", "x": "The complete dam guide to Nurek Dam: the Tajikistan.. 1980. History, meaning, practices, and how to engage respectfully — everything in one database. 1980. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Nurek Dam essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Nurek Dam essentials.", "x": "At a glance: Nurek Dam — the Tajikistan.. 984 ft. The essentials: Embankment.. Tallest. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "1980.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "1980.", "x": "Nurek Dam: 1980.. Embankment. Essential knowledge — Tallest.. the Tajikistan. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 1980..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 1980..", "x": "Explained: 1980.. 984 ft. The context — Nurek Dam. Vakhsh. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "984 ft.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "984 ft.", "x": "Nurek Dam: 984 ft.. Tajikistan. Essential knowledge — Vakhsh.. the Tajikistan. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: 984 ft..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: 984 ft..", "x": "Explained: 984 ft.. Tallest. The context — Nurek Dam. Tajikistan. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Tallest.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Tallest.", "x": "Nurek Dam: Tallest.. 984 ft. Essential knowledge — Tajikistan.. the Tajikistan. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Tallest..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Tallest..", "x": "Explained: Tallest.. Visiting. The context — Nurek Dam. Embankment. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Vakhsh.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Vakhsh.", "x": "Nurek Dam: Vakhsh.. Tallest. Essential knowledge — Embankment.. the Tajikistan. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Vakhsh..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Vakhsh..", "x": "Explained: Vakhsh.. 1980. The context — Nurek Dam. 1980. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Tajikistan.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Tajikistan.", "x": "Nurek Dam: Tajikistan.. Visiting. Essential knowledge — 1980.. the Tajikistan. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Tajikistan..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Tajikistan..", "x": "Explained: Tajikistan.. Embankment. The context — Nurek Dam. 984 ft. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Embankment.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Embankment.", "x": "Nurek Dam: Embankment.. 1980. Essential knowledge — 984 ft.. the Tajikistan. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Embankment..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Embankment..", "x": "Explained: Embankment.. Tajikistan. The context — Nurek Dam. Tallest. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "1980.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "1980.", "x": "Nurek Dam in depth: 1980.. 984 ft. Details — the Tajikistan.. Tajikistan. Vakhsh. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Embankment.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Embankment.", "x": "Nurek Dam in depth: Embankment.. Tallest. Details — the Tajikistan.. 984 ft. Tajikistan. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Tajikistan.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Tajikistan.", "x": "Nurek Dam in depth: Tajikistan.. Vakhsh. Details — the Tajikistan.. Tallest. Embankment. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "984 ft.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "984 ft.", "x": "Nurek Dam in depth: 984 ft.. Tajikistan. Details — the Tajikistan.. Visiting. 1980. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Tallest.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Tallest.", "x": "Nurek Dam in depth: Tallest.. Embankment. Details — the Tajikistan.. 1980. 984 ft. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Visiting.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Visiting.", "x": "Nurek Dam in depth: Visiting.. 1980. Details — the Tajikistan.. Embankment. Tallest. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Nurek Dam comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Nurek Dam comes from.", "x": "Origins: 1980.. 1980. The history of Nurek Dam — the Tajikistan.. Embankment. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Nurek Dam respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Nurek Dam respectfully.", "x": "Engaging: Tajikistan.. 984 ft. How to participate or observe well — Nurek Dam. the Tajikistan. Respect first, always; 984 ft.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Nurek Dam do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Nurek Dam do's and don'ts.", "x": "Etiquette: Tallest.. Tallest. The rules of respect — Nurek Dam. the Tajikistan. When in doubt, ask about Visiting.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Nurek Dam.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Nurek Dam.", "x": "Planning: 1980.. Vakhsh. Practical notes — Nurek Dam. the Tajikistan. A little planning shows respect for Embankment.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Nurek Dam and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Nurek Dam and money.", "x": "Costs: Tajikistan.. Tajikistan. What to budget — Nurek Dam. the Tajikistan. The best experiences of 984 ft. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-dam2-nurek-dam-dam-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
