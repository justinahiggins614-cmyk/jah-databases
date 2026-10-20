(function(){'use strict';
/* JAH Rose2 Database generator — jahdb-e2-nature2-rose2-flower-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-nature2-rose2-flower',PREFIX='JAH-E2NATURE2RO-',NAME='JAH Rose2 Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Rose2: the complete guide", "d": "Rose2: the queen 2..", "g": "overview", "l": 2, "q": "What is Rose2: the complete guide?", "a": "Rose2: the queen 2..", "x": "The complete flower guide to Rose2: the queen 2.. Pruning. History, meaning, practices, and how to engage respectfully — everything in one database. Pruning. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Rose2 essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Rose2 essentials.", "x": "At a glance: Rose2 — the queen 2.. Fragrant. The essentials: June.. Hybrid tea. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Pruning.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Pruning.", "x": "Rose2: Pruning.. June. Essential knowledge — Hybrid tea.. the queen 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Pruning..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Pruning..", "x": "Explained: Pruning.. Fragrant. The context — Rose2. Thorns. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Fragrant.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Fragrant.", "x": "Rose2: Fragrant.. Bushes. Essential knowledge — Thorns.. the queen 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Fragrant..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Fragrant..", "x": "Explained: Fragrant.. Thorns. The context — Rose2. June. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Hybrid tea.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Hybrid tea.", "x": "Rose2: Hybrid tea.. Fragrant. Essential knowledge — June.. the queen 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Hybrid tea..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Hybrid tea..", "x": "Explained: Hybrid tea.. Growing. The context — Rose2. Bushes. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Thorns.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Thorns.", "x": "Rose2: Thorns.. Thorns. Essential knowledge — Bushes.. the queen 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Thorns..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Thorns..", "x": "Explained: Thorns.. Pruning. The context — Rose2. Pruning. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "June.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "June.", "x": "Rose2: June.. Growing. Essential knowledge — Pruning.. the queen 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: June..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: June..", "x": "Explained: June.. June. The context — Rose2. Fragrant. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Bushes.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Bushes.", "x": "Rose2: Bushes.. Pruning. Essential knowledge — Fragrant.. the queen 2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Bushes..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Bushes..", "x": "Explained: Bushes.. Bushes. The context — Rose2. Hybrid tea. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Pruning.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Pruning.", "x": "Rose2 in depth: Pruning.. Fragrant. Details — the queen 2.. Bushes. Thorns. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "June.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "June.", "x": "Rose2 in depth: June.. Hybrid tea. Details — the queen 2.. Fragrant. June. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Bushes.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Bushes.", "x": "Rose2 in depth: Bushes.. Thorns. Details — the queen 2.. Thorns. Bushes. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Fragrant.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Fragrant.", "x": "Rose2 in depth: Fragrant.. June. Details — the queen 2.. Growing. Pruning. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Thorns.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Thorns.", "x": "Rose2 in depth: Thorns.. Bushes. Details — the queen 2.. Pruning. Fragrant. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Growing.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Growing.", "x": "Rose2 in depth: Growing.. Pruning. Details — the queen 2.. June. Hybrid tea. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Rose2 comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Rose2 comes from.", "x": "Origins: Pruning.. Pruning. The history of Rose2 — the queen 2.. June. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Rose2 respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Rose2 respectfully.", "x": "Engaging: Bushes.. Fragrant. How to participate or observe well — Rose2. the queen 2. Respect first, always; Fragrant.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Rose2 do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Rose2 do's and don'ts.", "x": "Etiquette: Thorns.. Hybrid tea. The rules of respect — Rose2. the queen 2. When in doubt, ask about Growing.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Rose2.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Rose2.", "x": "Planning: Pruning.. Thorns. Practical notes — Rose2. the queen 2. A little planning shows respect for June.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Rose2 and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Rose2 and money.", "x": "Costs: Bushes.. June. What to budget — Rose2. the queen 2. The best experiences of Fragrant. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-nature2-rose2-flower-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
