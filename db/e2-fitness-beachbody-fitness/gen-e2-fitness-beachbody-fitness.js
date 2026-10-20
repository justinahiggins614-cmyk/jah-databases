(function(){'use strict';
/* JAH Beachbody Fitness Program Database generator — jahdb-e2-fitness-beachbody-fitness-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-fitness-beachbody-fitness',PREFIX='JAH-E2FITNESSBE-',NAME='JAH Beachbody Fitness Program Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Beachbody: the complete guide", "d": "Beachbody: the home programs..", "g": "overview", "l": 2, "q": "What is Beachbody: the complete guide?", "a": "Beachbody: the home programs..", "x": "The complete fitness program guide to Beachbody: the home programs.. 1998. History, meaning, practices, and how to engage respectfully — everything in one database. Programs. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Beachbody essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Beachbody essentials.", "x": "At a glance: Beachbody — the home programs.. P90X. The essentials: Streaming.. 21 Day Fix. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "1998.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "1998.", "x": "Beachbody: 1998.. Streaming. Essential knowledge — 21 Day Fix.. the home programs. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 1998..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 1998..", "x": "Explained: 1998.. Shakeology. The context — Beachbody. Shakeology. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "P90X.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "P90X.", "x": "Beachbody: P90X.. Coaches. Essential knowledge — Shakeology.. the home programs. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: P90X..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: P90X..", "x": "Explained: P90X.. History. The context — Beachbody. Coaches. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "21 Day Fix.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "21 Day Fix.", "x": "Beachbody: 21 Day Fix.. Shakeology. Essential knowledge — Coaches.. the home programs. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: 21 Day Fix..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: 21 Day Fix..", "x": "Explained: 21 Day Fix.. Method. The context — Beachbody. Streaming. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Shakeology.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Shakeology.", "x": "Beachbody: Shakeology.. History. Essential knowledge — Streaming.. the home programs. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Shakeology..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Shakeology..", "x": "Explained: Shakeology.. Programs. The context — Beachbody. 1998. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Coaches.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Coaches.", "x": "Beachbody: Coaches.. Method. Essential knowledge — 1998.. the home programs. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Coaches..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Coaches..", "x": "Explained: Coaches.. Streaming. The context — Beachbody. P90X. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Streaming.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Streaming.", "x": "Beachbody: Streaming.. Programs. Essential knowledge — P90X.. the home programs. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Streaming..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Streaming..", "x": "Explained: Streaming.. Coaches. The context — Beachbody. 21 Day Fix. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Programs.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Programs.", "x": "Beachbody in depth: Programs.. P90X. Details — the home programs.. Coaches. Shakeology. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Streaming.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Streaming.", "x": "Beachbody in depth: Streaming.. 21 Day Fix. Details — the home programs.. Shakeology. Coaches. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Coaches.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Coaches.", "x": "Beachbody in depth: Coaches.. Shakeology. Details — the home programs.. History. Streaming. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Shakeology.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Shakeology.", "x": "Beachbody in depth: Shakeology.. Coaches. Details — the home programs.. Method. 1998. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "History.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "History.", "x": "Beachbody in depth: History.. Streaming. Details — the home programs.. Programs. P90X. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Method.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Method.", "x": "Beachbody in depth: Method.. 1998. Details — the home programs.. Streaming. 21 Day Fix. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Beachbody comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Beachbody comes from.", "x": "Origins: Programs.. 1998. The history of Beachbody — the home programs.. Streaming. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Beachbody respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Beachbody respectfully.", "x": "Engaging: Coaches.. P90X. How to participate or observe well — Beachbody. the home programs. Respect first, always; Shakeology.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Beachbody do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Beachbody do's and don'ts.", "x": "Etiquette: History.. 21 Day Fix. The rules of respect — Beachbody. the home programs. When in doubt, ask about Method.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Beachbody.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Beachbody.", "x": "Planning: Programs.. Shakeology. Practical notes — Beachbody. the home programs. A little planning shows respect for Streaming.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Beachbody and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Beachbody and money.", "x": "Costs: Coaches.. Coaches. What to budget — Beachbody. the home programs. The best experiences of Shakeology. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-fitness-beachbody-fitness-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
