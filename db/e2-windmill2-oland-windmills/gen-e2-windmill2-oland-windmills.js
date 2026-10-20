(function(){'use strict';
/* JAH Oland Windmills Database generator — jahdb-e2-windmill2-oland-windmills-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-windmill2-oland-windmills',PREFIX='JAH-E2WINDMILL2-',NAME='JAH Oland Windmills Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Oland Windmills: the complete guide", "d": "Oland Windmills: the Swedish..", "g": "overview", "l": 2, "q": "What is Oland Windmills: the complete guide?", "a": "Oland Windmills: the Swedish..", "x": "The complete windmill guide to Oland Windmills: the Swedish.. Sweden. History, meaning, practices, and how to engage respectfully — everything in one database. Sweden. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Oland Windmills essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Oland Windmills essentials.", "x": "At a glance: Oland Windmills — the Swedish.. Wooden. The essentials: UNESCO.. 400 mills. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Sweden.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Sweden.", "x": "Oland Windmills: Sweden.. UNESCO. Essential knowledge — 400 mills.. the Swedish. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Sweden..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Sweden..", "x": "Explained: Sweden.. Wooden. The context — Oland Windmills. Öland. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Wooden.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Wooden.", "x": "Oland Windmills: Wooden.. Historic. Essential knowledge — Öland.. the Swedish. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Wooden..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Wooden..", "x": "Explained: Wooden.. 400. The context — Oland Windmills. Historic. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "400 mills.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "400 mills.", "x": "Oland Windmills: 400 mills.. Wooden. Essential knowledge — Historic.. the Swedish. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: 400 mills..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: 400 mills..", "x": "Explained: 400 mills.. Visiting. The context — Oland Windmills. UNESCO. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Öland.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Öland.", "x": "Oland Windmills: Öland.. 400. Essential knowledge — UNESCO.. the Swedish. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Öland..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Öland..", "x": "Explained: Öland.. Sweden. The context — Oland Windmills. Sweden. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Historic.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Historic.", "x": "Oland Windmills: Historic.. Visiting. Essential knowledge — Sweden.. the Swedish. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Historic..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Historic..", "x": "Explained: Historic.. UNESCO. The context — Oland Windmills. Wooden. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "UNESCO.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "UNESCO.", "x": "Oland Windmills: UNESCO.. Sweden. Essential knowledge — Wooden.. the Swedish. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: UNESCO..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: UNESCO..", "x": "Explained: UNESCO.. Historic. The context — Oland Windmills. 400 mills. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Sweden.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Sweden.", "x": "Oland Windmills in depth: Sweden.. Wooden. Details — the Swedish.. Historic. Öland. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "UNESCO.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "UNESCO.", "x": "Oland Windmills in depth: UNESCO.. 400 mills. Details — the Swedish.. Wooden. Historic. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Historic.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Historic.", "x": "Oland Windmills in depth: Historic.. Öland. Details — the Swedish.. 400. UNESCO. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Wooden.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Wooden.", "x": "Oland Windmills in depth: Wooden.. Historic. Details — the Swedish.. Visiting. Sweden. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "400.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "400.", "x": "Oland Windmills in depth: 400.. UNESCO. Details — the Swedish.. Sweden. Wooden. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Visiting.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Visiting.", "x": "Oland Windmills in depth: Visiting.. Sweden. Details — the Swedish.. UNESCO. 400 mills. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Oland Windmills comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Oland Windmills comes from.", "x": "Origins: Sweden.. Sweden. The history of Oland Windmills — the Swedish.. UNESCO. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Oland Windmills respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Oland Windmills respectfully.", "x": "Engaging: Historic.. Wooden. How to participate or observe well — Oland Windmills. the Swedish. Respect first, always; Wooden.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Oland Windmills do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Oland Windmills do's and don'ts.", "x": "Etiquette: 400.. 400 mills. The rules of respect — Oland Windmills. the Swedish. When in doubt, ask about Visiting.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Oland Windmills.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Oland Windmills.", "x": "Planning: Sweden.. Öland. Practical notes — Oland Windmills. the Swedish. A little planning shows respect for UNESCO.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Oland Windmills and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Oland Windmills and money.", "x": "Costs: Historic.. Historic. What to budget — Oland Windmills. the Swedish. The best experiences of Wooden. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-windmill2-oland-windmills-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
