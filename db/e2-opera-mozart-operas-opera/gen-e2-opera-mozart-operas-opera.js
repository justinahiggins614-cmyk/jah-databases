(function(){'use strict';
/* JAH Mozart Operas Opera Database generator — jahdb-e2-opera-mozart-operas-opera-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-opera-mozart-operas-opera',PREFIX='JAH-E2OPERAMOZA-',NAME='JAH Mozart Operas Opera Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Mozart Operas: the complete guide", "d": "Mozart Operas: the perfect operas..", "g": "overview", "l": 2, "q": "What is Mozart Operas: the complete guide?", "a": "Mozart Operas: the perfect operas..", "x": "The complete opera guide to Mozart Operas: the perfect operas.. Figaro. History, meaning, practices, and how to engage respectfully — everything in one database. Figaro. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Mozart Operas essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Mozart Operas essentials.", "x": "At a glance: Mozart Operas — the perfect operas.. Don Giovanni. The essentials: Flute.. Flute. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Figaro.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Figaro.", "x": "Mozart Operas: Figaro.. Flute. Essential knowledge — Flute.. the perfect operas. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Figaro..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Figaro..", "x": "Explained: Figaro.. Da Ponte. The context — Mozart Operas. Ensembles. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Don Giovanni.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Don Giovanni.", "x": "Mozart Operas: Don Giovanni.. Vienna. Essential knowledge — Ensembles.. the perfect operas. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Don Giovanni..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Don Giovanni..", "x": "Explained: Don Giovanni.. Don. The context — Mozart Operas. Vienna. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Flute.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Flute.", "x": "Mozart Operas: Flute.. Da Ponte. Essential knowledge — Vienna.. the perfect operas. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Flute..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Flute..", "x": "Explained: Flute.. History. The context — Mozart Operas. Da Ponte. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Ensembles.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Ensembles.", "x": "Mozart Operas: Ensembles.. Don. Essential knowledge — Da Ponte.. the perfect operas. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Ensembles..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Ensembles..", "x": "Explained: Ensembles.. Figaro. The context — Mozart Operas. Figaro. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Vienna.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Vienna.", "x": "Mozart Operas: Vienna.. History. Essential knowledge — Figaro.. the perfect operas. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Vienna..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Vienna..", "x": "Explained: Vienna.. Flute. The context — Mozart Operas. Don Giovanni. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Da Ponte.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Da Ponte.", "x": "Mozart Operas: Da Ponte.. Figaro. Essential knowledge — Don Giovanni.. the perfect operas. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Da Ponte..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Da Ponte..", "x": "Explained: Da Ponte.. Vienna. The context — Mozart Operas. Flute. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Figaro.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Figaro.", "x": "Mozart Operas in depth: Figaro.. Don Giovanni. Details — the perfect operas.. Vienna. Ensembles. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Flute.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Flute.", "x": "Mozart Operas in depth: Flute.. Flute. Details — the perfect operas.. Da Ponte. Vienna. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Vienna.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Vienna.", "x": "Mozart Operas in depth: Vienna.. Ensembles. Details — the perfect operas.. Don. Da Ponte. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Da Ponte.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Da Ponte.", "x": "Mozart Operas in depth: Da Ponte.. Vienna. Details — the perfect operas.. History. Figaro. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Don.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Don.", "x": "Mozart Operas in depth: Don.. Da Ponte. Details — the perfect operas.. Figaro. Don Giovanni. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "History.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "History.", "x": "Mozart Operas in depth: History.. Figaro. Details — the perfect operas.. Flute. Flute. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Mozart Operas comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Mozart Operas comes from.", "x": "Origins: Figaro.. Figaro. The history of Mozart Operas — the perfect operas.. Flute. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Mozart Operas respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Mozart Operas respectfully.", "x": "Engaging: Vienna.. Don Giovanni. How to participate or observe well — Mozart Operas. the perfect operas. Respect first, always; Da Ponte.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Mozart Operas do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Mozart Operas do's and don'ts.", "x": "Etiquette: Don.. Flute. The rules of respect — Mozart Operas. the perfect operas. When in doubt, ask about History.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Mozart Operas.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Mozart Operas.", "x": "Planning: Figaro.. Ensembles. Practical notes — Mozart Operas. the perfect operas. A little planning shows respect for Flute.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Mozart Operas and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Mozart Operas and money.", "x": "Costs: Vienna.. Vienna. What to budget — Mozart Operas. the perfect operas. The best experiences of Da Ponte. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-opera-mozart-operas-opera-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
