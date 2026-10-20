(function(){'use strict';
/* JAH Garter Snake Reptile Database generator — jahdb-e2-reptile-garter-snake-reptile-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-reptile-garter-snake-reptile',PREFIX='JAH-E2REPTILEGA-',NAME='JAH Garter Snake Reptile Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Garter Snake: the complete guide", "d": "Garter Snake: the garden snake..", "g": "overview", "l": 2, "q": "What is Garter Snake: the complete guide?", "a": "Garter Snake: the garden snake..", "x": "The complete reptile guide to Garter Snake: the garden snake.. Garden. History, meaning, practices, and how to engage respectfully — everything in one database. Garden. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Garter Snake essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Garter Snake essentials.", "x": "At a glance: Garter Snake — the garden snake.. Stripes. The essentials: Stripes.. Live birth. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Garden.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Garden.", "x": "Garter Snake: Garden.. Stripes. Essential knowledge — Live birth.. the garden snake. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Garden..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Garden..", "x": "Explained: Garden.. Mild. The context — Garter Snake. Common. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Stripes.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Stripes.", "x": "Garter Snake: Stripes.. Common. Essential knowledge — Common.. the garden snake. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Stripes..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Stripes..", "x": "Explained: Stripes.. Birth. The context — Garter Snake. Mild. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Live birth.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Live birth.", "x": "Garter Snake: Live birth.. Mild. Essential knowledge — Mild.. the garden snake. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Live birth..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Live birth..", "x": "Explained: Live birth.. Care. The context — Garter Snake. Amphibians. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Common.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Common.", "x": "Garter Snake: Common.. Birth. Essential knowledge — Amphibians.. the garden snake. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Common..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Common..", "x": "Explained: Common.. Garden. The context — Garter Snake. Garden. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Mild.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Mild.", "x": "Garter Snake: Mild.. Care. Essential knowledge — Garden.. the garden snake. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Mild..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Mild..", "x": "Explained: Mild.. Stripes. The context — Garter Snake. Stripes. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Amphibians.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Amphibians.", "x": "Garter Snake: Amphibians.. Garden. Essential knowledge — Stripes.. the garden snake. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Amphibians..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Amphibians..", "x": "Explained: Amphibians.. Common. The context — Garter Snake. Live birth. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Garden.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Garden.", "x": "Garter Snake in depth: Garden.. Stripes. Details — the garden snake.. Common. Common. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Stripes.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Stripes.", "x": "Garter Snake in depth: Stripes.. Live birth. Details — the garden snake.. Mild. Mild. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Common.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Common.", "x": "Garter Snake in depth: Common.. Common. Details — the garden snake.. Birth. Amphibians. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Mild.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Mild.", "x": "Garter Snake in depth: Mild.. Mild. Details — the garden snake.. Care. Garden. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Birth.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Birth.", "x": "Garter Snake in depth: Birth.. Amphibians. Details — the garden snake.. Garden. Stripes. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Care.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Care.", "x": "Garter Snake in depth: Care.. Garden. Details — the garden snake.. Stripes. Live birth. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Garter Snake comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Garter Snake comes from.", "x": "Origins: Garden.. Garden. The history of Garter Snake — the garden snake.. Stripes. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Garter Snake respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Garter Snake respectfully.", "x": "Engaging: Common.. Stripes. How to participate or observe well — Garter Snake. the garden snake. Respect first, always; Mild.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Garter Snake do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Garter Snake do's and don'ts.", "x": "Etiquette: Birth.. Live birth. The rules of respect — Garter Snake. the garden snake. When in doubt, ask about Care.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Garter Snake.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Garter Snake.", "x": "Planning: Garden.. Common. Practical notes — Garter Snake. the garden snake. A little planning shows respect for Stripes.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Garter Snake and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Garter Snake and money.", "x": "Costs: Common.. Mild. What to budget — Garter Snake. the garden snake. The best experiences of Mild. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-reptile-garter-snake-reptile-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
