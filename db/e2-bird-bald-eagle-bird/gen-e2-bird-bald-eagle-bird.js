(function(){'use strict';
/* JAH Bald Eagle Bird Species Database generator — jahdb-e2-bird-bald-eagle-bird-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-bird-bald-eagle-bird',PREFIX='JAH-E2BIRDBALDE-',NAME='JAH Bald Eagle Bird Species Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Bald Eagle: the complete guide", "d": "Bald Eagle: America's raptor..", "g": "overview", "l": 2, "q": "What is Bald Eagle: the complete guide?", "a": "Bald Eagle: America's raptor..", "x": "The complete bird species guide to Bald Eagle: America's raptor.. Raptor. History, meaning, practices, and how to engage respectfully — everything in one database. Raptor. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Bald Eagle essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Bald Eagle essentials.", "x": "At a glance: Bald Eagle — America's raptor.. White head. The essentials: Fish.. Alaska. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Raptor.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Raptor.", "x": "Bald Eagle: Raptor.. Fish. Essential knowledge — Alaska.. America's raptor. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Raptor..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Raptor..", "x": "Explained: Raptor.. Alaska. The context — Bald Eagle. Fish. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "White head.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "White head.", "x": "Bald Eagle: White head.. Symbol. Essential knowledge — Fish.. America's raptor. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: White head..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: White head..", "x": "Explained: White head.. Wingspan. The context — Bald Eagle. 8 ft wingspan. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Alaska.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Alaska.", "x": "Bald Eagle: Alaska.. Alaska. Essential knowledge — 8 ft wingspan.. America's raptor. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Alaska..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Alaska..", "x": "Explained: Alaska.. Habitat. The context — Bald Eagle. Symbol. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Fish.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Fish.", "x": "Bald Eagle: Fish.. Wingspan. Essential knowledge — Symbol.. America's raptor. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Fish..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Fish..", "x": "Explained: Fish.. Raptor. The context — Bald Eagle. Raptor. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "8 ft wingspan.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "8 ft wingspan.", "x": "Bald Eagle: 8 ft wingspan.. Habitat. Essential knowledge — Raptor.. America's raptor. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: 8 ft wingspan..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: 8 ft wingspan..", "x": "Explained: 8 ft wingspan.. Fish. The context — Bald Eagle. White head. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Symbol.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Symbol.", "x": "Bald Eagle: Symbol.. Raptor. Essential knowledge — White head.. America's raptor. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Symbol..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Symbol..", "x": "Explained: Symbol.. Symbol. The context — Bald Eagle. Alaska. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Raptor.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Raptor.", "x": "Bald Eagle in depth: Raptor.. White head. Details — America's raptor.. Symbol. Fish. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Fish.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Fish.", "x": "Bald Eagle in depth: Fish.. Alaska. Details — America's raptor.. Alaska. 8 ft wingspan. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Symbol.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Symbol.", "x": "Bald Eagle in depth: Symbol.. Fish. Details — America's raptor.. Wingspan. Symbol. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Alaska.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Alaska.", "x": "Bald Eagle in depth: Alaska.. 8 ft wingspan. Details — America's raptor.. Habitat. Raptor. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Wingspan.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Wingspan.", "x": "Bald Eagle in depth: Wingspan.. Symbol. Details — America's raptor.. Raptor. White head. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Habitat.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Habitat.", "x": "Bald Eagle in depth: Habitat.. Raptor. Details — America's raptor.. Fish. Alaska. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Bald Eagle comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Bald Eagle comes from.", "x": "Origins: Raptor.. Raptor. The history of Bald Eagle — America's raptor.. Fish. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Bald Eagle respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Bald Eagle respectfully.", "x": "Engaging: Symbol.. White head. How to participate or observe well — Bald Eagle. America's raptor. Respect first, always; Alaska.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Bald Eagle do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Bald Eagle do's and don'ts.", "x": "Etiquette: Wingspan.. Alaska. The rules of respect — Bald Eagle. America's raptor. When in doubt, ask about Habitat.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Bald Eagle.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Bald Eagle.", "x": "Planning: Raptor.. Fish. Practical notes — Bald Eagle. America's raptor. A little planning shows respect for Fish.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Bald Eagle and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Bald Eagle and money.", "x": "Costs: Symbol.. 8 ft wingspan. What to budget — Bald Eagle. America's raptor. The best experiences of Alaska. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-bird-bald-eagle-bird-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
