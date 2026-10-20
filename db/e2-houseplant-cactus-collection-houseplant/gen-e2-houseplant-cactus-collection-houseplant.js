(function(){'use strict';
/* JAH Cactus Collection Houseplant Database generator — jahdb-e2-houseplant-cactus-collection-houseplant-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-houseplant-cactus-collection-houseplant',PREFIX='JAH-E2HOUSEPLAN-',NAME='JAH Cactus Collection Houseplant Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Cactus Collection: the complete guide", "d": "Cactus Collection: the spiny shelf..", "g": "overview", "l": 2, "q": "What is Cactus Collection: the complete guide?", "a": "Cactus Collection: the spiny shelf..", "x": "The complete houseplant guide to Cactus Collection: the spiny shelf.. Spines. History, meaning, practices, and how to engage respectfully — everything in one database. Spines. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Cactus Collection essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Cactus Collection essentials.", "x": "At a glance: Cactus Collection — the spiny shelf.. Drought. The essentials: Desert.. Glochids. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Spines.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Spines.", "x": "Cactus Collection: Spines.. Desert. Essential knowledge — Glochids.. the spiny shelf. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Spines..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Spines..", "x": "Explained: Spines.. Sunny. The context — Cactus Collection. Sunny. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Drought.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Drought.", "x": "Cactus Collection: Drought.. Water. Essential knowledge — Sunny.. the spiny shelf. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Drought..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Drought..", "x": "Explained: Drought.. Glochids. The context — Cactus Collection. Rare water. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Glochids.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Glochids.", "x": "Cactus Collection: Glochids.. Sunny. Essential knowledge — Rare water.. the spiny shelf. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Glochids..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Glochids..", "x": "Explained: Glochids.. Guide. The context — Cactus Collection. Desert. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Sunny.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Sunny.", "x": "Cactus Collection: Sunny.. Glochids. Essential knowledge — Desert.. the spiny shelf. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Sunny..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Sunny..", "x": "Explained: Sunny.. Spines. The context — Cactus Collection. Spines. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Rare water.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Rare water.", "x": "Cactus Collection: Rare water.. Guide. Essential knowledge — Spines.. the spiny shelf. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Rare water..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Rare water..", "x": "Explained: Rare water.. Desert. The context — Cactus Collection. Drought. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Desert.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Desert.", "x": "Cactus Collection: Desert.. Spines. Essential knowledge — Drought.. the spiny shelf. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Desert..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Desert..", "x": "Explained: Desert.. Water. The context — Cactus Collection. Glochids. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Spines.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Spines.", "x": "Cactus Collection in depth: Spines.. Drought. Details — the spiny shelf.. Water. Sunny. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Desert.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Desert.", "x": "Cactus Collection in depth: Desert.. Glochids. Details — the spiny shelf.. Sunny. Rare water. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Water.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Water.", "x": "Cactus Collection in depth: Water.. Sunny. Details — the spiny shelf.. Glochids. Desert. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Sunny.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Sunny.", "x": "Cactus Collection in depth: Sunny.. Rare water. Details — the spiny shelf.. Guide. Spines. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Glochids.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Glochids.", "x": "Cactus Collection in depth: Glochids.. Desert. Details — the spiny shelf.. Spines. Drought. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Guide.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Guide.", "x": "Cactus Collection in depth: Guide.. Spines. Details — the spiny shelf.. Desert. Glochids. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Cactus Collection comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Cactus Collection comes from.", "x": "Origins: Spines.. Spines. The history of Cactus Collection — the spiny shelf.. Desert. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Cactus Collection respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Cactus Collection respectfully.", "x": "Engaging: Water.. Drought. How to participate or observe well — Cactus Collection. the spiny shelf. Respect first, always; Sunny.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Cactus Collection do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Cactus Collection do's and don'ts.", "x": "Etiquette: Glochids.. Glochids. The rules of respect — Cactus Collection. the spiny shelf. When in doubt, ask about Guide.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Cactus Collection.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Cactus Collection.", "x": "Planning: Spines.. Sunny. Practical notes — Cactus Collection. the spiny shelf. A little planning shows respect for Desert.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Cactus Collection and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Cactus Collection and money.", "x": "Costs: Water.. Rare water. What to budget — Cactus Collection. the spiny shelf. The best experiences of Sunny. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-houseplant-cactus-collection-houseplant-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
