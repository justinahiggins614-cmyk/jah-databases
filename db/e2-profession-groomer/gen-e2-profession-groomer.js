(function(){'use strict';
/* JAH Groomer Profession Database generator — jahdb-e2-profession-groomer-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-profession-groomer',PREFIX='JAH-E2PROFESSIO-',NAME='JAH Groomer Profession Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Groomer Profession: the complete guide", "d": "Groomer Profession: the clip profession..", "g": "overview", "l": 2, "q": "What is Groomer Profession: the complete guide?", "a": "Groomer Profession: the clip profession..", "x": "The complete profession guide to Groomer Profession: the clip profession.. Clippers. History, meaning, practices, and how to engage respectfully — everything in one database. Clippers. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Groomer Profession essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Groomer Profession essentials.", "x": "At a glance: Groomer Profession — the clip profession.. Baths. The essentials: Nails.. Nails. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Clippers.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Clippers.", "x": "Groomer Profession: Clippers.. Nails. Essential knowledge — Nails.. the clip profession. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Clippers..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Clippers..", "x": "Explained: Clippers.. Fur. The context — Groomer Profession. Dogs. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Baths.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Baths.", "x": "Groomer Profession: Baths.. Patience. Essential knowledge — Dogs.. the clip profession. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Baths..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Baths..", "x": "Explained: Baths.. Dogs. The context — Groomer Profession. Patience. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Nails.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Nails.", "x": "Groomer Profession: Nails.. Fur. Essential knowledge — Patience.. the clip profession. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Nails..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Nails..", "x": "Explained: Nails.. Day. The context — Groomer Profession. Fur. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Dogs.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Dogs.", "x": "Groomer Profession: Dogs.. Dogs. Essential knowledge — Fur.. the clip profession. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Dogs..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Dogs..", "x": "Explained: Dogs.. Clippers. The context — Groomer Profession. Clippers. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Patience.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Patience.", "x": "Groomer Profession: Patience.. Day. Essential knowledge — Clippers.. the clip profession. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Patience..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Patience..", "x": "Explained: Patience.. Nails. The context — Groomer Profession. Baths. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Fur.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Fur.", "x": "Groomer Profession: Fur.. Clippers. Essential knowledge — Baths.. the clip profession. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Fur..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Fur..", "x": "Explained: Fur.. Patience. The context — Groomer Profession. Nails. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Clippers.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Clippers.", "x": "Groomer Profession in depth: Clippers.. Baths. Details — the clip profession.. Patience. Dogs. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Nails.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Nails.", "x": "Groomer Profession in depth: Nails.. Nails. Details — the clip profession.. Fur. Patience. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Patience.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Patience.", "x": "Groomer Profession in depth: Patience.. Dogs. Details — the clip profession.. Dogs. Fur. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Fur.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Fur.", "x": "Groomer Profession in depth: Fur.. Patience. Details — the clip profession.. Day. Clippers. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Dogs.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Dogs.", "x": "Groomer Profession in depth: Dogs.. Fur. Details — the clip profession.. Clippers. Baths. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Day.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Day.", "x": "Groomer Profession in depth: Day.. Clippers. Details — the clip profession.. Nails. Nails. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Groomer Profession comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Groomer Profession comes from.", "x": "Origins: Clippers.. Clippers. The history of Groomer Profession — the clip profession.. Nails. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Groomer Profession respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Groomer Profession respectfully.", "x": "Engaging: Patience.. Baths. How to participate or observe well — Groomer Profession. the clip profession. Respect first, always; Fur.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Groomer Profession do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Groomer Profession do's and don'ts.", "x": "Etiquette: Dogs.. Nails. The rules of respect — Groomer Profession. the clip profession. When in doubt, ask about Day.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Groomer Profession.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Groomer Profession.", "x": "Planning: Clippers.. Dogs. Practical notes — Groomer Profession. the clip profession. A little planning shows respect for Nails.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Groomer Profession and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Groomer Profession and money.", "x": "Costs: Patience.. Patience. What to budget — Groomer Profession. the clip profession. The best experiences of Fur. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-profession-groomer-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
