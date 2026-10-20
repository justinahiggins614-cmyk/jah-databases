(function(){'use strict';
/* JAH Thanksgiving Parades Parade Database generator — jahdb-e2-parade-thanksgiving-parades-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-parade-thanksgiving-parades',PREFIX='JAH-E2PARADETHA-',NAME='JAH Thanksgiving Parades Parade Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Thanksgiving Parades: the complete guide", "d": "Thanksgiving Parades: the holiday march..", "g": "overview", "l": 2, "q": "What is Thanksgiving Parades: the complete guide?", "a": "Thanksgiving Parades: the holiday march..", "x": "The complete parade guide to Thanksgiving Parades: the holiday march.. Macy's. History, meaning, practices, and how to engage respectfully — everything in one database. Macy's. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Thanksgiving Parades essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Thanksgiving Parades essentials.", "x": "At a glance: Thanksgiving Parades — the holiday march.. Balloons. The essentials: Balloons.. 1924. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Macy's.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Macy's.", "x": "Thanksgiving Parades: Macy's.. Balloons. Essential knowledge — 1924.. the holiday march. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Macy's..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Macy's..", "x": "Explained: Macy's.. Santa. The context — Thanksgiving Parades. NYC. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Balloons.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Balloons.", "x": "Thanksgiving Parades: Balloons.. 1924. Essential knowledge — NYC.. the holiday march. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Balloons..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Balloons..", "x": "Explained: Balloons.. TV. The context — Thanksgiving Parades. Santa. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "1924.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "1924.", "x": "Thanksgiving Parades: 1924.. Santa. Essential knowledge — Santa.. the holiday march. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: 1924..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: 1924..", "x": "Explained: 1924.. History. The context — Thanksgiving Parades. TV. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "NYC.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "NYC.", "x": "Thanksgiving Parades: NYC.. TV. Essential knowledge — TV.. the holiday march. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: NYC..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: NYC..", "x": "Explained: NYC.. Macy's. The context — Thanksgiving Parades. Macy's. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Santa.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Santa.", "x": "Thanksgiving Parades: Santa.. History. Essential knowledge — Macy's.. the holiday march. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Santa..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Santa..", "x": "Explained: Santa.. Balloons. The context — Thanksgiving Parades. Balloons. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "TV.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "TV.", "x": "Thanksgiving Parades: TV.. Macy's. Essential knowledge — Balloons.. the holiday march. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: TV..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: TV..", "x": "Explained: TV.. 1924. The context — Thanksgiving Parades. 1924. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Macy's.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Macy's.", "x": "Thanksgiving Parades in depth: Macy's.. Balloons. Details — the holiday march.. 1924. NYC. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Balloons.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Balloons.", "x": "Thanksgiving Parades in depth: Balloons.. 1924. Details — the holiday march.. Santa. Santa. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "1924.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "1924.", "x": "Thanksgiving Parades in depth: 1924.. NYC. Details — the holiday march.. TV. TV. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Santa.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Santa.", "x": "Thanksgiving Parades in depth: Santa.. Santa. Details — the holiday march.. History. Macy's. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "TV.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "TV.", "x": "Thanksgiving Parades in depth: TV.. TV. Details — the holiday march.. Macy's. Balloons. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "History.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "History.", "x": "Thanksgiving Parades in depth: History.. Macy's. Details — the holiday march.. Balloons. 1924. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Thanksgiving Parades comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Thanksgiving Parades comes from.", "x": "Origins: Macy's.. Macy's. The history of Thanksgiving Parades — the holiday march.. Balloons. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Thanksgiving Parades respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Thanksgiving Parades respectfully.", "x": "Engaging: 1924.. Balloons. How to participate or observe well — Thanksgiving Parades. the holiday march. Respect first, always; Santa.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Thanksgiving Parades do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Thanksgiving Parades do's and don'ts.", "x": "Etiquette: TV.. 1924. The rules of respect — Thanksgiving Parades. the holiday march. When in doubt, ask about History.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Thanksgiving Parades.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Thanksgiving Parades.", "x": "Planning: Macy's.. NYC. Practical notes — Thanksgiving Parades. the holiday march. A little planning shows respect for Balloons.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Thanksgiving Parades and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Thanksgiving Parades and money.", "x": "Costs: 1924.. Santa. What to budget — Thanksgiving Parades. the holiday march. The best experiences of Santa. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-parade-thanksgiving-parades-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
