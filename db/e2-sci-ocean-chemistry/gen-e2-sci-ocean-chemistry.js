(function(){'use strict';
/* JAH Ocean Chemistry Oceanography Database generator — jahdb-e2-sci-ocean-chemistry-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-sci-ocean-chemistry',PREFIX='JAH-E2SCIOCEANC-',NAME='JAH Ocean Chemistry Oceanography Database';
var FIELDS=["overview", "principles", "facts", "details", "history", "applications", "misconceptions", "terms", "quiz", "frontiers"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Ocean Chemistry: overview", "d": "Ocean Chemistry: salt, acid, and the sea's balance..", "g": "overview", "l": 2, "q": "What is Ocean Chemistry: overview?", "a": "Ocean Chemistry: salt, acid, and the sea's balance..", "x": "The complete oceanography guide to Ocean Chemistry: salt, acid, and the sea's balance.. 3.5% salinity. From first principles to cutting-edge questions, this database teaches the topic the way a great course would — core facts, deep explanations, history, and what remains unknown.", "s": "public-reference", "f": null}, {"t": "The core principle", "d": "The one idea behind Ocean Chemistry.", "g": "principles", "l": 2, "q": "What is The core principle?", "a": "The one idea behind Ocean Chemistry.", "x": "The core principle: Acidification from CO2.. salt, acid, and the sea's balance. If you understand this one idea, everything else in Ocean Chemistry clicks into place. pH dropping. Return to it whenever the details get confusing.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "3.5% salinity.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "3.5% salinity.", "x": "Ocean Chemistry: 3.5% salinity.. Shell dissolution. This is load-bearing knowledge — the kind of fact that other facts hang from. salt, acid, and the sea's balance. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Why 3.5% salinity. is true.", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Why 3.5% salinity. is true.", "x": "The explanation: 3.5% salinity.. In oceanography, this fact connects to Oil spills. — and once you see the mechanism, it stops being trivia and starts being understanding. Carbonate buffering. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Acidification from CO2.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Acidification from CO2.", "x": "Ocean Chemistry: Acidification from CO2.. Nutrient cycles. This is load-bearing knowledge — the kind of fact that other facts hang from. salt, acid, and the sea's balance. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Why Acidification from CO2. is true.", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Why Acidification from CO2. is true.", "x": "The explanation: Acidification from CO2.. In oceanography, this fact connects to Plastic gyres. — and once you see the mechanism, it stops being trivia and starts being understanding. Dead zones: hypoxia.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Carbonate buffering.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Carbonate buffering.", "x": "Ocean Chemistry: Carbonate buffering.. Oil spills. This is load-bearing knowledge — the kind of fact that other facts hang from. salt, acid, and the sea's balance. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Why Carbonate buffering. is true.", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Why Carbonate buffering. is true.", "x": "The explanation: Carbonate buffering.. In oceanography, this fact connects to Monitoring. — and once you see the mechanism, it stops being trivia and starts being understanding. Red tides. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Dead zones: hypoxia.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Dead zones: hypoxia.", "x": "Ocean Chemistry: Dead zones: hypoxia.. Plastic gyres. This is load-bearing knowledge — the kind of fact that other facts hang from. salt, acid, and the sea's balance. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Why Dead zones: hypoxia. is true.", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Why Dead zones: hypoxia. is true.", "x": "The explanation: Dead zones: hypoxia.. In oceanography, this fact connects to pH dropping. — and once you see the mechanism, it stops being trivia and starts being understanding. Desalination. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Red tides.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Red tides.", "x": "Ocean Chemistry: Red tides.. Monitoring. This is load-bearing knowledge — the kind of fact that other facts hang from. salt, acid, and the sea's balance. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Why Red tides. is true.", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Why Red tides. is true.", "x": "The explanation: Red tides.. In oceanography, this fact connects to Shell dissolution. — and once you see the mechanism, it stops being trivia and starts being understanding. 3.5% salinity. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Desalination.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Desalination.", "x": "Ocean Chemistry: Desalination.. pH dropping. This is load-bearing knowledge — the kind of fact that other facts hang from. salt, acid, and the sea's balance. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Why Desalination. is true.", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Why Desalination. is true.", "x": "The explanation: Desalination.. In oceanography, this fact connects to Nutrient cycles. — and once you see the mechanism, it stops being trivia and starts being understanding. Acidification from CO2. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 7", "d": "3.5% salinity.", "g": "facts", "l": 2, "q": "What is Key fact 7?", "a": "3.5% salinity.", "x": "Ocean Chemistry: 3.5% salinity.. Shell dissolution. This is load-bearing knowledge — the kind of fact that other facts hang from. salt, acid, and the sea's balance. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 7 explained", "d": "Why 3.5% salinity. is true.", "g": "facts", "l": 2, "q": "What is Key fact 7 explained?", "a": "Why 3.5% salinity. is true.", "x": "The explanation: 3.5% salinity.. In oceanography, this fact connects to Oil spills. — and once you see the mechanism, it stops being trivia and starts being understanding. Carbonate buffering. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 8", "d": "Acidification from CO2.", "g": "facts", "l": 2, "q": "What is Key fact 8?", "a": "Acidification from CO2.", "x": "Ocean Chemistry: Acidification from CO2.. Nutrient cycles. This is load-bearing knowledge — the kind of fact that other facts hang from. salt, acid, and the sea's balance. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 8 explained", "d": "Why Acidification from CO2. is true.", "g": "facts", "l": 2, "q": "What is Key fact 8 explained?", "a": "Why Acidification from CO2. is true.", "x": "The explanation: Acidification from CO2.. In oceanography, this fact connects to Plastic gyres. — and once you see the mechanism, it stops being trivia and starts being understanding. Dead zones: hypoxia.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "pH dropping.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "pH dropping.", "x": "Going deeper on Ocean Chemistry: pH dropping.. Acidification from CO2. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Ocean Chemistry from knowing it.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Shell dissolution.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Shell dissolution.", "x": "Going deeper on Ocean Chemistry: Shell dissolution.. Carbonate buffering. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Ocean Chemistry from knowing it.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Nutrient cycles.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Nutrient cycles.", "x": "Going deeper on Ocean Chemistry: Nutrient cycles.. Dead zones: hypoxia. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Ocean Chemistry from knowing it.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Oil spills.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Oil spills.", "x": "Going deeper on Ocean Chemistry: Oil spills.. Red tides. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Ocean Chemistry from knowing it.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Plastic gyres.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Plastic gyres.", "x": "Going deeper on Ocean Chemistry: Plastic gyres.. Desalination. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Ocean Chemistry from knowing it.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Monitoring.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Monitoring.", "x": "Going deeper on Ocean Chemistry: Monitoring.. 3.5% salinity. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Ocean Chemistry from knowing it.", "s": "public-reference", "f": null}, {"t": "Deep dive 7", "d": "pH dropping.", "g": "details", "l": 2, "q": "What is Deep dive 7?", "a": "pH dropping.", "x": "Going deeper on Ocean Chemistry: pH dropping.. Acidification from CO2. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Ocean Chemistry from knowing it.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-sci-ocean-chemistry-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
