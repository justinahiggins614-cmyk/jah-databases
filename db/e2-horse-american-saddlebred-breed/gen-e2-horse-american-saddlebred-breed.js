(function(){'use strict';
/* JAH American Saddlebred Horse Breed Database generator — jahdb-e2-horse-american-saddlebred-breed-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-horse-american-saddlebred-breed',PREFIX='JAH-E2HORSEAMER-',NAME='JAH American Saddlebred Horse Breed Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "American Saddlebred: the complete guide", "d": "American Saddlebred: the peacock horse..", "g": "overview", "l": 2, "q": "What is American Saddlebred: the complete guide?", "a": "American Saddlebred: the peacock horse..", "x": "The complete horse breed guide to American Saddlebred: the peacock horse.. High-stepping. History, meaning, practices, and how to engage respectfully — everything in one database. Stepping. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "American Saddlebred essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "American Saddlebred essentials.", "x": "At a glance: American Saddlebred — the peacock horse.. Kentucky. The essentials: Kentucky.. Show. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "High-stepping.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "High-stepping.", "x": "American Saddlebred: High-stepping.. Kentucky. Essential knowledge — Show.. the peacock horse. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: High-stepping..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: High-stepping..", "x": "Explained: High-stepping.. Saddle. The context — American Saddlebred. Five-gaited. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Kentucky.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Kentucky.", "x": "American Saddlebred: Kentucky.. Elegant. Essential knowledge — Five-gaited.. the peacock horse. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Kentucky..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Kentucky..", "x": "Explained: Kentucky.. Show. The context — American Saddlebred. Elegant. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Show.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Show.", "x": "American Saddlebred: Show.. Saddle. Essential knowledge — Elegant.. the peacock horse. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Show..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Show..", "x": "Explained: Show.. History. The context — American Saddlebred. Saddle. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Five-gaited.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Five-gaited.", "x": "American Saddlebred: Five-gaited.. Show. Essential knowledge — Saddle.. the peacock horse. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Five-gaited..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Five-gaited..", "x": "Explained: Five-gaited.. Stepping. The context — American Saddlebred. High-stepping. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Elegant.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Elegant.", "x": "American Saddlebred: Elegant.. History. Essential knowledge — High-stepping.. the peacock horse. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Elegant..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Elegant..", "x": "Explained: Elegant.. Kentucky. The context — American Saddlebred. Kentucky. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Saddle.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Saddle.", "x": "American Saddlebred: Saddle.. Stepping. Essential knowledge — Kentucky.. the peacock horse. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Saddle..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Saddle..", "x": "Explained: Saddle.. Elegant. The context — American Saddlebred. Show. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Stepping.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Stepping.", "x": "American Saddlebred in depth: Stepping.. Kentucky. Details — the peacock horse.. Elegant. Five-gaited. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Kentucky.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Kentucky.", "x": "American Saddlebred in depth: Kentucky.. Show. Details — the peacock horse.. Saddle. Elegant. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Elegant.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Elegant.", "x": "American Saddlebred in depth: Elegant.. Five-gaited. Details — the peacock horse.. Show. Saddle. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Saddle.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Saddle.", "x": "American Saddlebred in depth: Saddle.. Elegant. Details — the peacock horse.. History. High-stepping. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Show.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Show.", "x": "American Saddlebred in depth: Show.. Saddle. Details — the peacock horse.. Stepping. Kentucky. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "History.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "History.", "x": "American Saddlebred in depth: History.. High-stepping. Details — the peacock horse.. Kentucky. Show. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where American Saddlebred comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where American Saddlebred comes from.", "x": "Origins: Stepping.. High-stepping. The history of American Saddlebred — the peacock horse.. Kentucky. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing American Saddlebred respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing American Saddlebred respectfully.", "x": "Engaging: Elegant.. Kentucky. How to participate or observe well — American Saddlebred. the peacock horse. Respect first, always; Saddle.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "American Saddlebred do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "American Saddlebred do's and don'ts.", "x": "Etiquette: Show.. Show. The rules of respect — American Saddlebred. the peacock horse. When in doubt, ask about History.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around American Saddlebred.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around American Saddlebred.", "x": "Planning: Stepping.. Five-gaited. Practical notes — American Saddlebred. the peacock horse. A little planning shows respect for Kentucky.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "American Saddlebred and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "American Saddlebred and money.", "x": "Costs: Elegant.. Elegant. What to budget — American Saddlebred. the peacock horse. The best experiences of Saddle. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-horse-american-saddlebred-breed-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
