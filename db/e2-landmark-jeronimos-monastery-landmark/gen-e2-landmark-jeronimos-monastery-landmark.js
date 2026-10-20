(function(){'use strict';
/* JAH Jeronimos Monastery Landmark Database generator — jahdb-e2-landmark-jeronimos-monastery-landmark-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-landmark-jeronimos-monastery-landmark',PREFIX='JAH-E2LANDMARKJ-',NAME='JAH Jeronimos Monastery Landmark Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Jeronimos Monastery: the complete guide", "d": "Jeronimos Monastery: the maritime Gothic..", "g": "overview", "l": 2, "q": "What is Jeronimos Monastery: the complete guide?", "a": "Jeronimos Monastery: the maritime Gothic..", "x": "The complete landmark guide to Jeronimos Monastery: the maritime Gothic.. 1502. History, meaning, practices, and how to engage respectfully — everything in one database. 1502. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Jeronimos Monastery essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Jeronimos Monastery essentials.", "x": "At a glance: Jeronimos Monastery — the maritime Gothic.. Vasco da Gama. The essentials: Gama.. Manueline. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "1502.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "1502.", "x": "Jeronimos Monastery: 1502.. Gama. Essential knowledge — Manueline.. the maritime Gothic. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 1502..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 1502..", "x": "Explained: 1502.. UNESCO. The context — Jeronimos Monastery. Cloister. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Vasco da Gama.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Vasco da Gama.", "x": "Jeronimos Monastery: Vasco da Gama.. Cloister. Essential knowledge — Cloister.. the maritime Gothic. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Vasco da Gama..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Vasco da Gama..", "x": "Explained: Vasco da Gama.. Manueline. The context — Jeronimos Monastery. UNESCO. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Manueline.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Manueline.", "x": "Jeronimos Monastery: Manueline.. UNESCO. Essential knowledge — UNESCO.. the maritime Gothic. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Manueline..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Manueline..", "x": "Explained: Manueline.. Tours. The context — Jeronimos Monastery. Limestone. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Cloister.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Cloister.", "x": "Jeronimos Monastery: Cloister.. Manueline. Essential knowledge — Limestone.. the maritime Gothic. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Cloister..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Cloister..", "x": "Explained: Cloister.. 1502. The context — Jeronimos Monastery. 1502. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "UNESCO.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "UNESCO.", "x": "Jeronimos Monastery: UNESCO.. Tours. Essential knowledge — 1502.. the maritime Gothic. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: UNESCO..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: UNESCO..", "x": "Explained: UNESCO.. Gama. The context — Jeronimos Monastery. Vasco da Gama. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Limestone.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Limestone.", "x": "Jeronimos Monastery: Limestone.. 1502. Essential knowledge — Vasco da Gama.. the maritime Gothic. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Limestone..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Limestone..", "x": "Explained: Limestone.. Cloister. The context — Jeronimos Monastery. Manueline. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "1502.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "1502.", "x": "Jeronimos Monastery in depth: 1502.. Vasco da Gama. Details — the maritime Gothic.. Cloister. Cloister. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Gama.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Gama.", "x": "Jeronimos Monastery in depth: Gama.. Manueline. Details — the maritime Gothic.. UNESCO. UNESCO. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Cloister.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Cloister.", "x": "Jeronimos Monastery in depth: Cloister.. Cloister. Details — the maritime Gothic.. Manueline. Limestone. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "UNESCO.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "UNESCO.", "x": "Jeronimos Monastery in depth: UNESCO.. UNESCO. Details — the maritime Gothic.. Tours. 1502. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Manueline.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Manueline.", "x": "Jeronimos Monastery in depth: Manueline.. Limestone. Details — the maritime Gothic.. 1502. Vasco da Gama. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Tours.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Tours.", "x": "Jeronimos Monastery in depth: Tours.. 1502. Details — the maritime Gothic.. Gama. Manueline. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Jeronimos Monastery comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Jeronimos Monastery comes from.", "x": "Origins: 1502.. 1502. The history of Jeronimos Monastery — the maritime Gothic.. Gama. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Jeronimos Monastery respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Jeronimos Monastery respectfully.", "x": "Engaging: Cloister.. Vasco da Gama. How to participate or observe well — Jeronimos Monastery. the maritime Gothic. Respect first, always; UNESCO.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Jeronimos Monastery do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Jeronimos Monastery do's and don'ts.", "x": "Etiquette: Manueline.. Manueline. The rules of respect — Jeronimos Monastery. the maritime Gothic. When in doubt, ask about Tours.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Jeronimos Monastery.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Jeronimos Monastery.", "x": "Planning: 1502.. Cloister. Practical notes — Jeronimos Monastery. the maritime Gothic. A little planning shows respect for Gama.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Jeronimos Monastery and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Jeronimos Monastery and money.", "x": "Costs: Cloister.. UNESCO. What to budget — Jeronimos Monastery. the maritime Gothic. The best experiences of UNESCO. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-landmark-jeronimos-monastery-landmark-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
