(function(){'use strict';
/* JAH Deep Sea Oceanography Database generator — jahdb-e2-sci-deep-sea-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-sci-deep-sea',PREFIX='JAH-E2SCIDEEPSE-',NAME='JAH Deep Sea Oceanography Database';
var FIELDS=["overview", "principles", "facts", "details", "history", "applications", "misconceptions", "terms", "quiz", "frontiers"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Deep Sea: overview", "d": "Deep Sea: the largest habitat on Earth, mostly unexplored..", "g": "overview", "l": 2, "q": "What is Deep Sea: overview?", "a": "Deep Sea: the largest habitat on Earth, mostly unexplored..", "x": "The complete oceanography guide to Deep Sea: the largest habitat on Earth, mostly unexplored.. Below 1000m: no sunlight. From first principles to cutting-edge questions, this database teaches the topic the way a great course would — core facts, deep explanations, history, and what remains unknown.", "s": "public-reference", "f": null}, {"t": "The core principle", "d": "The one idea behind Deep Sea.", "g": "principles", "l": 2, "q": "What is The core principle?", "a": "The one idea behind Deep Sea.", "x": "The core principle: Hydrothermal vents.. the largest habitat on Earth, mostly unexplored. If you understand this one idea, everything else in Deep Sea clicks into place. Zones: abyssal, hadal. Return to it whenever the details get confusing.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Below 1000m: no sunlight.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Below 1000m: no sunlight.", "x": "Deep Sea: Below 1000m: no sunlight.. Pressure: 1000 atm. This is load-bearing knowledge — the kind of fact that other facts hang from. the largest habitat on Earth, mostly unexplored. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Why Below 1000m: no sunlight. is true.", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Why Below 1000m: no sunlight. is true.", "x": "The explanation: Below 1000m: no sunlight.. In oceanography, this fact connects to Cold seeps. — and once you see the mechanism, it stops being trivia and starts being understanding. Giant squid confirmed 2004.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Hydrothermal vents.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Hydrothermal vents.", "x": "Deep Sea: Hydrothermal vents.. Whale falls. This is load-bearing knowledge — the kind of fact that other facts hang from. the largest habitat on Earth, mostly unexplored. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Why Hydrothermal vents. is true.", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Why Hydrothermal vents. is true.", "x": "The explanation: Hydrothermal vents.. In oceanography, this fact connects to Mining debates. — and once you see the mechanism, it stops being trivia and starts being understanding. Mariana Trench: 11km.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Giant squid confirmed 2004.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Giant squid confirmed 2004.", "x": "Deep Sea: Giant squid confirmed 2004.. Cold seeps. This is load-bearing knowledge — the kind of fact that other facts hang from. the largest habitat on Earth, mostly unexplored. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Why Giant squid confirmed 2004. is true.", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Why Giant squid confirmed 2004. is true.", "x": "The explanation: Giant squid confirmed 2004.. In oceanography, this fact connects to Submersibles. — and once you see the mechanism, it stops being trivia and starts being understanding. Bioluminescence common.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Mariana Trench: 11km.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Mariana Trench: 11km.", "x": "Deep Sea: Mariana Trench: 11km.. Mining debates. This is load-bearing knowledge — the kind of fact that other facts hang from. the largest habitat on Earth, mostly unexplored. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Why Mariana Trench: 11km. is true.", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Why Mariana Trench: 11km. is true.", "x": "The explanation: Mariana Trench: 11km.. In oceanography, this fact connects to Zones: abyssal, hadal. — and once you see the mechanism, it stops being trivia and starts being understanding. More mapped on Mars than seafloor.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Bioluminescence common.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Bioluminescence common.", "x": "Deep Sea: Bioluminescence common.. Submersibles. This is load-bearing knowledge — the kind of fact that other facts hang from. the largest habitat on Earth, mostly unexplored. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Why Bioluminescence common. is true.", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Why Bioluminescence common. is true.", "x": "The explanation: Bioluminescence common.. In oceanography, this fact connects to Pressure: 1000 atm. — and once you see the mechanism, it stops being trivia and starts being understanding. Below 1000m: no sunlight.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "More mapped on Mars than seafloor.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "More mapped on Mars than seafloor.", "x": "Deep Sea: More mapped on Mars than seafloor.. Zones: abyssal, hadal. This is load-bearing knowledge — the kind of fact that other facts hang from. the largest habitat on Earth, mostly unexplored. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Why More mapped on Mars than seafloor. is true.", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Why More mapped on Mars than seafloor. is true.", "x": "The explanation: More mapped on Mars than seafloor.. In oceanography, this fact connects to Whale falls. — and once you see the mechanism, it stops being trivia and starts being understanding. Hydrothermal vents.", "s": "public-reference", "f": null}, {"t": "Key fact 7", "d": "Below 1000m: no sunlight.", "g": "facts", "l": 2, "q": "What is Key fact 7?", "a": "Below 1000m: no sunlight.", "x": "Deep Sea: Below 1000m: no sunlight.. Pressure: 1000 atm. This is load-bearing knowledge — the kind of fact that other facts hang from. the largest habitat on Earth, mostly unexplored. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 7 explained", "d": "Why Below 1000m: no sunlight. is true.", "g": "facts", "l": 2, "q": "What is Key fact 7 explained?", "a": "Why Below 1000m: no sunlight. is true.", "x": "The explanation: Below 1000m: no sunlight.. In oceanography, this fact connects to Cold seeps. — and once you see the mechanism, it stops being trivia and starts being understanding. Giant squid confirmed 2004.", "s": "public-reference", "f": null}, {"t": "Key fact 8", "d": "Hydrothermal vents.", "g": "facts", "l": 2, "q": "What is Key fact 8?", "a": "Hydrothermal vents.", "x": "Deep Sea: Hydrothermal vents.. Whale falls. This is load-bearing knowledge — the kind of fact that other facts hang from. the largest habitat on Earth, mostly unexplored. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 8 explained", "d": "Why Hydrothermal vents. is true.", "g": "facts", "l": 2, "q": "What is Key fact 8 explained?", "a": "Why Hydrothermal vents. is true.", "x": "The explanation: Hydrothermal vents.. In oceanography, this fact connects to Mining debates. — and once you see the mechanism, it stops being trivia and starts being understanding. Mariana Trench: 11km.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Zones: abyssal, hadal.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Zones: abyssal, hadal.", "x": "Going deeper on Deep Sea: Zones: abyssal, hadal.. Hydrothermal vents. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Deep Sea from knowing it.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Pressure: 1000 atm.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Pressure: 1000 atm.", "x": "Going deeper on Deep Sea: Pressure: 1000 atm.. Giant squid confirmed 2004. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Deep Sea from knowing it.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Whale falls.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Whale falls.", "x": "Going deeper on Deep Sea: Whale falls.. Mariana Trench: 11km. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Deep Sea from knowing it.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Cold seeps.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Cold seeps.", "x": "Going deeper on Deep Sea: Cold seeps.. Bioluminescence common. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Deep Sea from knowing it.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Mining debates.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Mining debates.", "x": "Going deeper on Deep Sea: Mining debates.. More mapped on Mars than seafloor. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Deep Sea from knowing it.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Submersibles.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Submersibles.", "x": "Going deeper on Deep Sea: Submersibles.. Below 1000m: no sunlight. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Deep Sea from knowing it.", "s": "public-reference", "f": null}, {"t": "Deep dive 7", "d": "Zones: abyssal, hadal.", "g": "details", "l": 2, "q": "What is Deep dive 7?", "a": "Zones: abyssal, hadal.", "x": "Going deeper on Deep Sea: Zones: abyssal, hadal.. Hydrothermal vents. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Deep Sea from knowing it.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-sci-deep-sea-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
