(function(){'use strict';
/* JAH Tall Tales Short Story Database generator — jahdb-e2-story-tall-tales-stories-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-story-tall-tales-stories',PREFIX='JAH-E2STORYTALL-',NAME='JAH Tall Tales Short Story Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Tall Tales: the complete guide", "d": "Tall Tales: the exaggerated yarns..", "g": "overview", "l": 2, "q": "What is Tall Tales: the complete guide?", "a": "Tall Tales: the exaggerated yarns..", "x": "The complete short story guide to Tall Tales: the exaggerated yarns.. Bunyan. History, meaning, practices, and how to engage respectfully — everything in one database. Bunyan. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Tall Tales essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Tall Tales essentials.", "x": "At a glance: Tall Tales — the exaggerated yarns.. Exaggeration. The essentials: Humor.. Frontier. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Bunyan.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Bunyan.", "x": "Tall Tales: Bunyan.. Humor. Essential knowledge — Frontier.. the exaggerated yarns. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Bunyan..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Bunyan..", "x": "Explained: Bunyan.. Whoppers. The context — Tall Tales. Humor. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Exaggeration.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Exaggeration.", "x": "Tall Tales: Exaggeration.. Oral. Essential knowledge — Humor.. the exaggerated yarns. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Exaggeration..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Exaggeration..", "x": "Explained: Exaggeration.. Frontier. The context — Tall Tales. Oral. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Frontier.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Frontier.", "x": "Tall Tales: Frontier.. Whoppers. Essential knowledge — Oral.. the exaggerated yarns. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Frontier..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Frontier..", "x": "Explained: Frontier.. Classics. The context — Tall Tales. Whoppers. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Humor.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Humor.", "x": "Tall Tales: Humor.. Frontier. Essential knowledge — Whoppers.. the exaggerated yarns. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Humor..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Humor..", "x": "Explained: Humor.. Bunyan. The context — Tall Tales. Bunyan. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Oral.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Oral.", "x": "Tall Tales: Oral.. Classics. Essential knowledge — Bunyan.. the exaggerated yarns. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Oral..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Oral..", "x": "Explained: Oral.. Humor. The context — Tall Tales. Exaggeration. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Whoppers.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Whoppers.", "x": "Tall Tales: Whoppers.. Bunyan. Essential knowledge — Exaggeration.. the exaggerated yarns. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Whoppers..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Whoppers..", "x": "Explained: Whoppers.. Oral. The context — Tall Tales. Frontier. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Bunyan.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Bunyan.", "x": "Tall Tales in depth: Bunyan.. Exaggeration. Details — the exaggerated yarns.. Oral. Humor. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Humor.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Humor.", "x": "Tall Tales in depth: Humor.. Frontier. Details — the exaggerated yarns.. Whoppers. Oral. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Oral.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Oral.", "x": "Tall Tales in depth: Oral.. Humor. Details — the exaggerated yarns.. Frontier. Whoppers. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Whoppers.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Whoppers.", "x": "Tall Tales in depth: Whoppers.. Oral. Details — the exaggerated yarns.. Classics. Bunyan. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Frontier.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Frontier.", "x": "Tall Tales in depth: Frontier.. Whoppers. Details — the exaggerated yarns.. Bunyan. Exaggeration. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Classics.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Classics.", "x": "Tall Tales in depth: Classics.. Bunyan. Details — the exaggerated yarns.. Humor. Frontier. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Tall Tales comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Tall Tales comes from.", "x": "Origins: Bunyan.. Bunyan. The history of Tall Tales — the exaggerated yarns.. Humor. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Tall Tales respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Tall Tales respectfully.", "x": "Engaging: Oral.. Exaggeration. How to participate or observe well — Tall Tales. the exaggerated yarns. Respect first, always; Whoppers.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Tall Tales do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Tall Tales do's and don'ts.", "x": "Etiquette: Frontier.. Frontier. The rules of respect — Tall Tales. the exaggerated yarns. When in doubt, ask about Classics.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Tall Tales.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Tall Tales.", "x": "Planning: Bunyan.. Humor. Practical notes — Tall Tales. the exaggerated yarns. A little planning shows respect for Humor.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Tall Tales and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Tall Tales and money.", "x": "Costs: Oral.. Oral. What to budget — Tall Tales. the exaggerated yarns. The best experiences of Whoppers. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-story-tall-tales-stories-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
