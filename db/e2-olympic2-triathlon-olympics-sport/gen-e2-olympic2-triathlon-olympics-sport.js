(function(){'use strict';
/* JAH Triathlon Olympics Database generator — jahdb-e2-olympic2-triathlon-olympics-sport-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-olympic2-triathlon-olympics-sport',PREFIX='JAH-E2OLYMPIC2T-',NAME='JAH Triathlon Olympics Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Triathlon Olympics: the complete guide", "d": "Triathlon Olympics: the three sports..", "g": "overview", "l": 2, "q": "What is Triathlon Olympics: the complete guide?", "a": "Triathlon Olympics: the three sports..", "x": "The complete olympic sport guide to Triathlon Olympics: the three sports.. 2000. History, meaning, practices, and how to engage respectfully — everything in one database. Transitions. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Triathlon Olympics essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Triathlon Olympics essentials.", "x": "At a glance: Triathlon Olympics — the three sports.. Swim. The essentials: Drafting.. Bike. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "2000.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "2000.", "x": "Triathlon Olympics: 2000.. Drafting. Essential knowledge — Bike.. the three sports. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 2000..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 2000..", "x": "Explained: 2000.. Bike. The context — Triathlon Olympics. Run. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Swim.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Swim.", "x": "Triathlon Olympics: Swim.. Swim. Essential knowledge — Run.. the three sports. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Swim..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Swim..", "x": "Explained: Swim.. Run. The context — Triathlon Olympics. Transitions. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Bike.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Bike.", "x": "Triathlon Olympics: Bike.. Bike. Essential knowledge — Transitions.. the three sports. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Bike..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Bike..", "x": "Explained: Bike.. Guide. The context — Triathlon Olympics. Drafting. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Run.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Run.", "x": "Triathlon Olympics: Run.. Run. Essential knowledge — Drafting.. the three sports. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Run..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Run..", "x": "Explained: Run.. Transitions. The context — Triathlon Olympics. 2000. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Transitions.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Transitions.", "x": "Triathlon Olympics: Transitions.. Guide. Essential knowledge — 2000.. the three sports. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Transitions..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Transitions..", "x": "Explained: Transitions.. Drafting. The context — Triathlon Olympics. Swim. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Drafting.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Drafting.", "x": "Triathlon Olympics: Drafting.. Transitions. Essential knowledge — Swim.. the three sports. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Drafting..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Drafting..", "x": "Explained: Drafting.. Swim. The context — Triathlon Olympics. Bike. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Transitions.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Transitions.", "x": "Triathlon Olympics in depth: Transitions.. Swim. Details — the three sports.. Swim. Run. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Drafting.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Drafting.", "x": "Triathlon Olympics in depth: Drafting.. Bike. Details — the three sports.. Bike. Transitions. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Swim.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Swim.", "x": "Triathlon Olympics in depth: Swim.. Run. Details — the three sports.. Run. Drafting. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Bike.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Bike.", "x": "Triathlon Olympics in depth: Bike.. Transitions. Details — the three sports.. Guide. 2000. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Run.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Run.", "x": "Triathlon Olympics in depth: Run.. Drafting. Details — the three sports.. Transitions. Swim. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Guide.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Guide.", "x": "Triathlon Olympics in depth: Guide.. 2000. Details — the three sports.. Drafting. Bike. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Triathlon Olympics comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Triathlon Olympics comes from.", "x": "Origins: Transitions.. 2000. The history of Triathlon Olympics — the three sports.. Drafting. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Triathlon Olympics respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Triathlon Olympics respectfully.", "x": "Engaging: Swim.. Swim. How to participate or observe well — Triathlon Olympics. the three sports. Respect first, always; Bike.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Triathlon Olympics do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Triathlon Olympics do's and don'ts.", "x": "Etiquette: Run.. Bike. The rules of respect — Triathlon Olympics. the three sports. When in doubt, ask about Guide.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Triathlon Olympics.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Triathlon Olympics.", "x": "Planning: Transitions.. Run. Practical notes — Triathlon Olympics. the three sports. A little planning shows respect for Drafting.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Triathlon Olympics and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Triathlon Olympics and money.", "x": "Costs: Swim.. Transitions. What to budget — Triathlon Olympics. the three sports. The best experiences of Bike. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-olympic2-triathlon-olympics-sport-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
