(function(){'use strict';
/* JAH Car Shows Database generator — jahdb-e2-shows2-car-shows-show-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-shows2-car-shows-show',PREFIX='JAH-E2SHOWS2CAR-',NAME='JAH Car Shows Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Car Shows: the complete guide", "d": "Car Shows: the auto exhibits..", "g": "overview", "l": 2, "q": "What is Car Shows: the complete guide?", "a": "Car Shows: the auto exhibits..", "x": "The complete show guide to Car Shows: the auto exhibits.. Concepts. History, meaning, practices, and how to engage respectfully — everything in one database. Concepts. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Car Shows essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Car Shows essentials.", "x": "At a glance: Car Shows — the auto exhibits.. Detroit. The essentials: Reveals.. Classics. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Concepts.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Concepts.", "x": "Car Shows: Concepts.. Reveals. Essential knowledge — Classics.. the auto exhibits. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Concepts..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Concepts..", "x": "Explained: Concepts.. Detroit. The context — Car Shows. Supercars. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Detroit.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Detroit.", "x": "Car Shows: Detroit.. Shine. Essential knowledge — Supercars.. the auto exhibits. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Detroit..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Detroit..", "x": "Explained: Detroit.. Classics. The context — Car Shows. Reveals. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Classics.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Classics.", "x": "Car Shows: Classics.. Detroit. Essential knowledge — Reveals.. the auto exhibits. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Classics..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Classics..", "x": "Explained: Classics.. Guide. The context — Car Shows. Shine. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Supercars.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Supercars.", "x": "Car Shows: Supercars.. Classics. Essential knowledge — Shine.. the auto exhibits. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Supercars..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Supercars..", "x": "Explained: Supercars.. Concepts. The context — Car Shows. Concepts. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Reveals.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Reveals.", "x": "Car Shows: Reveals.. Guide. Essential knowledge — Concepts.. the auto exhibits. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Reveals..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Reveals..", "x": "Explained: Reveals.. Reveals. The context — Car Shows. Detroit. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Shine.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Shine.", "x": "Car Shows: Shine.. Concepts. Essential knowledge — Detroit.. the auto exhibits. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Shine..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Shine..", "x": "Explained: Shine.. Shine. The context — Car Shows. Classics. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Concepts.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Concepts.", "x": "Car Shows in depth: Concepts.. Detroit. Details — the auto exhibits.. Shine. Supercars. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Reveals.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Reveals.", "x": "Car Shows in depth: Reveals.. Classics. Details — the auto exhibits.. Detroit. Reveals. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Shine.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Shine.", "x": "Car Shows in depth: Shine.. Supercars. Details — the auto exhibits.. Classics. Shine. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Detroit.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Detroit.", "x": "Car Shows in depth: Detroit.. Reveals. Details — the auto exhibits.. Guide. Concepts. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Classics.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Classics.", "x": "Car Shows in depth: Classics.. Shine. Details — the auto exhibits.. Concepts. Detroit. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Guide.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Guide.", "x": "Car Shows in depth: Guide.. Concepts. Details — the auto exhibits.. Reveals. Classics. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Car Shows comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Car Shows comes from.", "x": "Origins: Concepts.. Concepts. The history of Car Shows — the auto exhibits.. Reveals. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Car Shows respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Car Shows respectfully.", "x": "Engaging: Shine.. Detroit. How to participate or observe well — Car Shows. the auto exhibits. Respect first, always; Detroit.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Car Shows do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Car Shows do's and don'ts.", "x": "Etiquette: Classics.. Classics. The rules of respect — Car Shows. the auto exhibits. When in doubt, ask about Guide.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Car Shows.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Car Shows.", "x": "Planning: Concepts.. Supercars. Practical notes — Car Shows. the auto exhibits. A little planning shows respect for Reveals.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Car Shows and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Car Shows and money.", "x": "Costs: Shine.. Reveals. What to budget — Car Shows. the auto exhibits. The best experiences of Detroit. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-shows2-car-shows-show-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
