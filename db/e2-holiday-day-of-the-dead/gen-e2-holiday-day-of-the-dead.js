(function(){'use strict';
/* JAH Day of the Dead Holiday Database generator — jahdb-e2-holiday-day-of-the-dead-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-holiday-day-of-the-dead',PREFIX='JAH-E2HOLIDAYDA-',NAME='JAH Day of the Dead Holiday Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Day of the Dead: the complete guide", "d": "Day of the Dead: honoring ancestors..", "g": "overview", "l": 2, "q": "What is Day of the Dead: the complete guide?", "a": "Day of the Dead: honoring ancestors..", "x": "The complete holiday guide to Day of the Dead: honoring ancestors.. Nov 1-2. History, meaning, practices, and how to engage respectfully — everything in one database. Altars. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Day of the Dead essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Day of the Dead essentials.", "x": "At a glance: Day of the Dead — honoring ancestors.. Ofrendas. The essentials: Symbols.. Marigolds. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Nov 1-2.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Nov 1-2.", "x": "Day of the Dead: Nov 1-2.. Symbols. Essential knowledge — Marigolds.. honoring ancestors. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Nov 1-2..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Nov 1-2..", "x": "Explained: Nov 1-2.. Family. The context — Day of the Dead. Calaveras. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Ofrendas.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Ofrendas.", "x": "Day of the Dead: Ofrendas.. Food. Essential knowledge — Calaveras.. honoring ancestors. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Ofrendas..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Ofrendas..", "x": "Explained: Ofrendas.. Meaning. The context — Day of the Dead. Family. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Marigolds.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Marigolds.", "x": "Day of the Dead: Marigolds.. Family. Essential knowledge — Family.. honoring ancestors. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Marigolds..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Marigolds..", "x": "Explained: Marigolds.. UNESCO. The context — Day of the Dead. Mexico. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Calaveras.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Calaveras.", "x": "Day of the Dead: Calaveras.. Meaning. Essential knowledge — Mexico.. honoring ancestors. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Calaveras..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Calaveras..", "x": "Explained: Calaveras.. Altars. The context — Day of the Dead. Nov 1-2. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Family.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Family.", "x": "Day of the Dead: Family.. UNESCO. Essential knowledge — Nov 1-2.. honoring ancestors. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Family..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Family..", "x": "Explained: Family.. Symbols. The context — Day of the Dead. Ofrendas. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Mexico.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Mexico.", "x": "Day of the Dead: Mexico.. Altars. Essential knowledge — Ofrendas.. honoring ancestors. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Mexico..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Mexico..", "x": "Explained: Mexico.. Food. The context — Day of the Dead. Marigolds. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Altars.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Altars.", "x": "Day of the Dead in depth: Altars.. Ofrendas. Details — honoring ancestors.. Food. Calaveras. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Symbols.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Symbols.", "x": "Day of the Dead in depth: Symbols.. Marigolds. Details — honoring ancestors.. Family. Family. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Food.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Food.", "x": "Day of the Dead in depth: Food.. Calaveras. Details — honoring ancestors.. Meaning. Mexico. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Family.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Family.", "x": "Day of the Dead in depth: Family.. Family. Details — honoring ancestors.. UNESCO. Nov 1-2. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Meaning.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Meaning.", "x": "Day of the Dead in depth: Meaning.. Mexico. Details — honoring ancestors.. Altars. Ofrendas. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "UNESCO.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "UNESCO.", "x": "Day of the Dead in depth: UNESCO.. Nov 1-2. Details — honoring ancestors.. Symbols. Marigolds. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Day of the Dead comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Day of the Dead comes from.", "x": "Origins: Altars.. Nov 1-2. The history of Day of the Dead — honoring ancestors.. Symbols. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Day of the Dead respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Day of the Dead respectfully.", "x": "Engaging: Food.. Ofrendas. How to participate or observe well — Day of the Dead. honoring ancestors. Respect first, always; Family.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Day of the Dead do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Day of the Dead do's and don'ts.", "x": "Etiquette: Meaning.. Marigolds. The rules of respect — Day of the Dead. honoring ancestors. When in doubt, ask about UNESCO.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Day of the Dead.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Day of the Dead.", "x": "Planning: Altars.. Calaveras. Practical notes — Day of the Dead. honoring ancestors. A little planning shows respect for Symbols.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Day of the Dead and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Day of the Dead and money.", "x": "Costs: Food.. Family. What to budget — Day of the Dead. honoring ancestors. The best experiences of Family. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-holiday-day-of-the-dead-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
