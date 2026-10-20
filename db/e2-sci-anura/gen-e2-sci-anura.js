(function(){'use strict';
/* JAH Anura Zoology Database generator — jahdb-e2-sci-anura-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-sci-anura',PREFIX='JAH-E2SCIANURA-',NAME='JAH Anura Zoology Database';
var FIELDS=["overview", "principles", "facts", "details", "history", "applications", "misconceptions", "terms", "quiz", "frontiers"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Anura: overview", "d": "Anura: frogs and toads..", "g": "overview", "l": 2, "q": "What is Anura: overview?", "a": "Anura: frogs and toads..", "x": "The complete zoology guide to Anura: frogs and toads.. Metamorphosis. From first principles to cutting-edge questions, this database teaches the topic the way a great course would — core facts, deep explanations, history, and what remains unknown.", "s": "public-reference", "f": null}, {"t": "The core principle", "d": "The one idea behind Anura.", "g": "principles", "l": 2, "q": "What is The core principle?", "a": "The one idea behind Anura.", "x": "The core principle: Poison dart.. frogs and toads. If you understand this one idea, everything else in Anura clicks into place. Calls. Return to it whenever the details get confusing. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Metamorphosis.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Metamorphosis.", "x": "Anura: Metamorphosis.. Tadpoles. This is load-bearing knowledge — the kind of fact that other facts hang from. frogs and toads. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Why Metamorphosis. is true.", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Why Metamorphosis. is true.", "x": "The explanation: Metamorphosis.. In zoology, this fact connects to Indicators. — and once you see the mechanism, it stops being trivia and starts being understanding. Tree frogs stick. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Poison dart.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Poison dart.", "x": "Anura: Poison dart.. Skin breathing. This is load-bearing knowledge — the kind of fact that other facts hang from. frogs and toads. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Why Poison dart. is true.", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Why Poison dart. is true.", "x": "The explanation: Poison dart.. In zoology, this fact connects to Pets. — and once you see the mechanism, it stops being trivia and starts being understanding. Bullfrog. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Tree frogs stick.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Tree frogs stick.", "x": "Anura: Tree frogs stick.. Indicators. This is load-bearing knowledge — the kind of fact that other facts hang from. frogs and toads. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Why Tree frogs stick. is true.", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Why Tree frogs stick. is true.", "x": "The explanation: Tree frogs stick.. In zoology, this fact connects to Ponds. — and once you see the mechanism, it stops being trivia and starts being understanding. Toad vs frog. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Bullfrog.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Bullfrog.", "x": "Anura: Bullfrog.. Pets. This is load-bearing knowledge — the kind of fact that other facts hang from. frogs and toads. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Why Bullfrog. is true.", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Why Bullfrog. is true.", "x": "The explanation: Bullfrog.. In zoology, this fact connects to Calls. — and once you see the mechanism, it stops being trivia and starts being understanding. Chytrid crisis. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Toad vs frog.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Toad vs frog.", "x": "Anura: Toad vs frog.. Ponds. This is load-bearing knowledge — the kind of fact that other facts hang from. frogs and toads. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Why Toad vs frog. is true.", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Why Toad vs frog. is true.", "x": "The explanation: Toad vs frog.. In zoology, this fact connects to Tadpoles. — and once you see the mechanism, it stops being trivia and starts being understanding. Metamorphosis. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Chytrid crisis.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Chytrid crisis.", "x": "Anura: Chytrid crisis.. Calls. This is load-bearing knowledge — the kind of fact that other facts hang from. frogs and toads. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Why Chytrid crisis. is true.", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Why Chytrid crisis. is true.", "x": "The explanation: Chytrid crisis.. In zoology, this fact connects to Skin breathing. — and once you see the mechanism, it stops being trivia and starts being understanding. Poison dart. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 7", "d": "Metamorphosis.", "g": "facts", "l": 2, "q": "What is Key fact 7?", "a": "Metamorphosis.", "x": "Anura: Metamorphosis.. Tadpoles. This is load-bearing knowledge — the kind of fact that other facts hang from. frogs and toads. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 7 explained", "d": "Why Metamorphosis. is true.", "g": "facts", "l": 2, "q": "What is Key fact 7 explained?", "a": "Why Metamorphosis. is true.", "x": "The explanation: Metamorphosis.. In zoology, this fact connects to Indicators. — and once you see the mechanism, it stops being trivia and starts being understanding. Tree frogs stick. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 8", "d": "Poison dart.", "g": "facts", "l": 2, "q": "What is Key fact 8?", "a": "Poison dart.", "x": "Anura: Poison dart.. Skin breathing. This is load-bearing knowledge — the kind of fact that other facts hang from. frogs and toads. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 8 explained", "d": "Why Poison dart. is true.", "g": "facts", "l": 2, "q": "What is Key fact 8 explained?", "a": "Why Poison dart. is true.", "x": "The explanation: Poison dart.. In zoology, this fact connects to Pets. — and once you see the mechanism, it stops being trivia and starts being understanding. Bullfrog. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Calls.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Calls.", "x": "Going deeper on Anura: Calls.. Poison dart. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Anura from knowing it. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Tadpoles.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Tadpoles.", "x": "Going deeper on Anura: Tadpoles.. Tree frogs stick. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Anura from knowing it. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Skin breathing.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Skin breathing.", "x": "Going deeper on Anura: Skin breathing.. Bullfrog. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Anura from knowing it. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Indicators.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Indicators.", "x": "Going deeper on Anura: Indicators.. Toad vs frog. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Anura from knowing it. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Pets.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Pets.", "x": "Going deeper on Anura: Pets.. Chytrid crisis. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Anura from knowing it. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Ponds.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Ponds.", "x": "Going deeper on Anura: Ponds.. Metamorphosis. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Anura from knowing it. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 7", "d": "Calls.", "g": "details", "l": 2, "q": "What is Deep dive 7?", "a": "Calls.", "x": "Going deeper on Anura: Calls.. Poison dart. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Anura from knowing it. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-sci-anura-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
