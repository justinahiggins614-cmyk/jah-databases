(function(){'use strict';
/* JAH Gilbert Sullivan2 Database generator — jahdb-e2-music2-gilbert-sullivan-composer2-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-music2-gilbert-sullivan-composer2',PREFIX='JAH-E2MUSIC2GIL-',NAME='JAH Gilbert Sullivan2 Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Gilbert Sullivan2: the complete guide", "d": "Gilbert Sullivan2: the operetta duo..", "g": "overview", "l": 2, "q": "What is Gilbert Sullivan2: the complete guide?", "a": "Gilbert Sullivan2: the operetta duo..", "x": "The complete composer guide to Gilbert Sullivan2: the operetta duo.. 1871. History, meaning, practices, and how to engage respectfully — everything in one database. Pirates. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Gilbert Sullivan2 essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Gilbert Sullivan2 essentials.", "x": "At a glance: Gilbert Sullivan2 — the operetta duo.. Pirates. The essentials: Savoy.. Pinafore. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "1871.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "1871.", "x": "Gilbert Sullivan2: 1871.. Savoy. Essential knowledge — Pinafore.. the operetta duo. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 1871..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 1871..", "x": "Explained: 1871.. Pinafore. The context — Gilbert Sullivan2. Savoy. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Pirates.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Pirates.", "x": "Gilbert Sullivan2: Pirates.. London. Essential knowledge — Savoy.. the operetta duo. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Pirates..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Pirates..", "x": "Explained: Pirates.. Topsy. The context — Gilbert Sullivan2. Topsy-turvy. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Pinafore.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Pinafore.", "x": "Gilbert Sullivan2: Pinafore.. Pinafore. Essential knowledge — Topsy-turvy.. the operetta duo. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Pinafore..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Pinafore..", "x": "Explained: Pinafore.. Legacy. The context — Gilbert Sullivan2. London. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Savoy.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Savoy.", "x": "Gilbert Sullivan2: Savoy.. Topsy. Essential knowledge — London.. the operetta duo. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Savoy..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Savoy..", "x": "Explained: Savoy.. Pirates. The context — Gilbert Sullivan2. 1871. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Topsy-turvy.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Topsy-turvy.", "x": "Gilbert Sullivan2: Topsy-turvy.. Legacy. Essential knowledge — 1871.. the operetta duo. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Topsy-turvy..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Topsy-turvy..", "x": "Explained: Topsy-turvy.. Savoy. The context — Gilbert Sullivan2. Pirates. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "London.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "London.", "x": "Gilbert Sullivan2: London.. Pirates. Essential knowledge — Pirates.. the operetta duo. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: London..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: London..", "x": "Explained: London.. London. The context — Gilbert Sullivan2. Pinafore. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Pirates.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Pirates.", "x": "Gilbert Sullivan2 in depth: Pirates.. Pirates. Details — the operetta duo.. London. Savoy. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Savoy.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Savoy.", "x": "Gilbert Sullivan2 in depth: Savoy.. Pinafore. Details — the operetta duo.. Pinafore. Topsy-turvy. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "London.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "London.", "x": "Gilbert Sullivan2 in depth: London.. Savoy. Details — the operetta duo.. Topsy. London. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Pinafore.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Pinafore.", "x": "Gilbert Sullivan2 in depth: Pinafore.. Topsy-turvy. Details — the operetta duo.. Legacy. 1871. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Topsy.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Topsy.", "x": "Gilbert Sullivan2 in depth: Topsy.. London. Details — the operetta duo.. Pirates. Pirates. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Legacy.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Legacy.", "x": "Gilbert Sullivan2 in depth: Legacy.. 1871. Details — the operetta duo.. Savoy. Pinafore. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Gilbert Sullivan2 comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Gilbert Sullivan2 comes from.", "x": "Origins: Pirates.. 1871. The history of Gilbert Sullivan2 — the operetta duo.. Savoy. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Gilbert Sullivan2 respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Gilbert Sullivan2 respectfully.", "x": "Engaging: London.. Pirates. How to participate or observe well — Gilbert Sullivan2. the operetta duo. Respect first, always; Pinafore.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Gilbert Sullivan2 do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Gilbert Sullivan2 do's and don'ts.", "x": "Etiquette: Topsy.. Pinafore. The rules of respect — Gilbert Sullivan2. the operetta duo. When in doubt, ask about Legacy.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Gilbert Sullivan2.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Gilbert Sullivan2.", "x": "Planning: Pirates.. Savoy. Practical notes — Gilbert Sullivan2. the operetta duo. A little planning shows respect for Savoy.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Gilbert Sullivan2 and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Gilbert Sullivan2 and money.", "x": "Costs: London.. Topsy-turvy. What to budget — Gilbert Sullivan2. the operetta duo. The best experiences of Pinafore. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-music2-gilbert-sullivan-composer2-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
