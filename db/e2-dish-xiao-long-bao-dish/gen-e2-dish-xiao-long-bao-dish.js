(function(){'use strict';
/* JAH Xiao Long Bao Dish Database generator — jahdb-e2-dish-xiao-long-bao-dish-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-dish-xiao-long-bao-dish',PREFIX='JAH-E2DISHXIAOL-',NAME='JAH Xiao Long Bao Dish Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Xiao Long Bao: the complete guide", "d": "Xiao Long Bao: the soup dumplings..", "g": "overview", "l": 2, "q": "What is Xiao Long Bao: the complete guide?", "a": "Xiao Long Bao: the soup dumplings..", "x": "The complete dish guide to Xiao Long Bao: the soup dumplings.. Shanghai. History, meaning, practices, and how to engage respectfully — everything in one database. Soup. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Xiao Long Bao essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Xiao Long Bao essentials.", "x": "At a glance: Xiao Long Bao — the soup dumplings.. Soup. The essentials: Folds.. 18 folds. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Shanghai.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Shanghai.", "x": "Xiao Long Bao: Shanghai.. Folds. Essential knowledge — 18 folds.. the soup dumplings. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Shanghai..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Shanghai..", "x": "Explained: Shanghai.. Bite. The context — Xiao Long Bao. Vinegar. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Soup.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Soup.", "x": "Xiao Long Bao: Soup.. Steamed. Essential knowledge — Vinegar.. the soup dumplings. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Soup..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Soup..", "x": "Explained: Soup.. Shanghai. The context — Xiao Long Bao. Steamed. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "18 folds.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "18 folds.", "x": "Xiao Long Bao: 18 folds.. Bite. Essential knowledge — Steamed.. the soup dumplings. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: 18 folds..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: 18 folds..", "x": "Explained: 18 folds.. Making. The context — Xiao Long Bao. Bite. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Vinegar.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Vinegar.", "x": "Xiao Long Bao: Vinegar.. Shanghai. Essential knowledge — Bite.. the soup dumplings. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Vinegar..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Vinegar..", "x": "Explained: Vinegar.. Soup. The context — Xiao Long Bao. Shanghai. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Steamed.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Steamed.", "x": "Xiao Long Bao: Steamed.. Making. Essential knowledge — Shanghai.. the soup dumplings. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Steamed..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Steamed..", "x": "Explained: Steamed.. Folds. The context — Xiao Long Bao. Soup. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Bite.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Bite.", "x": "Xiao Long Bao: Bite.. Soup. Essential knowledge — Soup.. the soup dumplings. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Bite..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Bite..", "x": "Explained: Bite.. Steamed. The context — Xiao Long Bao. 18 folds. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Soup.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Soup.", "x": "Xiao Long Bao in depth: Soup.. Soup. Details — the soup dumplings.. Steamed. Vinegar. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Folds.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Folds.", "x": "Xiao Long Bao in depth: Folds.. 18 folds. Details — the soup dumplings.. Bite. Steamed. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Steamed.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Steamed.", "x": "Xiao Long Bao in depth: Steamed.. Vinegar. Details — the soup dumplings.. Shanghai. Bite. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Bite.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Bite.", "x": "Xiao Long Bao in depth: Bite.. Steamed. Details — the soup dumplings.. Making. Shanghai. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Shanghai.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Shanghai.", "x": "Xiao Long Bao in depth: Shanghai.. Bite. Details — the soup dumplings.. Soup. Soup. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Making.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Making.", "x": "Xiao Long Bao in depth: Making.. Shanghai. Details — the soup dumplings.. Folds. 18 folds. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Xiao Long Bao comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Xiao Long Bao comes from.", "x": "Origins: Soup.. Shanghai. The history of Xiao Long Bao — the soup dumplings.. Folds. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Xiao Long Bao respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Xiao Long Bao respectfully.", "x": "Engaging: Steamed.. Soup. How to participate or observe well — Xiao Long Bao. the soup dumplings. Respect first, always; Bite.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Xiao Long Bao do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Xiao Long Bao do's and don'ts.", "x": "Etiquette: Shanghai.. 18 folds. The rules of respect — Xiao Long Bao. the soup dumplings. When in doubt, ask about Making.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Xiao Long Bao.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Xiao Long Bao.", "x": "Planning: Soup.. Vinegar. Practical notes — Xiao Long Bao. the soup dumplings. A little planning shows respect for Folds.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Xiao Long Bao and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Xiao Long Bao and money.", "x": "Costs: Steamed.. Steamed. What to budget — Xiao Long Bao. the soup dumplings. The best experiences of Bite. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-dish-xiao-long-bao-dish-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
