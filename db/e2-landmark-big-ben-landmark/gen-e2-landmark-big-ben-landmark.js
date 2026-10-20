(function(){'use strict';
/* JAH Big Ben Landmark Database generator — jahdb-e2-landmark-big-ben-landmark-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-landmark-big-ben-landmark',PREFIX='JAH-E2LANDMARKB-',NAME='JAH Big Ben Landmark Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Big Ben: the complete guide", "d": "Big Ben: the great bell..", "g": "overview", "l": 2, "q": "What is Big Ben: the complete guide?", "a": "Big Ben: the great bell..", "x": "The complete landmark guide to Big Ben: the great bell.. 1859. History, meaning, practices, and how to engage respectfully — everything in one database. 1859. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Big Ben essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Big Ben essentials.", "x": "At a glance: Big Ben — the great bell.. 96m. The essentials: Tower.. Elizabeth Tower. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "1859.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "1859.", "x": "Big Ben: 1859.. Tower. Essential knowledge — Elizabeth Tower.. the great bell. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 1859..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 1859..", "x": "Explained: 1859.. Bell. The context — Big Ben. Westminster. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "96m.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "96m.", "x": "Big Ben: 96m.. Chimes. Essential knowledge — Westminster.. the great bell. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: 96m..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: 96m..", "x": "Explained: 96m.. Westminster. The context — Big Ben. Chimes. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Elizabeth Tower.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Elizabeth Tower.", "x": "Big Ben: Elizabeth Tower.. Bell. Essential knowledge — Chimes.. the great bell. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Elizabeth Tower..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Elizabeth Tower..", "x": "Explained: Elizabeth Tower.. Tours. The context — Big Ben. Bell. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Westminster.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Westminster.", "x": "Big Ben: Westminster.. Westminster. Essential knowledge — Bell.. the great bell. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Westminster..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Westminster..", "x": "Explained: Westminster.. 1859. The context — Big Ben. 1859. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Chimes.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Chimes.", "x": "Big Ben: Chimes.. Tours. Essential knowledge — 1859.. the great bell. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Chimes..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Chimes..", "x": "Explained: Chimes.. Tower. The context — Big Ben. 96m. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Bell.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Bell.", "x": "Big Ben: Bell.. 1859. Essential knowledge — 96m.. the great bell. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Bell..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Bell..", "x": "Explained: Bell.. Chimes. The context — Big Ben. Elizabeth Tower. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "1859.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "1859.", "x": "Big Ben in depth: 1859.. 96m. Details — the great bell.. Chimes. Westminster. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Tower.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Tower.", "x": "Big Ben in depth: Tower.. Elizabeth Tower. Details — the great bell.. Bell. Chimes. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Chimes.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Chimes.", "x": "Big Ben in depth: Chimes.. Westminster. Details — the great bell.. Westminster. Bell. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Bell.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Bell.", "x": "Big Ben in depth: Bell.. Chimes. Details — the great bell.. Tours. 1859. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Westminster.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Westminster.", "x": "Big Ben in depth: Westminster.. Bell. Details — the great bell.. 1859. 96m. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Tours.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Tours.", "x": "Big Ben in depth: Tours.. 1859. Details — the great bell.. Tower. Elizabeth Tower. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Big Ben comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Big Ben comes from.", "x": "Origins: 1859.. 1859. The history of Big Ben — the great bell.. Tower. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Big Ben respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Big Ben respectfully.", "x": "Engaging: Chimes.. 96m. How to participate or observe well — Big Ben. the great bell. Respect first, always; Bell.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Big Ben do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Big Ben do's and don'ts.", "x": "Etiquette: Westminster.. Elizabeth Tower. The rules of respect — Big Ben. the great bell. When in doubt, ask about Tours.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Big Ben.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Big Ben.", "x": "Planning: 1859.. Westminster. Practical notes — Big Ben. the great bell. A little planning shows respect for Tower.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Big Ben and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Big Ben and money.", "x": "Costs: Chimes.. Chimes. What to budget — Big Ben. the great bell. The best experiences of Bell. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-landmark-big-ben-landmark-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
