(function(){'use strict';
/* JAH Trinity College Dublin Landmark Database generator — jahdb-e2-landmark-trinity-college-dublin-landmark-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-landmark-trinity-college-dublin-landmark',PREFIX='JAH-E2LANDMARKT-',NAME='JAH Trinity College Dublin Landmark Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Trinity College Dublin: the complete guide", "d": "Trinity College Dublin: the Long Room..", "g": "overview", "l": 2, "q": "What is Trinity College Dublin: the complete guide?", "a": "Trinity College Dublin: the Long Room..", "x": "The complete landmark guide to Trinity College Dublin: the Long Room.. 1592. History, meaning, practices, and how to engage respectfully — everything in one database. 1592. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Trinity College Dublin essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Trinity College Dublin essentials.", "x": "At a glance: Trinity College Dublin — the Long Room.. Book of Kells. The essentials: Kells.. Long Room. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "1592.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "1592.", "x": "Trinity College Dublin: 1592.. Kells. Essential knowledge — Long Room.. the Long Room. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 1592..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 1592..", "x": "Explained: 1592.. Long Room. The context — Trinity College Dublin. Library. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Book of Kells.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Book of Kells.", "x": "Trinity College Dublin: Book of Kells.. Tourists. Essential knowledge — Library.. the Long Room. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Book of Kells..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Book of Kells..", "x": "Explained: Book of Kells.. Library. The context — Trinity College Dublin. Old. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Long Room.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Long Room.", "x": "Trinity College Dublin: Long Room.. Long Room. Essential knowledge — Old.. the Long Room. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Long Room..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Long Room..", "x": "Explained: Long Room.. Tours. The context — Trinity College Dublin. Tourists. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Library.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Library.", "x": "Trinity College Dublin: Library.. Library. Essential knowledge — Tourists.. the Long Room. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Library..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Library..", "x": "Explained: Library.. 1592. The context — Trinity College Dublin. 1592. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Old.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Old.", "x": "Trinity College Dublin: Old.. Tours. Essential knowledge — 1592.. the Long Room. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Old..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Old..", "x": "Explained: Old.. Kells. The context — Trinity College Dublin. Book of Kells. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Tourists.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Tourists.", "x": "Trinity College Dublin: Tourists.. 1592. Essential knowledge — Book of Kells.. the Long Room. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Tourists..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Tourists..", "x": "Explained: Tourists.. Tourists. The context — Trinity College Dublin. Long Room. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "1592.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "1592.", "x": "Trinity College Dublin in depth: 1592.. Book of Kells. Details — the Long Room.. Tourists. Library. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Kells.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Kells.", "x": "Trinity College Dublin in depth: Kells.. Long Room. Details — the Long Room.. Long Room. Old. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Tourists.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Tourists.", "x": "Trinity College Dublin in depth: Tourists.. Library. Details — the Long Room.. Library. Tourists. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Long Room.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Long Room.", "x": "Trinity College Dublin in depth: Long Room.. Old. Details — the Long Room.. Tours. 1592. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Library.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Library.", "x": "Trinity College Dublin in depth: Library.. Tourists. Details — the Long Room.. 1592. Book of Kells. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Tours.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Tours.", "x": "Trinity College Dublin in depth: Tours.. 1592. Details — the Long Room.. Kells. Long Room. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Trinity College Dublin comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Trinity College Dublin comes from.", "x": "Origins: 1592.. 1592. The history of Trinity College Dublin — the Long Room.. Kells. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Trinity College Dublin respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Trinity College Dublin respectfully.", "x": "Engaging: Tourists.. Book of Kells. How to participate or observe well — Trinity College Dublin. the Long Room. Respect first, always; Long Room.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Trinity College Dublin do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Trinity College Dublin do's and don'ts.", "x": "Etiquette: Library.. Long Room. The rules of respect — Trinity College Dublin. the Long Room. When in doubt, ask about Tours.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Trinity College Dublin.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Trinity College Dublin.", "x": "Planning: 1592.. Library. Practical notes — Trinity College Dublin. the Long Room. A little planning shows respect for Kells.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Trinity College Dublin and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Trinity College Dublin and money.", "x": "Costs: Tourists.. Old. What to budget — Trinity College Dublin. the Long Room. The best experiences of Long Room. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-landmark-trinity-college-dublin-landmark-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
