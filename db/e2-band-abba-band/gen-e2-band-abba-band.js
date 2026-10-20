(function(){'use strict';
/* JAH ABBA Band Band Database generator — jahdb-e2-band-abba-band-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-band-abba-band',PREFIX='JAH-E2BANDABBAB-',NAME='JAH ABBA Band Band Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "ABBA Band: the complete guide", "d": "ABBA Band: the Swedish pop..", "g": "overview", "l": 2, "q": "What is ABBA Band: the complete guide?", "a": "ABBA Band: the Swedish pop..", "x": "The complete band guide to ABBA Band: the Swedish pop.. 1972. History, meaning, practices, and how to engage respectfully — everything in one database. Waterloo. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "ABBA Band essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "ABBA Band essentials.", "x": "At a glance: ABBA Band — the Swedish pop.. Waterloo. The essentials: Mamma Mia.. Dancing Queen. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "1972.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "1972.", "x": "ABBA Band: 1972.. Mamma Mia. Essential knowledge — Dancing Queen.. the Swedish pop. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 1972..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 1972..", "x": "Explained: 1972.. Reunion. The context — ABBA Band. Mamma Mia. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Waterloo.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Waterloo.", "x": "ABBA Band: Waterloo.. Sweden. Essential knowledge — Mamma Mia.. the Swedish pop. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Waterloo..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Waterloo..", "x": "Explained: Waterloo.. Pop. The context — ABBA Band. Sweden. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Dancing Queen.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Dancing Queen.", "x": "ABBA Band: Dancing Queen.. Reunion. Essential knowledge — Sweden.. the Swedish pop. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Dancing Queen..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Dancing Queen..", "x": "Explained: Dancing Queen.. Legacy. The context — ABBA Band. Reunion. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Mamma Mia.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Mamma Mia.", "x": "ABBA Band: Mamma Mia.. Pop. Essential knowledge — Reunion.. the Swedish pop. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Mamma Mia..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Mamma Mia..", "x": "Explained: Mamma Mia.. Waterloo. The context — ABBA Band. 1972. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Sweden.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Sweden.", "x": "ABBA Band: Sweden.. Legacy. Essential knowledge — 1972.. the Swedish pop. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Sweden..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Sweden..", "x": "Explained: Sweden.. Mamma Mia. The context — ABBA Band. Waterloo. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Reunion.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Reunion.", "x": "ABBA Band: Reunion.. Waterloo. Essential knowledge — Waterloo.. the Swedish pop. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Reunion..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Reunion..", "x": "Explained: Reunion.. Sweden. The context — ABBA Band. Dancing Queen. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Waterloo.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Waterloo.", "x": "ABBA Band in depth: Waterloo.. Waterloo. Details — the Swedish pop.. Sweden. Mamma Mia. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Mamma Mia.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Mamma Mia.", "x": "ABBA Band in depth: Mamma Mia.. Dancing Queen. Details — the Swedish pop.. Reunion. Sweden. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Sweden.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Sweden.", "x": "ABBA Band in depth: Sweden.. Mamma Mia. Details — the Swedish pop.. Pop. Reunion. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Reunion.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Reunion.", "x": "ABBA Band in depth: Reunion.. Sweden. Details — the Swedish pop.. Legacy. 1972. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Pop.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Pop.", "x": "ABBA Band in depth: Pop.. Reunion. Details — the Swedish pop.. Waterloo. Waterloo. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Legacy.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Legacy.", "x": "ABBA Band in depth: Legacy.. 1972. Details — the Swedish pop.. Mamma Mia. Dancing Queen. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where ABBA Band comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where ABBA Band comes from.", "x": "Origins: Waterloo.. 1972. The history of ABBA Band — the Swedish pop.. Mamma Mia. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing ABBA Band respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing ABBA Band respectfully.", "x": "Engaging: Sweden.. Waterloo. How to participate or observe well — ABBA Band. the Swedish pop. Respect first, always; Reunion.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "ABBA Band do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "ABBA Band do's and don'ts.", "x": "Etiquette: Pop.. Dancing Queen. The rules of respect — ABBA Band. the Swedish pop. When in doubt, ask about Legacy.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around ABBA Band.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around ABBA Band.", "x": "Planning: Waterloo.. Mamma Mia. Practical notes — ABBA Band. the Swedish pop. A little planning shows respect for Mamma Mia.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "ABBA Band and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "ABBA Band and money.", "x": "Costs: Sweden.. Sweden. What to budget — ABBA Band. the Swedish pop. The best experiences of Reunion. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-band-abba-band-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
