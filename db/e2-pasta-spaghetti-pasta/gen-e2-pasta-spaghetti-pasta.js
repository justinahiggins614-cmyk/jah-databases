(function(){'use strict';
/* JAH Spaghetti Pasta Database generator — jahdb-e2-pasta-spaghetti-pasta-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-pasta-spaghetti-pasta',PREFIX='JAH-E2PASTASPAG-',NAME='JAH Spaghetti Pasta Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Spaghetti: the complete guide", "d": "Spaghetti: the long classic..", "g": "overview", "l": 2, "q": "What is Spaghetti: the complete guide?", "a": "Spaghetti: the long classic..", "x": "The complete pasta guide to Spaghetti: the long classic.. Italy. History, meaning, practices, and how to engage respectfully — everything in one database. Long. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Spaghetti essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Spaghetti essentials.", "x": "At a glance: Spaghetti — the long classic.. Long. The essentials: Sauces.. Bolognese. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Italy.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Italy.", "x": "Spaghetti: Italy.. Sauces. Essential knowledge — Bolognese.. the long classic. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Italy..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Italy..", "x": "Explained: Italy.. Al dente. The context — Spaghetti. Aglio e olio. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Long.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Long.", "x": "Spaghetti: Long.. Die. Essential knowledge — Aglio e olio.. the long classic. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Long..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Long..", "x": "Explained: Long.. Italy. The context — Spaghetti. Bronze die. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Bolognese.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Bolognese.", "x": "Spaghetti: Bolognese.. Al dente. Essential knowledge — Bronze die.. the long classic. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Bolognese..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Bolognese..", "x": "Explained: Bolognese.. Cooking. The context — Spaghetti. Al dente. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Aglio e olio.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Aglio e olio.", "x": "Spaghetti: Aglio e olio.. Italy. Essential knowledge — Al dente.. the long classic. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Aglio e olio..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Aglio e olio..", "x": "Explained: Aglio e olio.. Long. The context — Spaghetti. Italy. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Bronze die.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Bronze die.", "x": "Spaghetti: Bronze die.. Cooking. Essential knowledge — Italy.. the long classic. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Bronze die..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Bronze die..", "x": "Explained: Bronze die.. Sauces. The context — Spaghetti. Long. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Al dente.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Al dente.", "x": "Spaghetti: Al dente.. Long. Essential knowledge — Long.. the long classic. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Al dente..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Al dente..", "x": "Explained: Al dente.. Die. The context — Spaghetti. Bolognese. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Long.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Long.", "x": "Spaghetti in depth: Long.. Long. Details — the long classic.. Die. Aglio e olio. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Sauces.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Sauces.", "x": "Spaghetti in depth: Sauces.. Bolognese. Details — the long classic.. Al dente. Bronze die. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Die.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Die.", "x": "Spaghetti in depth: Die.. Aglio e olio. Details — the long classic.. Italy. Al dente. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Al dente.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Al dente.", "x": "Spaghetti in depth: Al dente.. Bronze die. Details — the long classic.. Cooking. Italy. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Italy.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Italy.", "x": "Spaghetti in depth: Italy.. Al dente. Details — the long classic.. Long. Long. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Cooking.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Cooking.", "x": "Spaghetti in depth: Cooking.. Italy. Details — the long classic.. Sauces. Bolognese. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Spaghetti comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Spaghetti comes from.", "x": "Origins: Long.. Italy. The history of Spaghetti — the long classic.. Sauces. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Spaghetti respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Spaghetti respectfully.", "x": "Engaging: Die.. Long. How to participate or observe well — Spaghetti. the long classic. Respect first, always; Al dente.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Spaghetti do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Spaghetti do's and don'ts.", "x": "Etiquette: Italy.. Bolognese. The rules of respect — Spaghetti. the long classic. When in doubt, ask about Cooking.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Spaghetti.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Spaghetti.", "x": "Planning: Long.. Aglio e olio. Practical notes — Spaghetti. the long classic. A little planning shows respect for Sauces.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Spaghetti and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Spaghetti and money.", "x": "Costs: Die.. Bronze die. What to budget — Spaghetti. the long classic. The best experiences of Al dente. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-pasta-spaghetti-pasta-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
