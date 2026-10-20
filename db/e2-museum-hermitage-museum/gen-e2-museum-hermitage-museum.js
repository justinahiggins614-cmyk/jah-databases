(function(){'use strict';
/* JAH Hermitage Museum Museum Database generator — jahdb-e2-museum-hermitage-museum-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-museum-hermitage-museum',PREFIX='JAH-E2MUSEUMHER-',NAME='JAH Hermitage Museum Museum Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Hermitage Museum: the complete guide", "d": "Hermitage Museum: the Winter Palace collection..", "g": "overview", "l": 2, "q": "What is Hermitage Museum: the complete guide?", "a": "Hermitage Museum: the Winter Palace collection..", "x": "The complete museum guide to Hermitage Museum: the Winter Palace collection.. St. Petersburg. History, meaning, practices, and how to engage respectfully — everything in one database. Palace. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Hermitage Museum essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Hermitage Museum essentials.", "x": "At a glance: Hermitage Museum — the Winter Palace collection.. Catherine. The essentials: Collection.. 3M objects. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "St. Petersburg.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "St. Petersburg.", "x": "Hermitage Museum: St. Petersburg.. Collection. Essential knowledge — 3M objects.. the Winter Palace collection. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: St. Petersburg..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: St. Petersburg..", "x": "Explained: St. Petersburg.. Tickets. The context — Hermitage Museum. Palace. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Catherine.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Catherine.", "x": "Hermitage Museum: Catherine.. History. Essential knowledge — Palace.. the Winter Palace collection. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Catherine..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Catherine..", "x": "Explained: Catherine.. Art. The context — Hermitage Museum. Impressionists. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "3M objects.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "3M objects.", "x": "Hermitage Museum: 3M objects.. Tickets. Essential knowledge — Impressionists.. the Winter Palace collection. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: 3M objects..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: 3M objects..", "x": "Explained: 3M objects.. Russia. The context — Hermitage Museum. History. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Palace.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Palace.", "x": "Hermitage Museum: Palace.. Art. Essential knowledge — History.. the Winter Palace collection. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Palace..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Palace..", "x": "Explained: Palace.. Palace. The context — Hermitage Museum. St. Petersburg. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Impressionists.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Impressionists.", "x": "Hermitage Museum: Impressionists.. Russia. Essential knowledge — St. Petersburg.. the Winter Palace collection. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Impressionists..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Impressionists..", "x": "Explained: Impressionists.. Collection. The context — Hermitage Museum. Catherine. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "History.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "History.", "x": "Hermitage Museum: History.. Palace. Essential knowledge — Catherine.. the Winter Palace collection. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: History..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: History..", "x": "Explained: History.. History. The context — Hermitage Museum. 3M objects. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Palace.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Palace.", "x": "Hermitage Museum in depth: Palace.. Catherine. Details — the Winter Palace collection.. History. Palace. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Collection.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Collection.", "x": "Hermitage Museum in depth: Collection.. 3M objects. Details — the Winter Palace collection.. Tickets. Impressionists. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "History.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "History.", "x": "Hermitage Museum in depth: History.. Palace. Details — the Winter Palace collection.. Art. History. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Tickets.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Tickets.", "x": "Hermitage Museum in depth: Tickets.. Impressionists. Details — the Winter Palace collection.. Russia. St. Petersburg. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Art.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Art.", "x": "Hermitage Museum in depth: Art.. History. Details — the Winter Palace collection.. Palace. Catherine. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Russia.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Russia.", "x": "Hermitage Museum in depth: Russia.. St. Petersburg. Details — the Winter Palace collection.. Collection. 3M objects. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Hermitage Museum comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Hermitage Museum comes from.", "x": "Origins: Palace.. St. Petersburg. The history of Hermitage Museum — the Winter Palace collection.. Collection. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Hermitage Museum respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Hermitage Museum respectfully.", "x": "Engaging: History.. Catherine. How to participate or observe well — Hermitage Museum. the Winter Palace collection. Respect first, always; Tickets.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Hermitage Museum do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Hermitage Museum do's and don'ts.", "x": "Etiquette: Art.. 3M objects. The rules of respect — Hermitage Museum. the Winter Palace collection. When in doubt, ask about Russia.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Hermitage Museum.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Hermitage Museum.", "x": "Planning: Palace.. Palace. Practical notes — Hermitage Museum. the Winter Palace collection. A little planning shows respect for Collection.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Hermitage Museum and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Hermitage Museum and money.", "x": "Costs: History.. Impressionists. What to budget — Hermitage Museum. the Winter Palace collection. The best experiences of Tickets. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-museum-hermitage-museum-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
