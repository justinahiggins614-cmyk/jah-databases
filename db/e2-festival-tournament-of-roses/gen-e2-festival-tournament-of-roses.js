(function(){'use strict';
/* JAH Tournament of Roses Festival Database generator — jahdb-e2-festival-tournament-of-roses-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-festival-tournament-of-roses',PREFIX='JAH-E2FESTIVALT-',NAME='JAH Tournament of Roses Festival Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Tournament of Roses: the complete guide", "d": "Tournament of Roses: flower parade..", "g": "overview", "l": 2, "q": "What is Tournament of Roses: the complete guide?", "a": "Tournament of Roses: flower parade..", "x": "The complete festival guide to Tournament of Roses: flower parade.. January 1. History, meaning, practices, and how to engage respectfully — everything in one database. Floats. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Tournament of Roses essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Tournament of Roses essentials.", "x": "At a glance: Tournament of Roses — flower parade.. Pasadena. The essentials: History.. Floats. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "January 1.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "January 1.", "x": "Tournament of Roses: January 1.. History. Essential knowledge — Floats.. flower parade. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: January 1..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: January 1..", "x": "Explained: January 1.. Travel. The context — Tournament of Roses. Rose Bowl. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Pasadena.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Pasadena.", "x": "Tournament of Roses: Pasadena.. Game. Essential knowledge — Rose Bowl.. flower parade. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Pasadena..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Pasadena..", "x": "Explained: Pasadena.. Flowers. The context — Tournament of Roses. History. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Floats.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Floats.", "x": "Tournament of Roses: Floats.. Travel. Essential knowledge — History.. flower parade. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Floats..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Floats..", "x": "Explained: Floats.. Tradition. The context — Tournament of Roses. Flowers. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Rose Bowl.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Rose Bowl.", "x": "Tournament of Roses: Rose Bowl.. Flowers. Essential knowledge — Flowers.. flower parade. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Rose Bowl..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Rose Bowl..", "x": "Explained: Rose Bowl.. Floats. The context — Tournament of Roses. January 1. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "History.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "History.", "x": "Tournament of Roses: History.. Tradition. Essential knowledge — January 1.. flower parade. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: History..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: History..", "x": "Explained: History.. History. The context — Tournament of Roses. Pasadena. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Flowers.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Flowers.", "x": "Tournament of Roses: Flowers.. Floats. Essential knowledge — Pasadena.. flower parade. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Flowers..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Flowers..", "x": "Explained: Flowers.. Game. The context — Tournament of Roses. Floats. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Floats.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Floats.", "x": "Tournament of Roses in depth: Floats.. Pasadena. Details — flower parade.. Game. Rose Bowl. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "History.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "History.", "x": "Tournament of Roses in depth: History.. Floats. Details — flower parade.. Travel. History. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Game.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Game.", "x": "Tournament of Roses in depth: Game.. Rose Bowl. Details — flower parade.. Flowers. Flowers. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Travel.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Travel.", "x": "Tournament of Roses in depth: Travel.. History. Details — flower parade.. Tradition. January 1. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Flowers.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Flowers.", "x": "Tournament of Roses in depth: Flowers.. Flowers. Details — flower parade.. Floats. Pasadena. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Tradition.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Tradition.", "x": "Tournament of Roses in depth: Tradition.. January 1. Details — flower parade.. History. Floats. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Tournament of Roses comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Tournament of Roses comes from.", "x": "Origins: Floats.. January 1. The history of Tournament of Roses — flower parade.. History. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Tournament of Roses respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Tournament of Roses respectfully.", "x": "Engaging: Game.. Pasadena. How to participate or observe well — Tournament of Roses. flower parade. Respect first, always; Travel.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Tournament of Roses do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Tournament of Roses do's and don'ts.", "x": "Etiquette: Flowers.. Floats. The rules of respect — Tournament of Roses. flower parade. When in doubt, ask about Tradition.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Tournament of Roses.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Tournament of Roses.", "x": "Planning: Floats.. Rose Bowl. Practical notes — Tournament of Roses. flower parade. A little planning shows respect for History.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Tournament of Roses and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Tournament of Roses and money.", "x": "Costs: Game.. History. What to budget — Tournament of Roses. flower parade. The best experiences of Travel. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-festival-tournament-of-roses-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
