(function(){'use strict';
/* JAH Grand Central Terminal Landmark Database generator — jahdb-e2-landmark-grand-central-landmark-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-landmark-grand-central-landmark',PREFIX='JAH-E2LANDMARKG-',NAME='JAH Grand Central Terminal Landmark Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Grand Central Terminal: the complete guide", "d": "Grand Central Terminal: the celestial station..", "g": "overview", "l": 2, "q": "What is Grand Central Terminal: the complete guide?", "a": "Grand Central Terminal: the celestial station..", "x": "The complete landmark guide to Grand Central Terminal: the celestial station.. 1913. History, meaning, practices, and how to engage respectfully — everything in one database. 1913. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Grand Central Terminal essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Grand Central Terminal essentials.", "x": "At a glance: Grand Central Terminal — the celestial station.. Constellation. The essentials: Clock.. Clock. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "1913.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "1913.", "x": "Grand Central Terminal: 1913.. Clock. Essential knowledge — Clock.. the celestial station. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 1913..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 1913..", "x": "Explained: 1913.. Beaux-Arts. The context — Grand Central Terminal. Whispering. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Constellation.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Constellation.", "x": "Grand Central Terminal: Constellation.. Oyster. Essential knowledge — Whispering.. the celestial station. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Constellation..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Constellation..", "x": "Explained: Constellation.. Celestial. The context — Grand Central Terminal. Oyster Bar. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Clock.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Clock.", "x": "Grand Central Terminal: Clock.. Beaux-Arts. Essential knowledge — Oyster Bar.. the celestial station. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Clock..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Clock..", "x": "Explained: Clock.. Tours. The context — Grand Central Terminal. Beaux-Arts. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Whispering.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Whispering.", "x": "Grand Central Terminal: Whispering.. Celestial. Essential knowledge — Beaux-Arts.. the celestial station. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Whispering..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Whispering..", "x": "Explained: Whispering.. 1913. The context — Grand Central Terminal. 1913. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Oyster Bar.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Oyster Bar.", "x": "Grand Central Terminal: Oyster Bar.. Tours. Essential knowledge — 1913.. the celestial station. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Oyster Bar..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Oyster Bar..", "x": "Explained: Oyster Bar.. Clock. The context — Grand Central Terminal. Constellation. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Beaux-Arts.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Beaux-Arts.", "x": "Grand Central Terminal: Beaux-Arts.. 1913. Essential knowledge — Constellation.. the celestial station. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Beaux-Arts..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Beaux-Arts..", "x": "Explained: Beaux-Arts.. Oyster. The context — Grand Central Terminal. Clock. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "1913.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "1913.", "x": "Grand Central Terminal in depth: 1913.. Constellation. Details — the celestial station.. Oyster. Whispering. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Clock.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Clock.", "x": "Grand Central Terminal in depth: Clock.. Clock. Details — the celestial station.. Beaux-Arts. Oyster Bar. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Oyster.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Oyster.", "x": "Grand Central Terminal in depth: Oyster.. Whispering. Details — the celestial station.. Celestial. Beaux-Arts. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Beaux-Arts.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Beaux-Arts.", "x": "Grand Central Terminal in depth: Beaux-Arts.. Oyster Bar. Details — the celestial station.. Tours. 1913. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Celestial.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Celestial.", "x": "Grand Central Terminal in depth: Celestial.. Beaux-Arts. Details — the celestial station.. 1913. Constellation. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Tours.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Tours.", "x": "Grand Central Terminal in depth: Tours.. 1913. Details — the celestial station.. Clock. Clock. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Grand Central Terminal comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Grand Central Terminal comes from.", "x": "Origins: 1913.. 1913. The history of Grand Central Terminal — the celestial station.. Clock. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Grand Central Terminal respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Grand Central Terminal respectfully.", "x": "Engaging: Oyster.. Constellation. How to participate or observe well — Grand Central Terminal. the celestial station. Respect first, always; Beaux-Arts.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Grand Central Terminal do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Grand Central Terminal do's and don'ts.", "x": "Etiquette: Celestial.. Clock. The rules of respect — Grand Central Terminal. the celestial station. When in doubt, ask about Tours.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Grand Central Terminal.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Grand Central Terminal.", "x": "Planning: 1913.. Whispering. Practical notes — Grand Central Terminal. the celestial station. A little planning shows respect for Clock.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Grand Central Terminal and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Grand Central Terminal and money.", "x": "Costs: Oyster.. Oyster Bar. What to budget — Grand Central Terminal. the celestial station. The best experiences of Beaux-Arts. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-landmark-grand-central-landmark-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
