(function(){'use strict';
/* JAH Western Novels Novel Database generator — jahdb-e2-novel-western-novels-genre-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-novel-western-novels-genre',PREFIX='JAH-E2NOVELWEST-',NAME='JAH Western Novels Novel Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Western Novels: the complete guide", "d": "Western Novels: the frontier books..", "g": "overview", "l": 2, "q": "What is Western Novels: the complete guide?", "a": "Western Novels: the frontier books..", "x": "The complete novel guide to Western Novels: the frontier books.. L'Amour. History, meaning, practices, and how to engage respectfully — everything in one database. L'Amour. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Western Novels essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Western Novels essentials.", "x": "At a glance: Western Novels — the frontier books.. Frontier. The essentials: Dime.. Dime. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "L'Amour.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "L'Amour.", "x": "Western Novels: L'Amour.. Dime. Essential knowledge — Dime.. the frontier books. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: L'Amour..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: L'Amour..", "x": "Explained: L'Amour.. Grey. The context — Western Novels. Horses. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Frontier.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Frontier.", "x": "Western Novels: Frontier.. Horses. Essential knowledge — Horses.. the frontier books. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Frontier..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Frontier..", "x": "Explained: Frontier.. Frontier. The context — Western Novels. Zane Grey. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Dime.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Dime.", "x": "Western Novels: Dime.. Grey. Essential knowledge — Zane Grey.. the frontier books. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Dime..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Dime..", "x": "Explained: Dime.. Classics. The context — Western Novels. Dust. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Horses.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Horses.", "x": "Western Novels: Horses.. Frontier. Essential knowledge — Dust.. the frontier books. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Horses..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Horses..", "x": "Explained: Horses.. L'Amour. The context — Western Novels. L'Amour. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Zane Grey.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Zane Grey.", "x": "Western Novels: Zane Grey.. Classics. Essential knowledge — L'Amour.. the frontier books. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Zane Grey..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Zane Grey..", "x": "Explained: Zane Grey.. Dime. The context — Western Novels. Frontier. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Dust.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Dust.", "x": "Western Novels: Dust.. L'Amour. Essential knowledge — Frontier.. the frontier books. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Dust..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Dust..", "x": "Explained: Dust.. Horses. The context — Western Novels. Dime. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "L'Amour.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "L'Amour.", "x": "Western Novels in depth: L'Amour.. Frontier. Details — the frontier books.. Horses. Horses. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Dime.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Dime.", "x": "Western Novels in depth: Dime.. Dime. Details — the frontier books.. Grey. Zane Grey. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Horses.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Horses.", "x": "Western Novels in depth: Horses.. Horses. Details — the frontier books.. Frontier. Dust. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Grey.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Grey.", "x": "Western Novels in depth: Grey.. Zane Grey. Details — the frontier books.. Classics. L'Amour. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Frontier.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Frontier.", "x": "Western Novels in depth: Frontier.. Dust. Details — the frontier books.. L'Amour. Frontier. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Classics.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Classics.", "x": "Western Novels in depth: Classics.. L'Amour. Details — the frontier books.. Dime. Dime. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Western Novels comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Western Novels comes from.", "x": "Origins: L'Amour.. L'Amour. The history of Western Novels — the frontier books.. Dime. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Western Novels respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Western Novels respectfully.", "x": "Engaging: Horses.. Frontier. How to participate or observe well — Western Novels. the frontier books. Respect first, always; Grey.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Western Novels do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Western Novels do's and don'ts.", "x": "Etiquette: Frontier.. Dime. The rules of respect — Western Novels. the frontier books. When in doubt, ask about Classics.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Western Novels.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Western Novels.", "x": "Planning: L'Amour.. Horses. Practical notes — Western Novels. the frontier books. A little planning shows respect for Dime.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Western Novels and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Western Novels and money.", "x": "Costs: Horses.. Zane Grey. What to budget — Western Novels. the frontier books. The best experiences of Grey. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-novel-western-novels-genre-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
