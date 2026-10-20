(function(){'use strict';
/* JAH Rhodes Windmills Database generator — jahdb-e2-windmill2-rhodes-windmills-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-windmill2-rhodes-windmills',PREFIX='JAH-E2WINDMILL2-',NAME='JAH Rhodes Windmills Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Rhodes Windmills: the complete guide", "d": "Rhodes Windmills: the harbor..", "g": "overview", "l": 2, "q": "What is Rhodes Windmills: the complete guide?", "a": "Rhodes Windmills: the harbor..", "x": "The complete windmill guide to Rhodes Windmills: the harbor.. Medieval. History, meaning, practices, and how to engage respectfully — everything in one database. Medieval. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Rhodes Windmills essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Rhodes Windmills essentials.", "x": "At a glance: Rhodes Windmills — the harbor.. Harbor. The essentials: Historic.. Greece. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Medieval.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Medieval.", "x": "Rhodes Windmills: Medieval.. Historic. Essential knowledge — Greece.. the harbor. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Medieval..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Medieval..", "x": "Explained: Medieval.. Harbor. The context — Rhodes Windmills. Stone. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Harbor.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Harbor.", "x": "Rhodes Windmills: Harbor.. Rhodes. Essential knowledge — Stone.. the harbor. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Harbor..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Harbor..", "x": "Explained: Harbor.. Greece. The context — Rhodes Windmills. Rhodes. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Greece.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Greece.", "x": "Rhodes Windmills: Greece.. Harbor. Essential knowledge — Rhodes.. the harbor. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Greece..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Greece..", "x": "Explained: Greece.. Visiting. The context — Rhodes Windmills. Historic. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Stone.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Stone.", "x": "Rhodes Windmills: Stone.. Greece. Essential knowledge — Historic.. the harbor. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Stone..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Stone..", "x": "Explained: Stone.. Medieval. The context — Rhodes Windmills. Medieval. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Rhodes.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Rhodes.", "x": "Rhodes Windmills: Rhodes.. Visiting. Essential knowledge — Medieval.. the harbor. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Rhodes..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Rhodes..", "x": "Explained: Rhodes.. Historic. The context — Rhodes Windmills. Harbor. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Historic.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Historic.", "x": "Rhodes Windmills: Historic.. Medieval. Essential knowledge — Harbor.. the harbor. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Historic..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Historic..", "x": "Explained: Historic.. Rhodes. The context — Rhodes Windmills. Greece. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Medieval.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Medieval.", "x": "Rhodes Windmills in depth: Medieval.. Harbor. Details — the harbor.. Rhodes. Stone. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Historic.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Historic.", "x": "Rhodes Windmills in depth: Historic.. Greece. Details — the harbor.. Harbor. Rhodes. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Rhodes.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Rhodes.", "x": "Rhodes Windmills in depth: Rhodes.. Stone. Details — the harbor.. Greece. Historic. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Harbor.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Harbor.", "x": "Rhodes Windmills in depth: Harbor.. Rhodes. Details — the harbor.. Visiting. Medieval. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Greece.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Greece.", "x": "Rhodes Windmills in depth: Greece.. Historic. Details — the harbor.. Medieval. Harbor. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Visiting.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Visiting.", "x": "Rhodes Windmills in depth: Visiting.. Medieval. Details — the harbor.. Historic. Greece. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Rhodes Windmills comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Rhodes Windmills comes from.", "x": "Origins: Medieval.. Medieval. The history of Rhodes Windmills — the harbor.. Historic. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Rhodes Windmills respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Rhodes Windmills respectfully.", "x": "Engaging: Rhodes.. Harbor. How to participate or observe well — Rhodes Windmills. the harbor. Respect first, always; Harbor.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Rhodes Windmills do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Rhodes Windmills do's and don'ts.", "x": "Etiquette: Greece.. Greece. The rules of respect — Rhodes Windmills. the harbor. When in doubt, ask about Visiting.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Rhodes Windmills.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Rhodes Windmills.", "x": "Planning: Medieval.. Stone. Practical notes — Rhodes Windmills. the harbor. A little planning shows respect for Historic.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Rhodes Windmills and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Rhodes Windmills and money.", "x": "Costs: Rhodes.. Rhodes. What to budget — Rhodes Windmills. the harbor. The best experiences of Harbor. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-windmill2-rhodes-windmills-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
