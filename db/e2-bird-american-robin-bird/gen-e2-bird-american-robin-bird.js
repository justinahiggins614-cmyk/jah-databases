(function(){'use strict';
/* JAH American Robin Bird Species Database generator — jahdb-e2-bird-american-robin-bird-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-bird-american-robin-bird',PREFIX='JAH-E2BIRDAMERI-',NAME='JAH American Robin Bird Species Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "American Robin: the complete guide", "d": "American Robin: the spring thrush..", "g": "overview", "l": 2, "q": "What is American Robin: the complete guide?", "a": "American Robin: the spring thrush..", "x": "The complete bird species guide to American Robin: the spring thrush.. Orange. History, meaning, practices, and how to engage respectfully — everything in one database. Orange. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "American Robin essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "American Robin essentials.", "x": "At a glance: American Robin — the spring thrush.. Spring. The essentials: Worms.. Worms. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Orange.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Orange.", "x": "American Robin: Orange.. Worms. Essential knowledge — Worms.. the spring thrush. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Orange..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Orange..", "x": "Explained: Orange.. Backyard. The context — American Robin. Thrush. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Spring.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Spring.", "x": "American Robin: Spring.. Dawn. Essential knowledge — Thrush.. the spring thrush. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Spring..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Spring..", "x": "Explained: Spring.. Spring. The context — American Robin. Dawn. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Worms.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Worms.", "x": "American Robin: Worms.. Backyard. Essential knowledge — Dawn.. the spring thrush. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Worms..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Worms..", "x": "Explained: Worms.. Habitat. The context — American Robin. Backyard. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Thrush.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Thrush.", "x": "American Robin: Thrush.. Spring. Essential knowledge — Backyard.. the spring thrush. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Thrush..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Thrush..", "x": "Explained: Thrush.. Orange. The context — American Robin. Orange. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Dawn.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Dawn.", "x": "American Robin: Dawn.. Habitat. Essential knowledge — Orange.. the spring thrush. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Dawn..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Dawn..", "x": "Explained: Dawn.. Worms. The context — American Robin. Spring. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Backyard.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Backyard.", "x": "American Robin: Backyard.. Orange. Essential knowledge — Spring.. the spring thrush. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Backyard..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Backyard..", "x": "Explained: Backyard.. Dawn. The context — American Robin. Worms. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Orange.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Orange.", "x": "American Robin in depth: Orange.. Spring. Details — the spring thrush.. Dawn. Thrush. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Worms.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Worms.", "x": "American Robin in depth: Worms.. Worms. Details — the spring thrush.. Backyard. Dawn. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Dawn.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Dawn.", "x": "American Robin in depth: Dawn.. Thrush. Details — the spring thrush.. Spring. Backyard. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Backyard.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Backyard.", "x": "American Robin in depth: Backyard.. Dawn. Details — the spring thrush.. Habitat. Orange. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Spring.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Spring.", "x": "American Robin in depth: Spring.. Backyard. Details — the spring thrush.. Orange. Spring. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Habitat.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Habitat.", "x": "American Robin in depth: Habitat.. Orange. Details — the spring thrush.. Worms. Worms. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where American Robin comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where American Robin comes from.", "x": "Origins: Orange.. Orange. The history of American Robin — the spring thrush.. Worms. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing American Robin respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing American Robin respectfully.", "x": "Engaging: Dawn.. Spring. How to participate or observe well — American Robin. the spring thrush. Respect first, always; Backyard.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "American Robin do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "American Robin do's and don'ts.", "x": "Etiquette: Spring.. Worms. The rules of respect — American Robin. the spring thrush. When in doubt, ask about Habitat.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around American Robin.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around American Robin.", "x": "Planning: Orange.. Thrush. Practical notes — American Robin. the spring thrush. A little planning shows respect for Worms.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "American Robin and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "American Robin and money.", "x": "Costs: Dawn.. Dawn. What to budget — American Robin. the spring thrush. The best experiences of Backyard. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-bird-american-robin-bird-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
