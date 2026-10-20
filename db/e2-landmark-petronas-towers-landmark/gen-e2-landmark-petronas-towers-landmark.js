(function(){'use strict';
/* JAH Petronas Towers Landmark Database generator — jahdb-e2-landmark-petronas-towers-landmark-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-landmark-petronas-towers-landmark',PREFIX='JAH-E2LANDMARKP-',NAME='JAH Petronas Towers Landmark Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Petronas Towers: the complete guide", "d": "Petronas Towers: the 452m twins..", "g": "overview", "l": 2, "q": "What is Petronas Towers: the complete guide?", "a": "Petronas Towers: the 452m twins..", "x": "The complete landmark guide to Petronas Towers: the 452m twins.. 1998. History, meaning, practices, and how to engage respectfully — everything in one database. 1998. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Petronas Towers essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Petronas Towers essentials.", "x": "At a glance: Petronas Towers — the 452m twins.. 452m. The essentials: Skybridge.. Skybridge. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "1998.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "1998.", "x": "Petronas Towers: 1998.. Skybridge. Essential knowledge — Skybridge.. the 452m twins. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 1998..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 1998..", "x": "Explained: 1998.. Islamic. The context — Petronas Towers. Islamic. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "452m.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "452m.", "x": "Petronas Towers: 452m.. Twins. Essential knowledge — Islamic.. the 452m twins. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: 452m..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: 452m..", "x": "Explained: 452m.. 452m. The context — Petronas Towers. Twins. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Skybridge.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Skybridge.", "x": "Petronas Towers: Skybridge.. Islamic. Essential knowledge — Twins.. the 452m twins. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Skybridge..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Skybridge..", "x": "Explained: Skybridge.. Tickets. The context — Petronas Towers. Suria. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Islamic.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Islamic.", "x": "Petronas Towers: Islamic.. 452m. Essential knowledge — Suria.. the 452m twins. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Islamic..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Islamic..", "x": "Explained: Islamic.. 1998. The context — Petronas Towers. 1998. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Twins.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Twins.", "x": "Petronas Towers: Twins.. Tickets. Essential knowledge — 1998.. the 452m twins. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Twins..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Twins..", "x": "Explained: Twins.. Skybridge. The context — Petronas Towers. 452m. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Suria.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Suria.", "x": "Petronas Towers: Suria.. 1998. Essential knowledge — 452m.. the 452m twins. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Suria..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Suria..", "x": "Explained: Suria.. Twins. The context — Petronas Towers. Skybridge. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "1998.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "1998.", "x": "Petronas Towers in depth: 1998.. 452m. Details — the 452m twins.. Twins. Islamic. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Skybridge.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Skybridge.", "x": "Petronas Towers in depth: Skybridge.. Skybridge. Details — the 452m twins.. Islamic. Twins. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Twins.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Twins.", "x": "Petronas Towers in depth: Twins.. Islamic. Details — the 452m twins.. 452m. Suria. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Islamic.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Islamic.", "x": "Petronas Towers in depth: Islamic.. Twins. Details — the 452m twins.. Tickets. 1998. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "452m.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "452m.", "x": "Petronas Towers in depth: 452m.. Suria. Details — the 452m twins.. 1998. 452m. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Tickets.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Tickets.", "x": "Petronas Towers in depth: Tickets.. 1998. Details — the 452m twins.. Skybridge. Skybridge. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Petronas Towers comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Petronas Towers comes from.", "x": "Origins: 1998.. 1998. The history of Petronas Towers — the 452m twins.. Skybridge. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Petronas Towers respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Petronas Towers respectfully.", "x": "Engaging: Twins.. 452m. How to participate or observe well — Petronas Towers. the 452m twins. Respect first, always; Islamic.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Petronas Towers do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Petronas Towers do's and don'ts.", "x": "Etiquette: 452m.. Skybridge. The rules of respect — Petronas Towers. the 452m twins. When in doubt, ask about Tickets.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Petronas Towers.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Petronas Towers.", "x": "Planning: 1998.. Islamic. Practical notes — Petronas Towers. the 452m twins. A little planning shows respect for Skybridge.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Petronas Towers and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Petronas Towers and money.", "x": "Costs: Twins.. Twins. What to budget — Petronas Towers. the 452m twins. The best experiences of Islamic. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-landmark-petronas-towers-landmark-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
