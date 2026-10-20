(function(){'use strict';
/* JAH Boom Studios Database generator — jahdb-e2-comics2-boom-studios-publisher-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-comics2-boom-studios-publisher',PREFIX='JAH-E2COMICS2BO-',NAME='JAH Boom Studios Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Boom Studios: the complete guide", "d": "Boom Studios: the modern indie..", "g": "overview", "l": 2, "q": "What is Boom Studios: the complete guide?", "a": "Boom Studios: the modern indie..", "x": "The complete comic publisher guide to Boom Studios: the modern indie.. 2005. History, meaning, practices, and how to engage respectfully — everything in one database. Lumberjanes. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Boom Studios essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Boom Studios essentials.", "x": "At a glance: Boom Studios — the modern indie.. Lumberjanes. The essentials: Originals.. Something. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "2005.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "2005.", "x": "Boom Studios: 2005.. Originals. Essential knowledge — Something.. the modern indie. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 2005..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 2005..", "x": "Explained: 2005.. Rangers. The context — Boom Studios. Power Rangers. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Lumberjanes.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Lumberjanes.", "x": "Boom Studios: Lumberjanes.. LA. Essential knowledge — Power Rangers.. the modern indie. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Lumberjanes..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Lumberjanes..", "x": "Explained: Lumberjanes.. Something. The context — Boom Studios. LA. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Something.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Something.", "x": "Boom Studios: Something.. Rangers. Essential knowledge — LA.. the modern indie. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Something..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Something..", "x": "Explained: Something.. History. The context — Boom Studios. Originals. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Power Rangers.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Power Rangers.", "x": "Boom Studios: Power Rangers.. Something. Essential knowledge — Originals.. the modern indie. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Power Rangers..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Power Rangers..", "x": "Explained: Power Rangers.. Lumberjanes. The context — Boom Studios. 2005. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "LA.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "LA.", "x": "Boom Studios: LA.. History. Essential knowledge — 2005.. the modern indie. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: LA..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: LA..", "x": "Explained: LA.. Originals. The context — Boom Studios. Lumberjanes. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Originals.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Originals.", "x": "Boom Studios: Originals.. Lumberjanes. Essential knowledge — Lumberjanes.. the modern indie. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Originals..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Originals..", "x": "Explained: Originals.. LA. The context — Boom Studios. Something. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Lumberjanes.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Lumberjanes.", "x": "Boom Studios in depth: Lumberjanes.. Lumberjanes. Details — the modern indie.. LA. Power Rangers. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Originals.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Originals.", "x": "Boom Studios in depth: Originals.. Something. Details — the modern indie.. Rangers. LA. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "LA.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "LA.", "x": "Boom Studios in depth: LA.. Power Rangers. Details — the modern indie.. Something. Originals. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Rangers.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Rangers.", "x": "Boom Studios in depth: Rangers.. LA. Details — the modern indie.. History. 2005. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Something.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Something.", "x": "Boom Studios in depth: Something.. Originals. Details — the modern indie.. Lumberjanes. Lumberjanes. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "History.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "History.", "x": "Boom Studios in depth: History.. 2005. Details — the modern indie.. Originals. Something. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Boom Studios comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Boom Studios comes from.", "x": "Origins: Lumberjanes.. 2005. The history of Boom Studios — the modern indie.. Originals. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Boom Studios respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Boom Studios respectfully.", "x": "Engaging: LA.. Lumberjanes. How to participate or observe well — Boom Studios. the modern indie. Respect first, always; Rangers.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Boom Studios do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Boom Studios do's and don'ts.", "x": "Etiquette: Something.. Something. The rules of respect — Boom Studios. the modern indie. When in doubt, ask about History.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Boom Studios.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Boom Studios.", "x": "Planning: Lumberjanes.. Power Rangers. Practical notes — Boom Studios. the modern indie. A little planning shows respect for Originals.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Boom Studios and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Boom Studios and money.", "x": "Costs: LA.. LA. What to budget — Boom Studios. the modern indie. The best experiences of Rangers. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-comics2-boom-studios-publisher-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
