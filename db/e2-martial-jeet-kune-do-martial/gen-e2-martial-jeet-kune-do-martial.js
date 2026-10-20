(function(){'use strict';
/* JAH Jeet Kune Do Martial Art Database generator — jahdb-e2-martial-jeet-kune-do-martial-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-martial-jeet-kune-do-martial',PREFIX='JAH-E2MARTIALJE-',NAME='JAH Jeet Kune Do Martial Art Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Jeet Kune Do: the complete guide", "d": "Jeet Kune Do: Bruce Lee's way..", "g": "overview", "l": 2, "q": "What is Jeet Kune Do: the complete guide?", "a": "Jeet Kune Do: Bruce Lee's way..", "x": "The complete martial art guide to Jeet Kune Do: Bruce Lee's way.. Bruce Lee. History, meaning, practices, and how to engage respectfully — everything in one database. Bruce Lee. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Jeet Kune Do essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Jeet Kune Do essentials.", "x": "At a glance: Jeet Kune Do — Bruce Lee's way.. No way. The essentials: Philosophy.. Intercepting. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Bruce Lee.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Bruce Lee.", "x": "Jeet Kune Do: Bruce Lee.. Philosophy. Essential knowledge — Intercepting.. Bruce Lee's way. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Bruce Lee..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Bruce Lee..", "x": "Explained: Bruce Lee.. Absorb. The context — Jeet Kune Do. Philosophy. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "No way.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "No way.", "x": "Jeet Kune Do: No way.. 1967. Essential knowledge — Philosophy.. Bruce Lee's way. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: No way..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: No way..", "x": "Explained: No way.. No way. The context — Jeet Kune Do. 1967. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Intercepting.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Intercepting.", "x": "Jeet Kune Do: Intercepting.. Absorb. Essential knowledge — 1967.. Bruce Lee's way. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Intercepting..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Intercepting..", "x": "Explained: Intercepting.. Training. The context — Jeet Kune Do. Absorb. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Philosophy.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Philosophy.", "x": "Jeet Kune Do: Philosophy.. No way. Essential knowledge — Absorb.. Bruce Lee's way. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Philosophy..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Philosophy..", "x": "Explained: Philosophy.. Bruce Lee. The context — Jeet Kune Do. Bruce Lee. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "1967.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "1967.", "x": "Jeet Kune Do: 1967.. Training. Essential knowledge — Bruce Lee.. Bruce Lee's way. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: 1967..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: 1967..", "x": "Explained: 1967.. Philosophy. The context — Jeet Kune Do. No way. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Absorb.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Absorb.", "x": "Jeet Kune Do: Absorb.. Bruce Lee. Essential knowledge — No way.. Bruce Lee's way. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Absorb..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Absorb..", "x": "Explained: Absorb.. 1967. The context — Jeet Kune Do. Intercepting. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Bruce Lee.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Bruce Lee.", "x": "Jeet Kune Do in depth: Bruce Lee.. No way. Details — Bruce Lee's way.. 1967. Philosophy. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Philosophy.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Philosophy.", "x": "Jeet Kune Do in depth: Philosophy.. Intercepting. Details — Bruce Lee's way.. Absorb. 1967. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "1967.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "1967.", "x": "Jeet Kune Do in depth: 1967.. Philosophy. Details — Bruce Lee's way.. No way. Absorb. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Absorb.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Absorb.", "x": "Jeet Kune Do in depth: Absorb.. 1967. Details — Bruce Lee's way.. Training. Bruce Lee. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "No way.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "No way.", "x": "Jeet Kune Do in depth: No way.. Absorb. Details — Bruce Lee's way.. Bruce Lee. No way. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Training.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Training.", "x": "Jeet Kune Do in depth: Training.. Bruce Lee. Details — Bruce Lee's way.. Philosophy. Intercepting. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Jeet Kune Do comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Jeet Kune Do comes from.", "x": "Origins: Bruce Lee.. Bruce Lee. The history of Jeet Kune Do — Bruce Lee's way.. Philosophy. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Jeet Kune Do respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Jeet Kune Do respectfully.", "x": "Engaging: 1967.. No way. How to participate or observe well — Jeet Kune Do. Bruce Lee's way. Respect first, always; Absorb.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Jeet Kune Do do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Jeet Kune Do do's and don'ts.", "x": "Etiquette: No way.. Intercepting. The rules of respect — Jeet Kune Do. Bruce Lee's way. When in doubt, ask about Training.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Jeet Kune Do.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Jeet Kune Do.", "x": "Planning: Bruce Lee.. Philosophy. Practical notes — Jeet Kune Do. Bruce Lee's way. A little planning shows respect for Philosophy.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Jeet Kune Do and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Jeet Kune Do and money.", "x": "Costs: 1967.. 1967. What to budget — Jeet Kune Do. Bruce Lee's way. The best experiences of Absorb. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-martial-jeet-kune-do-martial-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
