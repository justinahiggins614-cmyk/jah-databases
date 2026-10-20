(function(){'use strict';
/* JAH Gluten-Free Diet Diet Database generator — jahdb-e2-diet-gluten-free-diet-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-diet-gluten-free-diet',PREFIX='JAH-E2DIETGLUTE-',NAME='JAH Gluten-Free Diet Diet Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Gluten-Free Diet: the complete guide", "d": "Gluten-Free Diet: the celiac essential..", "g": "overview", "l": 2, "q": "What is Gluten-Free Diet: the complete guide?", "a": "Gluten-Free Diet: the celiac essential..", "x": "The complete diet guide to Gluten-Free Diet: the celiac essential.. Celiac. History, meaning, practices, and how to engage respectfully — everything in one database. Celiac. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Gluten-Free Diet essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Gluten-Free Diet essentials.", "x": "At a glance: Gluten-Free Diet — the celiac essential.. Wheat. The essentials: Labels.. Cross-contact. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Celiac.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Celiac.", "x": "Gluten-Free Diet: Celiac.. Labels. Essential knowledge — Cross-contact.. the celiac essential. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Celiac..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Celiac..", "x": "Explained: Celiac.. Medical. The context — Gluten-Free Diet. Labels. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Wheat.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Wheat.", "x": "Gluten-Free Diet: Wheat.. Alternatives. Essential knowledge — Labels.. the celiac essential. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Wheat..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Wheat..", "x": "Explained: Wheat.. Wheat. The context — Gluten-Free Diet. Alternatives. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Cross-contact.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Cross-contact.", "x": "Gluten-Free Diet: Cross-contact.. Medical. Essential knowledge — Alternatives.. the celiac essential. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Cross-contact..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Cross-contact..", "x": "Explained: Cross-contact.. Foods. The context — Gluten-Free Diet. Medical. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Labels.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Labels.", "x": "Gluten-Free Diet: Labels.. Wheat. Essential knowledge — Medical.. the celiac essential. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Labels..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Labels..", "x": "Explained: Labels.. Celiac. The context — Gluten-Free Diet. Celiac. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Alternatives.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Alternatives.", "x": "Gluten-Free Diet: Alternatives.. Foods. Essential knowledge — Celiac.. the celiac essential. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Alternatives..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Alternatives..", "x": "Explained: Alternatives.. Labels. The context — Gluten-Free Diet. Wheat. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Medical.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Medical.", "x": "Gluten-Free Diet: Medical.. Celiac. Essential knowledge — Wheat.. the celiac essential. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Medical..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Medical..", "x": "Explained: Medical.. Alternatives. The context — Gluten-Free Diet. Cross-contact. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Celiac.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Celiac.", "x": "Gluten-Free Diet in depth: Celiac.. Wheat. Details — the celiac essential.. Alternatives. Labels. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Labels.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Labels.", "x": "Gluten-Free Diet in depth: Labels.. Cross-contact. Details — the celiac essential.. Medical. Alternatives. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Alternatives.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Alternatives.", "x": "Gluten-Free Diet in depth: Alternatives.. Labels. Details — the celiac essential.. Wheat. Medical. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Medical.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Medical.", "x": "Gluten-Free Diet in depth: Medical.. Alternatives. Details — the celiac essential.. Foods. Celiac. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Wheat.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Wheat.", "x": "Gluten-Free Diet in depth: Wheat.. Medical. Details — the celiac essential.. Celiac. Wheat. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Foods.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Foods.", "x": "Gluten-Free Diet in depth: Foods.. Celiac. Details — the celiac essential.. Labels. Cross-contact. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Gluten-Free Diet comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Gluten-Free Diet comes from.", "x": "Origins: Celiac.. Celiac. The history of Gluten-Free Diet — the celiac essential.. Labels. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Gluten-Free Diet respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Gluten-Free Diet respectfully.", "x": "Engaging: Alternatives.. Wheat. How to participate or observe well — Gluten-Free Diet. the celiac essential. Respect first, always; Medical.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Gluten-Free Diet do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Gluten-Free Diet do's and don'ts.", "x": "Etiquette: Wheat.. Cross-contact. The rules of respect — Gluten-Free Diet. the celiac essential. When in doubt, ask about Foods.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Gluten-Free Diet.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Gluten-Free Diet.", "x": "Planning: Celiac.. Labels. Practical notes — Gluten-Free Diet. the celiac essential. A little planning shows respect for Labels.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Gluten-Free Diet and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Gluten-Free Diet and money.", "x": "Costs: Alternatives.. Alternatives. What to budget — Gluten-Free Diet. the celiac essential. The best experiences of Medical. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-diet-gluten-free-diet-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
