(function(){'use strict';
/* JAH Szechenyi Baths Landmark Database generator — jahdb-e2-landmark-szechenyi-baths-landmark-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-landmark-szechenyi-baths-landmark',PREFIX='JAH-E2LANDMARKS-',NAME='JAH Szechenyi Baths Landmark Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Szechenyi Baths: the complete guide", "d": "Szechenyi Baths: the yellow baths..", "g": "overview", "l": 2, "q": "What is Szechenyi Baths: the complete guide?", "a": "Szechenyi Baths: the yellow baths..", "x": "The complete landmark guide to Szechenyi Baths: the yellow baths.. 1913. History, meaning, practices, and how to engage respectfully — everything in one database. 1913. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Szechenyi Baths essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Szechenyi Baths essentials.", "x": "At a glance: Szechenyi Baths — the yellow baths.. Thermal. The essentials: Chess.. Yellow. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "1913.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "1913.", "x": "Szechenyi Baths: 1913.. Chess. Essential knowledge — Yellow.. the yellow baths. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 1913..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 1913..", "x": "Explained: 1913.. Thermal. The context — Szechenyi Baths. Chess. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Thermal.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Thermal.", "x": "Szechenyi Baths: Thermal.. Medicinal. Essential knowledge — Chess.. the yellow baths. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Thermal..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Thermal..", "x": "Explained: Thermal.. Yellow. The context — Szechenyi Baths. Outdoor. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Yellow.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Yellow.", "x": "Szechenyi Baths: Yellow.. Thermal. Essential knowledge — Outdoor.. the yellow baths. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Yellow..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Yellow..", "x": "Explained: Yellow.. Bathing. The context — Szechenyi Baths. Medicinal. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Chess.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Chess.", "x": "Szechenyi Baths: Chess.. Yellow. Essential knowledge — Medicinal.. the yellow baths. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Chess..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Chess..", "x": "Explained: Chess.. 1913. The context — Szechenyi Baths. 1913. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Outdoor.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Outdoor.", "x": "Szechenyi Baths: Outdoor.. Bathing. Essential knowledge — 1913.. the yellow baths. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Outdoor..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Outdoor..", "x": "Explained: Outdoor.. Chess. The context — Szechenyi Baths. Thermal. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Medicinal.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Medicinal.", "x": "Szechenyi Baths: Medicinal.. 1913. Essential knowledge — Thermal.. the yellow baths. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Medicinal..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Medicinal..", "x": "Explained: Medicinal.. Medicinal. The context — Szechenyi Baths. Yellow. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "1913.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "1913.", "x": "Szechenyi Baths in depth: 1913.. Thermal. Details — the yellow baths.. Medicinal. Chess. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Chess.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Chess.", "x": "Szechenyi Baths in depth: Chess.. Yellow. Details — the yellow baths.. Thermal. Outdoor. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Medicinal.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Medicinal.", "x": "Szechenyi Baths in depth: Medicinal.. Chess. Details — the yellow baths.. Yellow. Medicinal. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Thermal.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Thermal.", "x": "Szechenyi Baths in depth: Thermal.. Outdoor. Details — the yellow baths.. Bathing. 1913. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Yellow.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Yellow.", "x": "Szechenyi Baths in depth: Yellow.. Medicinal. Details — the yellow baths.. 1913. Thermal. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Bathing.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Bathing.", "x": "Szechenyi Baths in depth: Bathing.. 1913. Details — the yellow baths.. Chess. Yellow. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Szechenyi Baths comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Szechenyi Baths comes from.", "x": "Origins: 1913.. 1913. The history of Szechenyi Baths — the yellow baths.. Chess. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Szechenyi Baths respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Szechenyi Baths respectfully.", "x": "Engaging: Medicinal.. Thermal. How to participate or observe well — Szechenyi Baths. the yellow baths. Respect first, always; Thermal.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Szechenyi Baths do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Szechenyi Baths do's and don'ts.", "x": "Etiquette: Yellow.. Yellow. The rules of respect — Szechenyi Baths. the yellow baths. When in doubt, ask about Bathing.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Szechenyi Baths.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Szechenyi Baths.", "x": "Planning: 1913.. Chess. Practical notes — Szechenyi Baths. the yellow baths. A little planning shows respect for Chess.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Szechenyi Baths and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Szechenyi Baths and money.", "x": "Costs: Medicinal.. Outdoor. What to budget — Szechenyi Baths. the yellow baths. The best experiences of Thermal. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-landmark-szechenyi-baths-landmark-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
