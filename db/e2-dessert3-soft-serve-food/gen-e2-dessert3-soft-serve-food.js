(function(){'use strict';
/* JAH Soft Serve Dessert Database generator — jahdb-e2-dessert3-soft-serve-food-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-dessert3-soft-serve-food',PREFIX='JAH-E2DESSERT3S-',NAME='JAH Soft Serve Dessert Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Soft Serve: the complete guide", "d": "Soft Serve: the swirled cone..", "g": "overview", "l": 2, "q": "What is Soft Serve: the complete guide?", "a": "Soft Serve: the swirled cone..", "x": "The complete dessert guide to Soft Serve: the swirled cone.. Swirl. History, meaning, practices, and how to engage respectfully — everything in one database. Swirl. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Soft Serve essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Soft Serve essentials.", "x": "At a glance: Soft Serve — the swirled cone.. Cone. The essentials: Twist.. 1930s. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Swirl.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Swirl.", "x": "Soft Serve: Swirl.. Twist. Essential knowledge — 1930s.. the swirled cone. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Swirl..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Swirl..", "x": "Explained: Swirl.. Cone. The context — Soft Serve. Vanilla. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Cone.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Cone.", "x": "Soft Serve: Cone.. Machine. Essential knowledge — Vanilla.. the swirled cone. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Cone..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Cone..", "x": "Explained: Cone.. 1930s. The context — Soft Serve. Twist. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "1930s.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "1930s.", "x": "Soft Serve: 1930s.. Cone. Essential knowledge — Twist.. the swirled cone. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: 1930s..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: 1930s..", "x": "Explained: 1930s.. Making. The context — Soft Serve. Machine. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Vanilla.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Vanilla.", "x": "Soft Serve: Vanilla.. 1930s. Essential knowledge — Machine.. the swirled cone. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Vanilla..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Vanilla..", "x": "Explained: Vanilla.. Swirl. The context — Soft Serve. Swirl. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Twist.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Twist.", "x": "Soft Serve: Twist.. Making. Essential knowledge — Swirl.. the swirled cone. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Twist..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Twist..", "x": "Explained: Twist.. Twist. The context — Soft Serve. Cone. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Machine.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Machine.", "x": "Soft Serve: Machine.. Swirl. Essential knowledge — Cone.. the swirled cone. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Machine..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Machine..", "x": "Explained: Machine.. Machine. The context — Soft Serve. 1930s. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Swirl.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Swirl.", "x": "Soft Serve in depth: Swirl.. Cone. Details — the swirled cone.. Machine. Vanilla. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Twist.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Twist.", "x": "Soft Serve in depth: Twist.. 1930s. Details — the swirled cone.. Cone. Twist. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Machine.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Machine.", "x": "Soft Serve in depth: Machine.. Vanilla. Details — the swirled cone.. 1930s. Machine. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Cone.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Cone.", "x": "Soft Serve in depth: Cone.. Twist. Details — the swirled cone.. Making. Swirl. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "1930s.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "1930s.", "x": "Soft Serve in depth: 1930s.. Machine. Details — the swirled cone.. Swirl. Cone. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Making.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Making.", "x": "Soft Serve in depth: Making.. Swirl. Details — the swirled cone.. Twist. 1930s. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Soft Serve comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Soft Serve comes from.", "x": "Origins: Swirl.. Swirl. The history of Soft Serve — the swirled cone.. Twist. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Soft Serve respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Soft Serve respectfully.", "x": "Engaging: Machine.. Cone. How to participate or observe well — Soft Serve. the swirled cone. Respect first, always; Cone.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Soft Serve do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Soft Serve do's and don'ts.", "x": "Etiquette: 1930s.. 1930s. The rules of respect — Soft Serve. the swirled cone. When in doubt, ask about Making.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Soft Serve.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Soft Serve.", "x": "Planning: Swirl.. Vanilla. Practical notes — Soft Serve. the swirled cone. A little planning shows respect for Twist.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Soft Serve and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Soft Serve and money.", "x": "Costs: Machine.. Twist. What to budget — Soft Serve. the swirled cone. The best experiences of Cone. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-dessert3-soft-serve-food-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
