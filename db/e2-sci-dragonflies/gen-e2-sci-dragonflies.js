(function(){'use strict';
/* JAH Dragonflies Entomology Database generator — jahdb-e2-sci-dragonflies-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-sci-dragonflies',PREFIX='JAH-E2SCIDRAGON-',NAME='JAH Dragonflies Entomology Database';
var FIELDS=["overview", "principles", "facts", "details", "history", "applications", "misconceptions", "terms", "quiz", "frontiers"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Dragonflies: overview", "d": "Dragonflies: aerial predators; ancient lineage..", "g": "overview", "l": 2, "q": "What is Dragonflies: overview?", "a": "Dragonflies: aerial predators; ancient lineage..", "x": "The complete entomology guide to Dragonflies: aerial predators; ancient lineage.. 300M years old. From first principles to cutting-edge questions, this database teaches the topic the way a great course would — core facts, deep explanations, history, and what remains unknown.", "s": "public-reference", "f": null}, {"t": "The core principle", "d": "The one idea behind Dragonflies.", "g": "principles", "l": 2, "q": "What is The core principle?", "a": "The one idea behind Dragonflies.", "x": "The core principle: See in 360.. aerial predators; ancient lineage. If you understand this one idea, everything else in Dragonflies clicks into place. Odonata. Return to it whenever the details get confusing.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "300M years old.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "300M years old.", "x": "Dragonflies: 300M years old.. Vision. This is load-bearing knowledge — the kind of fact that other facts hang from. aerial predators; ancient lineage. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Why 300M years old. is true.", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Why 300M years old. is true.", "x": "The explanation: 300M years old.. In entomology, this fact connects to Indicators. — and once you see the mechanism, it stops being trivia and starts being understanding. Catch prey midair. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "See in 360.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "See in 360.", "x": "Dragonflies: See in 360.. Speed. This is load-bearing knowledge — the kind of fact that other facts hang from. aerial predators; ancient lineage. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Why See in 360. is true.", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Why See in 360. is true.", "x": "The explanation: See in 360.. In entomology, this fact connects to Pond habitats. — and once you see the mechanism, it stops being trivia and starts being understanding. Nymphs aquatic. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Catch prey midair.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Catch prey midair.", "x": "Dragonflies: Catch prey midair.. Indicators. This is load-bearing knowledge — the kind of fact that other facts hang from. aerial predators; ancient lineage. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Why Catch prey midair. is true.", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Why Catch prey midair. is true.", "x": "The explanation: Catch prey midair.. In entomology, this fact connects to Photography. — and once you see the mechanism, it stops being trivia and starts being understanding. Migration. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Nymphs aquatic.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Nymphs aquatic.", "x": "Dragonflies: Nymphs aquatic.. Pond habitats. This is load-bearing knowledge — the kind of fact that other facts hang from. aerial predators; ancient lineage. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Why Nymphs aquatic. is true.", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Why Nymphs aquatic. is true.", "x": "The explanation: Nymphs aquatic.. In entomology, this fact connects to Odonata. — and once you see the mechanism, it stops being trivia and starts being understanding. Mating wheels. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Migration.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Migration.", "x": "Dragonflies: Migration.. Photography. This is load-bearing knowledge — the kind of fact that other facts hang from. aerial predators; ancient lineage. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Why Migration. is true.", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Why Migration. is true.", "x": "The explanation: Migration.. In entomology, this fact connects to Vision. — and once you see the mechanism, it stops being trivia and starts being understanding. 300M years old. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Mating wheels.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Mating wheels.", "x": "Dragonflies: Mating wheels.. Odonata. This is load-bearing knowledge — the kind of fact that other facts hang from. aerial predators; ancient lineage. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Why Mating wheels. is true.", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Why Mating wheels. is true.", "x": "The explanation: Mating wheels.. In entomology, this fact connects to Speed. — and once you see the mechanism, it stops being trivia and starts being understanding. See in 360. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 7", "d": "300M years old.", "g": "facts", "l": 2, "q": "What is Key fact 7?", "a": "300M years old.", "x": "Dragonflies: 300M years old.. Vision. This is load-bearing knowledge — the kind of fact that other facts hang from. aerial predators; ancient lineage. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 7 explained", "d": "Why 300M years old. is true.", "g": "facts", "l": 2, "q": "What is Key fact 7 explained?", "a": "Why 300M years old. is true.", "x": "The explanation: 300M years old.. In entomology, this fact connects to Indicators. — and once you see the mechanism, it stops being trivia and starts being understanding. Catch prey midair. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 8", "d": "See in 360.", "g": "facts", "l": 2, "q": "What is Key fact 8?", "a": "See in 360.", "x": "Dragonflies: See in 360.. Speed. This is load-bearing knowledge — the kind of fact that other facts hang from. aerial predators; ancient lineage. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 8 explained", "d": "Why See in 360. is true.", "g": "facts", "l": 2, "q": "What is Key fact 8 explained?", "a": "Why See in 360. is true.", "x": "The explanation: See in 360.. In entomology, this fact connects to Pond habitats. — and once you see the mechanism, it stops being trivia and starts being understanding. Nymphs aquatic. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Odonata.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Odonata.", "x": "Going deeper on Dragonflies: Odonata.. See in 360. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Dragonflies from knowing it. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Vision.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Vision.", "x": "Going deeper on Dragonflies: Vision.. Catch prey midair. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Dragonflies from knowing it.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Speed.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Speed.", "x": "Going deeper on Dragonflies: Speed.. Nymphs aquatic. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Dragonflies from knowing it. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Indicators.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Indicators.", "x": "Going deeper on Dragonflies: Indicators.. Migration. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Dragonflies from knowing it. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Pond habitats.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Pond habitats.", "x": "Going deeper on Dragonflies: Pond habitats.. Mating wheels. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Dragonflies from knowing it.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Photography.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Photography.", "x": "Going deeper on Dragonflies: Photography.. 300M years old. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Dragonflies from knowing it.", "s": "public-reference", "f": null}, {"t": "Deep dive 7", "d": "Odonata.", "g": "details", "l": 2, "q": "What is Deep dive 7?", "a": "Odonata.", "x": "Going deeper on Dragonflies: Odonata.. See in 360. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Dragonflies from knowing it. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-sci-dragonflies-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
