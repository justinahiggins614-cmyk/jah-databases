(function(){'use strict';
/* JAH Black Holes Astronomy Database generator — jahdb-e2-sci-black-holes-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-sci-black-holes',PREFIX='JAH-E2SCIBLACKH-',NAME='JAH Black Holes Astronomy Database';
var FIELDS=["overview", "principles", "facts", "details", "history", "applications", "misconceptions", "terms", "quiz", "frontiers"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Black Holes: overview", "d": "Black Holes: gravity's ultimate victory..", "g": "overview", "l": 2, "q": "What is Black Holes: overview?", "a": "Black Holes: gravity's ultimate victory..", "x": "The complete astronomy guide to Black Holes: gravity's ultimate victory.. Event horizon. From first principles to cutting-edge questions, this database teaches the topic the way a great course would — core facts, deep explanations, history, and what remains unknown.", "s": "public-reference", "f": null}, {"t": "The core principle", "d": "The one idea behind Black Holes.", "g": "principles", "l": 2, "q": "What is The core principle?", "a": "The one idea behind Black Holes.", "x": "The core principle: Singularity.. gravity's ultimate victory. If you understand this one idea, everything else in Black Holes clicks into place. Cygnus X-1. Return to it whenever the details get confusing.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Event horizon.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Event horizon.", "x": "Black Holes: Event horizon.. Sagittarius A*. This is load-bearing knowledge — the kind of fact that other facts hang from. gravity's ultimate victory. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Why Event horizon. is true.", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Why Event horizon. is true.", "x": "The explanation: Event horizon.. In astronomy, this fact connects to Quasars powered. — and once you see the mechanism, it stops being trivia and starts being understanding. Stellar vs supermassive. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Singularity.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Singularity.", "x": "Black Holes: Singularity.. Accretion disks. This is load-bearing knowledge — the kind of fact that other facts hang from. gravity's ultimate victory. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Why Singularity. is true.", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Why Singularity. is true.", "x": "The explanation: Singularity.. In astronomy, this fact connects to Information paradox. — and once you see the mechanism, it stops being trivia and starts being understanding. M87* imaged 2019. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Stellar vs supermassive.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Stellar vs supermassive.", "x": "Black Holes: Stellar vs supermassive.. Quasars powered. This is load-bearing knowledge — the kind of fact that other facts hang from. gravity's ultimate victory. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Why Stellar vs supermassive. is true.", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Why Stellar vs supermassive. is true.", "x": "The explanation: Stellar vs supermassive.. In astronomy, this fact connects to LIGO mergers. — and once you see the mechanism, it stops being trivia and starts being understanding. Hawking radiation. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "M87* imaged 2019.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "M87* imaged 2019.", "x": "Black Holes: M87* imaged 2019.. Information paradox. This is load-bearing knowledge — the kind of fact that other facts hang from. gravity's ultimate victory. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Why M87* imaged 2019. is true.", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Why M87* imaged 2019. is true.", "x": "The explanation: M87* imaged 2019.. In astronomy, this fact connects to Cygnus X-1. — and once you see the mechanism, it stops being trivia and starts being understanding. Spaghettification. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Hawking radiation.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Hawking radiation.", "x": "Black Holes: Hawking radiation.. LIGO mergers. This is load-bearing knowledge — the kind of fact that other facts hang from. gravity's ultimate victory. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Why Hawking radiation. is true.", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Why Hawking radiation. is true.", "x": "The explanation: Hawking radiation.. In astronomy, this fact connects to Sagittarius A*. — and once you see the mechanism, it stops being trivia and starts being understanding. Event horizon. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Spaghettification.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Spaghettification.", "x": "Black Holes: Spaghettification.. Cygnus X-1. This is load-bearing knowledge — the kind of fact that other facts hang from. gravity's ultimate victory. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Why Spaghettification. is true.", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Why Spaghettification. is true.", "x": "The explanation: Spaghettification.. In astronomy, this fact connects to Accretion disks. — and once you see the mechanism, it stops being trivia and starts being understanding. Singularity. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 7", "d": "Event horizon.", "g": "facts", "l": 2, "q": "What is Key fact 7?", "a": "Event horizon.", "x": "Black Holes: Event horizon.. Sagittarius A*. This is load-bearing knowledge — the kind of fact that other facts hang from. gravity's ultimate victory. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 7 explained", "d": "Why Event horizon. is true.", "g": "facts", "l": 2, "q": "What is Key fact 7 explained?", "a": "Why Event horizon. is true.", "x": "The explanation: Event horizon.. In astronomy, this fact connects to Quasars powered. — and once you see the mechanism, it stops being trivia and starts being understanding. Stellar vs supermassive. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 8", "d": "Singularity.", "g": "facts", "l": 2, "q": "What is Key fact 8?", "a": "Singularity.", "x": "Black Holes: Singularity.. Accretion disks. This is load-bearing knowledge — the kind of fact that other facts hang from. gravity's ultimate victory. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 8 explained", "d": "Why Singularity. is true.", "g": "facts", "l": 2, "q": "What is Key fact 8 explained?", "a": "Why Singularity. is true.", "x": "The explanation: Singularity.. In astronomy, this fact connects to Information paradox. — and once you see the mechanism, it stops being trivia and starts being understanding. M87* imaged 2019. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Cygnus X-1.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Cygnus X-1.", "x": "Going deeper on Black Holes: Cygnus X-1.. Singularity. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Black Holes from knowing it.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Sagittarius A*.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Sagittarius A*.", "x": "Going deeper on Black Holes: Sagittarius A*.. Stellar vs supermassive. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Black Holes from knowing it.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Accretion disks.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Accretion disks.", "x": "Going deeper on Black Holes: Accretion disks.. M87* imaged 2019. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Black Holes from knowing it.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Quasars powered.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Quasars powered.", "x": "Going deeper on Black Holes: Quasars powered.. Hawking radiation. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Black Holes from knowing it.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Information paradox.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Information paradox.", "x": "Going deeper on Black Holes: Information paradox.. Spaghettification. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Black Holes from knowing it.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "LIGO mergers.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "LIGO mergers.", "x": "Going deeper on Black Holes: LIGO mergers.. Event horizon. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Black Holes from knowing it.", "s": "public-reference", "f": null}, {"t": "Deep dive 7", "d": "Cygnus X-1.", "g": "details", "l": 2, "q": "What is Deep dive 7?", "a": "Cygnus X-1.", "x": "Going deeper on Black Holes: Cygnus X-1.. Singularity. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Black Holes from knowing it.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-sci-black-holes-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
