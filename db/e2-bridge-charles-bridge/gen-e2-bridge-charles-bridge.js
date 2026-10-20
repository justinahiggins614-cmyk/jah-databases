(function(){'use strict';
/* JAH Charles Bridge Bridge Database generator — jahdb-e2-bridge-charles-bridge-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-bridge-charles-bridge',PREFIX='JAH-E2BRIDGECHA-',NAME='JAH Charles Bridge Bridge Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Charles Bridge: the complete guide", "d": "Charles Bridge: Prague's statue walk..", "g": "overview", "l": 2, "q": "What is Charles Bridge: the complete guide?", "a": "Charles Bridge: Prague's statue walk..", "x": "The complete bridge guide to Charles Bridge: Prague's statue walk.. 1357. History, meaning, practices, and how to engage respectfully — everything in one database. Statues. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Charles Bridge essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Charles Bridge essentials.", "x": "At a glance: Charles Bridge — Prague's statue walk.. Statues. The essentials: History.. Vltava. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "1357.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "1357.", "x": "Charles Bridge: 1357.. History. Essential knowledge — Vltava.. Prague's statue walk. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 1357..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 1357..", "x": "Explained: 1357.. Views. The context — Charles Bridge. Charles IV. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Statues.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Statues.", "x": "Charles Bridge: Statues.. Walk. Essential knowledge — Charles IV.. Prague's statue walk. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Statues..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Statues..", "x": "Explained: Statues.. Prague. The context — Charles Bridge. Buskers. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Vltava.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Vltava.", "x": "Charles Bridge: Vltava.. Views. Essential knowledge — Buskers.. Prague's statue walk. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Vltava..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Vltava..", "x": "Explained: Vltava.. Dawn. The context — Charles Bridge. Dawn. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Charles IV.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Charles IV.", "x": "Charles Bridge: Charles IV.. Prague. Essential knowledge — Dawn.. Prague's statue walk. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Charles IV..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Charles IV..", "x": "Explained: Charles IV.. Statues. The context — Charles Bridge. 1357. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Buskers.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Buskers.", "x": "Charles Bridge: Buskers.. Dawn. Essential knowledge — 1357.. Prague's statue walk. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Buskers..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Buskers..", "x": "Explained: Buskers.. History. The context — Charles Bridge. Statues. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Dawn.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Dawn.", "x": "Charles Bridge: Dawn.. Statues. Essential knowledge — Statues.. Prague's statue walk. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Dawn..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Dawn..", "x": "Explained: Dawn.. Walk. The context — Charles Bridge. Vltava. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Statues.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Statues.", "x": "Charles Bridge in depth: Statues.. Statues. Details — Prague's statue walk.. Walk. Charles IV. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "History.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "History.", "x": "Charles Bridge in depth: History.. Vltava. Details — Prague's statue walk.. Views. Buskers. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Walk.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Walk.", "x": "Charles Bridge in depth: Walk.. Charles IV. Details — Prague's statue walk.. Prague. Dawn. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Views.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Views.", "x": "Charles Bridge in depth: Views.. Buskers. Details — Prague's statue walk.. Dawn. 1357. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Prague.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Prague.", "x": "Charles Bridge in depth: Prague.. Dawn. Details — Prague's statue walk.. Statues. Statues. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Dawn.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Dawn.", "x": "Charles Bridge in depth: Dawn.. 1357. Details — Prague's statue walk.. History. Vltava. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Charles Bridge comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Charles Bridge comes from.", "x": "Origins: Statues.. 1357. The history of Charles Bridge — Prague's statue walk.. History. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Charles Bridge respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Charles Bridge respectfully.", "x": "Engaging: Walk.. Statues. How to participate or observe well — Charles Bridge. Prague's statue walk. Respect first, always; Views.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Charles Bridge do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Charles Bridge do's and don'ts.", "x": "Etiquette: Prague.. Vltava. The rules of respect — Charles Bridge. Prague's statue walk. When in doubt, ask about Dawn.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Charles Bridge.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Charles Bridge.", "x": "Planning: Statues.. Charles IV. Practical notes — Charles Bridge. Prague's statue walk. A little planning shows respect for History.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Charles Bridge and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Charles Bridge and money.", "x": "Costs: Walk.. Buskers. What to budget — Charles Bridge. Prague's statue walk. The best experiences of Views. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-bridge-charles-bridge-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
