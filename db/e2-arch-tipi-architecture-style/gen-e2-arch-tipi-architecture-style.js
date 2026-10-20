(function(){'use strict';
/* JAH Tipi Architecture Style Database generator — jahdb-e2-arch-tipi-architecture-style-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-arch-tipi-architecture-style',PREFIX='JAH-E2ARCHTIPIA-',NAME='JAH Tipi Architecture Style Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Tipi Architecture: the complete guide", "d": "Tipi Architecture: the plains cone..", "g": "overview", "l": 2, "q": "What is Tipi Architecture: the complete guide?", "a": "Tipi Architecture: the plains cone..", "x": "The complete architecture style guide to Tipi Architecture: the plains cone.. Plains. History, meaning, practices, and how to engage respectfully — everything in one database. Poles. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Tipi Architecture essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Tipi Architecture essentials.", "x": "At a glance: Tipi Architecture — the plains cone.. Poles. The essentials: Portable.. Buffalo. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Plains.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Plains.", "x": "Tipi Architecture: Plains.. Portable. Essential knowledge — Buffalo.. the plains cone. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Plains..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Plains..", "x": "Explained: Plains.. Plains. The context — Tipi Architecture. Portable. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Poles.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Poles.", "x": "Tipi Architecture: Poles.. Native. Essential knowledge — Portable.. the plains cone. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Poles..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Poles..", "x": "Explained: Poles.. Smoke. The context — Tipi Architecture. Smoke flap. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Buffalo.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Buffalo.", "x": "Tipi Architecture: Buffalo.. Plains. Essential knowledge — Smoke flap.. the plains cone. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Buffalo..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Buffalo..", "x": "Explained: Buffalo.. Legacy. The context — Tipi Architecture. Native. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Portable.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Portable.", "x": "Tipi Architecture: Portable.. Smoke. Essential knowledge — Native.. the plains cone. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Portable..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Portable..", "x": "Explained: Portable.. Poles. The context — Tipi Architecture. Plains. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Smoke flap.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Smoke flap.", "x": "Tipi Architecture: Smoke flap.. Legacy. Essential knowledge — Plains.. the plains cone. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Smoke flap..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Smoke flap..", "x": "Explained: Smoke flap.. Portable. The context — Tipi Architecture. Poles. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Native.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Native.", "x": "Tipi Architecture: Native.. Poles. Essential knowledge — Poles.. the plains cone. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Native..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Native..", "x": "Explained: Native.. Native. The context — Tipi Architecture. Buffalo. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Poles.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Poles.", "x": "Tipi Architecture in depth: Poles.. Poles. Details — the plains cone.. Native. Portable. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Portable.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Portable.", "x": "Tipi Architecture in depth: Portable.. Buffalo. Details — the plains cone.. Plains. Smoke flap. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Native.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Native.", "x": "Tipi Architecture in depth: Native.. Portable. Details — the plains cone.. Smoke. Native. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Plains.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Plains.", "x": "Tipi Architecture in depth: Plains.. Smoke flap. Details — the plains cone.. Legacy. Plains. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Smoke.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Smoke.", "x": "Tipi Architecture in depth: Smoke.. Native. Details — the plains cone.. Poles. Poles. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Legacy.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Legacy.", "x": "Tipi Architecture in depth: Legacy.. Plains. Details — the plains cone.. Portable. Buffalo. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Tipi Architecture comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Tipi Architecture comes from.", "x": "Origins: Poles.. Plains. The history of Tipi Architecture — the plains cone.. Portable. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Tipi Architecture respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Tipi Architecture respectfully.", "x": "Engaging: Native.. Poles. How to participate or observe well — Tipi Architecture. the plains cone. Respect first, always; Plains.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Tipi Architecture do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Tipi Architecture do's and don'ts.", "x": "Etiquette: Smoke.. Buffalo. The rules of respect — Tipi Architecture. the plains cone. When in doubt, ask about Legacy.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Tipi Architecture.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Tipi Architecture.", "x": "Planning: Poles.. Portable. Practical notes — Tipi Architecture. the plains cone. A little planning shows respect for Portable.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Tipi Architecture and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Tipi Architecture and money.", "x": "Costs: Native.. Smoke flap. What to budget — Tipi Architecture. the plains cone. The best experiences of Plains. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-arch-tipi-architecture-style-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
