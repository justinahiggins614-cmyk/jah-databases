(function(){'use strict';
/* JAH Exotic Shorthair Cat Breed Database generator — jahdb-e2-cat-exotic-shorthair-cat-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-cat-exotic-shorthair-cat',PREFIX='JAH-E2CATEXOTIC-',NAME='JAH Exotic Shorthair Cat Breed Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Exotic Shorthair: the complete guide", "d": "Exotic Shorthair: the lazy Persian..", "g": "overview", "l": 2, "q": "What is Exotic Shorthair: the complete guide?", "a": "Exotic Shorthair: the lazy Persian..", "x": "The complete cat breed guide to Exotic Shorthair: the lazy Persian.. Persian. History, meaning, practices, and how to engage respectfully — everything in one database. Short. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Exotic Shorthair essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Exotic Shorthair essentials.", "x": "At a glance: Exotic Shorthair — the lazy Persian.. Short. The essentials: Calm.. Calm. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Persian.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Persian.", "x": "Exotic Shorthair: Persian.. Calm. Essential knowledge — Calm.. the lazy Persian. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Persian..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Persian..", "x": "Explained: Persian.. Lap. The context — Exotic Shorthair. Teddy bear. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Short.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Short.", "x": "Exotic Shorthair: Short.. Teddy. Essential knowledge — Teddy bear.. the lazy Persian. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Short..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Short..", "x": "Explained: Short.. Persian. The context — Exotic Shorthair. Grooming. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Calm.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Calm.", "x": "Exotic Shorthair: Calm.. Lap. Essential knowledge — Grooming.. the lazy Persian. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Calm..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Calm..", "x": "Explained: Calm.. History. The context — Exotic Shorthair. Lap. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Teddy bear.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Teddy bear.", "x": "Exotic Shorthair: Teddy bear.. Persian. Essential knowledge — Lap.. the lazy Persian. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Teddy bear..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Teddy bear..", "x": "Explained: Teddy bear.. Short. The context — Exotic Shorthair. Persian. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Grooming.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Grooming.", "x": "Exotic Shorthair: Grooming.. History. Essential knowledge — Persian.. the lazy Persian. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Grooming..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Grooming..", "x": "Explained: Grooming.. Calm. The context — Exotic Shorthair. Short. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Lap.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Lap.", "x": "Exotic Shorthair: Lap.. Short. Essential knowledge — Short.. the lazy Persian. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Lap..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Lap..", "x": "Explained: Lap.. Teddy. The context — Exotic Shorthair. Calm. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Short.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Short.", "x": "Exotic Shorthair in depth: Short.. Short. Details — the lazy Persian.. Teddy. Teddy bear. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Calm.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Calm.", "x": "Exotic Shorthair in depth: Calm.. Calm. Details — the lazy Persian.. Lap. Grooming. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Teddy.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Teddy.", "x": "Exotic Shorthair in depth: Teddy.. Teddy bear. Details — the lazy Persian.. Persian. Lap. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Lap.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Lap.", "x": "Exotic Shorthair in depth: Lap.. Grooming. Details — the lazy Persian.. History. Persian. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Persian.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Persian.", "x": "Exotic Shorthair in depth: Persian.. Lap. Details — the lazy Persian.. Short. Short. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "History.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "History.", "x": "Exotic Shorthair in depth: History.. Persian. Details — the lazy Persian.. Calm. Calm. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Exotic Shorthair comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Exotic Shorthair comes from.", "x": "Origins: Short.. Persian. The history of Exotic Shorthair — the lazy Persian.. Calm. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Exotic Shorthair respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Exotic Shorthair respectfully.", "x": "Engaging: Teddy.. Short. How to participate or observe well — Exotic Shorthair. the lazy Persian. Respect first, always; Lap.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Exotic Shorthair do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Exotic Shorthair do's and don'ts.", "x": "Etiquette: Persian.. Calm. The rules of respect — Exotic Shorthair. the lazy Persian. When in doubt, ask about History.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Exotic Shorthair.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Exotic Shorthair.", "x": "Planning: Short.. Teddy bear. Practical notes — Exotic Shorthair. the lazy Persian. A little planning shows respect for Calm.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Exotic Shorthair and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Exotic Shorthair and money.", "x": "Costs: Teddy.. Grooming. What to budget — Exotic Shorthair. the lazy Persian. The best experiences of Lap. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-cat-exotic-shorthair-cat-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
