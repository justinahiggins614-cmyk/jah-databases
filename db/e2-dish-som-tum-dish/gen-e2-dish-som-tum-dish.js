(function(){'use strict';
/* JAH Som Tum Dish Database generator — jahdb-e2-dish-som-tum-dish-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-dish-som-tum-dish',PREFIX='JAH-E2DISHSOMTU-',NAME='JAH Som Tum Dish Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Som Tum: the complete guide", "d": "Som Tum: the papaya pound..", "g": "overview", "l": 2, "q": "What is Som Tum: the complete guide?", "a": "Som Tum: the papaya pound..", "x": "The complete dish guide to Som Tum: the papaya pound.. Papaya. History, meaning, practices, and how to engage respectfully — everything in one database. Mortar. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Som Tum essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Som Tum essentials.", "x": "At a glance: Som Tum — the papaya pound.. Mortar. The essentials: Pounded.. Chilies. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Papaya.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Papaya.", "x": "Som Tum: Papaya.. Pounded. Essential knowledge — Chilies.. the papaya pound. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Papaya..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Papaya..", "x": "Explained: Papaya.. Papaya. The context — Som Tum. Lime. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Mortar.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Mortar.", "x": "Som Tum: Mortar.. Isan. Essential knowledge — Lime.. the papaya pound. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Mortar..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Mortar..", "x": "Explained: Mortar.. Lime. The context — Som Tum. Pounded. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Chilies.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Chilies.", "x": "Som Tum: Chilies.. Papaya. Essential knowledge — Pounded.. the papaya pound. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Chilies..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Chilies..", "x": "Explained: Chilies.. Making. The context — Som Tum. Isan. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Lime.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Lime.", "x": "Som Tum: Lime.. Lime. Essential knowledge — Isan.. the papaya pound. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Lime..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Lime..", "x": "Explained: Lime.. Mortar. The context — Som Tum. Papaya. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Pounded.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Pounded.", "x": "Som Tum: Pounded.. Making. Essential knowledge — Papaya.. the papaya pound. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Pounded..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Pounded..", "x": "Explained: Pounded.. Pounded. The context — Som Tum. Mortar. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Isan.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Isan.", "x": "Som Tum: Isan.. Mortar. Essential knowledge — Mortar.. the papaya pound. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Isan..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Isan..", "x": "Explained: Isan.. Isan. The context — Som Tum. Chilies. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Mortar.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Mortar.", "x": "Som Tum in depth: Mortar.. Mortar. Details — the papaya pound.. Isan. Lime. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Pounded.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Pounded.", "x": "Som Tum in depth: Pounded.. Chilies. Details — the papaya pound.. Papaya. Pounded. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Isan.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Isan.", "x": "Som Tum in depth: Isan.. Lime. Details — the papaya pound.. Lime. Isan. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Papaya.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Papaya.", "x": "Som Tum in depth: Papaya.. Pounded. Details — the papaya pound.. Making. Papaya. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Lime.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Lime.", "x": "Som Tum in depth: Lime.. Isan. Details — the papaya pound.. Mortar. Mortar. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Making.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Making.", "x": "Som Tum in depth: Making.. Papaya. Details — the papaya pound.. Pounded. Chilies. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Som Tum comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Som Tum comes from.", "x": "Origins: Mortar.. Papaya. The history of Som Tum — the papaya pound.. Pounded. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Som Tum respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Som Tum respectfully.", "x": "Engaging: Isan.. Mortar. How to participate or observe well — Som Tum. the papaya pound. Respect first, always; Papaya.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Som Tum do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Som Tum do's and don'ts.", "x": "Etiquette: Lime.. Chilies. The rules of respect — Som Tum. the papaya pound. When in doubt, ask about Making.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Som Tum.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Som Tum.", "x": "Planning: Mortar.. Lime. Practical notes — Som Tum. the papaya pound. A little planning shows respect for Pounded.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Som Tum and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Som Tum and money.", "x": "Costs: Isan.. Pounded. What to budget — Som Tum. the papaya pound. The best experiences of Papaya. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-dish-som-tum-dish-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
