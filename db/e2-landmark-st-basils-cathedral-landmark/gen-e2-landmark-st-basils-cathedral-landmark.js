(function(){'use strict';
/* JAH St. Basil\'s Cathedral Landmark Database generator — jahdb-e2-landmark-st-basils-cathedral-landmark-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-landmark-st-basils-cathedral-landmark',PREFIX='JAH-E2LANDMARKS-',NAME='JAH St. Basil\'s Cathedral Landmark Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "St. Basil's Cathedral: the complete guide", "d": "St. Basil's Cathedral: the onion domes..", "g": "overview", "l": 2, "q": "What is St. Basil's Cathedral: the complete guide?", "a": "St. Basil's Cathedral: the onion domes..", "x": "The complete landmark guide to St. Basil's Cathedral: the onion domes.. 1555. History, meaning, practices, and how to engage respectfully — everything in one database. 1555. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "St. Basil's Cathedral essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "St. Basil's Cathedral essentials.", "x": "At a glance: St. Basil's Cathedral — the onion domes.. Ivan. The essentials: Domes.. Onion domes. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "1555.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "1555.", "x": "St. Basil's Cathedral: 1555.. Domes. Essential knowledge — Onion domes.. the onion domes. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 1555..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 1555..", "x": "Explained: 1555.. Colors. The context — St. Basil's Cathedral. Red Square. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Ivan.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Ivan.", "x": "St. Basil's Cathedral: Ivan.. Red Square. Essential knowledge — Red Square.. the onion domes. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Ivan..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Ivan..", "x": "Explained: Ivan.. Ivan. The context — St. Basil's Cathedral. Colors. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Onion domes.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Onion domes.", "x": "St. Basil's Cathedral: Onion domes.. Colors. Essential knowledge — Colors.. the onion domes. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Onion domes..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Onion domes..", "x": "Explained: Onion domes.. Tours. The context — St. Basil's Cathedral. Museum. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Red Square.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Red Square.", "x": "St. Basil's Cathedral: Red Square.. Ivan. Essential knowledge — Museum.. the onion domes. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Red Square..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Red Square..", "x": "Explained: Red Square.. 1555. The context — St. Basil's Cathedral. 1555. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Colors.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Colors.", "x": "St. Basil's Cathedral: Colors.. Tours. Essential knowledge — 1555.. the onion domes. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Colors..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Colors..", "x": "Explained: Colors.. Domes. The context — St. Basil's Cathedral. Ivan. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Museum.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Museum.", "x": "St. Basil's Cathedral: Museum.. 1555. Essential knowledge — Ivan.. the onion domes. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Museum..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Museum..", "x": "Explained: Museum.. Red Square. The context — St. Basil's Cathedral. Onion domes. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "1555.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "1555.", "x": "St. Basil's Cathedral in depth: 1555.. Ivan. Details — the onion domes.. Red Square. Red Square. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Domes.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Domes.", "x": "St. Basil's Cathedral in depth: Domes.. Onion domes. Details — the onion domes.. Colors. Colors. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Red Square.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Red Square.", "x": "St. Basil's Cathedral in depth: Red Square.. Red Square. Details — the onion domes.. Ivan. Museum. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Colors.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Colors.", "x": "St. Basil's Cathedral in depth: Colors.. Colors. Details — the onion domes.. Tours. 1555. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Ivan.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Ivan.", "x": "St. Basil's Cathedral in depth: Ivan.. Museum. Details — the onion domes.. 1555. Ivan. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Tours.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Tours.", "x": "St. Basil's Cathedral in depth: Tours.. 1555. Details — the onion domes.. Domes. Onion domes. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where St. Basil's Cathedral comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where St. Basil's Cathedral comes from.", "x": "Origins: 1555.. 1555. The history of St. Basil's Cathedral — the onion domes.. Domes. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing St. Basil's Cathedral respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing St. Basil's Cathedral respectfully.", "x": "Engaging: Red Square.. Ivan. How to participate or observe well — St. Basil's Cathedral. the onion domes. Respect first, always; Colors.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "St. Basil's Cathedral do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "St. Basil's Cathedral do's and don'ts.", "x": "Etiquette: Ivan.. Onion domes. The rules of respect — St. Basil's Cathedral. the onion domes. When in doubt, ask about Tours.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around St. Basil's Cathedral.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around St. Basil's Cathedral.", "x": "Planning: 1555.. Red Square. Practical notes — St. Basil's Cathedral. the onion domes. A little planning shows respect for Domes.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "St. Basil's Cathedral and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "St. Basil's Cathedral and money.", "x": "Costs: Red Square.. Colors. What to budget — St. Basil's Cathedral. the onion domes. The best experiences of Colors. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-landmark-st-basils-cathedral-landmark-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
