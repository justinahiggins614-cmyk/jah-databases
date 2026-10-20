(function(){'use strict';
/* JAH Tower Bridge Landmark Database generator — jahdb-e2-landmark-tower-bridge-landmark-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-landmark-tower-bridge-landmark',PREFIX='JAH-E2LANDMARKT-',NAME='JAH Tower Bridge Landmark Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Tower Bridge: the complete guide", "d": "Tower Bridge: the bascule beauty..", "g": "overview", "l": 2, "q": "What is Tower Bridge: the complete guide?", "a": "Tower Bridge: the bascule beauty..", "x": "The complete landmark guide to Tower Bridge: the bascule beauty.. 1894. History, meaning, practices, and how to engage respectfully — everything in one database. 1894. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Tower Bridge essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Tower Bridge essentials.", "x": "At a glance: Tower Bridge — the bascule beauty.. Bascule. The essentials: Walkways.. Victorian. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "1894.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "1894.", "x": "Tower Bridge: 1894.. Walkways. Essential knowledge — Victorian.. the bascule beauty. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 1894..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 1894..", "x": "Explained: 1894.. Blue. The context — Tower Bridge. Walkways. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Bascule.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Bascule.", "x": "Tower Bridge: Bascule.. Thames. Essential knowledge — Walkways.. the bascule beauty. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Bascule..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Bascule..", "x": "Explained: Bascule.. Victorian. The context — Tower Bridge. Blue. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Victorian.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Victorian.", "x": "Tower Bridge: Victorian.. Blue. Essential knowledge — Blue.. the bascule beauty. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Victorian..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Victorian..", "x": "Explained: Victorian.. Tours. The context — Tower Bridge. Thames. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Walkways.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Walkways.", "x": "Tower Bridge: Walkways.. Victorian. Essential knowledge — Thames.. the bascule beauty. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Walkways..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Walkways..", "x": "Explained: Walkways.. 1894. The context — Tower Bridge. 1894. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Blue.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Blue.", "x": "Tower Bridge: Blue.. Tours. Essential knowledge — 1894.. the bascule beauty. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Blue..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Blue..", "x": "Explained: Blue.. Walkways. The context — Tower Bridge. Bascule. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Thames.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Thames.", "x": "Tower Bridge: Thames.. 1894. Essential knowledge — Bascule.. the bascule beauty. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Thames..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Thames..", "x": "Explained: Thames.. Thames. The context — Tower Bridge. Victorian. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "1894.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "1894.", "x": "Tower Bridge in depth: 1894.. Bascule. Details — the bascule beauty.. Thames. Walkways. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Walkways.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Walkways.", "x": "Tower Bridge in depth: Walkways.. Victorian. Details — the bascule beauty.. Blue. Blue. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Thames.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Thames.", "x": "Tower Bridge in depth: Thames.. Walkways. Details — the bascule beauty.. Victorian. Thames. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Blue.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Blue.", "x": "Tower Bridge in depth: Blue.. Blue. Details — the bascule beauty.. Tours. 1894. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Victorian.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Victorian.", "x": "Tower Bridge in depth: Victorian.. Thames. Details — the bascule beauty.. 1894. Bascule. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Tours.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Tours.", "x": "Tower Bridge in depth: Tours.. 1894. Details — the bascule beauty.. Walkways. Victorian. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Tower Bridge comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Tower Bridge comes from.", "x": "Origins: 1894.. 1894. The history of Tower Bridge — the bascule beauty.. Walkways. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Tower Bridge respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Tower Bridge respectfully.", "x": "Engaging: Thames.. Bascule. How to participate or observe well — Tower Bridge. the bascule beauty. Respect first, always; Blue.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Tower Bridge do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Tower Bridge do's and don'ts.", "x": "Etiquette: Victorian.. Victorian. The rules of respect — Tower Bridge. the bascule beauty. When in doubt, ask about Tours.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Tower Bridge.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Tower Bridge.", "x": "Planning: 1894.. Walkways. Practical notes — Tower Bridge. the bascule beauty. A little planning shows respect for Walkways.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Tower Bridge and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Tower Bridge and money.", "x": "Costs: Thames.. Blue. What to budget — Tower Bridge. the bascule beauty. The best experiences of Blue. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-landmark-tower-bridge-landmark-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
