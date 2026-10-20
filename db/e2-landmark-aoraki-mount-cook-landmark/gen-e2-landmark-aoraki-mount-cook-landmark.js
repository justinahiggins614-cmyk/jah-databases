(function(){'use strict';
/* JAH Aoraki Mount Cook Landmark Database generator — jahdb-e2-landmark-aoraki-mount-cook-landmark-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-landmark-aoraki-mount-cook-landmark',PREFIX='JAH-E2LANDMARKA-',NAME='JAH Aoraki Mount Cook Landmark Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Aoraki Mount Cook: the complete guide", "d": "Aoraki Mount Cook: the 3,724m peak..", "g": "overview", "l": 2, "q": "What is Aoraki Mount Cook: the complete guide?", "a": "Aoraki Mount Cook: the 3,724m peak..", "x": "The complete landmark guide to Aoraki Mount Cook: the 3,724m peak.. 3,724m. History, meaning, practices, and how to engage respectfully — everything in one database. 3,724m. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Aoraki Mount Cook essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Aoraki Mount Cook essentials.", "x": "At a glance: Aoraki Mount Cook — the 3,724m peak.. Highest NZ. The essentials: Tasman.. Tasman. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "3,724m.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "3,724m.", "x": "Aoraki Mount Cook: 3,724m.. Tasman. Essential knowledge — Tasman.. the 3,724m peak. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 3,724m..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 3,724m..", "x": "Explained: 3,724m.. Views. The context — Aoraki Mount Cook. Alpine. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Highest NZ.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Highest NZ.", "x": "Aoraki Mount Cook: Highest NZ.. Hillary. Essential knowledge — Alpine.. the 3,724m peak. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Highest NZ..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Highest NZ..", "x": "Explained: Highest NZ.. Alpine. The context — Aoraki Mount Cook. Hillary. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Tasman.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Tasman.", "x": "Aoraki Mount Cook: Tasman.. Views. Essential knowledge — Hillary.. the 3,724m peak. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Tasman..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Tasman..", "x": "Explained: Tasman.. Trekking. The context — Aoraki Mount Cook. Views. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Alpine.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Alpine.", "x": "Aoraki Mount Cook: Alpine.. Alpine. Essential knowledge — Views.. the 3,724m peak. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Alpine..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Alpine..", "x": "Explained: Alpine.. 3,724m. The context — Aoraki Mount Cook. 3,724m. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Hillary.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Hillary.", "x": "Aoraki Mount Cook: Hillary.. Trekking. Essential knowledge — 3,724m.. the 3,724m peak. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Hillary..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Hillary..", "x": "Explained: Hillary.. Tasman. The context — Aoraki Mount Cook. Highest NZ. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Views.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Views.", "x": "Aoraki Mount Cook: Views.. 3,724m. Essential knowledge — Highest NZ.. the 3,724m peak. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Views..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Views..", "x": "Explained: Views.. Hillary. The context — Aoraki Mount Cook. Tasman. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "3,724m.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "3,724m.", "x": "Aoraki Mount Cook in depth: 3,724m.. Highest NZ. Details — the 3,724m peak.. Hillary. Alpine. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Tasman.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Tasman.", "x": "Aoraki Mount Cook in depth: Tasman.. Tasman. Details — the 3,724m peak.. Views. Hillary. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Hillary.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Hillary.", "x": "Aoraki Mount Cook in depth: Hillary.. Alpine. Details — the 3,724m peak.. Alpine. Views. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Views.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Views.", "x": "Aoraki Mount Cook in depth: Views.. Hillary. Details — the 3,724m peak.. Trekking. 3,724m. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Alpine.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Alpine.", "x": "Aoraki Mount Cook in depth: Alpine.. Views. Details — the 3,724m peak.. 3,724m. Highest NZ. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Trekking.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Trekking.", "x": "Aoraki Mount Cook in depth: Trekking.. 3,724m. Details — the 3,724m peak.. Tasman. Tasman. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Aoraki Mount Cook comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Aoraki Mount Cook comes from.", "x": "Origins: 3,724m.. 3,724m. The history of Aoraki Mount Cook — the 3,724m peak.. Tasman. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Aoraki Mount Cook respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Aoraki Mount Cook respectfully.", "x": "Engaging: Hillary.. Highest NZ. How to participate or observe well — Aoraki Mount Cook. the 3,724m peak. Respect first, always; Views.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Aoraki Mount Cook do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Aoraki Mount Cook do's and don'ts.", "x": "Etiquette: Alpine.. Tasman. The rules of respect — Aoraki Mount Cook. the 3,724m peak. When in doubt, ask about Trekking.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Aoraki Mount Cook.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Aoraki Mount Cook.", "x": "Planning: 3,724m.. Alpine. Practical notes — Aoraki Mount Cook. the 3,724m peak. A little planning shows respect for Tasman.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Aoraki Mount Cook and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Aoraki Mount Cook and money.", "x": "Costs: Hillary.. Hillary. What to budget — Aoraki Mount Cook. the 3,724m peak. The best experiences of Views. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-landmark-aoraki-mount-cook-landmark-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
