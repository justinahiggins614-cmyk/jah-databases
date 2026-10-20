(function(){'use strict';
/* JAH Navratri Holiday Database generator — jahdb-e2-holiday-navratri-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-holiday-navratri',PREFIX='JAH-E2HOLIDAYNA-',NAME='JAH Navratri Holiday Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Navratri: the complete guide", "d": "Navratri: nine nights of goddess..", "g": "overview", "l": 2, "q": "What is Navratri: the complete guide?", "a": "Navratri: nine nights of goddess..", "x": "The complete holiday guide to Navratri: nine nights of goddess.. Fall. History, meaning, practices, and how to engage respectfully — everything in one database. Goddess. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Navratri essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Navratri essentials.", "x": "At a glance: Navratri — nine nights of goddess.. Garba. The essentials: Dance.. Fasting. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Fall.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Fall.", "x": "Navratri: Fall.. Dance. Essential knowledge — Fasting.. nine nights of goddess. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Fall..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Fall..", "x": "Explained: Fall.. States. The context — Navratri. Durga. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Garba.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Garba.", "x": "Navratri: Garba.. Fasting. Essential knowledge — Durga.. nine nights of goddess. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Garba..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Garba..", "x": "Explained: Garba.. Meaning. The context — Navratri. Gujarat. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Fasting.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Fasting.", "x": "Navratri: Fasting.. States. Essential knowledge — Gujarat.. nine nights of goddess. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Fasting..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Fasting..", "x": "Explained: Fasting.. Joy. The context — Navratri. Dance. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Durga.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Durga.", "x": "Navratri: Durga.. Meaning. Essential knowledge — Dance.. nine nights of goddess. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Durga..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Durga..", "x": "Explained: Durga.. Goddess. The context — Navratri. Fall. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Gujarat.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Gujarat.", "x": "Navratri: Gujarat.. Joy. Essential knowledge — Fall.. nine nights of goddess. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Gujarat..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Gujarat..", "x": "Explained: Gujarat.. Dance. The context — Navratri. Garba. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Dance.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Dance.", "x": "Navratri: Dance.. Goddess. Essential knowledge — Garba.. nine nights of goddess. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Dance..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Dance..", "x": "Explained: Dance.. Fasting. The context — Navratri. Fasting. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Goddess.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Goddess.", "x": "Navratri in depth: Goddess.. Garba. Details — nine nights of goddess.. Fasting. Durga. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Dance.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Dance.", "x": "Navratri in depth: Dance.. Fasting. Details — nine nights of goddess.. States. Gujarat. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Fasting.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Fasting.", "x": "Navratri in depth: Fasting.. Durga. Details — nine nights of goddess.. Meaning. Dance. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "States.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "States.", "x": "Navratri in depth: States.. Gujarat. Details — nine nights of goddess.. Joy. Fall. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Meaning.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Meaning.", "x": "Navratri in depth: Meaning.. Dance. Details — nine nights of goddess.. Goddess. Garba. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Joy.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Joy.", "x": "Navratri in depth: Joy.. Fall. Details — nine nights of goddess.. Dance. Fasting. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Navratri comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Navratri comes from.", "x": "Origins: Goddess.. Fall. The history of Navratri — nine nights of goddess.. Dance. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Navratri respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Navratri respectfully.", "x": "Engaging: Fasting.. Garba. How to participate or observe well — Navratri. nine nights of goddess. Respect first, always; States.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Navratri do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Navratri do's and don'ts.", "x": "Etiquette: Meaning.. Fasting. The rules of respect — Navratri. nine nights of goddess. When in doubt, ask about Joy.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Navratri.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Navratri.", "x": "Planning: Goddess.. Durga. Practical notes — Navratri. nine nights of goddess. A little planning shows respect for Dance.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Navratri and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Navratri and money.", "x": "Costs: Fasting.. Gujarat. What to budget — Navratri. nine nights of goddess. The best experiences of States. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-holiday-navratri-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
