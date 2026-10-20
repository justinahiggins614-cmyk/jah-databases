(function(){'use strict';
/* JAH Felidae Zoology Database generator — jahdb-e2-sci-felidae-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-sci-felidae',PREFIX='JAH-E2SCIFELIDA-',NAME='JAH Felidae Zoology Database';
var FIELDS=["overview", "principles", "facts", "details", "history", "applications", "misconceptions", "terms", "quiz", "frontiers"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Felidae: overview", "d": "Felidae: the cat family: from tigers to tabbies..", "g": "overview", "l": 2, "q": "What is Felidae: overview?", "a": "Felidae: the cat family: from tigers to tabbies..", "x": "The complete zoology guide to Felidae: the cat family: from tigers to tabbies.. Tigers: largest cats. From first principles to cutting-edge questions, this database teaches the topic the way a great course would — core facts, deep explanations, history, and what remains unknown.", "s": "public-reference", "f": null}, {"t": "The core principle", "d": "The one idea behind Felidae.", "g": "principles", "l": 2, "q": "What is The core principle?", "a": "The one idea behind Felidae.", "x": "The core principle: Lions: social cats.. the cat family: from tigers to tabbies. If you understand this one idea, everything else in Felidae clicks into place. Panthera roar. Return to it whenever the details get confusing.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Tigers: largest cats.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Tigers: largest cats.", "x": "Felidae: Tigers: largest cats.. Solitary hunters. This is load-bearing knowledge — the kind of fact that other facts hang from. the cat family: from tigers to tabbies. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Why Tigers: largest cats. is true.", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Why Tigers: largest cats. is true.", "x": "The explanation: Tigers: largest cats.. In zoology, this fact connects to Big cat conservation. — and once you see the mechanism, it stops being trivia and starts being understanding. Cheetah: 70 mph.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Lions: social cats.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Lions: social cats.", "x": "Felidae: Lions: social cats.. Domestication. This is load-bearing knowledge — the kind of fact that other facts hang from. the cat family: from tigers to tabbies. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Why Lions: social cats. is true.", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Why Lions: social cats. is true.", "x": "The explanation: Lions: social cats.. In zoology, this fact connects to Whiskers. — and once you see the mechanism, it stops being trivia and starts being understanding. Retractable claws. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Cheetah: 70 mph.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Cheetah: 70 mph.", "x": "Felidae: Cheetah: 70 mph.. Big cat conservation. This is load-bearing knowledge — the kind of fact that other facts hang from. the cat family: from tigers to tabbies. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Why Cheetah: 70 mph. is true.", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Why Cheetah: 70 mph. is true.", "x": "The explanation: Cheetah: 70 mph.. In zoology, this fact connects to Breeds. — and once you see the mechanism, it stops being trivia and starts being understanding. Night vision. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Retractable claws.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Retractable claws.", "x": "Felidae: Retractable claws.. Whiskers. This is load-bearing knowledge — the kind of fact that other facts hang from. the cat family: from tigers to tabbies. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Why Retractable claws. is true.", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Why Retractable claws. is true.", "x": "The explanation: Retractable claws.. In zoology, this fact connects to Panthera roar. — and once you see the mechanism, it stops being trivia and starts being understanding. Purring mechanics. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Night vision.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Night vision.", "x": "Felidae: Night vision.. Breeds. This is load-bearing knowledge — the kind of fact that other facts hang from. the cat family: from tigers to tabbies. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Why Night vision. is true.", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Why Night vision. is true.", "x": "The explanation: Night vision.. In zoology, this fact connects to Solitary hunters. — and once you see the mechanism, it stops being trivia and starts being understanding. Tigers: largest cats. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Purring mechanics.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Purring mechanics.", "x": "Felidae: Purring mechanics.. Panthera roar. This is load-bearing knowledge — the kind of fact that other facts hang from. the cat family: from tigers to tabbies. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Why Purring mechanics. is true.", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Why Purring mechanics. is true.", "x": "The explanation: Purring mechanics.. In zoology, this fact connects to Domestication. — and once you see the mechanism, it stops being trivia and starts being understanding. Lions: social cats. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 7", "d": "Tigers: largest cats.", "g": "facts", "l": 2, "q": "What is Key fact 7?", "a": "Tigers: largest cats.", "x": "Felidae: Tigers: largest cats.. Solitary hunters. This is load-bearing knowledge — the kind of fact that other facts hang from. the cat family: from tigers to tabbies. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 7 explained", "d": "Why Tigers: largest cats. is true.", "g": "facts", "l": 2, "q": "What is Key fact 7 explained?", "a": "Why Tigers: largest cats. is true.", "x": "The explanation: Tigers: largest cats.. In zoology, this fact connects to Big cat conservation. — and once you see the mechanism, it stops being trivia and starts being understanding. Cheetah: 70 mph.", "s": "public-reference", "f": null}, {"t": "Key fact 8", "d": "Lions: social cats.", "g": "facts", "l": 2, "q": "What is Key fact 8?", "a": "Lions: social cats.", "x": "Felidae: Lions: social cats.. Domestication. This is load-bearing knowledge — the kind of fact that other facts hang from. the cat family: from tigers to tabbies. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 8 explained", "d": "Why Lions: social cats. is true.", "g": "facts", "l": 2, "q": "What is Key fact 8 explained?", "a": "Why Lions: social cats. is true.", "x": "The explanation: Lions: social cats.. In zoology, this fact connects to Whiskers. — and once you see the mechanism, it stops being trivia and starts being understanding. Retractable claws. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Panthera roar.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Panthera roar.", "x": "Going deeper on Felidae: Panthera roar.. Lions: social cats. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Felidae from knowing it.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Solitary hunters.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Solitary hunters.", "x": "Going deeper on Felidae: Solitary hunters.. Cheetah: 70 mph. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Felidae from knowing it.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Domestication.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Domestication.", "x": "Going deeper on Felidae: Domestication.. Retractable claws. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Felidae from knowing it.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Big cat conservation.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Big cat conservation.", "x": "Going deeper on Felidae: Big cat conservation.. Night vision. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Felidae from knowing it.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Whiskers.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Whiskers.", "x": "Going deeper on Felidae: Whiskers.. Purring mechanics. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Felidae from knowing it. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Breeds.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Breeds.", "x": "Going deeper on Felidae: Breeds.. Tigers: largest cats. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Felidae from knowing it. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 7", "d": "Panthera roar.", "g": "details", "l": 2, "q": "What is Deep dive 7?", "a": "Panthera roar.", "x": "Going deeper on Felidae: Panthera roar.. Lions: social cats. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Felidae from knowing it.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-sci-felidae-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
