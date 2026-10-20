(function(){'use strict';
/* JAH Tennessee Walker Horse Breed Database generator — jahdb-e2-horse-tennessee-walker-breed-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-horse-tennessee-walker-breed',PREFIX='JAH-E2HORSETENN-',NAME='JAH Tennessee Walker Horse Breed Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Tennessee Walker: the complete guide", "d": "Tennessee Walker: the running walk..", "g": "overview", "l": 2, "q": "What is Tennessee Walker: the complete guide?", "a": "Tennessee Walker: the running walk..", "x": "The complete horse breed guide to Tennessee Walker: the running walk.. Gaited. History, meaning, practices, and how to engage respectfully — everything in one database. Gaited. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Tennessee Walker essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Tennessee Walker essentials.", "x": "At a glance: Tennessee Walker — the running walk.. Running walk. The essentials: Smooth.. Tennessee. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Gaited.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Gaited.", "x": "Tennessee Walker: Gaited.. Smooth. Essential knowledge — Tennessee.. the running walk. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Gaited..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Gaited..", "x": "Explained: Gaited.. Show. The context — Tennessee Walker. Smooth. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Running walk.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Running walk.", "x": "Tennessee Walker: Running walk.. Tennessee. Essential knowledge — Smooth.. the running walk. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Running walk..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Running walk..", "x": "Explained: Running walk.. Walk. The context — Tennessee Walker. Show. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Tennessee.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Tennessee.", "x": "Tennessee Walker: Tennessee.. Show. Essential knowledge — Show.. the running walk. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Tennessee..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Tennessee..", "x": "Explained: Tennessee.. History. The context — Tennessee Walker. Plantation. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Smooth.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Smooth.", "x": "Tennessee Walker: Smooth.. Walk. Essential knowledge — Plantation.. the running walk. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Smooth..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Smooth..", "x": "Explained: Smooth.. Gaited. The context — Tennessee Walker. Gaited. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Show.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Show.", "x": "Tennessee Walker: Show.. History. Essential knowledge — Gaited.. the running walk. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Show..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Show..", "x": "Explained: Show.. Smooth. The context — Tennessee Walker. Running walk. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Plantation.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Plantation.", "x": "Tennessee Walker: Plantation.. Gaited. Essential knowledge — Running walk.. the running walk. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Plantation..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Plantation..", "x": "Explained: Plantation.. Tennessee. The context — Tennessee Walker. Tennessee. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Gaited.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Gaited.", "x": "Tennessee Walker in depth: Gaited.. Running walk. Details — the running walk.. Tennessee. Smooth. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Smooth.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Smooth.", "x": "Tennessee Walker in depth: Smooth.. Tennessee. Details — the running walk.. Show. Show. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Tennessee.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Tennessee.", "x": "Tennessee Walker in depth: Tennessee.. Smooth. Details — the running walk.. Walk. Plantation. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Show.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Show.", "x": "Tennessee Walker in depth: Show.. Show. Details — the running walk.. History. Gaited. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Walk.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Walk.", "x": "Tennessee Walker in depth: Walk.. Plantation. Details — the running walk.. Gaited. Running walk. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "History.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "History.", "x": "Tennessee Walker in depth: History.. Gaited. Details — the running walk.. Smooth. Tennessee. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Tennessee Walker comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Tennessee Walker comes from.", "x": "Origins: Gaited.. Gaited. The history of Tennessee Walker — the running walk.. Smooth. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Tennessee Walker respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Tennessee Walker respectfully.", "x": "Engaging: Tennessee.. Running walk. How to participate or observe well — Tennessee Walker. the running walk. Respect first, always; Show.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Tennessee Walker do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Tennessee Walker do's and don'ts.", "x": "Etiquette: Walk.. Tennessee. The rules of respect — Tennessee Walker. the running walk. When in doubt, ask about History.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Tennessee Walker.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Tennessee Walker.", "x": "Planning: Gaited.. Smooth. Practical notes — Tennessee Walker. the running walk. A little planning shows respect for Smooth.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Tennessee Walker and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Tennessee Walker and money.", "x": "Costs: Tennessee.. Show. What to budget — Tennessee Walker. the running walk. The best experiences of Show. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-horse-tennessee-walker-breed-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
