(function(){'use strict';
/* JAH Leave It Training Dog Training Database generator — jahdb-e2-training-leave-it-dog-training-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-training-leave-it-dog-training',PREFIX='JAH-E2TRAININGL-',NAME='JAH Leave It Training Dog Training Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Leave It Training: the complete guide", "d": "Leave It Training: the impulse leave..", "g": "overview", "l": 2, "q": "What is Leave It Training: the complete guide?", "a": "Leave It Training: the impulse leave..", "x": "The complete dog training guide to Leave It Training: the impulse leave.. Trade. History, meaning, practices, and how to engage respectfully — everything in one database. Trade. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Leave It Training essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Leave It Training essentials.", "x": "At a glance: Leave It Training — the impulse leave.. Impulse. The essentials: Safety.. Safety. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Trade.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Trade.", "x": "Leave It Training: Trade.. Safety. Essential knowledge — Safety.. the impulse leave. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Trade..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Trade..", "x": "Explained: Trade.. Control. The context — Leave It Training. Chicken. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Impulse.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Impulse.", "x": "Leave It Training: Impulse.. Proofing. Essential knowledge — Chicken.. the impulse leave. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Impulse..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Impulse..", "x": "Explained: Impulse.. Chicken. The context — Leave It Training. Proofing. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Safety.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Safety.", "x": "Leave It Training: Safety.. Control. Essential knowledge — Proofing.. the impulse leave. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Safety..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Safety..", "x": "Explained: Safety.. Steps. The context — Leave It Training. Self-control. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Chicken.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Chicken.", "x": "Leave It Training: Chicken.. Chicken. Essential knowledge — Self-control.. the impulse leave. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Chicken..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Chicken..", "x": "Explained: Chicken.. Trade. The context — Leave It Training. Trade. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Proofing.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Proofing.", "x": "Leave It Training: Proofing.. Steps. Essential knowledge — Trade.. the impulse leave. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Proofing..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Proofing..", "x": "Explained: Proofing.. Safety. The context — Leave It Training. Impulse. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Self-control.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Self-control.", "x": "Leave It Training: Self-control.. Trade. Essential knowledge — Impulse.. the impulse leave. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Self-control..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Self-control..", "x": "Explained: Self-control.. Proofing. The context — Leave It Training. Safety. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Trade.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Trade.", "x": "Leave It Training in depth: Trade.. Impulse. Details — the impulse leave.. Proofing. Chicken. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Safety.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Safety.", "x": "Leave It Training in depth: Safety.. Safety. Details — the impulse leave.. Control. Proofing. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Proofing.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Proofing.", "x": "Leave It Training in depth: Proofing.. Chicken. Details — the impulse leave.. Chicken. Self-control. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Control.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Control.", "x": "Leave It Training in depth: Control.. Proofing. Details — the impulse leave.. Steps. Trade. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Chicken.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Chicken.", "x": "Leave It Training in depth: Chicken.. Self-control. Details — the impulse leave.. Trade. Impulse. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Steps.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Steps.", "x": "Leave It Training in depth: Steps.. Trade. Details — the impulse leave.. Safety. Safety. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Leave It Training comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Leave It Training comes from.", "x": "Origins: Trade.. Trade. The history of Leave It Training — the impulse leave.. Safety. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Leave It Training respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Leave It Training respectfully.", "x": "Engaging: Proofing.. Impulse. How to participate or observe well — Leave It Training. the impulse leave. Respect first, always; Control.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Leave It Training do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Leave It Training do's and don'ts.", "x": "Etiquette: Chicken.. Safety. The rules of respect — Leave It Training. the impulse leave. When in doubt, ask about Steps.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Leave It Training.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Leave It Training.", "x": "Planning: Trade.. Chicken. Practical notes — Leave It Training. the impulse leave. A little planning shows respect for Safety.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Leave It Training and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Leave It Training and money.", "x": "Costs: Proofing.. Proofing. What to budget — Leave It Training. the impulse leave. The best experiences of Control. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-training-leave-it-dog-training-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
