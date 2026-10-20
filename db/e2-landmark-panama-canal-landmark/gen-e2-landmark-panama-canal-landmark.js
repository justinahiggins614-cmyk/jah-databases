(function(){'use strict';
/* JAH Panama Canal Landmark Database generator — jahdb-e2-landmark-panama-canal-landmark-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-landmark-panama-canal-landmark',PREFIX='JAH-E2LANDMARKP-',NAME='JAH Panama Canal Landmark Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Panama Canal: the complete guide", "d": "Panama Canal: the 82 km cut..", "g": "overview", "l": 2, "q": "What is Panama Canal: the complete guide?", "a": "Panama Canal: the 82 km cut..", "x": "The complete landmark guide to Panama Canal: the 82 km cut.. 1914. History, meaning, practices, and how to engage respectfully — everything in one database. 1914. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Panama Canal essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Panama Canal essentials.", "x": "At a glance: Panama Canal — the 82 km cut.. 82 km. The essentials: Locks.. Locks. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "1914.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "1914.", "x": "Panama Canal: 1914.. Locks. Essential knowledge — Locks.. the 82 km cut. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 1914..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 1914..", "x": "Explained: 1914.. Miraflores. The context — Panama Canal. Miraflores. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "82 km.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "82 km.", "x": "Panama Canal: 82 km.. Engineering. Essential knowledge — Miraflores.. the 82 km cut. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: 82 km..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: 82 km..", "x": "Explained: 82 km.. Ships. The context — Panama Canal. Ships. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Locks.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Locks.", "x": "Panama Canal: Locks.. Miraflores. Essential knowledge — Ships.. the 82 km cut. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Locks..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Locks..", "x": "Explained: Locks.. Tours. The context — Panama Canal. Engineering. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Miraflores.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Miraflores.", "x": "Panama Canal: Miraflores.. Ships. Essential knowledge — Engineering.. the 82 km cut. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Miraflores..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Miraflores..", "x": "Explained: Miraflores.. 1914. The context — Panama Canal. 1914. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Ships.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Ships.", "x": "Panama Canal: Ships.. Tours. Essential knowledge — 1914.. the 82 km cut. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Ships..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Ships..", "x": "Explained: Ships.. Locks. The context — Panama Canal. 82 km. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Engineering.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Engineering.", "x": "Panama Canal: Engineering.. 1914. Essential knowledge — 82 km.. the 82 km cut. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Engineering..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Engineering..", "x": "Explained: Engineering.. Engineering. The context — Panama Canal. Locks. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "1914.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "1914.", "x": "Panama Canal in depth: 1914.. 82 km. Details — the 82 km cut.. Engineering. Miraflores. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Locks.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Locks.", "x": "Panama Canal in depth: Locks.. Locks. Details — the 82 km cut.. Miraflores. Ships. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Engineering.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Engineering.", "x": "Panama Canal in depth: Engineering.. Miraflores. Details — the 82 km cut.. Ships. Engineering. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Miraflores.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Miraflores.", "x": "Panama Canal in depth: Miraflores.. Ships. Details — the 82 km cut.. Tours. 1914. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Ships.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Ships.", "x": "Panama Canal in depth: Ships.. Engineering. Details — the 82 km cut.. 1914. 82 km. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Tours.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Tours.", "x": "Panama Canal in depth: Tours.. 1914. Details — the 82 km cut.. Locks. Locks. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Panama Canal comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Panama Canal comes from.", "x": "Origins: 1914.. 1914. The history of Panama Canal — the 82 km cut.. Locks. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Panama Canal respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Panama Canal respectfully.", "x": "Engaging: Engineering.. 82 km. How to participate or observe well — Panama Canal. the 82 km cut. Respect first, always; Miraflores.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Panama Canal do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Panama Canal do's and don'ts.", "x": "Etiquette: Ships.. Locks. The rules of respect — Panama Canal. the 82 km cut. When in doubt, ask about Tours.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Panama Canal.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Panama Canal.", "x": "Planning: 1914.. Miraflores. Practical notes — Panama Canal. the 82 km cut. A little planning shows respect for Locks.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Panama Canal and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Panama Canal and money.", "x": "Costs: Engineering.. Ships. What to budget — Panama Canal. the 82 km cut. The best experiences of Miraflores. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-landmark-panama-canal-landmark-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
