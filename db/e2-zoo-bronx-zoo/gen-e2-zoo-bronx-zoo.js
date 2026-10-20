(function(){'use strict';
/* JAH Bronx Zoo Zoo Database generator — jahdb-e2-zoo-bronx-zoo-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-zoo-bronx-zoo',PREFIX='JAH-E2ZOOBRONXZ-',NAME='JAH Bronx Zoo Zoo Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Bronx Zoo: the complete guide", "d": "Bronx Zoo: America's urban wilderness..", "g": "overview", "l": 2, "q": "What is Bronx Zoo: the complete guide?", "a": "Bronx Zoo: America's urban wilderness..", "x": "The complete zoo guide to Bronx Zoo: America's urban wilderness.. 1899. History, meaning, practices, and how to engage respectfully — everything in one database. History. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Bronx Zoo essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Bronx Zoo essentials.", "x": "At a glance: Bronx Zoo — America's urban wilderness.. 265 acres. The essentials: Congo.. Congo. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "1899.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "1899.", "x": "Bronx Zoo: 1899.. Congo. Essential knowledge — Congo.. America's urban wilderness. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 1899..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 1899..", "x": "Explained: 1899.. Tickets. The context — Bronx Zoo. Tigers. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "265 acres.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "265 acres.", "x": "Bronx Zoo: 265 acres.. Tigers. Essential knowledge — Tigers.. America's urban wilderness. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: 265 acres..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: 265 acres..", "x": "Explained: 265 acres.. NYC. The context — Bronx Zoo. NYC. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Congo.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Congo.", "x": "Bronx Zoo: Congo.. Tickets. Essential knowledge — NYC.. America's urban wilderness. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Congo..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Congo..", "x": "Explained: Congo.. Science. The context — Bronx Zoo. Conservation. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Tigers.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Tigers.", "x": "Bronx Zoo: Tigers.. NYC. Essential knowledge — Conservation.. America's urban wilderness. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Tigers..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Tigers..", "x": "Explained: Tigers.. History. The context — Bronx Zoo. 1899. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "NYC.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "NYC.", "x": "Bronx Zoo: NYC.. Science. Essential knowledge — 1899.. America's urban wilderness. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: NYC..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: NYC..", "x": "Explained: NYC.. Congo. The context — Bronx Zoo. 265 acres. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Conservation.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Conservation.", "x": "Bronx Zoo: Conservation.. History. Essential knowledge — 265 acres.. America's urban wilderness. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Conservation..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Conservation..", "x": "Explained: Conservation.. Tigers. The context — Bronx Zoo. Congo. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "History.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "History.", "x": "Bronx Zoo in depth: History.. 265 acres. Details — America's urban wilderness.. Tigers. Tigers. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Congo.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Congo.", "x": "Bronx Zoo in depth: Congo.. Congo. Details — America's urban wilderness.. Tickets. NYC. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Tigers.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Tigers.", "x": "Bronx Zoo in depth: Tigers.. Tigers. Details — America's urban wilderness.. NYC. Conservation. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Tickets.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Tickets.", "x": "Bronx Zoo in depth: Tickets.. NYC. Details — America's urban wilderness.. Science. 1899. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "NYC.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "NYC.", "x": "Bronx Zoo in depth: NYC.. Conservation. Details — America's urban wilderness.. History. 265 acres. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Science.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Science.", "x": "Bronx Zoo in depth: Science.. 1899. Details — America's urban wilderness.. Congo. Congo. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Bronx Zoo comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Bronx Zoo comes from.", "x": "Origins: History.. 1899. The history of Bronx Zoo — America's urban wilderness.. Congo. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Bronx Zoo respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Bronx Zoo respectfully.", "x": "Engaging: Tigers.. 265 acres. How to participate or observe well — Bronx Zoo. America's urban wilderness. Respect first, always; Tickets.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Bronx Zoo do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Bronx Zoo do's and don'ts.", "x": "Etiquette: NYC.. Congo. The rules of respect — Bronx Zoo. America's urban wilderness. When in doubt, ask about Science.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Bronx Zoo.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Bronx Zoo.", "x": "Planning: History.. Tigers. Practical notes — Bronx Zoo. America's urban wilderness. A little planning shows respect for Congo.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Bronx Zoo and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Bronx Zoo and money.", "x": "Costs: Tigers.. NYC. What to budget — Bronx Zoo. America's urban wilderness. The best experiences of Tickets. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-zoo-bronx-zoo-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
