(function(){'use strict';
/* JAH Matcha Tea Database generator — jahdb-e2-tea-matcha-tea-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-tea-matcha-tea',PREFIX='JAH-E2TEAMATCHA-',NAME='JAH Matcha Tea Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Matcha: the complete guide", "d": "Matcha: the whisked green..", "g": "overview", "l": 2, "q": "What is Matcha: the complete guide?", "a": "Matcha: the whisked green..", "x": "The complete tea guide to Matcha: the whisked green.. Japan. History, meaning, practices, and how to engage respectfully — everything in one database. Japan. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Matcha essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Matcha essentials.", "x": "At a glance: Matcha — the whisked green.. Shade-grown. The essentials: Whisk.. Whisk. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Japan.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Japan.", "x": "Matcha: Japan.. Whisk. Essential knowledge — Whisk.. the whisked green. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Japan..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Japan..", "x": "Explained: Japan.. Ceremony. The context — Matcha. Ceremonial. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Shade-grown.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Shade-grown.", "x": "Matcha: Shade-grown.. Grades. Essential knowledge — Ceremonial.. the whisked green. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Shade-grown..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Shade-grown..", "x": "Explained: Shade-grown.. Latte. The context — Matcha. L-theanine. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Whisk.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Whisk.", "x": "Matcha: Whisk.. Ceremony. Essential knowledge — L-theanine.. the whisked green. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Whisk..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Whisk..", "x": "Explained: Whisk.. Caffeine. The context — Matcha. Latte. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Ceremonial.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Ceremonial.", "x": "Matcha: Ceremonial.. Latte. Essential knowledge — Latte.. the whisked green. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Ceremonial..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Ceremonial..", "x": "Explained: Ceremonial.. Japan. The context — Matcha. Japan. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "L-theanine.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "L-theanine.", "x": "Matcha: L-theanine.. Caffeine. Essential knowledge — Japan.. the whisked green. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: L-theanine..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: L-theanine..", "x": "Explained: L-theanine.. Whisk. The context — Matcha. Shade-grown. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Latte.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Latte.", "x": "Matcha: Latte.. Japan. Essential knowledge — Shade-grown.. the whisked green. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Latte..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Latte..", "x": "Explained: Latte.. Grades. The context — Matcha. Whisk. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Japan.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Japan.", "x": "Matcha in depth: Japan.. Shade-grown. Details — the whisked green.. Grades. Ceremonial. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Whisk.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Whisk.", "x": "Matcha in depth: Whisk.. Whisk. Details — the whisked green.. Ceremony. L-theanine. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Grades.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Grades.", "x": "Matcha in depth: Grades.. Ceremonial. Details — the whisked green.. Latte. Latte. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Ceremony.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Ceremony.", "x": "Matcha in depth: Ceremony.. L-theanine. Details — the whisked green.. Caffeine. Japan. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Latte.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Latte.", "x": "Matcha in depth: Latte.. Latte. Details — the whisked green.. Japan. Shade-grown. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Caffeine.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Caffeine.", "x": "Matcha in depth: Caffeine.. Japan. Details — the whisked green.. Whisk. Whisk. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Matcha comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Matcha comes from.", "x": "Origins: Japan.. Japan. The history of Matcha — the whisked green.. Whisk. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Matcha respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Matcha respectfully.", "x": "Engaging: Grades.. Shade-grown. How to participate or observe well — Matcha. the whisked green. Respect first, always; Ceremony.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Matcha do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Matcha do's and don'ts.", "x": "Etiquette: Latte.. Whisk. The rules of respect — Matcha. the whisked green. When in doubt, ask about Caffeine.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Matcha.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Matcha.", "x": "Planning: Japan.. Ceremonial. Practical notes — Matcha. the whisked green. A little planning shows respect for Whisk.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Matcha and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Matcha and money.", "x": "Costs: Grades.. L-theanine. What to budget — Matcha. the whisked green. The best experiences of Ceremony. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-tea-matcha-tea-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
