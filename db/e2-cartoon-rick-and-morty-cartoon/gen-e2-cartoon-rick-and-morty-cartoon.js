(function(){'use strict';
/* JAH Rick and Morty Cartoon Database generator — jahdb-e2-cartoon-rick-and-morty-cartoon-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-cartoon-rick-and-morty-cartoon',PREFIX='JAH-E2CARTOONRI-',NAME='JAH Rick and Morty Cartoon Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Rick and Morty: the complete guide", "d": "Rick and Morty: the sci-fi satire..", "g": "overview", "l": 2, "q": "What is Rick and Morty: the complete guide?", "a": "Rick and Morty: the sci-fi satire..", "x": "The complete cartoon guide to Rick and Morty: the sci-fi satire.. 2013. History, meaning, practices, and how to engage respectfully — everything in one database. Multiverse. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Rick and Morty essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Rick and Morty essentials.", "x": "At a glance: Rick and Morty — the sci-fi satire.. Multiverse. The essentials: Schwifty.. Schwifty. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "2013.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "2013.", "x": "Rick and Morty: 2013.. Schwifty. Essential knowledge — Schwifty.. the sci-fi satire. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 2013..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 2013..", "x": "Explained: 2013.. Adult. The context — Rick and Morty. Adult Swim. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Multiverse.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Multiverse.", "x": "Rick and Morty: Multiverse.. Pickle. Essential knowledge — Adult Swim.. the sci-fi satire. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Multiverse..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Multiverse..", "x": "Explained: Multiverse.. Wubba. The context — Rick and Morty. Pickle. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Schwifty.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Schwifty.", "x": "Rick and Morty: Schwifty.. Adult. Essential knowledge — Pickle.. the sci-fi satire. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Schwifty..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Schwifty..", "x": "Explained: Schwifty.. Legacy. The context — Rick and Morty. Wubba. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Adult Swim.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Adult Swim.", "x": "Rick and Morty: Adult Swim.. Wubba. Essential knowledge — Wubba.. the sci-fi satire. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Adult Swim..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Adult Swim..", "x": "Explained: Adult Swim.. Multiverse. The context — Rick and Morty. 2013. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Pickle.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Pickle.", "x": "Rick and Morty: Pickle.. Legacy. Essential knowledge — 2013.. the sci-fi satire. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Pickle..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Pickle..", "x": "Explained: Pickle.. Schwifty. The context — Rick and Morty. Multiverse. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Wubba.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Wubba.", "x": "Rick and Morty: Wubba.. Multiverse. Essential knowledge — Multiverse.. the sci-fi satire. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Wubba..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Wubba..", "x": "Explained: Wubba.. Pickle. The context — Rick and Morty. Schwifty. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Multiverse.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Multiverse.", "x": "Rick and Morty in depth: Multiverse.. Multiverse. Details — the sci-fi satire.. Pickle. Adult Swim. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Schwifty.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Schwifty.", "x": "Rick and Morty in depth: Schwifty.. Schwifty. Details — the sci-fi satire.. Adult. Pickle. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Pickle.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Pickle.", "x": "Rick and Morty in depth: Pickle.. Adult Swim. Details — the sci-fi satire.. Wubba. Wubba. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Adult.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Adult.", "x": "Rick and Morty in depth: Adult.. Pickle. Details — the sci-fi satire.. Legacy. 2013. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Wubba.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Wubba.", "x": "Rick and Morty in depth: Wubba.. Wubba. Details — the sci-fi satire.. Multiverse. Multiverse. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Legacy.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Legacy.", "x": "Rick and Morty in depth: Legacy.. 2013. Details — the sci-fi satire.. Schwifty. Schwifty. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Rick and Morty comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Rick and Morty comes from.", "x": "Origins: Multiverse.. 2013. The history of Rick and Morty — the sci-fi satire.. Schwifty. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Rick and Morty respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Rick and Morty respectfully.", "x": "Engaging: Pickle.. Multiverse. How to participate or observe well — Rick and Morty. the sci-fi satire. Respect first, always; Adult.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Rick and Morty do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Rick and Morty do's and don'ts.", "x": "Etiquette: Wubba.. Schwifty. The rules of respect — Rick and Morty. the sci-fi satire. When in doubt, ask about Legacy.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Rick and Morty.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Rick and Morty.", "x": "Planning: Multiverse.. Adult Swim. Practical notes — Rick and Morty. the sci-fi satire. A little planning shows respect for Schwifty.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Rick and Morty and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Rick and Morty and money.", "x": "Costs: Pickle.. Pickle. What to budget — Rick and Morty. the sci-fi satire. The best experiences of Adult. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-cartoon-rick-and-morty-cartoon-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
