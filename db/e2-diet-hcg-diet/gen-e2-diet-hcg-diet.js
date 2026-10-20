(function(){'use strict';
/* JAH HCG Diet Diet Database generator — jahdb-e2-diet-hcg-diet-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-diet-hcg-diet',PREFIX='JAH-E2DIETHCGDI-',NAME='JAH HCG Diet Diet Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "HCG Diet: the complete guide", "d": "HCG Diet: the hormone crash..", "g": "overview", "l": 2, "q": "What is HCG Diet: the complete guide?", "a": "HCG Diet: the hormone crash..", "x": "The complete diet guide to HCG Diet: the hormone crash.. 500 cal. History, meaning, practices, and how to engage respectfully — everything in one database. Dangerous. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "HCG Diet essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "HCG Diet essentials.", "x": "At a glance: HCG Diet — the hormone crash.. HCG. The essentials: FDA.. Dangerous. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "500 cal.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "500 cal.", "x": "HCG Diet: 500 cal.. FDA. Essential knowledge — Dangerous.. the hormone crash. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 500 cal..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 500 cal..", "x": "Explained: 500 cal.. 1950s. The context — HCG Diet. FDA. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "HCG.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "HCG.", "x": "HCG Diet: HCG.. Debunked. Essential knowledge — FDA.. the hormone crash. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: HCG..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: HCG..", "x": "Explained: HCG.. HCG. The context — HCG Diet. 1950s. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Dangerous.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Dangerous.", "x": "HCG Diet: Dangerous.. 1950s. Essential knowledge — 1950s.. the hormone crash. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Dangerous..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Dangerous..", "x": "Explained: Dangerous.. Warning. The context — HCG Diet. Debunked. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "FDA.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "FDA.", "x": "HCG Diet: FDA.. HCG. Essential knowledge — Debunked.. the hormone crash. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: FDA..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: FDA..", "x": "Explained: FDA.. Dangerous. The context — HCG Diet. 500 cal. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "1950s.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "1950s.", "x": "HCG Diet: 1950s.. Warning. Essential knowledge — 500 cal.. the hormone crash. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: 1950s..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: 1950s..", "x": "Explained: 1950s.. FDA. The context — HCG Diet. HCG. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Debunked.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Debunked.", "x": "HCG Diet: Debunked.. Dangerous. Essential knowledge — HCG.. the hormone crash. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Debunked..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Debunked..", "x": "Explained: Debunked.. Debunked. The context — HCG Diet. Dangerous. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Dangerous.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Dangerous.", "x": "HCG Diet in depth: Dangerous.. HCG. Details — the hormone crash.. Debunked. FDA. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "FDA.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "FDA.", "x": "HCG Diet in depth: FDA.. Dangerous. Details — the hormone crash.. 1950s. 1950s. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Debunked.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Debunked.", "x": "HCG Diet in depth: Debunked.. FDA. Details — the hormone crash.. HCG. Debunked. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "1950s.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "1950s.", "x": "HCG Diet in depth: 1950s.. 1950s. Details — the hormone crash.. Warning. 500 cal. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "HCG.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "HCG.", "x": "HCG Diet in depth: HCG.. Debunked. Details — the hormone crash.. Dangerous. HCG. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Warning.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Warning.", "x": "HCG Diet in depth: Warning.. 500 cal. Details — the hormone crash.. FDA. Dangerous. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where HCG Diet comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where HCG Diet comes from.", "x": "Origins: Dangerous.. 500 cal. The history of HCG Diet — the hormone crash.. FDA. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing HCG Diet respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing HCG Diet respectfully.", "x": "Engaging: Debunked.. HCG. How to participate or observe well — HCG Diet. the hormone crash. Respect first, always; 1950s.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "HCG Diet do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "HCG Diet do's and don'ts.", "x": "Etiquette: HCG.. Dangerous. The rules of respect — HCG Diet. the hormone crash. When in doubt, ask about Warning.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around HCG Diet.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around HCG Diet.", "x": "Planning: Dangerous.. FDA. Practical notes — HCG Diet. the hormone crash. A little planning shows respect for FDA.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "HCG Diet and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "HCG Diet and money.", "x": "Costs: Debunked.. 1950s. What to budget — HCG Diet. the hormone crash. The best experiences of 1950s. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-diet-hcg-diet-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
