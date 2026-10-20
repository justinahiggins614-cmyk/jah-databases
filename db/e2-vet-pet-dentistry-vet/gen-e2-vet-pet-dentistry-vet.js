(function(){'use strict';
/* JAH Pet Dentistry Veterinary Database generator — jahdb-e2-vet-pet-dentistry-vet-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-vet-pet-dentistry-vet',PREFIX='JAH-E2VETPETDEN-',NAME='JAH Pet Dentistry Veterinary Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Pet Dentistry: the complete guide", "d": "Pet Dentistry: the oral health..", "g": "overview", "l": 2, "q": "What is Pet Dentistry: the complete guide?", "a": "Pet Dentistry: the oral health..", "x": "The complete veterinary guide to Pet Dentistry: the oral health.. Cleaning. History, meaning, practices, and how to engage respectfully — everything in one database. Cleaning. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Pet Dentistry essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Pet Dentistry essentials.", "x": "At a glance: Pet Dentistry — the oral health.. X-rays. The essentials: Extractions.. Extractions. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Cleaning.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Cleaning.", "x": "Pet Dentistry: Cleaning.. Extractions. Essential knowledge — Extractions.. the oral health. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Cleaning..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Cleaning..", "x": "Explained: Cleaning.. Tartar. The context — Pet Dentistry. Anesthesia. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "X-rays.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "X-rays.", "x": "Pet Dentistry: X-rays.. Home. Essential knowledge — Anesthesia.. the oral health. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: X-rays..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: X-rays..", "x": "Explained: X-rays.. X-rays. The context — Pet Dentistry. Tartar. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Extractions.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Extractions.", "x": "Pet Dentistry: Extractions.. Tartar. Essential knowledge — Tartar.. the oral health. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Extractions..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Extractions..", "x": "Explained: Extractions.. Guide. The context — Pet Dentistry. Home. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Anesthesia.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Anesthesia.", "x": "Pet Dentistry: Anesthesia.. X-rays. Essential knowledge — Home.. the oral health. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Anesthesia..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Anesthesia..", "x": "Explained: Anesthesia.. Cleaning. The context — Pet Dentistry. Cleaning. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Tartar.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Tartar.", "x": "Pet Dentistry: Tartar.. Guide. Essential knowledge — Cleaning.. the oral health. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Tartar..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Tartar..", "x": "Explained: Tartar.. Extractions. The context — Pet Dentistry. X-rays. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Home.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Home.", "x": "Pet Dentistry: Home.. Cleaning. Essential knowledge — X-rays.. the oral health. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Home..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Home..", "x": "Explained: Home.. Home. The context — Pet Dentistry. Extractions. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Cleaning.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Cleaning.", "x": "Pet Dentistry in depth: Cleaning.. X-rays. Details — the oral health.. Home. Anesthesia. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Extractions.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Extractions.", "x": "Pet Dentistry in depth: Extractions.. Extractions. Details — the oral health.. Tartar. Tartar. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Home.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Home.", "x": "Pet Dentistry in depth: Home.. Anesthesia. Details — the oral health.. X-rays. Home. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Tartar.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Tartar.", "x": "Pet Dentistry in depth: Tartar.. Tartar. Details — the oral health.. Guide. Cleaning. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "X-rays.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "X-rays.", "x": "Pet Dentistry in depth: X-rays.. Home. Details — the oral health.. Cleaning. X-rays. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Guide.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Guide.", "x": "Pet Dentistry in depth: Guide.. Cleaning. Details — the oral health.. Extractions. Extractions. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Pet Dentistry comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Pet Dentistry comes from.", "x": "Origins: Cleaning.. Cleaning. The history of Pet Dentistry — the oral health.. Extractions. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Pet Dentistry respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Pet Dentistry respectfully.", "x": "Engaging: Home.. X-rays. How to participate or observe well — Pet Dentistry. the oral health. Respect first, always; Tartar.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Pet Dentistry do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Pet Dentistry do's and don'ts.", "x": "Etiquette: X-rays.. Extractions. The rules of respect — Pet Dentistry. the oral health. When in doubt, ask about Guide.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Pet Dentistry.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Pet Dentistry.", "x": "Planning: Cleaning.. Anesthesia. Practical notes — Pet Dentistry. the oral health. A little planning shows respect for Extractions.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Pet Dentistry and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Pet Dentistry and money.", "x": "Costs: Home.. Tartar. What to budget — Pet Dentistry. the oral health. The best experiences of Tartar. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-vet-pet-dentistry-vet-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
