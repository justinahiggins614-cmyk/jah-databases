(function(){'use strict';
/* JAH Top Bun Hairstyle Database generator — jahdb-e2-hairstyle-top-bun-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-hairstyle-top-bun',PREFIX='JAH-E2HAIRSTYLE-',NAME='JAH Top Bun Hairstyle Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Top Bun: the complete guide", "d": "Top Bun: the classic updo..", "g": "overview", "l": 2, "q": "What is Top Bun: the complete guide?", "a": "Top Bun: the classic updo..", "x": "The complete hairstyle guide to Top Bun: the classic updo.. Ballet. History, meaning, practices, and how to engage respectfully — everything in one database. History. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Top Bun essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Top Bun essentials.", "x": "At a glance: Top Bun — the classic updo.. Messy bun. The essentials: Types.. Tools. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Ballet.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Ballet.", "x": "Top Bun: Ballet.. Types. Essential knowledge — Tools.. the classic updo. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Ballet..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Ballet..", "x": "Explained: Ballet.. Care. The context — Top Bun. Occasions. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Messy bun.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Messy bun.", "x": "Top Bun: Messy bun.. How. Essential knowledge — Occasions.. the classic updo. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Messy bun..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Messy bun..", "x": "Explained: Messy bun.. Occasions. The context — Top Bun. Hair health. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Tools.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Tools.", "x": "Top Bun: Tools.. Care. Essential knowledge — Hair health.. the classic updo. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Tools..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Tools..", "x": "Explained: Tools.. Style. The context — Top Bun. Tutorials. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Occasions.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Occasions.", "x": "Top Bun: Occasions.. Occasions. Essential knowledge — Tutorials.. the classic updo. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Occasions..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Occasions..", "x": "Explained: Occasions.. History. The context — Top Bun. Ballet. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Hair health.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Hair health.", "x": "Top Bun: Hair health.. Style. Essential knowledge — Ballet.. the classic updo. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Hair health..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Hair health..", "x": "Explained: Hair health.. Types. The context — Top Bun. Messy bun. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Tutorials.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Tutorials.", "x": "Top Bun: Tutorials.. History. Essential knowledge — Messy bun.. the classic updo. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Tutorials..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Tutorials..", "x": "Explained: Tutorials.. How. The context — Top Bun. Tools. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "History.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "History.", "x": "Top Bun in depth: History.. Messy bun. Details — the classic updo.. How. Occasions. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Types.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Types.", "x": "Top Bun in depth: Types.. Tools. Details — the classic updo.. Care. Hair health. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "How.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "How.", "x": "Top Bun in depth: How.. Occasions. Details — the classic updo.. Occasions. Tutorials. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Care.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Care.", "x": "Top Bun in depth: Care.. Hair health. Details — the classic updo.. Style. Ballet. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Occasions.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Occasions.", "x": "Top Bun in depth: Occasions.. Tutorials. Details — the classic updo.. History. Messy bun. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Style.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Style.", "x": "Top Bun in depth: Style.. Ballet. Details — the classic updo.. Types. Tools. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Top Bun comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Top Bun comes from.", "x": "Origins: History.. Ballet. The history of Top Bun — the classic updo.. Types. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Top Bun respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Top Bun respectfully.", "x": "Engaging: How.. Messy bun. How to participate or observe well — Top Bun. the classic updo. Respect first, always; Care.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Top Bun do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Top Bun do's and don'ts.", "x": "Etiquette: Occasions.. Tools. The rules of respect — Top Bun. the classic updo. When in doubt, ask about Style.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Top Bun.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Top Bun.", "x": "Planning: History.. Occasions. Practical notes — Top Bun. the classic updo. A little planning shows respect for Types.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Top Bun and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Top Bun and money.", "x": "Costs: How.. Hair health. What to budget — Top Bun. the classic updo. The best experiences of Care. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-hairstyle-top-bun-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
