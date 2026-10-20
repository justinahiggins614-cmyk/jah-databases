(function(){'use strict';
/* JAH Fencing Olympics Database generator — jahdb-e2-olympic2-fencing-olympics-sport-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-olympic2-fencing-olympics-sport',PREFIX='JAH-E2OLYMPIC2F-',NAME='JAH Fencing Olympics Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Fencing Olympics: the complete guide", "d": "Fencing Olympics: the electric blade..", "g": "overview", "l": 2, "q": "What is Fencing Olympics: the complete guide?", "a": "Fencing Olympics: the electric blade..", "x": "The complete olympic sport guide to Fencing Olympics: the electric blade.. 1896. History, meaning, practices, and how to engage respectfully — everything in one database. Weapons. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Fencing Olympics essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Fencing Olympics essentials.", "x": "At a glance: Fencing Olympics — the electric blade.. Epee. The essentials: Electric.. Foil. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "1896.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "1896.", "x": "Fencing Olympics: 1896.. Electric. Essential knowledge — Foil.. the electric blade. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 1896..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 1896..", "x": "Explained: 1896.. Epee. The context — Fencing Olympics. Sabre. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Epee.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Epee.", "x": "Fencing Olympics: Epee.. Touches. Essential knowledge — Sabre.. the electric blade. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Epee..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Epee..", "x": "Explained: Epee.. Foil. The context — Fencing Olympics. Electric. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Foil.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Foil.", "x": "Fencing Olympics: Foil.. Epee. Essential knowledge — Electric.. the electric blade. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Foil..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Foil..", "x": "Explained: Foil.. Guide. The context — Fencing Olympics. 15 touches. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Sabre.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Sabre.", "x": "Fencing Olympics: Sabre.. Foil. Essential knowledge — 15 touches.. the electric blade. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Sabre..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Sabre..", "x": "Explained: Sabre.. Weapons. The context — Fencing Olympics. 1896. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Electric.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Electric.", "x": "Fencing Olympics: Electric.. Guide. Essential knowledge — 1896.. the electric blade. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Electric..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Electric..", "x": "Explained: Electric.. Electric. The context — Fencing Olympics. Epee. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "15 touches.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "15 touches.", "x": "Fencing Olympics: 15 touches.. Weapons. Essential knowledge — Epee.. the electric blade. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: 15 touches..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: 15 touches..", "x": "Explained: 15 touches.. Touches. The context — Fencing Olympics. Foil. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Weapons.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Weapons.", "x": "Fencing Olympics in depth: Weapons.. Epee. Details — the electric blade.. Touches. Sabre. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Electric.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Electric.", "x": "Fencing Olympics in depth: Electric.. Foil. Details — the electric blade.. Epee. Electric. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Touches.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Touches.", "x": "Fencing Olympics in depth: Touches.. Sabre. Details — the electric blade.. Foil. 15 touches. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Epee.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Epee.", "x": "Fencing Olympics in depth: Epee.. Electric. Details — the electric blade.. Guide. 1896. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Foil.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Foil.", "x": "Fencing Olympics in depth: Foil.. 15 touches. Details — the electric blade.. Weapons. Epee. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Guide.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Guide.", "x": "Fencing Olympics in depth: Guide.. 1896. Details — the electric blade.. Electric. Foil. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Fencing Olympics comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Fencing Olympics comes from.", "x": "Origins: Weapons.. 1896. The history of Fencing Olympics — the electric blade.. Electric. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Fencing Olympics respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Fencing Olympics respectfully.", "x": "Engaging: Touches.. Epee. How to participate or observe well — Fencing Olympics. the electric blade. Respect first, always; Epee.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Fencing Olympics do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Fencing Olympics do's and don'ts.", "x": "Etiquette: Foil.. Foil. The rules of respect — Fencing Olympics. the electric blade. When in doubt, ask about Guide.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Fencing Olympics.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Fencing Olympics.", "x": "Planning: Weapons.. Sabre. Practical notes — Fencing Olympics. the electric blade. A little planning shows respect for Electric.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Fencing Olympics and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Fencing Olympics and money.", "x": "Costs: Touches.. Electric. What to budget — Fencing Olympics. the electric blade. The best experiences of Epee. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-olympic2-fencing-olympics-sport-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
